#include <stdint.h>
#include <stdio.h>
#include <string.h>
#include <vector>
#include "axcl_sys.h"
#include "randomizer.hpp"
#include "serializer.hpp"

#define IMPLEMENT_SERIALIZE(...)                       \
    do {                                               \
        SERILAIZER()->input()->serialize(__VA_ARGS__); \
        AX_S32 ret = initialize_random<AX_S32>();      \
        SERILAIZER()->output()->serialize(ret);        \
        return ret;                                    \
    } while (0)

AXCL_EXPORT AX_S32 AXCL_SYS_Init(AX_VOID) {
    IMPLEMENT_SERIALIZE();
}

AXCL_EXPORT AX_S32 AXCL_SYS_Deinit(AX_VOID) {
    IMPLEMENT_SERIALIZE();
}

AXCL_EXPORT AX_S32 AXCL_SYS_MemAlloc(AX_U64 *phyaddr, AX_VOID **pviraddr, AX_U32 size, AX_U32 align, const AX_S8 *token) {
    if (token) {
        uint8_array arr;
        arr.data = (void *)token;
        arr.size = strlen((const char *)token);
        SERILAIZER()->input()->serialize(size, align, arr);
    } else {
        SERILAIZER()->input()->serialize(size, align);
    }

    AX_S32 ret = initialize_random<AX_S32>();
    *phyaddr = initialize_random<AX_U64>();
    *pviraddr = reinterpret_cast<AX_VOID *>(initialize_random<AX_U64>());
    SERILAIZER()->output()->serialize(ret, *phyaddr, reinterpret_cast<AX_U64>(*pviraddr));
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_SYS_MemAllocCached(AX_U64 *phyaddr, AX_VOID **pviraddr, AX_U32 size, AX_U32 align, const AX_S8 *token) {
    if (token) {
        uint8_array arr;
        arr.data = (void *)token;
        arr.size = strlen((const char *)token);
        SERILAIZER()->input()->serialize(size, align, arr);
    } else {
        SERILAIZER()->input()->serialize(size, align);
    }

    AX_S32 ret = initialize_random<AX_S32>();
    *phyaddr = initialize_random<AX_U64>();
    *pviraddr = reinterpret_cast<AX_VOID *>(initialize_random<AX_U64>());
    SERILAIZER()->output()->serialize(ret, *phyaddr, reinterpret_cast<AX_U64>(*pviraddr));
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_SYS_MemFree(AX_U64 phyaddr, AX_VOID *pviraddr) {
    IMPLEMENT_SERIALIZE(phyaddr, reinterpret_cast<AX_U64>(pviraddr));
}

AXCL_EXPORT AX_VOID *AXCL_SYS_Mmap(AX_U64 phyaddr, AX_U32 size) {
    SERILAIZER()->input()->serialize(phyaddr, size);
    AX_U64 addr = initialize_random<AX_U64>();
    SERILAIZER()->output()->serialize(addr);
    return reinterpret_cast<AX_VOID *>(addr);
}

AXCL_EXPORT AX_VOID *AXCL_SYS_MmapCache(AX_U64 phyaddr, AX_U32 size) {
    SERILAIZER()->input()->serialize(phyaddr, size);
    AX_U64 addr = initialize_random<AX_U64>();
    SERILAIZER()->output()->serialize(addr);
    return reinterpret_cast<AX_VOID *>(addr);
}

AXCL_EXPORT AX_VOID *AXCL_SYS_MmapFast(AX_U64 phyaddr, AX_U32 size) {
    SERILAIZER()->input()->serialize(phyaddr, size);
    AX_U64 addr = initialize_random<AX_U64>();
    SERILAIZER()->output()->serialize(addr);
    return reinterpret_cast<AX_VOID *>(addr);
}

AXCL_EXPORT AX_VOID *AXCL_SYS_MmapCacheFast(AX_U64 phyaddr, AX_U32 size) {
    SERILAIZER()->input()->serialize(phyaddr, size);
    AX_U64 addr = initialize_random<AX_U64>();
    SERILAIZER()->output()->serialize(addr);
    return reinterpret_cast<AX_VOID *>(addr);
}

AXCL_EXPORT AX_S32 AXCL_SYS_Munmap(AX_VOID *pviraddr, AX_U32 size) {
    IMPLEMENT_SERIALIZE(reinterpret_cast<AX_U64>(pviraddr), size);
}

AXCL_EXPORT AX_S32 AXCL_SYS_MflushCache(AX_U64 phyaddr, AX_VOID *pviraddr, AX_U32 size) {
    IMPLEMENT_SERIALIZE(phyaddr, reinterpret_cast<AX_U64>(pviraddr), size);
}

AXCL_EXPORT AX_S32 AXCL_SYS_MinvalidateCache(AX_U64 phyaddr, AX_VOID *pviraddr, AX_U32 size) {
    IMPLEMENT_SERIALIZE(phyaddr, reinterpret_cast<AX_U64>(pviraddr), size);
}

AXCL_EXPORT AX_S32 AXCL_SYS_MemGetBlockInfoByPhy(AX_U64 phyaddr, AX_S32 *pmemType, AX_VOID **pviraddr, AX_U32 *pblockSize) {
    SERILAIZER()->input()->serialize(phyaddr);
    *pmemType = initialize_random<AX_S32>();
    *pviraddr = reinterpret_cast<AX_VOID *>(initialize_random<AX_U64>());
    *pblockSize = initialize_random<AX_U32>();
    AX_S32 ret = initialize_random<AX_S32>();
    SERILAIZER()->output()->serialize(ret, *pmemType, reinterpret_cast<AX_U64>(*pviraddr), *pblockSize);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_SYS_MemGetBlockInfoByVirt(AX_VOID *pviraddr, AX_U64 *phyaddr, AX_S32 *pmemType) {
    SERILAIZER()->input()->serialize(reinterpret_cast<AX_U64>(pviraddr));
    *phyaddr = initialize_random<AX_U64>();
    *pmemType = initialize_random<AX_S32>();
    AX_S32 ret = initialize_random<AX_S32>();
    SERILAIZER()->output()->serialize(ret, *phyaddr, *pmemType);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_SYS_MemGetPartitionInfo(AX_CMM_PARTITION_INFO_T *pCmmPartitionInfo) {
    SERILAIZER()->input()->serialize();

    memset(pCmmPartitionInfo, 0, sizeof(AX_CMM_PARTITION_INFO_T));
    pCmmPartitionInfo->PartitionCnt = create_int32_random_instance(1, AX_MAX_PARTITION_COUNT);
    for (AX_U32 i = 0; i < pCmmPartitionInfo->PartitionCnt; ++i) {
        pCmmPartitionInfo->PartitionInfo[i].PhysAddr = initialize_random<AX_U64>();
        pCmmPartitionInfo->PartitionInfo[i].SizeKB = initialize_random<AX_U32>();
        sprintf((AX_CHAR *)pCmmPartitionInfo->PartitionInfo[0].Name, "part%d", i);
    }

    AX_S32 ret = 0;
    SERILAIZER()->output()->serialize(ret, *pCmmPartitionInfo);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_SYS_MemSetConfig(const AX_MOD_INFO_T *pModInfo, const AX_S8 *pPartitionName) {
    if (pPartitionName) {
        uint8_array arr;
        arr.data = (void *)pPartitionName;
        arr.size = strlen((const char *)pPartitionName);
        SERILAIZER()->input()->serialize(pModInfo, arr);
    } else {
        SERILAIZER()->input()->serialize(pModInfo);
    }

    AX_S32 ret = initialize_random<AX_S32>();
    SERILAIZER()->output()->serialize(ret);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_SYS_MemGetConfig(const AX_MOD_INFO_T *pModInfo, AX_S8 *pPartitionName) {
    SERILAIZER()->input()->serialize(pModInfo);
    sprintf((AX_CHAR *)pPartitionName, "partX");
    AX_S32 ret = 0;
    uint8_array arr;
    arr.data = (void *)pPartitionName;
    arr.size = strlen((const char *)pPartitionName);
    SERILAIZER()->output()->serialize(ret, arr);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_SYS_MemQueryStatus(AX_CMM_STATUS_T *pCmmStatus) {
    SERILAIZER()->input()->serialize();

    memset(pCmmStatus, 0, sizeof(AX_CMM_STATUS_T));
    pCmmStatus->TotalSize = initialize_random<AX_U32>();
    pCmmStatus->RemainSize = initialize_random<AX_U32>();
    pCmmStatus->BlockCnt = initialize_random<AX_U32>();
    pCmmStatus->Partition.PartitionCnt = create_int32_random_instance(1, AX_MAX_PARTITION_COUNT);
    for (AX_U32 i = 0; i < pCmmStatus->Partition.PartitionCnt; ++i) {
        pCmmStatus->Partition.PartitionInfo[i].PhysAddr = initialize_random<AX_U64>();
        pCmmStatus->Partition.PartitionInfo[i].SizeKB = initialize_random<AX_U32>();
        sprintf((AX_CHAR *)pCmmStatus->Partition.PartitionInfo[0].Name, "part%d", i);
    }

    AX_S32 ret = 0;
    SERILAIZER()->output()->serialize(ret, *pCmmStatus);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_SYS_Link(const AX_MOD_INFO_T *pSrc, const AX_MOD_INFO_T *pDest) {
    IMPLEMENT_SERIALIZE(pSrc, pDest);
}

AXCL_EXPORT AX_S32 AXCL_SYS_UnLink(const AX_MOD_INFO_T *pSrc, const AX_MOD_INFO_T *pDest) {
    IMPLEMENT_SERIALIZE(pSrc, pDest);
}

AXCL_EXPORT AX_S32 AXCL_SYS_GetLinkByDest(const AX_MOD_INFO_T *pDest, AX_MOD_INFO_T *pSrc) {
    SERILAIZER()->input()->serialize(pDest);

    memset(pSrc, 0, sizeof(AX_MOD_INFO_T));
    pSrc->enModId = AX_ID_IVPS;
    pSrc->s32GrpId = initialize_random<AX_S32>();
    pSrc->s32ChnId = initialize_random<AX_S32>();

    AX_S32 ret = 0;
    SERILAIZER()->output()->serialize(ret, *pSrc);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_SYS_GetLinkBySrc(const AX_MOD_INFO_T *pSrc, AX_LINK_DEST_T *pLinkDest) {
    SERILAIZER()->input()->serialize(pSrc);

    const std::vector<AX_MOD_ID_E> mods = {AX_ID_VDEC, AX_ID_VENC, AX_ID_IVPS, AX_ID_VO};

    memset(pLinkDest, 0, sizeof(AX_LINK_DEST_T));
    pLinkDest->u32DestNum = create_int32_random_instance(1, AX_LINK_DEST_MAXNUM);
    for (AX_U32 i = 0; i < pLinkDest->u32DestNum; ++i) {
        pLinkDest->astDestMod[i].enModId = choose_random_from_array<AX_MOD_ID_E>(mods);
        pLinkDest->astDestMod[i].s32GrpId = initialize_random<AX_S32>();
        pLinkDest->astDestMod[i].s32ChnId = initialize_random<AX_S32>();
    }

    AX_S32 ret = 0;
    SERILAIZER()->output()->serialize(ret, *pLinkDest);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_POOL_SetConfig(const AX_POOL_FLOORPLAN_T *pPoolFloorPlan) {
    IMPLEMENT_SERIALIZE(pPoolFloorPlan);
}

AXCL_EXPORT AX_S32 AXCL_POOL_GetConfig(AX_POOL_FLOORPLAN_T *pPoolFloorPlan) {
    SERILAIZER()->input()->serialize();

    memset(pPoolFloorPlan, 0, sizeof(AX_POOL_FLOORPLAN_T));
    for (size_t i = 0; i < AX_MAX_COMM_POOLS; i++) {
        pPoolFloorPlan->CommPool[i].MetaSize = initialize_random<AX_U64>();
        pPoolFloorPlan->CommPool[i].BlkSize = initialize_random<AX_U64>();
        pPoolFloorPlan->CommPool[i].BlkCnt = initialize_random<AX_U32>();
        pPoolFloorPlan->CommPool[i].IsMergeMode = (AX_BOOL)(i % 2 == 0);
        pPoolFloorPlan->CommPool[i].CacheMode = (AX_POOL_CACHE_MODE_E)(i % 2 == 1);
        sprintf((AX_CHAR *)pPoolFloorPlan->CommPool[i].PartitionName, "part%ld", i);
        sprintf((AX_CHAR *)pPoolFloorPlan->CommPool[i].PoolName, "pool%ld", i);
    }

    AX_S32 ret = 0;
    SERILAIZER()->output()->serialize(ret, *pPoolFloorPlan);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_POOL_Init(AX_VOID) {
    IMPLEMENT_SERIALIZE();
}

AXCL_EXPORT AX_S32 AXCL_POOL_Exit(AX_VOID) {
    IMPLEMENT_SERIALIZE();
}

AXCL_EXPORT AX_POOL AXCL_POOL_CreatePool(AX_POOL_CONFIG_T *pPoolConfig) {
    SERILAIZER()->input()->serialize(pPoolConfig);
    AX_POOL pool = initialize_random<AX_POOL>();
    SERILAIZER()->output()->serialize(pool);
    return pool;
}

AXCL_EXPORT AX_S32 AXCL_POOL_DestroyPool(AX_POOL PoolId) {
    IMPLEMENT_SERIALIZE(PoolId);
}

AXCL_EXPORT AX_BLK AXCL_POOL_GetBlock(AX_POOL PoolId, AX_U64 BlkSize, const AX_S8 *pPartitionName) {
    if (pPartitionName) {
        uint8_array arr;
        arr.data = (void *)pPartitionName;
        arr.size = strlen((const char *)pPartitionName);
        SERILAIZER()->input()->serialize(PoolId, BlkSize, arr);
    } else {
        SERILAIZER()->input()->serialize(PoolId, BlkSize);
    }

    AX_BLK blk = initialize_random<AX_BLK>();
    SERILAIZER()->output()->serialize(blk);
    return blk;
}

AXCL_EXPORT AX_S32 AXCL_POOL_ReleaseBlock(AX_BLK BlockId) {
    IMPLEMENT_SERIALIZE(BlockId);
}

AXCL_EXPORT AX_BLK AXCL_POOL_PhysAddr2Handle(AX_U64 PhysAddr) {
    SERILAIZER()->input()->serialize(PhysAddr);
    AX_BLK blk = initialize_random<AX_BLK>();
    SERILAIZER()->output()->serialize(blk);
    return blk;
}

AXCL_EXPORT AX_U64 AXCL_POOL_Handle2PhysAddr(AX_BLK BlockId) {
    SERILAIZER()->input()->serialize(BlockId);
    AX_U64 phyaddr = initialize_random<AX_U64>();
    SERILAIZER()->output()->serialize(phyaddr);
    return phyaddr;
}

AXCL_EXPORT AX_U64 AXCL_POOL_Handle2MetaPhysAddr(AX_BLK BlockId) {
    SERILAIZER()->input()->serialize(BlockId);
    AX_U64 phyaddr = initialize_random<AX_U64>();
    SERILAIZER()->output()->serialize(phyaddr);
    return phyaddr;
}

AXCL_EXPORT AX_POOL AXCL_POOL_Handle2PoolId(AX_BLK BlockId) {
    SERILAIZER()->input()->serialize(BlockId);
    AX_POOL pool = initialize_random<AX_POOL>();
    SERILAIZER()->output()->serialize(pool);
    return pool;
}

AXCL_EXPORT AX_U64 AXCL_POOL_Handle2BlkSize(AX_BLK BlockId) {
    SERILAIZER()->input()->serialize(BlockId);
    AX_U64 size = initialize_random<AX_U64>();
    SERILAIZER()->output()->serialize(size);
    return size;
}

AXCL_EXPORT AX_S32 AXCL_POOL_MmapPool(AX_POOL PoolId) {
    IMPLEMENT_SERIALIZE(PoolId);
}

AXCL_EXPORT AX_S32 AXCL_POOL_MunmapPool(AX_POOL PoolId) {
    IMPLEMENT_SERIALIZE(PoolId);
}

AXCL_EXPORT AX_VOID *AXCL_POOL_GetBlockVirAddr(AX_BLK BlockId) {
    SERILAIZER()->input()->serialize(BlockId);
    AX_U64 viraddr = initialize_random<AX_U64>();
    SERILAIZER()->output()->serialize(viraddr);
    return reinterpret_cast<AX_VOID *>(viraddr);
}

AXCL_EXPORT AX_VOID *AXCL_POOL_GetMetaVirAddr(AX_BLK BlockId) {
    SERILAIZER()->input()->serialize(BlockId);
    AX_U64 viraddr = initialize_random<AX_U64>();
    SERILAIZER()->output()->serialize(viraddr);
    return reinterpret_cast<AX_VOID *>(viraddr);
}

AXCL_EXPORT AX_S32 AXCL_POOL_IncreaseRefCnt(AX_BLK BlockId) {
    IMPLEMENT_SERIALIZE(BlockId);
}

AXCL_EXPORT AX_S32 AXCL_POOL_DecreaseRefCnt(AX_BLK BlockId) {
    IMPLEMENT_SERIALIZE(BlockId);
}

AXCL_EXPORT AX_S32 AXCL_SYS_GetCurPTS(AX_U64 *pu64CurPTS) {
    SERILAIZER()->input()->serialize();
    *pu64CurPTS = initialize_random<AX_U64>();
    AX_S32 ret = 0;
    SERILAIZER()->output()->serialize(ret, *pu64CurPTS);
    return ret;
}

AXCL_EXPORT AX_S32 AXCL_SYS_InitPTSBase(AX_U64 u64PTSBase) {
    IMPLEMENT_SERIALIZE(u64PTSBase);
}

AXCL_EXPORT AX_S32 AXCL_SYS_SyncPTS(AX_U64 u64PTSBase) {
    IMPLEMENT_SERIALIZE(u64PTSBase);
}

AXCL_EXPORT AX_CHIP_TYPE_E AXCL_SYS_GetChipType(AX_VOID) {
    return AX650N_CHIP;
}

AXCL_EXPORT AX_S32 AXCL_SYS_SetLogLevel(AX_LOG_LEVEL_E target) {
    IMPLEMENT_SERIALIZE(target);
}

AXCL_EXPORT AX_S32 AXCL_SYS_SetLogTarget(AX_LOG_TARGET_E target) {
    IMPLEMENT_SERIALIZE(target);
}

AXCL_EXPORT AX_S32 AXCL_SYS_EnableTimestamp(AX_BOOL enable) {
    IMPLEMENT_SERIALIZE(enable);
}

AXCL_EXPORT AX_S32 AXCL_SYS_Sleep(AX_VOID) {
    IMPLEMENT_SERIALIZE();
}

AXCL_EXPORT AX_S32 AXCL_SYS_WakeLock(const AX_MOD_ID_E ModId) {
    IMPLEMENT_SERIALIZE(ModId);
}

AXCL_EXPORT AX_S32 AXCL_SYS_WakeUnlock(const AX_MOD_ID_E ModId) {
    IMPLEMENT_SERIALIZE(ModId);
}

AXCL_EXPORT AX_S32 AXCL_SYS_RegisterEventCb(const AX_MOD_ID_E ModId, NotifyEventCallback pFunction, AX_VOID *pData) {
    IMPLEMENT_SERIALIZE(ModId, reinterpret_cast<AX_U64>(pFunction), reinterpret_cast<AX_U64>(pData));
}

AXCL_EXPORT AX_S32 AXCL_SYS_UnregisterEventCb(const AX_MOD_ID_E ModId) {
    IMPLEMENT_SERIALIZE(ModId);
}
