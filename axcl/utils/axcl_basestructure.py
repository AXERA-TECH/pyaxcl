from ctypes import Structure, Union, Array, sizeof, memset, byref, addressof, pointer, cast, c_void_p, c_char_p, POINTER
from axcl.ax_base_type import *
import random
import os
import sys
import traceback

class StructureError(Exception):
    pass

class UnionError(Exception):
    pass

class BaseUnion(Union):
    value_union_type_mapping = {}
    field_aliases = {}

class BaseStructure(Structure):
    field_aliases = {}
    name_union_type_mapping = {}
    _fields_dict = {}

    p_type_list = [
        POINTER(AX_U64),
        POINTER(AX_U32),
        POINTER(AX_U16),
        POINTER(AX_U8),
        POINTER(AX_S64),
        POINTER(AX_S32),
        POINTER(AX_S16),
        POINTER(AX_S8),
        POINTER(AX_CHAR),
        POINTER(AX_LONG),
        POINTER(AX_ULONG),
        POINTER(AX_ADDR),
        POINTER(AX_F32),
        POINTER(AX_F64),
        POINTER(c_char_p),
        c_void_p
    ]

    def __init__(self):
        self._fields_dict = dict(self._fields_)

    def get_field_value(self, field_name, parent=None):
        if len(self._fields_dict) == 0:
            self._fields_dict = dict(self._fields_)
        if field_name in self._fields_dict:
            return getattr(self, field_name, None)
        elif parent is not None:
            return getattr(parent, field_name, None)
        return None

    def get_union_struct(self, u_name, parent):
        union_val = getattr(self, u_name)
        type_field_name = self.name_union_type_mapping.get(u_name)

        type_value = self.get_field_value(type_field_name, parent)
        if type_value is None:
            return None, "", ""

        struct_field_name = union_val.value_union_type_mapping.get(type_value)
        if struct_field_name is None:
            return None, "", ""

        struct_alias = union_val.field_aliases.get(struct_field_name, struct_field_name)
        return getattr(union_val, struct_field_name), struct_field_name, struct_alias

    def dict2struct(self, d, parent=None):
        # try:
        for field_name, field_type in self._fields_:
            alias = self.field_aliases.get(field_name, field_name)
            if alias in d:
                value = d.get(alias, 0)
                current_field = getattr(self, field_name)
                if isinstance(current_field, BaseStructure):
                    current_field.dict2struct(value)
                elif isinstance(current_field, Array):
                    self.dict_handle_array(current_field, value)
                else:
                    if field_type in self.p_type_list:
                        setattr(self, field_name, cast(value, field_type))
                    else:
                        setattr(self, field_name, field_type(value))
            else:
                current_field = getattr(self, field_name)
                if isinstance(current_field, Union):
                    u_field_val, u_field_name, u_alias = self.get_union_struct(field_name, parent)
                    d_value = d.get(u_alias, -1)
                    if d_value != -1:
                        if u_field_val is not None:
                            if isinstance(u_field_val, Array):
                                self.dict_handle_array(u_field_val, d_value, parent)
                            else:
                                u_field_val.dict2struct(d_value, parent)
        # except:
        #     print(sys.exc_info())
        #     print(traceback.format_exc())

    def dict_handle_array(self, current_field, value, parent=None):
        if not isinstance(value, (list, tuple)):
            raise StructureError(f"Expected list or tuple for array field, got {type(value)}.")
        memset(byref(current_field), 0, sizeof(current_field))
        length = len(current_field)
        for i, val in enumerate(value):
            if i >= length:
                break
            if isinstance(current_field[i], BaseStructure):
                current_field[i].dict2struct(val, parent)
            elif isinstance(current_field[i], Array):
                self.dict_handle_array(current_field[i], val, parent)
            else:
                current_field[i] = val

    def struct2dict(self, parent=None):
        result = {}
        for field_name, _ in self._fields_:
            value = getattr(self, field_name)
            alias = self.field_aliases.get(field_name, field_name)

            if isinstance(value, BaseStructure):
                result[alias] = value.struct2dict()
            elif isinstance(value, Array):
                result[alias] = self.struct_handle_array(value)
            elif isinstance(value, Union):
                u_field_val, u_field_name, u_alias = self.get_union_struct(field_name, parent)
                if u_field_val is not None:
                    if isinstance(u_field_val, Array):
                        result[u_alias] = self.struct_handle_array(u_field_val, parent)
                    else:
                        result[u_alias] = u_field_val.struct2dict(parent)
            else:
                result[alias] = value

        return result

    def struct_handle_array(self, array, parent=None):
        result_list = []
        for item in array:
            if isinstance(item, BaseStructure):
                result_list.append(item.struct2dict(parent))
            elif isinstance(item, Array):
                result_list.append(self.struct_handle_array(item, parent))
            else:
                result_list.append(item)
        return result_list

    def random_struct(self, parent=None):
        d = self.struct2dict(parent)

        for field_name, field_type in self._fields_:
            alias = self.field_aliases.get(field_name, field_name)
            if alias in d:
                value = d.get(alias, 0)
                current_field = getattr(self, field_name)
                if isinstance(current_field, BaseStructure):
                    current_field.random_struct(value)
                elif isinstance(current_field, Array):
                    self.dict_handle_random_array(current_field, value)
                else:
                    if field_type in self.p_type_list:
                        setattr(self, field_name, cast(random.randint(0, 255), field_type))
                    elif field_name in self.name_union_type_mapping.values():
                        pass
                    else:
                        setattr(self, field_name, field_type(random.randint(0, 255)))
            else:
                current_field = getattr(self, field_name)
                if isinstance(current_field, Union):
                    u_field_val, u_field_name, u_alias = self.get_union_struct(field_name, parent)
                    d_value = d.get(u_alias, 0)
                    if u_field_val is not None:
                        if isinstance(u_field_val, Array):
                            self.dict_handle_array(u_field_val, d_value, parent)
                        else:
                            u_field_val.random_struct(parent)

    def dict_handle_random_array(self, current_field, value, parent=None):
        if not isinstance(value, (list, tuple)):
            raise StructureError(f"Expected list or tuple for array field, got {type(value)}.")
        memset(byref(current_field), 0, sizeof(current_field))
        length = len(current_field)
        for i, val in enumerate(value):
            if i >= length:
                break
            if isinstance(current_field[i], BaseStructure):
                current_field[i].random_struct(parent)
            elif isinstance(current_field[i], Array):
                self.dict_handle_random_array(current_field[i], val, parent)
            else:
                current_field[i] = random.randint(0, 255)