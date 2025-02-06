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
#include <string.h>
#include <vector>
#include "axcl_rt_engine.h"
#include "randomizer.hpp"
#include "serializer.hpp"

#define IMPLEMENT_SERIALIZE(...)                        \
    do {                                                \
        SERILAIZER()->input()->serialize(__VA_ARGS__);  \
        axclError ret = initialize_random<axclError>(); \
        SERILAIZER()->output()->serialize(ret);         \
        return ret;                                     \
    } while (0)

AXCL_EXPORT axclError axclrtEngineInit(axclrtEngineVNpuKind npuKind) {
    IMPLEMENT_SERIALIZE(npuKind);
}

AXCL_EXPORT axclError axclrtEngineGetVNpuKind(axclrtEngineVNpuKind *npuKind) {
    SERILAIZER()->input()->serialize();
    *npuKind = initialize_random<axclrtEngineVNpuKind>();
    axclError ret = initialize_random<axclError>();
    SERILAIZER()->output()->serialize(ret, *npuKind);
    return ret;
}

AXCL_EXPORT axclError axclrtEngineFinalize() {
    IMPLEMENT_SERIALIZE();
}

AXCL_EXPORT axclError axclrtEngineLoadFromFile(const char *modelPath, uint64_t *modelId) {
    if (modelPath) {
        uint8_array arr;
        arr.data = (void *)modelPath;
        arr.size = strlen(modelPath);
        SERILAIZER()->input()->serialize(arr);
    } else {
        SERILAIZER()->input()->serialize();
    }

    *modelId = initialize_random<uint64_t>();
    axclError ret = initialize_random<axclError>();
    SERILAIZER()->output()->serialize(ret, *modelId);
    return ret;
}

AXCL_EXPORT axclError axclrtEngineLoadFromMem(const void *model, uint64_t modelSize, uint64_t *modelId) {
    uint8_array arr;
    arr.data = (void *)model;
    arr.size = modelSize;
    SERILAIZER()->input()->serialize(arr);
    *modelId = initialize_random<uint64_t>();
    axclError ret = initialize_random<axclError>();
    SERILAIZER()->output()->serialize(ret, *modelId);
    return ret;
}

AXCL_EXPORT axclError axclrtEngineUnload(uint64_t modelId) {
    IMPLEMENT_SERIALIZE(modelId);
}

AXCL_EXPORT const char *axclrtEngineGetModelCompilerVersion(uint64_t modelId) {
    SERILAIZER()->input()->serialize(modelId);
    static const char *compile_version = "vX.YY.zz";
    uint8_array arr;
    arr.data = (void *)compile_version;
    arr.size = strlen(compile_version);
    SERILAIZER()->output()->serialize(arr);
    return compile_version;
}

AXCL_EXPORT axclError axclrtEngineSetAffinity(uint64_t modelId, axclrtEngineSet set) {
    IMPLEMENT_SERIALIZE(modelId, set);
}

AXCL_EXPORT axclError axclrtEngineGetAffinity(uint64_t modelId, axclrtEngineSet *set) {
    SERILAIZER()->input()->serialize(modelId);
    *set = initialize_random<axclrtEngineSet>();
    axclError ret = initialize_random<axclError>();
    SERILAIZER()->output()->serialize(ret, *set);
    return ret;
}

AXCL_EXPORT axclError axclrtEngineGetUsage(const char *modelPath, int64_t *sysSize, int64_t *cmmSize) {
    uint8_array arr;
    arr.data = (void *)modelPath;
    arr.size = strlen(modelPath);
    SERILAIZER()->input()->serialize(arr);
    *sysSize = initialize_random<int64_t>();
    *cmmSize = initialize_random<int64_t>();
    axclError ret = initialize_random<axclError>();
    SERILAIZER()->output()->serialize(ret, *sysSize, *cmmSize);
    return ret;
}

