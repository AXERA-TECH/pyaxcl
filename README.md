# pyAXCL

[![License](https://img.shields.io/badge/license-BSD--3--Clause-blue.svg)](https://raw.githubusercontent.com/AXERA-TECH/pyaxengine/main/LICENSE)



## Overview

**pyAXCL**基于[AXCL](https://axcl-docs.readthedocs.io/zh-cn/latest/) 驱动上实现的python API，支持M.2算力卡形态。

<img src="https://axcl-docs.readthedocs.io/zh-cn/latest/_images/axcl_architecture.svg" style="zoom:80%;" />

支持芯片：

- AX650N

支持功能：

- NPU推理
- IVE算子
- 多媒体：Codec编解码（H264，H265，JPG）、IVPS图像变换（缩放，颜色空间转换，裁剪等）



## 版本要求

Python >= 3.9 64bit




## 环境搭建
1.  正确[安装AXCL驱动(deb, rpm)](https://axcl-docs.readthedocs.io/zh-cn/latest/doc_guide_setup.html)，执行**axcl-smi**确认设备连接正常。

2.  编译wheel包并安装

   - 编译：`./build.sh`生成的wheel路径：***out**/pyAXCL-x.yy.z-py3-none-any.whl*

   - 安装：

     ```python
     $ pip3 install setuptools wheel

     $ pip3 install pyAXCL-X.YY.Z-py3-none-any.whl
     $ pip3 show pyAXCL

     Python 3.9.5 (default, Mar 14 2023, 08:11:14)
     [GCC 9.4.0] on linux
     Type "help", "copyright", "credits" or "license" for more information.
     >>> import axcl
     >>>
     ```

   - 卸载：

     ```python
     $ pip3 uninstall pyAXCL -y
     ```



## 示例程序

将 [sample](./sample)目录拷贝到开发板或者主控系统中，以下示例的硬件环境为 CentOS9 + M.2计算卡。

### 推理

模型推理示例 [sample_engine.py](./sample/engine/sample_engine.py) ，命令参数说明如下：

| 命令参数       | 参数说明                                           | 必选 |
| -------------- | -------------------------------------------------- | ---- |
| -m, --model    | 模型文件路径                                       | ☑    |
| -v, --vnpu     | VNPU类型，默认0                                    |      |
| -w, --warmup   | 模型warmup次数，默认1                              |      |
| -r, --repeat   | 模型运行次数，默认5                                |      |
| ---d, --device | 选择设备号，可选。不指定则默认选择连接的第一个设备 |      |
| --json         | 指定`axcl.json`配置文件，默认不指定                |      |

```bash
[axera@localhost]$ python sample/engine/sample_engine.py -m yolov5s.axmodel  -r 100
   Run AxModel:
         model: yolov5s.axmodel
        warmup: 1
        repeat: 100
          vnpu: Disable
          type: 1 core
         input:
                [0]: name='images', layout=nhwc, dtype=uint8, dims=[1, 640, 640, 3], size=1228800
        output:
                [0]: name='326', layout=none, dtype=fp32, dims=[1, 80, 80, 255], size=6528000
                [1]: name='370', layout=none, dtype=fp32, dims=[1, 40, 40, 255], size=1632000
                [2]: name='414', layout=none, dtype=fp32, dims=[1, 20, 20, 255], size=408000
  ------------------------------------------------------
  min =   7.879 ms   max =   8.276 ms   avg =   8.184 ms
  ------------------------------------------------------
```



### 解码

[sample_vdec.py](./sample/vdec/sample_vdec.py) 示例程序将H264和H265码流解码输出NV12图片，命令参数说明如下：

| 命令参数      | 参数说明                                                     | 必选 |
| ------------- | ------------------------------------------------------------ | ---- |
| -i, --input   | 仅支持**Annex B**格式H264和H265 **raw**码流，**不支持封装格式，比如mp4等** | ☑    |
| --width       | 输入视频码流的宽度                                           | ☑    |
| --height      | 输入视频码流的高度                                           | ☑    |
| --fps         | 输入视频码流的帧率                                           | ☑    |
| h264, h265    | 码流格式                                                     | ☑    |
| --d, --device | 选择设备号，可选。不指定则默认选择连接的第一个设备           |      |
| --dump        | 将解码后的NV12图片保存到本地。0（默认）: 仅解码不保存，-1: 全部保存， > 0: 指定保存的图片帧数 |      |
| --json        | 指定`axcl.json`配置文件，默认不指定                          |      |

> [!NOTE]
>
> sample_vdec.py不支持mp4等格式解封装，只支持简单的Annex B格式码流的帧边界解析，因此若mp4封装格式，建议用ffmpeg解封装并转成Annex B格式码流，参考如下：
>
> ```bash
> ffmpeg -i input.mp4 -c:v copy -bsf:v h264_mp4toannexb -an output.h264
> ffmpeg -i input.mp4 -c:v copy -bsf:v hevc_mp4toannexb -an output.h265
> ```

**示例** : 解码`bangkok_30952_1920x1080_30fps_gop60_4Mbps.264`并保存前10帧图像。

```bash
[axera@localhost]$ python sample/vdec/sample_vdec.py -i bangkok_30952_1920x1080_30fps_gop60_4Mbps.264 --width 1920 --height 1080 h264 --fps 30 --dump 100
============== sample vdec started ==============
device 05: vdGrp 0 vdChn 0 is disabled
device 05: vdGrp 0 vdChn 1 is enabled
device 05: vdGrp 0 vdChn 2 is disabled
device 05: vdGrp 0 is created
device 05: vdGrp 0 is started
device 05: reach annexB stream eof
device 05: dispatch NAL end
device 05: total recv frames 470, decoded 470
device 05: vdGrp 0 is stopped
device 05: vdGrp 0 is destroyed
device 05: /tmp/axcl/dump_chn1_decoded_2048x1080.nv12.yuv is saved
============== sample vdec exited ==============
```

### 编码

[sample_venc.py](./sample/venc/sample_venc.py) 示例程序将NV12图片编码成码流，命令参数说明如下：

| 命令参数      | 参数说明                                                     | 必选 |
| ------------- | ------------------------------------------------------------ | ---- |
| -i, --input   | 输入待编码的图像文件，该文件包含若干帧相同尺寸的NV12格式图像 | ☑    |
| --width       | 输入图片宽度                                                 | ☑    |
| --height      | 输入图片高度                                                 | ☑    |
| --fps         | 码流帧率                                                     | ☑    |
| h264, h265    | 输出码流格式                                                 | ☑    |
| --d, --device | 选择设备号，可选。不指定则默认选择连接的第一个设备           |      |
| --dump        | 将编码后的码流保存到本地，0（默认）：不保存， 1： 保存       |      |
| --json        | 指定`axcl.json`配置文件，默认不指定                          |      |

**示例** : 将100帧NV12图片编码成H265码流。

```bash
[axera@localhost]$ python sample/venc/sample_venc.py -i /tmp/axcl/dump_chn1_decoded_2048x1080.nv12.yuv --width 2048 --height 1080 --fps 30 h265 --dump 1
============== sample venc started ==============
device 05: set venc buf size to 3317760
device 05: veChn 0 is created
device 05: veChn 0 is started 8
device 05: veChn 0 is stopped
device 05: veChn 0 is destroyed
device 05: /tmp/axcl/dump_encoded.h265 is saved
============== sample venc exited ==============
```

### 转码

[sample_transcode.py](./sample/ppl/transcode/sample_transcode.py) 示例下图转码业务场景：

![](https://axcl-docs.readthedocs.io/zh-cn/latest/_images/transcode_ppl.png)

> [!NOTE]
>
> - sample仅包含解码，缩放和编码流程，不包含拉流和推流；
> - sample编码固定输出和源视频相同宽高的H265码流。

| 命令参数      | 参数说明                                                     | 必选 |
| ------------- | ------------------------------------------------------------ | ---- |
| -i, --input   | 仅支持**Annex B**格式H264和H265 **raw**码流，**不支持封装格式，比如mp4等** | ☑    |
| --width       | 输入视频码流的宽度                                           | ☑    |
| --height      | 输入视频码流的高度                                           | ☑    |
| --fps         | 输入视频码流的帧率                                           | ☑    |
| h264, h265    | 码流格式                                                     | ☑    |
| --d, --device | 选择设备号，可选。不指定则默认选择连接的第一个设备           |      |
| --dump        | 将编码后的码流保存到本地，0（默认）：不保存， 1： 保存       |      |
| --json        | 指定`axcl.json`配置文件，默认不指定                          |      |

**示例** : 解码`bangkok_30952_1920x1080_30fps_gop60_4Mbps.264`转码输出1920x1080@30fps H265码流。

```bash
[axera@localhost]$ python sample/ppl/transcode/sample_transcode.py -i ./bangkok_30952_1920x1080_30fps_gop60_4Mbps.264 --width 1920 --height 1080 h264 --fps 30 --dump 1
============== sample transcode started ==============
device 05: vdGrp 0 vdChn 0 is disabled
device 05: vdGrp 0 vdChn 1 is enabled
device 05: vdGrp 0 vdChn 2 is disabled
device 05: vdGrp 0 is created
device 05: set venc buf size to 3110400
device 05: veChn 0 is created
device 05: ivGrp 0 is created
device 05: veChn 0 is started
device 05: ivGrp 0 is started
device 05: vdGrp 0 is started
device 05: reach annexB stream eof
device 05: dispatch NAL end
device 05: total recv frames 470, decoded 470
device 05: vdGrp 0 is stopped
device 05: ivGrp 0 is stopped
device 05: veChn 0 is stopped
device 05: ivGrp 0 is destroyed
device 05: veChn 0 is destroyed
device 05: vdGrp 0 is destroyed
device 05: /tmp/axcl/dump_transcode.h265 is saved
```



### IVPS

[sample_ivps.py](./sample/sample_ivps.py) 示例对单帧图像进行裁剪缩放和颜色空间转换功能。

| 命令参数       | 参数说明                                                     | 必选 |
| -------------- | ------------------------------------------------------------ | ---- |
| -i, --input    | 输入NV12单帧图像                                             | ☑    |
| -c, --case     | 功能选项：`crop_resize` 或 `csc`                             | ☑    |
| --width        | 输入图像宽度                                                 | ☑    |
| --height       | 输入图像高度                                                 | ☑    |
| -s, --src_type | 输入图像格式，可选项：nv12/nv21/rgb888/bgr888/rgb565/argb8888/rgba8888， 默认nv12 |      |
| -t, --dst_type | 输出图像格式，可选项：nv12/nv21/rgb888/bgr888/rgb565/argb8888/rgba8888， 默认nv12 |      |
| -e, --engine   | 指定硬件引擎，可选项：vgp/vpp/tdp， 默认vgp                  |      |
| -v, --version  | 指定接口版本，可选项：1/2/3/4， 默认1                        |      |
| -o, --output   | 输出图像路径，默认：*/tmp/axcl/data/output*                  |      |
| --d, --device  | 选择设备号，可选。不指定则默认选择连接的第一个设备           |      |
| --json         | 指定`axcl.json`配置文件，默认不指定                          |      |

#### 示例1 - 裁剪缩放

```
[axera@localhost]$ python sample/ivps/sample_ivps.py -i ./1920x1080.nv12.yuv -c crop_resize --width 1920 --height 1080 -e vgp -v 1
============== sample ivps started ==============
cmd args: device id=0, json=/usr/bin/axcl/axcl.json
crop_resize_vgp operation completed successfully
store file '/tmp/axcl/data/output/crop_resize_vgp_output_image_960x540.nv12' successfully.
============== sample ivps exited ==============
```

#### 示例2 - NV12转换成RGB888

```
[axera@localhost]$ python sample/ivps/sample_ivps.py -i ./1920x1080.nv12.yuv -c csc --width 1920 --height 1080 -e vgp --src_type nv12 --dst_type bgr888
============== sample ivps started ==============
cmd args: device id=0, json=/usr/bin/axcl/axcl.json
csc_vgp operation completed successfully
store file '/tmp/axcl/data/output/csc_vgp_output_image_1920x1080.bgr888' successfully.
```

> [!NOTE]
>
> IVPS硬件RGB的字节序定义参考SDK的头文件`ax_global_type.h`说明，若输出RGB图像，--dst_type配置bgr888
>
> ```c
> AX_FORMAT_RGB888                                = 0xA1,      /* BGRBGR..., RGB888 24bpp */
> AX_FORMAT_BGR888                                = 0xA5,      /* RGBRGB..., BGR888 32bpp */
> ```



### IVE

[sample_ive.py](./sample/ive/sample_ive.py) 示例部分IVE算子：

- dma：DMA拷贝实现灰度图的拷贝
- filter:   滤波
- gmm2：背景建模，输出前景和背景图像
- cropresize：对输入图像裁剪放大

#### 示例1 - DMA实现灰度图拷贝

```bash
[axera@localhost]$ python sample/ive/sample_ive.py -c 0 -i ./1280x720_u8c1_gray.yuv --width 1280 --height 720
============== sample ive started ==============
cmd args: device id=0, json=/usr/bin/axcl/axcl.json
dma operation completed successfully.
return handle: 1
dst: {'phy_addr': 5523177472, 'vir_addr': 0, 'stride': 1280, 'width': 1280, 'height': 720, 'reserved': 0}
store file '/tmp/axcl/data/output/out_dma_1280x720_u8c1_gray.yuv' successfully.
============== sample ive exited ==============
```

#### 示例2 - 灰度图滤波

```bash
[axera@localhost]$ python sample/ive/sample_ive.py -c 1 -i ./1280x720_u8c1_gray.yuv --width 1280 --height 720
============== sample ive started ==============
cmd args: device id=0, json=/usr/bin/axcl/axcl.json
dma operation completed successfully.
return handle: 1
dst: {'phy_addr': [5523177472, 0, 0], 'vir_addr': [0, 0, 0], 'stride': [1280, 1280, 0], 'width': 1280, 'height': 720, 'type': 0}
store file '/tmp/axcl/data/output/out_filter_1280x720_u8c1_gray.yuv' successfully.
============== sample ive exited ==============
```

#### 示例3 - GMM2背景建模

```
[axera@localhost]$ python sample/ive/sample_ive.py -c 2 -i ./1280x720_u8c1_gray.yuv --width 1280 --height 720 --model ./gmm_gray_1280x720_model.bin
============== sample ive started ==============
cmd args: device id=0, json=/usr/bin/axcl/axcl.json
dma operation completed successfully.
return handle: 1
dst_fg: {'phy_addr': [5567414272, 0, 0], 'vir_addr': [0, 0, 0], 'stride': [1280, 1280, 0], 'width': 1280, 'height': 720, 'type': 0}
dst_bg: {'phy_addr': [5568335872, 0, 0], 'vir_addr': [0, 0, 0], 'stride': [1280, 1280, 0], 'width': 1280, 'height': 720, 'type': 0}
store file '/tmp/axcl/data/output/out_gmm2_fg_1280x720_u8c1_gray.yuv' successfully.
store file '/tmp/axcl/data/output/out_gmm2_bg_1280x720_u8c1_gray.yuv' successfully.
============== sample ive exited ==============
```

#### 示例4 - NV12图像裁剪[0, 0, 640, 360]区域并放大

```bash
[axera@localhost]$ python sample/ive/sample_ive.py -c 3 -e 2 -t 3 -i ./1280x720_nv12.yuv --width 1280 --height 720
============== sample ive started ==============
cmd args: device id=0, json=/usr/bin/axcl/axcl.json
dma operation completed successfully.
return handle: 65535
dst: [{'phy_addr': [5523640320, 0, 0], 'vir_addr': [0, 0, 0], 'stride': [1280, 1280, 0], 'width': 1280, 'height': 720, 'glb_type': 3}]
store file '/tmp/axcl/data/output/out_crop_resize_1280x720_nv12.yuv' successfully.
============== sample ive exited ==============
```



### DMA

[sample_dmadim.py](./sample/dmadim/sample_dmadim.py) 示例如下子功能：

- copy：设备侧4M物理内存拷贝
- memset：将设备侧4M内存初始化为0xAA
- checksum：计算checksum
- crop：使用DMA 2D拷贝功能实现裁剪NV12图像的[x = 0, y = 0, w = 1/2, h = 1/2] 区域

| 命令参数      | 参数说明                                            | 必选 |
| ------------- | --------------------------------------------------- | ---- |
| -i, --input   | 输入1帧 NV12图像                                    | ☑    |
| --width       | NV12图像宽度                                        | ☑    |
| --height      | NV12图像高度                                        | ☑    |
| -o, --output  | 指定裁剪图像保存路径，默认：*/tmp/axcl/data/output* |      |
| --d, --device | 选择设备号，可选。不指定则默认选择连接的第一个设备  |      |
| --json        | 指定`axcl.json`配置文件，默认不指定                 |      |

**示例：**

```bash
[axera@localhost]$ python sample/dmadim/sample_dmadim.py -i 1920x1080.nv12.yuv --width 1920 --height 1080
============== sample dmadim started ==============
cmd args: device id=0, json=/usr/bin/axcl/axcl.json
memory [0]: device 0x14926f000
memory [1]: device 0x14966f000
dma_copy: compare dev memory[0] 0x14926f000 and dev memory[1] 0x14966f000 successfully
memory : device 0x14926f000
dma_memset: memset 0x14926f000 operation completed successfully.
memory : device 0x14926f000
dma_checksum: checksum: 0xaaa00000 successfully
dma_copy2d: mem_copy_xd operation completed successfully
store file '/tmp/axcl/data/output/dma2d_output_image_960x540.nv12' successfully.
============== sample dmadim exited ==============
```



## 关联项目

- [axcl](https://axcl-docs.readthedocs.io/zh-cn/latest/)



## 技术讨论

- [issue](https://github.com/AXERA-TECH/pyaxcl/issues)
- QQ 群: 139953715
