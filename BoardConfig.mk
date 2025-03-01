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

# Bluetooth
BOARD_HAVE_BLUETOOTH_BCM := true
BOARD_BLUETOOTH_BDROID_BUILDCFG_INCLUDE_DIR := device/huawei/angler/bluetooth
BOARD_CUSTOM_BT_CONFIG := device/huawei/angler/bluetooth/vnd_angler.txt


# Board
TARGET_BOOTLOADER_BOARD_NAME := angler


# Inline kernel building
TARGET_KERNEL_SOURCE := kernel/huawei/angler
TARGET_KERNEL_CONFIG := angler_defconfig
BOARD_KERNEL_CMDLINE := androidboot.hardware=angler
BOARD_MKBOOTIMG_ARGS := --ramdisk_offset $(BOARD_RAMDISK_OFFSET) --tags_offset $(BOARD_KERNEL_TAGS_OFFSET)


#Images
BOARD_BOOTIMAGE_PARTITION_SIZE := 33554432
BOARD_RECOVERYIMAGE_PARTITION_SIZE := 33554432
BOARD_SYSTEMIMAGE_PARTITION_SIZE := 3221225472 
BOARD_USERDATAIMAGE_PARTITION_SIZE := 26503790080
BOARD_CACHEIMAGE_PARTITION_SIZE := 104857600
BOARD_VENDORIMAGE_PARTITION_SIZE := 975872000
# BOARD_SUPER_PARTITION_SIZE := 3221225472
# BOARD_SUPER_PARTITION_SYSTEM_DEVICE_SIZE := 3221225472
# BOARD_QCOM_DYNAMIC_PARTITIONS_SIZE := 3217031168

#NFC
NXP_CHIP_TYPE := 2

# Recovery
TARGET_RECOVERY_FSTAB = device/huawei/angler/rootdir/etc/fstab.angler

# Testing related defines
BOARD_PERFSETUP_SCRIPT := platform_testing/scripts/perf-setup/angler-setup.sh


-include vendor/huawei/angler/BoardConfigVendor.mk
-include device/huawei/msm8994-common/BoardConfigCommon.mk