AXCL_EXPORT axclError axclrtEngineGetUsageFromMem(const void *model, uint64_t modelSize, int64_t *sysSize, int64_t *cmmSize) {
    uint8_array arr;
    arr.data = (void *)model;
    arr.size = modelSize;
    SERILAIZER()->input()->serialize(arr);
    *sysSize = initialize_random<int64_t>();
    *cmmSize = initialize_random<int64_t>();
    axclError ret = initialize_random<axclError>();
    SERILAIZER()->output()->serialize(ret, *sysSize, *cmmSize);
    return ret;
}

AXCL_EXPORT axclError axclrtEngineGetUsageFromModelId(uint64_t modelId, int64_t *sysSize, int64_t *cmmSize) {
    SERILAIZER()->input()->serialize(modelId);
    *sysSize = initialize_random<int64_t>();
    *cmmSize = initialize_random<int64_t>();
    axclError ret = initialize_random<axclError>();
    SERILAIZER()->output()->serialize(ret, *sysSize, *cmmSize);
    return ret;
}

AXCL_EXPORT axclError axclrtEngineGetModelType(const char *modelPath, axclrtEngineModelKind *modelType) {
    uint8_array arr;
    arr.data = (void *)modelPath;
    arr.size = strlen(modelPath);
    SERILAIZER()->input()->serialize(arr);
    *modelType = initialize_random<axclrtEngineModelKind>();
    axclError ret = initialize_random<axclError>();
    SERILAIZER()->output()->serialize(ret, *modelType);
    return ret;
}

AXCL_EXPORT axclError axclrtEngineGetModelTypeFromMem(const void *model, uint64_t modelSize, axclrtEngineModelKind *modelType) {
    uint8_array arr;
    arr.data = (void *)model;
    arr.size = modelSize;
    SERILAIZER()->input()->serialize(arr);
    *modelType = initialize_random<axclrtEngineModelKind>();
    axclError ret = initialize_random<axclError>();
    SERILAIZER()->output()->serialize(ret, *modelType);
    return ret;
}

AXCL_EXPORT axclError axclrtEngineGetModelTypeFromModelId(uint64_t modelId, axclrtEngineModelKind *modelType) {
    SERILAIZER()->input()->serialize(modelId);
    *modelType = initialize_random<axclrtEngineModelKind>();
    axclError ret = initialize_random<axclError>();
    SERILAIZER()->output()->serialize(ret, *modelType);
    return ret;
}

AXCL_EXPORT axclError axclrtEngineGetIOInfo(uint64_t modelId, axclrtEngineIOInfo *ioInfo) {
    SERILAIZER()->input()->serialize(modelId);
    *ioInfo = reinterpret_cast<axclrtEngineIOInfo>(initialize_random<uint64_t>());
    axclError ret = initialize_random<axclError>();
    SERILAIZER()->output()->serialize(ret, reinterpret_cast<uint64_t>(*ioInfo));
    return ret;
}

AXCL_EXPORT axclError axclrtEngineDestroyIOInfo(axclrtEngineIOInfo ioInfo) {
    IMPLEMENT_SERIALIZE(reinterpret_cast<uint64_t>(ioInfo));
}

AXCL_EXPORT axclError axclrtEngineGetShapeGroupsCount(axclrtEngineIOInfo ioInfo, int32_t *count) {
    SERILAIZER()->input()->serialize(reinterpret_cast<uint64_t>(ioInfo));
    *count = initialize_random<int32_t>();
    axclError ret = initialize_random<axclError>();
    SERILAIZER()->output()->serialize(ret, *count);
    return ret;
}

AXCL_EXPORT uint32_t axclrtEngineGetNumInputs(axclrtEngineIOInfo ioInfo) {
    SERILAIZER()->input()->serialize(reinterpret_cast<uint64_t>(ioInfo));
    uint32_t num = initialize_random<uint32_t>();
    SERILAIZER()->output()->serialize(num);
    return num;
}

