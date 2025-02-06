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
    printf("=====>%s:\n", __func__);
    return AXCL_SUCC;
}

AXCL_EXPORT AX_VOID AXCL_IVE_Exit(AX_VOID) {
    printf("=====>%s:\n", __func__);
    return;
}

AXCL_EXPORT AX_S32 AXCL_IVE_Query(AX_IVE_HANDLE IveHandle, AX_BOOL *pbFinish, AX_BOOL bBlock) {
    CHECK_NULL_POINTER(IveHandle);
    CHECK_NULL_POINTER(pbFinish);

    *pbFinish = AX_TRUE;

    printf("=====>%s:\n", __func__);
    printf("=====>handle: %d\n", IveHandle);
    printf("=====>bBlock: %d\n", bBlock);
    printf("=====>bFinish: %d\n", *pbFinish);

    return AXCL_SUCC;
}

AXCL_EXPORT AX_S32 AXCL_IVE_DMA(AX_IVE_HANDLE *pIveHandle, AX_IVE_SRC_DATA_T *pstSrc, AX_IVE_DST_DATA_T *pstDst,
                                AX_IVE_DMA_CTRL_T *pstDmaCtrl, AX_BOOL bInstant) {
    CHECK_NULL_POINTER(pIveHandle);
    CHECK_NULL_POINTER(pstSrc);
    CHECK_NULL_POINTER(pstDst);
    CHECK_NULL_POINTER(pstDmaCtrl);

    *pIveHandle = 1;

    printf("=====>%s:\n", __func__);
    printf("=====>created handle: %d\n", *pIveHandle);
    printf("=====>src: u64PhyAddr: 0x%llx, u64VirAddr: 0x%llx, u32Stride: %d, u32Width: %d, u32Height: %d, u32Reserved: %d\n",
                                pstSrc->u64PhyAddr,
                                pstSrc->u64VirAddr,
                                pstSrc->u32Stride,
                                pstSrc->u32Width,
                                pstSrc->u32Height,
                                pstSrc->u32Reserved);
    printf("=====>dst: u64PhyAddr: 0x%llx, u64VirAddr: 0x%llx, u32Stride: %d, u32Width: %d, u32Height: %d, u32Reserved: %d\n",
                                pstDst->u64PhyAddr,
                                pstDst->u64VirAddr,
                                pstDst->u32Stride,
                                pstDst->u32Width,
                                pstDst->u32Height,
                                pstDst->u32Reserved);
    printf("=====>ctrl: enMode: %d, u64Val: %lld, u8HorSegSize: %d, u8ElemSize: %d, u8VerSegRows: %d, u16CrpX0: %d, u16CrpY0: %d\n",
                                pstDmaCtrl->enMode,
                                pstDmaCtrl->u64Val,
                                pstDmaCtrl->u8HorSegSize,
                                pstDmaCtrl->u8ElemSize,
                                pstDmaCtrl->u8VerSegRows,
                                pstDmaCtrl->u16CrpX0,
                                pstDmaCtrl->u16CrpY0);
    printf("=====>bInstant: %d\n", bInstant);

    // only for test
    pstDst->u64PhyAddr = 0x11000000 + *pIveHandle;
    pstDst->u64VirAddr = 0x22000000 + *pIveHandle;

    return AXCL_SUCC;
}

AXCL_EXPORT AX_S32 AXCL_IVE_Add(AX_IVE_HANDLE *pIveHandle, AX_IVE_SRC_IMAGE_T *pstSrc1, AX_IVE_SRC_IMAGE_T *pstSrc2,
                                AX_IVE_DST_IMAGE_T *pstDst, AX_IVE_ADD_CTRL_T *pstAddCtrl, AX_BOOL bInstant) {
    CHECK_NULL_POINTER(pIveHandle);
    CHECK_NULL_POINTER(pstSrc1);
    CHECK_NULL_POINTER(pstSrc2);
    CHECK_NULL_POINTER(pstDst);
    CHECK_NULL_POINTER(pstAddCtrl);

    *pIveHandle = 2;

    printf("=====>%s:\n", __func__);
    printf("=====>created handle: %d\n", *pIveHandle);
    printf("=====>src1: au64PhyAddr: [0x%llx, 0x%llx, 0x%llx], au64VirAddr: [0x%llx, 0x%llx, 0x%llx], au32Stride: [%d, %d, %d], u32Width: %d, u32Height: %d, enType: %d\n",
                                pstSrc1->au64PhyAddr[0], pstSrc1->au64PhyAddr[1], pstSrc1->au64PhyAddr[2],
                                pstSrc1->au64VirAddr[0], pstSrc1->au64VirAddr[1], pstSrc1->au64VirAddr[2],
                                pstSrc1->au32Stride[0], pstSrc1->au32Stride[1], pstSrc1->au32Stride[2],
                                pstSrc1->u32Width,
                                pstSrc1->u32Height,
                                pstSrc1->enType);
    printf("=====>src2: au64PhyAddr: [0x%llx, 0x%llx, 0x%llx], au64VirAddr: [0x%llx, 0x%llx, 0x%llx], au32Stride: [%d, %d, %d], u32Width: %d, u32Height: %d, enType: %d\n",
                                pstSrc2->au64PhyAddr[0], pstSrc2->au64PhyAddr[1], pstSrc2->au64PhyAddr[2],
                                pstSrc2->au64VirAddr[0], pstSrc2->au64VirAddr[1], pstSrc2->au64VirAddr[2],
                                pstSrc2->au32Stride[0], pstSrc2->au32Stride[1], pstSrc2->au32Stride[2],
                                pstSrc2->u32Width,
                                pstSrc2->u32Height,
                                pstSrc2->enType);
    printf("=====>dst: au64PhyAddr: [0x%llx, 0x%llx, 0x%llx], au64VirAddr: [0x%llx, 0x%llx, 0x%llx], au32Stride: [%d, %d, %d], u32Width: %d, u32Height: %d, enType: %d\n",
                                pstDst->au64PhyAddr[0], pstDst->au64PhyAddr[1], pstDst->au64PhyAddr[2],
                                pstDst->au64VirAddr[0], pstDst->au64VirAddr[1], pstDst->au64VirAddr[2],
                                pstDst->au32Stride[0], pstDst->au32Stride[1], pstDst->au32Stride[2],
                                pstDst->u32Width,
                                pstDst->u32Height,
                                pstDst->enType);
    printf("=====>ctrl: u1q7X: %d, u1q7Y: %d\n", pstAddCtrl->u1q7X, pstAddCtrl->u1q7Y);
    printf("=====>bInstant: %d\n", bInstant);

    // only for test
    pstDst->au64PhyAddr[0] = 0x11000000 + *pIveHandle;
    pstDst->au64PhyAddr[1] = 0x12000000 + *pIveHandle;
    pstDst->au64PhyAddr[2] = 0x13000000 + *pIveHandle;
    pstDst->au64VirAddr[0] = 0x21000000 + *pIveHandle;
    pstDst->au64VirAddr[1] = 0x22000000 + *pIveHandle;
    pstDst->au64VirAddr[2] = 0x23000000 + *pIveHandle;

    return AXCL_SUCC;
}

AXCL_EXPORT AX_S32 AXCL_IVE_Sub(AX_IVE_HANDLE *pIveHandle, AX_IVE_SRC_IMAGE_T *pstSrc1, AX_IVE_SRC_IMAGE_T *pstSrc2,
                                AX_IVE_DST_IMAGE_T *pstDst, AX_IVE_SUB_CTRL_T *pstSubCtrl, AX_BOOL bInstant) {
    CHECK_NULL_POINTER(pIveHandle);
    CHECK_NULL_POINTER(pstSrc1);
    CHECK_NULL_POINTER(pstSrc2);
    CHECK_NULL_POINTER(pstDst);
    CHECK_NULL_POINTER(pstSubCtrl);

    *pIveHandle = 3;

    printf("=====>%s:\n", __func__);
    printf("=====>created handle: %d\n", *pIveHandle);
    printf("=====>src1: au64PhyAddr: [0x%llx, 0x%llx, 0x%llx], au64VirAddr: [0x%llx, 0x%llx, 0x%llx], au32Stride: [%d, %d, %d], u32Width: %d, u32Height: %d, enType: %d\n",
                                pstSrc1->au64PhyAddr[0], pstSrc1->au64PhyAddr[1], pstSrc1->au64PhyAddr[2],
                                pstSrc1->au64VirAddr[0], pstSrc1->au64VirAddr[1], pstSrc1->au64VirAddr[2],
                                pstSrc1->au32Stride[0], pstSrc1->au32Stride[1], pstSrc1->au32Stride[2],
                                pstSrc1->u32Width,
                                pstSrc1->u32Height,
                                pstSrc1->enType);
    printf("=====>src2: au64PhyAddr: [0x%llx, 0x%llx, 0x%llx], au64VirAddr: [0x%llx, 0x%llx, 0x%llx], au32Stride: [%d, %d, %d], u32Width: %d, u32Height: %d, enType: %d\n",
                                pstSrc2->au64PhyAddr[0], pstSrc2->au64PhyAddr[1], pstSrc2->au64PhyAddr[2],
                                pstSrc2->au64VirAddr[0], pstSrc2->au64VirAddr[1], pstSrc2->au64VirAddr[2],
                                pstSrc2->au32Stride[0], pstSrc2->au32Stride[1], pstSrc2->au32Stride[2],
                                pstSrc2->u32Width,
                                pstSrc2->u32Height,
                                pstSrc2->enType);
    printf("=====>dst: au64PhyAddr: [0x%llx, 0x%llx, 0x%llx], au64VirAddr: [0x%llx, 0x%llx, 0x%llx], au32Stride: [%d, %d, %d], u32Width: %d, u32Height: %d, enType: %d\n",
                                pstDst->au64PhyAddr[0], pstDst->au64PhyAddr[1], pstDst->au64PhyAddr[2],
                                pstDst->au64VirAddr[0], pstDst->au64VirAddr[1], pstDst->au64VirAddr[2],
                                pstDst->au32Stride[0], pstDst->au32Stride[1], pstDst->au32Stride[2],
                                pstDst->u32Width,
                                pstDst->u32Height,
                                pstDst->enType);
    printf("=====>ctrl: enMode: %d\n", pstSubCtrl->enMode);
    printf("=====>bInstant: %d\n", bInstant);

    // only for test
    pstDst->au64PhyAddr[0] = 0x11000000 + *pIveHandle;
    pstDst->au64PhyAddr[1] = 0x12000000 + *pIveHandle;
    pstDst->au64PhyAddr[2] = 0x13000000 + *pIveHandle;
    pstDst->au64VirAddr[0] = 0x21000000 + *pIveHandle;
    pstDst->au64VirAddr[1] = 0x22000000 + *pIveHandle;
    pstDst->au64VirAddr[2] = 0x23000000 + *pIveHandle;

    return AXCL_SUCC;
}

AXCL_EXPORT AX_S32 AXCL_IVE_And(AX_IVE_HANDLE *pIveHandle, AX_IVE_SRC_IMAGE_T *pstSrc1, AX_IVE_SRC_IMAGE_T *pstSrc2,
                                AX_IVE_DST_IMAGE_T *pstDst, AX_BOOL bInstant) {
    CHECK_NULL_POINTER(pIveHandle);
    CHECK_NULL_POINTER(pstSrc1);
    CHECK_NULL_POINTER(pstSrc2);
    CHECK_NULL_POINTER(pstDst);

    *pIveHandle = 4;

    printf("=====>%s:\n", __func__);
    printf("=====>created handle: %d\n", *pIveHandle);
    printf("=====>src1: au64PhyAddr: [0x%llx, 0x%llx, 0x%llx], au64VirAddr: [0x%llx, 0x%llx, 0x%llx], au32Stride: [%d, %d, %d], u32Width: %d, u32Height: %d, enType: %d\n",
                                pstSrc1->au64PhyAddr[0], pstSrc1->au64PhyAddr[1], pstSrc1->au64PhyAddr[2],
                                pstSrc1->au64VirAddr[0], pstSrc1->au64VirAddr[1], pstSrc1->au64VirAddr[2],
                                pstSrc1->au32Stride[0], pstSrc1->au32Stride[1], pstSrc1->au32Stride[2],
                                pstSrc1->u32Width,
                                pstSrc1->u32Height,
                                pstSrc1->enType);
    printf("=====>src2: au64PhyAddr: [0x%llx, 0x%llx, 0x%llx], au64VirAddr: [0x%llx, 0x%llx, 0x%llx], au32Stride: [%d, %d, %d], u32Width: %d, u32Height: %d, enType: %d\n",
                                pstSrc2->au64PhyAddr[0], pstSrc2->au64PhyAddr[1], pstSrc2->au64PhyAddr[2],
                                pstSrc2->au64VirAddr[0], pstSrc2->au64VirAddr[1], pstSrc2->au64VirAddr[2],
                                pstSrc2->au32Stride[0], pstSrc2->au32Stride[1], pstSrc2->au32Stride[2],
                                pstSrc2->u32Width,
                                pstSrc2->u32Height,
                                pstSrc2->enType);
    printf("=====>dst: au64PhyAddr: [0x%llx, 0x%llx, 0x%llx], au64VirAddr: [0x%llx, 0x%llx, 0x%llx], au32Stride: [%d, %d, %d], u32Width: %d, u32Height: %d, enType: %d\n",
                                pstDst->au64PhyAddr[0], pstDst->au64PhyAddr[1], pstDst->au64PhyAddr[2],
                                pstDst->au64VirAddr[0], pstDst->au64VirAddr[1], pstDst->au64VirAddr[2],
                                pstDst->au32Stride[0], pstDst->au32Stride[1], pstDst->au32Stride[2],
                                pstDst->u32Width,
                                pstDst->u32Height,
                                pstDst->enType);
    printf("=====>bInstant: %d\n", bInstant);

    // only for test
    pstDst->au64PhyAddr[0] = 0x11000000 + *pIveHandle;
    pstDst->au64PhyAddr[1] = 0x12000000 + *pIveHandle;
    pstDst->au64PhyAddr[2] = 0x13000000 + *pIveHandle;
    pstDst->au64VirAddr[0] = 0x21000000 + *pIveHandle;
    pstDst->au64VirAddr[1] = 0x22000000 + *pIveHandle;
    pstDst->au64VirAddr[2] = 0x23000000 + *pIveHandle;

    return AXCL_SUCC;
}

