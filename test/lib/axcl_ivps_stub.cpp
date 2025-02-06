/**************************************************************************************************
 *
 * Copyright (c) 2019-2024 Axera Semiconductor Co., Ltd. All Rights Reserved.
 *
 * This source file is the property of Axera Semiconductor Co., Ltd. and
 * may not be copied or distributed in any isomorphic form without the prior
 * written consent of Axera Semiconductor Co., Ltd.
 *
 **************************************************************************************************/

#include "axcl_base.h"
#include "axcl_module_version.h"
#include "randomizer.hpp"
#include "serializer.hpp"
#include <cstring>

#include "axcl_ivps.h"

static AX_VOID set_dst_frame(AX_VIDEO_FRAME_T *ptFrame) {
    ptFrame->u32Width = 1920;
    ptFrame->u32Height = 1080;
    ptFrame->enImgFormat = AX_FORMAT_YUV444_PACKED;
    ptFrame->enVscanFormat = AX_VSCAN_FORMAT_RASTER;

    ptFrame->stCompressInfo.enCompressMode = AX_COMPRESS_MODE_LOSSY;
    ptFrame->stCompressInfo.u32CompressLevel = 2;

    ptFrame->stDynamicRange = AX_DYNAMIC_RANGE_HLG;
    ptFrame->stColorGamut = AX_COLOR_GAMUT_BT2020;

    for (int i = 0; i < AX_MAX_COLOR_COMPONENT; i++) {
        ptFrame->u32PicStride[i] = 1920;
        ptFrame->u32ExtStride[i] = 1920;
        ptFrame->u64PhyAddr[i] = 0x10000000 + (i * 0x1000);
        ptFrame->u64VirAddr[i] = 0x20000000 + (i * 0x1000);
        ptFrame->u64ExtPhyAddr[i] = 0x30000000 + (i * 0x1000);
        ptFrame->u64ExtVirAddr[i] = 0x40000000 + (i * 0x1000);
        ptFrame->u32HeaderSize[i] = 128;
        ptFrame->u32BlkId[i] = i;
    }

    ptFrame->s16CropX = 0;
    ptFrame->s16CropY = 0;
    ptFrame->s16CropWidth = 1920;
    ptFrame->s16CropHeight = 1080;

    ptFrame->u32TimeRef = 0;
    ptFrame->u64PTS = 123456789;
    ptFrame->u64SeqNum = 1;
    ptFrame->u64UserData = 2;
    ptFrame->u64PrivateData = 3;
    ptFrame->u32FrameFlag = 4;
    ptFrame->u32FrameSize = 1920 * 1080 * 3;
}

