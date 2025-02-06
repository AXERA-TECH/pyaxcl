# !/usr/bin/env python
# -*- coding:utf-8 -*-
# ******************************************************************************
#
#  Copyright (c) 2019-2024 Axera Semiconductor Co., Ltd. All Rights Reserved.
#
#  This source file is the property of Axera Semiconductor Co., Ltd. and
#  may not be copied or distributed in any isomorphic form without the prior
#  written consent of Axera Semiconductor Co., Ltd.
#
# ******************************************************************************

from ctypes import Structure

import os
import sys
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)

from axcl.ax_global_type import *
from axcl.utils.axcl_utils import *
from axcl.utils.axcl_basestructure import *


MAX_JENC_EXIF_IMAGE_DESC_LEN            = 128
MAX_JENC_EXIF_MAKE_LEN                  = 32
MAX_JENC_EXIF_MODEL_LEN                 = 32
MAX_JENC_EXIF_SOFTWARE_LEN              = 32
MAX_JENC_EXIF_DATETIME_LEN              = 20
MAX_JENC_EXIF_WHITE_POINT_LEN           = 2
MAX_JENC_EXIF_PRIMARY_CHROMATICITY_LEN  = 6
MAX_JENX_EXIF_YCBCR_COEFFICIENTS_LEN    = 3
MAX_JENC_EXIF_REFERENCE_BLACK_WHITE_LEN = 6
MAX_JENC_EXIF_VERSION_LEN               = 4
MAX_JENC_EXIF_COMPONENTS_CONFIG_LEN     = 4
MAX_JENC_EXIF_GPS_TIME_STAMP_LEN        = 3
MAX_JENC_EXIF_GPS_SATELLITES_LEN        = 64
MAX_JENC_EXIF_GPS_MAP_DATUM_LEN         = 12
MAX_JENC_EXIF_GPS_PROCESSING_METHOD_LEN = 64
MAX_JENC_EXIF_GPS_AREA_INFORMATION_LEN  = 64
MAX_JENC_EXIF_GPS_DATE_STAMP_LEN        = 10

AX_VENC_EXIF_ORIENTATION_E = AX_S32
"""
    exif orientation.

    .. parsed-literal::

        AX_VENC_EXIF_ORIENTATION_NONE = 0
        AX_VENC_EXIF_ORIENTATION_DEFAULT = 1
        AX_VENC_EXIF_ORIENTATION_FLIP_HORIZONTAL = 2
        AX_VENC_EXIF_ORIENTATION_ROTATE_180 = 3
        AX_VENC_EXIF_ORIENTATION_FLIP_VERTICAL = 4
        AX_VENC_EXIF_ORIENTATION_TRANSPOSE = 5
        AX_VENC_EXIF_ORIENTATION_ROTATE_90_CLOCKWISE = 6
        AX_VENC_EXIF_ORIENTATION_TRANSVERSE = 7
        AX_VENC_EXIF_ORIENTATION_ROTATE_270_CLOCKWISE = 8
"""
AX_VENC_EXIF_ORIENTATION_NONE = 0
AX_VENC_EXIF_ORIENTATION_DEFAULT = 1
AX_VENC_EXIF_ORIENTATION_FLIP_HORIZONTAL = 2
AX_VENC_EXIF_ORIENTATION_ROTATE_180 = 3
AX_VENC_EXIF_ORIENTATION_FLIP_VERTICAL = 4
AX_VENC_EXIF_ORIENTATION_TRANSPOSE = 5
AX_VENC_EXIF_ORIENTATION_ROTATE_90_CLOCKWISE = 6
AX_VENC_EXIF_ORIENTATION_TRANSVERSE = 7
AX_VENC_EXIF_ORIENTATION_ROTATE_270_CLOCKWISE = 8


AX_VENC_EXIF_RES_UNIT_E = AX_S32
"""
    exif resolution unit.

    .. parsed-literal::

        AX_VENC_EXIF_RES_UNIT_NONE = 0
        AX_VENC_EXIF_RES_UNIT_UNKNOWN = 1
        AX_VENC_EXIF_RES_UNIT_INCHES = 2
        AX_VENC_EXIF_RES_UNIT_CENTIMETERS = 3
"""
AX_VENC_EXIF_RES_UNIT_NONE = 0
AX_VENC_EXIF_RES_UNIT_UNKNOWN = 1
AX_VENC_EXIF_RES_UNIT_INCHES = 2
AX_VENC_EXIF_RES_UNIT_CENTIMETERS = 3