AXCL_EXPORT AX_S32 AXCL_IVE_Or(AX_IVE_HANDLE *pIveHandle, AX_IVE_SRC_IMAGE_T *pstSrc1, AX_IVE_SRC_IMAGE_T *pstSrc2,
                               AX_IVE_DST_IMAGE_T *pstDst, AX_BOOL bInstant) {
    CHECK_NULL_POINTER(pIveHandle);
    CHECK_NULL_POINTER(pstSrc1);
    CHECK_NULL_POINTER(pstSrc2);
    CHECK_NULL_POINTER(pstDst);

    *pIveHandle = 5;

    printf("=====>%s:\n", __func__);
    printf("=====>created handle: %d\n", *pIveHandle);
    printf("=====>src1: au64PhyAddr: [0x%llx, 0x%llx, 0x%llx], au64VirAddr: [0x%llx, 0x%llx, 0x%llx], au32Stride: [%d, %d, %d], u32Width: %d, u32Height: %d, enType: %d\n",
                                pstSrc1->au64PhyAddr[0], pstSrc1->au64PhyAddr[1], pstSrc1->au64PhyAddr[2],
                                pstSrc1->au64VirAddr[0], pstSrc1->au64VirAddr[1], pstSrc1->au64VirAddr[2],
                                pstSrc1->au32Stride[0], pstSrc1->au32Stride[1], pstSrc1->au32Stride[2],
                                pstSrc1->u32Width,
                                pstSrc1->u32Height,
                                pstSrc1->enType);
    printf("=====>src2: au64PhyAddr: [0x%llx, 0x%llx, 0x%llx], au64VirAddr: [0x%llx, 0x%llx, 0x%llx], au32Stride: [%d, %d, %d], u32Width: %d, u32Height: %d, enType: %d\n",
                                pstSrc2->au64PhyAddr[0], pstSrc2->au64PhyAddr[1], pstSrc2->au64PhyAddr[2],
                                pstSrc2->au64VirAddr[0], pstSrc2->au64VirAddr[1], pstSrc2->au64VirAddr[2],
                                pstSrc2->au32Stride[0], pstSrc2->au32Stride[1], pstSrc2->au32Stride[2],
                                pstSrc2->u32Width,
                                pstSrc2->u32Height,
                                pstSrc2->enType);
    printf("=====>dst: au64PhyAddr: [0x%llx, 0x%llx, 0x%llx], au64VirAddr: [0x%llx, 0x%llx, 0x%llx], au32Stride: [%d, %d, %d], u32Width: %d, u32Height: %d, enType: %d\n",
                                pstDst->au64PhyAddr[0], pstDst->au64PhyAddr[1], pstDst->au64PhyAddr[2],
                                pstDst->au64VirAddr[0], pstDst->au64VirAddr[1], pstDst->au64VirAddr[2],
                                pstDst->au32Stride[0], pstDst->au32Stride[1], pstDst->au32Stride[2],
                                pstDst->u32Width,
                                pstDst->u32Height,
                                pstDst->enType);
    printf("=====>bInstant: %d\n", bInstant);

    // only for test
    pstDst->au64PhyAddr[0] = 0x11000000 + *pIveHandle;
    pstDst->au64PhyAddr[1] = 0x12000000 + *pIveHandle;
    pstDst->au64PhyAddr[2] = 0x13000000 + *pIveHandle;
    pstDst->au64VirAddr[0] = 0x21000000 + *pIveHandle;
    pstDst->au64VirAddr[1] = 0x22000000 + *pIveHandle;
    pstDst->au64VirAddr[2] = 0x23000000 + *pIveHandle;

    return AXCL_SUCC;
}

AXCL_EXPORT AX_S32 AXCL_IVE_Xor(AX_IVE_HANDLE *pIveHandle, AX_IVE_SRC_IMAGE_T *pstSrc1, AX_IVE_SRC_IMAGE_T *pstSrc2,
                                AX_IVE_DST_IMAGE_T *pstDst, AX_BOOL bInstant) {
    CHECK_NULL_POINTER(pIveHandle);
    CHECK_NULL_POINTER(pstSrc1);
    CHECK_NULL_POINTER(pstSrc2);
    CHECK_NULL_POINTER(pstDst);

    *pIveHandle = 6;

    printf("=====>%s:\n", __func__);
    printf("=====>created handle: %d\n", *pIveHandle);
    printf("=====>src1: au64PhyAddr: [0x%llx, 0x%llx, 0x%llx], au64VirAddr: [0x%llx, 0x%llx, 0x%llx], au32Stride: [%d, %d, %d], u32Width: %d, u32Height: %d, enType: %d\n",
                                pstSrc1->au64PhyAddr[0], pstSrc1->au64PhyAddr[1], pstSrc1->au64PhyAddr[2],
                                pstSrc1->au64VirAddr[0], pstSrc1->au64VirAddr[1], pstSrc1->au64VirAddr[2],
                                pstSrc1->au32Stride[0], pstSrc1->au32Stride[1], pstSrc1->au32Stride[2],
                                pstSrc1->u32Width,
                                pstSrc1->u32Height,
                                pstSrc1->enType);
    printf("=====>src2: au64PhyAddr: [0x%llx, 0x%llx, 0x%llx], au64VirAddr: [0x%llx, 0x%llx, 0x%llx], au32Stride: [%d, %d, %d], u32Width: %d, u32Height: %d, enType: %d\n",
                                pstSrc2->au64PhyAddr[0], pstSrc2->au64PhyAddr[1], pstSrc2->au64PhyAddr[2],
                                pstSrc2->au64VirAddr[0], pstSrc2->au64VirAddr[1], pstSrc2->au64VirAddr[2],
                                pstSrc2->au32Stride[0], pstSrc2->au32Stride[1], pstSrc2->au32Stride[2],
                                pstSrc2->u32Width,
                                pstSrc2->u32Height,
                                pstSrc2->enType);
    printf("=====>dst: au64PhyAddr: [0x%llx, 0x%llx, 0x%llx], au64VirAddr: [0x%llx, 0x%llx, 0x%llx], au32Stride: [%d, %d, %d], u32Width: %d, u32Height: %d, enType: %d\n",
                                pstDst->au64PhyAddr[0], pstDst->au64PhyAddr[1], pstDst->au64PhyAddr[2],
                                pstDst->au64VirAddr[0], pstDst->au64VirAddr[1], pstDst->au64VirAddr[2],
                                pstDst->au32Stride[0], pstDst->au32Stride[1], pstDst->au32Stride[2],
                                pstDst->u32Width,
                                pstDst->u32Height,
                                pstDst->enType);
    printf("=====>bInstant: %d\n", bInstant);

    // only for test
    pstDst->au64PhyAddr[0] = 0x11000000 + *pIveHandle;
    pstDst->au64PhyAddr[1] = 0x12000000 + *pIveHandle;
    pstDst->au64PhyAddr[2] = 0x13000000 + *pIveHandle;
    pstDst->au64VirAddr[0] = 0x21000000 + *pIveHandle;
    pstDst->au64VirAddr[1] = 0x22000000 + *pIveHandle;
    pstDst->au64VirAddr[2] = 0x23000000 + *pIveHandle;

    return AXCL_SUCC;
}

AXCL_EXPORT AX_S32 AXCL_IVE_Mse(AX_IVE_HANDLE *pIveHandle, AX_IVE_SRC_IMAGE_T *pstSrc1, AX_IVE_SRC_IMAGE_T *pstSrc2,
                                AX_IVE_DST_IMAGE_T *pstDst, AX_IVE_MSE_CTRL_T *pstMseCtrl, AX_BOOL bInstant) {
    CHECK_NULL_POINTER(pIveHandle);
    CHECK_NULL_POINTER(pstSrc1);
    CHECK_NULL_POINTER(pstSrc2);
    CHECK_NULL_POINTER(pstDst);
    CHECK_NULL_POINTER(pstMseCtrl);

    *pIveHandle = 7;

    printf("=====>%s:\n", __func__);
    printf("=====>created handle: %d\n", *pIveHandle);
    printf("=====>src1: au64PhyAddr: [0x%llx, 0x%llx, 0x%llx], au64VirAddr: [0x%llx, 0x%llx, 0x%llx], au32Stride: [%d, %d, %d], u32Width: %d, u32Height: %d, enType: %d\n",
                                pstSrc1->au64PhyAddr[0], pstSrc1->au64PhyAddr[1], pstSrc1->au64PhyAddr[2],
                                pstSrc1->au64VirAddr[0], pstSrc1->au64VirAddr[1], pstSrc1->au64VirAddr[2],
                                pstSrc1->au32Stride[0], pstSrc1->au32Stride[1], pstSrc1->au32Stride[2],
                                pstSrc1->u32Width,
                                pstSrc1->u32Height,
                                pstSrc1->enType);
    printf("=====>src2: au64PhyAddr: [0x%llx, 0x%llx, 0x%llx], au64VirAddr: [0x%llx, 0x%llx, 0x%llx], au32Stride: [%d, %d, %d], u32Width: %d, u32Height: %d, enType: %d\n",
                                pstSrc2->au64PhyAddr[0], pstSrc2->au64PhyAddr[1], pstSrc2->au64PhyAddr[2],
                                pstSrc2->au64VirAddr[0], pstSrc2->au64VirAddr[1], pstSrc2->au64VirAddr[2],
                                pstSrc2->au32Stride[0], pstSrc2->au32Stride[1], pstSrc2->au32Stride[2],
                                pstSrc2->u32Width,
                                pstSrc2->u32Height,
                                pstSrc2->enType);
    printf("=====>dst: au64PhyAddr: [0x%llx, 0x%llx, 0x%llx], au64VirAddr: [0x%llx, 0x%llx, 0x%llx], au32Stride: [%d, %d, %d], u32Width: %d, u32Height: %d, enType: %d\n",
                                pstDst->au64PhyAddr[0], pstDst->au64PhyAddr[1], pstDst->au64PhyAddr[2],
                                pstDst->au64VirAddr[0], pstDst->au64VirAddr[1], pstDst->au64VirAddr[2],
                                pstDst->au32Stride[0], pstDst->au32Stride[1], pstDst->au32Stride[2],
                                pstDst->u32Width,
                                pstDst->u32Height,
                                pstDst->enType);
    printf("=====>ctrl: u1q15MseCoef: %d\n", pstMseCtrl->u1q15MseCoef);
    printf("=====>bInstant: %d\n", bInstant);

    // only for test
    pstDst->au64PhyAddr[0] = 0x11000000 + *pIveHandle;
    pstDst->au64PhyAddr[1] = 0x12000000 + *pIveHandle;
    pstDst->au64PhyAddr[2] = 0x13000000 + *pIveHandle;
    pstDst->au64VirAddr[0] = 0x21000000 + *pIveHandle;
    pstDst->au64VirAddr[1] = 0x22000000 + *pIveHandle;
    pstDst->au64VirAddr[2] = 0x23000000 + *pIveHandle;

    return AXCL_SUCC;
}

AXCL_EXPORT AX_S32 AXCL_IVE_CannyHysEdge(AX_IVE_HANDLE *pIveHandle, AX_IVE_SRC_IMAGE_T *pstSrc1, AX_IVE_SRC_IMAGE_T *pstSrc2,
                                         AX_IVE_DST_IMAGE_T *pstDst, AX_IVE_HYS_EDGE_CTRL_T *pstCannyHysEdgeCtrl, AX_BOOL bInstant) {
    CHECK_NULL_POINTER(pIveHandle);
    CHECK_NULL_POINTER(pstSrc1);
    CHECK_NULL_POINTER(pstSrc2);
    CHECK_NULL_POINTER(pstDst);
    CHECK_NULL_POINTER(pstCannyHysEdgeCtrl);

    *pIveHandle = 8;

    printf("=====>%s:\n", __func__);
    printf("=====>created handle: %d\n", *pIveHandle);
    printf("=====>src1: au64PhyAddr: [0x%llx, 0x%llx, 0x%llx], au64VirAddr: [0x%llx, 0x%llx, 0x%llx], au32Stride: [%d, %d, %d], u32Width: %d, u32Height: %d, enType: %d\n",
                                pstSrc1->au64PhyAddr[0], pstSrc1->au64PhyAddr[1], pstSrc1->au64PhyAddr[2],
                                pstSrc1->au64VirAddr[0], pstSrc1->au64VirAddr[1], pstSrc1->au64VirAddr[2],
                                pstSrc1->au32Stride[0], pstSrc1->au32Stride[1], pstSrc1->au32Stride[2],
                                pstSrc1->u32Width,
                                pstSrc1->u32Height,
                                pstSrc1->enType);
    printf("=====>src2: au64PhyAddr: [0x%llx, 0x%llx, 0x%llx], au64VirAddr: [0x%llx, 0x%llx, 0x%llx], au32Stride: [%d, %d, %d], u32Width: %d, u32Height: %d, enType: %d\n",
                                pstSrc2->au64PhyAddr[0], pstSrc2->au64PhyAddr[1], pstSrc2->au64PhyAddr[2],
                                pstSrc2->au64VirAddr[0], pstSrc2->au64VirAddr[1], pstSrc2->au64VirAddr[2],
                                pstSrc2->au32Stride[0], pstSrc2->au32Stride[1], pstSrc2->au32Stride[2],
                                pstSrc2->u32Width,
                                pstSrc2->u32Height,
                                pstSrc2->enType);
    printf("=====>dst: au64PhyAddr: [0x%llx, 0x%llx, 0x%llx], au64VirAddr: [0x%llx, 0x%llx, 0x%llx], au32Stride: [%d, %d, %d], u32Width: %d, u32Height: %d, enType: %d\n",
                                pstDst->au64PhyAddr[0], pstDst->au64PhyAddr[1], pstDst->au64PhyAddr[2],
                                pstDst->au64VirAddr[0], pstDst->au64VirAddr[1], pstDst->au64VirAddr[2],
                                pstDst->au32Stride[0], pstDst->au32Stride[1], pstDst->au32Stride[2],
                                pstDst->u32Width,
                                pstDst->u32Height,
                                pstDst->enType);
    printf("=====>ctrl: u16LowThr: %d, u16HighThr: %d\n", pstCannyHysEdgeCtrl->u16LowThr, pstCannyHysEdgeCtrl->u16HighThr);
    printf("=====>bInstant: %d\n", bInstant);

    // only for test
    pstDst->au64PhyAddr[0] = 0x11000000 + *pIveHandle;
    pstDst->au64PhyAddr[1] = 0x12000000 + *pIveHandle;
    pstDst->au64PhyAddr[2] = 0x13000000 + *pIveHandle;
    pstDst->au64VirAddr[0] = 0x21000000 + *pIveHandle;
    pstDst->au64VirAddr[1] = 0x22000000 + *pIveHandle;
    pstDst->au64VirAddr[2] = 0x23000000 + *pIveHandle;

    return AXCL_SUCC;
}