AXCL_EXPORT uint32_t axclrtEngineGetNumOutputs(axclrtEngineIOInfo ioInfo) {
    SERILAIZER()->input()->serialize(reinterpret_cast<uint64_t>(ioInfo));
    uint32_t num = initialize_random<uint32_t>();
    SERILAIZER()->output()->serialize(num);
    return num;
}

AXCL_EXPORT uint64_t axclrtEngineGetInputSizeByIndex(axclrtEngineIOInfo ioInfo, uint32_t group, uint32_t index) {
    SERILAIZER()->input()->serialize(reinterpret_cast<uint64_t>(ioInfo), group, index);
    uint64_t size = initialize_random<uint64_t>();
    SERILAIZER()->output()->serialize(size);
    return size;
}

AXCL_EXPORT uint64_t axclrtEngineGetOutputSizeByIndex(axclrtEngineIOInfo ioInfo, uint32_t group, uint32_t index) {
    SERILAIZER()->input()->serialize(reinterpret_cast<uint64_t>(ioInfo), group, index);
    uint64_t size = initialize_random<uint64_t>();
    SERILAIZER()->output()->serialize(size);
    return size;
}

AXCL_EXPORT const char *axclrtEngineGetInputNameByIndex(axclrtEngineIOInfo ioInfo, uint32_t index) {
    SERILAIZER()->input()->serialize(reinterpret_cast<uint64_t>(ioInfo), index);
    static const char *name = "InputName";
    uint8_array arr;
    arr.data = (void *)name;
    arr.size = strlen(name);
    SERILAIZER()->output()->serialize(arr);
    return name;
}

AXCL_EXPORT const char *axclrtEngineGetOutputNameByIndex(axclrtEngineIOInfo ioInfo, uint32_t index) {
    SERILAIZER()->input()->serialize(reinterpret_cast<uint64_t>(ioInfo), index);
    static const char *name = "OutputName";
    uint8_array arr;
    arr.data = (void *)name;
    arr.size = strlen(name);
    SERILAIZER()->output()->serialize(arr);
    return name;
}

AXCL_EXPORT int32_t axclrtEngineGetInputIndexByName(axclrtEngineIOInfo ioInfo, const char *name) {
    uint8_array arr;
    arr.data = (void *)name;
    arr.size = strlen(name);
    SERILAIZER()->input()->serialize(reinterpret_cast<uint64_t>(ioInfo), arr);
    int32_t index = initialize_random<int32_t>();
    SERILAIZER()->output()->serialize(index);
    return index;
}

AXCL_EXPORT int32_t axclrtEngineGetOutputIndexByName(axclrtEngineIOInfo ioInfo, const char *name) {
    uint8_array arr;
    arr.data = (void *)name;
    arr.size = strlen(name);
    SERILAIZER()->input()->serialize(reinterpret_cast<uint64_t>(ioInfo), arr);
    int32_t index = initialize_random<int32_t>();
    SERILAIZER()->output()->serialize(index);
    return index;
}

AXCL_EXPORT axclError axclrtEngineGetInputDims(axclrtEngineIOInfo ioInfo, uint32_t group, uint32_t index, axclrtEngineIODims *dims) {
    SERILAIZER()->input()->serialize(reinterpret_cast<uint64_t>(ioInfo), group, index);
    memset(dims, 0, sizeof(axclrtEngineIODims));
    dims->dimCount = create_int32_random_instance(1, AXCLRT_ENGINE_MAX_DIM_CNT);
    for (int32_t i = 0; i < dims->dimCount; ++i) {
        dims->dims[i] = initialize_random<int32_t>();
    }
    axclError ret = 0;
    SERILAIZER()->output()->serialize(ret, *dims);
    return ret;
}

