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
from axclite.axclite_msys import AxcliteMSys, AXCL_LITE_VENC
from axclite.axclite_venc import AxcliteVenc
from axclite.axclite_pool import AxclitePool
from axclite.axclite_observer import AxcliteObserver
from axclite.axclite_file import AxcliteStoreFileFromDevice


class VencObserver(AxcliteObserver):
    def __init__(self, dump_path, dump_file):
        self.seq_num = 0
        self.dump_path = dump_path
        self.dump_file = dump_file

    def update(self, data):
        self.seq_num += 1
        pack = data['pack']
        # print(f"seq_num {pack['seq_num']:05d}: len: {pack['len']}, type: {pack['type']}, pts: {pack['pts']}, phy_addr: 0x{pack['phy_addr']:x}")

        if self.dump_file:
            AxcliteStoreFileFromDevice(pack['phy_addr'], pack['len'], self.dump_path, self.dump_file, False if self.seq_num == 1 else True)


def main(device: int, image_file: str, codec: str, width: int, height: int, fps: int, dump: int):
    if not os.path.exists(image_file):
        print(f"device {device:02x}: {image_file} not exist")
        return

    size = int(width * height * 1.5)
    image_num = os.path.getsize(image_file) // size
    if image_num < 1:
        print(f"device {device:02x}: no image in {image_file}")
        return

    dump_path = "/tmp/axcl"
    dump_file = "dump_encoded.{}".format(codec)
    observer = VencObserver(dump_path, dump_file)
    encoder = AxcliteVenc()
    encoder.register_observer(observer)
    attr = {
        'venc_attr': {
            'link_mode': axcl.AX_VENC_UNLINK_MODE,
            'type': axcl.PT_H264 if codec == 'h264' else axcl.PT_H265,
            'pic_width_src': width,
            'pic_height_src': height,
            'profile': axcl.AX_VENC_H264_MAIN_PROFILE if codec == 'h264' else axcl.AX_VENC_HEVC_MAIN_PROFILE,
            'level': axcl.AX_VENC_H264_LEVEL_5_1 if codec == 'h264' else axcl.AX_VENC_HEVC_LEVEL_5_1,
            'tier': axcl.AX_VENC_HEVC_MAIN_TIER,
            'in_fifo_depth': 4,
            'out_fifo_depth': 4,
            'flag': 0
        },
        'rc_attr': {
            'rc_mode': axcl.AX_VENC_RC_MODE_H264CBR if codec == 'h264' else axcl.AX_VENC_RC_MODE_H265CBR,
            'first_frame_start_qp': -1,
            'frame_rate': {
                'src_frame_rate': fps,
                'dst_frame_rate': fps
            },
            'h264_cbr_rc_attr': {
                'gop': fps * 2,
                'stat_time': 0,
                'bitrate': 4096,
                'max_qp': 51,
                'min_qp': 10,
                'max_iqp': 51,
                'min_iqp': 10,
                'max_iprop': 40,
                'min_iprop': 10,
                'intra_qp_delta': -2,
                'idr_qp_delta_range': 0
            },
            'h265_cbr_rc_attr': {
                'gop': fps * 2,
                'stat_time': 0,
                'bitrate': 4096,
                'max_qp': 51,
                'min_qp': 10,
                'max_iqp': 51,
                'min_iqp': 10,
                'max_iprop': 40,
                'min_iprop': 10,
                'intra_qp_delta': -2,
                'idr_qp_delta_range': 0
            }
        },
        'gop_attr': {
            'gop_mode': axcl.AX_VENC_GOPMODE_NORMALP
        }
    }

    # create video encoder
    if axcl.AXCL_SUCC != encoder.create(attr, device):
        return

    # create device pool to hold nv12 yuv image
    pool = AxclitePool()
    if axcl.AX_INVALID_POOLID == pool.create(size, 8, 'nv12'):
        encoder.destroy()
        return

    # start video encoder
    if axcl.AXCL_SUCC != encoder.start():
        pool.destroy()
        encoder.destroy()
        return

    with open(image_file, 'rb') as f:
        seq_num = 0
        while True:
            # read one image from input file
            img = f.read(size)
            if not img:
                break
            else:
                seq_num += 1

                # try to get one free vb block from device to hold loaded yuv image
                while True:
                    blk_id = pool.get_blk()
                    if blk_id != axcl.AX_INVALID_BLOCKID:
                        break
                    else:
                        time.sleep(0.1)

                # transfer yuv image to device by invoke axcl.rt.memcpy from host to device
                phy_addr = pool.get_blk_phy_addr(blk_id)
                axcl.rt.memcpy(phy_addr, axcl.utils.bytes_to_ptr(img), size, axcl.AXCL_MEMCPY_HOST_TO_DEVICE)

                # send yuv image to video encoder
                frame = {
                    'video_frame': {
                        'width': width, 'height': height, 'img_format': axcl.AX_FORMAT_YUV420_SEMIPLANAR,
                        'compress_info': {'compress_mode': axcl.AX_COMPRESS_MODE_NONE, 'compress_level': 0},
                        'pic_stride': [width, width, 0], 'phy_addr': [phy_addr, 0, 0], 'vir_addr': [0, 0, 0],
                        'blk_id': [blk_id, 0, 0], 'seq_num': seq_num, 'frame_size': size
                    },
                    'mod_id': axcl.AX_ID_VENC,
                    'is_end_of_stream': False
                }
                encoder.send_frame(frame, -1)

                pool.release_blk(blk_id)

    time.sleep(2)
    encoder.stop()
    encoder.destroy()
    pool.destroy()

    if dump:
        print(f"device {device:02x}: {os.path.join(dump_path, dump_file)} is saved")


if __name__ == '__main__':
    print(f"============== sample venc started ==============")

    parser = argparse.ArgumentParser(
        description='encode sample: encode input nv12.yuv images to h264/h265 stream',
        epilog=f'eg: {os.path.basename(__file__)} -i input.nv12.yuv --width 1920 --height 1080 h264 --fps 30 --dump 1'
    )
    parser.add_argument('-i', '--input', type=str, required=True, help='input nv12 yuv file')
    parser.add_argument('--width', type=int, required=True, help='width')
    parser.add_argument('--height', type=int, required=True, help='height')
    parser.add_argument('codec', choices=['h264', 'h265'], help='choose codec: h264, h265')
    parser.add_argument('--fps', type=int, default=30)
    parser.add_argument('--dump', type=int, default=0, help='dump encoded NAL stream, 0: no dump 1: dump')
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

    if width % 16 != 0 or height % 2 != 0:
        print(f'width {width} must be aligned to 16, and height {height} must be aligned to 2')
        sys.exit(1)

    try:
        with axclite_system(json):
            # create device
            device = AxcliteDevice(device_id)
            if device.create():
                # initialize video decoder and sys module
                ret = AxcliteMSys().init(AXCL_LITE_VENC)
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

    print("============== sample venc exited ==============")
