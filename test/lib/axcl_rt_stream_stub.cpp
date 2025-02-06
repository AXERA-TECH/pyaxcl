/**************************************************************************************************
 *
 * Copyright (c) 2019-2024 Axera Semiconductor Co., Ltd. All Rights Reserved.
 *
 * This source file is the property of Axera Semiconductor Co., Ltd. and
 * may not be copied or distributed in any isomorphic form without the prior
 * written consent of Axera Semiconductor Co., Ltd.
 *
 **************************************************************************************************/


#include <stdio.h>
#include <stdint.h>
#include "axcl_rt_stream.h"
#include "randomizer.hpp"
#include "serializer.hpp"

#define IMPLEMENT_SERIALIZE(...)                        \
    do {                                                \
        SERILAIZER()->input()->serialize(__VA_ARGS__);  \
        axclError ret = initialize_random<axclError>(); \
        SERILAIZER()->output()->serialize(ret);         \
        return ret;                                     \
    } while (0)

AXCL_EXPORT axclError axclrtCreateStream(axclrtStream *stream) {
    SERILAIZER()->input()->serialize();
    axclError ret = initialize_random<axclError>();
    *stream = reinterpret_cast<axclrtStream>(initialize_random<uint64_t>());
    SERILAIZER()->output()->serialize(ret, reinterpret_cast<uint64_t>(*stream));
    return ret;
}

AXCL_EXPORT axclError axclrtDestroyStream(axclrtStream stream) {
    IMPLEMENT_SERIALIZE(reinterpret_cast<uint64_t>(stream));
}

AXCL_EXPORT axclError axclrtDestroyStreamForce(axclrtStream stream) {
    IMPLEMENT_SERIALIZE(reinterpret_cast<uint64_t>(stream));
}

AXCL_EXPORT axclError axclrtSynchronizeStream(axclrtStream stream) {
    IMPLEMENT_SERIALIZE(reinterpret_cast<uint64_t>(stream));
}

AXCL_EXPORT axclError axclrtSynchronizeStreamWithTimeout(axclrtStream stream, int32_t timeout) {
    IMPLEMENT_SERIALIZE(reinterpret_cast<uint64_t>(stream), timeout);
}