AX_VENC_EXIF_YCBCR_POSITIONING_E = AX_S32
"""
    exif YCBCR positioning.

    .. parsed-literal::

        AX_VENC_EXIF_YCBCR_POSITIONING_NONE = 0
        AX_VENC_EXIF_YCBCR_POSITIONING_CENTERED = 1
        AX_VENC_EXIF_YCBCR_POSITIONING_COSITED = 2
"""
AX_VENC_EXIF_YCBCR_POSITIONING_NONE = 0
AX_VENC_EXIF_YCBCR_POSITIONING_CENTERED = 1
AX_VENC_EXIF_YCBCR_POSITIONING_COSITED = 2


AX_VENC_EXIF_EXPOSURE_PROGRAM_E = AX_S32
"""
    exif exposure program.

    .. parsed-literal::

        AX_VENC_EXIF_EXPOSURE_PROGRAM_NONE = 0
        AX_VENC_EXIF_EXPOSURE_PROGRAM_MANUAL = 1
        AX_VENC_EXIF_EXPOSURE_PROGRAM_NORMAL = 2
        AX_VENC_EXIF_EXPOSURE_PROGRAM_APERTURE_PRIORITY  = 3
        AX_VENC_EXIF_EXPOSURE_PROGRAM_SHUTTER_PRIORITY = 4
        AX_VENC_EXIF_EXPOSURE_PROGRAM_CREATIVE = 4
        AX_VENC_EXIF_EXPOSURE_PROGRAM_ACTION = 5
        AX_VENC_EXIF_EXPOSURE_PROGRAM_PORTRAIT = 6
        AX_VENC_EXIF_EXPOSURE_PROGRAM_LANDSCAPE = 7
"""
AX_VENC_EXIF_EXPOSURE_PROGRAM_NONE = 0
AX_VENC_EXIF_EXPOSURE_PROGRAM_MANUAL = 1
AX_VENC_EXIF_EXPOSURE_PROGRAM_NORMAL = 2
AX_VENC_EXIF_EXPOSURE_PROGRAM_APERTURE_PRIORITY  = 3
AX_VENC_EXIF_EXPOSURE_PROGRAM_SHUTTER_PRIORITY = 4
AX_VENC_EXIF_EXPOSURE_PROGRAM_CREATIVE = 4
AX_VENC_EXIF_EXPOSURE_PROGRAM_ACTION = 5
AX_VENC_EXIF_EXPOSURE_PROGRAM_PORTRAIT = 6
AX_VENC_EXIF_EXPOSURE_PROGRAM_LANDSCAPE = 7


AX_VENC_EXIF_COLOR_SPACE_E = AX_S32
"""
    exif color space.

    .. parsed-literal::

        AX_VENC_EXIF_COLOR_SPACE_NONE = 0
        AX_VENC_EXIF_COLOR_SPACE_SRGB = 1
        AX_VENC_EXIF_COLOR_SPACE_UNCALIBRATED = 65535
"""
AX_VENC_EXIF_COLOR_SPACE_NONE = 0
AX_VENC_EXIF_COLOR_SPACE_SRGB = 1
AX_VENC_EXIF_COLOR_SPACE_UNCALIBRATED = 65535


AX_VENC_EXIF_METERING_MODE_E = AX_S32
"""
    exif metering mode.

    .. parsed-literal::

        AX_VENC_EXIF_METERING_MODE_NONE = 0
        AX_VENC_EXIF_METERING_MODE_UNKNOWN = 1
        AX_VENC_EXIF_METERING_MODE_AVERAGE = 2
        AX_VENC_EXIF_METERING_MODE_CENTER_WEIGHTED = 3
        AX_VENC_EXIF_METERING_MODE_SPOT = 4
        AX_VENC_EXIF_METERING_MODE_MULTI_SPOT = 5
        AX_VENC_EXIF_METERING_MODE_OTHER = 255
"""
AX_VENC_EXIF_METERING_MODE_NONE = 0
AX_VENC_EXIF_METERING_MODE_UNKNOWN = 1
AX_VENC_EXIF_METERING_MODE_AVERAGE = 2
AX_VENC_EXIF_METERING_MODE_CENTER_WEIGHTED = 3
AX_VENC_EXIF_METERING_MODE_SPOT = 4
AX_VENC_EXIF_METERING_MODE_MULTI_SPOT = 5
AX_VENC_EXIF_METERING_MODE_OTHER = 255