AXCL_EXPORT AX_S32 AXCL_IVPS_Init(AX_VOID) {
    AX_S32 ret = 0;
    SERILAIZER()->output()->serialize(ret);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_IVPS_Deinit(AX_VOID) {
    SERILAIZER()->input()->serialize();
    AX_S32 ret = 0;
    SERILAIZER()->output()->serialize(ret);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_IVPS_CreateGrp(IVPS_GRP IvpsGrp, const AX_IVPS_GRP_ATTR_T *ptGrpAttr) {
    SERILAIZER()->input()->serialize(IvpsGrp, ptGrpAttr);
    AX_S32 ret = initialize_random<AX_S32>();
    SERILAIZER()->output()->serialize(ret);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_IVPS_CreateGrpEx(IVPS_GRP *IvpsGrp, const AX_IVPS_GRP_ATTR_T *ptGrpAttr) {
    SERILAIZER()->input()->serialize(ptGrpAttr);
    AX_S32 ret = 0;
    *IvpsGrp = initialize_random<IVPS_GRP>();
    SERILAIZER()->output()->serialize(ret, *IvpsGrp);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_IVPS_DestoryGrp(IVPS_GRP IvpsGrp) {
    SERILAIZER()->input()->serialize(IvpsGrp);
    AX_S32 ret = 0;
    SERILAIZER()->output()->serialize(ret);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_IVPS_SetPipelineAttr(IVPS_GRP IvpsGrp, AX_IVPS_PIPELINE_ATTR_T *ptPipelineAttr) {
    SERILAIZER()->input()->serialize(IvpsGrp, ptPipelineAttr);
    AX_S32 ret = initialize_random<AX_S32>();
    SERILAIZER()->output()->serialize(ret);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_IVPS_GetPipelineAttr(IVPS_GRP IvpsGrp, AX_IVPS_PIPELINE_ATTR_T *ptPipelineAttr) {
    SERILAIZER()->input()->serialize(IvpsGrp);
    AX_S32 ret = 0;
    // *ptPipelineAttr = initialize_random<AX_IVPS_PIPELINE_ATTR_T>();
    memset(ptPipelineAttr, 0, sizeof(AX_IVPS_PIPELINE_ATTR_T));
    ptPipelineAttr->nInDebugFifoDepth = 3;
    ptPipelineAttr->nOutChnNum = 1;
    SERILAIZER()->output()->serialize(ret, ptPipelineAttr);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_IVPS_StartGrp(IVPS_GRP IvpsGrp) {
    SERILAIZER()->input()->serialize(IvpsGrp);
    AX_S32 ret = initialize_random<AX_S32>();
    SERILAIZER()->output()->serialize(ret);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_IVPS_StopGrp(IVPS_GRP IvpsGrp) {
    SERILAIZER()->input()->serialize(IvpsGrp);
    AX_S32 ret = initialize_random<AX_S32>();
    SERILAIZER()->output()->serialize(ret);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_IVPS_EnableChn(IVPS_GRP IvpsGrp, IVPS_CHN IvpsChn) {
    SERILAIZER()->input()->serialize(IvpsGrp, IvpsChn);
    AX_S32 ret = initialize_random<AX_S32>();
    SERILAIZER()->output()->serialize(ret);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_IVPS_DisableChn(IVPS_GRP IvpsGrp, IVPS_CHN IvpsChn) {
    SERILAIZER()->input()->serialize(IvpsGrp, IvpsChn);
    AX_S32 ret = initialize_random<AX_S32>();
    SERILAIZER()->output()->serialize(ret);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_IVPS_SendFrame(IVPS_GRP IvpsGrp, const AX_VIDEO_FRAME_T *ptFrame, AX_S32 nMilliSec) {
    SERILAIZER()->input()->serialize(IvpsGrp, ptFrame, nMilliSec);
    AX_S32 ret = initialize_random<AX_S32>();
    SERILAIZER()->output()->serialize(ret);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_IVPS_GetChnFrame(IVPS_GRP IvpsGrp, IVPS_CHN IvpsChn, AX_VIDEO_FRAME_T *ptFrame, AX_S32 nMilliSec) {
    SERILAIZER()->input()->serialize(IvpsGrp, IvpsChn, nMilliSec);
    AX_S32 ret = 0;
    set_dst_frame(ptFrame);
    SERILAIZER()->output()->serialize(ret, ptFrame);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_IVPS_ReleaseChnFrame(IVPS_GRP IvpsGrp, IVPS_CHN IvpsChn, AX_VIDEO_FRAME_T *ptFrame) {
    SERILAIZER()->input()->serialize(IvpsGrp, IvpsChn, ptFrame);
    AX_S32 ret = initialize_random<AX_S32>();
    SERILAIZER()->output()->serialize(ret);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_IVPS_GetGrpFrame(IVPS_GRP IvpsGrp, AX_VIDEO_FRAME_T *ptFrame, AX_S32 nMilliSec) {
    SERILAIZER()->input()->serialize(IvpsGrp, nMilliSec);
    AX_S32 ret = 0;
    set_dst_frame(ptFrame);
    SERILAIZER()->output()->serialize(ret, ptFrame);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_IVPS_ReleaseGrpFrame(IVPS_GRP IvpsGrp, AX_VIDEO_FRAME_T *ptFrame) {
    SERILAIZER()->input()->serialize(IvpsGrp, ptFrame);
    AX_S32 ret = initialize_random<AX_S32>();
    SERILAIZER()->output()->serialize(ret);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_IVPS_GetChnFd(IVPS_GRP IvpsGrp, IVPS_CHN IvpsChn) {
    SERILAIZER()->input()->serialize(IvpsGrp, IvpsChn);
    AX_S32 ret = initialize_random<AX_S32>();
    SERILAIZER()->output()->serialize(ret);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_IVPS_GetDebugFifoFrame(IVPS_GRP IvpsGrp, AX_VIDEO_FRAME_T *ptFrame) {
    SERILAIZER()->input()->serialize(IvpsGrp);
    AX_S32 ret = 0;
    set_dst_frame(ptFrame);
    SERILAIZER()->output()->serialize(ret, ptFrame);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_IVPS_ReleaseDebugFifoFrame(IVPS_GRP IvpsGrp, AX_VIDEO_FRAME_T *ptFrame) {
    SERILAIZER()->input()->serialize(IvpsGrp, ptFrame);
    AX_S32 ret = initialize_random<AX_S32>();
    SERILAIZER()->output()->serialize(ret);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_IVPS_CloseAllFd(AX_VOID) {
    SERILAIZER()->input()->serialize();
    AX_S32 ret = 0;
    SERILAIZER()->output()->serialize(ret);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_IVPS_SetGrpLDCAttr(IVPS_GRP IvpsGrp, IVPS_FILTER IvpsFilter, const AX_IVPS_LDC_ATTR_T *ptLDCAttr) {
    SERILAIZER()->input()->serialize(IvpsGrp, IvpsFilter, ptLDCAttr);
    AX_S32 ret = initialize_random<AX_S32>();
    SERILAIZER()->output()->serialize(ret);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_IVPS_GetGrpLDCAttr(IVPS_GRP IvpsGrp, IVPS_FILTER IvpsFilter, AX_IVPS_LDC_ATTR_T *ptLDCAttr) {
    SERILAIZER()->input()->serialize(IvpsGrp, IvpsFilter);
    AX_S32 ret = 0;
    // *ptLDCAttr = initialize_random<AX_IVPS_LDC_ATTR_T>();
    memset(ptLDCAttr, 0, sizeof(AX_IVPS_LDC_ATTR_T));
    ptLDCAttr->bAspect = AX_TRUE;
    ptLDCAttr->nYRatio = 1;
    SERILAIZER()->output()->serialize(ret, ptLDCAttr);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_IVPS_SetChnLDCAttr(IVPS_GRP IvpsGrp, IVPS_CHN IvpsChn, IVPS_FILTER IvpsFilter, const AX_IVPS_LDC_ATTR_T *ptLDCAttr) {
    SERILAIZER()->input()->serialize(IvpsGrp, IvpsChn, IvpsFilter, ptLDCAttr);
    AX_S32 ret = initialize_random<AX_S32>();
    SERILAIZER()->output()->serialize(ret);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_IVPS_GetChnLDCAttr(IVPS_GRP IvpsGrp, IVPS_CHN IvpsChn, IVPS_FILTER IvpsFilter, AX_IVPS_LDC_ATTR_T *ptLDCAttr) {
    SERILAIZER()->input()->serialize(IvpsGrp, IvpsChn, IvpsFilter);
    AX_S32 ret = 0;
    // *ptLDCAttr = initialize_random<AX_IVPS_LDC_ATTR_T>();
    memset(ptLDCAttr, 0, sizeof(AX_IVPS_LDC_ATTR_T));
    ptLDCAttr->bAspect = AX_TRUE;
    ptLDCAttr->nYRatio = 1;
    SERILAIZER()->output()->serialize(ret, ptLDCAttr);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_IVPS_SetGrpPoolAttr(IVPS_GRP IvpsGrp, const AX_IVPS_POOL_ATTR_T *ptPoolAttr) {
    SERILAIZER()->input()->serialize(IvpsGrp, ptPoolAttr);
    AX_S32 ret = initialize_random<AX_S32>();
    SERILAIZER()->output()->serialize(ret);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_IVPS_SetChnPoolAttr(IVPS_GRP IvpsGrp, IVPS_CHN IvpsChn, const AX_IVPS_POOL_ATTR_T *ptPoolAttr) {
    SERILAIZER()->input()->serialize(IvpsGrp, IvpsChn, ptPoolAttr);
    AX_S32 ret = initialize_random<AX_S32>();
    SERILAIZER()->output()->serialize(ret);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_IVPS_SetGrpUserFRC(IVPS_GRP IvpsGrp, const AX_IVPS_USER_FRAME_RATE_CTRL_T *ptFrameRateAttr) {
    SERILAIZER()->input()->serialize(IvpsGrp, ptFrameRateAttr);
    AX_S32 ret = initialize_random<AX_S32>();
    SERILAIZER()->output()->serialize(ret);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_IVPS_SetChnUserFRC(IVPS_GRP IvpsGrp, IVPS_CHN IvpsChn, const AX_IVPS_USER_FRAME_RATE_CTRL_T *ptFrameRateAttr) {
    SERILAIZER()->input()->serialize(IvpsGrp, IvpsChn, ptFrameRateAttr);
    AX_S32 ret = initialize_random<AX_S32>();
    SERILAIZER()->output()->serialize(ret);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_IVPS_SetGrpCrop(IVPS_GRP IvpsGrp, const AX_IVPS_CROP_INFO_T *ptCropInfo) {
    SERILAIZER()->input()->serialize(IvpsGrp, ptCropInfo);
    AX_S32 ret = initialize_random<AX_S32>();
    SERILAIZER()->output()->serialize(ret);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_IVPS_GetGrpCrop(IVPS_GRP IvpsGrp, AX_IVPS_CROP_INFO_T *ptCropInfo) {
    SERILAIZER()->input()->serialize(IvpsGrp);
    AX_S32 ret = 0;
    *ptCropInfo = initialize_random<AX_IVPS_CROP_INFO_T>();
    SERILAIZER()->output()->serialize(ret, ptCropInfo);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_IVPS_SetChnAttr(IVPS_GRP IvpsGrp, IVPS_CHN IvpsChn, IVPS_FILTER IvpsFilter, const AX_IVPS_CHN_ATTR_T *ptChnAttr) {
    SERILAIZER()->input()->serialize(IvpsGrp, IvpsChn, IvpsFilter, ptChnAttr);
    AX_S32 ret = initialize_random<AX_S32>();
    SERILAIZER()->output()->serialize(ret);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_IVPS_GetChnAttr(IVPS_GRP IvpsGrp, IVPS_CHN IvpsChn, IVPS_FILTER IvpsFilter, AX_IVPS_CHN_ATTR_T *ptChnAttr) {
    SERILAIZER()->input()->serialize(IvpsGrp, IvpsChn, IvpsFilter);
    AX_S32 ret = 0;
    // *ptChnAttr = initialize_random<AX_IVPS_CHN_ATTR_T>();
    memset(ptChnAttr, 0, sizeof(AX_IVPS_CHN_ATTR_T));
    ptChnAttr->nFRC = 30;
    ptChnAttr->nOutFifoDepth = 2;
    SERILAIZER()->output()->serialize(ret, ptChnAttr);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_IVPS_EnableBackupFrame(IVPS_GRP IvpsGrp, AX_U8 nFifoDepth) {
    SERILAIZER()->input()->serialize(IvpsGrp, nFifoDepth);
    AX_S32 ret = initialize_random<AX_S32>();
    SERILAIZER()->output()->serialize(ret);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_IVPS_DisableBackupFrame(IVPS_GRP IvpsGrp) {
    SERILAIZER()->input()->serialize(IvpsGrp);
    AX_S32 ret = initialize_random<AX_S32>();
    SERILAIZER()->output()->serialize(ret);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_IVPS_ResetGrp(IVPS_GRP IvpsGrp) {
    SERILAIZER()->input()->serialize(IvpsGrp);
    AX_S32 ret = initialize_random<AX_S32>();
    SERILAIZER()->output()->serialize(ret);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_IVPS_GetEngineDutyCycle(AX_IVPS_DUTY_CYCLE_ATTR_T *ptDutyCycle) {
    SERILAIZER()->input()->serialize();
    AX_S32 ret = 0;
    *ptDutyCycle = initialize_random<AX_IVPS_DUTY_CYCLE_ATTR_T>();
    SERILAIZER()->output()->serialize(ret, ptDutyCycle);
    return ret;
}

AXCL_EXPORT IVPS_RGN_HANDLE AXCL_IVPS_RGN_Create(AX_VOID) {
    SERILAIZER()->input()->serialize();
    AX_S32 handle = initialize_random<IVPS_RGN_HANDLE>();
    SERILAIZER()->output()->serialize(handle);
    return handle;
}

AXCL_EXPORT AX_S32 AXCL_IVPS_RGN_Destroy(IVPS_RGN_HANDLE hRegion) {
    SERILAIZER()->input()->serialize(hRegion);
    AX_S32 ret = 0;
    SERILAIZER()->output()->serialize(ret);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_IVPS_RGN_AttachToFilter(IVPS_RGN_HANDLE hRegion, IVPS_GRP IvpsGrp, IVPS_FILTER IvpsFilter) {
    SERILAIZER()->input()->serialize(hRegion, IvpsGrp, IvpsFilter);
    AX_S32 ret = initialize_random<AX_S32>();
    SERILAIZER()->output()->serialize(ret);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_IVPS_RGN_DetachFromFilter(IVPS_RGN_HANDLE hRegion, IVPS_GRP IvpsGrp, IVPS_FILTER IvpsFilter) {
    SERILAIZER()->input()->serialize(hRegion, IvpsGrp, IvpsFilter);
    AX_S32 ret = initialize_random<AX_S32>();
    SERILAIZER()->output()->serialize(ret);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_IVPS_RGN_Update(IVPS_RGN_HANDLE hRegion, const AX_IVPS_RGN_DISP_GROUP_T *ptDisp) {
    SERILAIZER()->input()->serialize(hRegion, ptDisp);
    AX_S32 ret = initialize_random<AX_S32>();
    SERILAIZER()->output()->serialize(ret);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_IVPS_CmmCopyTdp(AX_U64 nSrcPhyAddr, AX_U64 nDstPhyAddr, AX_U64 nMemSize) {
    SERILAIZER()->input()->serialize(nSrcPhyAddr, nDstPhyAddr, nMemSize);
    AX_S32 ret = initialize_random<AX_S32>();
    SERILAIZER()->output()->serialize(ret);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_IVPS_FlipAndRotationTdp(const AX_VIDEO_FRAME_T *ptSrc, AX_IVPS_CHN_FLIP_MODE_E eFlipMode, AX_IVPS_ROTATION_E eRotation, AX_VIDEO_FRAME_T *ptDst) {
    SERILAIZER()->input()->serialize(ptSrc, eFlipMode, eRotation, ptDst);
    AX_S32 ret = 0;
    SERILAIZER()->output()->serialize(ret);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_IVPS_CscTdp(const AX_VIDEO_FRAME_T *ptSrc, AX_VIDEO_FRAME_T *ptDst) {
    SERILAIZER()->input()->serialize(ptSrc, ptDst);
    AX_S32 ret = 0;
    SERILAIZER()->output()->serialize(ret);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_IVPS_CropResizeTdp(const AX_VIDEO_FRAME_T *ptSrc, AX_VIDEO_FRAME_T *ptDst, const AX_IVPS_ASPECT_RATIO_T *ptAspectRatio) {
    SERILAIZER()->input()->serialize(ptSrc, ptDst, ptAspectRatio);
    AX_S32 ret = 0;
    SERILAIZER()->output()->serialize(ret);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_IVPS_CropResizeV2Tdp(const AX_VIDEO_FRAME_T *ptSrc, const AX_IVPS_RECT_T tBox[], AX_U32 nCropNum, AX_VIDEO_FRAME_T *ptDst[], const AX_IVPS_ASPECT_RATIO_T *ptAspectRatio) {
    AX_S32 ret = 0;
    SERILAIZER()->input()->serialize(ptSrc, tBox, nCropNum, *ptDst, ptAspectRatio);
    SERILAIZER()->output()->serialize(ret);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_IVPS_AlphaBlendingTdp(const AX_VIDEO_FRAME_T *ptSrc, const AX_VIDEO_FRAME_T *ptOverlay, const AX_IVPS_POINT_T tOffset, AX_U8 nAlpha, AX_VIDEO_FRAME_T *ptDst) {
    SERILAIZER()->input()->serialize(ptSrc, ptOverlay, tOffset, nAlpha, ptDst);
    AX_S32 ret = 0;
    SERILAIZER()->output()->serialize(ret);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_IVPS_AlphaBlendingV3Tdp(const AX_VIDEO_FRAME_T *ptSrc, const AX_OVERLAY_T *ptOverlay, AX_VIDEO_FRAME_T *ptDst) {
    SERILAIZER()->input()->serialize(ptSrc, ptOverlay, ptDst);
    AX_S32 ret = 0;
    SERILAIZER()->output()->serialize(ret);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_IVPS_DrawOsdTdp(const AX_VIDEO_FRAME_T *ptFrame, const AX_OSD_BMP_ATTR_T arrBmp[], AX_U32 nNum) {
    SERILAIZER()->input()->serialize(ptFrame, arrBmp, nNum);
    AX_S32 ret = initialize_random<AX_S32>();
    SERILAIZER()->output()->serialize(ret);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_IVPS_DrawMosaicTdp(const AX_VIDEO_FRAME_T *ptSrc, AX_IVPS_RGN_MOSAIC_T tMosaic[], AX_U32 nNum) {
    SERILAIZER()->input()->serialize(ptSrc, tMosaic, nNum);
    AX_S32 ret = initialize_random<AX_S32>();
    SERILAIZER()->output()->serialize(ret);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_IVPS_CmmCopyVpp(AX_U64 nSrcPhyAddr, AX_U64 nDstPhyAddr, AX_U64 nMemSize) {
    SERILAIZER()->input()->serialize(nSrcPhyAddr, nDstPhyAddr, nMemSize);
    AX_S32 ret = initialize_random<AX_S32>();
    SERILAIZER()->output()->serialize(ret);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_IVPS_CropResizeVpp(const AX_VIDEO_FRAME_T *ptSrc, AX_VIDEO_FRAME_T *ptDst, const AX_IVPS_ASPECT_RATIO_T *ptAspectRatio) {
    SERILAIZER()->input()->serialize(ptSrc, ptDst, ptAspectRatio);
    AX_S32 ret = 0;
    SERILAIZER()->output()->serialize(ret);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_IVPS_CropResizeV2Vpp(const AX_VIDEO_FRAME_T *ptSrc, const AX_IVPS_RECT_T tBox[], AX_U32 nCropNum, AX_VIDEO_FRAME_T *ptDst[], const AX_IVPS_ASPECT_RATIO_T *ptAspectRatio) {
    AX_S32 ret = 0;
    SERILAIZER()->input()->serialize(ptSrc, tBox, nCropNum, *ptDst, ptAspectRatio);
    SERILAIZER()->output()->serialize(ret);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_IVPS_CropResizeV3Vpp(const AX_VIDEO_FRAME_T *ptSrc, AX_VIDEO_FRAME_T *ptDst[], AX_U32 nNum, const AX_IVPS_ASPECT_RATIO_T *ptAspectRatio) {
    AX_S32 ret = 0;
    SERILAIZER()->input()->serialize(ptSrc, *ptDst, nNum, ptAspectRatio);
    for (AX_U32 i = 0; i < nNum; ++i) {
        set_dst_frame(ptDst[i]);
    }
    SERILAIZER()->output()->serialize(ret);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_IVPS_CscVpp(const AX_VIDEO_FRAME_T *ptSrc, AX_VIDEO_FRAME_T *ptDst) {
    SERILAIZER()->input()->serialize(ptSrc, ptDst);
    AX_S32 ret = 0;
    SERILAIZER()->output()->serialize(ret);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_IVPS_DrawMosaicVpp(const AX_VIDEO_FRAME_T *ptSrc, AX_IVPS_RGN_MOSAIC_T tMosaic[], AX_U32 nNum) {
    SERILAIZER()->input()->serialize(ptSrc, tMosaic, nNum);
    AX_S32 ret = initialize_random<AX_S32>();
    SERILAIZER()->output()->serialize(ret);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_IVPS_SetScaleCoefLevelVpp(const AX_IVPS_SCALE_RANGE_T *ScaleRange, const AX_IVPS_SCALE_COEF_LEVEL_T *CoefLevel) {
    SERILAIZER()->input()->serialize(ScaleRange, CoefLevel);
    AX_S32 ret = initialize_random<AX_S32>();
    SERILAIZER()->output()->serialize(ret);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_IVPS_GetScaleCoefLevelVpp(const AX_IVPS_SCALE_RANGE_T *ScaleRange, AX_IVPS_SCALE_COEF_LEVEL_T *CoefLevel) {
    SERILAIZER()->input()->serialize(ScaleRange);
    AX_S32 ret = 0;
    memset(CoefLevel, 0, sizeof(AX_IVPS_SCALE_COEF_LEVEL_T));
    CoefLevel->eHorLuma = AX_IVPS_COEF_LEVEL_6;
    CoefLevel->eHorChroma = AX_IVPS_COEF_LEVEL_6;
    CoefLevel->eVerLuma = AX_IVPS_COEF_LEVEL_6;
    CoefLevel->eVerChroma = AX_IVPS_COEF_LEVEL_6;
    SERILAIZER()->output()->serialize(ret, CoefLevel);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_IVPS_CmmCopyVgp(AX_U64 nSrcPhyAddr, AX_U64 nDstPhyAddr, AX_U64 nMemSize) {
    SERILAIZER()->input()->serialize(nSrcPhyAddr, nDstPhyAddr, nMemSize);
    AX_S32 ret = initialize_random<AX_S32>();
    SERILAIZER()->output()->serialize(ret);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_IVPS_CscVgp(const AX_VIDEO_FRAME_T *ptSrc, AX_VIDEO_FRAME_T *ptDst) {
    SERILAIZER()->input()->serialize(ptSrc, ptDst);
    AX_S32 ret = 0;
    SERILAIZER()->output()->serialize(ret);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_IVPS_CropResizeVgp(const AX_VIDEO_FRAME_T *ptSrc, AX_VIDEO_FRAME_T *ptDst, const AX_IVPS_ASPECT_RATIO_T *ptAspectRatio) {
    SERILAIZER()->input()->serialize(ptSrc, ptDst, ptAspectRatio);
    AX_S32 ret = 0;
    SERILAIZER()->output()->serialize(ret);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_IVPS_CropResizeV2Vgp(const AX_VIDEO_FRAME_T *ptSrc, const AX_IVPS_RECT_T tBox[], AX_U32 nCropNum, AX_VIDEO_FRAME_T *ptDst[], const AX_IVPS_ASPECT_RATIO_T *ptAspectRatio) {
    AX_S32 ret = 0;
    SERILAIZER()->input()->serialize(ptSrc, tBox, nCropNum, *ptDst, ptAspectRatio);
    SERILAIZER()->output()->serialize(ret);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_IVPS_CropResizeV4Vgp(const AX_VIDEO_FRAME_T *ptSrc, AX_VIDEO_FRAME_T *ptDst, const AX_IVPS_ASPECT_RATIO_T *ptAspectRatio, const AX_IVPS_SCALE_STEP_T *ptScaleStep) {
    SERILAIZER()->input()->serialize(ptSrc, ptDst, ptAspectRatio, ptScaleStep);
    AX_S32 ret = 0;
    SERILAIZER()->output()->serialize(ret);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_IVPS_AlphaBlendingVgp(const AX_VIDEO_FRAME_T *ptSrc, const AX_VIDEO_FRAME_T *ptOverlay, const AX_IVPS_POINT_T tOffset, AX_U8 nAlpha, AX_VIDEO_FRAME_T *ptDst) {
    SERILAIZER()->input()->serialize(ptSrc, ptOverlay, tOffset, nAlpha, ptDst);
    AX_S32 ret = 0;
    SERILAIZER()->output()->serialize(ret);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_IVPS_AlphaBlendingV2Vgp(const AX_VIDEO_FRAME_T *ptSrc, const AX_VIDEO_FRAME_T *ptOverlay, const AX_IVPS_POINT_T tOffset, const AX_IVPS_ALPHA_LUT_T *ptSpAlpha, AX_VIDEO_FRAME_T *ptDst) {
    SERILAIZER()->input()->serialize(ptSrc, ptOverlay, tOffset, ptSpAlpha, ptDst);
    AX_S32 ret = 0;
    SERILAIZER()->output()->serialize(ret);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_IVPS_AlphaBlendingV3Vgp(const AX_VIDEO_FRAME_T *ptSrc, const AX_OVERLAY_T *ptOverlay, AX_VIDEO_FRAME_T *ptDst) {
    SERILAIZER()->input()->serialize(ptSrc, ptOverlay, ptDst);
    AX_S32 ret = 0;
    SERILAIZER()->output()->serialize(ret);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_IVPS_DrawOsdVgp(const AX_VIDEO_FRAME_T *ptFrame, const AX_OSD_BMP_ATTR_T arrBmp[], AX_U32 nNum) {
    SERILAIZER()->input()->serialize(ptFrame, arrBmp, nNum);
    AX_S32 ret = initialize_random<AX_S32>();
    SERILAIZER()->output()->serialize(ret);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_IVPS_DrawMosaicVgp(const AX_VIDEO_FRAME_T *ptSrc, AX_IVPS_RGN_MOSAIC_T tMosaic[], AX_U32 nNum) {
    SERILAIZER()->input()->serialize(ptSrc, tMosaic, nNum);
    AX_S32 ret = initialize_random<AX_S32>();
    SERILAIZER()->output()->serialize(ret);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_IVPS_SetScaleCoefLevelVgp(const AX_IVPS_SCALE_RANGE_T *ScaleRange, const AX_IVPS_SCALE_COEF_LEVEL_T *CoefLevel) {
    SERILAIZER()->input()->serialize(ScaleRange, CoefLevel);
    AX_S32 ret = initialize_random<AX_S32>();
    SERILAIZER()->output()->serialize(ret);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_IVPS_GetScaleCoefLevelVgp(const AX_IVPS_SCALE_RANGE_T *ScaleRange, AX_IVPS_SCALE_COEF_LEVEL_T *CoefLevel) {
    SERILAIZER()->input()->serialize(ScaleRange);
    AX_S32 ret = 0;
    memset(CoefLevel, 0, sizeof(AX_IVPS_SCALE_COEF_LEVEL_T));
    CoefLevel->eHorLuma = AX_IVPS_COEF_LEVEL_4;
    CoefLevel->eHorChroma = AX_IVPS_COEF_LEVEL_6;
    CoefLevel->eVerLuma = AX_IVPS_COEF_LEVEL_6;
    CoefLevel->eVerChroma = AX_IVPS_COEF_LEVEL_6;
    SERILAIZER()->output()->serialize(ret, CoefLevel);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_IVPS_DrawLine(const AX_IVPS_RGN_CANVAS_INFO_T *ptCanvas, AX_IVPS_GDI_ATTR_T tAttr, const AX_IVPS_POINT_T tPoint[], AX_U32 nPointNum) {
    SERILAIZER()->input()->serialize(ptCanvas, tAttr, tPoint, nPointNum);
    AX_S32 ret = initialize_random<AX_S32>();
    SERILAIZER()->output()->serialize(ret);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_IVPS_DrawPolygon(const AX_IVPS_RGN_CANVAS_INFO_T *ptCanvas, AX_IVPS_GDI_ATTR_T tAttr, const AX_IVPS_POINT_T tPoint[], AX_U32 nPointNum) {
    SERILAIZER()->input()->serialize(ptCanvas, tAttr, tPoint, nPointNum);
    AX_S32 ret = initialize_random<AX_S32>();
    SERILAIZER()->output()->serialize(ret);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_IVPS_DrawRect(const AX_IVPS_RGN_CANVAS_INFO_T *ptCanvas, AX_IVPS_GDI_ATTR_T tAttr, AX_IVPS_RECT_T tRect) {
    SERILAIZER()->input()->serialize(ptCanvas, tAttr, tRect);
    AX_S32 ret = initialize_random<AX_S32>();
    SERILAIZER()->output()->serialize(ret);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_IVPS_Dewarp(const AX_VIDEO_FRAME_T *ptSrc, AX_VIDEO_FRAME_T *ptDst, const AX_IVPS_DEWARP_ATTR_T *ptAttr) {
    SERILAIZER()->input()->serialize(ptSrc, ptDst, ptAttr);
    AX_S32 ret = initialize_random<AX_S32>();
    SERILAIZER()->output()->serialize(ret);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_PyraLite_Gen(const AX_PYRA_FRAME_T *tSrcFrame, AX_PYRA_FRAME_T *tDstFrame, AX_BOOL bMaskFlag) {
    SERILAIZER()->input()->serialize(tSrcFrame, tDstFrame, bMaskFlag);
    AX_S32 ret = initialize_random<AX_S32>();
    SERILAIZER()->output()->serialize(ret);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_PyraLite_Rcn(const AX_PYRA_FRAME_T *tSrcFrame, AX_PYRA_FRAME_T *tDstFrame, AX_BOOL bBottom) {
    SERILAIZER()->input()->serialize(tSrcFrame, tDstFrame, bBottom);
    AX_S32 ret = initialize_random<AX_S32>();
    SERILAIZER()->output()->serialize(ret);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_IVPS_GdcWorkCreate(GDC_HANDLE *pGdcHandle) {
    SERILAIZER()->input()->serialize();
    AX_S32 ret = 0;
    *pGdcHandle = initialize_random<GDC_HANDLE>();
    SERILAIZER()->output()->serialize(ret, *pGdcHandle);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_IVPS_GdcWorkAttrSet(GDC_HANDLE nGdcHandle, const AX_IVPS_GDC_ATTR_T *ptGdcAttr) {
    SERILAIZER()->input()->serialize(nGdcHandle, ptGdcAttr);
    AX_S32 ret = initialize_random<AX_S32>();
    SERILAIZER()->output()->serialize(ret);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_IVPS_GdcWorkRun(GDC_HANDLE nGdcHandle, const AX_VIDEO_FRAME_T *ptSrc, AX_VIDEO_FRAME_T *ptDst) {
    SERILAIZER()->input()->serialize(nGdcHandle, ptSrc, ptDst);
    AX_S32 ret = 0;
    SERILAIZER()->output()->serialize(ret);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_IVPS_GdcWorkDestroy(GDC_HANDLE nGdcHandle) {
    SERILAIZER()->input()->serialize(nGdcHandle);
    AX_S32 ret = 0;
    SERILAIZER()->output()->serialize(ret);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_IVPS_FisheyePointQueryDst2Src(AX_IVPS_POINT_NICE_T *ptSrcPoint, const AX_IVPS_POINT_NICE_T *ptDstPoint, AX_U16 nInputW, AX_U16 nInputH, AX_U8 nRgnIdx, const AX_IVPS_FISHEYE_ATTR_T *ptFisheyeAttr) {
    AX_S32 ret = 0;
    SERILAIZER()->input()->serialize(ptDstPoint, nInputW, nInputH, nRgnIdx, ptFisheyeAttr);
    // *ptDstPoint = initialize_random<AX_IVPS_POINT_NICE_T>();
    ptSrcPoint->fX = 3;
    ptSrcPoint->fY = 3;
    SERILAIZER()->output()->serialize(ret, ptDstPoint);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_IVPS_FisheyePointQuerySrc2Dst(AX_IVPS_POINT_NICE_T *ptDstPoint, const AX_IVPS_POINT_NICE_T *ptSrcPoint, AX_U16 nInputW, AX_U16 nInputH, AX_U8 nRgnIdx, const AX_IVPS_FISHEYE_ATTR_T *ptFisheyeAttr) {
    SERILAIZER()->input()->serialize(ptSrcPoint, nInputW, nInputH, nRgnIdx, ptFisheyeAttr);
    AX_S32 ret = 0;
    // *ptDstPoint = initialize_random<AX_IVPS_POINT_NICE_T>();
    ptDstPoint->fX = 3;
    ptDstPoint->fY = 3;
    SERILAIZER()->output()->serialize(ret, ptDstPoint);
    return ret;
}