AXCL_EXPORT AX_S32 AXCL_IVE_CannyEdge(AX_IVE_HANDLE *pIveHandle, AX_IVE_SRC_IMAGE_T *pstSrc, AX_IVE_DST_IMAGE_T *pstDst,
                                      AX_IVE_CANNY_EDGE_CTRL_T *pstCannyEdgeCtrl, AX_BOOL bInstant) {
    CHECK_NULL_POINTER(pIveHandle);
    CHECK_NULL_POINTER(pstSrc);
    CHECK_NULL_POINTER(pstDst);
    CHECK_NULL_POINTER(pstCannyEdgeCtrl);

    *pIveHandle = 9;

    printf("=====>%s:\n", __func__);
    printf("=====>created handle: %d\n", *pIveHandle);
    printf("=====>src: au64PhyAddr: [0x%llx, 0x%llx, 0x%llx], au64VirAddr: [0x%llx, 0x%llx, 0x%llx], au32Stride: [%d, %d, %d], u32Width: %d, u32Height: %d, enType: %d\n",
                                pstSrc->au64PhyAddr[0], pstSrc->au64PhyAddr[1], pstSrc->au64PhyAddr[2],
                                pstSrc->au64VirAddr[0], pstSrc->au64VirAddr[1], pstSrc->au64VirAddr[2],
                                pstSrc->au32Stride[0], pstSrc->au32Stride[1], pstSrc->au32Stride[2],
                                pstSrc->u32Width,
                                pstSrc->u32Height,
                                pstSrc->enType);
    printf("=====>dst: au64PhyAddr: [0x%llx, 0x%llx, 0x%llx], au64VirAddr: [0x%llx, 0x%llx, 0x%llx], au32Stride: [%d, %d, %d], u32Width: %d, u32Height: %d, enType: %d\n",
                                pstDst->au64PhyAddr[0], pstDst->au64PhyAddr[1], pstDst->au64PhyAddr[2],
                                pstDst->au64VirAddr[0], pstDst->au64VirAddr[1], pstDst->au64VirAddr[2],
                                pstDst->au32Stride[0], pstDst->au32Stride[1], pstDst->au32Stride[2],
                                pstDst->u32Width,
                                pstDst->u32Height,
                                pstDst->enType);
    printf("=====>ctrl: u8Thr: %d\n", pstCannyEdgeCtrl->u8Thr);
    printf("=====>bInstant: %d\n", bInstant);

    // only for test
    pstDst->au64PhyAddr[0] = 0x11000000 + *pIveHandle;
    pstDst->au64PhyAddr[1] = 0x12000000 + *pIveHandle;
    pstDst->au64PhyAddr[2] = 0x13000000 + *pIveHandle;
    pstDst->au64VirAddr[0] = 0x21000000 + *pIveHandle;
    pstDst->au64VirAddr[1] = 0x22000000 + *pIveHandle;
    pstDst->au64VirAddr[2] = 0x23000000 + *pIveHandle;

    return AXCL_SUCC;
}

AXCL_EXPORT AX_S32 AXCL_IVE_CCL(AX_IVE_HANDLE *pIveHandle, AX_IVE_SRC_IMAGE_T *pstSrc, AX_IVE_DST_IMAGE_T *pstDst,
                                AX_IVE_DST_MEM_INFO_T *pstBlob, AX_IVE_CCL_CTRL_T *pstCclCtrl, AX_BOOL bInstant) {
    CHECK_NULL_POINTER(pIveHandle);
    CHECK_NULL_POINTER(pstSrc);
    CHECK_NULL_POINTER(pstDst);
    CHECK_NULL_POINTER(pstBlob);
    CHECK_NULL_POINTER(pstCclCtrl);

    *pIveHandle = 10;

    printf("=====>%s:\n", __func__);
    printf("=====>created handle: %d\n", *pIveHandle);
    printf("=====>src: au64PhyAddr: [0x%llx, 0x%llx, 0x%llx], au64VirAddr: [0x%llx, 0x%llx, 0x%llx], au32Stride: [%d, %d, %d], u32Width: %d, u32Height: %d, enType: %d\n",
                                pstSrc->au64PhyAddr[0], pstSrc->au64PhyAddr[1], pstSrc->au64PhyAddr[2],
                                pstSrc->au64VirAddr[0], pstSrc->au64VirAddr[1], pstSrc->au64VirAddr[2],
                                pstSrc->au32Stride[0], pstSrc->au32Stride[1], pstSrc->au32Stride[2],
                                pstSrc->u32Width,
                                pstSrc->u32Height,
                                pstSrc->enType);
    printf("=====>dst: au64PhyAddr: [0x%llx, 0x%llx, 0x%llx], au64VirAddr: [0x%llx, 0x%llx, 0x%llx], au32Stride: [%d, %d, %d], u32Width: %d, u32Height: %d, enType: %d\n",
                                pstDst->au64PhyAddr[0], pstDst->au64PhyAddr[1], pstDst->au64PhyAddr[2],
                                pstDst->au64VirAddr[0], pstDst->au64VirAddr[1], pstDst->au64VirAddr[2],
                                pstDst->au32Stride[0], pstDst->au32Stride[1], pstDst->au32Stride[2],
                                pstDst->u32Width,
                                pstDst->u32Height,
                                pstDst->enType);
    printf("=====>dst blob: u64PhyAddr: 0x%llx, u64VirAddr: 0x%llx, u32Size: %d\n", pstBlob->u64PhyAddr, pstBlob->u64VirAddr, pstBlob->u32Size);
    printf("=====>ctrl: enMode: %d\n", pstCclCtrl->enMode);
    printf("=====>bInstant: %d\n", bInstant);

    // only for test
    pstDst->au64PhyAddr[0] = 0x11000000 + *pIveHandle;
    pstDst->au64PhyAddr[1] = 0x12000000 + *pIveHandle;
    pstDst->au64PhyAddr[2] = 0x13000000 + *pIveHandle;
    pstDst->au64VirAddr[0] = 0x21000000 + *pIveHandle;
    pstDst->au64VirAddr[1] = 0x22000000 + *pIveHandle;
    pstDst->au64VirAddr[2] = 0x23000000 + *pIveHandle;

    pstBlob->u64PhyAddr = 0x31000000 + *pIveHandle;;
    pstBlob->u64VirAddr = 0x32000000 + *pIveHandle;;
    pstBlob->u32Size = 0x1000;

    return AXCL_SUCC;
}

AXCL_EXPORT AX_S32 AXCL_IVE_Erode(AX_IVE_HANDLE *pIveHandle, AX_IVE_SRC_IMAGE_T *pstSrc, AX_IVE_DST_IMAGE_T *pstDst,
                                  AX_IVE_ERODE_CTRL_T *pstErodeCtrl, AX_BOOL bInstant) {
    CHECK_NULL_POINTER(pIveHandle);
    CHECK_NULL_POINTER(pstSrc);
    CHECK_NULL_POINTER(pstDst);
    CHECK_NULL_POINTER(pstErodeCtrl);

    *pIveHandle = 11;

    printf("=====>%s:\n", __func__);
    printf("=====>created handle: %d\n", *pIveHandle);
    printf("=====>src: au64PhyAddr: [0x%llx, 0x%llx, 0x%llx], au64VirAddr: [0x%llx, 0x%llx, 0x%llx], au32Stride: [%d, %d, %d], u32Width: %d, u32Height: %d, enType: %d\n",
                                pstSrc->au64PhyAddr[0], pstSrc->au64PhyAddr[1], pstSrc->au64PhyAddr[2],
                                pstSrc->au64VirAddr[0], pstSrc->au64VirAddr[1], pstSrc->au64VirAddr[2],
                                pstSrc->au32Stride[0], pstSrc->au32Stride[1], pstSrc->au32Stride[2],
                                pstSrc->u32Width,
                                pstSrc->u32Height,
                                pstSrc->enType);
    printf("=====>dst: au64PhyAddr: [0x%llx, 0x%llx, 0x%llx], au64VirAddr: [0x%llx, 0x%llx, 0x%llx], au32Stride: [%d, %d, %d], u32Width: %d, u32Height: %d, enType: %d\n",
                                pstDst->au64PhyAddr[0], pstDst->au64PhyAddr[1], pstDst->au64PhyAddr[2],
                                pstDst->au64VirAddr[0], pstDst->au64VirAddr[1], pstDst->au64VirAddr[2],
                                pstDst->au32Stride[0], pstDst->au32Stride[1], pstDst->au32Stride[2],
                                pstDst->u32Width,
                                pstDst->u32Height,
                                pstDst->enType);
    printf("=====>ctrl: au8Mask: [");
    for (size_t i = 0; i < 25; i ++) {
        printf("0x%02x", pstErodeCtrl->au8Mask[i]);
        if (i < 24) {
            printf(", ");
        }
    }
    printf("]\n");
    printf("=====>bInstant: %d\n", bInstant);

    // only for test
    pstDst->au64PhyAddr[0] = 0x11000000 + *pIveHandle;
    pstDst->au64PhyAddr[1] = 0x12000000 + *pIveHandle;
    pstDst->au64PhyAddr[2] = 0x13000000 + *pIveHandle;
    pstDst->au64VirAddr[0] = 0x21000000 + *pIveHandle;
    pstDst->au64VirAddr[1] = 0x22000000 + *pIveHandle;
    pstDst->au64VirAddr[2] = 0x23000000 + *pIveHandle;

    return AXCL_SUCC;
}

AXCL_EXPORT AX_S32 AXCL_IVE_Dilate(AX_IVE_HANDLE *pIveHandle, AX_IVE_SRC_IMAGE_T *pstSrc, AX_IVE_DST_IMAGE_T *pstDst,
                                   AX_IVE_DILATE_CTRL_T *pstDilateCtrl, AX_BOOL bInstant) {
    CHECK_NULL_POINTER(pIveHandle);
    CHECK_NULL_POINTER(pstSrc);
    CHECK_NULL_POINTER(pstDst);
    CHECK_NULL_POINTER(pstDilateCtrl);

    *pIveHandle = 12;

    printf("=====>%s:\n", __func__);
    printf("=====>created handle: %d\n", *pIveHandle);
    printf("=====>src: au64PhyAddr: [0x%llx, 0x%llx, 0x%llx], au64VirAddr: [0x%llx, 0x%llx, 0x%llx], au32Stride: [%d, %d, %d], u32Width: %d, u32Height: %d, enType: %d\n",
                                pstSrc->au64PhyAddr[0], pstSrc->au64PhyAddr[1], pstSrc->au64PhyAddr[2],
                                pstSrc->au64VirAddr[0], pstSrc->au64VirAddr[1], pstSrc->au64VirAddr[2],
                                pstSrc->au32Stride[0], pstSrc->au32Stride[1], pstSrc->au32Stride[2],
                                pstSrc->u32Width,
                                pstSrc->u32Height,
                                pstSrc->enType);
    printf("=====>dst: au64PhyAddr: [0x%llx, 0x%llx, 0x%llx], au64VirAddr: [0x%llx, 0x%llx, 0x%llx], au32Stride: [%d, %d, %d], u32Width: %d, u32Height: %d, enType: %d\n",
                                pstDst->au64PhyAddr[0], pstDst->au64PhyAddr[1], pstDst->au64PhyAddr[2],
                                pstDst->au64VirAddr[0], pstDst->au64VirAddr[1], pstDst->au64VirAddr[2],
                                pstDst->au32Stride[0], pstDst->au32Stride[1], pstDst->au32Stride[2],
                                pstDst->u32Width,
                                pstDst->u32Height,
                                pstDst->enType);
    printf("=====>ctrl: au8Mask: [");
    for (size_t i = 0; i < 25; i ++) {
        printf("0x%02x", pstDilateCtrl->au8Mask[i]);
        if (i < 24) {
            printf(", ");
        }
    }
    printf("]\n");
    printf("=====>bInstant: %d\n", bInstant);

    // only for test
    pstDst->au64PhyAddr[0] = 0x11000000 + *pIveHandle;
    pstDst->au64PhyAddr[1] = 0x12000000 + *pIveHandle;
    pstDst->au64PhyAddr[2] = 0x13000000 + *pIveHandle;
    pstDst->au64VirAddr[0] = 0x21000000 + *pIveHandle;
    pstDst->au64VirAddr[1] = 0x22000000 + *pIveHandle;
    pstDst->au64VirAddr[2] = 0x23000000 + *pIveHandle;

    return AXCL_SUCC;
}

AXCL_EXPORT AX_S32 AXCL_IVE_Filter(AX_IVE_HANDLE *pIveHandle, AX_IVE_SRC_IMAGE_T *pstSrc, AX_IVE_DST_IMAGE_T *pstDst,
                                   AX_IVE_FILTER_CTRL_T *pstFltCtrl, AX_BOOL bInstant) {
    CHECK_NULL_POINTER(pIveHandle);
    CHECK_NULL_POINTER(pstSrc);
    CHECK_NULL_POINTER(pstDst);
    CHECK_NULL_POINTER(pstFltCtrl);

    *pIveHandle = 13;

    printf("=====>%s:\n", __func__);
    printf("=====>created handle: %d\n", *pIveHandle);
    printf("=====>src: au64PhyAddr: [0x%llx, 0x%llx, 0x%llx], au64VirAddr: [0x%llx, 0x%llx, 0x%llx], au32Stride: [%d, %d, %d], u32Width: %d, u32Height: %d, enType: %d\n",
                                pstSrc->au64PhyAddr[0], pstSrc->au64PhyAddr[1], pstSrc->au64PhyAddr[2],
                                pstSrc->au64VirAddr[0], pstSrc->au64VirAddr[1], pstSrc->au64VirAddr[2],
                                pstSrc->au32Stride[0], pstSrc->au32Stride[1], pstSrc->au32Stride[2],
                                pstSrc->u32Width,
                                pstSrc->u32Height,
                                pstSrc->enType);
    printf("=====>dst: au64PhyAddr: [0x%llx, 0x%llx, 0x%llx], au64VirAddr: [0x%llx, 0x%llx, 0x%llx], au32Stride: [%d, %d, %d], u32Width: %d, u32Height: %d, enType: %d\n",
                                pstDst->au64PhyAddr[0], pstDst->au64PhyAddr[1], pstDst->au64PhyAddr[2],
                                pstDst->au64VirAddr[0], pstDst->au64VirAddr[1], pstDst->au64VirAddr[2],
                                pstDst->au32Stride[0], pstDst->au32Stride[1], pstDst->au32Stride[2],
                                pstDst->u32Width,
                                pstDst->u32Height,
                                pstDst->enType);
    printf("=====>ctrl: au8Mask: [");
    for (size_t i = 0; i < 25; i ++) {
        printf("0x%02x", pstFltCtrl->as6q10Mask[i]);
        if (i < 24) {
            printf(", ");
        }
    }
    printf("]\n");
    printf("=====>bInstant: %d\n", bInstant);

    // only for test
    pstDst->au64PhyAddr[0] = 0x11000000 + *pIveHandle;
    pstDst->au64PhyAddr[1] = 0x12000000 + *pIveHandle;
    pstDst->au64PhyAddr[2] = 0x13000000 + *pIveHandle;
    pstDst->au64VirAddr[0] = 0x21000000 + *pIveHandle;
    pstDst->au64VirAddr[1] = 0x22000000 + *pIveHandle;
    pstDst->au64VirAddr[2] = 0x23000000 + *pIveHandle;

    return AXCL_SUCC;
}