AX_VENC_EXIF_FLASH_E = AX_S32
"""
    exif flash.

    .. parsed-literal::

        AX_VENC_EXIF_FLASH_NONE = 0
        AX_VENC_EXIF_FLASH_NOLIGHT = 1
        AX_VENC_EXIF_FLASH_FIRED = 2
        AX_VENC_EXIF_FLASH_FIRED_RETURN_LIGHT_NONE = 6
        AX_VENC_EXIF_FLASH_FIRED_RETURN_LIGHT = 8
"""
AX_VENC_EXIF_FLASH_NONE = 0
AX_VENC_EXIF_FLASH_NOLIGHT = 1
AX_VENC_EXIF_FLASH_FIRED = 2
AX_VENC_EXIF_FLASH_FIRED_RETURN_LIGHT_NONE = 6
AX_VENC_EXIF_FLASH_FIRED_RETURN_LIGHT = 8


AX_VENC_EXIF_GPS_LATITUDE_REF_E = AX_S32
"""
    exif GPS latitude reference.

    .. parsed-literal::

        AX_VENC_EXIF_GPS_LATITUDE_REF_NONE = 0
        AX_VENC_EXIF_GPS_LATITUDE_REF_NORTH = 1
        AX_VENC_EXIF_GPS_LATITUDE_REF_SOUTH = 2
"""
AX_VENC_EXIF_GPS_LATITUDE_REF_NONE = 0
AX_VENC_EXIF_GPS_LATITUDE_REF_NORTH = 1
AX_VENC_EXIF_GPS_LATITUDE_REF_SOUTH = 2


AX_VENC_EXIF_GPS_LONGITUDE_REF_E = AX_S32
"""
    exif GPS longitude reference.

    .. parsed-literal::

        AX_VENC_EXIF_GPS_LONGITUDE_REF_NONE = 0
        AX_VENC_EXIF_GPS_LONGITUDE_REF_EAST = 1
        AX_VENC_EXIF_GPS_LONGITUDE_REF_WEST = 2
"""
AX_VENC_EXIF_GPS_LONGITUDE_REF_NONE = 0
AX_VENC_EXIF_GPS_LONGITUDE_REF_EAST = 1
AX_VENC_EXIF_GPS_LONGITUDE_REF_WEST = 2


AX_VENC_EXIF_GPS_ALTITUDE_REF_E = AX_S32
"""
    exif GPS altitude reference.

    .. parsed-literal::

        AX_VENC_EXIF_GPS_ALTITUDE_REF_NONE = 0
        AX_VENC_EXIF_GPS_ALTITUDE_REF_ABOVE_SEA_LEVEL = 1
        AX_VENC_EXIF_GPS_ALTITUDE_REF_BELOW_SEA_LEVEL = 2
"""
AX_VENC_EXIF_GPS_ALTITUDE_REF_NONE = 0
AX_VENC_EXIF_GPS_ALTITUDE_REF_ABOVE_SEA_LEVEL = 1
AX_VENC_EXIF_GPS_ALTITUDE_REF_BELOW_SEA_LEVEL = 2


AX_VENC_EXIF_GPS_SPEED_REF_E = AX_S32
"""
    exif GPS speed reference.

    .. parsed-literal::

        AX_VENC_EXIF_GPS_SPEED_REF_NONE = 0
        AX_VENC_EXIF_GPS_SPEED_REF_KILOMETERS_PER_HOUR = 1
        AX_VENC_EXIF_GPS_SPEED_REF_MILES_PER_HOUR = 2
        AX_VENC_EXIF_GPS_SPEED_REF_KNOTS = 3
"""
AX_VENC_EXIF_GPS_SPEED_REF_NONE = 0
AX_VENC_EXIF_GPS_SPEED_REF_KILOMETERS_PER_HOUR = 1
AX_VENC_EXIF_GPS_SPEED_REF_MILES_PER_HOUR = 2
AX_VENC_EXIF_GPS_SPEED_REF_KNOTS = 3


AX_VENC_EXIF_GPS_STATUS_E = AX_S32
"""
    exif GPS status.

    .. parsed-literal::

        AX_VENC_EXIF_GPS_STATUS_NONE = 0
        AX_VENC_EXIF_GPS_STATUS_VOID = 1
        AX_VENC_EXIF_GPS_STATUS_ACTIVE = 2
"""
AX_VENC_EXIF_GPS_STATUS_NONE = 0
AX_VENC_EXIF_GPS_STATUS_VOID = 1
AX_VENC_EXIF_GPS_STATUS_ACTIVE = 2


