#include <stdint.h>
#include <stdio.h>
#include <string.h>
#include "axcl_rt_device.h"
#include "randomizer.hpp"
#include "serializer.hpp"

#define IMPLEMENT_SERIALIZE(...)                        \
    do {                                                \
        SERILAIZER()->input()->serialize(__VA_ARGS__);  \
        axclError ret = initialize_random<axclError>(); \
        SERILAIZER()->output()->serialize(ret);         \
        return ret;                                     \
    } while (0)

AXCL_EXPORT axclError axclrtSetDevice(int32_t deviceId) {
    IMPLEMENT_SERIALIZE(deviceId);
}

AXCL_EXPORT axclError axclrtResetDevice(int32_t deviceId) {
    IMPLEMENT_SERIALIZE(deviceId);
}

AXCL_EXPORT axclError axclrtGetDevice(int32_t *deviceId) {
    SERILAIZER()->input()->serialize();
    *deviceId = initialize_random<int32_t>();
    axclError ret = initialize_random<axclError>();
    SERILAIZER()->output()->serialize(ret, *deviceId);
    return ret;
}

AXCL_EXPORT axclError axclrtGetDeviceCount(uint32_t *count) {
    SERILAIZER()->input()->serialize();
    *count = initialize_random<uint32_t>();
    axclError ret = initialize_random<axclError>();
    SERILAIZER()->output()->serialize(ret, *count);
    return ret;
}

AXCL_EXPORT axclError axclrtGetDeviceList(axclrtDeviceList *deviceList) {
    SERILAIZER()->input()->serialize();

    memset(deviceList, 0, sizeof(axclrtDeviceList));
    deviceList->num = static_cast<uint32_t>(create_int32_random_instance(0, AXCL_MAX_DEVICE_COUNT));
    for (uint32_t i = 0; i < deviceList->num; ++i) {
        deviceList->devices[i] = initialize_random<int32_t>();
    }
    axclError ret = 0;
    SERILAIZER()->output()->serialize(ret, *deviceList);
    return ret;
}

AXCL_EXPORT axclError axclrtSynchronizeDevice() {
    IMPLEMENT_SERIALIZE();
}

AXCL_EXPORT axclError axclrtGetDeviceUtilizationRate(int32_t deviceId, axclrtUtilizationInfo *utilizationInfo) {
    SERILAIZER()->input()->serialize(deviceId);
    utilizationInfo->cpuUtilization = initialize_random<int32_t>();
    utilizationInfo->npuUtilization = initialize_random<int32_t>();
    utilizationInfo->memUtilization = initialize_random<int32_t>();
    utilizationInfo->extUtilization = nullptr;
    axclError ret = initialize_random<axclError>();
    SERILAIZER()->output()->serialize(ret, *utilizationInfo);
    return ret;
}