AXCL_EXPORT AX_S32 AXCL_IVE_Hist(AX_IVE_HANDLE *pIveHandle, AX_IVE_SRC_IMAGE_T *pstSrc, AX_IVE_DST_MEM_INFO_T *pstDst, AX_BOOL bInstant) {
    CHECK_NULL_POINTER(pIveHandle);
    CHECK_NULL_POINTER(pstSrc);
    CHECK_NULL_POINTER(pstDst);

    *pIveHandle = 14;

    printf("=====>%s:\n", __func__);
    printf("=====>created handle: %d\n", *pIveHandle);
    printf("=====>src: au64PhyAddr: [0x%llx, 0x%llx, 0x%llx], au64VirAddr: [0x%llx, 0x%llx, 0x%llx], au32Stride: [%d, %d, %d], u32Width: %d, u32Height: %d, enType: %d\n",
                                pstSrc->au64PhyAddr[0], pstSrc->au64PhyAddr[1], pstSrc->au64PhyAddr[2],
                                pstSrc->au64VirAddr[0], pstSrc->au64VirAddr[1], pstSrc->au64VirAddr[2],
                                pstSrc->au32Stride[0], pstSrc->au32Stride[1], pstSrc->au32Stride[2],
                                pstSrc->u32Width,
                                pstSrc->u32Height,
                                pstSrc->enType);
    printf("=====>dst blob: u64PhyAddr: 0x%llx, u64VirAddr: 0x%llx, u32Size: %d\n", pstDst->u64PhyAddr, pstDst->u64VirAddr, pstDst->u32Size);
    printf("=====>bInstant: %d\n", bInstant);

    // only for test
    pstDst->u64PhyAddr = 0x31000000 + *pIveHandle;;
    pstDst->u64VirAddr = 0x32000000 + *pIveHandle;;
    pstDst->u32Size = 0x1000;

    return AXCL_SUCC;
}

AXCL_EXPORT AX_S32 AXCL_IVE_EqualizeHist(AX_IVE_HANDLE *pIveHandle, AX_IVE_SRC_IMAGE_T *pstSrc, AX_IVE_DST_MEM_INFO_T *pstDst,
                                         AX_IVE_EQUALIZE_HIST_CTRL_T *pstEqualizeHistCtrl, AX_BOOL bInstant) {
    CHECK_NULL_POINTER(pIveHandle);
    CHECK_NULL_POINTER(pstSrc);
    CHECK_NULL_POINTER(pstDst);
    CHECK_NULL_POINTER(pstEqualizeHistCtrl);

    *pIveHandle = 15;

    printf("=====>%s:\n", __func__);
    printf("=====>created handle: %d\n", *pIveHandle);
    printf("=====>src: au64PhyAddr: [0x%llx, 0x%llx, 0x%llx], au64VirAddr: [0x%llx, 0x%llx, 0x%llx], au32Stride: [%d, %d, %d], u32Width: %d, u32Height: %d, enType: %d\n",
                                pstSrc->au64PhyAddr[0], pstSrc->au64PhyAddr[1], pstSrc->au64PhyAddr[2],
                                pstSrc->au64VirAddr[0], pstSrc->au64VirAddr[1], pstSrc->au64VirAddr[2],
                                pstSrc->au32Stride[0], pstSrc->au32Stride[1], pstSrc->au32Stride[2],
                                pstSrc->u32Width,
                                pstSrc->u32Height,
                                pstSrc->enType);
    printf("=====>dst blob: u64PhyAddr: 0x%llx, u64VirAddr: 0x%llx, u32Size: %d\n", pstDst->u64PhyAddr, pstDst->u64VirAddr, pstDst->u32Size);
    printf("=====>ctrl: u0q20HistEqualCoef: %d\n", pstEqualizeHistCtrl->u0q20HistEqualCoef);
    printf("=====>bInstant: %d\n", bInstant);

    // only for test
    pstDst->u64PhyAddr = 0x31000000 + *pIveHandle;;
    pstDst->u64VirAddr = 0x32000000 + *pIveHandle;;
    pstDst->u32Size = 0x1000;

    return AXCL_SUCC;
}

AXCL_EXPORT AX_S32 AXCL_IVE_Integ(AX_IVE_HANDLE *pIveHandle, AX_IVE_SRC_IMAGE_T *pstSrc, AX_IVE_DST_IMAGE_T *pstDst,
                                  AX_IVE_INTEG_CTRL_T *pstIntegCtrl, AX_BOOL bInstant) {
    CHECK_NULL_POINTER(pIveHandle);
    CHECK_NULL_POINTER(pstSrc);
    CHECK_NULL_POINTER(pstDst);
    CHECK_NULL_POINTER(pstIntegCtrl);

    *pIveHandle = 16;

    printf("=====>%s:\n", __func__);
    printf("=====>created handle: %d\n", *pIveHandle);
    printf("=====>src: au64PhyAddr: [0x%llx, 0x%llx, 0x%llx], au64VirAddr: [0x%llx, 0x%llx, 0x%llx], au32Stride: [%d, %d, %d], u32Width: %d, u32Height: %d, enType: %d\n",
                                pstSrc->au64PhyAddr[0], pstSrc->au64PhyAddr[1], pstSrc->au64PhyAddr[2],
                                pstSrc->au64VirAddr[0], pstSrc->au64VirAddr[1], pstSrc->au64VirAddr[2],
                                pstSrc->au32Stride[0], pstSrc->au32Stride[1], pstSrc->au32Stride[2],
                                pstSrc->u32Width,
                                pstSrc->u32Height,
                                pstSrc->enType);
    printf("=====>dst: au64PhyAddr: [0x%llx, 0x%llx, 0x%llx], au64VirAddr: [0x%llx, 0x%llx, 0x%llx], au32Stride: [%d, %d, %d], u32Width: %d, u32Height: %d, enType: %d\n",
                                pstDst->au64PhyAddr[0], pstDst->au64PhyAddr[1], pstDst->au64PhyAddr[2],
                                pstDst->au64VirAddr[0], pstDst->au64VirAddr[1], pstDst->au64VirAddr[2],
                                pstDst->au32Stride[0], pstDst->au32Stride[1], pstDst->au32Stride[2],
                                pstDst->u32Width,
                                pstDst->u32Height,
                                pstDst->enType);
    printf("=====>ctrl: enOutCtrl: %d\n", pstIntegCtrl->enOutCtrl);
    printf("=====>bInstant: %d\n", bInstant);

    // only for test
    pstDst->au64PhyAddr[0] = 0x11000000 + *pIveHandle;
    pstDst->au64PhyAddr[1] = 0x12000000 + *pIveHandle;
    pstDst->au64PhyAddr[2] = 0x13000000 + *pIveHandle;
    pstDst->au64VirAddr[0] = 0x21000000 + *pIveHandle;
    pstDst->au64VirAddr[1] = 0x22000000 + *pIveHandle;
    pstDst->au64VirAddr[2] = 0x23000000 + *pIveHandle;

    return AXCL_SUCC;
}

AXCL_EXPORT AX_S32 AXCL_IVE_MagAndAng(AX_IVE_HANDLE *pIveHandle, AX_IVE_SRC_IMAGE_T *pstSrc1, AX_IVE_SRC_IMAGE_T *pstSrc2,
                                      AX_IVE_DST_IMAGE_T *pstDstMag, AX_IVE_DST_IMAGE_T *pstDstAng, AX_BOOL bInstant) {
    CHECK_NULL_POINTER(pIveHandle);
    CHECK_NULL_POINTER(pstSrc1);
    CHECK_NULL_POINTER(pstSrc2);
    CHECK_NULL_POINTER(pstDstMag);
    CHECK_NULL_POINTER(pstDstAng);

    *pIveHandle = 17;

    printf("=====>%s:\n", __func__);
    printf("=====>created handle: %d\n", *pIveHandle);
    printf("=====>src1: au64PhyAddr: [0x%llx, 0x%llx, 0x%llx], au64VirAddr: [0x%llx, 0x%llx, 0x%llx], au32Stride: [%d, %d, %d], u32Width: %d, u32Height: %d, enType: %d\n",
                                pstSrc1->au64PhyAddr[0], pstSrc1->au64PhyAddr[1], pstSrc1->au64PhyAddr[2],
                                pstSrc1->au64VirAddr[0], pstSrc1->au64VirAddr[1], pstSrc1->au64VirAddr[2],
                                pstSrc1->au32Stride[0], pstSrc1->au32Stride[1], pstSrc1->au32Stride[2],
                                pstSrc1->u32Width,
                                pstSrc1->u32Height,
                                pstSrc1->enType);
    printf("=====>src2: au64PhyAddr: [0x%llx, 0x%llx, 0x%llx], au64VirAddr: [0x%llx, 0x%llx, 0x%llx], au32Stride: [%d, %d, %d], u32Width: %d, u32Height: %d, enType: %d\n",
                                pstSrc2->au64PhyAddr[0], pstSrc2->au64PhyAddr[1], pstSrc2->au64PhyAddr[2],
                                pstSrc2->au64VirAddr[0], pstSrc2->au64VirAddr[1], pstSrc2->au64VirAddr[2],
                                pstSrc2->au32Stride[0], pstSrc2->au32Stride[1], pstSrc2->au32Stride[2],
                                pstSrc2->u32Width,
                                pstSrc2->u32Height,
                                pstSrc2->enType);
    printf("=====>dst_mag: au64PhyAddr: [0x%llx, 0x%llx, 0x%llx], au64VirAddr: [0x%llx, 0x%llx, 0x%llx], au32Stride: [%d, %d, %d], u32Width: %d, u32Height: %d, enType: %d\n",
                                pstDstMag->au64PhyAddr[0], pstDstMag->au64PhyAddr[1], pstDstMag->au64PhyAddr[2],
                                pstDstMag->au64VirAddr[0], pstDstMag->au64VirAddr[1], pstDstMag->au64VirAddr[2],
                                pstDstMag->au32Stride[0], pstDstMag->au32Stride[1], pstDstMag->au32Stride[2],
                                pstDstMag->u32Width,
                                pstDstMag->u32Height,
                                pstDstMag->enType);
    printf("=====>dst_ang: au64PhyAddr: [0x%llx, 0x%llx, 0x%llx], au64VirAddr: [0x%llx, 0x%llx, 0x%llx], au32Stride: [%d, %d, %d], u32Width: %d, u32Height: %d, enType: %d\n",
                                pstDstAng->au64PhyAddr[0], pstDstAng->au64PhyAddr[1], pstDstAng->au64PhyAddr[2],
                                pstDstAng->au64VirAddr[0], pstDstAng->au64VirAddr[1], pstDstAng->au64VirAddr[2],
                                pstDstAng->au32Stride[0], pstDstAng->au32Stride[1], pstDstAng->au32Stride[2],
                                pstDstAng->u32Width,
                                pstDstAng->u32Height,
                                pstDstAng->enType);
    printf("=====>bInstant: %d\n", bInstant);

    // only for test
    pstDstMag->au64PhyAddr[0] = 0x11000000 + *pIveHandle;
    pstDstMag->au64PhyAddr[1] = 0x12000000 + *pIveHandle;
    pstDstMag->au64PhyAddr[2] = 0x13000000 + *pIveHandle;
    pstDstMag->au64VirAddr[0] = 0x21000000 + *pIveHandle;
    pstDstMag->au64VirAddr[1] = 0x22000000 + *pIveHandle;
    pstDstMag->au64VirAddr[2] = 0x23000000 + *pIveHandle;

    pstDstAng->au64PhyAddr[0] = 0x31000000 + *pIveHandle;
    pstDstAng->au64PhyAddr[1] = 0x32000000 + *pIveHandle;
    pstDstAng->au64PhyAddr[2] = 0x33000000 + *pIveHandle;
    pstDstAng->au64VirAddr[0] = 0x41000000 + *pIveHandle;
    pstDstAng->au64VirAddr[1] = 0x42000000 + *pIveHandle;
    pstDstAng->au64VirAddr[2] = 0x43000000 + *pIveHandle;

    return AXCL_SUCC;
}

AXCL_EXPORT AX_S32 AXCL_IVE_Sobel(AX_IVE_HANDLE *pIveHandle, AX_IVE_SRC_IMAGE_T *pstSrc, AX_IVE_DST_IMAGE_T *pstDst,
                                  AX_IVE_SOBEL_CTRL_T *pstSobelCtrl, AX_BOOL bInstant) {
    CHECK_NULL_POINTER(pIveHandle);
    CHECK_NULL_POINTER(pstSrc);
    CHECK_NULL_POINTER(pstDst);
    CHECK_NULL_POINTER(pstSobelCtrl);

    *pIveHandle = 18;

    printf("=====>%s:\n", __func__);
    printf("=====>created handle: %d\n", *pIveHandle);
    printf("=====>src: au64PhyAddr: [0x%llx, 0x%llx, 0x%llx], au64VirAddr: [0x%llx, 0x%llx, 0x%llx], au32Stride: [%d, %d, %d], u32Width: %d, u32Height: %d, enType: %d\n",
                                pstSrc->au64PhyAddr[0], pstSrc->au64PhyAddr[1], pstSrc->au64PhyAddr[2],
                                pstSrc->au64VirAddr[0], pstSrc->au64VirAddr[1], pstSrc->au64VirAddr[2],
                                pstSrc->au32Stride[0], pstSrc->au32Stride[1], pstSrc->au32Stride[2],
                                pstSrc->u32Width,
                                pstSrc->u32Height,
                                pstSrc->enType);
    printf("=====>dst: au64PhyAddr: [0x%llx, 0x%llx, 0x%llx], au64VirAddr: [0x%llx, 0x%llx, 0x%llx], au32Stride: [%d, %d, %d], u32Width: %d, u32Height: %d, enType: %d\n",
                                pstDst->au64PhyAddr[0], pstDst->au64PhyAddr[1], pstDst->au64PhyAddr[2],
                                pstDst->au64VirAddr[0], pstDst->au64VirAddr[1], pstDst->au64VirAddr[2],
                                pstDst->au32Stride[0], pstDst->au32Stride[1], pstDst->au32Stride[2],
                                pstDst->u32Width,
                                pstDst->u32Height,
                                pstDst->enType);
    printf("=====>ctrl: au8Mask: [");
    for (size_t i = 0; i < 25; i ++) {
        printf("0x%02x", pstSobelCtrl->as6q10Mask[i]);
        if (i < 24) {
            printf(", ");
        }
    }
    printf("]\n");
    printf("=====>bInstant: %d\n", bInstant);

    // only for test
    pstDst->au64PhyAddr[0] = 0x11000000 + *pIveHandle;
    pstDst->au64PhyAddr[1] = 0x12000000 + *pIveHandle;
    pstDst->au64PhyAddr[2] = 0x13000000 + *pIveHandle;
    pstDst->au64VirAddr[0] = 0x21000000 + *pIveHandle;
    pstDst->au64VirAddr[1] = 0x22000000 + *pIveHandle;
    pstDst->au64VirAddr[2] = 0x23000000 + *pIveHandle;

    return AXCL_SUCC;
}

