#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

#include "axcl_ive.h"
#include "randomizer.hpp"
#include "serializer.hpp"

#define CHECK_NULL_POINTER(p)                           \
    do {                                                \
        if (!(p)) {                                     \
            return -1; \
        } \
    } while(0)

AXCL_EXPORT AX_S32 AXCL_IVE_Init(AX_VOID) {
    AX_S32 ret = 0;
    SERILAIZER()->output()->serialize(ret);
    return ret;
}

AXCL_EXPORT AX_VOID AXCL_IVE_Exit(AX_VOID) {
    return;
}

AXCL_EXPORT AX_S32 AXCL_IVE_Query(AX_IVE_HANDLE IveHandle, AX_BOOL *pbFinish, AX_BOOL bBlock) {
    SERILAIZER()->input()->serialize(IveHandle, bBlock);
    AX_S32 ret = AXCL_SUCC;
    *pbFinish = AX_TRUE;
    SERILAIZER()->output()->serialize(*pbFinish, ret);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_IVE_DMA(AX_IVE_HANDLE *pIveHandle, AX_IVE_SRC_DATA_T *pstSrc, AX_IVE_DST_DATA_T *pstDst,
                                AX_IVE_DMA_CTRL_T *pstDmaCtrl, AX_BOOL bInstant) {
    SERILAIZER()->input()->serialize(pstSrc, pstDmaCtrl, bInstant);
    AX_S32 ret = AXCL_SUCC;
    *pIveHandle = initialize_random<AX_IVE_HANDLE>();
    pstDst->u64PhyAddr = initialize_random<AX_U64>();
    pstDst->u64VirAddr = initialize_random<AX_U64>();

    SERILAIZER()->output()->serialize(*pIveHandle, pstDst, ret);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_IVE_Add(AX_IVE_HANDLE *pIveHandle, AX_IVE_SRC_IMAGE_T *pstSrc1, AX_IVE_SRC_IMAGE_T *pstSrc2,
                                AX_IVE_DST_IMAGE_T *pstDst, AX_IVE_ADD_CTRL_T *pstAddCtrl, AX_BOOL bInstant) {

    SERILAIZER()->input()->serialize(pstSrc1, pstSrc2, pstAddCtrl, bInstant);
    AX_S32 ret = AXCL_SUCC;
    *pIveHandle = initialize_random<AX_IVE_HANDLE>();
    pstDst->au64PhyAddr[0] = initialize_random<AX_U64>();
    pstDst->au64PhyAddr[1] = initialize_random<AX_U64>();
    pstDst->au64PhyAddr[2] = initialize_random<AX_U64>();
    pstDst->au64VirAddr[0] = initialize_random<AX_U64>();
    pstDst->au64VirAddr[1] = initialize_random<AX_U64>();
    pstDst->au64VirAddr[2] = initialize_random<AX_U64>();
    SERILAIZER()->output()->serialize(*pIveHandle, pstDst, ret);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_IVE_Sub(AX_IVE_HANDLE *pIveHandle, AX_IVE_SRC_IMAGE_T *pstSrc1, AX_IVE_SRC_IMAGE_T *pstSrc2,
                                AX_IVE_DST_IMAGE_T *pstDst, AX_IVE_SUB_CTRL_T *pstSubCtrl, AX_BOOL bInstant) {

    SERILAIZER()->input()->serialize(pstSrc1, pstSrc2, pstSubCtrl, bInstant);
    AX_S32 ret = AXCL_SUCC;
    *pIveHandle = initialize_random<AX_IVE_HANDLE>();
    pstDst->au64PhyAddr[0] = initialize_random<AX_U64>();
    pstDst->au64PhyAddr[1] = initialize_random<AX_U64>();
    pstDst->au64PhyAddr[2] = initialize_random<AX_U64>();
    pstDst->au64VirAddr[0] = initialize_random<AX_U64>();
    pstDst->au64VirAddr[1] = initialize_random<AX_U64>();
    pstDst->au64VirAddr[2] = initialize_random<AX_U64>();
    SERILAIZER()->output()->serialize(*pIveHandle, pstDst, ret);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_IVE_And(AX_IVE_HANDLE *pIveHandle, AX_IVE_SRC_IMAGE_T *pstSrc1, AX_IVE_SRC_IMAGE_T *pstSrc2,
                                AX_IVE_DST_IMAGE_T *pstDst, AX_BOOL bInstant) {

    SERILAIZER()->input()->serialize(pstSrc1, pstSrc2, bInstant);
    AX_S32 ret = AXCL_SUCC;
    *pIveHandle = initialize_random<AX_IVE_HANDLE>();
    pstDst->au64PhyAddr[0] = initialize_random<AX_U64>();
    pstDst->au64PhyAddr[1] = initialize_random<AX_U64>();
    pstDst->au64PhyAddr[2] = initialize_random<AX_U64>();
    pstDst->au64VirAddr[0] = initialize_random<AX_U64>();
    pstDst->au64VirAddr[1] = initialize_random<AX_U64>();
    pstDst->au64VirAddr[2] = initialize_random<AX_U64>();
    SERILAIZER()->output()->serialize(*pIveHandle, pstDst, ret);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_IVE_Or(AX_IVE_HANDLE *pIveHandle, AX_IVE_SRC_IMAGE_T *pstSrc1, AX_IVE_SRC_IMAGE_T *pstSrc2,
                               AX_IVE_DST_IMAGE_T *pstDst, AX_BOOL bInstant) {

    SERILAIZER()->input()->serialize(pstSrc1, pstSrc2, bInstant);
    AX_S32 ret = AXCL_SUCC;
    *pIveHandle = initialize_random<AX_IVE_HANDLE>();
    pstDst->au64PhyAddr[0] = initialize_random<AX_U64>();
    pstDst->au64PhyAddr[1] = initialize_random<AX_U64>();
    pstDst->au64PhyAddr[2] = initialize_random<AX_U64>();
    pstDst->au64VirAddr[0] = initialize_random<AX_U64>();
    pstDst->au64VirAddr[1] = initialize_random<AX_U64>();
    pstDst->au64VirAddr[2] = initialize_random<AX_U64>();
    SERILAIZER()->output()->serialize(*pIveHandle, pstDst, ret);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_IVE_Xor(AX_IVE_HANDLE *pIveHandle, AX_IVE_SRC_IMAGE_T *pstSrc1, AX_IVE_SRC_IMAGE_T *pstSrc2,
                                AX_IVE_DST_IMAGE_T *pstDst, AX_BOOL bInstant) {

    SERILAIZER()->input()->serialize(pstSrc1, pstSrc2, bInstant);
    AX_S32 ret = AXCL_SUCC;
    *pIveHandle = initialize_random<AX_IVE_HANDLE>();
    pstDst->au64PhyAddr[0] = initialize_random<AX_U64>();
    pstDst->au64PhyAddr[1] = initialize_random<AX_U64>();
    pstDst->au64PhyAddr[2] = initialize_random<AX_U64>();
    pstDst->au64VirAddr[0] = initialize_random<AX_U64>();
    pstDst->au64VirAddr[1] = initialize_random<AX_U64>();
    pstDst->au64VirAddr[2] = initialize_random<AX_U64>();
    SERILAIZER()->output()->serialize(*pIveHandle, pstDst, ret);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_IVE_Mse(AX_IVE_HANDLE *pIveHandle, AX_IVE_SRC_IMAGE_T *pstSrc1, AX_IVE_SRC_IMAGE_T *pstSrc2,
                                AX_IVE_DST_IMAGE_T *pstDst, AX_IVE_MSE_CTRL_T *pstMseCtrl, AX_BOOL bInstant) {
    SERILAIZER()->input()->serialize(pstSrc1, pstSrc2, pstMseCtrl, bInstant);
    AX_S32 ret = AXCL_SUCC;
    *pIveHandle = initialize_random<AX_IVE_HANDLE>();
    pstDst->au64PhyAddr[0] = initialize_random<AX_U64>();
    pstDst->au64PhyAddr[1] = initialize_random<AX_U64>();
    pstDst->au64PhyAddr[2] = initialize_random<AX_U64>();
    pstDst->au64VirAddr[0] = initialize_random<AX_U64>();
    pstDst->au64VirAddr[1] = initialize_random<AX_U64>();
    pstDst->au64VirAddr[2] = initialize_random<AX_U64>();
    SERILAIZER()->output()->serialize(*pIveHandle, pstDst, ret);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_IVE_CannyHysEdge(AX_IVE_HANDLE *pIveHandle, AX_IVE_SRC_IMAGE_T *pstSrc1, AX_IVE_SRC_IMAGE_T *pstSrc2,
                                         AX_IVE_DST_IMAGE_T *pstDst, AX_IVE_HYS_EDGE_CTRL_T *pstCannyHysEdgeCtrl, AX_BOOL bInstant) {
    SERILAIZER()->input()->serialize(pstSrc1, pstSrc2, pstCannyHysEdgeCtrl, bInstant);
    AX_S32 ret = AXCL_SUCC;
    *pIveHandle = initialize_random<AX_IVE_HANDLE>();
    pstDst->au64PhyAddr[0] = initialize_random<AX_U64>();
    pstDst->au64PhyAddr[1] = initialize_random<AX_U64>();
    pstDst->au64PhyAddr[2] = initialize_random<AX_U64>();
    pstDst->au64VirAddr[0] = initialize_random<AX_U64>();
    pstDst->au64VirAddr[1] = initialize_random<AX_U64>();
    pstDst->au64VirAddr[2] = initialize_random<AX_U64>();
    SERILAIZER()->output()->serialize(*pIveHandle, pstDst, ret);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_IVE_CannyEdge(AX_IVE_HANDLE *pIveHandle, AX_IVE_SRC_IMAGE_T *pstSrc, AX_IVE_DST_IMAGE_T *pstDst,
                                      AX_IVE_CANNY_EDGE_CTRL_T *pstCannyEdgeCtrl, AX_BOOL bInstant) {

    SERILAIZER()->input()->serialize(pstSrc, pstCannyEdgeCtrl, bInstant);
    AX_S32 ret = AXCL_SUCC;
    *pIveHandle = initialize_random<AX_IVE_HANDLE>();
    pstDst->au64PhyAddr[0] = initialize_random<AX_U64>();
    pstDst->au64PhyAddr[1] = initialize_random<AX_U64>();
    pstDst->au64PhyAddr[2] = initialize_random<AX_U64>();
    pstDst->au64VirAddr[0] = initialize_random<AX_U64>();
    pstDst->au64VirAddr[1] = initialize_random<AX_U64>();
    pstDst->au64VirAddr[2] = initialize_random<AX_U64>();
    SERILAIZER()->output()->serialize(*pIveHandle, pstDst, ret);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_IVE_CCL(AX_IVE_HANDLE *pIveHandle, AX_IVE_SRC_IMAGE_T *pstSrc, AX_IVE_DST_IMAGE_T *pstDst,
                                AX_IVE_DST_MEM_INFO_T *pstBlob, AX_IVE_CCL_CTRL_T *pstCclCtrl, AX_BOOL bInstant) {

    SERILAIZER()->input()->serialize(pstSrc, pstCclCtrl, bInstant);
    AX_S32 ret = AXCL_SUCC;
    *pIveHandle = initialize_random<AX_IVE_HANDLE>();
    pstDst->au64PhyAddr[0] = initialize_random<AX_U64>();
    pstDst->au64PhyAddr[1] = initialize_random<AX_U64>();
    pstDst->au64PhyAddr[2] = initialize_random<AX_U64>();
    pstDst->au64VirAddr[0] = initialize_random<AX_U64>();
    pstDst->au64VirAddr[1] = initialize_random<AX_U64>();
    pstDst->au64VirAddr[2] = initialize_random<AX_U64>();

    pstBlob->u64PhyAddr = initialize_random<AX_U64>();
    pstBlob->u64VirAddr = initialize_random<AX_U64>();
    pstBlob->u32Size = initialize_random<AX_U32>();

    SERILAIZER()->output()->serialize(*pIveHandle, pstDst, pstBlob, ret);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_IVE_Erode(AX_IVE_HANDLE *pIveHandle, AX_IVE_SRC_IMAGE_T *pstSrc, AX_IVE_DST_IMAGE_T *pstDst,
                                  AX_IVE_ERODE_CTRL_T *pstErodeCtrl, AX_BOOL bInstant) {

    SERILAIZER()->input()->serialize(pstSrc, pstErodeCtrl, bInstant);
    AX_S32 ret = AXCL_SUCC;
    *pIveHandle = initialize_random<AX_IVE_HANDLE>();
    pstDst->au64PhyAddr[0] = initialize_random<AX_U64>();
    pstDst->au64PhyAddr[1] = initialize_random<AX_U64>();
    pstDst->au64PhyAddr[2] = initialize_random<AX_U64>();
    pstDst->au64VirAddr[0] = initialize_random<AX_U64>();
    pstDst->au64VirAddr[1] = initialize_random<AX_U64>();
    pstDst->au64VirAddr[2] = initialize_random<AX_U64>();
    SERILAIZER()->output()->serialize(*pIveHandle, pstDst, ret);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_IVE_Dilate(AX_IVE_HANDLE *pIveHandle, AX_IVE_SRC_IMAGE_T *pstSrc, AX_IVE_DST_IMAGE_T *pstDst,
                                   AX_IVE_DILATE_CTRL_T *pstDilateCtrl, AX_BOOL bInstant) {

    SERILAIZER()->input()->serialize(pstSrc, pstDilateCtrl, bInstant);
    AX_S32 ret = AXCL_SUCC;
    *pIveHandle = initialize_random<AX_IVE_HANDLE>();
    pstDst->au64PhyAddr[0] = initialize_random<AX_U64>();
    pstDst->au64PhyAddr[1] = initialize_random<AX_U64>();
    pstDst->au64PhyAddr[2] = initialize_random<AX_U64>();
    pstDst->au64VirAddr[0] = initialize_random<AX_U64>();
    pstDst->au64VirAddr[1] = initialize_random<AX_U64>();
    pstDst->au64VirAddr[2] = initialize_random<AX_U64>();
    SERILAIZER()->output()->serialize(*pIveHandle, pstDst, ret);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_IVE_Filter(AX_IVE_HANDLE *pIveHandle, AX_IVE_SRC_IMAGE_T *pstSrc, AX_IVE_DST_IMAGE_T *pstDst,
                                   AX_IVE_FILTER_CTRL_T *pstFltCtrl, AX_BOOL bInstant) {

    SERILAIZER()->input()->serialize(pstSrc, pstFltCtrl, bInstant);
    AX_S32 ret = AXCL_SUCC;
    *pIveHandle = initialize_random<AX_IVE_HANDLE>();
    pstDst->au64PhyAddr[0] = initialize_random<AX_U64>();
    pstDst->au64PhyAddr[1] = initialize_random<AX_U64>();
    pstDst->au64PhyAddr[2] = initialize_random<AX_U64>();
    pstDst->au64VirAddr[0] = initialize_random<AX_U64>();
    pstDst->au64VirAddr[1] = initialize_random<AX_U64>();
    pstDst->au64VirAddr[2] = initialize_random<AX_U64>();
    SERILAIZER()->output()->serialize(*pIveHandle, pstDst, ret);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_IVE_Hist(AX_IVE_HANDLE *pIveHandle, AX_IVE_SRC_IMAGE_T *pstSrc, AX_IVE_DST_MEM_INFO_T *pstDst, AX_BOOL bInstant) {

    SERILAIZER()->input()->serialize(pstSrc, bInstant);

    AX_S32 ret = AXCL_SUCC;
    *pIveHandle = initialize_random<AX_IVE_HANDLE>();
    pstDst->u64PhyAddr = initialize_random<AX_U64>();
    pstDst->u64VirAddr = initialize_random<AX_U64>();
    pstDst->u32Size = initialize_random<AX_U32>();
    SERILAIZER()->output()->serialize(*pIveHandle, pstDst, ret);

    return AXCL_SUCC;
}

AXCL_EXPORT AX_S32 AXCL_IVE_EqualizeHist(AX_IVE_HANDLE *pIveHandle, AX_IVE_SRC_IMAGE_T *pstSrc, AX_IVE_DST_MEM_INFO_T *pstDst,
                                         AX_IVE_EQUALIZE_HIST_CTRL_T *pstEqualizeHistCtrl, AX_BOOL bInstant) {
    SERILAIZER()->input()->serialize(pstSrc, pstEqualizeHistCtrl, bInstant);

    AX_S32 ret = AXCL_SUCC;
    *pIveHandle = initialize_random<AX_IVE_HANDLE>();
    pstDst->u64PhyAddr = initialize_random<AX_U64>();
    pstDst->u64VirAddr = initialize_random<AX_U64>();
    pstDst->u32Size = initialize_random<AX_U32>();
    SERILAIZER()->output()->serialize(*pIveHandle, pstDst, ret);

    return AXCL_SUCC;
}

AXCL_EXPORT AX_S32 AXCL_IVE_Integ(AX_IVE_HANDLE *pIveHandle, AX_IVE_SRC_IMAGE_T *pstSrc, AX_IVE_DST_IMAGE_T *pstDst,
                                  AX_IVE_INTEG_CTRL_T *pstIntegCtrl, AX_BOOL bInstant) {

    SERILAIZER()->input()->serialize(pstSrc, pstIntegCtrl, bInstant);
    AX_S32 ret = AXCL_SUCC;
    *pIveHandle = initialize_random<AX_IVE_HANDLE>();
    pstDst->au64PhyAddr[0] = initialize_random<AX_U64>();
    pstDst->au64PhyAddr[1] = initialize_random<AX_U64>();
    pstDst->au64PhyAddr[2] = initialize_random<AX_U64>();
    pstDst->au64VirAddr[0] = initialize_random<AX_U64>();
    pstDst->au64VirAddr[1] = initialize_random<AX_U64>();
    pstDst->au64VirAddr[2] = initialize_random<AX_U64>();
    SERILAIZER()->output()->serialize(*pIveHandle, pstDst, ret);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_IVE_MagAndAng(AX_IVE_HANDLE *pIveHandle, AX_IVE_SRC_IMAGE_T *pstSrc1, AX_IVE_SRC_IMAGE_T *pstSrc2,
                                      AX_IVE_DST_IMAGE_T *pstDstMag, AX_IVE_DST_IMAGE_T *pstDstAng, AX_BOOL bInstant) {

    SERILAIZER()->input()->serialize(pstSrc1, pstSrc2, bInstant);

    AX_S32 ret = AXCL_SUCC;
    *pIveHandle = initialize_random<AX_IVE_HANDLE>();
    pstDstMag->au64PhyAddr[0] = initialize_random<AX_U64>();
    pstDstMag->au64PhyAddr[1] = initialize_random<AX_U64>();
    pstDstMag->au64PhyAddr[2] = initialize_random<AX_U64>();
    pstDstMag->au64VirAddr[0] = initialize_random<AX_U64>();
    pstDstMag->au64VirAddr[1] = initialize_random<AX_U64>();
    pstDstMag->au64VirAddr[2] = initialize_random<AX_U64>();

    pstDstAng->au64PhyAddr[0] = initialize_random<AX_U64>();
    pstDstAng->au64PhyAddr[1] = initialize_random<AX_U64>();
    pstDstAng->au64PhyAddr[2] = initialize_random<AX_U64>();
    pstDstAng->au64VirAddr[0] = initialize_random<AX_U64>();
    pstDstAng->au64VirAddr[1] = initialize_random<AX_U64>();
    pstDstAng->au64VirAddr[2] = initialize_random<AX_U64>();

    SERILAIZER()->output()->serialize(*pIveHandle, pstDstMag, pstDstAng, ret);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_IVE_Sobel(AX_IVE_HANDLE *pIveHandle, AX_IVE_SRC_IMAGE_T *pstSrc, AX_IVE_DST_IMAGE_T *pstDst,
                                  AX_IVE_SOBEL_CTRL_T *pstSobelCtrl, AX_BOOL bInstant) {

    SERILAIZER()->input()->serialize(pstSrc, pstSobelCtrl, bInstant);
    AX_S32 ret = AXCL_SUCC;
    *pIveHandle = initialize_random<AX_IVE_HANDLE>();
    pstDst->au64PhyAddr[0] = initialize_random<AX_U64>();
    pstDst->au64PhyAddr[1] = initialize_random<AX_U64>();
    pstDst->au64PhyAddr[2] = initialize_random<AX_U64>();
    pstDst->au64VirAddr[0] = initialize_random<AX_U64>();
    pstDst->au64VirAddr[1] = initialize_random<AX_U64>();
    pstDst->au64VirAddr[2] = initialize_random<AX_U64>();
    SERILAIZER()->output()->serialize(*pIveHandle, pstDst, ret);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_IVE_GMM(AX_IVE_HANDLE *pIveHandle, AX_IVE_SRC_IMAGE_T *pstSrc, AX_IVE_DST_IMAGE_T *pstFg, AX_IVE_DST_IMAGE_T *pstBg,
                                AX_IVE_MEM_INFO_T *pstModel, AX_IVE_GMM_CTRL_T *pstGmmCtrl, AX_BOOL bInstant) {
    SERILAIZER()->input()->serialize(pstSrc, pstModel, pstGmmCtrl, bInstant);
    AX_S32 ret = AXCL_SUCC;
    *pIveHandle = initialize_random<AX_IVE_HANDLE>();
    pstFg->au64PhyAddr[0] = initialize_random<AX_U64>();
    pstFg->au64PhyAddr[1] = initialize_random<AX_U64>();
    pstFg->au64PhyAddr[2] = initialize_random<AX_U64>();
    pstFg->au64VirAddr[0] = initialize_random<AX_U64>();
    pstFg->au64VirAddr[1] = initialize_random<AX_U64>();
    pstFg->au64VirAddr[2] = initialize_random<AX_U64>();

    pstBg->au64PhyAddr[0] = initialize_random<AX_U64>();
    pstBg->au64PhyAddr[1] = initialize_random<AX_U64>();
    pstBg->au64PhyAddr[2] = initialize_random<AX_U64>();
    pstBg->au64VirAddr[0] = initialize_random<AX_U64>();
    pstBg->au64VirAddr[1] = initialize_random<AX_U64>();
    pstBg->au64VirAddr[2] = initialize_random<AX_U64>();
    SERILAIZER()->output()->serialize(*pIveHandle, pstFg, pstBg, ret);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_IVE_GMM2(AX_IVE_HANDLE *pIveHandle, AX_IVE_SRC_IMAGE_T *pstSrc, AX_IVE_DST_IMAGE_T *pstFg,
                                 AX_IVE_DST_IMAGE_T *pstBg, AX_IVE_MEM_INFO_T *pstModel, AX_IVE_GMM2_CTRL_T *pstGmm2Ctrl,
                                 AX_BOOL bInstant) {

    SERILAIZER()->input()->serialize(pstSrc, pstModel, pstGmm2Ctrl, bInstant);
    AX_S32 ret = AXCL_SUCC;
    *pIveHandle = initialize_random<AX_IVE_HANDLE>();
    pstFg->au64PhyAddr[0] = initialize_random<AX_U64>();
    pstFg->au64PhyAddr[1] = initialize_random<AX_U64>();
    pstFg->au64PhyAddr[2] = initialize_random<AX_U64>();
    pstFg->au64VirAddr[0] = initialize_random<AX_U64>();
    pstFg->au64VirAddr[1] = initialize_random<AX_U64>();
    pstFg->au64VirAddr[2] = initialize_random<AX_U64>();

    pstBg->au64PhyAddr[0] = initialize_random<AX_U64>();
    pstBg->au64PhyAddr[1] = initialize_random<AX_U64>();
    pstBg->au64PhyAddr[2] = initialize_random<AX_U64>();
    pstBg->au64VirAddr[0] = initialize_random<AX_U64>();
    pstBg->au64VirAddr[1] = initialize_random<AX_U64>();
    pstBg->au64VirAddr[2] = initialize_random<AX_U64>();
    SERILAIZER()->output()->serialize(*pIveHandle, pstFg, pstBg, ret);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_IVE_Thresh(AX_IVE_HANDLE *pIveHandle, AX_IVE_SRC_IMAGE_T *pstSrc, AX_IVE_DST_IMAGE_T *pstDst,
                                   AX_IVE_THRESH_CTRL_T *pstThrCtrl, AX_BOOL bInstant) {
    SERILAIZER()->input()->serialize(pstSrc, pstThrCtrl, bInstant);
    AX_S32 ret = AXCL_SUCC;
    *pIveHandle = initialize_random<AX_IVE_HANDLE>();
    pstDst->au64PhyAddr[0] = initialize_random<AX_U64>();
    pstDst->au64PhyAddr[1] = initialize_random<AX_U64>();
    pstDst->au64PhyAddr[2] = initialize_random<AX_U64>();
    pstDst->au64VirAddr[0] = initialize_random<AX_U64>();
    pstDst->au64VirAddr[1] = initialize_random<AX_U64>();
    pstDst->au64VirAddr[2] = initialize_random<AX_U64>();
    SERILAIZER()->output()->serialize(*pIveHandle, pstDst, ret);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_IVE_16BitTo8Bit(AX_IVE_HANDLE *pIveHandle, AX_IVE_SRC_IMAGE_T *pstSrc, AX_IVE_DST_IMAGE_T *pstDst,
                                        AX_IVE_16BIT_TO_8BIT_CTRL_T *pst16BitTo8BitCtrl, AX_BOOL bInstant) {
    SERILAIZER()->input()->serialize(pstSrc, pst16BitTo8BitCtrl, bInstant);
    AX_S32 ret = AXCL_SUCC;
    *pIveHandle = initialize_random<AX_IVE_HANDLE>();
    pstDst->au64PhyAddr[0] = initialize_random<AX_U64>();
    pstDst->au64PhyAddr[1] = initialize_random<AX_U64>();
    pstDst->au64PhyAddr[2] = initialize_random<AX_U64>();
    pstDst->au64VirAddr[0] = initialize_random<AX_U64>();
    pstDst->au64VirAddr[1] = initialize_random<AX_U64>();
    pstDst->au64VirAddr[2] = initialize_random<AX_U64>();
    SERILAIZER()->output()->serialize(*pIveHandle, pstDst, ret);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_IVE_CropImage(AX_IVE_HANDLE *pIveHandle, AX_IVE_SRC_IMAGE_T *pstSrc, AX_IVE_DST_IMAGE_T *pastDst[],
                                      AX_IVE_RECT_U16_T *pastSrcBoxs[], AX_IVE_CROP_IMAGE_CTRL_T *pstCropImageCtrl,
                                      AX_IVE_ENGINE_E enEngine, AX_BOOL bInstant) {

    SERILAIZER()->input()->serialize(pstSrc, *pastSrcBoxs, pstCropImageCtrl, enEngine, bInstant);
    AX_S32 ret = AXCL_SUCC;
    *pIveHandle = initialize_random<AX_IVE_HANDLE>();
    // pstCropImageCtrl->u16Num = 1
    for (size_t i = 0; i < pstCropImageCtrl->u16Num; i++) {
        pastDst[i]->au64PhyAddr[0] = initialize_random<AX_U64>();
        pastDst[i]->au64PhyAddr[1] = initialize_random<AX_U64>();
        pastDst[i]->au64PhyAddr[2] = initialize_random<AX_U64>();
        pastDst[i]->au64VirAddr[0] = initialize_random<AX_U64>();
        pastDst[i]->au64VirAddr[1] = initialize_random<AX_U64>();
        pastDst[i]->au64VirAddr[2] = initialize_random<AX_U64>();
    }
    SERILAIZER()->output()->serialize(*pIveHandle, *pastDst, ret);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_IVE_CropResize(AX_IVE_HANDLE *pIveHandle, AX_IVE_SRC_IMAGE_T *pstSrc, AX_IVE_DST_IMAGE_T *pastDst[],
                                       AX_IVE_RECT_U16_T *pastSrcBoxs[], AX_IVE_CROP_RESIZE_CTRL_T *pstCropResizeCtrl,
                                       AX_IVE_ENGINE_E enEngine, AX_BOOL bInstant) {

    SERILAIZER()->input()->serialize(pstSrc, *pastSrcBoxs, pstCropResizeCtrl, enEngine, bInstant);
    AX_S32 ret = AXCL_SUCC;
    *pIveHandle = initialize_random<AX_IVE_HANDLE>();
    // pstCropResizeCtrl->u16Num = 1
    for (size_t i = 0; i < pstCropResizeCtrl->u16Num; i++) {
        pastDst[i]->au64PhyAddr[0] = initialize_random<AX_U64>();
        pastDst[i]->au64PhyAddr[1] = initialize_random<AX_U64>();
        pastDst[i]->au64PhyAddr[2] = initialize_random<AX_U64>();
        pastDst[i]->au64VirAddr[0] = initialize_random<AX_U64>();
        pastDst[i]->au64VirAddr[1] = initialize_random<AX_U64>();
        pastDst[i]->au64VirAddr[2] = initialize_random<AX_U64>();
    }
    SERILAIZER()->output()->serialize(*pIveHandle, *pastDst, ret);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_IVE_CropResizeForSplitYUV(AX_IVE_HANDLE *pIveHandle, AX_IVE_SRC_IMAGE_T *pstSrc1, AX_IVE_SRC_IMAGE_T *pstSrc2,
                                                  AX_IVE_DST_IMAGE_T *pastDst1[], AX_IVE_DST_IMAGE_T *pastDst2[],
                                                  AX_IVE_RECT_U16_T *pastSrcBoxs[], AX_IVE_CROP_RESIZE_CTRL_T *pstCropResizeCtrl,
                                                  AX_IVE_ENGINE_E enEngine, AX_BOOL bInstant) {

    SERILAIZER()->input()->serialize(pstSrc1, pstSrc2, *pastSrcBoxs, pstCropResizeCtrl, enEngine, bInstant);
    AX_S32 ret = AXCL_SUCC;
    *pIveHandle = initialize_random<AX_IVE_HANDLE>();
    // pstCropResizeCtrl->u16Num = 1
    for (size_t i = 0; i < pstCropResizeCtrl->u16Num; i++) {
        pastDst1[i]->au64PhyAddr[0] = initialize_random<AX_U64>();
        pastDst1[i]->au64PhyAddr[1] = initialize_random<AX_U64>();
        pastDst1[i]->au64PhyAddr[2] = initialize_random<AX_U64>();
        pastDst1[i]->au64VirAddr[0] = initialize_random<AX_U64>();
        pastDst1[i]->au64VirAddr[1] = initialize_random<AX_U64>();
        pastDst1[i]->au64VirAddr[2] = initialize_random<AX_U64>();

        pastDst2[i]->au64PhyAddr[0] = initialize_random<AX_U64>();
        pastDst2[i]->au64PhyAddr[1] = initialize_random<AX_U64>();
        pastDst2[i]->au64PhyAddr[2] = initialize_random<AX_U64>();
        pastDst2[i]->au64VirAddr[0] = initialize_random<AX_U64>();
        pastDst2[i]->au64VirAddr[1] = initialize_random<AX_U64>();
        pastDst2[i]->au64VirAddr[2] = initialize_random<AX_U64>();
    }
    SERILAIZER()->output()->serialize(*pIveHandle, *pastDst1, *pastDst2, ret);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_IVE_CSC(AX_IVE_HANDLE *pIveHandle, AX_IVE_SRC_IMAGE_T *pstSrc, AX_IVE_DST_IMAGE_T *pstDst, AX_IVE_ENGINE_E enEngine,
                                AX_BOOL bInstant) {

    SERILAIZER()->input()->serialize(pstSrc, enEngine, bInstant);
    AX_S32 ret = AXCL_SUCC;
    *pIveHandle = initialize_random<AX_IVE_HANDLE>();
    pstDst->au64PhyAddr[0] = initialize_random<AX_U64>();
    pstDst->au64PhyAddr[1] = initialize_random<AX_U64>();
    pstDst->au64PhyAddr[2] = initialize_random<AX_U64>();
    pstDst->au64VirAddr[0] = initialize_random<AX_U64>();
    pstDst->au64VirAddr[1] = initialize_random<AX_U64>();
    pstDst->au64VirAddr[2] = initialize_random<AX_U64>();
    SERILAIZER()->output()->serialize(*pIveHandle, pstDst, ret);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_IVE_CropResize2(AX_IVE_HANDLE *pIveHandle, AX_IVE_SRC_IMAGE_T *pstSrc, AX_IVE_IMAGE_T *pastDst[],
                                        AX_IVE_RECT_U16_T *pastSrcBoxs[], AX_IVE_RECT_U16_T *pastDstBoxs[],
                                        AX_IVE_CROP_IMAGE_CTRL_T *pstCropResize2Ctrl, AX_IVE_ENGINE_E enEngine, AX_BOOL bInstant) {

    SERILAIZER()->input()->serialize(pstSrc, *pastSrcBoxs, *pastDstBoxs, pstCropResize2Ctrl, enEngine, bInstant);
    AX_S32 ret = AXCL_SUCC;
    *pIveHandle = initialize_random<AX_IVE_HANDLE>();
    // pstCropResize2Ctrl->u16Num = 1
    for (size_t i = 0; i < pstCropResize2Ctrl->u16Num; i++) {
        pastDst[i]->au64PhyAddr[0] = initialize_random<AX_U64>();
        pastDst[i]->au64PhyAddr[1] = initialize_random<AX_U64>();
        pastDst[i]->au64PhyAddr[2] = initialize_random<AX_U64>();
        pastDst[i]->au64VirAddr[0] = initialize_random<AX_U64>();
        pastDst[i]->au64VirAddr[1] = initialize_random<AX_U64>();
        pastDst[i]->au64VirAddr[2] = initialize_random<AX_U64>();
    }
    SERILAIZER()->output()->serialize(*pIveHandle, *pastDst, ret);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_IVE_CropResize2ForSplitYUV(AX_IVE_HANDLE *pIveHandle, AX_IVE_SRC_IMAGE_T *pstSrc1, AX_IVE_SRC_IMAGE_T *pstSrc2,
                                                   AX_IVE_IMAGE_T *pastDst1[], AX_IVE_IMAGE_T *pastDst2[], AX_IVE_RECT_U16_T *pastSrcBoxs[],
                                                   AX_IVE_RECT_U16_T *pastDstBoxs[], AX_IVE_CROP_IMAGE_CTRL_T *pstCropResize2Ctrl,
                                                   AX_IVE_ENGINE_E enEngine, AX_BOOL bInstant) {

    SERILAIZER()->input()->serialize(pstSrc1, pstSrc2, *pastSrcBoxs, *pastDstBoxs, pstCropResize2Ctrl, enEngine, bInstant);
    AX_S32 ret = AXCL_SUCC;
    *pIveHandle = initialize_random<AX_IVE_HANDLE>();
    // pstCropResize2Ctrl->u16Num = 1
    for (size_t i = 0; i < pstCropResize2Ctrl->u16Num; i++) {
        pastDst1[i]->au64PhyAddr[0] = initialize_random<AX_U64>();
        pastDst1[i]->au64PhyAddr[1] = initialize_random<AX_U64>();
        pastDst1[i]->au64PhyAddr[2] = initialize_random<AX_U64>();
        pastDst1[i]->au64VirAddr[0] = initialize_random<AX_U64>();
        pastDst1[i]->au64VirAddr[1] = initialize_random<AX_U64>();
        pastDst1[i]->au64VirAddr[2] = initialize_random<AX_U64>();

        pastDst2[i]->au64PhyAddr[0] = initialize_random<AX_U64>();
        pastDst2[i]->au64PhyAddr[1] = initialize_random<AX_U64>();
        pastDst2[i]->au64PhyAddr[2] = initialize_random<AX_U64>();
        pastDst2[i]->au64VirAddr[0] = initialize_random<AX_U64>();
        pastDst2[i]->au64VirAddr[1] = initialize_random<AX_U64>();
        pastDst2[i]->au64VirAddr[2] = initialize_random<AX_U64>();
    }
    SERILAIZER()->output()->serialize(*pIveHandle, *pastDst1, *pastDst2, ret);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_IVE_MAU_MatMul(AX_IVE_HANDLE *pIveHandle, AX_IVE_MAU_MATMUL_INPUT_T *pstSrc, AX_IVE_MAU_MATMUL_OUTPUT_T *pstDst,
                                       AX_IVE_MAU_MATMUL_CTRL_T *pstMatMulCtrl, AX_IVE_ENGINE_E enEngine, AX_BOOL bInstant) {

    SERILAIZER()->input()->serialize(pstSrc, pstMatMulCtrl, enEngine, bInstant);
    AX_S32 ret = AXCL_SUCC;
    *pIveHandle = initialize_random<AX_IVE_HANDLE>();
    pstDst->stMulRes.u64PhyAddr = initialize_random<AX_U64>();
    pstDst->stMulRes.pVirAddr = (AX_VOID *)initialize_random<AX_U64>();
    pstDst->stMulRes.enDataType = AX_IVE_MAU_DT_UINT16;
    pstDst->stTopNRes.u64PhyAddr = initialize_random<AX_U64>();
    pstDst->stTopNRes.pVirAddr = (AX_VOID *)initialize_random<AX_U64>();
    pstDst->stTopNRes.enDataType = AX_IVE_MAU_DT_FLOAT32;
    SERILAIZER()->output()->serialize(*pIveHandle, pstDst, ret);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_IVE_NPU_CreateMatMulHandle(AX_IVE_MATMUL_HANDLE *pHandle, AX_IVE_NPU_MATMUL_CTRL_T *pstMatMulCtrl) {
    SERILAIZER()->input()->serialize(pstMatMulCtrl);
    AX_S32 ret = AXCL_SUCC;
    *pHandle = initialize_random<AX_IVE_MATMUL_HANDLE>();
    SERILAIZER()->output()->serialize((AX_U64)*pHandle, ret);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_IVE_NPU_DestroyMatMulHandle(AX_IVE_MATMUL_HANDLE *pHandle) {
    SERILAIZER()->input()->serialize((AX_U64)*pHandle);
    AX_S32 ret = AXCL_SUCC;
    SERILAIZER()->output()->serialize(ret);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_IVE_NPU_MatMul(AX_IVE_MATMUL_HANDLE hHandle, AX_IVE_MAU_MATMUL_INPUT_T *pstSrc, AX_IVE_MAU_MATMUL_OUTPUT_T *pstDst,
                                       AX_IVE_ENGINE_E enEngine, AX_BOOL bInstant) {

    SERILAIZER()->input()->serialize((AX_U64)hHandle, pstSrc, enEngine, bInstant);
    AX_S32 ret = AXCL_SUCC;
    pstDst->stMulRes.u64PhyAddr = initialize_random<AX_U64>();
    pstDst->stMulRes.pVirAddr = (AX_VOID *)initialize_random<AX_U64>();
    pstDst->stMulRes.enDataType = AX_IVE_MAU_DT_UINT16;
    pstDst->stTopNRes.u64PhyAddr = initialize_random<AX_U64>();
    pstDst->stTopNRes.pVirAddr = (AX_VOID *)initialize_random<AX_U64>();
    pstDst->stTopNRes.enDataType = AX_IVE_MAU_DT_FLOAT32;
    SERILAIZER()->output()->serialize(pstDst, ret);
    return ret;
}