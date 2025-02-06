/**************************************************************************************************
 *
 * Copyright (c) 2019-2024 Axera Semiconductor Co., Ltd. All Rights Reserved.
 *
 * This source file is the property of Axera Semiconductor Co., Ltd. and
 * may not be copied or distributed in any isomorphic form without the prior
 * written consent of Axera Semiconductor Co., Ltd.
 *
 **************************************************************************************************/

#include <algorithm>
#include <cstdint>
#include <random>
#include <type_traits>

template <typename T>
std::enable_if_t<std::is_floating_point_v<T>, T> initialize_random_ex(float min, float max, int decimal_places) {
    if (min >= max) {
        throw std::invalid_argument("min must be less than max");
    }

    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_real_distribution<T> dist(min, max);

    T random_value = dist(gen);

    float scale = std::pow(10.0f, decimal_places);
    random_value = std::round(random_value * scale) / scale;

    return random_value;
}

/**
 * Important =>:
 * If POD structure, padding also be set to random, for example
 *    struct MyStruct {
 *       char c;
 *       int  a;
 *    };
 *    struct MyStruct t1 = initialize_random<MyStruct>();
 *    print_hex(&t1, sizeof(t1));
 *
 *    A5 04 06 C5 CC 4C 4B E6
 *    t1.c = 0xA5;
 *    t2.a = 0xE64B4CCC
 *    padding: 04 06 C5
 */
template <typename T>
std::enable_if_t<std::is_trivially_copyable_v<T> && std::is_trivially_constructible_v<T>, T> initialize_random() {
    T obj{};

    // Special handling for floating-point types
    if constexpr (std::is_floating_point_v<T>) {
        std::random_device rd;
        std::mt19937 gen(rd());
        std::uniform_real_distribution<T> dist(-100.0, 100.0); // Adjust range as needed
        obj = dist(gen);
    } else {
        // For integral and other trivially copyable types
        uint8_t* mem = reinterpret_cast<uint8_t*>(&obj);
        size_t size = sizeof(T);

        std::random_device rd;
        std::mt19937 gen(rd());
        std::uniform_int_distribution<uint8_t> dist(0, 255);
        std::generate(mem, mem + size, [&]() -> uint8_t { return dist(gen); });
    }

    return obj;
}

template <typename T>
T create_enum_random_instance(T min, T max) {
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<int32_t> dist(min, max);
    return static_cast<T>(dist(gen));
}

template <typename T>
T choose_random_from_array(const std::vector<T>& arr) {
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<> dist(0, arr.size() - 1);
    return arr[dist(gen)];
}

extern int32_t create_int32_random_instance(int32_t min, int32_t max);
extern void fill_random_array(uint8_t *arr, uint32_t size);