AXCL_EXPORT AX_S32 AXCL_IVE_GMM(AX_IVE_HANDLE *pIveHandle, AX_IVE_SRC_IMAGE_T *pstSrc, AX_IVE_DST_IMAGE_T *pstFg, AX_IVE_DST_IMAGE_T *pstBg,
                                AX_IVE_MEM_INFO_T *pstModel, AX_IVE_GMM_CTRL_T *pstGmmCtrl, AX_BOOL bInstant) {
    CHECK_NULL_POINTER(pIveHandle);
    CHECK_NULL_POINTER(pstSrc);
    CHECK_NULL_POINTER(pstFg);
    CHECK_NULL_POINTER(pstBg);
    CHECK_NULL_POINTER(pstModel);
    CHECK_NULL_POINTER(pstGmmCtrl);

    *pIveHandle = 19;

    printf("=====>%s:\n", __func__);
    printf("=====>created handle: %d\n", *pIveHandle);
    printf("=====>src: au64PhyAddr: [0x%llx, 0x%llx, 0x%llx], au64VirAddr: [0x%llx, 0x%llx, 0x%llx], au32Stride: [%d, %d, %d], u32Width: %d, u32Height: %d, enType: %d\n",
                                pstSrc->au64PhyAddr[0], pstSrc->au64PhyAddr[1], pstSrc->au64PhyAddr[2],
                                pstSrc->au64VirAddr[0], pstSrc->au64VirAddr[1], pstSrc->au64VirAddr[2],
                                pstSrc->au32Stride[0], pstSrc->au32Stride[1], pstSrc->au32Stride[2],
                                pstSrc->u32Width,
                                pstSrc->u32Height,
                                pstSrc->enType);
    printf("=====>dst_fg: au64PhyAddr: [0x%llx, 0x%llx, 0x%llx], au64VirAddr: [0x%llx, 0x%llx, 0x%llx], au32Stride: [%d, %d, %d], u32Width: %d, u32Height: %d, enType: %d\n",
                                pstFg->au64PhyAddr[0], pstFg->au64PhyAddr[1], pstFg->au64PhyAddr[2],
                                pstFg->au64VirAddr[0], pstFg->au64VirAddr[1], pstFg->au64VirAddr[2],
                                pstFg->au32Stride[0], pstFg->au32Stride[1], pstFg->au32Stride[2],
                                pstFg->u32Width,
                                pstFg->u32Height,
                                pstFg->enType);
    printf("=====>dst_bg: au64PhyAddr: [0x%llx, 0x%llx, 0x%llx], au64VirAddr: [0x%llx, 0x%llx, 0x%llx], au32Stride: [%d, %d, %d], u32Width: %d, u32Height: %d, enType: %d\n",
                                pstBg->au64PhyAddr[0], pstBg->au64PhyAddr[1], pstBg->au64PhyAddr[2],
                                pstBg->au64VirAddr[0], pstBg->au64VirAddr[1], pstBg->au64VirAddr[2],
                                pstBg->au32Stride[0], pstBg->au32Stride[1], pstBg->au32Stride[2],
                                pstBg->u32Width,
                                pstBg->u32Height,
                                pstBg->enType);
    printf("=====>model: u64PhyAddr: 0x%llx, u64VirAddr: 0x%llx, u32Size: %d\n", pstModel->u64PhyAddr, pstModel->u64VirAddr, pstModel->u32Size);
    printf("=====>bInstant: %d\n", bInstant);

    // only for test
    pstFg->au64PhyAddr[0] = 0x11000000 + *pIveHandle;
    pstFg->au64PhyAddr[1] = 0x12000000 + *pIveHandle;
    pstFg->au64PhyAddr[2] = 0x13000000 + *pIveHandle;
    pstFg->au64VirAddr[0] = 0x21000000 + *pIveHandle;
    pstFg->au64VirAddr[1] = 0x22000000 + *pIveHandle;
    pstFg->au64VirAddr[2] = 0x23000000 + *pIveHandle;

    pstBg->au64PhyAddr[0] = 0x31000000 + *pIveHandle;
    pstBg->au64PhyAddr[1] = 0x32000000 + *pIveHandle;
    pstBg->au64PhyAddr[2] = 0x33000000 + *pIveHandle;
    pstBg->au64VirAddr[0] = 0x41000000 + *pIveHandle;
    pstBg->au64VirAddr[1] = 0x42000000 + *pIveHandle;
    pstBg->au64VirAddr[2] = 0x43000000 + *pIveHandle;

    return AXCL_SUCC;
}

AXCL_EXPORT AX_S32 AXCL_IVE_GMM2(AX_IVE_HANDLE *pIveHandle, AX_IVE_SRC_IMAGE_T *pstSrc, AX_IVE_DST_IMAGE_T *pstFg,
                                 AX_IVE_DST_IMAGE_T *pstBg, AX_IVE_MEM_INFO_T *pstModel, AX_IVE_GMM2_CTRL_T *pstGmm2Ctrl,
                                 AX_BOOL bInstant) {
    CHECK_NULL_POINTER(pIveHandle);
    CHECK_NULL_POINTER(pstSrc);
    CHECK_NULL_POINTER(pstFg);
    CHECK_NULL_POINTER(pstBg);
    CHECK_NULL_POINTER(pstModel);
    CHECK_NULL_POINTER(pstGmm2Ctrl);

    *pIveHandle = 20;

    printf("=====>%s:\n", __func__);
    printf("=====>created handle: %d\n", *pIveHandle);
    printf("=====>src: au64PhyAddr: [0x%llx, 0x%llx, 0x%llx], au64VirAddr: [0x%llx, 0x%llx, 0x%llx], au32Stride: [%d, %d, %d], u32Width: %d, u32Height: %d, enType: %d\n",
                                pstSrc->au64PhyAddr[0], pstSrc->au64PhyAddr[1], pstSrc->au64PhyAddr[2],
                                pstSrc->au64VirAddr[0], pstSrc->au64VirAddr[1], pstSrc->au64VirAddr[2],
                                pstSrc->au32Stride[0], pstSrc->au32Stride[1], pstSrc->au32Stride[2],
                                pstSrc->u32Width,
                                pstSrc->u32Height,
                                pstSrc->enType);
    printf("=====>dst_fg: au64PhyAddr: [0x%llx, 0x%llx, 0x%llx], au64VirAddr: [0x%llx, 0x%llx, 0x%llx], au32Stride: [%d, %d, %d], u32Width: %d, u32Height: %d, enType: %d\n",
                                pstFg->au64PhyAddr[0], pstFg->au64PhyAddr[1], pstFg->au64PhyAddr[2],
                                pstFg->au64VirAddr[0], pstFg->au64VirAddr[1], pstFg->au64VirAddr[2],
                                pstFg->au32Stride[0], pstFg->au32Stride[1], pstFg->au32Stride[2],
                                pstFg->u32Width,
                                pstFg->u32Height,
                                pstFg->enType);
    printf("=====>dst_bg: au64PhyAddr: [0x%llx, 0x%llx, 0x%llx], au64VirAddr: [0x%llx, 0x%llx, 0x%llx], au32Stride: [%d, %d, %d], u32Width: %d, u32Height: %d, enType: %d\n",
                                pstBg->au64PhyAddr[0], pstBg->au64PhyAddr[1], pstBg->au64PhyAddr[2],
                                pstBg->au64VirAddr[0], pstBg->au64VirAddr[1], pstBg->au64VirAddr[2],
                                pstBg->au32Stride[0], pstBg->au32Stride[1], pstBg->au32Stride[2],
                                pstBg->u32Width,
                                pstBg->u32Height,
                                pstBg->enType);
    printf("=====>model: u64PhyAddr: 0x%llx, u64VirAddr: 0x%llx, u32Size: %d\n", pstModel->u64PhyAddr, pstModel->u64VirAddr, pstModel->u32Size);
    printf("=====>ctrl: u14q4InitVar: %d, u14q4MinVar: %d, u14q4MaxVar: %d, u1q7LearnRate: %d, u1q7BgRatio: %d, u4q4VarThr: %d, u4q4VarThrCheck: %d, s1q7CT: %d, u8Thr: %d\n",
                                pstGmm2Ctrl->u14q4InitVar,
                                pstGmm2Ctrl->u14q4MinVar,
                                pstGmm2Ctrl->u14q4MaxVar,
                                pstGmm2Ctrl->u1q7LearnRate,
                                pstGmm2Ctrl->u1q7BgRatio,
                                pstGmm2Ctrl->u4q4VarThr,
                                pstGmm2Ctrl->u4q4VarThrCheck,
                                pstGmm2Ctrl->s1q7CT,
                                pstGmm2Ctrl->u8Thr);
    printf("=====>bInstant: %d\n", bInstant);

    // only for test
    pstFg->au64PhyAddr[0] = 0x11000000 + *pIveHandle;
    pstFg->au64PhyAddr[1] = 0x12000000 + *pIveHandle;
    pstFg->au64PhyAddr[2] = 0x13000000 + *pIveHandle;
    pstFg->au64VirAddr[0] = 0x21000000 + *pIveHandle;
    pstFg->au64VirAddr[1] = 0x22000000 + *pIveHandle;
    pstFg->au64VirAddr[2] = 0x23000000 + *pIveHandle;

    pstBg->au64PhyAddr[0] = 0x31000000 + *pIveHandle;
    pstBg->au64PhyAddr[1] = 0x32000000 + *pIveHandle;
    pstBg->au64PhyAddr[2] = 0x33000000 + *pIveHandle;
    pstBg->au64VirAddr[0] = 0x41000000 + *pIveHandle;
    pstBg->au64VirAddr[1] = 0x42000000 + *pIveHandle;
    pstBg->au64VirAddr[2] = 0x43000000 + *pIveHandle;

    return AXCL_SUCC;
}

AXCL_EXPORT AX_S32 AXCL_IVE_Thresh(AX_IVE_HANDLE *pIveHandle, AX_IVE_SRC_IMAGE_T *pstSrc, AX_IVE_DST_IMAGE_T *pstDst,
                                   AX_IVE_THRESH_CTRL_T *pstThrCtrl, AX_BOOL bInstant) {
    CHECK_NULL_POINTER(pIveHandle);
    CHECK_NULL_POINTER(pstSrc);
    CHECK_NULL_POINTER(pstDst);
    CHECK_NULL_POINTER(pstThrCtrl);

    *pIveHandle = 21;

    printf("=====>%s:\n", __func__);
    printf("=====>created handle: %d\n", *pIveHandle);
    printf("=====>src: au64PhyAddr: [0x%llx, 0x%llx, 0x%llx], au64VirAddr: [0x%llx, 0x%llx, 0x%llx], au32Stride: [%d, %d, %d], u32Width: %d, u32Height: %d, enType: %d\n",
                                pstSrc->au64PhyAddr[0], pstSrc->au64PhyAddr[1], pstSrc->au64PhyAddr[2],
                                pstSrc->au64VirAddr[0], pstSrc->au64VirAddr[1], pstSrc->au64VirAddr[2],
                                pstSrc->au32Stride[0], pstSrc->au32Stride[1], pstSrc->au32Stride[2],
                                pstSrc->u32Width,
                                pstSrc->u32Height,
                                pstSrc->enType);
    printf("=====>dst: au64PhyAddr: [0x%llx, 0x%llx, 0x%llx], au64VirAddr: [0x%llx, 0x%llx, 0x%llx], au32Stride: [%d, %d, %d], u32Width: %d, u32Height: %d, enType: %d\n",
                                pstDst->au64PhyAddr[0], pstDst->au64PhyAddr[1], pstDst->au64PhyAddr[2],
                                pstDst->au64VirAddr[0], pstDst->au64VirAddr[1], pstDst->au64VirAddr[2],
                                pstDst->au32Stride[0], pstDst->au32Stride[1], pstDst->au32Stride[2],
                                pstDst->u32Width,
                                pstDst->u32Height,
                                pstDst->enType);
    printf("=====>ctrl: enMode: %d, u8LowThr: %d, u8HighThr: %d, u8MinVal: %d, u8MidVal: %d, u8MaxVal: %d\n",
                                pstThrCtrl->enMode,
                                pstThrCtrl->u8LowThr,
                                pstThrCtrl->u8HighThr,
                                pstThrCtrl->u8MinVal,
                                pstThrCtrl->u8MidVal,
                                pstThrCtrl->u8MaxVal);
    printf("=====>bInstant: %d\n", bInstant);

    // only for test
    pstDst->au64PhyAddr[0] = 0x11000000 + *pIveHandle;
    pstDst->au64PhyAddr[1] = 0x12000000 + *pIveHandle;
    pstDst->au64PhyAddr[2] = 0x13000000 + *pIveHandle;
    pstDst->au64VirAddr[0] = 0x21000000 + *pIveHandle;
    pstDst->au64VirAddr[1] = 0x22000000 + *pIveHandle;
    pstDst->au64VirAddr[2] = 0x23000000 + *pIveHandle;

    return AXCL_SUCC;
}

