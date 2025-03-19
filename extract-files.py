#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: 2024 The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)
from extract_utils.fixups_lib import (
    lib_fixup_remove,
    lib_fixups,
    lib_fixups_user_type,
)
from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

namespace_imports = [
    'device/huawei/angler',
    'device/huawei/msm8994-common',
    'vendor/qcom/opensource/commonsys-intf/display',
    'vendor/qcom/opensource/dataservices',
]


def lib_fixup_vendor_suffix(lib: str, partition: str, *args, **kwargs):
    return f'{lib}_{partition}' if partition == 'vendor' else None

lib_fixups: lib_fixups_user_type = {
    **lib_fixups,
    (
        'libqdutils',
        'libqservice',
        'libgps.utils'
    ): lib_fixup_remove,
}

blob_fixups: blob_fixups_user_type = {
    ('vendor/bin/ATFWD-daemon', 'vendor/lib64/libcne.so'): blob_fixup()
        .add_needed('libcutils_shim.so'),
    'vendor/lib/liboemcamera.so': blob_fixup()
        .add_needed('libshim_sensor.so'),
    'vendor/bin/pm-service': blob_fixup()
        .replace_needed('libutils.so', 'libutils-v33.so'),
    ('vendor/lib/libmmcamera_faceproc.so', 'vendor/lib/libgoog_eis_armeabi-v7a.so', 'vendor/lib/libgoog_rownr.so'): blob_fixup()
        .replace_needed('libstdc++.so', 'libstdc++_vendor.so'),
    'vendor/lib64/libmmcamera2_q3a_core.so': blob_fixup()
        .remove_needed('libmmcamera2_is.so'),
    ('vendor/lib/lib-imsvt.so', 'vendor/lib64/lib-imsvt.so'): blob_fixup()
        .remove_needed('libvcel.so'),
}  # fmt: skip

module = ExtractUtilsModule(
    'angler',
    'huawei',
    blob_fixups=blob_fixups,
    lib_fixups=lib_fixups,
    namespace_imports=namespace_imports,
)

if __name__ == '__main__':
    utils = ExtractUtils.device(module)
    utils.run()