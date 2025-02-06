#include <stdint.h>
#include <stdio.h>
#include "axcl_rt_context.h"
#include "randomizer.hpp"
#include "serializer.hpp"

#define IMPLEMENT_SERIALIZE(...)                        \
    do {                                                \
        SERILAIZER()->input()->serialize(__VA_ARGS__);  \
        axclError ret = initialize_random<axclError>(); \
        SERILAIZER()->output()->serialize(ret);         \
        return ret;                                     \
    } while (0)

AXCL_EXPORT axclError axclrtCreateContext(axclrtContext *context, int32_t deviceId) {
    SERILAIZER()->input()->serialize(deviceId);
    axclError ret = initialize_random<axclError>();
    *context = reinterpret_cast<axclrtContext>(initialize_random<uint64_t>());
    SERILAIZER()->output()->serialize(ret, reinterpret_cast<uint64_t>(*context));
    return ret;
}

AXCL_EXPORT axclError axclrtDestroyContext(axclrtContext context) {
    IMPLEMENT_SERIALIZE(reinterpret_cast<uint64_t>(context));
}

AXCL_EXPORT axclError axclrtSetCurrentContext(axclrtContext context) {
    IMPLEMENT_SERIALIZE(reinterpret_cast<uint64_t>(context));
}

AXCL_EXPORT axclError axclrtGetCurrentContext(axclrtContext *context) {
    SERILAIZER()->input()->serialize();
    axclError ret = initialize_random<axclError>();
    *context = reinterpret_cast<axclrtContext>(initialize_random<uint64_t>());
    SERILAIZER()->output()->serialize(ret, reinterpret_cast<uint64_t>(*context));
    return ret;
}

AXCL_EXPORT axclError axclrtGetDefaultContext(axclrtContext *context, int32_t deviceId) {
    SERILAIZER()->input()->serialize(deviceId);
    axclError ret = initialize_random<axclError>();
    *context = reinterpret_cast<axclrtContext>(initialize_random<uint64_t>());
    SERILAIZER()->output()->serialize(ret, reinterpret_cast<uint64_t>(*context));
    return ret;
}
