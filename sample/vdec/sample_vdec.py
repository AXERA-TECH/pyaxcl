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
import argparse
import os
import sys
import time
import traceback

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR + '.')
sys.path.append(BASE_DIR + '/..')
sys.path.append(BASE_DIR + '/../..')

import axcl
from axclite.axclite_device import AxcliteDevice
from axclite.axclite_system import axclite_system
from axclite.axclite_msys import AxcliteMSys, AXCL_LITE_VDEC
from axclite.axclite_vdec import AxcliteVdec
from axclite.axclite_utils import axclite_align_up
from axclite.axclite_observer import AxcliteObserver
from axclite.axclite_file import AxcliteStoreFileFromDevice
from vdec.simple_annexb_split import SimpleAnnexbSplit


class VdecObserver(AxcliteObserver):
    def __init__(self, chn, max_dump_num, dump_path, dump_file):
        self.max_dump_num = max_dump_num
        self.seq_num = 0
        self.chn = chn
        self.dump_path = dump_path
        self.dump_file = dump_file

    def update(self, data):
        self.seq_num += 1
        frame = data['video_frame']
        """
        print(
            f"seq_num {frame['seq_num']:05d}: {frame['width']} x {frame['height']} stride {frame['pic_stride'][0]}, "
            f"size {frame['frame_size']}, phy_addr 0x{frame['phy_addr'][0]:x}, blk 0x{frame['blk_id'][0]:x}"
        )
        """

        if self.max_dump_num < 0 or self.seq_num <= self.max_dump_num:
            AxcliteStoreFileFromDevice(frame['phy_addr'][0], frame['frame_size'], self.dump_path, self.dump_file, False if self.seq_num == 1 else True)


def main(device: int, input_file: str, codec: str, width: int, height: int, fps: int, max_dump_num: int):
    streamer = SimpleAnnexbSplit(device)
    if not streamer.open(input_file, codec, fps):
        return

    decoder = AxcliteVdec()

    attr = {
        'grp_attr': {
            'codec_type': axcl.PT_H264 if codec == 'h264' else axcl.PT_H265,
            'max_pic_width': width,
            'max_pic_height': height,
            'output_order': axcl.AX_VDEC_OUTPUT_ORDER_DEC,
            'display_mode': axcl.AX_VDEC_DISPLAY_MODE_PLAYBACK
        },
        'chn_attr': [
            {'enable': False},
            {'enable': True, 'link': False, 'pic_width': width, 'pic_height': height, 'output_fifo_depth': 4, 'frame_buf_cnt': 8, 'recv_frame_timeout': 1000},
            {'enable': False}
        ]
    }

    # register observer for enabled and unlink channel
    observers = [None for _ in range(axcl.AX_VDEC_MAX_CHN_NUM)]
    dump_path = "/tmp/axcl"
    dump_file = [None for _ in range(axcl.AX_VDEC_MAX_CHN_NUM)]
    for i in range(len(attr['chn_attr'])):
        if attr['chn_attr'][i]['enable'] and not attr['chn_attr'][i]['link']:
            dump_file[i] = "dump_chn{}_decoded_{}x{}.nv12.yuv".format(i, axclite_align_up(width, 256), height)
            observers[i] = VdecObserver(i, max_dump_num, dump_path, dump_file[i])
            decoder.register_observer(i, observers[i])

    # create video decoder
    if decoder.create(attr, device) == axcl.AXCL_SUCC:
        # start video decoder
        decoder.start()

        # start streaming
        def on_recv_nal_frame(seq_num, frame, pts, userdata):
            decoder.send_stream(frame, pts)

        streamer.start(on_recv_nal_frame, None)

        # wait all NALs have been decoded
        streamer.join()
        while True:
            status = decoder.query_status()
            if status:
                if 0 == (status['left_stream_frames'] + status['left_pics'][0] + status['left_pics'][1] + status['left_pics'][2]):
                    print(f"device {device:02x}: total recv frames {status['recv_stream_frames']}, decoded {status['decode_stream_frames']}")
                    break

            time.sleep(2)

        # stop and destroy video decoder
        decoder.stop()
        decoder.destroy()

    for i in range(axcl.AX_VDEC_MAX_CHN_NUM):
        if dump_file[i]:
            print(f"device {device:02x}: {os.path.join(dump_path, dump_file[i])} is saved")

    streamer.close()


if __name__ == '__main__':
    print(f"============== sample vdec started ==============")

    parser = argparse.ArgumentParser(
        description='decode sample: decode h264/h265 raw annexB stream to nv12.yuv images',
        epilog=f'eg: {os.path.basename(__file__)} -i input.h264 --width 1920 --height 1080 h264 --fps 30 --dump 10'
    )
    parser.add_argument('-i', '--input', type=str, required=True, help='input raw annexB h264 or h265 stream file')
    parser.add_argument('--width', type=int, required=True, help='width')
    parser.add_argument('--height', type=int, required=True, help='height')
    parser.add_argument('codec', choices=['h264', 'h265'], help='choose codec: h264, h265')
    parser.add_argument('--fps', type=int, default=30)
    parser.add_argument('--dump', type=int, default=0, help='dump number of decode nv12 image from device. 0: no dump, -1: dump all')
    parser.add_argument('-d', '--device', type=int, default=0, help='device id, 0 means auto select 1 from connected')
    parser.add_argument('--json', type=str, default='/usr/bin/axcl/axcl.json', help='axcl.json path')

    args = parser.parse_args()
    device_id = args.device
    json = args.json
    input_file = args.input
    codec = args.codec
    fps = args.fps
    width = args.width
    height = args.height
    dump = args.dump

    try:
        with axclite_system(json):
            # create device
            device = AxcliteDevice(device_id)
            if device.create():
                # initialize video decoder and sys module
                ret = AxcliteMSys().init(AXCL_LITE_VDEC)
                if ret != axcl.AXCL_SUCC:
                    device.destroy()
                else:
                    # invoke main function
                    main(device.device_id, input_file, codec, width, height, fps, dump)

                    # de-initialize sys and video decoder module
                    AxcliteMSys().deinit()

                    # destroy device
                    device.destroy()
    except:
        print(sys.exc_info())
        print(traceback.format_exc())

    print("============== sample vdec exited ==============")