AX_VENC_EXIF_GPS_MEASURE_MODE_E  = AX_S32
"""
    exif GPS measure mode.

    .. parsed-literal::

        AX_VENC_EXIF_GPS_MEASURE_MODE_NONE = 0
        AX_VENC_EXIF_GPS_MEASURE_MODE_2D = 2
        AX_VENC_EXIF_GPS_MEASURE_MODE_3D = 3
"""
AX_VENC_EXIF_GPS_MEASURE_MODE_NONE = 0
AX_VENC_EXIF_GPS_MEASURE_MODE_2D = 2
AX_VENC_EXIF_GPS_MEASURE_MODE_3D = 3


AX_VENC_EXIF_GPS_DISTANCE_REF_E = AX_S32
"""
    exif GPS distance reference.

    .. parsed-literal::

        AX_VENC_EXIF_GPS_DISTANCE_REF_NONE = 0
        AX_VENC_EXIF_GPS_DISTANCE_REF_KILOMETERS = 1
        AX_VENC_EXIF_GPS_DISTANCE_REF_METERS = 2
        AX_VENC_EXIF_GPS_DISTANCE_REF_NAUTICAL_MILES = 2
"""
AX_VENC_EXIF_GPS_DISTANCE_REF_NONE = 0
AX_VENC_EXIF_GPS_DISTANCE_REF_KILOMETERS = 1
AX_VENC_EXIF_GPS_DISTANCE_REF_METERS = 2
AX_VENC_EXIF_GPS_DISTANCE_REF_NAUTICAL_MILES = 2


AX_VENC_EXIF_GPS_DIFFERENTIAL_E = AX_S32
"""
    exif GPS differential.

    .. parsed-literal::

        AX_VENC_EXIF_GPS_DIFFERENTIAL_NONE = 0
        AX_VENC_EXIF_GPS_DIFFERENTIAL_NOT_APPLIED = 1
        AX_VENC_EXIF_GPS_DIFFERENTIAL_APPLIED = 2
"""
AX_VENC_EXIF_GPS_DIFFERENTIAL_NONE = 0
AX_VENC_EXIF_GPS_DIFFERENTIAL_NOT_APPLIED = 1
AX_VENC_EXIF_GPS_DIFFERENTIAL_APPLIED = 2


AX_VENC_EXIF_GPS_NORTH_REF_E = AX_S32
"""
    exif GPS north reference.

    .. parsed-literal::

        AX_VENC_EXIF_GPS_NORTH_REF_NONE = 0
        AX_VENC_EXIF_GPS_NORTH_REF_TRUE = 1
        AX_VENC_EXIF_GPS_NORTH_REF_MAGNETIC = 2
"""
AX_VENC_EXIF_GPS_NORTH_REF_NONE = 0
AX_VENC_EXIF_GPS_NORTH_REF_TRUE = 1
AX_VENC_EXIF_GPS_NORTH_REF_MAGNETIC = 2


