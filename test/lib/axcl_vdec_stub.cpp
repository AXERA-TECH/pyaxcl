/**************************************************************************************************
 *
 * Copyright (c) 2019-2024 Axera Semiconductor Co., Ltd. All Rights Reserved.
 *
 * This source file is the property of Axera Semiconductor Co., Ltd. and
 * may not be copied or distributed in any isomorphic form without the prior
 * written consent of Axera Semiconductor Co., Ltd.
 *
 **************************************************************************************************/

#include <string.h>
#include "axcl_vdec.h"
#include "randomizer.hpp"
#include "serializer.hpp"

#define IMPLEMENT_SERIALIZE(...)                       \
    do {                                               \
        SERILAIZER()->input()->serialize(__VA_ARGS__); \
        AX_S32 ret = initialize_random<AX_S32>();      \
        SERILAIZER()->output()->serialize(ret);        \
        return ret;                                    \
    } while (0)

AXCL_EXPORT AX_S32 AXCL_VDEC_Init(const AX_VDEC_MOD_ATTR_T *pstModAttr) {
    IMPLEMENT_SERIALIZE(pstModAttr);
}

AXCL_EXPORT AX_S32 AXCL_VDEC_Deinit(AX_VOID) {
    IMPLEMENT_SERIALIZE();
}