AXCL_EXPORT AX_S32 AXCL_IVE_16BitTo8Bit(AX_IVE_HANDLE *pIveHandle, AX_IVE_SRC_IMAGE_T *pstSrc, AX_IVE_DST_IMAGE_T *pstDst,
                                        AX_IVE_16BIT_TO_8BIT_CTRL_T *pst16BitTo8BitCtrl, AX_BOOL bInstant) {
    CHECK_NULL_POINTER(pIveHandle);
    CHECK_NULL_POINTER(pstSrc);
    CHECK_NULL_POINTER(pstDst);
    CHECK_NULL_POINTER(pst16BitTo8BitCtrl);

    *pIveHandle = 22;

    printf("=====>%s:\n", __func__);
    printf("=====>created handle: %d\n", *pIveHandle);
    printf("=====>src: au64PhyAddr: [0x%llx, 0x%llx, 0x%llx], au64VirAddr: [0x%llx, 0x%llx, 0x%llx], au32Stride: [%d, %d, %d], u32Width: %d, u32Height: %d, enType: %d\n",
                                pstSrc->au64PhyAddr[0], pstSrc->au64PhyAddr[1], pstSrc->au64PhyAddr[2],
                                pstSrc->au64VirAddr[0], pstSrc->au64VirAddr[1], pstSrc->au64VirAddr[2],
                                pstSrc->au32Stride[0], pstSrc->au32Stride[1], pstSrc->au32Stride[2],
                                pstSrc->u32Width,
                                pstSrc->u32Height,
                                pstSrc->enType);
    printf("=====>dst: au64PhyAddr: [0x%llx, 0x%llx, 0x%llx], au64VirAddr: [0x%llx, 0x%llx, 0x%llx], au32Stride: [%d, %d, %d], u32Width: %d, u32Height: %d, enType: %d\n",
                                pstDst->au64PhyAddr[0], pstDst->au64PhyAddr[1], pstDst->au64PhyAddr[2],
                                pstDst->au64VirAddr[0], pstDst->au64VirAddr[1], pstDst->au64VirAddr[2],
                                pstDst->au32Stride[0], pstDst->au32Stride[1], pstDst->au32Stride[2],
                                pstDst->u32Width,
                                pstDst->u32Height,
                                pstDst->enType);
    printf("=====>ctrl: enMode: %d, s1q14Gain: %d, s1q14Gain: %d\n",
                                pst16BitTo8BitCtrl->enMode,
                                pst16BitTo8BitCtrl->s1q14Gain,
                                pst16BitTo8BitCtrl->s16Bias);
    printf("=====>bInstant: %d\n", bInstant);

    // only for test
    pstDst->au64PhyAddr[0] = 0x11000000 + *pIveHandle;
    pstDst->au64PhyAddr[1] = 0x12000000 + *pIveHandle;
    pstDst->au64PhyAddr[2] = 0x13000000 + *pIveHandle;
    pstDst->au64VirAddr[0] = 0x21000000 + *pIveHandle;
    pstDst->au64VirAddr[1] = 0x22000000 + *pIveHandle;
    pstDst->au64VirAddr[2] = 0x23000000 + *pIveHandle;

    return AXCL_SUCC;
}

AXCL_EXPORT AX_S32 AXCL_IVE_CropImage(AX_IVE_HANDLE *pIveHandle, AX_IVE_SRC_IMAGE_T *pstSrc, AX_IVE_DST_IMAGE_T *pastDst[],
                                      AX_IVE_RECT_U16_T *pastSrcBoxs[], AX_IVE_CROP_IMAGE_CTRL_T *pstCropImageCtrl,
                                      AX_IVE_ENGINE_E enEngine, AX_BOOL bInstant) {
    CHECK_NULL_POINTER(pIveHandle);
    CHECK_NULL_POINTER(pstSrc);
    CHECK_NULL_POINTER(pastDst);
    CHECK_NULL_POINTER(pastSrcBoxs);
    CHECK_NULL_POINTER(pstCropImageCtrl);

    *pIveHandle = 23;

    printf("=====>%s:\n", __func__);
    printf("=====>created handle: %d\n", *pIveHandle);
    printf("=====>src: au64PhyAddr: [0x%llx, 0x%llx, 0x%llx], au64VirAddr: [0x%llx, 0x%llx, 0x%llx], au32Stride: [%d, %d, %d], u32Width: %d, u32Height: %d, enType: %d\n",
                                pstSrc->au64PhyAddr[0], pstSrc->au64PhyAddr[1], pstSrc->au64PhyAddr[2],
                                pstSrc->au64VirAddr[0], pstSrc->au64VirAddr[1], pstSrc->au64VirAddr[2],
                                pstSrc->au32Stride[0], pstSrc->au32Stride[1], pstSrc->au32Stride[2],
                                pstSrc->u32Width,
                                pstSrc->u32Height,
                                pstSrc->enType);

    for (size_t i = 0; i < pstCropImageCtrl->u16Num; i++) {
        printf("=====>dst[%ld]: au64PhyAddr: [0x%llx, 0x%llx, 0x%llx], au64VirAddr: [0x%llx, 0x%llx, 0x%llx], au32Stride: [%d, %d, %d], u32Width: %d, u32Height: %d, enType: %d\n",
                                    i,
                                    pastDst[i]->au64PhyAddr[0], pastDst[i]->au64PhyAddr[1], pastDst[i]->au64PhyAddr[2],
                                    pastDst[i]->au64VirAddr[0], pastDst[i]->au64VirAddr[1], pastDst[i]->au64VirAddr[2],
                                    pastDst[i]->au32Stride[0], pastDst[i]->au32Stride[1], pastDst[i]->au32Stride[2],
                                    pastDst[i]->u32Width,
                                    pastDst[i]->u32Height,
                                    pastDst[i]->enType);
    }

    for (size_t i = 0; i < pstCropImageCtrl->u16Num; i++) {
        printf("=====>box[%ld]: [x: %d, y: %d, w: %d, h: %d]\n",
                                    i,
                                    pastSrcBoxs[i]->u16X,
                                    pastSrcBoxs[i]->u16Y,
                                    pastSrcBoxs[i]->u16Width,
                                    pastSrcBoxs[i]->u16Height);
    }
    printf("=====>ctrl: num: %d\n", pstCropImageCtrl->u16Num);
    printf("=====>engine: %d\n", enEngine);
    printf("=====>bInstant: %d\n", bInstant);

    // only for test
    for (size_t i = 0; i < pstCropImageCtrl->u16Num; i++) {
        pastDst[i]->au64PhyAddr[0] = 0x01000000 + (2 * i + 1)* 0x10000000 + *pIveHandle;
        pastDst[i]->au64PhyAddr[1] = 0x02000000 + (2 * i + 1)* 0x10000000 + *pIveHandle;
        pastDst[i]->au64PhyAddr[2] = 0x03000000 + (2 * i + 1)* 0x10000000 + *pIveHandle;
        pastDst[i]->au64VirAddr[0] = 0x01000000 + (2 * i + 2)* 0x10000000 + *pIveHandle;
        pastDst[i]->au64VirAddr[1] = 0x02000000 + (2 * i + 2)* 0x10000000 + *pIveHandle;
        pastDst[i]->au64VirAddr[2] = 0x03000000 + (2 * i + 2)* 0x10000000 + *pIveHandle;
    }

    return AXCL_SUCC;
}

AXCL_EXPORT AX_S32 AXCL_IVE_CropResize(AX_IVE_HANDLE *pIveHandle, AX_IVE_SRC_IMAGE_T *pstSrc, AX_IVE_DST_IMAGE_T *pastDst[],
                                       AX_IVE_RECT_U16_T *pastSrcBoxs[], AX_IVE_CROP_RESIZE_CTRL_T *pstCropResizeCtrl,
                                       AX_IVE_ENGINE_E enEngine, AX_BOOL bInstant) {
    CHECK_NULL_POINTER(pIveHandle);
    CHECK_NULL_POINTER(pstSrc);
    CHECK_NULL_POINTER(pastDst);
    CHECK_NULL_POINTER(pastSrcBoxs);
    CHECK_NULL_POINTER(pstCropResizeCtrl);

    *pIveHandle = 24;

    printf("=====>%s:\n", __func__);
    printf("=====>created handle: %d\n", *pIveHandle);
    printf("=====>src: au64PhyAddr: [0x%llx, 0x%llx, 0x%llx], au64VirAddr: [0x%llx, 0x%llx, 0x%llx], au32Stride: [%d, %d, %d], u32Width: %d, u32Height: %d, enType: %d\n",
                                pstSrc->au64PhyAddr[0], pstSrc->au64PhyAddr[1], pstSrc->au64PhyAddr[2],
                                pstSrc->au64VirAddr[0], pstSrc->au64VirAddr[1], pstSrc->au64VirAddr[2],
                                pstSrc->au32Stride[0], pstSrc->au32Stride[1], pstSrc->au32Stride[2],
                                pstSrc->u32Width,
                                pstSrc->u32Height,
                                pstSrc->enType);

    for (size_t i = 0; i < pstCropResizeCtrl->u16Num; i++) {
        printf("=====>dst[%ld]: au64PhyAddr: [0x%llx, 0x%llx, 0x%llx], au64VirAddr: [0x%llx, 0x%llx, 0x%llx], au32Stride: [%d, %d, %d], u32Width: %d, u32Height: %d, enType: %d\n",
                                    i,
                                    pastDst[i]->au64PhyAddr[0], pastDst[i]->au64PhyAddr[1], pastDst[i]->au64PhyAddr[2],
                                    pastDst[i]->au64VirAddr[0], pastDst[i]->au64VirAddr[1], pastDst[i]->au64VirAddr[2],
                                    pastDst[i]->au32Stride[0], pastDst[i]->au32Stride[1], pastDst[i]->au32Stride[2],
                                    pastDst[i]->u32Width,
                                    pastDst[i]->u32Height,
                                    pastDst[i]->enType);
    }

    for (size_t i = 0; i < pstCropResizeCtrl->u16Num; i++) {
        printf("=====>box[%ld]: [x: %d, y: %d, w: %d, h: %d]\n",
                                    i,
                                    pastSrcBoxs[i]->u16X,
                                    pastSrcBoxs[i]->u16Y,
                                    pastSrcBoxs[i]->u16Width,
                                    pastSrcBoxs[i]->u16Height);
    }
    printf("=====>ctrl: num: %d, enAlign[%d, %d], u32BorderColor: 0x%04X\n",
                                    pstCropResizeCtrl->u16Num,
                                    pstCropResizeCtrl->enAlign[0],
                                    pstCropResizeCtrl->enAlign[1],
                                    pstCropResizeCtrl->u32BorderColor);
    printf("=====>engine: %d\n", enEngine);
    printf("=====>bInstant: %d\n", bInstant);

    // only for test
    for (size_t i = 0; i < pstCropResizeCtrl->u16Num; i++) {
        pastDst[i]->au64PhyAddr[0] = 0x01000000 + (2 * i + 1)* 0x10000000 + *pIveHandle;
        pastDst[i]->au64PhyAddr[1] = 0x02000000 + (2 * i + 1)* 0x10000000 + *pIveHandle;
        pastDst[i]->au64PhyAddr[2] = 0x03000000 + (2 * i + 1)* 0x10000000 + *pIveHandle;
        pastDst[i]->au64VirAddr[0] = 0x01000000 + (2 * i + 2)* 0x10000000 + *pIveHandle;
        pastDst[i]->au64VirAddr[1] = 0x02000000 + (2 * i + 2)* 0x10000000 + *pIveHandle;
        pastDst[i]->au64VirAddr[2] = 0x03000000 + (2 * i + 2)* 0x10000000 + *pIveHandle;
    }

    return AXCL_SUCC;
}

AXCL_EXPORT AX_S32 AXCL_IVE_CropResizeForSplitYUV(AX_IVE_HANDLE *pIveHandle, AX_IVE_SRC_IMAGE_T *pstSrc1, AX_IVE_SRC_IMAGE_T *pstSrc2,
                                                  AX_IVE_DST_IMAGE_T *pastDst1[], AX_IVE_DST_IMAGE_T *pastDst2[],
                                                  AX_IVE_RECT_U16_T *pastSrcBoxs[], AX_IVE_CROP_RESIZE_CTRL_T *pstCropResizeCtrl,
                                                  AX_IVE_ENGINE_E enEngine, AX_BOOL bInstant) {
    CHECK_NULL_POINTER(pIveHandle);
    CHECK_NULL_POINTER(pstSrc1);
    CHECK_NULL_POINTER(pstSrc2);
    CHECK_NULL_POINTER(pastDst1);
    CHECK_NULL_POINTER(pastDst2);
    CHECK_NULL_POINTER(pastSrcBoxs);
    CHECK_NULL_POINTER(pstCropResizeCtrl);

    *pIveHandle = 25;

    printf("=====>%s:\n", __func__);
    printf("=====>created handle: %d\n", *pIveHandle);
    printf("=====>src1: au64PhyAddr: [0x%llx, 0x%llx, 0x%llx], au64VirAddr: [0x%llx, 0x%llx, 0x%llx], au32Stride: [%d, %d, %d], u32Width: %d, u32Height: %d, enType: %d\n",
                                pstSrc1->au64PhyAddr[0], pstSrc1->au64PhyAddr[1], pstSrc1->au64PhyAddr[2],
                                pstSrc1->au64VirAddr[0], pstSrc1->au64VirAddr[1], pstSrc1->au64VirAddr[2],
                                pstSrc1->au32Stride[0], pstSrc1->au32Stride[1], pstSrc1->au32Stride[2],
                                pstSrc1->u32Width,
                                pstSrc1->u32Height,
                                pstSrc1->enType);

    printf("=====>src2: au64PhyAddr: [0x%llx, 0x%llx, 0x%llx], au64VirAddr: [0x%llx, 0x%llx, 0x%llx], au32Stride: [%d, %d, %d], u32Width: %d, u32Height: %d, enType: %d\n",
                                pstSrc2->au64PhyAddr[0], pstSrc2->au64PhyAddr[1], pstSrc2->au64PhyAddr[2],
                                pstSrc2->au64VirAddr[0], pstSrc2->au64VirAddr[1], pstSrc2->au64VirAddr[2],
                                pstSrc2->au32Stride[0], pstSrc2->au32Stride[1], pstSrc2->au32Stride[2],
                                pstSrc2->u32Width,
                                pstSrc2->u32Height,
                                pstSrc2->enType);

    for (size_t i = 0; i < pstCropResizeCtrl->u16Num; i++) {
        printf("=====>dst1[%ld]: au64PhyAddr: [0x%llx, 0x%llx, 0x%llx], au64VirAddr: [0x%llx, 0x%llx, 0x%llx], au32Stride: [%d, %d, %d], u32Width: %d, u32Height: %d, enType: %d\n",
                                    i,
                                    pastDst1[i]->au64PhyAddr[0], pastDst1[i]->au64PhyAddr[1], pastDst1[i]->au64PhyAddr[2],
                                    pastDst1[i]->au64VirAddr[0], pastDst1[i]->au64VirAddr[1], pastDst1[i]->au64VirAddr[2],
                                    pastDst1[i]->au32Stride[0], pastDst1[i]->au32Stride[1], pastDst1[i]->au32Stride[2],
                                    pastDst1[i]->u32Width,
                                    pastDst1[i]->u32Height,
                                    pastDst1[i]->enType);
    }

    for (size_t i = 0; i < pstCropResizeCtrl->u16Num; i++) {
        printf("=====>dst2[%ld]: au64PhyAddr: [0x%llx, 0x%llx, 0x%llx], au64VirAddr: [0x%llx, 0x%llx, 0x%llx], au32Stride: [%d, %d, %d], u32Width: %d, u32Height: %d, enType: %d\n",
                                    i,
                                    pastDst2[i]->au64PhyAddr[0], pastDst2[i]->au64PhyAddr[1], pastDst2[i]->au64PhyAddr[2],
                                    pastDst2[i]->au64VirAddr[0], pastDst2[i]->au64VirAddr[1], pastDst2[i]->au64VirAddr[2],
                                    pastDst2[i]->au32Stride[0], pastDst2[i]->au32Stride[1], pastDst2[i]->au32Stride[2],
                                    pastDst2[i]->u32Width,
                                    pastDst2[i]->u32Height,
                                    pastDst2[i]->enType);
    }

    for (size_t i = 0; i < pstCropResizeCtrl->u16Num; i++) {
        printf("=====>box[%ld]: [x: %d, y: %d, w: %d, h: %d]\n",
                                    i,
                                    pastSrcBoxs[i]->u16X,
                                    pastSrcBoxs[i]->u16Y,
                                    pastSrcBoxs[i]->u16Width,
                                    pastSrcBoxs[i]->u16Height);
    }
    printf("=====>ctrl: num: %d, enAlign[%d, %d], u32BorderColor: 0x%04X\n",
                                    pstCropResizeCtrl->u16Num,
                                    pstCropResizeCtrl->enAlign[0],
                                    pstCropResizeCtrl->enAlign[1],
                                    pstCropResizeCtrl->u32BorderColor);
    printf("=====>engine: %d\n", enEngine);
    printf("=====>bInstant: %d\n", bInstant);

    // only for test
    for (size_t i = 0; i < pstCropResizeCtrl->u16Num; i++) {
        pastDst1[i]->au64PhyAddr[0] = 0x01000000 + (2 * i + 1)* 0x10000000 + *pIveHandle;
        pastDst1[i]->au64PhyAddr[1] = 0x02000000 + (2 * i + 1)* 0x10000000 + *pIveHandle;
        pastDst1[i]->au64PhyAddr[2] = 0x03000000 + (2 * i + 1)* 0x10000000 + *pIveHandle;
        pastDst1[i]->au64VirAddr[0] = 0x01000000 + (2 * i + 2)* 0x10000000 + *pIveHandle;
        pastDst1[i]->au64VirAddr[1] = 0x02000000 + (2 * i + 2)* 0x10000000 + *pIveHandle;
        pastDst1[i]->au64VirAddr[2] = 0x03000000 + (2 * i + 2)* 0x10000000 + *pIveHandle;
    }

    for (size_t i = 0; i < pstCropResizeCtrl->u16Num; i++) {
        pastDst2[i]->au64PhyAddr[0] = 0x04000000 + (2 * i + 1)* 0x10000000 + *pIveHandle;
        pastDst2[i]->au64PhyAddr[1] = 0x05000000 + (2 * i + 1)* 0x10000000 + *pIveHandle;
        pastDst2[i]->au64PhyAddr[2] = 0x06000000 + (2 * i + 1)* 0x10000000 + *pIveHandle;
        pastDst2[i]->au64VirAddr[0] = 0x04000000 + (2 * i + 2)* 0x10000000 + *pIveHandle;
        pastDst2[i]->au64VirAddr[1] = 0x05000000 + (2 * i + 2)* 0x10000000 + *pIveHandle;
        pastDst2[i]->au64VirAddr[2] = 0x06000000 + (2 * i + 2)* 0x10000000 + *pIveHandle;
    }

    return AXCL_SUCC;
}