class AX_VENC_EXIF_IFD0_INFO_T(BaseStructure):
    """
    .. parsed-literal::

        dict_exif_ifd0_info = {
            "image_description": [int],
            "make": [int],
            "model": [int],
            "orientation": :class:`AX_VENC_EXIF_ORIENTATION_E <axcl.venc.axcl_venc_exif.AX_VENC_EXIF_ORIENTATION_E>`,
            "x_resolution": int,
            "y_resolution": int,
            "resolution_unit": :class:`AX_VENC_EXIF_RES_UNIT_E <axcl.venc.axcl_venc_exif.AX_VENC_EXIF_RES_UNIT_E>`,
            "software": [int],
            "date_time": [int],
            "white_point": [int],
            "primary_chromaticities": [int],
            "y_cbcr_coefficients": [int],
            "y_cbcr_positioning": :class:`AX_VENC_EXIF_YCBCR_POSITIONING_E <axcl.venc.axcl_venc_exif.AX_VENC_EXIF_YCBCR_POSITIONING_E>`,
            "reference_blackWhite": [int]
        }
    """
    _fields_ = [
        ("u8ImageDescription", AX_U8 * MAX_JENC_EXIF_IMAGE_DESC_LEN),
        ("u8Make", AX_U8 * MAX_JENC_EXIF_MAKE_LEN),
        ("u8Model", AX_U8 *MAX_JENC_EXIF_MODEL_LEN),
        ("enOrientation", AX_VENC_EXIF_ORIENTATION_E),
        ("u32XResolution", AX_U32), # default: 72 / 1
        ("u32YResolution", AX_U32), # default: 72 / 1
        ("enResolutionUnit", AX_VENC_EXIF_RES_UNIT_E),
        ("u8Software", AX_U8 * MAX_JENC_EXIF_SOFTWARE_LEN),
        ("u8DateTime", AX_U8 * MAX_JENC_EXIF_DATETIME_LEN),
        ("u32WhitePoint", AX_U32 * MAX_JENC_EXIF_WHITE_POINT_LEN),
        ("u32PrimaryChromaticities", AX_U32 * MAX_JENC_EXIF_PRIMARY_CHROMATICITY_LEN),
        ("f32YCbCrCoefficients", AX_F32 * MAX_JENX_EXIF_YCBCR_COEFFICIENTS_LEN),
        ("enYCbCrPositioning", AX_VENC_EXIF_YCBCR_POSITIONING_E),
        ("u16ReferenceBlackWhite", AX_U16 * MAX_JENC_EXIF_REFERENCE_BLACK_WHITE_LEN)
    ]
    field_aliases = {
        "u8ImageDescription": "image_description",
        "u8Make": "make",
        "u8Model": "model",
        "enOrientation": "orientation",
        "u32XResolution": "x_resolution",
        "u32YResolution": "y_resolution",
        "enResolutionUnit": "resolution_unit",
        "u8Software": "software",
        "u8DateTime": "date_time",
        "u32WhitePoint": "white_point",
        "u32PrimaryChromaticities": "primary_chromaticities",
        "f32YCbCrCoefficients": "y_cbcr_coefficients",
        "enYCbCrPositioning": "y_cbcr_positioning",
        "u16ReferenceBlackWhite": "reference_blackWhite"
    }


