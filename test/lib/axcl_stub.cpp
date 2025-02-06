
/**************************************************************************************************
 *
 * Copyright (c) 2019-2024 Axera Semiconductor Co., Ltd. All Rights Reserved.
 *
 * This source file is the property of Axera Semiconductor Co., Ltd. and
 * may not be copied or distributed in any isomorphic form without the prior
 * written consent of Axera Semiconductor Co., Ltd.
 *
 **************************************************************************************************/

#include "axcl_stub.h"
#include <stdio.h>
#include <string.h>
#include "serializer.hpp"

static void print_hex_array(const char* title, const uint8_t* const buf, uint32_t len) {
    printf("\n%s:\n", title);
    for (uint32_t i = 0; i < len; ++i) {
        printf("%02X ", buf[i]);
        if ((i + 1) % 16 == 0 || i == (len - 1)) {
            printf("\n");
        }
    }
}

AXCL_EXPORT int32_t AXCL_STUB_CheckInputAndOutput(const void* input, uint32_t input_size, const void* output, uint32_t output_size) {
    const auto& input_compare = SERILAIZER()->input()->data();
    if (input_compare.size() != input_size) {
        printf("input args size check fail, c api %ld != input %d\n", input_compare.size(), input_size);
        return 1;
    }

    if (input_size > 0) {
        if (0 != ::memcmp(input_compare.data(), input, input_size)) {
            print_hex_array("c api", input_compare.data(), input_size);
            print_hex_array("input", static_cast<const uint8_t*>(input), input_size);
            return 1;
        }
    }

    const auto& output_compare = SERILAIZER()->output()->data();
    if (output_compare.size() != output_size) {
        printf("output args size check fail, c api %ld != output %d\n", output_compare.size(), output_size);
        return 1;
    }

    if (output_size > 0) {
        if (0 != ::memcmp(output_compare.data(), output, output_size)) {
            print_hex_array("c  api", output_compare.data(), output_size);
            print_hex_array("output", static_cast<const uint8_t*>(output), output_size);
            return 1;
        }
    }

    return 0;
}