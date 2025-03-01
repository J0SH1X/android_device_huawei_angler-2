#!/bin/bash
#
# Copyright (C) 2016 The CyanogenMod Project
# Copyright (C) 2017-2020 The LineageOS Project
#
# SPDX-License-Identifier: Apache-2.0
#

set -e

DEVICE=angler-treble
VENDOR=huawei

# Load extractutils and do some sanity checks
MY_DIR="${BASH_SOURCE%/*}"
if [[ ! -d "${MY_DIR}" ]]; then MY_DIR="${PWD}"; fi

ANDROID_ROOT="${MY_DIR}/../../.."

HELPER="${ANDROID_ROOT}/tools/extract-utils/extract_utils.sh"
if [ ! -f "${HELPER}" ]; then
    echo "Unable to find helper script at ${HELPER}"
    exit 1
fi
source "${HELPER}"

# Default to sanitizing the vendor folder before extraction
CLEAN_VENDOR=true

KANG=
SECTION=

while [ "${#}" -gt 0 ]; do
    case "${1}" in
        -n | --no-cleanup )
                CLEAN_VENDOR=false
                ;;
        -k | --kang )
                KANG="--kang"
                ;;
        -s | --section )
                SECTION="${2}"; shift
                CLEAN_VENDOR=false
                ;;
        * )
                SRC="${1}"
                ;;
    esac
    shift
done

if [ -z "${SRC}" ]; then
    SRC="adb"
 fi
#     /vendor/bin/ATFWD-daemon|libcutils_shim.so \
#     /vendor/lib64/libcne.so|libcutils_shim.so



# sed -i 's!/system/etc/thermal-engine.conf!/vendor/etc/thermal-engine.conf!' bin/thermal-engine 
# sed -i 's!system/etc/sound_trigger_mixer_paths.xml!vendor/etc/sound_trigger_mixer_paths.xml!' lib/hw/sound_trigger.primary.msm8994.so 
# sed -i 's!system/etc/sound_trigger_mixer_paths.xml!vendor/etc/sound_trigger_mixer_paths.xml!' lib64/hw/sound_trigger.primary.msm8994.so
# sed -i 's!/system/etc/sound_trigger_platform_info.xml!/vendor/etc/sound_trigger_platform_info.xml!' lib/hw/sound_trigger.primary.msm8994.so 
# sed -i 's!/system/etc/sound_trigger_platform_info.xml!/vendor/etc/sound_trigger_platform_info.xml!' lib64/hw/sound_trigger.primary.msm8994.so

#sed -i "s/SSLv3_client_method/SSLv23_method\x00\x00\x00\x00\x00\x00/" "${2}"

function blob_fixup() {
    case "${1}" in
    vendor/bin/ATFWD-daemon)
        patchelf --add-needed "libcutils_shim.so" "${2}"
    ;;
    vendor/bin/cne)
        patchelf --add-needed "libcutils_shim.so" "${2}"
    ;;
    vendor/lib/liboemcamera.so )
        patchelf --add-needed "libshim_sensor.so" "${2}"
        patchelf --replace-needed "libgui.so" "libgui_vendor.so" "${2}"
        patchelf --replace-needed "libsensor.so" "libsensor_vendor.so" "${2}"
        patchelf --replace-needed "libandroid.so" "libsensorndkbridge.so" "${2}"
    ;;
    vendor/lib/libmmcamera2_stats_modules.so )
        patchelf --replace-needed "libandroid.so" "libsensorndkbridge.so" "${2}"
        patchelf --replace-needed "libgui.so" "libgui_vendor.so" "${2}"
        patchelf --replace-needed "libsensor.so" "libsensor_vendor.so" "${2}"
    ;;
    vendor/bin/thermal-engine )
        sed -i 's!/system/etc/thermal-engine.conf!/vendor/etc/thermal-engine.conf!' "${2}"
    ;;
    vendor/lib/hw/sound_trigger.primary.msm8994.so )
        sed -i 's!system/etc/sound_trigger_mixer_paths.xml!vendor/etc/sound_trigger_mixer_paths.xml!' "${2}"
        sed -i 's!/system/etc/sound_trigger_platform_info.xml!/vendor/etc/sound_trigger_platform_info.xml!' "${2}"
    ;;
    vendor/lib/hw/sound_trigger.primary.msm8994.so )
        sed -i 's!system/etc/sound_trigger_mixer_paths.xml!vendor/etc/sound_trigger_mixer_paths.xml!' "${2}"
        sed -i 's!/system/etc/sound_trigger_platform_info.xml!/vendor/etc/sound_trigger_platform_info.xml!' "${2}"
    ;;
    esac
}

# Initialize the helper
setup_vendor "${DEVICE}" "${VENDOR}" "${ANDROID_ROOT}" false "${CLEAN_VENDOR}"

extract "${MY_DIR}/proprietary-files.txt" "${SRC}" "${KANG}" --section "${SECTION}"

"$MY_DIR"/setup-makefiles.sh