AXCL_EXPORT axclError axclrtEngineGetOutputDims(axclrtEngineIOInfo ioInfo, uint32_t group, uint32_t index, axclrtEngineIODims *dims) {
    SERILAIZER()->input()->serialize(reinterpret_cast<uint64_t>(ioInfo), group, index);
    memset(dims, 0, sizeof(axclrtEngineIODims));
    dims->dimCount = create_int32_random_instance(1, AXCLRT_ENGINE_MAX_DIM_CNT);
    for (int32_t i = 0; i < dims->dimCount; ++i) {
        dims->dims[i] = initialize_random<int32_t>();
    }
    axclError ret = 0;
    SERILAIZER()->output()->serialize(ret, *dims);
    return ret;
}

AXCL_EXPORT int32_t axclrtEngineGetInputDataType(axclrtEngineIOInfo ioInfo, uint32_t index, axclrtEngineDataType *type) {
    SERILAIZER()->input()->serialize(reinterpret_cast<uint64_t>(ioInfo), index);
    const std::vector<axclrtEngineDataType> data_types = {
        AXCL_DATA_TYPE_NONE,   AXCL_DATA_TYPE_INT4,   AXCL_DATA_TYPE_UINT4, AXCL_DATA_TYPE_INT8,   AXCL_DATA_TYPE_UINT8,
        AXCL_DATA_TYPE_INT16,  AXCL_DATA_TYPE_UINT16, AXCL_DATA_TYPE_INT32, AXCL_DATA_TYPE_UINT32, AXCL_DATA_TYPE_INT64,
        AXCL_DATA_TYPE_UINT64, AXCL_DATA_TYPE_FP4,    AXCL_DATA_TYPE_FP8,   AXCL_DATA_TYPE_FP16,   AXCL_DATA_TYPE_BF16,
        AXCL_DATA_TYPE_FP32,   AXCL_DATA_TYPE_FP64};
    *type = choose_random_from_array<axclrtEngineDataType>(data_types);
    int32_t ret = initialize_random<int32_t>();
    SERILAIZER()->output()->serialize(ret, *type);
    return ret;
}

AXCL_EXPORT int32_t axclrtEngineGetOutputDataType(axclrtEngineIOInfo ioInfo, uint32_t index, axclrtEngineDataType *type) {
    SERILAIZER()->input()->serialize(reinterpret_cast<uint64_t>(ioInfo), index);
    const std::vector<axclrtEngineDataType> data_types = {
        AXCL_DATA_TYPE_NONE,   AXCL_DATA_TYPE_INT4,   AXCL_DATA_TYPE_UINT4, AXCL_DATA_TYPE_INT8,   AXCL_DATA_TYPE_UINT8,
        AXCL_DATA_TYPE_INT16,  AXCL_DATA_TYPE_UINT16, AXCL_DATA_TYPE_INT32, AXCL_DATA_TYPE_UINT32, AXCL_DATA_TYPE_INT64,
        AXCL_DATA_TYPE_UINT64, AXCL_DATA_TYPE_FP4,    AXCL_DATA_TYPE_FP8,   AXCL_DATA_TYPE_FP16,   AXCL_DATA_TYPE_BF16,
        AXCL_DATA_TYPE_FP32,   AXCL_DATA_TYPE_FP64};
    *type = choose_random_from_array<axclrtEngineDataType>(data_types);
    int32_t ret = initialize_random<int32_t>();
    SERILAIZER()->output()->serialize(ret, *type);
    return ret;
}

AXCL_EXPORT int32_t axclrtEngineGetInputDataLayout(axclrtEngineIOInfo ioInfo, uint32_t index, axclrtEngineDataLayout *layout) {
    SERILAIZER()->input()->serialize(reinterpret_cast<uint64_t>(ioInfo), index);
    const std::vector<axclrtEngineDataLayout> data_layouts = {AXCL_DATA_LAYOUT_NONE, AXCL_DATA_LAYOUT_NHWC, AXCL_DATA_LAYOUT_NCHW};
    *layout = choose_random_from_array<axclrtEngineDataLayout>(data_layouts);
    int32_t ret = initialize_random<int32_t>();
    SERILAIZER()->output()->serialize(ret, *layout);
    return ret;
}

