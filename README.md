# pyAXCL

[![License](https://img.shields.io/badge/license-BSD--3--Clause-blue.svg)](https://raw.githubusercontent.com/AXERA-TECH/pyaxengine/main/LICENSE)



## Overview

**pyAXCL**基于[AXCL](https://axcl-docs.readthedocs.io/zh-cn/latest/) 驱动上实现的  Python API，支持开发板和M.2算力卡形态。

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

模型推理示例 sample_engine.py ，命令参数说明如下：

| 命令参数       | 参数说明                                           | 是否强制 |
| -------------- | -------------------------------------------------- | -------- |
| -m, --model    | 模型文件路径                                       | ☑        |
| -v, --vnpu     | VNPU类型，默认0                                    |          |
| -w, --warmup   | 模型warmup次数，默认1                              |          |
| -r, --repeat   | 模型运行次数，默认5                                |          |
| ---d, --device | 选择设备号，可选。不指定则默认选择连接的第一个设备 |          |
| --json         | 指定`axcl.json`配置文件，默认不指定                |          |

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

sample_vdec.py 示例程序将H264和H265码流解码输出NV12图片，命令参数说明如下：

| 命令参数      | 参数说明                                                     | 是否强制 |
| ------------- | ------------------------------------------------------------ | -------- |
| -i, --input   | 仅支持AnnexB格式H264和H265 raw码流，**不支持封装格式，比如mp4等** | ☑        |
| --width       | 输入视频码流的宽度                                           | ☑        |
| --height      | 输入视频码流的高度                                           | ☑        |
| --fps         | 输入视频码流的帧率                                           | ☑        |
| h264, h265    | 码流格式                                                     | ☑        |
| --d, --device | 选择设备号，可选。不指定则默认选择连接的第一个设备           |          |
| --dump        | 将解码后的NV12图片保存到本地。0（默认）: 仅解码不保存，-1: 全部保存， > 0: 指定保存的图片帧数 |          |
| --json        | 指定`axcl.json`配置文件，默认不指定                          |          |

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

sample_venc.py 示例程序将NV12图片编码成码流，命令参数说明如下：

| 命令参数      | 参数说明                                               | 是否强制 |
| ------------- | ------------------------------------------------------ | -------- |
| -i, --input   | 输入待编码的NV12图片                                   | ☑        |
| --width       | 输入图片宽度                                           | ☑        |
| --height      | 输入图片高度                                           | ☑        |
| --fps         | 码流帧率                                               | ☑        |
| h264, h265    | 输出码流格式                                           | ☑        |
| --d, --device | 选择设备号，可选。不指定则默认选择连接的第一个设备     |          |
| --dump        | 将编码后的码流保存到本地，0（默认）：不保存， 1： 保存 |          |
| --json        | 指定`axcl.json`配置文件，默认不指定                    |          |

**示例** : 将100帧NV12图片编码成H265码流。

```bash
[axera@localhost]$ python sample/venc/sample_venc.py -i /tmp/axcl/dump_chn1_decoded_2048x1080.nv12.yuv --width 2048 --height 1080 --fps 30 h265 --dump 1
============== sample venc started ==============
device 05: set venc buf size to 3317760
device 05: veChn 0 is created
device 05: veChn 0 is started
device 05: veChn 0 is stopped
device 05: veChn 0 is destroyed
device 05: /tmp/axcl/dump_encoded.h265 is saved
============== sample venc exited ==============
```



## 关联项目

- [axcl](https://axcl-docs.readthedocs.io/zh-cn/latest/)



## 技术讨论

- [github issue](https://github.com/AXERA-TECH/pyaxcl/issues)
- QQ 群: 139953715
