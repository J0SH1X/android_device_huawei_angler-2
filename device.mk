#
# Copyright (C) 2015 The Android Open-Source Project
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

# This file includes all definitions that apply to ALL angler devices, and
# are also specific to angler devices
#
# Everything in this directory will become public

# # Camera
# PRODUCT_PACKAGES += \
#     camera.msm8994 \
#     libmmcamera_interface \
#     libmmjpeg_interface \
#     libqomx_core \
#     mm-qcamera-app


# Characteristics
PRODUCT_CHARACTERISTICS := nosdcard

# Fingerprint sensor
PRODUCT_PACKAGES += \
    android.hardware.biometrics.fingerprint@2.0-service.angler

# Filesystem
# For android_filesystem_config.h
PRODUCT_PACKAGES += \
   fs_config_files

# Fingerprint Sensor#
#PRODUCT_PACKAGES += \
    #fingerprint.angler


# GPS configuration
PRODUCT_COPY_FILES += \
    $(LOCAL_PATH)/configs/gps.conf:$(TARGET_COPY_OUT_VENDOR)/etc/gps.conf


# Keylayouts
PRODUCT_COPY_FILES += \
    $(LOCAL_PATH)/keylayout/uinput-fpc.kl:$(TARGET_COPY_OUT_VENDOR)/usr/keylayout/uinput-fpc.kl \
    $(LOCAL_PATH)/keylayout/uinput-fpc.idc:$(TARGET_COPY_OUT_VENDOR)/usr/idc/uinput-fpc.idc


# Light
 PRODUCT_PACKAGES += \
     android.hardware.light@2.0-service.angler


# NFC configurations
PRODUCT_COPY_FILES += \
    $(LOCAL_PATH)/configs/libnfc-nci.conf:$(TARGET_COPY_OUT_VENDOR)/etc/libnfc-nci.conf \
    $(LOCAL_PATH)/configs/libnfc-nxp.conf:$(TARGET_COPY_OUT_VENDOR)/etc/libnfc-nxp.conf

# Ramdisk

PRODUCT_COPY_FILES += \
    device/huawei/angler/rootdir/etc/init.angler.rc:$(TARGET_COPY_OUT_VENDOR)/etc/init/hw/init.angler.rc \
    device/huawei/angler/rootdir/etc/init.angler.nanohub.rc:$(TARGET_COPY_OUT_VENDOR)/etc/init/hw/init.angler.nanohub.rc \
    device/huawei/angler/rootdir/etc/init.angler.sensorhub.rc:$(TARGET_COPY_OUT_VENDOR)/etc/init/hw/init.angler.sensorhub.rc \
    device/huawei/angler/rootdir/etc/fstab.angler:$(TARGET_RAMDISK_OUT)/fstab.angler \
    device/huawei/angler/rootdir/etc/fstab.angler:$(TARGET_COPY_OUT_VENDOR)/etc/fstab.angler \

PRODUCT_PACKAGES += \
    fstab.ramdisk \
    fstab.angler 


# Sensor
TARGET_USES_NANOHUB_SENSORHAL := true
TARGET_USES_CHINOOK_SENSORHUB := false
NANOHUB_SENSORHAL_LID_STATE_ENABLED := true
NANOHUB_SENSORHAL_USB_MAG_BIAS_ENABLED := true
NANOHUB_SENSORHAL_SENSORLIST := $(LOCAL_PATH)/sensorhal/sensorlist.cpp
NANOHUB_SENSORHAL_DIRECT_REPORT_ENABLED := true

PRODUCT_PACKAGES += \
    sensors.angler
   # activity_recognition.angler

ifeq ($(TARGET_USES_CHINOOK_SENSORHUB),true)
PRODUCT_PACKAGES += \
    sensortool.angler \
    nano4x1.bin
else
PRODUCT_PACKAGES += \
    nanoapp_cmd
endif

# Sensor utilities
ifneq (,$(filter userdebug eng, $(TARGET_BUILD_VARIANT)))
PRODUCT_PACKAGES += \
    nanotool \
    sensortest
endif

# Shims
PRODUCT_PACKAGES += \
    libshim_sensor

# Thermal configuration
PRODUCT_COPY_FILES += \
    $(LOCAL_PATH)/configs/thermal-engine-angler.conf:$(TARGET_COPY_OUT_VENDOR)/etc/thermal-engine.conf


# WiFi cal NVRAM files
PRODUCT_COPY_FILES += \
    $(LOCAL_PATH)/wifi/bcmdhd.cal:$(TARGET_COPY_OUT_VENDOR)/etc/wifi/bcmdhd.cal \
    $(LOCAL_PATH)/wifi/bcmdhd-pme.cal:$(TARGET_COPY_OUT_VENDOR)/etc/wifi/bcmdhd-pme.cal \
    $(LOCAL_PATH)/wifi/bcmdhd-high.cal:$(TARGET_COPY_OUT_VENDOR)/etc/wifi/bcmdhd-high.cal \
    $(LOCAL_PATH)/wifi/bcmdhd-low.cal:$(TARGET_COPY_OUT_VENDOR)/etc/wifi/bcmdhd-low.cal \
    $(LOCAL_PATH)/wifi/filter_ie:$(TARGET_COPY_OUT_VENDOR)/etc/wifi/filter_ie


-include device/huawei/msm8994-common/msm8994.mk