class AX_VENC_EXIF_SUBIFD_INFO_T(BaseStructure):
    """
    .. parsed-literal::

        dict_exif_subifd_info = {
            "eposure_time": int,
            "f_number": int,
            "exposure_program": :class:`AX_VENC_EXIF_EXPOSURE_PROGRAM_E <axcl.venc.axcl_venc_exif.AX_VENC_EXIF_EXPOSURE_PROGRAM_E>`,
            "iso_speed_ratings": int,
            "exif_version": [int],
            "date_time_original": [int],
            "date_time_digitized": [int],
            "components_configuration": [int],
            "compressed_bits_per_pixel": int,
            "shutter_speed_value": int,
            "aperture_value": int,
            "brightness_value": int,
            "exposure_bias_value": int,
            "max_aperture_value": int,
            "subject_distance": int,
            "metering_mode": :class:`AX_VENC_EXIF_METERING_MODE_E <axcl.venc.axcl_venc_exif.AX_VENC_EXIF_METERING_MODE_E>`,
            "light_source": int,
            "flash": :class:`AX_VENC_EXIF_FLASH_E <axcl.venc.axcl_venc_exif.AX_VENC_EXIF_FLASH_E>`,
            "focal_length": int,
            "subsec_time": int,
            "subsec_time_original": int,
            "subsec_time_digitized": int,
            "flash_pix_version": [int],
            "color_space": :class:`AX_VENC_EXIF_COLOR_SPACE_E <axcl.venc.axcl_venc_exif.AX_VENC_EXIF_COLOR_SPACE_E>`,
            "exif_image_width": int,
            "exif_image_height": int,
            "focal_plane_x_resolution": int,
            "focal_plane_y_resolution": int,
            "focal_plane_resolution_unit": :class:`AX_VENC_EXIF_RES_UNIT_E <axcl.venc.axcl_venc_exif.AX_VENC_EXIF_RES_UNIT_E>`,
            "sensing_method": int
        }
    """
    _fields_ = [
        ("u32EposureTime", AX_U32), # denominator value.
        ("f32FNumber", AX_F32),
        ("enExposureProgram", AX_VENC_EXIF_EXPOSURE_PROGRAM_E),
        ("u16ISOSpeedRatings", AX_U16),
        ("u8ExifVersion", AX_U8 * MAX_JENC_EXIF_VERSION_LEN),
        ("u8DateTimeOriginal", AX_U8 * MAX_JENC_EXIF_DATETIME_LEN),
        ("u8DateTimeDigitized", AX_U8 * MAX_JENC_EXIF_DATETIME_LEN),
        ("u8ComponentsConfiguration", AX_U8 * MAX_JENC_EXIF_COMPONENTS_CONFIG_LEN),
        ("f32CompressedBitsPerPixel", AX_F32),
        ("u16ShutterSpeedValue", AX_U16), # APEX, 2^n .
        ("u16ApertureValue", AX_U16), # 2^ (n / 2)
        ("f32BrightnessValue", AX_F32),
        ("f32ExposureBiasValue", AX_F32),
        ("u16MaxApertureValue", AX_U16), # 2^ (n / 2)
        ("u16SubjectDistance", AX_U16),  # meter unit
        ("enMeteringMode", AX_VENC_EXIF_METERING_MODE_E),
        ("u16LightSource", AX_U16),
        ("enFlash", AX_VENC_EXIF_FLASH_E),
        ("f32FocalLength", AX_F32), # mm unit
        ("u16SubsecTime", AX_U16), # [0, 999]
        ("u16SubsecTimeOriginal", AX_U16), # [0, 999]
        ("u16SubsecTimeDigitized", AX_U16), # [0, 999]
        ("u8FlashpixVersion", AX_U8 * MAX_JENC_EXIF_VERSION_LEN),
        ("enColorSpace", AX_VENC_EXIF_COLOR_SPACE_E),
        ("u32ExifImageWidth", AX_U32),
        ("u32ExifImageHeight", AX_U32),
        ("u32FocalPlaneXResolution", AX_U32),
        ("u32FocalPlaneYResolution", AX_U32),
        ("enFocalPlaneResolutionUnit", AX_VENC_EXIF_RES_UNIT_E),
        ("u16SensingMethod", AX_U16)
    ]
    field_aliases = {
        "u32EposureTime": "eposure_time",
        "f32FNumber": "f_number",
        "enExposureProgram": "exposure_program",
        "u16ISOSpeedRatings": "iso_speed_ratings",
        "u8ExifVersion": "exif_version",
        "u8DateTimeOriginal": "date_time_original",
        "u8DateTimeDigitized": "date_time_digitized",
        "u8ComponentsConfiguration": "components_configuration",
        "f32CompressedBitsPerPixel": "compressed_bits_per_pixel",
        "u16ShutterSpeedValue": "shutter_speed_value",
        "u16ApertureValue": "aperture_value",
        "f32BrightnessValue": "brightness_value",
        "f32ExposureBiasValue": "exposure_bias_value",
        "u16MaxApertureValue": "max_aperture_value",
        "u16SubjectDistance": "subject_distance",
        "enMeteringMode": "metering_mode",
        "u16LightSource": "light_source",
        "enFlash": "flash",
        "f32FocalLength": "focal_length",
        "u16SubsecTime": "subsec_time",
        "u16SubsecTimeOriginal": "subsec_time_original",
        "u16SubsecTimeDigitized": "subsec_time_digitized",
        "u8FlashpixVersion": "flash_pix_version",
        "enColorSpace": "color_space",
        "u32ExifImageWidth": "exif_image_width",
        "u32ExifImageHeight": "exif_image_height",
        "u32FocalPlaneXResolution": "focal_plane_x_resolution",
        "u32FocalPlaneYResolution": "focal_plane_y_resolution",
        "enFocalPlaneResolutionUnit": "focal_plane_resolution_unit",
        "u16SensingMethod": "sensing_method"
    }


