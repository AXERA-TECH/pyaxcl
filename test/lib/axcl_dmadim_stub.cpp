#include <stdint.h>
#include <stdio.h>
#include <string.h>
#include "axcl_dmadim.h"
#include "randomizer.hpp"
#include "serializer.hpp"

#define IMPLEMENT_SERIALIZE(...)                       \
    do {                                               \
        SERILAIZER()->input()->serialize(__VA_ARGS__); \
        AX_S32 ret = initialize_random<AX_S32>();      \
        SERILAIZER()->output()->serialize(ret);        \
        return ret;                                    \
    } while (0)

AXCL_EXPORT AX_S32 AXCL_DMADIM_Open(AX_BOOL bSync) {
    IMPLEMENT_SERIALIZE(bSync);
}

AXCL_EXPORT AX_S32 AXCL_DMADIM_Cfg(AX_S32 s32DmaChn, AX_DMADIM_MSG_T *pDmaMsg) {
    if (pDmaMsg->u32DescNum > 0) {
        uint8_array arr;
        arr.data = pDmaMsg->pDescBuf;
        arr.size = sizeof(AX_DMADIM_DESC_T) * pDmaMsg->u32DescNum;
        IMPLEMENT_SERIALIZE(s32DmaChn, pDmaMsg->u32DescNum, pDmaMsg->eEndian, pDmaMsg->eDmaMode, arr);
    } else {
        IMPLEMENT_SERIALIZE(s32DmaChn, pDmaMsg->u32DescNum, pDmaMsg->eEndian, pDmaMsg->eDmaMode);
    }
}

AXCL_EXPORT AX_S32 AXCL_DMADIM_Start(AX_S32 s32DmaChn, AX_S32 s32Id) {
    IMPLEMENT_SERIALIZE(s32DmaChn, s32Id);
}

AXCL_EXPORT AX_S32 AXCL_DMADIM_Waitdone(AX_S32 s32DmaChn, AX_DMADIM_XFER_STAT_T *pXferStat, AX_S32 s32Timeout) {
    SERILAIZER()->input()->serialize(s32DmaChn, pXferStat->s32Id, s32Timeout);
    pXferStat->u32CheckSum = initialize_random<AX_U32>();
    pXferStat->u32Stat = initialize_random<AX_U32>();
    AX_S32 ret = 0;
    SERILAIZER()->output()->serialize(ret, *pXferStat);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_DMADIM_Close(AX_S32 s32DmaChn) {
    IMPLEMENT_SERIALIZE(s32DmaChn);
}

AXCL_EXPORT AX_S32 AXCL_DMA_MemCopy(AX_U64 u64PhyDst, AX_U64 u64PhySrc, AX_U64 U64Size) {
    IMPLEMENT_SERIALIZE(u64PhyDst, u64PhySrc, U64Size);
}

AXCL_EXPORT AX_S32 AXCL_DMA_MemSet(AX_U64 u64PhyDst, AX_U8 u8InitVal, AX_U64 U64Size) {
    IMPLEMENT_SERIALIZE(u64PhyDst, u8InitVal, U64Size);
}

AXCL_EXPORT AX_S32 AXCL_DMA_MemCopyXD(AX_DMADIM_DESC_XD_T tDimDesc, AX_DMADIM_XFER_MODE_E eMode) {
    IMPLEMENT_SERIALIZE(tDimDesc, eMode);
}

AXCL_EXPORT AX_S32 AXCL_DMA_CheckSum(AX_U32 *u32Result, AX_U64 u64PhySrc, AX_U64 U64Size) {
    SERILAIZER()->input()->serialize(u64PhySrc, U64Size);
    *u32Result = initialize_random<AX_U32>();
    AX_S32 ret = initialize_random<AX_S32>();
    SERILAIZER()->output()->serialize(ret, *u32Result);
    return ret;
}
