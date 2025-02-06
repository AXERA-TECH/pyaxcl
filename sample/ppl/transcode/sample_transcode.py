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
from axclite.axclite_msys import AxcliteMSys, AXCL_LITE_VDEC, AXCL_LITE_VENC, AXCL_LITE_IVPS
from axclite.axclite_vdec import AxcliteVdec
from axclite.axclite_venc import AxcliteVenc
from axclite.axclite_ivps import AxcliteIvps
from axclite.axclite_utils import axclite_align_up
from axclite.axclite_observer import AxcliteObserver
from axclite.axclite_file import AxcliteStoreFileFromDevice
from vdec.simple_annexb_split import SimpleAnnexbSplit
from axclite.axclite_resource import axclite_resource_manager


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


def create_vdec_instance(device: int, codec: str, width: int, height: int) -> object:
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
            {
                'enable': True,     # PP1 supports scale down, max output size is 4096x4096
                'link': True,       # link to next module (IVPS or VENC)
                'pic_width': width, 'pic_height': height,
                'compress_info': {
                    'compress_mode': axcl.AX_COMPRESS_MODE_LOSSY,  # enable FBC to save DDR bandwidth
                    'compress_level': 4
                },
                'output_fifo_depth': 4,
                'frame_buf_cnt': 8,
                'recv_frame_timeout': 1000
            },
            {'enable': False}
        ]
    }

    obj = AxcliteVdec()
    if obj.create(attr, device) != axcl.AXCL_SUCC:
        return None

    return obj


def create_venc_instance(device: int, codec: str, width: int, height: int, fps: int) -> object:
    attr = {
        'venc_attr': {
            'link_mode': axcl.AX_VENC_LINK_MODE,
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
                'idr_qp_delta_range': 0,
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

    obj = AxcliteVenc()
    if obj.create(attr, device) != axcl.AXCL_SUCC:
        return None

    return obj


def create_ivps_instance(device: int, width: int, height: int) -> object:
    attr = {
        'grp_attr': {
            'in_fifo_depth': 4
        },
        'filters': [{
            'engaged': True,
            'link': True,
            'out_fifo_depth': 4,
            'engine': axcl.AX_IVPS_ENGINE_VPP,
            'dst_pic_width': width,
            'dst_pic_height': height,
            'dst_pic_stride': axclite_align_up(width, 256),  # VENC FBC stride should be aligned to 256
            'dst_pic_format': axcl.AX_FORMAT_YUV420_SEMIPLANAR,
            'compression_info': {
                'compress_mode': axcl.AX_COMPRESS_MODE_LOSSY,
                'compress_level': 4
            },
            'frame_buf_num': 4
        }]
    }

    obj = AxcliteIvps()
    if obj.create(attr, device) != axcl.AXCL_SUCC:
        return None

    return obj


def main(device: int, input_file: str, codec: str, width: int, height: int, fps: int, dump: int):
    streamer = SimpleAnnexbSplit(device)
    if not streamer.open(input_file, codec, fps):
        return

    # create video decoder object
    vdec = create_vdec_instance(device, codec, width, height)
    axclite_resource_manager.register(vdec)

    # create video encoder object
    venc = create_venc_instance(device, 'h265', width, height, fps)
    axclite_resource_manager.register(venc)
    dump_path = "/tmp/axcl"
    dump_file = "dump_transcode.{}".format('h265')
    venc.register_observer(VencObserver(dump_path if dump else None, dump_file if dump else None))

    """
        The decoder only supports downscaling by chn1 or chn2 and cannot scale up. 
        Therefore, if upscaling is required for the output, IVPS is needed; otherwise, the decoder can directly handle the downscaling. 
        In this example, IVPS is always enabled to demonstrate how it is used.
    """
    ivps = create_ivps_instance(device, width, height)
    axclite_resource_manager.register(ivps)

    # link modules
    AxcliteMSys().link(
        {'mod_id': axcl.AX_ID_VDEC, 'grp_id': vdec.get_grp_id(), 'chn_id': 1},
        {'mod_id': axcl.AX_ID_IVPS, 'grp_id': ivps.get_grp_id(), 'chn_id': 0}
    )
    AxcliteMSys().link(
        {'mod_id': axcl.AX_ID_IVPS, 'grp_id': ivps.get_grp_id(), 'chn_id': 0},
        {'mod_id': axcl.AX_ID_VENC, 'grp_id': 0, 'chn_id':  venc.get_chn_id()}
    )

    def on_recv_nal_frame(seq_num, frame, pts, userdata):
        vdec.send_stream(frame, pts)

    # start all modules
    venc.start()
    ivps.start()
    vdec.start()

    streamer.start(on_recv_nal_frame, None)

    # wait streamer and decoder eof
    streamer.join()
    while True:
        status = vdec.query_status()
        if status:
            if 0 == (status['left_stream_frames'] + status['left_pics'][0] + status['left_pics'][1] + status['left_pics'][2]):
                print(f"device {device:02x}: total recv frames {status['recv_stream_frames']}, decoded {status['decode_stream_frames']}")
                break

        time.sleep(2)

    # unlink all
    AxcliteMSys().unlink_all()

    # stop all modules
    vdec.stop()
    ivps.stop()
    venc.stop()
    streamer.close()

    # destroy all modules
    axclite_resource_manager.destroy()

    if dump:
        print(f"device {device:02x}: {os.path.join(dump_path, dump_file)} is saved")


if __name__ == '__main__':
    print(f"============== sample transcode started ==============")

    parser = argparse.ArgumentParser(
        description='transcode sample: decode -> resize ->  encode',
        epilog=f'eg: {os.path.basename(__file__)} -i input.h264 --width 1920 --height 1080 h264 --fps 30 --dump 1'
    )
    parser.add_argument('-i', '--input', type=str, required=True, help='input raw annexB h264 or h265 stream file')
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

    try:
        with axclite_system(json):
            # create device
            device = AxcliteDevice(device_id)
            if device.create():
                # initialize video decoder, video encoder and ivps
                ret = AxcliteMSys().init(AXCL_LITE_VDEC | AXCL_LITE_VENC | AXCL_LITE_IVPS)
                if ret != axcl.AXCL_SUCC:
                    device.destroy()
                else:
                    # invoke main function
                    main(device.device_id, input_file, codec, width, height, fps, dump)

                    # de-initialize modules
                    AxcliteMSys().deinit()

                    # destroy device
                    device.destroy()
    except:
        print(sys.exc_info())
        print(traceback.format_exc())

    print("============== sample transcode exited ==============")