AXCL_EXPORT int32_t axclrtEngineGetOutputDataLayout(axclrtEngineIOInfo ioInfo, uint32_t index, axclrtEngineDataLayout *layout) {
    SERILAIZER()->input()->serialize(reinterpret_cast<uint64_t>(ioInfo), index);
    const std::vector<axclrtEngineDataLayout> data_layouts = {AXCL_DATA_LAYOUT_NONE, AXCL_DATA_LAYOUT_NHWC, AXCL_DATA_LAYOUT_NCHW};
    *layout = choose_random_from_array<axclrtEngineDataLayout>(data_layouts);
    int32_t ret = initialize_random<int32_t>();
    SERILAIZER()->output()->serialize(ret, *layout);
    return ret;
}

AXCL_EXPORT axclError axclrtEngineCreateIO(axclrtEngineIOInfo ioInfo, axclrtEngineIO *io) {
    SERILAIZER()->input()->serialize(reinterpret_cast<uint64_t>(ioInfo));

    *io = reinterpret_cast<axclrtEngineIO>(initialize_random<uint64_t>());
    axclError ret = initialize_random<axclError>();
    SERILAIZER()->output()->serialize(ret, reinterpret_cast<uint64_t>(*io));
    return ret;
}

AXCL_EXPORT axclError axclrtEngineDestroyIO(axclrtEngineIO io) {
    IMPLEMENT_SERIALIZE(reinterpret_cast<uint64_t>(io));
}

AXCL_EXPORT axclError axclrtEngineSetInputBufferByIndex(axclrtEngineIO io, uint32_t index, const void *dataBuffer, uint64_t size) {
    uint8_array arr;
    arr.data = (void *)dataBuffer;
    arr.size = (uint32_t)size;
    IMPLEMENT_SERIALIZE(reinterpret_cast<uint64_t>(io), index, arr);
}

AXCL_EXPORT axclError axclrtEngineSetOutputBufferByIndex(axclrtEngineIO io, uint32_t index, const void *dataBuffer, uint64_t size) {
    uint8_array arr;
    arr.data = (void *)dataBuffer;
    arr.size = (uint32_t)size;
    IMPLEMENT_SERIALIZE(reinterpret_cast<uint64_t>(io), index, arr);
}

AXCL_EXPORT axclError axclrtEngineSetInputBufferByName(axclrtEngineIO io, const char *name, const void *dataBuffer, uint64_t size) {
    uint8_array arr1, arr2;
    arr1.data = (void *)name;
    arr1.size = (uint32_t)strlen(name);
    arr2.data = (void *)dataBuffer;
    arr2.size = (uint32_t)size;
    IMPLEMENT_SERIALIZE(reinterpret_cast<uint64_t>(io), arr1, arr2);
}

AXCL_EXPORT axclError axclrtEngineSetOutputBufferByName(axclrtEngineIO io, const char *name, const void *dataBuffer, uint64_t size) {
    uint8_array arr1, arr2;
    arr1.data = (void *)name;
    arr1.size = (uint32_t)strlen(name);
    arr2.data = (void *)dataBuffer;
    arr2.size = (uint32_t)size;
    IMPLEMENT_SERIALIZE(reinterpret_cast<uint64_t>(io), arr1, arr2);
}

static uint8_t g_buffer[4096];
AXCL_EXPORT axclError axclrtEngineGetInputBufferByIndex(axclrtEngineIO io, uint32_t index, void **dataBuffer, uint64_t *size) {
    SERILAIZER()->input()->serialize(reinterpret_cast<uint64_t>(io), index);
    fill_random_array(g_buffer, sizeof(g_buffer));
    *size = create_int32_random_instance(4, sizeof(g_buffer));
    *dataBuffer = reinterpret_cast<void *>(g_buffer);
    uint8_array arr;
    arr.data = *dataBuffer;
    arr.size = (uint32_t)*size;
    axclError ret = initialize_random<axclError>();
    SERILAIZER()->output()->serialize(ret, arr);
    return ret;
}

