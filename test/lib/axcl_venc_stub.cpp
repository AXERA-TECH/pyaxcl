#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <vector>
#include "axcl_venc.h"
#include "randomizer.hpp"
#include "serializer.hpp"

#define CHECK_NULL_POINTER(p) \
    do {                      \
        if (!(p)) {           \
            return -1;        \
        }                     \
    } while (0)

#define CHECK_SMALLER_AND_EQUAL_UINT(threshold, actual) \
    do {                                                \
        if (actual <= threshold) {                      \
            return -1;                                  \
        }                                               \
    } while (0)

#define IMPLEMENT_SERIALIZE(...)                       \
    do {                                               \
        SERILAIZER()->input()->serialize(__VA_ARGS__); \
        AX_S32 ret = initialize_random<AX_S32>();      \
        SERILAIZER()->output()->serialize(ret);        \
        return ret;                                    \
    } while (0)

static AX_VENC_RC_PARAM_T create_random_rc_param();
static AX_VENC_CHN_ATTR_T create_random_chn_attr();

AXCL_EXPORT AX_S32 AXCL_VENC_Init(const AX_VENC_MOD_ATTR_T *pstModAttr) {
    IMPLEMENT_SERIALIZE(pstModAttr);
}

AXCL_EXPORT AX_S32 AXCL_VENC_Deinit() {
    IMPLEMENT_SERIALIZE();
}

AXCL_EXPORT AX_S32 AXCL_VENC_CreateChn(VENC_CHN VeChn, const AX_VENC_CHN_ATTR_T *pstAttr) {
    IMPLEMENT_SERIALIZE(VeChn, pstAttr);
}

