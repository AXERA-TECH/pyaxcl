/**************************************************************************************************
 *
 * Copyright (c) 2019-2024 Axera Semiconductor Co., Ltd. All Rights Reserved.
 *
 * This source file is the property of Axera Semiconductor Co., Ltd. and
 * may not be copied or distributed in any isomorphic form without the prior
 * written consent of Axera Semiconductor Co., Ltd.
 *
 **************************************************************************************************/


#ifndef __AXCL_STUB_API_H__
#define __AXCL_STUB_API_H__

#include "axcl_base.h"

#ifdef __cplusplus
extern "C" {
#endif

int32_t AXCL_STUB_CheckInputAndOutput(const void* input, uint32_t input_size, const void* output, uint32_t output_size);

#ifdef __cplusplus
}
#endif

#endif /* __AXCL_STUB_API_H__ */