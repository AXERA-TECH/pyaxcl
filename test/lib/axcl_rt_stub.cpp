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
#include <string.h>
#include "axcl.h"
#include "axcl_rt.h"
#include "randomizer.hpp"
#include "serializer.hpp"

#define IMPLEMENT_SERIALIZE(...)                        \
    do {                                                \
        SERILAIZER()->input()->serialize(__VA_ARGS__);  \
        axclError ret = initialize_random<axclError>(); \
        SERILAIZER()->output()->serialize(ret);         \
        return ret;                                     \
    } while (0)

AXCL_EXPORT axclError axclInit(const char *config) {
    if (strcmp(config, "xxxx.json") == 0) {
        return 0;
    } else {
        return 1;
    }
}

AXCL_EXPORT axclError axclFinalize() {
    IMPLEMENT_SERIALIZE();
}

AXCL_EXPORT axclError axclSetLogLevel(int32_t lv) {
    IMPLEMENT_SERIALIZE(lv);
}

AXCL_EXPORT void axclAppLog(int32_t lv, const char *func, const char *file, uint32_t line, const char *fmt, ...) {
    uint8_array arr1, arr2, arr3;
    arr1.data = reinterpret_cast<void *>(const_cast<char *>(func));
    arr1.size = strlen(func);
    arr2.data = reinterpret_cast<void *>(const_cast<char *>(file));
    arr2.size = strlen(file);
    arr3.data = reinterpret_cast<void *>(const_cast<char *>(fmt));
    arr3.size = strlen(fmt);
    SERILAIZER()->input()->serialize(lv, arr1, arr2, line, arr3);
    SERILAIZER()->output()->serialize();
}

AXCL_EXPORT axclError axclrtGetVersion(int32_t *major, int32_t *minor, int32_t *patch) {
    SERILAIZER()->input()->serialize();
    *major = initialize_random<int32_t>();
    *minor = initialize_random<int32_t>();
    *patch = initialize_random<int32_t>();

    axclError ret = initialize_random<axclError>();
    SERILAIZER()->output()->serialize(ret, *major, *minor, *patch);
    return ret;
}

AXCL_EXPORT const char *axclrtGetSocName() {
    return "AX650N";
}