AXCL_EXPORT AX_S32 AXCL_VENC_CreateChnEx(VENC_CHN *pVeChn, const AX_VENC_CHN_ATTR_T *pstAttr) {
    SERILAIZER()->input()->serialize(pstAttr);
    *pVeChn = initialize_random<VENC_CHN>();
    AX_S32 ret = 0;
    SERILAIZER()->output()->serialize(ret, *pVeChn);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_VENC_DestroyChn(VENC_CHN VeChn) {
    IMPLEMENT_SERIALIZE(VeChn);
}

AXCL_EXPORT AX_S32 AXCL_VENC_SendFrame(VENC_CHN VeChn, const AX_VIDEO_FRAME_INFO_T *pstFrame, AX_S32 s32MilliSec) {
    IMPLEMENT_SERIALIZE(VeChn, pstFrame, s32MilliSec);
}

AXCL_EXPORT AX_S32 AXCL_VENC_SendFrameEx(VENC_CHN VeChn, const AX_USER_FRAME_INFO_T *pstFrame, AX_S32 s32MilliSec) {
    IMPLEMENT_SERIALIZE(VeChn, pstFrame, s32MilliSec);
}

AXCL_EXPORT AX_S32 AXCL_VENC_SelectGrp(VENC_GRP grpId, AX_CHN_STREAM_STATUS_T *pstChnStrmState, AX_S32 s32MilliSec) {
    SERILAIZER()->input()->serialize(grpId, s32MilliSec);

    memset(pstChnStrmState, 0, sizeof(AX_CHN_STREAM_STATUS_T));
    pstChnStrmState->u32TotalChnNum = initialize_random<AX_U32>();
    for (int i = 0; i < MAX_VENC_CHN_NUM; ++i) {
        pstChnStrmState->au32ChnIndex[i] = initialize_random<AX_U32>();
        pstChnStrmState->aenChnCodecType[i] = PT_H264;
    }

    AX_S32 ret = 0;
    SERILAIZER()->output()->serialize(ret, *pstChnStrmState);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_VENC_SelectClearGrp(VENC_GRP grpId) {
    IMPLEMENT_SERIALIZE(grpId);
}

AXCL_EXPORT AX_S32 AXCL_VENC_SelectGrpAddChn(VENC_GRP grpId, VENC_CHN VeChn) {
    IMPLEMENT_SERIALIZE(grpId, VeChn);
}

AXCL_EXPORT AX_S32 AXCL_VENC_SelectGrpDeleteChn(VENC_GRP grpId, VENC_CHN VeChn) {
    IMPLEMENT_SERIALIZE(grpId, VeChn);
}

AXCL_EXPORT AX_S32 AXCL_VENC_SelectGrpQuery(VENC_GRP grpId, AX_VENC_SELECT_GRP_PARAM_T *pstGrpInfo) {
    SERILAIZER()->input()->serialize(grpId);

    memset(pstGrpInfo, 0, sizeof(AX_VENC_SELECT_GRP_PARAM_T));
    pstGrpInfo->u16TotalChnNum = initialize_random<AX_U16>();
    for (int i = 0; i < MAX_VENC_CHN_NUM; ++i) {
        pstGrpInfo->u16ChnInGrp[i] = initialize_random<AX_U16>();
    }

    AX_S32 ret = 0;
    SERILAIZER()->output()->serialize(ret, *pstGrpInfo);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_VENC_GetFd(VENC_CHN VeChn) {
    IMPLEMENT_SERIALIZE(VeChn);
}

AXCL_EXPORT AX_S32 AXCL_VENC_GetStream(VENC_CHN VeChn, AX_VENC_STREAM_T *pstStream, AX_S32 s32MilliSec) {
    CHECK_NULL_POINTER(pstStream);

    printf("=====>%s:\n", __func__);
    printf("=====>VeChn[%d]: s32MilliSec: %d\n", VeChn, s32MilliSec);

    // only for test
    pstStream->stPack.ulPhyAddr = 0x1100000;
    pstStream->stPack.pu8Addr = (AX_U8 *)0x1200000;
    pstStream->stPack.u32Len = 123456;
    pstStream->stPack.u64PTS = 1111222233334444;
    pstStream->stPack.u64SeqNum = 666677778889999;
    pstStream->stPack.u64UserData = 111111;

    pstStream->stPack.enType = PT_H264;
    pstStream->stPack.enCodingType = AX_VENC_PREDICTED_FRAME;
    pstStream->stPack.u32TemporalID = 22;
    pstStream->stPack.u32NaluNum = 3;
    pstStream->stPack.stNaluInfo[0].u32NaluLength = 100;
    pstStream->stPack.stNaluInfo[0].unNaluType.enH264EType = AX_H264E_NALU_IDRSLICE;
    pstStream->stPack.stNaluInfo[0].u32NaluOffset = 0;
    pstStream->stPack.stNaluInfo[1].u32NaluLength = 200;
    pstStream->stPack.stNaluInfo[1].unNaluType.enH264EType = AX_H264E_NALU_BSLICE;
    pstStream->stPack.stNaluInfo[1].u32NaluOffset = 100;
    pstStream->stPack.stNaluInfo[0].u32NaluLength = 400;
    pstStream->stPack.stNaluInfo[0].unNaluType.enH264EType = AX_H264E_NALU_PSLICE;
    pstStream->stPack.stNaluInfo[0].u32NaluOffset = 300;

    pstStream->stH264Info.u32PicBytesNum = 1;
    pstStream->stH264Info.u32Inter16x16MbNum = 2;
    pstStream->stH264Info.u32Inter8x8MbNum = 3;
    pstStream->stH264Info.u32Intra16MbNum = 4;
    pstStream->stH264Info.u32Intra8MbNum = 5;
    pstStream->stH264Info.u32Intra4MbNum = 6;
    pstStream->stH264Info.enRefType = AX_BASE_PSLICE_REFBYBASE;
    pstStream->stH264Info.u32UpdateAttrCnt = 7;
    pstStream->stH264Info.u32StartQp = 8;
    pstStream->stH264Info.u32MeanQp = 9;
    pstStream->stH264Info.bPSkip = AX_TRUE;

    pstStream->stAdvanceH264Info.u32ResidualBitNum = 10;
    pstStream->stAdvanceH264Info.u32HeadBitNum = 11;
    pstStream->stAdvanceH264Info.u32MadiVal = 12;
    pstStream->stAdvanceH264Info.u32MadpVal = 13;
    pstStream->stAdvanceH264Info.f64PSNRVal = 14;
    pstStream->stAdvanceH264Info.u32MseLcuCnt = 15;
    pstStream->stAdvanceH264Info.u32MseSum = 16;
    memset(pstStream->stAdvanceH264Info.stSSEInfo, 0x00, sizeof(pstStream->stAdvanceH264Info.stSSEInfo));
    pstStream->stAdvanceH264Info.stSSEInfo[0].bSSEEn = AX_TRUE;
    pstStream->stAdvanceH264Info.stSSEInfo[0].u32SSEVal = 17;
    memset(pstStream->stAdvanceH264Info.u32QpHstgrm, 0x00, sizeof(pstStream->stAdvanceH264Info.u32QpHstgrm));
    pstStream->stAdvanceH264Info.u32QpHstgrm[0] = 18;
    pstStream->stAdvanceH264Info.u32QpHstgrm[1] = 19;
    pstStream->stAdvanceH264Info.u32MoveScene16x16Num = 20;
    pstStream->stAdvanceH264Info.u32MoveSceneBits = 21;

    return AXCL_SUCC;
}

AXCL_EXPORT AX_S32 AXCL_VENC_ReleaseStream(VENC_CHN VeChn, const AX_VENC_STREAM_T *pstStream) {
    CHECK_NULL_POINTER(pstStream);

    printf("=====>%s:\n", __func__);
    printf(
        "=====>VeChn[%d]: ulPhyAddr: 0x%llx, pu8Addr: %p, u32Len: %d, u64PTS: %lld, u64SeqNum: %lld, u64UserData: %lld, enType: %d, "
        "enCodingType: %d, u32TemporalID: %d, u32NaluNum: %d\n",
        VeChn, pstStream->stPack.ulPhyAddr, pstStream->stPack.pu8Addr, pstStream->stPack.u32Len, pstStream->stPack.u64PTS,
        pstStream->stPack.u64SeqNum, pstStream->stPack.u64UserData, pstStream->stPack.enType, pstStream->stPack.enCodingType,
        pstStream->stPack.u32TemporalID, pstStream->stPack.u32NaluNum);

    printf("=====>VeChn[%d]: stNaluInfo: u32NaluNum: %d, [0]: [unNaluType: %d, u32NaluOffset: %d, u32NaluLength: %d]\n", VeChn,
           pstStream->stPack.u32NaluNum, pstStream->stPack.stNaluInfo[0].unNaluType.enH264EType,
           pstStream->stPack.stNaluInfo[0].u32NaluOffset, pstStream->stPack.stNaluInfo[0].u32NaluLength);

    printf(
        "=====>VeChn[%d]: stH264Info: u32PicBytesNum: %d, u32Inter16x16MbNum: %d, u32Inter8x8MbNum: %d, u32Intra16MbNum: %d, "
        "u32Intra8MbNum: %d, u32Intra4MbNum: %d, enRefType: %d, u32UpdateAttrCnt: %d, u32StartQp: %d, u32MeanQp: %d, bPSkip: %d\n",
        VeChn, pstStream->stH264Info.u32PicBytesNum, pstStream->stH264Info.u32Inter16x16MbNum, pstStream->stH264Info.u32Inter8x8MbNum,
        pstStream->stH264Info.u32Intra16MbNum, pstStream->stH264Info.u32Intra8MbNum, pstStream->stH264Info.u32Intra4MbNum,
        pstStream->stH264Info.enRefType, pstStream->stH264Info.u32UpdateAttrCnt, pstStream->stH264Info.u32StartQp,
        pstStream->stH264Info.u32MeanQp, pstStream->stH264Info.bPSkip);

    printf(
        "=====>VeChn[%d]: stAdvanceH264Info: u32ResidualBitNum: %d, u32HeadBitNum: %d, u32MadiVal: %d, u32MadpVal: %d, f64PSNRVal: %f, "
        "u32MseLcuCnt: %d, u32MseSum: %d, stSSEInfo[0]: [bSSEEn: %d, u32SSEVal: %d], u32QpHstgrm: [0]%d, [1]%d, u32MoveScene16x16Num: %d, "
        "u32MoveSceneBits: %d\n",
        VeChn, pstStream->stAdvanceH264Info.u32ResidualBitNum, pstStream->stAdvanceH264Info.u32HeadBitNum,
        pstStream->stAdvanceH264Info.u32MadiVal, pstStream->stAdvanceH264Info.u32MadpVal, pstStream->stAdvanceH264Info.f64PSNRVal,
        pstStream->stAdvanceH264Info.u32MseLcuCnt, pstStream->stAdvanceH264Info.u32MseSum, pstStream->stAdvanceH264Info.stSSEInfo[0].bSSEEn,
        pstStream->stAdvanceH264Info.stSSEInfo[0].u32SSEVal, pstStream->stAdvanceH264Info.u32QpHstgrm[0],
        pstStream->stAdvanceH264Info.u32QpHstgrm[1], pstStream->stAdvanceH264Info.u32MoveScene16x16Num,
        pstStream->stAdvanceH264Info.u32MoveSceneBits);

    return AXCL_SUCC;
}

AXCL_EXPORT AX_S32 AXCL_VENC_GetStreamBufInfo(VENC_CHN VeChn, AX_VENC_STREAM_BUF_INFO_T *pstStreamBufInfo) {
    SERILAIZER()->input()->serialize(VeChn);

    memset(pstStreamBufInfo, 0, sizeof(AX_VENC_STREAM_BUF_INFO_T));
    pstStreamBufInfo->u64PhyAddr = initialize_random<AX_U64>();
    pstStreamBufInfo->pUserAddr = reinterpret_cast<AX_VOID *>(initialize_random<AX_U64>());
    pstStreamBufInfo->u32BufSize = initialize_random<AX_U32>();
    AX_S32 ret = 0;
    SERILAIZER()->output()->serialize(ret, *pstStreamBufInfo);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_VENC_StartRecvFrame(VENC_CHN VeChn, const AX_VENC_RECV_PIC_PARAM_T *pstRecvParam) {
    IMPLEMENT_SERIALIZE(VeChn, pstRecvParam);
}

AXCL_EXPORT AX_S32 AXCL_VENC_StopRecvFrame(VENC_CHN VeChn) {
    IMPLEMENT_SERIALIZE(VeChn);
}

AXCL_EXPORT AX_S32 AXCL_VENC_ResetChn(VENC_CHN VeChn) {
    IMPLEMENT_SERIALIZE(VeChn);
}

AXCL_EXPORT AX_S32 AXCL_VENC_SetRoiAttr(VENC_CHN VeChn, const AX_VENC_ROI_ATTR_T *pstRoiAttr) {
    IMPLEMENT_SERIALIZE(VeChn, pstRoiAttr);
}

AXCL_EXPORT AX_S32 AXCL_VENC_GetRoiAttr(VENC_CHN VeChn, AX_U32 u32Index, AX_VENC_ROI_ATTR_T *pstRoiAttr) {
    SERILAIZER()->input()->serialize(VeChn, u32Index);

    memset(pstRoiAttr, 0, sizeof(AX_VENC_ROI_ATTR_T));
    pstRoiAttr->u32Index = initialize_random<AX_U32>();
    pstRoiAttr->bEnable = initialize_random<AX_BOOL>();
    pstRoiAttr->bAbsQp = initialize_random<AX_BOOL>();
    pstRoiAttr->s32RoiQp = initialize_random<AX_S32>();
    pstRoiAttr->stRoiArea.u32X = initialize_random<AX_U32>();
    pstRoiAttr->stRoiArea.u32Y = initialize_random<AX_U32>();
    pstRoiAttr->stRoiArea.u32Width = initialize_random<AX_U32>();
    pstRoiAttr->stRoiArea.u32Width = initialize_random<AX_U32>();
    AX_S32 ret = 0;
    SERILAIZER()->output()->serialize(ret, *pstRoiAttr);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_VENC_SetRcParam(VENC_CHN VeChn, const AX_VENC_RC_PARAM_T *pstRcParam) {
    IMPLEMENT_SERIALIZE(VeChn, pstRcParam);
}

AXCL_EXPORT AX_S32 AXCL_VENC_GetRcParam(VENC_CHN VeChn, AX_VENC_RC_PARAM_T *pstRcParam) {
    SERILAIZER()->input()->serialize(VeChn);

    *pstRcParam = create_random_rc_param();
    AX_S32 ret = 0;
    SERILAIZER()->output()->serialize(ret, *pstRcParam);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_VENC_SetModParam(AX_VENC_ENCODER_TYPE_E enVencType, const AX_VENC_MOD_PARAM_T *pstModParam) {
    IMPLEMENT_SERIALIZE(enVencType, pstModParam);
}

AXCL_EXPORT AX_S32 AXCL_VENC_GetModParam(AX_VENC_ENCODER_TYPE_E enVencType, AX_VENC_MOD_PARAM_T *pstModParam) {
    SERILAIZER()->input()->serialize(enVencType);

    memset(pstModParam, 0, sizeof(AX_VENC_MOD_PARAM_T));
    pstModParam->enVencHwClk = create_enum_random_instance<AX_VENC_HW_CLK_E>(AX_VENC_CLK_FREQUENCY_624M, AX_VENC_CLK_FREQUENCY_BUTT);
    AX_S32 ret = 0;
    SERILAIZER()->output()->serialize(ret, *pstModParam);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_VENC_SetVuiParam(VENC_CHN VeChn, const AX_VENC_VUI_PARAM_T *pstVuiParam) {
    IMPLEMENT_SERIALIZE(VeChn, pstVuiParam);
}

AXCL_EXPORT AX_S32 AXCL_VENC_GetVuiParam(VENC_CHN VeChn, AX_VENC_VUI_PARAM_T *pstVuiParam) {
    SERILAIZER()->input()->serialize(VeChn);

    memset(pstVuiParam, 0, sizeof(AX_VENC_VUI_PARAM_T));
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

AXCL_EXPORT AX_S32 AXCL_VENC_SetChnAttr(VENC_CHN VeChn, const AX_VENC_CHN_ATTR_T *pstChnAttr) {
    IMPLEMENT_SERIALIZE(VeChn, pstChnAttr);
}

AXCL_EXPORT AX_S32 AXCL_VENC_GetChnAttr(VENC_CHN VeChn, AX_VENC_CHN_ATTR_T *pstChnAttr) {
    SERILAIZER()->input()->serialize(VeChn);

    *pstChnAttr = create_random_chn_attr();
    AX_S32 ret = 0;
    SERILAIZER()->output()->serialize(ret, *pstChnAttr);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_VENC_SetRateJamStrategy(VENC_CHN VeChn, const AX_VENC_RATE_JAM_CFG_T *pstRateJamParam) {
    IMPLEMENT_SERIALIZE(VeChn, pstRateJamParam);
}

AXCL_EXPORT AX_S32 AXCL_VENC_GetRateJamStrategy(VENC_CHN VeChn, AX_VENC_RATE_JAM_CFG_T *pstRateJamParam) {
    const std::vector<AX_VENC_DROPFRAME_MODE_E> drop_frm_modes = {AX_VENC_DROPFRM_NORMAL, AX_VENC_DROPFRM_PSKIP};

    SERILAIZER()->input()->serialize(VeChn);

    memset(pstRateJamParam, 0, sizeof(AX_VENC_RATE_JAM_CFG_T));
    pstRateJamParam->bDropFrmEn = initialize_random<AX_BOOL>();
    pstRateJamParam->u32DropFrmThrBps = initialize_random<AX_U32>();
    pstRateJamParam->enDropFrmMode = choose_random_from_array<AX_VENC_DROPFRAME_MODE_E>(drop_frm_modes);
    pstRateJamParam->u32EncFrmGaps = initialize_random<AX_U32>();
    AX_S32 ret = 0;
    SERILAIZER()->output()->serialize(ret, *pstRateJamParam);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_VENC_SetSuperFrameStrategy(VENC_CHN VeChn, const AX_VENC_SUPERFRAME_CFG_T *pstSuperFrameCfg) {
    IMPLEMENT_SERIALIZE(VeChn, pstSuperFrameCfg);
}

AXCL_EXPORT AX_S32 AXCL_VENC_GetSuperFrameStrategy(VENC_CHN VeChn, AX_VENC_SUPERFRAME_CFG_T *pstSuperFrameCfg) {
    const std::vector<AX_VENC_RC_PRIORITY_E> priorities = {AX_VENC_RC_PRIORITY_FRAMEBITS_FIRST, AX_VENC_RC_PRIORITY_BITRATE_FIRST};

    SERILAIZER()->input()->serialize(VeChn);

    memset(pstSuperFrameCfg, 0, sizeof(AX_VENC_SUPERFRAME_CFG_T));
    pstSuperFrameCfg->bStrategyEn = initialize_random<AX_BOOL>();
    pstSuperFrameCfg->u32SuperIFrmBitsThr = initialize_random<AX_U32>();
    pstSuperFrameCfg->u32SuperPFrmBitsThr = initialize_random<AX_U32>();
    pstSuperFrameCfg->u32SuperBFrmBitsThr = initialize_random<AX_U32>();
    pstSuperFrameCfg->enRcPriority = choose_random_from_array<AX_VENC_RC_PRIORITY_E>(priorities);

    AX_S32 ret = 0;
    SERILAIZER()->output()->serialize(ret, *pstSuperFrameCfg);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_VENC_SetIntraRefresh(VENC_CHN VeChn, const AX_VENC_INTRA_REFRESH_T *pstIntraRefresh) {
    IMPLEMENT_SERIALIZE(VeChn, pstIntraRefresh);
}

AXCL_EXPORT AX_S32 AXCL_VENC_GetIntraRefresh(VENC_CHN VeChn, AX_VENC_INTRA_REFRESH_T *pstIntraRefresh) {
    const std::vector<AX_VENC_INTRA_REFRESH_MODE_E> modes = {AX_VENC_INTRA_REFRESH_ROW, AX_VENC_INTRA_REFRESH_COLUMN};

    SERILAIZER()->input()->serialize(VeChn);

    memset(pstIntraRefresh, 0, sizeof(AX_VENC_INTRA_REFRESH_T));
    pstIntraRefresh->bRefresh = initialize_random<AX_BOOL>();
    pstIntraRefresh->u32RefreshNum = initialize_random<AX_U32>();
    pstIntraRefresh->u32ReqIQp = initialize_random<AX_U32>();
    pstIntraRefresh->enIntraRefreshMode = choose_random_from_array<AX_VENC_INTRA_REFRESH_MODE_E>(modes);

    AX_S32 ret = 0;
    SERILAIZER()->output()->serialize(ret, *pstIntraRefresh);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_VENC_SetUsrData(VENC_CHN VeChn, const AX_VENC_USR_DATA_T *pstUsrData) {
    IMPLEMENT_SERIALIZE(VeChn, pstUsrData);
}

AXCL_EXPORT AX_S32 AXCL_VENC_GetUsrData(VENC_CHN VeChn, AX_VENC_USR_DATA_T *pstUsrData) {
    SERILAIZER()->input()->serialize(VeChn, pstUsrData);

    memset(pstUsrData, 0, sizeof(AX_VENC_USR_DATA_T));
    pstUsrData->bEnable = initialize_random<AX_BOOL>();
    pstUsrData->u32DataSize = initialize_random<AX_U32>();
    pstUsrData->pu8UsrData = reinterpret_cast<AX_U8 *>(initialize_random<AX_U64>());

    AX_S32 ret = 0;
    SERILAIZER()->output()->serialize(ret, *pstUsrData);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_VENC_SetSliceSplit(VENC_CHN VeChn, const AX_VENC_SLICE_SPLIT_T *pstSliceSplit) {
    IMPLEMENT_SERIALIZE(VeChn, pstSliceSplit);
}

AXCL_EXPORT AX_S32 AXCL_VENC_GetSliceSplit(VENC_CHN VeChn, AX_VENC_SLICE_SPLIT_T *pstSliceSplit) {
    SERILAIZER()->input()->serialize(VeChn);

    memset(pstSliceSplit, 0, sizeof(AX_VENC_SLICE_SPLIT_T));
    pstSliceSplit->bSplit = initialize_random<AX_BOOL>();
    pstSliceSplit->u32LcuLineNum = initialize_random<AX_U32>();

    AX_S32 ret = 0;
    SERILAIZER()->output()->serialize(ret, *pstSliceSplit);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_VENC_RequestIDR(VENC_CHN VeChn, AX_BOOL bInstant) {
    IMPLEMENT_SERIALIZE(VeChn, bInstant);
}

AXCL_EXPORT AX_S32 AXCL_VENC_QueryStatus(VENC_CHN VeChn, AX_VENC_CHN_STATUS_T *pstStatus) {
    SERILAIZER()->input()->serialize(VeChn);

    memset(pstStatus, 0, sizeof(AX_VENC_CHN_STATUS_T));
    pstStatus->u32LeftPics = initialize_random<AX_U32>();
    pstStatus->u32LeftStreamBytes = initialize_random<AX_U32>();
    pstStatus->u32LeftStreamFrames = initialize_random<AX_U32>();
    pstStatus->u32CurPacks = initialize_random<AX_U32>();
    pstStatus->u32LeftRecvPics = initialize_random<AX_U32>();
    pstStatus->u32LeftEncPics = initialize_random<AX_U32>();
    pstStatus->u32Reserved = initialize_random<AX_U32>();

    AX_S32 ret = 0;
    SERILAIZER()->output()->serialize(ret, *pstStatus);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_VENC_SetJpegParam(VENC_CHN VeChn, const AX_VENC_JPEG_PARAM_T *pstJpegParam) {
    IMPLEMENT_SERIALIZE(VeChn, pstJpegParam);
}

AXCL_EXPORT AX_S32 AXCL_VENC_GetJpegParam(VENC_CHN VeChn, AX_VENC_JPEG_PARAM_T *pstJpegParam) {
    SERILAIZER()->input()->serialize(VeChn);

    memset(pstJpegParam, 0, sizeof(AX_VENC_JPEG_PARAM_T));
    pstJpegParam->u32Qfactor = initialize_random<AX_U32>();
    for (auto &m : pstJpegParam->u8YQt) {
        m = initialize_random<AX_U8>();
    }
    for (auto &m : pstJpegParam->u8CbCrQt) {
        m = initialize_random<AX_U8>();
    }
    pstJpegParam->bEnableRoi = initialize_random<AX_BOOL>();
    pstJpegParam->bSaveNonRoiQt = initialize_random<AX_BOOL>();
    pstJpegParam->u32RoiQfactor = initialize_random<AX_U32>();
    for (auto &m : pstJpegParam->u8RoiYQt) {
        m = initialize_random<AX_U8>();
    }
    for (auto &m : pstJpegParam->u8RoiCbCrQt) {
        m = initialize_random<AX_U8>();
    }
    for (auto &m : pstJpegParam->bEnable) {
        m = initialize_random<AX_BOOL>();
    }
    for (auto &m : pstJpegParam->stRoiArea) {
        m.u32X = initialize_random<AX_U32>();
        m.u32Y = initialize_random<AX_U32>();
        m.u32Width = initialize_random<AX_U32>();
        m.u32Height = initialize_random<AX_U32>();
    }
    pstJpegParam->u32MCUPerECS = initialize_random<AX_U32>();
    pstJpegParam->bDblkEnable = initialize_random<AX_BOOL>();

    AX_S32 ret = 0;
    SERILAIZER()->output()->serialize(ret, *pstJpegParam);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_VENC_JpegEncodeOneFrame(AX_JPEG_ENCODE_ONCE_PARAMS_T *pstJpegParam) {
    SERILAIZER()->input()->serialize(pstJpegParam);

    pstJpegParam->ulPhyAddr = initialize_random<AX_U64>();
    pstJpegParam->pu8Addr = reinterpret_cast<AX_U8 *>(initialize_random<AX_U64>());
    pstJpegParam->u32Len = initialize_random<AX_U32>();
    AX_S32 ret = 0;
    SERILAIZER()->output()->serialize(ret, *pstJpegParam);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_VENC_JpegGetThumbnail(const AX_VOID *pRawData, AX_VOID *pThumbData, AX_U32 *pThumbSize) {
    return AXCL_SUCC;
}

static AX_VENC_RC_MODE_E create_random_rc_mode() {
    const std::vector<AX_VENC_RC_MODE_E> rc_modes = {AX_VENC_RC_MODE_H264CBR,    AX_VENC_RC_MODE_H264VBR,  AX_VENC_RC_MODE_H264AVBR,
                                                     AX_VENC_RC_MODE_H264QVBR,   AX_VENC_RC_MODE_H264CVBR, AX_VENC_RC_MODE_H264FIXQP,
                                                     AX_VENC_RC_MODE_H264QPMAP,  AX_VENC_RC_MODE_MJPEGCBR, AX_VENC_RC_MODE_MJPEGVBR,
                                                     AX_VENC_RC_MODE_MJPEGFIXQP, AX_VENC_RC_MODE_H265CBR,  AX_VENC_RC_MODE_H265VBR,
                                                     AX_VENC_RC_MODE_H265AVBR,   AX_VENC_RC_MODE_H265QVBR, AX_VENC_RC_MODE_H265CVBR,
                                                     AX_VENC_RC_MODE_H265FIXQP,  AX_VENC_RC_MODE_H265QPMAP};

    return choose_random_from_array<AX_VENC_RC_MODE_E>(rc_modes);
}

static AX_VENC_QPMAP_META_T create_random_qpmap_meta() {
    AX_VENC_QPMAP_META_T meta = {};
    meta.enCtbRcMode = create_enum_random_instance<AX_VENC_RC_CTBRC_MODE_E>(AX_VENC_RC_CTBRC_DISABLE, AX_VENC_RC_CTBRC_BUTT);
    meta.enQpmapQpType = create_enum_random_instance<AX_VENC_QPMAP_QP_TYPE_E>(AX_VENC_QPMAP_QP_DISABLE, AX_VENC_QPMAP_QP_BUTT);
    meta.enQpmapBlockType = create_enum_random_instance<AX_VENC_QPMAP_BLOCK_TYPE_E>(AX_VENC_QPMAP_BLOCK_DISABLE, AX_VENC_QPMAP_BLOCK_BUTT);
    meta.enQpmapBlockUnit =
        create_enum_random_instance<AX_VENC_QPMAP_BLOCK_UNIT_E>(AX_VENC_QPMAP_BLOCK_UNIT_NONE, AX_VENC_QPMAP_BLOCK_UNIT_BUTT);

    return meta;
}

static AX_VENC_H264_CBR_T create_random_h264_cbr() {
    AX_VENC_H264_CBR_T cbr = {};
    cbr.u32Gop = initialize_random<AX_U32>();
    cbr.u32StatTime = initialize_random<AX_U32>();
    cbr.u32BitRate = initialize_random<AX_U32>();
    cbr.u32MaxQp = initialize_random<AX_U32>();
    cbr.u32MinQp = initialize_random<AX_U32>();
    cbr.u32MaxIQp = initialize_random<AX_U32>();
    cbr.u32MinIQp = initialize_random<AX_U32>();
    cbr.u32MaxIprop = initialize_random<AX_U32>();
    cbr.u32MinIprop = initialize_random<AX_U32>();
    cbr.s32IntraQpDelta = initialize_random<AX_S32>();
    cbr.u32IdrQpDeltaRange = initialize_random<AX_U32>();
    cbr.stQpmapInfo = create_random_qpmap_meta();

    return cbr;
}

static AX_VENC_H264_VBR_T create_random_h264_vbr() {
    AX_VENC_H264_VBR_T vbr = {};
    vbr.u32Gop = initialize_random<AX_U32>();
    vbr.u32StatTime = initialize_random<AX_U32>();
    vbr.u32MaxBitRate = initialize_random<AX_U32>();
    vbr.enVQ = create_enum_random_instance<AX_VENC_VBR_QUALITY_LEVEL_E>(AX_VENC_VBR_QUALITY_LEVEL_INV, AX_VENC_VBR_QUALITY_LEVEL_BUTT);
    vbr.u32MaxQp = initialize_random<AX_U32>();
    vbr.u32MinQp = initialize_random<AX_U32>();
    vbr.u32MaxIQp = initialize_random<AX_U32>();
    vbr.u32MinIQp = initialize_random<AX_U32>();
    vbr.s32IntraQpDelta = initialize_random<AX_S32>();
    vbr.u32IdrQpDeltaRange = initialize_random<AX_U32>();
    vbr.stQpmapInfo = create_random_qpmap_meta();
    vbr.u32ChangePos = initialize_random<AX_U32>();

    return vbr;
}

static AX_VENC_H264_CVBR_T create_random_h264_cvbr() {
    AX_VENC_H264_CVBR_T cvbr = {};
    cvbr.u32Gop = initialize_random<AX_U32>();
    cvbr.u32StatTime = initialize_random<AX_U32>();
    cvbr.u32MaxQp = initialize_random<AX_U32>();
    cvbr.u32MinQp = initialize_random<AX_U32>();
    cvbr.u32MaxIQp = initialize_random<AX_U32>();
    cvbr.u32MinIQp = initialize_random<AX_U32>();
    cvbr.u32MinQpDelta = initialize_random<AX_U32>();
    cvbr.u32MaxQpDelta = initialize_random<AX_U32>();
    cvbr.u32MaxIprop = initialize_random<AX_U32>();
    cvbr.u32MinIprop = initialize_random<AX_U32>();
    cvbr.u32MaxBitRate = initialize_random<AX_U32>();
    cvbr.u32ShortTermStatTime = initialize_random<AX_U32>();
    cvbr.u32LongTermStatTime = initialize_random<AX_U32>();
    cvbr.u32LongTermMinBitrate = initialize_random<AX_U32>();
    cvbr.stQpmapInfo = create_random_qpmap_meta();
    cvbr.u32ExtraBitPercent = initialize_random<AX_U32>();
    cvbr.u32LongTermStatTimeUnit = initialize_random<AX_U32>();
    cvbr.s32IntraQpDelta = initialize_random<AX_S32>();
    cvbr.u32IdrQpDeltaRange = initialize_random<AX_U32>();

    return cvbr;
}

static AX_VENC_H264_AVBR_T create_random_h264_avbr() {
    AX_VENC_H264_AVBR_T avbr = {};
    avbr.u32Gop = initialize_random<AX_U32>();
    avbr.u32StatTime = initialize_random<AX_U32>();
    avbr.u32MaxBitRate = initialize_random<AX_U32>();
    avbr.u32MaxQp = initialize_random<AX_U32>();
    avbr.u32MinQp = initialize_random<AX_U32>();
    avbr.u32MaxIQp = initialize_random<AX_U32>();
    avbr.u32MinIQp = initialize_random<AX_U32>();
    avbr.s32IntraQpDelta = initialize_random<AX_S32>();
    avbr.u32IdrQpDeltaRange = initialize_random<AX_U32>();
    avbr.stQpmapInfo = create_random_qpmap_meta();
    avbr.u32ChangePos = initialize_random<AX_U32>();
    avbr.u32MinStillPercent = initialize_random<AX_U32>();
    avbr.u32MaxStillQp = initialize_random<AX_U32>();

    return avbr;
}

static AX_VENC_H264_FIXQP_T create_random_h264_fixqp() {
    AX_VENC_H264_FIXQP_T fixqp = {};
    fixqp.u32Gop = initialize_random<AX_U32>();
    fixqp.u32IQp = initialize_random<AX_U32>();
    fixqp.u32PQp = initialize_random<AX_U32>();
    fixqp.u32BQp = initialize_random<AX_U32>();

    return fixqp;
}

static AX_VENC_H264_QPMAP_T create_random_h264_qpmap() {
    AX_VENC_H264_QPMAP_T qpmap = {};
    qpmap.u32Gop = initialize_random<AX_U32>();
    qpmap.u32StatTime = initialize_random<AX_U32>();
    qpmap.u32TargetBitRate = initialize_random<AX_U32>();
    qpmap.stQpmapInfo = create_random_qpmap_meta();

    return qpmap;
}

static AX_VENC_H264_QVBR_T create_random_h264_qvbr() {
    AX_VENC_H264_QVBR_T qvbr = {};
    qvbr.u32Gop = initialize_random<AX_U32>();
    qvbr.u32StatTime = initialize_random<AX_U32>();
    qvbr.u32TargetBitRate = initialize_random<AX_U32>();

    return qvbr;
}

static AX_VENC_H265_QPMAP_T create_random_h265_qmap() {
    AX_VENC_H265_QPMAP_T qpmap = {};
    qpmap.u32Gop = initialize_random<AX_U32>();
    qpmap.u32StatTime = initialize_random<AX_U32>();
    qpmap.u32TargetBitRate = initialize_random<AX_U32>();
    qpmap.stQpmapInfo = create_random_qpmap_meta();

    return qpmap;
}

static AX_VENC_H265_CBR_T create_random_h265_cbr() {
    return create_random_h264_cbr();
}

static AX_VENC_H265_VBR_T create_random_h265_vbr() {
    return create_random_h264_vbr();
}

static AX_VENC_H265_AVBR_T create_random_h265_avbr() {
    return create_random_h264_avbr();
}

static AX_VENC_H265_FIXQP_T create_random_h265_fixqp() {
    return create_random_h264_fixqp();
}

static AX_VENC_H265_QVBR_T create_random_h265_qvbr() {
    return create_random_h264_qvbr();
}

static AX_VENC_H265_CVBR_T create_random_h265_cvbr() {
    return create_random_h264_cvbr();
}

static AX_VENC_MJPEG_FIXQP_T create_random_mjpeg_fixqp() {
    AX_VENC_MJPEG_FIXQP_T fixqp = {};
    fixqp.s32FixedQp = initialize_random<AX_S32>();

    return fixqp;
}

static AX_VENC_MJPEG_CBR_T create_random_mjpeg_cbr() {
    AX_VENC_MJPEG_CBR_T cbr = {};
    cbr.u32StatTime = initialize_random<AX_U32>();
    cbr.u32BitRate = initialize_random<AX_U32>();
    cbr.u32MaxQp = initialize_random<AX_U32>();
    cbr.u32MinQp = initialize_random<AX_U32>();

    return cbr;
}

static AX_VENC_MJPEG_VBR_T create_random_mjpeg_vbr() {
    AX_VENC_MJPEG_VBR_T vbr = {};
    vbr.u32StatTime = initialize_random<AX_U32>();
    vbr.u32MaxBitRate = initialize_random<AX_U32>();
    vbr.u32MaxQp = initialize_random<AX_U32>();
    vbr.u32MinQp = initialize_random<AX_U32>();

    return vbr;
}

static AX_VENC_RC_PARAM_T create_random_rc_param() {
    AX_VENC_RC_PARAM_T param = {};
    param.u32RowQpDelta = initialize_random<AX_U32>();
    param.s32FirstFrameStartQp = initialize_random<AX_S32>();
    param.stSceneChangeDetect.bDetectSceneChange = initialize_random<AX_BOOL>();
    param.stSceneChangeDetect.bAdaptiveInsertIDRFrame = initialize_random<AX_BOOL>();
    param.enRcMode = create_random_rc_mode();
    param.stFrameRate.fSrcFrameRate = initialize_random<AX_F32>();
    param.stFrameRate.fDstFrameRate = initialize_random<AX_F32>();
    switch (param.enRcMode) {
        case AX_VENC_RC_MODE_H264CBR:
            param.stH264Cbr = create_random_h264_cbr();
            break;
        case AX_VENC_RC_MODE_H264VBR:
            param.stH264Vbr = create_random_h264_vbr();
            break;
        case AX_VENC_RC_MODE_H264AVBR:
            param.stH264AVbr = create_random_h264_avbr();
            break;
        case AX_VENC_RC_MODE_H264QVBR:
            param.stH264QVbr = create_random_h264_qvbr();
            break;
        case AX_VENC_RC_MODE_H264CVBR:
            param.stH264CVbr = create_random_h264_cvbr();
            break;
        case AX_VENC_RC_MODE_H264FIXQP:
            param.stH264FixQp = create_random_h264_fixqp();
            break;
        case AX_VENC_RC_MODE_H264QPMAP:
            param.stH264QpMap = create_random_h264_qpmap();
            break;
        case AX_VENC_RC_MODE_MJPEGCBR:
            param.stMjpegCbr = create_random_mjpeg_cbr();
            break;
        case AX_VENC_RC_MODE_MJPEGVBR:
            param.stMjpegVbr = create_random_mjpeg_vbr();
            break;
        case AX_VENC_RC_MODE_MJPEGFIXQP:
            param.stMjpegFixQp = create_random_mjpeg_fixqp();
            break;
        case AX_VENC_RC_MODE_H265CBR:
            param.stH265Cbr = create_random_h265_cbr();
            break;
        case AX_VENC_RC_MODE_H265VBR:
            param.stH265Vbr = create_random_h265_vbr();
            break;
        case AX_VENC_RC_MODE_H265AVBR:
            param.stH265AVbr = create_random_h265_avbr();
            break;
        case AX_VENC_RC_MODE_H265QVBR:
            param.stH265QVbr = create_random_h265_qvbr();
            break;
        case AX_VENC_RC_MODE_H265CVBR:
            param.stH265CVbr = create_random_h265_cvbr();
            break;
        case AX_VENC_RC_MODE_H265FIXQP:
            param.stH265FixQp = create_random_h265_fixqp();
            break;
        case AX_VENC_RC_MODE_H265QPMAP:
            param.stH265QpMap = create_random_h265_qmap();
            break;
        default:
            break;
    }

    return param;
}

static AX_VENC_RC_ATTR_T create_random_rc_attr() {
    AX_VENC_RC_ATTR_T rc = {};
    rc.s32FirstFrameStartQp = initialize_random<AX_S32>();
    rc.enRcMode = create_random_rc_mode();
    rc.stFrameRate.fSrcFrameRate = initialize_random<AX_F32>();
    rc.stFrameRate.fDstFrameRate = initialize_random<AX_F32>();
    switch (rc.enRcMode) {
        case AX_VENC_RC_MODE_H264CBR:
            rc.stH264Cbr = create_random_h264_cbr();
            break;
        case AX_VENC_RC_MODE_H264VBR:
            rc.stH264Vbr = create_random_h264_vbr();
            break;
        case AX_VENC_RC_MODE_H264AVBR:
            rc.stH264AVbr = create_random_h264_avbr();
            break;
        case AX_VENC_RC_MODE_H264QVBR:
            rc.stH264QVbr = create_random_h264_qvbr();
            break;
        case AX_VENC_RC_MODE_H264CVBR:
            rc.stH264CVbr = create_random_h264_cvbr();
            break;
        case AX_VENC_RC_MODE_H264FIXQP:
            rc.stH264FixQp = create_random_h264_fixqp();
            break;
        case AX_VENC_RC_MODE_H264QPMAP:
            rc.stH264QpMap = create_random_h264_qpmap();
            break;
        case AX_VENC_RC_MODE_MJPEGCBR:
            rc.stMjpegCbr = create_random_mjpeg_cbr();
            break;
        case AX_VENC_RC_MODE_MJPEGVBR:
            rc.stMjpegVbr = create_random_mjpeg_vbr();
            break;
        case AX_VENC_RC_MODE_MJPEGFIXQP:
            rc.stMjpegFixQp = create_random_mjpeg_fixqp();
            break;
        case AX_VENC_RC_MODE_H265CBR:
            rc.stH265Cbr = create_random_h265_cbr();
            break;
        case AX_VENC_RC_MODE_H265VBR:
            rc.stH265Vbr = create_random_h265_vbr();
            break;
        case AX_VENC_RC_MODE_H265AVBR:
            rc.stH265AVbr = create_random_h265_avbr();
            break;
        case AX_VENC_RC_MODE_H265QVBR:
            rc.stH265QVbr = create_random_h265_qvbr();
            break;
        case AX_VENC_RC_MODE_H265CVBR:
            rc.stH265CVbr = create_random_h265_cvbr();
            break;
        case AX_VENC_RC_MODE_H265FIXQP:
            rc.stH265FixQp = create_random_h265_fixqp();
            break;
        case AX_VENC_RC_MODE_H265QPMAP:
            rc.stH265QpMap = create_random_h265_qmap();
            break;
        default:
            break;
    }

    return rc;
}

static AX_VENC_GOP_ATTR_T create_random_gop_attr() {
    const std::vector<AX_VENC_GOP_MODE_E> gop_modes = {AX_VENC_GOPMODE_NORMALP, AX_VENC_GOPMODE_ONELTR, AX_VENC_GOPMODE_SVC_T};
    static const AX_CHAR *stSvcTCfg[] = {
        "Frame1:  P      1      0       0.4624        2        1           -1          1",
        "Frame2:  P      2      0       0.4624        1        1           -2          1",
        "Frame3:  P      3      0       0.4624        2        2           -1 -3       1 0",
        "Frame4:  P      4      0       0.4624        0        1           -4          1",
        NULL,
    };

    AX_VENC_GOP_ATTR_T gop = {};
    gop.enGopMode = choose_random_from_array<AX_VENC_GOP_MODE_E>(gop_modes);
    switch (gop.enGopMode) {
        case AX_VENC_GOPMODE_NORMALP:
            gop.stNormalP.stPicConfig.s32QpOffset = initialize_random<AX_S32>();
            gop.stNormalP.stPicConfig.f32QpFactor = initialize_random<AX_F32>();
            break;
        case AX_VENC_GOPMODE_ONELTR:
            gop.stOneLTR.stPicConfig.s32QpOffset = initialize_random<AX_S32>();
            gop.stOneLTR.stPicConfig.f32QpFactor = initialize_random<AX_F32>();
            gop.stOneLTR.stPicSpecialConfig.s32QpOffset = initialize_random<AX_S32>();
            gop.stOneLTR.stPicSpecialConfig.f32QpFactor = initialize_random<AX_F32>();
            gop.stOneLTR.stPicSpecialConfig.s32Interval = initialize_random<AX_S32>();
            break;
        case AX_VENC_GOPMODE_SVC_T:
            gop.stSvcT.s8SvcTCfg = (AX_CHAR **)stSvcTCfg;
            gop.stSvcT.u32GopSize = 4;
            break;
        default:
            break;
    }

    return gop;
}

static AX_VENC_ATTR_T create_random_venc_attr() {
    const std::vector<AX_PAYLOAD_TYPE_E> types = {PT_H264, PT_H265, PT_MJPEG, PT_JPEG};
    const std::vector<AX_VENC_PROFILE_E> profiles = {AX_VENC_HEVC_MAIN_PROFILE,    AX_VENC_HEVC_MAIN_STILL_PICTURE_PROFILE,
                                                     AX_VENC_HEVC_MAIN_10_PROFILE, AX_VENC_HEVC_MAINREXT,
                                                     AX_VENC_H264_BASE_PROFILE,    AX_VENC_H264_MAIN_PROFILE,
                                                     AX_VENC_H264_HIGH_PROFILE,    AX_VENC_H264_HIGH_10_PROFILE};
    const std::vector<AX_VENC_LEVEL_E> levels = {
        AX_VENC_HEVC_LEVEL_1,   AX_VENC_HEVC_LEVEL_2,   AX_VENC_HEVC_LEVEL_2_1, AX_VENC_HEVC_LEVEL_3,   AX_VENC_HEVC_LEVEL_3_1,
        AX_VENC_HEVC_LEVEL_4,   AX_VENC_HEVC_LEVEL_4_1, AX_VENC_HEVC_LEVEL_5,   AX_VENC_HEVC_LEVEL_5_1, AX_VENC_HEVC_LEVEL_5_2,
        AX_VENC_HEVC_LEVEL_6,   AX_VENC_HEVC_LEVEL_6_1, AX_VENC_HEVC_LEVEL_6_2, AX_VENC_H264_LEVEL_1,   AX_VENC_H264_LEVEL_1_b,
        AX_VENC_H264_LEVEL_1_1, AX_VENC_H264_LEVEL_1_2, AX_VENC_H264_LEVEL_1_3, AX_VENC_H264_LEVEL_2,   AX_VENC_H264_LEVEL_2_1,
        AX_VENC_H264_LEVEL_2_2, AX_VENC_H264_LEVEL_3,   AX_VENC_H264_LEVEL_3_1, AX_VENC_H264_LEVEL_3_2, AX_VENC_H264_LEVEL_4,
        AX_VENC_H264_LEVEL_4_1, AX_VENC_H264_LEVEL_4_2, AX_VENC_H264_LEVEL_5,   AX_VENC_H264_LEVEL_5_1, AX_VENC_H264_LEVEL_5_2,
        AX_VENC_H264_LEVEL_6,   AX_VENC_H264_LEVEL_6_1, AX_VENC_H264_LEVEL_6_2};
    const std::vector<AX_VENC_TIER_E> tiers = {AX_VENC_HEVC_MAIN_TIER, AX_VENC_HEVC_HIGH_TIER};
    const std::vector<AX_VENC_STREAM_BIT_E> bits = {AX_VENC_STREAM_BIT_8, AX_VENC_STREAM_BIT_10};
    const std::vector<AX_VENC_LINK_MODE_E> links = {AX_VENC_LINK_MODE, AX_VENC_UNLINK_MODE};

    AX_VENC_ATTR_T attr = {};
    attr.enType = choose_random_from_array<AX_PAYLOAD_TYPE_E>(types);
    attr.u32MaxPicWidth = initialize_random<AX_U32>();
    attr.u32MaxPicHeight = initialize_random<AX_U32>();
    attr.enMemSource = create_enum_random_instance<AX_MEMORY_SOURCE_E>(AX_MEMORY_SOURCE_CMM, AX_MEMORY_SOURCE_BUTT);
    attr.u32BufSize = initialize_random<AX_U32>();
    attr.enProfile = choose_random_from_array<AX_VENC_PROFILE_E>(profiles);
    attr.enLevel = choose_random_from_array<AX_VENC_LEVEL_E>(levels);
    attr.enTier = choose_random_from_array<AX_VENC_TIER_E>(tiers);
    attr.enStrmBitDepth = choose_random_from_array<AX_VENC_STREAM_BIT_E>(bits);
    attr.u32PicWidthSrc = initialize_random<AX_U32>();
    attr.u32PicHeightSrc = initialize_random<AX_U32>();
    attr.stCropCfg.bEnable = initialize_random<AX_BOOL>();
    attr.stCropCfg.stRect.s32X = initialize_random<AX_S32>();
    attr.stCropCfg.stRect.s32Y = initialize_random<AX_S32>();
    attr.stCropCfg.stRect.u32Width = initialize_random<AX_U32>();
    attr.stCropCfg.stRect.u32Height = initialize_random<AX_U32>();
    attr.enLinkMode = choose_random_from_array<AX_VENC_LINK_MODE_E>(links);
    attr.s32StopWaitTime = initialize_random<AX_S32>();
    attr.u8InFifoDepth = initialize_random<AX_U8>();
    attr.u8OutFifoDepth = initialize_random<AX_U8>();
    attr.flag = initialize_random<AX_S32>();

    switch (attr.enType) {
        case PT_H264:
            attr.stAttrH264e.bRcnRefShareBuf = initialize_random<AX_BOOL>();
            break;
        case PT_H265:
            attr.stAttrH265e.bRcnRefShareBuf = initialize_random<AX_BOOL>();
            break;
        case PT_MJPEG:
            break;
        case PT_JPEG:
            break;
        default:
            break;
    }

    return attr;
}

static AX_VENC_CHN_ATTR_T create_random_chn_attr() {
    AX_VENC_CHN_ATTR_T attr = {};
    attr.stVencAttr = create_random_venc_attr();
    attr.stRcAttr = create_random_rc_attr();
    attr.stGopAttr = create_random_gop_attr();

    return attr;
}