AXCL_EXPORT AX_S32 AXCL_IVE_CSC(AX_IVE_HANDLE *pIveHandle, AX_IVE_SRC_IMAGE_T *pstSrc, AX_IVE_DST_IMAGE_T *pstDst, AX_IVE_ENGINE_E enEngine,
                                AX_BOOL bInstant) {
    CHECK_NULL_POINTER(pIveHandle);
    CHECK_NULL_POINTER(pstSrc);
    CHECK_NULL_POINTER(pstDst);

    *pIveHandle = 26;

    printf("=====>%s:\n", __func__);
    printf("=====>created handle: %d\n", *pIveHandle);
    printf("=====>src: au64PhyAddr: [0x%llx, 0x%llx, 0x%llx], au64VirAddr: [0x%llx, 0x%llx, 0x%llx], au32Stride: [%d, %d, %d], u32Width: %d, u32Height: %d, enType: %d\n",
                                pstSrc->au64PhyAddr[0], pstSrc->au64PhyAddr[1], pstSrc->au64PhyAddr[2],
                                pstSrc->au64VirAddr[0], pstSrc->au64VirAddr[1], pstSrc->au64VirAddr[2],
                                pstSrc->au32Stride[0], pstSrc->au32Stride[1], pstSrc->au32Stride[2],
                                pstSrc->u32Width,
                                pstSrc->u32Height,
                                pstSrc->enType);
    printf("=====>dst: au64PhyAddr: [0x%llx, 0x%llx, 0x%llx], au64VirAddr: [0x%llx, 0x%llx, 0x%llx], au32Stride: [%d, %d, %d], u32Width: %d, u32Height: %d, enType: %d\n",
                                pstDst->au64PhyAddr[0], pstDst->au64PhyAddr[1], pstDst->au64PhyAddr[2],
                                pstDst->au64VirAddr[0], pstDst->au64VirAddr[1], pstDst->au64VirAddr[2],
                                pstDst->au32Stride[0], pstDst->au32Stride[1], pstDst->au32Stride[2],
                                pstDst->u32Width,
                                pstDst->u32Height,
                                pstDst->enType);
    printf("=====>engine: %d\n", enEngine);
    printf("=====>bInstant: %d\n", bInstant);

    // only for test
    pstDst->au64PhyAddr[0] = 0x11000000 + *pIveHandle;
    pstDst->au64PhyAddr[1] = 0x12000000 + *pIveHandle;
    pstDst->au64PhyAddr[2] = 0x13000000 + *pIveHandle;
    pstDst->au64VirAddr[0] = 0x21000000 + *pIveHandle;
    pstDst->au64VirAddr[1] = 0x22000000 + *pIveHandle;
    pstDst->au64VirAddr[2] = 0x23000000 + *pIveHandle;

    return AXCL_SUCC;
}

AXCL_EXPORT AX_S32 AXCL_IVE_CropResize2(AX_IVE_HANDLE *pIveHandle, AX_IVE_SRC_IMAGE_T *pstSrc, AX_IVE_IMAGE_T *pastDst[],
                                        AX_IVE_RECT_U16_T *pastSrcBoxs[], AX_IVE_RECT_U16_T *pastDstBoxs[],
                                        AX_IVE_CROP_IMAGE_CTRL_T *pstCropResize2Ctrl, AX_IVE_ENGINE_E enEngine, AX_BOOL bInstant) {
    CHECK_NULL_POINTER(pIveHandle);
    CHECK_NULL_POINTER(pstSrc);
    CHECK_NULL_POINTER(pastDst);
    CHECK_NULL_POINTER(pastSrcBoxs);
    CHECK_NULL_POINTER(pastDstBoxs);
    CHECK_NULL_POINTER(pstCropResize2Ctrl);

    *pIveHandle = 27;

    printf("=====>%s:\n", __func__);
    printf("=====>created handle: %d\n", *pIveHandle);
    printf("=====>src: au64PhyAddr: [0x%llx, 0x%llx, 0x%llx], au64VirAddr: [0x%llx, 0x%llx, 0x%llx], au32Stride: [%d, %d, %d], u32Width: %d, u32Height: %d, enType: %d\n",
                                pstSrc->au64PhyAddr[0], pstSrc->au64PhyAddr[1], pstSrc->au64PhyAddr[2],
                                pstSrc->au64VirAddr[0], pstSrc->au64VirAddr[1], pstSrc->au64VirAddr[2],
                                pstSrc->au32Stride[0], pstSrc->au32Stride[1], pstSrc->au32Stride[2],
                                pstSrc->u32Width,
                                pstSrc->u32Height,
                                pstSrc->enType);

    for (size_t i = 0; i < pstCropResize2Ctrl->u16Num; i++) {
        printf("=====>dst[%ld]: au64PhyAddr: [0x%llx, 0x%llx, 0x%llx], au64VirAddr: [0x%llx, 0x%llx, 0x%llx], au32Stride: [%d, %d, %d], u32Width: %d, u32Height: %d, enType: %d\n",
                                    i,
                                    pastDst[i]->au64PhyAddr[0], pastDst[i]->au64PhyAddr[1], pastDst[i]->au64PhyAddr[2],
                                    pastDst[i]->au64VirAddr[0], pastDst[i]->au64VirAddr[1], pastDst[i]->au64VirAddr[2],
                                    pastDst[i]->au32Stride[0], pastDst[i]->au32Stride[1], pastDst[i]->au32Stride[2],
                                    pastDst[i]->u32Width,
                                    pastDst[i]->u32Height,
                                    pastDst[i]->enType);
    }

    for (size_t i = 0; i < pstCropResize2Ctrl->u16Num; i++) {
        printf("=====>src box[%ld]: [x: %d, y: %d, w: %d, h: %d]\n",
                                    i,
                                    pastSrcBoxs[i]->u16X,
                                    pastSrcBoxs[i]->u16Y,
                                    pastSrcBoxs[i]->u16Width,
                                    pastSrcBoxs[i]->u16Height);
    }
    for (size_t i = 0; i < pstCropResize2Ctrl->u16Num; i++) {
        printf("=====>dst box[%ld]: [x: %d, y: %d, w: %d, h: %d]\n",
                                    i,
                                    pastDstBoxs[i]->u16X,
                                    pastDstBoxs[i]->u16Y,
                                    pastDstBoxs[i]->u16Width,
                                    pastDstBoxs[i]->u16Height);
    }
    printf("=====>ctrl: num: %d\n", pstCropResize2Ctrl->u16Num);
    printf("=====>engine: %d\n", enEngine);
    printf("=====>bInstant: %d\n", bInstant);

    // only for test
    for (size_t i = 0; i < pstCropResize2Ctrl->u16Num; i++) {
        pastDst[i]->au64PhyAddr[0] = 0x01000000 + (2 * i + 1)* 0x10000000 + *pIveHandle;
        pastDst[i]->au64PhyAddr[1] = 0x02000000 + (2 * i + 1)* 0x10000000 + *pIveHandle;
        pastDst[i]->au64PhyAddr[2] = 0x03000000 + (2 * i + 1)* 0x10000000 + *pIveHandle;
        pastDst[i]->au64VirAddr[0] = 0x01000000 + (2 * i + 2)* 0x10000000 + *pIveHandle;
        pastDst[i]->au64VirAddr[1] = 0x02000000 + (2 * i + 2)* 0x10000000 + *pIveHandle;
        pastDst[i]->au64VirAddr[2] = 0x03000000 + (2 * i + 2)* 0x10000000 + *pIveHandle;
    }

    return AXCL_SUCC;
}

AXCL_EXPORT AX_S32 AXCL_IVE_CropResize2ForSplitYUV(AX_IVE_HANDLE *pIveHandle, AX_IVE_SRC_IMAGE_T *pstSrc1, AX_IVE_SRC_IMAGE_T *pstSrc2,
                                                   AX_IVE_IMAGE_T *pastDst1[], AX_IVE_IMAGE_T *pastDst2[], AX_IVE_RECT_U16_T *pastSrcBoxs[],
                                                   AX_IVE_RECT_U16_T *pastDstBoxs[], AX_IVE_CROP_IMAGE_CTRL_T *pstCropResize2Ctrl,
                                                   AX_IVE_ENGINE_E enEngine, AX_BOOL bInstant) {
    CHECK_NULL_POINTER(pIveHandle);
    CHECK_NULL_POINTER(pstSrc1);
    CHECK_NULL_POINTER(pstSrc2);
    CHECK_NULL_POINTER(pastDst1);
    CHECK_NULL_POINTER(pastDst2);
    CHECK_NULL_POINTER(pastSrcBoxs);
    CHECK_NULL_POINTER(pastDstBoxs);
    CHECK_NULL_POINTER(pstCropResize2Ctrl);

    *pIveHandle = 28;

    printf("=====>%s:\n", __func__);
    printf("=====>created handle: %d\n", *pIveHandle);
    printf("=====>src1: au64PhyAddr: [0x%llx, 0x%llx, 0x%llx], au64VirAddr: [0x%llx, 0x%llx, 0x%llx], au32Stride: [%d, %d, %d], u32Width: %d, u32Height: %d, enType: %d\n",
                                pstSrc1->au64PhyAddr[0], pstSrc1->au64PhyAddr[1], pstSrc1->au64PhyAddr[2],
                                pstSrc1->au64VirAddr[0], pstSrc1->au64VirAddr[1], pstSrc1->au64VirAddr[2],
                                pstSrc1->au32Stride[0], pstSrc1->au32Stride[1], pstSrc1->au32Stride[2],
                                pstSrc1->u32Width,
                                pstSrc1->u32Height,
                                pstSrc1->enType);

    printf("=====>src2: au64PhyAddr: [0x%llx, 0x%llx, 0x%llx], au64VirAddr: [0x%llx, 0x%llx, 0x%llx], au32Stride: [%d, %d, %d], u32Width: %d, u32Height: %d, enType: %d\n",
                                pstSrc2->au64PhyAddr[0], pstSrc2->au64PhyAddr[1], pstSrc2->au64PhyAddr[2],
                                pstSrc2->au64VirAddr[0], pstSrc2->au64VirAddr[1], pstSrc2->au64VirAddr[2],
                                pstSrc2->au32Stride[0], pstSrc2->au32Stride[1], pstSrc2->au32Stride[2],
                                pstSrc2->u32Width,
                                pstSrc2->u32Height,
                                pstSrc2->enType);

    for (size_t i = 0; i < pstCropResize2Ctrl->u16Num; i++) {
        printf("=====>dst1[%ld]: au64PhyAddr: [0x%llx, 0x%llx, 0x%llx], au64VirAddr: [0x%llx, 0x%llx, 0x%llx], au32Stride: [%d, %d, %d], u32Width: %d, u32Height: %d, enType: %d\n",
                                    i,
                                    pastDst1[i]->au64PhyAddr[0], pastDst1[i]->au64PhyAddr[1], pastDst1[i]->au64PhyAddr[2],
                                    pastDst1[i]->au64VirAddr[0], pastDst1[i]->au64VirAddr[1], pastDst1[i]->au64VirAddr[2],
                                    pastDst1[i]->au32Stride[0], pastDst1[i]->au32Stride[1], pastDst1[i]->au32Stride[2],
                                    pastDst1[i]->u32Width,
                                    pastDst1[i]->u32Height,
                                    pastDst1[i]->enType);
    }

    for (size_t i = 0; i < pstCropResize2Ctrl->u16Num; i++) {
        printf("=====>dst2[%ld]: au64PhyAddr: [0x%llx, 0x%llx, 0x%llx], au64VirAddr: [0x%llx, 0x%llx, 0x%llx], au32Stride: [%d, %d, %d], u32Width: %d, u32Height: %d, enType: %d\n",
                                    i,
                                    pastDst2[i]->au64PhyAddr[0], pastDst2[i]->au64PhyAddr[1], pastDst2[i]->au64PhyAddr[2],
                                    pastDst2[i]->au64VirAddr[0], pastDst2[i]->au64VirAddr[1], pastDst2[i]->au64VirAddr[2],
                                    pastDst2[i]->au32Stride[0], pastDst2[i]->au32Stride[1], pastDst2[i]->au32Stride[2],
                                    pastDst2[i]->u32Width,
                                    pastDst2[i]->u32Height,
                                    pastDst2[i]->enType);
    }

    for (size_t i = 0; i < pstCropResize2Ctrl->u16Num; i++) {
        printf("=====>src box[%ld]: [x: %d, y: %d, w: %d, h: %d]\n",
                                    i,
                                    pastSrcBoxs[i]->u16X,
                                    pastSrcBoxs[i]->u16Y,
                                    pastSrcBoxs[i]->u16Width,
                                    pastSrcBoxs[i]->u16Height);
    }
    for (size_t i = 0; i < pstCropResize2Ctrl->u16Num; i++) {
        printf("=====>dst box[%ld]: [x: %d, y: %d, w: %d, h: %d]\n",
                                    i,
                                    pastDstBoxs[i]->u16X,
                                    pastDstBoxs[i]->u16Y,
                                    pastDstBoxs[i]->u16Width,
                                    pastDstBoxs[i]->u16Height);
    }
    printf("=====>ctrl: num: %d\n", pstCropResize2Ctrl->u16Num);
    printf("=====>engine: %d\n", enEngine);
    printf("=====>bInstant: %d\n", bInstant);

    // only for test
    for (size_t i = 0; i < pstCropResize2Ctrl->u16Num; i++) {
        pastDst1[i]->au64PhyAddr[0] = 0x01000000 + (2 * i + 1)* 0x10000000 + *pIveHandle;
        pastDst1[i]->au64PhyAddr[1] = 0x02000000 + (2 * i + 1)* 0x10000000 + *pIveHandle;
        pastDst1[i]->au64PhyAddr[2] = 0x03000000 + (2 * i + 1)* 0x10000000 + *pIveHandle;
        pastDst1[i]->au64VirAddr[0] = 0x01000000 + (2 * i + 2)* 0x10000000 + *pIveHandle;
        pastDst1[i]->au64VirAddr[1] = 0x02000000 + (2 * i + 2)* 0x10000000 + *pIveHandle;
        pastDst1[i]->au64VirAddr[2] = 0x03000000 + (2 * i + 2)* 0x10000000 + *pIveHandle;
    }

    for (size_t i = 0; i < pstCropResize2Ctrl->u16Num; i++) {
        pastDst2[i]->au64PhyAddr[0] = 0x04000000 + (2 * i + 1)* 0x10000000 + *pIveHandle;
        pastDst2[i]->au64PhyAddr[1] = 0x05000000 + (2 * i + 1)* 0x10000000 + *pIveHandle;
        pastDst2[i]->au64PhyAddr[2] = 0x06000000 + (2 * i + 1)* 0x10000000 + *pIveHandle;
        pastDst2[i]->au64VirAddr[0] = 0x04000000 + (2 * i + 2)* 0x10000000 + *pIveHandle;
        pastDst2[i]->au64VirAddr[1] = 0x05000000 + (2 * i + 2)* 0x10000000 + *pIveHandle;
        pastDst2[i]->au64VirAddr[2] = 0x06000000 + (2 * i + 2)* 0x10000000 + *pIveHandle;
    }

    return AXCL_SUCC;
}