AXCL_EXPORT axclError axclrtEngineGetOutputBufferByIndex(axclrtEngineIO io, uint32_t index, void **dataBuffer, uint64_t *size) {
    SERILAIZER()->input()->serialize(reinterpret_cast<uint64_t>(io), index);
    fill_random_array(g_buffer, sizeof(g_buffer));
    *size = create_int32_random_instance(4, sizeof(g_buffer));
    *dataBuffer = reinterpret_cast<void *>(g_buffer);
    uint8_array arr;
    arr.data = *dataBuffer;
    arr.size = (uint32_t)*size;
    axclError ret = initialize_random<axclError>();
    SERILAIZER()->output()->serialize(ret, arr);
    return ret;
}

AXCL_EXPORT axclError axclrtEngineGetInputBufferByName(axclrtEngineIO io, const char *name, void **dataBuffer, uint64_t *size) {
    uint8_array arr1;
    arr1.data = (void *)name;
    arr1.size = strlen(name);
    SERILAIZER()->input()->serialize(reinterpret_cast<uint64_t>(io), arr1);
    fill_random_array(g_buffer, sizeof(g_buffer));
    *size = create_int32_random_instance(4, sizeof(g_buffer));
    *dataBuffer = reinterpret_cast<void *>(g_buffer);
    uint8_array arr2;
    arr2.data = *dataBuffer;
    arr2.size = (uint32_t)*size;
    axclError ret = initialize_random<axclError>();
    SERILAIZER()->output()->serialize(ret, arr2);
    return ret;
}

AXCL_EXPORT axclError axclrtEngineGetOutputBufferByName(axclrtEngineIO io, const char *name, void **dataBuffer, uint64_t *size) {
    uint8_array arr1;
    arr1.data = (void *)name;
    arr1.size = strlen(name);
    SERILAIZER()->input()->serialize(reinterpret_cast<uint64_t>(io), arr1);
    fill_random_array(g_buffer, sizeof(g_buffer));
    *size = create_int32_random_instance(4, sizeof(g_buffer));
    *dataBuffer = reinterpret_cast<void *>(g_buffer);
    uint8_array arr2;
    arr2.data = *dataBuffer;
    arr2.size = (uint32_t)*size;
    axclError ret = initialize_random<axclError>();
    SERILAIZER()->output()->serialize(ret, arr2);
    return ret;
}

AXCL_EXPORT axclError axclrtEngineSetDynamicBatchSize(axclrtEngineIO io, uint32_t batchSize) {
    IMPLEMENT_SERIALIZE(reinterpret_cast<uint64_t>(io), batchSize);
}

AXCL_EXPORT axclError axclrtEngineCreateContext(uint64_t modelId, uint64_t *contextId) {
    SERILAIZER()->input()->serialize(modelId);
    *contextId = initialize_random<uint64_t>();
    axclError ret = initialize_random<axclError>();
    SERILAIZER()->output()->serialize(ret, *contextId);
    return ret;
}

AXCL_EXPORT axclError axclrtEngineExecute(uint64_t modelId, uint64_t contextId, uint32_t group, axclrtEngineIO io) {
    IMPLEMENT_SERIALIZE(modelId, contextId, group, reinterpret_cast<uint64_t>(io));
}

AXCL_EXPORT axclError axclrtEngineExecuteAsync(uint64_t modelId, uint64_t contextId, uint32_t group, axclrtEngineIO io,
                                               axclrtStream stream) {
    IMPLEMENT_SERIALIZE(modelId, contextId, group, reinterpret_cast<uint64_t>(io), reinterpret_cast<uint64_t>(stream));
}