class AX_VENC_EXIF_GPS_INFO_T(BaseStructure):
    """
    .. parsed-literal::

        dict_exif_gps_info = {
            "gps_version_id": [int],
            "gps_latitude_ref": :class:`AX_VENC_EXIF_GPS_LATITUDE_REF_E <axcl.venc.axcl_venc_exif.AX_VENC_EXIF_GPS_LATITUDE_REF_E>`,
            "gps_latitude": int,
            "gps_longitude_ref": :class:`AX_VENC_EXIF_GPS_LONGITUDE_REF_E <axcl.venc.axcl_venc_exif.AX_VENC_EXIF_GPS_LONGITUDE_REF_E>`,
            "gps_longitude": int,
            "gps_altitude_ref": :class:`AX_VENC_EXIF_GPS_ALTITUDE_REF_E <axcl.venc.axcl_venc_exif.AX_VENC_EXIF_GPS_ALTITUDE_REF_E>`,
            "gps_altitude": int,
            "gps_time_stamp": [int],
            "gps_satellites": [int],
            "gps_status": :class:`AX_VENC_EXIF_GPS_STATUS_E <axcl.venc.axcl_venc_exif.AX_VENC_EXIF_GPS_STATUS_E>`,
            "gps_measure_mode": :class:`AX_VENC_EXIF_GPS_MEASURE_MODE_E <axcl.venc.axcl_venc_exif.AX_VENC_EXIF_GPS_MEASURE_MODE_E>`,
            "gps_dop": int,
            "gps_speed_ref": :class:`AX_VENC_EXIF_GPS_SPEED_REF_E <axcl.venc.axcl_venc_exif.AX_VENC_EXIF_GPS_SPEED_REF_E>`,
            "gps_speed": int,
            "gps_track_ref": :class:`AX_VENC_EXIF_GPS_NORTH_REF_E <axcl.venc.axcl_venc_exif.AX_VENC_EXIF_GPS_NORTH_REF_E>`,
            "gps_track": int,
            "gps_img_direction_ref": :class:`AX_VENC_EXIF_GPS_NORTH_REF_E <axcl.venc.axcl_venc_exif.AX_VENC_EXIF_GPS_NORTH_REF_E>`,
            "gps_img_direction": int,
            "gps_map_datum": [int],
            "gps_dst_latitude_ref": :class:`AX_VENC_EXIF_GPS_LATITUDE_REF_E <axcl.venc.axcl_venc_exif.AX_VENC_EXIF_GPS_LATITUDE_REF_E>`,
            "gps_dst_latitude": int,
            "gps_dst_longitude_ref": :class:`AX_VENC_EXIF_GPS_LONGITUDE_REF_E <axcl.venc.axcl_venc_exif.AX_VENC_EXIF_GPS_LONGITUDE_REF_E>`,
            "gps_dst_longitude": int,
            "gps_dst_bearing_ref": :class:`AX_VENC_EXIF_GPS_NORTH_REF_E <axcl.venc.axcl_venc_exif.AX_VENC_EXIF_GPS_NORTH_REF_E>`,
            "gps_dst_bearing": int,
            "gps_dst_distance_ref": :class:`AX_VENC_EXIF_GPS_DISTANCE_REF_E <axcl.venc.axcl_venc_exif.AX_VENC_EXIF_GPS_DISTANCE_REF_E>`,
            "gps_dst_distance": int,
            "gps_processing_method": [int],
            "gps_area_information": [int],
            "gps_date_stamp": [int],
            "gps_differential": :class:`AX_VENC_EXIF_GPS_DIFFERENTIAL_E <axcl.venc.axcl_venc_exif.AX_VENC_EXIF_GPS_DIFFERENTIAL_E>`,
            "gps_h_positioning_error": int
        }
    """
    _fields_ = [
        ("u8GpsVersionID", AX_U8 * MAX_JENC_EXIF_VERSION_LEN),
        ("enGpsLatitudeRef", AX_VENC_EXIF_GPS_LATITUDE_REF_E),
        ("f32GpsLatitude", AX_F32), # [0, 90)
        ("enGpsLongitudeRef", AX_VENC_EXIF_GPS_LONGITUDE_REF_E),
        ("f32GpsLongitude", AX_F32), # [0, 180)
        ("enGpsAltitudeRef", AX_VENC_EXIF_GPS_ALTITUDE_REF_E),
        ("u32GpsAltitude", AX_U32),
        ("u32GpsTimeStamp", AX_U32 * 3),
        ("u8GpsSatellites", AX_U8 * MAX_JENC_EXIF_GPS_SATELLITES_LEN),
        ("enGpsStatus", AX_VENC_EXIF_GPS_STATUS_E),
        ("enGpsMeasureMode", AX_VENC_EXIF_GPS_MEASURE_MODE_E),
        ("f32GpsDop", AX_F32),
        ("enGpsSpeedRef", AX_VENC_EXIF_GPS_SPEED_REF_E),
        ("f32GpsSpeed", AX_F32),
        ("enGpsTrackRef", AX_VENC_EXIF_GPS_NORTH_REF_E),
        ("f32GpsTrack", AX_F32), # [0, 360)
        ("enGpsImgDirectionRef", AX_VENC_EXIF_GPS_NORTH_REF_E),
        ("f32GpsImgDirection", AX_F32), # [0, 360)
        ("u8GpsMapDatum", AX_U8 * MAX_JENC_EXIF_GPS_MAP_DATUM_LEN),
        ("enGpsDstLatitudeRef", AX_VENC_EXIF_GPS_LATITUDE_REF_E),
        ("f32GpsDstLatitude", AX_F32), # [0, 90)
        ("enGpsDstLongitudeRef", AX_VENC_EXIF_GPS_LONGITUDE_REF_E),
        ("f32GpsDstLongitude", AX_F32), # [0, 180)
        ("enGpsDstBearingRef", AX_VENC_EXIF_GPS_NORTH_REF_E),
        ("f32GpsDstBearing", AX_F32), # [0, 360)
        ("enGpsDstDistanceRef", AX_VENC_EXIF_GPS_DISTANCE_REF_E),
        ("f32GpsDstDistance", AX_F32),
        ("u8GpsProcessingMethod", AX_U8 * MAX_JENC_EXIF_GPS_PROCESSING_METHOD_LEN),
        ("u8GpsAreaInformation", AX_U8 * MAX_JENC_EXIF_GPS_AREA_INFORMATION_LEN),
        ("u8GpsDateStamp", AX_U8 * 100), # one byte for '\0'
        ("enGpsDifferential", AX_VENC_EXIF_GPS_DIFFERENTIAL_E),
        ("f32GpsHPositioningError", AX_F32)
    ]
    field_aliases = {
        "u8GpsVersionID": "gps_version_id",
        "enGpsLatitudeRef": "gps_latitude_ref",
        "f32GpsLatitude": "gps_latitude",
        "enGpsLongitudeRef": "gps_longitude_ref",
        "f32GpsLongitude": "gps_longitude",
        "enGpsAltitudeRef": "gps_altitude_ref",
        "u32GpsAltitude": "gps_altitude",
        "u32GpsTimeStamp": "gps_time_stamp",
        "u8GpsSatellites": "gps_satellites",
        "enGpsStatus": "gps_status",
        "enGpsMeasureMode": "gps_measure_mode",
        "f32GpsDop": "gps_dop",
        "enGpsSpeedRef": "gps_speed_ref",
        "f32GpsSpeed": "gps_speed",
        "enGpsTrackRef": "gps_track_ref",
        "f32GpsTrack": "gps_track",
        "enGpsImgDirectionRef": "gps_img_direction_ref",
        "f32GpsImgDirection": "gps_img_direction",
        "u8GpsMapDatum": "gps_map_datum",
        "enGpsDstLatitudeRef": "gps_dst_latitude_ref",
        "f32GpsDstLatitude": "gps_dst_latitude",
        "enGpsDstLongitudeRef": "gps_dst_longitude_ref",
        "f32GpsDstLongitude": "gps_dst_longitude",
        "enGpsDstBearingRef": "gps_dst_bearing_ref",
        "f32GpsDstBearing": "gps_dst_bearing",
        "enGpsDstDistanceRef": "gps_dst_distance_ref",
        "f32GpsDstDistance": "gps_dst_distance",
        "u8GpsProcessingMethod": "gps_processing_method",
        "u8GpsAreaInformation": "gps_area_information",
        "u8GpsDateStamp": "gps_date_stamp",
        "enGpsDifferential": "gps_differential",
        "f32GpsHPositioningError": "gps_h_positioning_error"
    }