AXCL_EXPORT AX_S32 AXCL_VDEC_ExtractStreamHeaderInfo(const AX_VDEC_STREAM_T *pstStreamBuf, AX_PAYLOAD_TYPE_E enVideoType,
                                                     AX_VDEC_BITSTREAM_INFO_T *pstBitStreamInfo) {
    SERILAIZER()->input()->serialize(pstStreamBuf, enVideoType);

    memset(pstBitStreamInfo, 0, sizeof(*pstBitStreamInfo));
    pstBitStreamInfo->u32Width = initialize_random<AX_U32>();
    pstBitStreamInfo->u32Height = initialize_random<AX_U32>();
    pstBitStreamInfo->u32RefFramesNum = initialize_random<AX_U32>();
    pstBitStreamInfo->u32BitDepthY = initialize_random<AX_U32>();
    pstBitStreamInfo->u32BitDepthC = initialize_random<AX_U32>();
    AX_S32 ret = 0;
    SERILAIZER()->output()->serialize(ret, pstBitStreamInfo);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_VDEC_CreateGrp(AX_VDEC_GRP VdGrp, const AX_VDEC_GRP_ATTR_T *pstGrpAttr) {
    IMPLEMENT_SERIALIZE(VdGrp, pstGrpAttr);
}

AXCL_EXPORT AX_S32 AXCL_VDEC_CreateGrpEx(AX_VDEC_GRP *VdGrp, const AX_VDEC_GRP_ATTR_T *pstGrpAttr) {
    SERILAIZER()->input()->serialize(pstGrpAttr);

    *VdGrp = initialize_random<AX_VDEC_GRP>();
    AX_S32 ret = 0;
    SERILAIZER()->output()->serialize(ret, *VdGrp);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_VDEC_DestroyGrp(AX_VDEC_GRP VdGrp) {
    IMPLEMENT_SERIALIZE(VdGrp);
}

AXCL_EXPORT AX_S32 AXCL_VDEC_GetGrpAttr(AX_VDEC_GRP VdGrp, AX_VDEC_GRP_ATTR_T *pstGrpAttr) {
    SERILAIZER()->input()->serialize(VdGrp);

    memset(pstGrpAttr, 0, sizeof(*pstGrpAttr));
    pstGrpAttr->enCodecType = create_enum_random_instance<AX_PAYLOAD_TYPE_E>(PT_PCMU, PT_BUTT);
    pstGrpAttr->enInputMode = create_enum_random_instance<AX_VDEC_INPUT_MODE_E>(AX_VDEC_INPUT_MODE_NAL, AX_VDEC_INPUT_MODE_BUTT);
    pstGrpAttr->u32MaxPicWidth = initialize_random<AX_U32>();
    pstGrpAttr->u32MaxPicHeight = initialize_random<AX_U32>();
    pstGrpAttr->u32StreamBufSize = initialize_random<AX_U32>();
    pstGrpAttr->bSdkAutoFramePool = initialize_random<AX_BOOL>();
    pstGrpAttr->bSkipSdkStreamPool = initialize_random<AX_BOOL>();
    pstGrpAttr->stStreamBufAddr.u64PhyAddr = initialize_random<AX_U64>();
    pstGrpAttr->stStreamBufAddr.pVirAddr = reinterpret_cast<AX_VOID *>(initialize_random<AX_U64>());
    AX_S32 ret = 0;
    SERILAIZER()->output()->serialize(ret, *pstGrpAttr);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_VDEC_SetGrpAttr(AX_VDEC_GRP VdGrp, const AX_VDEC_GRP_ATTR_T *pstGrpAttr) {
    IMPLEMENT_SERIALIZE(VdGrp, pstGrpAttr);
}

AXCL_EXPORT AX_S32 AXCL_VDEC_StartRecvStream(AX_VDEC_GRP VdGrp, const AX_VDEC_RECV_PIC_PARAM_T *pstRecvParam) {
    IMPLEMENT_SERIALIZE(VdGrp, pstRecvParam);
}

AXCL_EXPORT AX_S32 AXCL_VDEC_StopRecvStream(AX_VDEC_GRP VdGrp) {
    IMPLEMENT_SERIALIZE(VdGrp);
}

AXCL_EXPORT AX_S32 AXCL_VDEC_QueryStatus(AX_VDEC_GRP VdGrp, AX_VDEC_GRP_STATUS_T *pstGrpStatus) {
    SERILAIZER()->input()->serialize(VdGrp);

    memset(pstGrpStatus, 0, sizeof(*pstGrpStatus));
    pstGrpStatus->enCodecType = create_enum_random_instance<AX_PAYLOAD_TYPE_E>(PT_PCMU, PT_BUTT);
    pstGrpStatus->u32LeftStreamBytes = initialize_random<AX_U32>();
    pstGrpStatus->u32LeftStreamFrames = initialize_random<AX_U32>();
    for (auto &m : pstGrpStatus->u32LeftPics) {
        m = initialize_random<AX_U32>();
    }
    pstGrpStatus->bStartRecvStream = initialize_random<AX_BOOL>();
    pstGrpStatus->u32RecvStreamFrames = initialize_random<AX_U32>();
    pstGrpStatus->u32DecodeStreamFrames = initialize_random<AX_U32>();
    pstGrpStatus->u32PicWidth = initialize_random<AX_U32>();
    pstGrpStatus->u32PicHeight = initialize_random<AX_U32>();
    pstGrpStatus->bInputFifoIsFull = initialize_random<AX_BOOL>();
    pstGrpStatus->stVdecDecErr.s32FormatErr = initialize_random<AX_S32>();
    pstGrpStatus->stVdecDecErr.s32PicSizeErrSet = initialize_random<AX_S32>();
    pstGrpStatus->stVdecDecErr.s32StreamUnsprt = initialize_random<AX_S32>();
    pstGrpStatus->stVdecDecErr.s32PackErr = initialize_random<AX_S32>();
    pstGrpStatus->stVdecDecErr.s32RefErrSet = initialize_random<AX_S32>();
    pstGrpStatus->stVdecDecErr.s32PicBufSizeErrSet = initialize_random<AX_S32>();
    pstGrpStatus->stVdecDecErr.s32StreamSizeOver = initialize_random<AX_S32>();
    pstGrpStatus->stVdecDecErr.s32VdecStreamNotRelease = initialize_random<AX_S32>();
    AX_S32 ret = 0;
    SERILAIZER()->output()->serialize(ret, *pstGrpStatus);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_VDEC_ResetGrp(AX_VDEC_GRP VdGrp) {
    IMPLEMENT_SERIALIZE(VdGrp);
}

AXCL_EXPORT AX_S32 AXCL_VDEC_SetGrpParam(AX_VDEC_GRP VdGrp, const AX_VDEC_GRP_PARAM_T *pstGrpParam) {
    IMPLEMENT_SERIALIZE(VdGrp, pstGrpParam);
}

AXCL_EXPORT AX_S32 AXCL_VDEC_GetGrpParam(AX_VDEC_GRP VdGrp, AX_VDEC_GRP_PARAM_T *pstGrpParam) {
    SERILAIZER()->input()->serialize(VdGrp);

    memset(pstGrpParam, 0, sizeof(*pstGrpParam));
    pstGrpParam->stVdecVideoParam.enOutputOrder =
        create_enum_random_instance<AX_VDEC_OUTPUT_ORDER_E>(AX_VDEC_OUTPUT_ORDER_DISP, AX_VDEC_OUTPUT_ORDER_BUTT);
    pstGrpParam->stVdecVideoParam.enVdecMode = create_enum_random_instance<AX_VDEC_MODE_E>(VIDEO_DEC_MODE_IPB, VIDEO_DEC_MODE_BUTT);
    pstGrpParam->f32SrcFrmRate = initialize_random<AX_F32>();
    AX_S32 ret = 0;
    SERILAIZER()->output()->serialize(ret, *pstGrpParam);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_VDEC_SelectGrp(AX_VDEC_GRP_SET_INFO_T *pstGrpSet, AX_S32 s32MilliSec) {
    SERILAIZER()->input()->serialize(s32MilliSec);

    memset(pstGrpSet, 0, sizeof(*pstGrpSet));
    pstGrpSet->u32GrpCount = static_cast<AX_U32>(create_int32_random_instance(0, AX_DEC_MAX_CHN_NUM));
    for (int i = 0; i < AX_VDEC_MAX_GRP_NUM; ++i) {
        pstGrpSet->stChnSet[i].VdGrp = static_cast<AX_U32>(create_int32_random_instance(0, AX_VDEC_MAX_GRP_NUM));
        pstGrpSet->stChnSet[i].u32ChnCount = static_cast<AX_U32>(create_int32_random_instance(0, AX_DEC_MAX_CHN_NUM));
        for (int j = 0; j < AX_DEC_MAX_CHN_NUM; ++j) {
            pstGrpSet->stChnSet[i].VdChn[j] = static_cast<AX_VDEC_CHN>(create_int32_random_instance(0, AX_DEC_MAX_CHN_NUM));
            pstGrpSet->stChnSet[i].u64ChnFrameNum[j] = initialize_random<AX_U64>();
        }
    }

    AX_S32 ret = 0;
    SERILAIZER()->output()->serialize(ret, *pstGrpSet);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_VDEC_SendStream(AX_VDEC_GRP VdGrp, const AX_VDEC_STREAM_T *pstStream, AX_S32 s32MilliSec) {
    IMPLEMENT_SERIALIZE(VdGrp, pstStream, s32MilliSec);
}

AXCL_EXPORT AX_S32 AXCL_VDEC_GetChnFrame(AX_VDEC_GRP VdGrp, AX_VDEC_CHN VdChn, AX_VIDEO_FRAME_INFO_T *pstFrameInfo, AX_S32 s32MilliSec) {
    SERILAIZER()->input()->serialize(VdGrp, VdChn, s32MilliSec);

    memset(pstFrameInfo, 0, sizeof(*pstFrameInfo));
    pstFrameInfo->stVFrame.u32Width = initialize_random<AX_U32>();
    pstFrameInfo->stVFrame.u32Height = initialize_random<AX_U32>();
    pstFrameInfo->stVFrame.enImgFormat = create_enum_random_instance<AX_IMG_FORMAT_E>(AX_FORMAT_INVALID, AX_FORMAT_MAX);
    pstFrameInfo->stVFrame.enVscanFormat = create_enum_random_instance<AX_VSCAN_FORMAT_E>(AX_VSCAN_FORMAT_RASTER, AX_VSCAN_FORMAT_BUTT);
    pstFrameInfo->stVFrame.stCompressInfo.enCompressMode =
        create_enum_random_instance<AX_COMPRESS_MODE_E>(AX_COMPRESS_MODE_NONE, AX_COMPRESS_MODE_BUTT);
    pstFrameInfo->stVFrame.stCompressInfo.u32CompressLevel = initialize_random<AX_U32>();
    pstFrameInfo->stVFrame.stDynamicRange = create_enum_random_instance<AX_DYNAMIC_RANGE_E>(AX_DYNAMIC_RANGE_SDR8, AX_DYNAMIC_RANGE_BUTT);
    pstFrameInfo->stVFrame.stColorGamut = create_enum_random_instance<AX_COLOR_GAMUT_E>(AX_COLOR_GAMUT_BT601, AX_COLOR_GAMUT_BUTT);

    for (int i = 0; i < AX_MAX_COLOR_COMPONENT; ++i) {
        pstFrameInfo->stVFrame.u32PicStride[i] = initialize_random<AX_U32>();
        pstFrameInfo->stVFrame.u32ExtStride[i] = initialize_random<AX_U32>();
        pstFrameInfo->stVFrame.u64PhyAddr[i] = initialize_random<AX_U64>();
        pstFrameInfo->stVFrame.u64VirAddr[i] = initialize_random<AX_U64>();
        pstFrameInfo->stVFrame.u64ExtPhyAddr[i] = initialize_random<AX_U64>();
        pstFrameInfo->stVFrame.u64ExtVirAddr[i] = initialize_random<AX_U64>();
        pstFrameInfo->stVFrame.u32HeaderSize[i] = initialize_random<AX_U32>();
    }

    pstFrameInfo->stVFrame.s16CropX = initialize_random<AX_S16>();
    pstFrameInfo->stVFrame.s16CropY = initialize_random<AX_S16>();
    pstFrameInfo->stVFrame.s16CropWidth = initialize_random<AX_S16>();
    pstFrameInfo->stVFrame.s16CropHeight = initialize_random<AX_S16>();

    pstFrameInfo->stVFrame.u32TimeRef = initialize_random<AX_U32>();
    pstFrameInfo->stVFrame.u64PTS = initialize_random<AX_U64>();
    pstFrameInfo->stVFrame.u64SeqNum = initialize_random<AX_U64>();
    pstFrameInfo->stVFrame.u64UserData = initialize_random<AX_U64>();
    pstFrameInfo->stVFrame.u64PrivateData = initialize_random<AX_U64>();
    pstFrameInfo->stVFrame.u32FrameFlag = initialize_random<AX_U32>();
    pstFrameInfo->stVFrame.u32FrameSize = initialize_random<AX_U32>();

    pstFrameInfo->enModId = create_enum_random_instance<AX_MOD_ID_E>(AX_ID_MIN, AX_ID_MAX);
    pstFrameInfo->bEndOfStream = initialize_random<AX_BOOL>();

    AX_S32 ret = 0;
    SERILAIZER()->output()->serialize(ret, *pstFrameInfo);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_VDEC_ReleaseChnFrame(AX_VDEC_GRP VdGrp, AX_VDEC_CHN VdChn, const AX_VIDEO_FRAME_INFO_T *pstFrameInfo) {
    IMPLEMENT_SERIALIZE(VdGrp, VdChn, pstFrameInfo);
}

AXCL_EXPORT AX_S32 AXCL_VDEC_GetUserData(AX_VDEC_GRP VdGrp, AX_VDEC_USERDATA_T *pstUserData) {
    SERILAIZER()->input()->serialize(VdGrp);

    memset(pstUserData, 0, sizeof(*pstUserData));
    pstUserData->u64PhyAddr = initialize_random<AX_U64>();
    pstUserData->u32UserDataCnt = initialize_random<AX_U32>();
    pstUserData->u32Len = initialize_random<AX_U32>();
    pstUserData->u32BufSize = initialize_random<AX_U32>();
    for (auto &m : pstUserData->u32DataLen) {
        m = initialize_random<AX_U32>();
    }
    pstUserData->bValid = initialize_random<AX_BOOL>();
    pstUserData->pu8Addr = reinterpret_cast<AX_U8 *>(initialize_random<AX_U64>());

    AX_S32 ret = 0;
    SERILAIZER()->output()->serialize(ret, *pstUserData);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_VDEC_ReleaseUserData(AX_VDEC_GRP VdGrp, const AX_VDEC_USERDATA_T *pstUserData) {
    IMPLEMENT_SERIALIZE(VdGrp, pstUserData);
}

AXCL_EXPORT AX_S32 AXCL_VDEC_SetUserPic(AX_VDEC_GRP VdGrp, const AX_VDEC_USRPIC_T *pstUsrPic) {
    IMPLEMENT_SERIALIZE(VdGrp, pstUsrPic);
}

AXCL_EXPORT AX_S32 AXCL_VDEC_EnableUserPic(AX_VDEC_GRP VdGrp) {
    IMPLEMENT_SERIALIZE(VdGrp);
}

AXCL_EXPORT AX_S32 AXCL_VDEC_DisableUserPic(AX_VDEC_GRP VdGrp) {
    IMPLEMENT_SERIALIZE(VdGrp);
}

AXCL_EXPORT AX_S32 AXCL_VDEC_SetDisplayMode(AX_VDEC_GRP VdGrp, AX_VDEC_DISPLAY_MODE_E enDisplayMode) {
    IMPLEMENT_SERIALIZE(VdGrp, enDisplayMode);
}

AXCL_EXPORT AX_S32 AXCL_VDEC_GetDisplayMode(AX_VDEC_GRP VdGrp, AX_VDEC_DISPLAY_MODE_E *penDisplayMode) {
    SERILAIZER()->input()->serialize(VdGrp);

    *penDisplayMode = create_enum_random_instance<AX_VDEC_DISPLAY_MODE_E>(AX_VDEC_DISPLAY_MODE_PREVIEW, AX_VDEC_DISPLAY_MODE_BUTT);
    AX_S32 ret = 0;
    SERILAIZER()->output()->serialize(ret, *penDisplayMode);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_VDEC_AttachPool(AX_VDEC_GRP VdGrp, AX_VDEC_CHN VdChn, AX_POOL PoolId) {
    IMPLEMENT_SERIALIZE(VdGrp, VdChn, PoolId);
}

AXCL_EXPORT AX_S32 AXCL_VDEC_DetachPool(AX_VDEC_GRP VdGrp, AX_VDEC_CHN VdChn) {
    IMPLEMENT_SERIALIZE(VdGrp, VdChn);
}

AXCL_EXPORT AX_S32 AXCL_VDEC_EnableChn(AX_VDEC_GRP VdGrp, AX_VDEC_CHN VdChn) {
    IMPLEMENT_SERIALIZE(VdGrp, VdChn);
}

AXCL_EXPORT AX_S32 AXCL_VDEC_DisableChn(AX_VDEC_GRP VdGrp, AX_VDEC_CHN VdChn) {
    IMPLEMENT_SERIALIZE(VdGrp, VdChn);
}

AXCL_EXPORT AX_S32 AXCL_VDEC_SetChnAttr(AX_VDEC_GRP VdGrp, AX_VDEC_CHN VdChn, const AX_VDEC_CHN_ATTR_T *pstVdChnAttr) {
    IMPLEMENT_SERIALIZE(VdGrp, VdChn, pstVdChnAttr);
}

AXCL_EXPORT AX_S32 AXCL_VDEC_GetChnAttr(AX_VDEC_GRP VdGrp, AX_VDEC_CHN VdChn, AX_VDEC_CHN_ATTR_T *pstVdChnAttr) {
    SERILAIZER()->input()->serialize(VdGrp, VdChn);

    memset(pstVdChnAttr, 0, sizeof(*pstVdChnAttr));
    pstVdChnAttr->u32PicWidth = initialize_random<AX_U32>();
    pstVdChnAttr->u32PicHeight = initialize_random<AX_U32>();
    pstVdChnAttr->u32FrameStride = initialize_random<AX_U32>();
    pstVdChnAttr->u32FramePadding = initialize_random<AX_U32>();
    pstVdChnAttr->u32CropX = initialize_random<AX_U32>();
    pstVdChnAttr->u32CropY = initialize_random<AX_U32>();
    pstVdChnAttr->u32ScaleRatioX = initialize_random<AX_U32>();
    pstVdChnAttr->u32ScaleRatioY = initialize_random<AX_U32>();
    pstVdChnAttr->u32OutputFifoDepth = initialize_random<AX_U32>();
    pstVdChnAttr->u32FrameBufCnt = initialize_random<AX_U32>();
    pstVdChnAttr->u32FrameBufSize = initialize_random<AX_U32>();
    pstVdChnAttr->enOutputMode = create_enum_random_instance<AX_VDEC_OUTPUT_MODE_E>(AX_VDEC_OUTPUT_ORIGINAL, AX_VDEC_OUTPUT_MODE_BUTT);
    pstVdChnAttr->enImgFormat = create_enum_random_instance<AX_IMG_FORMAT_E>(AX_FORMAT_INVALID, AX_FORMAT_MAX);
    pstVdChnAttr->stCompressInfo.enCompressMode =
        create_enum_random_instance<AX_COMPRESS_MODE_E>(AX_COMPRESS_MODE_NONE, AX_COMPRESS_MODE_BUTT);
    pstVdChnAttr->stCompressInfo.u32CompressLevel = initialize_random<AX_U32>();
    pstVdChnAttr->stOutputFrmRate.f32DstFrmRate = initialize_random<AX_F32>();
    pstVdChnAttr->stOutputFrmRate.bFrmRateCtrl = initialize_random<AX_BOOL>();

    AX_S32 ret = 0;
    SERILAIZER()->output()->serialize(ret, *pstVdChnAttr);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_VDEC_JpegDecodeOneFrame(AX_VDEC_DEC_ONE_FRM_T *pstParam) {
    IMPLEMENT_SERIALIZE(pstParam);
}

AXCL_EXPORT AX_S32 AXCL_VDEC_GetStreamBufInfo(AX_VDEC_GRP VdGrp, AX_VDEC_STREAM_BUF_INFO_T *pstStreamBufInfo) {
    SERILAIZER()->input()->serialize(VdGrp);

    memset(pstStreamBufInfo, 0, sizeof(*pstStreamBufInfo));
    pstStreamBufInfo->phyStart = initialize_random<AX_U64>();
    pstStreamBufInfo->virStart = reinterpret_cast<AX_U8 *>(initialize_random<AX_U64>());
    pstStreamBufInfo->totalSize = initialize_random<AX_U32>();
    pstStreamBufInfo->readAbleSize = initialize_random<AX_U32>();
    pstStreamBufInfo->writeAbleSize = initialize_random<AX_U32>();
    pstStreamBufInfo->readOffset = initialize_random<AX_U32>();
    pstStreamBufInfo->writeOffset = initialize_random<AX_U32>();
    AX_S32 ret = 0;
    SERILAIZER()->output()->serialize(ret, *pstStreamBufInfo);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_VDEC_GetVuiParam(AX_VDEC_GRP VdGrp, AX_VDEC_VUI_PARAM_T *pstVuiParam) {
    SERILAIZER()->input()->serialize(VdGrp);

    memset(pstVuiParam, 0, sizeof(*pstVuiParam));
    pstVuiParam->stVuiAspectRatio.aspect_ratio_info_present_flag = initialize_random<AX_U8>();
    pstVuiParam->stVuiAspectRatio.aspect_ratio_idc = initialize_random<AX_U8>();
    pstVuiParam->stVuiAspectRatio.overscan_info_present_flag = initialize_random<AX_U8>();
    pstVuiParam->stVuiAspectRatio.overscan_appropriate_flag = initialize_random<AX_U8>();
    pstVuiParam->stVuiAspectRatio.sar_width = initialize_random<AX_U16>();
    pstVuiParam->stVuiAspectRatio.sar_height = initialize_random<AX_U16>();

    pstVuiParam->stVuiTimeInfo.timing_info_present_flag = initialize_random<AX_U8>();
    pstVuiParam->stVuiTimeInfo.num_units_in_tick = initialize_random<AX_U32>();
    pstVuiParam->stVuiTimeInfo.time_scale = initialize_random<AX_U32>();
    pstVuiParam->stVuiTimeInfo.fixed_frame_rate_flag = initialize_random<AX_U8>();
    pstVuiParam->stVuiTimeInfo.num_ticks_poc_diff_one_minus1 = initialize_random<AX_U32>();

    pstVuiParam->stVuiVideoSignal.video_signal_type_present_flag = initialize_random<AX_U8>();
    pstVuiParam->stVuiVideoSignal.video_format = initialize_random<AX_U8>();
    pstVuiParam->stVuiVideoSignal.video_full_range_flag = initialize_random<AX_U8>();
    pstVuiParam->stVuiVideoSignal.colour_description_present_flag = initialize_random<AX_U8>();
    pstVuiParam->stVuiVideoSignal.colour_primaries = initialize_random<AX_U8>();
    pstVuiParam->stVuiVideoSignal.transfer_characteristics = initialize_random<AX_U8>();
    pstVuiParam->stVuiVideoSignal.matrix_coefficients = initialize_random<AX_U8>();

    pstVuiParam->stVuiBitstreamRestric.bitstream_restriction_flag = initialize_random<AX_U8>();

    AX_S32 ret = 0;
    SERILAIZER()->output()->serialize(ret, *pstVuiParam);
    return ret;
}
