/**************************************************************************************************
 *
 * Copyright (c) 2019-2024 Axera Semiconductor Co., Ltd. All Rights Reserved.
 *
 * This source file is the property of Axera Semiconductor Co., Ltd. and
 * may not be copied or distributed in any isomorphic form without the prior
 * written consent of Axera Semiconductor Co., Ltd.
 *
 **************************************************************************************************/

#include <stdint.h>
#include <stdio.h>
#include "axcl_rt_memory.h"
#include "randomizer.hpp"
#include "serializer.hpp"

#define IMPLEMENT_SERIALIZE(...)                        \
    do {                                                \
        SERILAIZER()->input()->serialize(__VA_ARGS__);  \
        axclError ret = initialize_random<axclError>(); \
        SERILAIZER()->output()->serialize(ret);         \
        return ret;                                     \
    } while (0)

AXCL_EXPORT axclError axclrtMalloc(void **devPtr, size_t size, axclrtMemMallocPolicy policy) {
    SERILAIZER()->input()->serialize(size, policy);
    *devPtr = reinterpret_cast<void *>(initialize_random<uint64_t>());
    axclError ret = initialize_random<axclError>();
    SERILAIZER()->output()->serialize(ret, reinterpret_cast<uint64_t>(*devPtr));
    return ret;
}

AXCL_EXPORT axclError axclrtMallocCached(void **devPtr, size_t size, axclrtMemMallocPolicy policy) {
    SERILAIZER()->input()->serialize(size, policy);
    *devPtr = reinterpret_cast<void *>(initialize_random<uint64_t>());
    axclError ret = initialize_random<axclError>();
    SERILAIZER()->output()->serialize(ret, reinterpret_cast<uint64_t>(*devPtr));
    return ret;
}

AXCL_EXPORT axclError axclrtFree(void *devPtr) {
    IMPLEMENT_SERIALIZE(reinterpret_cast<uint64_t>(devPtr));
}

AXCL_EXPORT axclError axclrtMemFlush(void *devPtr, size_t size) {
    IMPLEMENT_SERIALIZE(reinterpret_cast<uint64_t>(devPtr), size);
}

AXCL_EXPORT axclError axclrtMemInvalidate(void *devPtr, size_t size) {
    IMPLEMENT_SERIALIZE(reinterpret_cast<uint64_t>(devPtr), size);
}

AXCL_EXPORT axclError axclrtMallocHost(void **hostPtr, size_t size) {
    SERILAIZER()->input()->serialize(size);
    *hostPtr = reinterpret_cast<void *>(initialize_random<uint64_t>());
    axclError ret = initialize_random<axclError>();
    SERILAIZER()->output()->serialize(ret, reinterpret_cast<uint64_t>(*hostPtr));
    return ret;
}

AXCL_EXPORT axclError axclrtFreeHost(void *hostPtr) {
    IMPLEMENT_SERIALIZE(reinterpret_cast<uint64_t>(hostPtr));
}

AXCL_EXPORT axclError axclrtMemset(void *devPtr, uint8_t value, size_t count) {
    IMPLEMENT_SERIALIZE(reinterpret_cast<uint64_t>(devPtr), value, count);
}

AXCL_EXPORT axclError axclrtMemcpy(void *dstPtr, const void *srcPtr, size_t count, axclrtMemcpyKind kind) {
    IMPLEMENT_SERIALIZE(reinterpret_cast<uint64_t>(dstPtr), reinterpret_cast<uint64_t>(srcPtr), count, kind);
}

AXCL_EXPORT axclError axclrtMemcmp(const void *devPtr1, const void *devPtr2, size_t count) {
    IMPLEMENT_SERIALIZE(reinterpret_cast<uint64_t>(devPtr1), reinterpret_cast<uint64_t>(devPtr2), count);
}
