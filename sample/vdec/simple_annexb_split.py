# !/usr/bin/env python
# -*- coding:utf-8 -*-
# ******************************************************************************
#
#  Copyright (c) 2019-2024 Axera Semiconductor Co., Ltd. All Rights Reserved.
#
#  This source file is the property of Axera Semiconductor Co., Ltd. and
#  may not be copied or distributed in any isomorphic form without the prior
#  written consent of Axera Semiconductor Co., Ltd.
#
# ******************************************************************************
import os
import time
import copy
from queue import Queue
import threading
from axclite.axclite_context import AxcliteContext


def find_start_codes(data):
    start_codes = []

    length = len(data)
    if length <= 4:
        return start_codes

    i = 0
    while i < length - 3:
        if data[i] == 0x00 and data[i + 1] == 0x00:
            if data[i + 2] == 0x01:
                start_codes.append(i)
                i += 3
                continue
            elif data[i + 2] == 0x00 and data[i + 3] == 0x01:
                start_codes.append(i)
                i += 4
                continue
        i += 1

    return start_codes


class SimpleAnnexbSplit(object):
    """
     Simple annexB splitter:
        1. Split NAL units into frames by identifying the start code (00 00 01 or 00 00 00 01).
        2. Combine SPS, PPS, VPS, and IDR frames into a single frame.

        Note:
        1. This is just an example and should not be used in official applications.
           It is recommended to use av (https://pyav.org/) or FFmpeg instead.
        2. For input frame mode, SPS, PPS (or VPS) should be combined with the IDR frame before being sent to the VDEC.
    """
    def __init__(self, device: int):
        self.queue = Queue()
        self.h264 = False
        self.chunk_size = 8192
        self.f = None
        self.split_thread = None
        self.dispatch_thread = None
        self.sps = None
        self.pps = None
        self.vps = None
        self.seq_num = 0
        self.next_tick = 0
        self.interval = 0
        self.pts = 0
        self.callback = None
        self.userdata = None
        self.device = device
        self.stop = True

    def open(self, file_path, codec='h264', fps=30, chunk_size=0x10000):
        """
        :param file_path: raw h264 or h265 stream file in annex B format, such as 00 00 00 01 27 ...
        :param codec: 'h264' or 'h265'
        :param fps: delay 1/fps seconds between two frames to simulate frame control
        :param chunk_size: chunk size to read from file each time
        :return: True success, False failure
        """
        if codec not in ['h264', 'h265']:
            print(f"codec {codec} not support")
            return False

        if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
            print(f"{file_path} not exist or empty file")
            return False

        try:
            self.f = open(file_path, 'rb')
        except Exception as e:
            print(f"open {file_path} fail, {e}")
            return False

        self.h264 = True if codec == 'h264' else False
        self.chunk_size = chunk_size
        self.interval = int(1000000 / fps) if fps > 0 else 0
        return True

    def close(self):
        self.f.close()

    def start(self, callback, userdata):
        self.stop = False
        self.sps = b''
        self.pps = b''
        self.vps = b''
        self.queue.queue.clear()
        self.seq_num = 0
        self.next_tick = 0
        self.callback = callback
        self.userdata = userdata
        self.split_thread = threading.Thread(target=self.split_worker, name='split_annexb')
        self.dispatch_thread = threading.Thread(target=self.dispatch_work, name='disp_annexb')
        self.split_thread.start()
        self.dispatch_thread.start()

    def join(self):
        self.split_thread.join()
        self.dispatch_thread.join()

    def stop(self):
        self.stop = True

    def dispatch_work(self):
        context = AxcliteContext()
        context.create(self.device)

        try:
            while not self.stop:
                seq_num, frame = self.queue.get()
                if frame:
                    self.pts += self.interval
                self.callback(seq_num, frame, self.pts, self.userdata)
                if frame is None:
                    break
        finally:
            context.destroy()
            print(f"device {self.device:02x}: dispatch NAL end")

    def push(self, frame):
        self.seq_num += 1

        if frame:
            self.queue.put((self.seq_num, frame))

            """
            Simulate frame rate control.
            if now is behind than next, sleep(next - now)
            if now is forward  to next, do nothing

            # 1          2          3          4          5          6          7  us
              | interval |
              |----------|----------|----------|----------|----------|----------|
                  ^    next2                 next4              ^                  us
                  ^                                             ^
                 now2                                          now4                us
            """
            if self.interval > 0:
                now = time.monotonic_ns() // 1000
                if self.seq_num == 1:
                    self.next_tick = now + self.interval
                else:
                    if now < self.next_tick:
                        us = self.next_tick - now
                        time.sleep(us / 1000000)
                    '''
                        print(f"seq_num {self.seq_num:05d}: now = {int(now)}, target = {int(self.next_tick)}, sleep = {int(us)}")
                    else:
                        print(f"seq_num {self.seq_num:05d}: now = {int(now)}, target = {int(self.next_tick)}, delay = {int(now - self.next_tick)}")
                    '''
                    self.next_tick += self.interval
        else:
            self.queue.put((self.seq_num, frame))

    def split_worker(self):
        buffer = b''
        while not self.stop:
            chunk = self.f.read(self.chunk_size)
            if not chunk:
                # eof
                if buffer:
                    self.push(buffer)

                # stop dispatcher
                self.push(None)
                print(f"device {self.device:02x}: reach annexB stream eof")
                break

            buffer += chunk

            start_codes = find_start_codes(buffer)
            if len(start_codes) < 2:
                continue

            end = 0
            for i in range(len(start_codes) - 1):
                start = start_codes[i]
                if buffer[start:start + 4] == b'\x00\x00\x00\x01':
                    sc_len = 4
                else:
                    sc_len = 3

                beg = start
                end = start_codes[i + 1]
                nal = buffer[beg:end]
                if len(nal) > 1:
                    self.joint(nal, sc_len)
                else:
                    raise Exception(f"device {self.device:02x}: invalid frame len {len(nal)}")

            buffer = buffer[end:]

    def joint(self, frame, sc_len):
        if self.h264:
            SPS = 7
            PPS = 8
            IDR = 5
        else:
            VPS = 32
            SPS = 33
            PPS = 34
            IDR = 19

        head = frame[sc_len]
        type = (head & 0x1F) if self.h264 else ((head >> 1) & 0x3F)

        if self.h264:
            if type == SPS:
                self.sps = copy.deepcopy(frame)
            elif type == PPS:
                self.pps = copy.deepcopy(frame)
            elif type == IDR:
                # joint SPS, PPS and IDR
                if self.sps and self.pps:
                    joint_frame = self.sps + self.pps + frame
                else:
                    joint_frame = frame

                self.push(joint_frame)
            else:
                self.push(frame)
        else:
            if type == VPS:
                self.vps = copy.deepcopy(frame)
            elif type == SPS:
                self.sps = copy.deepcopy(frame)
            elif type == PPS:
                self.pps = copy.deepcopy(frame)
            elif type == IDR:
                # joint VPS, SPS, PPS and IDR
                if self.vps or self.sps or self.pps:
                    joint_frame = b''
                    if self.vps:
                        joint_frame += self.vps
                    if self.sps:
                        joint_frame += self.sps
                    if self.pps:
                        joint_frame += self.pps
                    joint_frame += frame
                else:
                    joint_frame = frame

                self.push(joint_frame)
            else:
                self.push(frame)


if __name__ == "__main__":
    def on_recv_nal_frame(seq_num, frame, pts, userdata):
        if frame:
            print(f"seq_num {seq_num}: pts {pts}, len {len(frame)}")

    splitter = SimpleAnnexbSplit()
    splitter.open('D:/bangkok_30952_1920x1080_30fps_gop60_4Mbps.h264', 'h264', fps=0)
    splitter.start(on_recv_nal_frame, None)
    splitter.stop()
    splitter.close()