AXCL_EXPORT AX_S32 AXCL_IVE_MAU_MatMul(AX_IVE_HANDLE *pIveHandle, AX_IVE_MAU_MATMUL_INPUT_T *pstSrc, AX_IVE_MAU_MATMUL_OUTPUT_T *pstDst,
                                       AX_IVE_MAU_MATMUL_CTRL_T *pstMatMulCtrl, AX_IVE_ENGINE_E enEngine, AX_BOOL bInstant) {
    CHECK_NULL_POINTER(pIveHandle);
    CHECK_NULL_POINTER(pstSrc);
    CHECK_NULL_POINTER(pstDst);
    CHECK_NULL_POINTER(pstMatMulCtrl);

    *pIveHandle = 29;

    printf("=====>%s:\n", __func__);
    printf("=====>created handle: %d\n", *pIveHandle);
    printf("=====>src mat_q: u64PhyAddr: 0x%llx, pVirAddr: %p, pShape: %p, u8ShapeSize: %d, enDataType: %d\n",
                                pstSrc->stMatQ.u64PhyAddr,
                                pstSrc->stMatQ.pVirAddr,
                                pstSrc->stMatQ.pShape,
                                pstSrc->stMatQ.u8ShapeSize,
                                pstSrc->stMatQ.enDataType);
    if (pstSrc->stMatQ.pShape && pstSrc->stMatQ.u8ShapeSize) {
        printf("=====>dst mat_q shape: [");
        for (AX_U8 i = 0; i < pstSrc->stMatQ.u8ShapeSize; i ++) {
            printf("0x%02x", pstSrc->stMatQ.pShape[i]);
            if (i < pstSrc->stMatQ.u8ShapeSize - 1) {
                printf(", ");
            }
        }
        printf("]\n");
    }
    printf("=====>src mat_b: u64PhyAddr: 0x%llx, pVirAddr: %p, pShape: %p, u8ShapeSize: %d, enDataType: %d\n",
                                pstSrc->stMatB.u64PhyAddr,
                                pstSrc->stMatB.pVirAddr,
                                pstSrc->stMatB.pShape,
                                pstSrc->stMatB.u8ShapeSize,
                                pstSrc->stMatB.enDataType);
    if (pstSrc->stMatB.pShape && pstSrc->stMatB.u8ShapeSize) {
        printf("=====>dst mat_b shape: [");
        for (AX_U8 i = 0; i < pstSrc->stMatB.u8ShapeSize; i ++) {
            printf("0x%02x", pstSrc->stMatB.pShape[i]);
            if (i < pstSrc->stMatB.u8ShapeSize - 1) {
                printf(", ");
            }
        }
        printf("]\n");
    }
    printf("=====>dst mul_res: u64PhyAddr: 0x%llx, pVirAddr: %p, pShape: %p, u8ShapeSize: %d, enDataType: %d\n",
                                pstDst->stMulRes.u64PhyAddr,
                                pstDst->stMulRes.pVirAddr,
                                pstDst->stMulRes.pShape,
                                pstDst->stMulRes.u8ShapeSize,
                                pstDst->stMulRes.enDataType);
    if (pstDst->stMulRes.pShape && pstDst->stMulRes.u8ShapeSize) {
        printf("=====>dst mul_res shape: [");
        for (AX_U8 i = 0; i < pstDst->stMulRes.u8ShapeSize; i ++) {
            printf("0x%02x", pstDst->stMulRes.pShape[i]);
            if (i < pstDst->stMulRes.u8ShapeSize - 1) {
                printf(", ");
            }
        }
        printf("]\n");
    }
    printf("=====>dst top_n_res: u64PhyAddr: 0x%llx, pVirAddr: %p, pShape: %p, u8ShapeSize: %d, enDataType: %d\n",
                                pstDst->stTopNRes.u64PhyAddr,
                                pstDst->stTopNRes.pVirAddr,
                                pstDst->stTopNRes.pShape,
                                pstDst->stTopNRes.u8ShapeSize,
                                pstDst->stTopNRes.enDataType);
    if (pstDst->stTopNRes.pShape && pstDst->stTopNRes.u8ShapeSize) {
        printf("=====>dst top_n_res shape: [");
        for (AX_U8 i = 0; i < pstDst->stTopNRes.u8ShapeSize; i ++) {
            printf("0x%02x", pstDst->stTopNRes.pShape[i]);
            if (i < pstDst->stTopNRes.u8ShapeSize - 1) {
                printf(", ");
            }
        }
        printf("]\n");
    }

    printf("=====>ctrl: enMauId: %d, s32DdrReadBandwidthLimit: %d, bEnableMulRes: %d, bEnableTopNRes: %d, enOrder: %d, s32TopN: %d\n",
                                pstMatMulCtrl->enMauId,
                                pstMatMulCtrl->s32DdrReadBandwidthLimit,
                                pstMatMulCtrl->bEnableMulRes,
                                pstMatMulCtrl->bEnableTopNRes,
                                pstMatMulCtrl->enOrder,
                                pstMatMulCtrl->s32TopN);
    printf("=====>engine: %d\n", enEngine);
    printf("=====>bInstant: %d\n", bInstant);

    // only for test
    pstDst->stMulRes.u64PhyAddr = 0x11000000;
    pstDst->stMulRes.pVirAddr = (AX_VOID *)0x22000000;
    pstDst->stMulRes.enDataType = AX_IVE_MAU_DT_UINT16;

    pstDst->stTopNRes.u64PhyAddr = 0x44000000;
    pstDst->stTopNRes.pVirAddr = (AX_VOID *)0x55000000;
    pstDst->stTopNRes.enDataType = AX_IVE_MAU_DT_FLOAT32;

    return AXCL_SUCC;
}

AXCL_EXPORT AX_S32 AXCL_IVE_NPU_CreateMatMulHandle(AX_IVE_MATMUL_HANDLE *pHandle, AX_IVE_NPU_MATMUL_CTRL_T *pstMatMulCtrl) {
    CHECK_NULL_POINTER(pHandle);
    CHECK_NULL_POINTER(pstMatMulCtrl);

    *pHandle = (AX_IVE_MATMUL_HANDLE)0x123456;

    printf("=====>%s:\n", __func__);
    printf("=====>pchModelDir: %s\n", pstMatMulCtrl->pchModelDir);
    printf("=====>enDataType: %d\n", pstMatMulCtrl->enDataType);
    printf("=====>s32KSize: %d\n", pstMatMulCtrl->s32KSize);
    printf("=====>created handle: %p\n", *pHandle);

    return AXCL_SUCC;
}

AXCL_EXPORT AX_S32 AXCL_IVE_NPU_DestroyMatMulHandle(AX_IVE_MATMUL_HANDLE *pHandle) {
    CHECK_NULL_POINTER(pHandle);

    printf("=====>%s:\n", __func__);
    printf("=====>destroied handle: %p\n", *pHandle);

    return AXCL_SUCC;
}

AXCL_EXPORT AX_S32 AXCL_IVE_NPU_MatMul(AX_IVE_MATMUL_HANDLE hHandle, AX_IVE_MAU_MATMUL_INPUT_T *pstSrc, AX_IVE_MAU_MATMUL_OUTPUT_T *pstDst,
                                       AX_IVE_ENGINE_E enEngine, AX_BOOL bInstant) {
    CHECK_NULL_POINTER(hHandle);
    CHECK_NULL_POINTER(pstSrc);
    CHECK_NULL_POINTER(pstDst);

    printf("=====>%s:\n", __func__);
    printf("=====>handle: %p\n", hHandle);
    printf("=====>src->stMatQ: u64PhyAddr: 0x%llx, pVirAddr: %p, pShape: %p, u8ShapeSize: %d, enDataType: %d\n",
                                pstSrc->stMatQ.u64PhyAddr,
                                pstSrc->stMatQ.pVirAddr,
                                pstSrc->stMatQ.pShape,
                                pstSrc->stMatQ.u8ShapeSize,
                                pstSrc->stMatQ.enDataType);
    if (pstSrc->stMatQ.pShape && pstSrc->stMatQ.u8ShapeSize) {
        printf("=====>dst mat_q shape: [");
        for (AX_U8 i = 0; i < pstSrc->stMatQ.u8ShapeSize; i ++) {
            printf("0x%02x", pstSrc->stMatQ.pShape[i]);
            if (i < pstSrc->stMatQ.u8ShapeSize - 1) {
                printf(", ");
            }
        }
        printf("]\n");
    }
    printf("=====>src->stMatB: u64PhyAddr: 0x%llx, pVirAddr: %p, pShape: %p, u8ShapeSize: %d, enDataType: %d\n",
                                pstSrc->stMatB.u64PhyAddr,
                                pstSrc->stMatB.pVirAddr,
                                pstSrc->stMatB.pShape,
                                pstSrc->stMatB.u8ShapeSize,
                                pstSrc->stMatB.enDataType);
    if (pstSrc->stMatB.pShape && pstSrc->stMatB.u8ShapeSize) {
        printf("=====>dst mat_b shape: [");
        for (AX_U8 i = 0; i < pstSrc->stMatB.u8ShapeSize; i ++) {
            printf("0x%02x", pstSrc->stMatB.pShape[i]);
            if (i < pstSrc->stMatB.u8ShapeSize - 1) {
                printf(", ");
            }
        }
        printf("]\n");
    }
    printf("=====>dst->stMulRes: u64PhyAddr: 0x%llx, pVirAddr: %p, pShape: %p, u8ShapeSize: %d, enDataType: %d\n",
                                pstDst->stMulRes.u64PhyAddr,
                                pstDst->stMulRes.pVirAddr,
                                pstDst->stMulRes.pShape,
                                pstDst->stMulRes.u8ShapeSize,
                                pstDst->stMulRes.enDataType);
    if (pstDst->stMulRes.pShape && pstDst->stMulRes.u8ShapeSize) {
        printf("=====>dst mul_res shape: [");
        for (AX_U8 i = 0; i < pstDst->stMulRes.u8ShapeSize; i ++) {
            printf("0x%02x", pstDst->stMulRes.pShape[i]);
            if (i < pstDst->stMulRes.u8ShapeSize - 1) {
                printf(", ");
            }
        }
        printf("]\n");
    }
    printf("=====>dst->stTopNRes: u64PhyAddr: 0x%llx, pVirAddr: %p, pShape: %p, u8ShapeSize: %d, enDataType: %d\n",
                                pstDst->stTopNRes.u64PhyAddr,
                                pstDst->stTopNRes.pVirAddr,
                                pstDst->stTopNRes.pShape,
                                pstDst->stTopNRes.u8ShapeSize,
                                pstDst->stTopNRes.enDataType);
    if (pstDst->stTopNRes.pShape && pstDst->stTopNRes.u8ShapeSize) {
        printf("=====>dst top_n_res shape: [");
        for (AX_U8 i = 0; i < pstDst->stTopNRes.u8ShapeSize; i ++) {
            printf("0x%02x", pstDst->stTopNRes.pShape[i]);
            if (i < pstDst->stTopNRes.u8ShapeSize - 1) {
                printf(", ");
            }
        }
        printf("]\n");
    }

    printf("=====>engine: %d\n", enEngine);
    printf("=====>bInstant: %d\n", bInstant);

    // only for test
    pstDst->stMulRes.u64PhyAddr = 0x11000000;
    pstDst->stMulRes.pVirAddr = (AX_VOID *)0x22000000;
    pstDst->stMulRes.enDataType = AX_IVE_MAU_DT_UINT16;

    pstDst->stTopNRes.u64PhyAddr = 0x44000000;
    pstDst->stTopNRes.pVirAddr = (AX_VOID *)0x55000000;
    pstDst->stTopNRes.enDataType = AX_IVE_MAU_DT_FLOAT32;

    return AXCL_SUCC;
}
