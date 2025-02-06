/**************************************************************************************************
 *
 * Copyright (c) 2019-2024 Axera Semiconductor Co., Ltd. All Rights Reserved.
 *
 * This source file is the property of Axera Semiconductor Co., Ltd. and
 * may not be copied or distributed in any isomorphic form without the prior
 * written consent of Axera Semiconductor Co., Ltd.
 *
 **************************************************************************************************/

#include <cstdint>
#include <iostream>
#include <type_traits>
#include <vector>
#include "singleton.hpp"

struct uint8_array {
    void* data = nullptr;
    uint32_t size = 0;
};

class serialize_helper {
public:
    serialize_helper() {
        m_data.reserve(1024);
    }

    template <typename... Args>
    void serialize(Args&&... args) {
        clear();
        (add(std::forward<Args>(args)), ...);
    }

    template <typename T>
    std::enable_if_t<std::is_enum_v<T> && !std::is_pointer_v<T>, void> add(T value) {
        insert(&value, sizeof(T));
    }

    template <typename T>
    std::enable_if_t<std::is_fundamental_v<T> && !std::is_pointer_v<T>, void> add(const T& value) {
        insert(&value, sizeof(T));
    }

    template <typename T>
    std::enable_if_t<std::is_class_v<T> && std::is_trivially_copyable_v<T> && !std::is_same_v<T, uint8_array> && !std::is_pointer_v<T>,
                     void>
    add(const T& value) {
        insert(&value, sizeof(T));
    }

    template <typename T>
    std::enable_if_t<std::is_pointer_v<T> && std::is_class_v<std::remove_const_t<std::remove_pointer_t<T>>> &&
                         std::is_trivially_copyable_v<std::remove_const_t<std::remove_pointer_t<T>>>,
                     void>
    add(const T value) {
        if (value) {
            insert(value, sizeof(*value));
        } else {
            std::cout << "add nil pointer\n";
        }
    }

    template <typename T>
    std::enable_if_t<std::is_same_v<T, uint8_array> && !std::is_pointer_v<T>, void> add(const T& value) {
        insert(value.data, value.size);
    }

    void add(const void* buf, size_t size) {
        insert(buf, size);
    }

    void clear() noexcept {
        m_data.clear();
    }

    const std::vector<uint8_t>& data() const noexcept {
        return m_data;
    }

private:
    void insert(const void* buf, size_t size) {
        if (buf && size > 0) {
            if (m_data.capacity() < m_data.size() + size) {
                m_data.reserve(m_data.size() + size);
            }

            const uint8_t* p = static_cast<const uint8_t*>(buf);
            m_data.insert(m_data.end(), p, p + size);
        }
    }

private:
    std::vector<uint8_t> m_data;
};

class serializer : public axcl::singleton<serializer> {
    friend class axcl::singleton<serializer>;

public:
    serialize_helper* input() {
        return &m_input;
    }

    serialize_helper* output() {
        return &m_output;
    }

private:
    serializer() = default;

private:
    serialize_helper m_input;
    serialize_helper m_output;
};

#define SERILAIZER() serializer::get_instance()