class AX_USER_EXIF_INFO_T(BaseStructure):
    """
    .. parsed-literal::

        dict_exif_gps_info = {
            "exif_enable": bool,
            "exif_ifd0_info": :class:`AX_VENC_EXIF_IFD0_INFO_T <axcl.venc.axcl_venc_exif.AX_VENC_EXIF_IFD0_INFO_T>`,
            "exif_sub_ifd_info": :class:`AX_VENC_EXIF_SUBIFD_INFO_T <axcl.venc.axcl_venc_exif.AX_VENC_EXIF_SUBIFD_INFO_T>`,
            "exif_gps_info": :class:`AX_VENC_EXIF_GPS_INFO_T <axcl.venc.axcl_venc_exif.AX_VENC_EXIF_GPS_INFO_T>`
        }
    """
    _fields_ = [
        ("bExifEnable", AX_BOOL),
        ("stExifIFD0Info", AX_VENC_EXIF_IFD0_INFO_T),
        ("stExifSubIFDInfo", AX_VENC_EXIF_SUBIFD_INFO_T),
        ("stExifGpsInfo", AX_VENC_EXIF_GPS_INFO_T)
    ]
    field_aliases = {
        "bExifEnable": "exif_enable",
        "stExifIFD0Info": "exif_ifd0_info",
        "stExifSubIFDInfo": "exif_sub_ifd_info",
        "stExifGpsInfo": "exif_gps_info"
    }
