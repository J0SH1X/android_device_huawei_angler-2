#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: 2024 The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.extract import extract_fns_user_type
from extract_utils.extract_pixel import (
    extract_pixel_factory_image,
    pixel_factory_image_regex,
)

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
        'libgps.utils',
        'libloc_core'
    ): lib_fixup_remove,
}

blob_fixups: blob_fixups_user_type = {
    'vendor/bin/ATFWD-daemon': blob_fixup()
        .add_needed('libcutils_shim.so'),
    ('vendor/lib64/libcne.so', 'vendor/lib/libcne.so'): blob_fixup()
        .add_needed('libcutils_shim.so')
        .add_needed('liblog.so')
        .clear_symbol_version('__aeabi_memcpy')
        .clear_symbol_version('__aeabi_memset')
        .clear_symbol_version('__aeabi_memmove')
        .clear_symbol_version('__gnu_Unwind_Find_exidx'),
    'vendor/lib/liboemcamera.so': blob_fixup()
        .add_needed('libshim_sensor.msm8994.so')
        .add_needed('liblog.so')
        .clear_symbol_version('__aeabi_memcpy')
        .clear_symbol_version('__aeabi_memset')
        .clear_symbol_version('__aeabi_memmove')
        .clear_symbol_version('__gnu_Unwind_Find_exidx'),
    'vendor/bin/mm-qcamera-daemon': blob_fixup()
        .add_needed('libshim_mutexdestroy.so')
        .add_needed('liblog.so')
        .clear_symbol_version('__aeabi_memcpy')
        .clear_symbol_version('__aeabi_memset')
        .clear_symbol_version('__aeabi_memmove')
        .clear_symbol_version('__gnu_Unwind_Find_exidx'),
    ('vendor/lib/libmmcamera_faceproc.so', 'vendor/lib/libgoog_eis_armeabi-v7a.so', 'vendor/lib/libgoog_rownr.so'): blob_fixup()
        .replace_needed('libstdc++.so', 'libstdc++_vendor.so'),
    'vendor/lib64/libmmcamera2_q3a_core.so': blob_fixup()
        .add_needed('liblog.so')
        .add_needed('libshim_awb.so')
        .remove_needed('libmmcamera2_is.so'),
   ('vendor/lib/libmmcamera2_stats_algorithm.so', 'vendor/lib64/libmmcamera2_stats_algorithm.so', 'vendor/lib/libmmcamera2_is.so', 'vendor/lib/libcneapiclient.so','vendor/lib/libmmcamera2_q3a_core.so', 'vendor/lib/lib-imss.so', 'vendor/lib64/lib-imss.so', 'vendor/lib/libQSEEComAPI.so','vendor/lib/libmmcamera2_frame_algorithm.so', 'vendor/lib/libmmcamera_cac2_lib.so', 'vendor/lib/libdsutils.so', 'vendor/lib/libconfigdb.so', 'vendor/lib/libqdi.so', 'vendor/lib/libnetmgr.so','system/lib/libdmengine.so','system/lib/libdmjavaplugin.so','system/lib/libfilterpack_facedetect.so','system/lib/libfrsdk.so','vendor/bin/diag_test_server','vendor/lib/egl/eglSubDriverAndroid.so','vendor/lib/egl/libEGL_adreno.so','vendor/lib/egl/libGLESv1_CM_adreno.so','vendor/lib/egl/libGLESv2_adreno.so','vendor/lib/egl/libq3dtools_adreno.so','vendor/lib/egl/libq3dtools_esx.so','vendor/lib/hw/nfc_nci.angler.so','vendor/lib/hw/tof.vl6180.so','vendor/lib/hw/vulkan.msm8994.so','vendor/lib/lib-dplmedia.so','vendor/lib/lib-imsSDP.so','vendor/lib/lib-imsdpl.so','vendor/lib/lib-imsqimf.so','vendor/lib/lib-imsrcs.so','vendor/lib/lib-imsrcscm.so','vendor/lib/lib-imss.so','vendor/lib/lib-imsvt.so','vendor/lib/lib-imsxml.so','vendor/lib/lib-rcsimssjni.so','vendor/lib/lib-rcsjni.so','vendor/lib/lib-rtpcommon.so','vendor/lib/lib-rtpcore.so','vendor/lib/lib-rtpdaemoninterface.so','vendor/lib/lib-rtpsl.so','vendor/lib/libC2D2.so','vendor/lib/libCB.so','vendor/lib/libQSEEComAPI.so','vendor/lib/libRSDriver_adreno.so','vendor/lib/libacdb-fts.so','vendor/lib/libacdbmapper.so','vendor/lib/libacdbrtac.so','vendor/lib/libactuator_lc898212xd.so','vendor/lib/libactuator_lc898212xd_camcorder.so','vendor/lib/libactuator_lc898212xd_camera.so','vendor/lib/libadiertac.so','vendor/lib/libadm.so','vendor/lib/libadpcmdec.so','vendor/lib/libadreno_utils.so','vendor/lib/libadsprpc.so','vendor/lib/libaudcal.so','vendor/lib/libaudioalsa.so','vendor/lib/libbccQTI.so','vendor/lib/libc2d30-a3xx.so','vendor/lib/libc2d30-a4xx.so','vendor/lib/libchromatix_imx179_liteon_common.so','vendor/lib/libchromatix_imx179_liteon_cpp_liveshot.so','vendor/lib/libchromatix_imx179_liteon_cpp_preview.so','vendor/lib/libchromatix_imx179_liteon_cpp_snapshot.so','vendor/lib/libchromatix_imx179_liteon_cpp_video.so','vendor/lib/libchromatix_imx179_liteon_default_video.so','vendor/lib/libchromatix_imx179_liteon_liveshot.so','vendor/lib/libchromatix_imx179_liteon_postproc.so','vendor/lib/libchromatix_imx179_liteon_preview.so','vendor/lib/libchromatix_imx179_liteon_snapshot.so','vendor/lib/libchromatix_imx179_liteon_video_binning.so','vendor/lib/libchromatix_imx179_sunny_common.so','vendor/lib/libchromatix_imx179_sunny_cpp_liveshot.so','vendor/lib/libchromatix_imx179_sunny_cpp_preview.so','vendor/lib/libchromatix_imx179_sunny_cpp_snapshot.so','vendor/lib/libchromatix_imx179_sunny_cpp_video.so','vendor/lib/libchromatix_imx179_sunny_default_video.so','vendor/lib/libchromatix_imx179_sunny_liveshot.so','vendor/lib/libchromatix_imx179_sunny_postproc.so','vendor/lib/libchromatix_imx179_sunny_preview.so','vendor/lib/libchromatix_imx179_sunny_snapshot.so','vendor/lib/libchromatix_imx179_sunny_video_binning.so','vendor/lib/libchromatix_imx377_common.so','vendor/lib/libchromatix_imx377_cpp_hfr_120.so','vendor/lib/libchromatix_imx377_cpp_hfr_240.so','vendor/lib/libchromatix_imx377_cpp_hfr_60.so','vendor/lib/libchromatix_imx377_cpp_hfr_90.so','vendor/lib/libchromatix_imx377_cpp_liveshot.so','vendor/lib/libchromatix_imx377_cpp_preview.so','vendor/lib/libchromatix_imx377_cpp_snapshot.so','vendor/lib/libchromatix_imx377_cpp_uhd_video.so','vendor/lib/libchromatix_imx377_cpp_video.so','vendor/lib/libchromatix_imx377_default_video.so','vendor/lib/libchromatix_imx377_hfr_120.so','vendor/lib/libchromatix_imx377_hfr_240.so','vendor/lib/libchromatix_imx377_hfr_60.so','vendor/lib/libchromatix_imx377_hfr_90.so','vendor/lib/libchromatix_imx377_liveshot.so','vendor/lib/libchromatix_imx377_postproc.so','vendor/lib/libchromatix_imx377_preview.so','vendor/lib/libchromatix_imx377_snapshot.so','vendor/lib/libconfigdb.so','vendor/lib/libdiag.so','vendor/lib/libdrmfs.so','vendor/lib/libdrmtime.so','vendor/lib/libdsi_netctrl.so','vendor/lib/libdsutils.so','vendor/lib/libflash_pmic.so','vendor/lib/libgsl.so','vendor/lib/libidl.so','vendor/lib/libimscamera_jni.so','vendor/lib/libimsmedia_jni.so','vendor/lib/libjpegdhw.so','vendor/lib/libjpegdmahw.so','vendor/lib/libjpegehw.so','vendor/lib/libkmcrypto.so','vendor/lib/liblistensoundmodel2.so','vendor/lib/libllvm-glnext.so','vendor/lib/libllvm-qcom.so','vendor/lib/libllvm-qgl.so','vendor/lib/libloc_api_v02.so','vendor/lib/libloc_ds_api.so','vendor/lib/libmdmdetect.so','vendor/lib/libmdsprpc.so','vendor/lib/libmm-abl-oem.so','vendor/lib/libmm-abl.so','vendor/lib/libmm-als.so','vendor/lib/libmm-disp-apis.so','vendor/lib/libmm-qdcm.so','vendor/lib/libmmcamera2_c2d_module.so','vendor/lib/libmmcamera2_cpp_module.so','vendor/lib/libmmcamera2_iface_modules.so','vendor/lib/libmmcamera2_imglib_modules.so','vendor/lib/libmmcamera2_isp_modules.so','vendor/lib/libmmcamera2_pp_buf_mgr.so','vendor/lib/libmmcamera2_pproc_modules.so','vendor/lib/libmmcamera2_sensor_debug.so','vendor/lib/libmmcamera2_sensor_modules.so','vendor/lib/libmmcamera2_stats_modules.so','vendor/lib/libmmcamera2_vpe_module.so','vendor/lib/libmmcamera2_wnr_module.so','vendor/lib/libmmcamera_dw9761b_eeprom.so','vendor/lib/libmmcamera_eeprom_util.so','vendor/lib/libmmcamera_eztune_module.so','vendor/lib/libmmcamera_imglib.so','vendor/lib/libmmcamera_imx179_liteon.so','vendor/lib/libmmcamera_imx179_sunny.so','vendor/lib/libmmcamera_imx377.so','vendor/lib/libmmcamera_isp_abcc44.so','vendor/lib/libmmcamera_isp_abf44.so','vendor/lib/libmmcamera_isp_bcc44.so','vendor/lib/libmmcamera_isp_be_stats44.so','vendor/lib/libmmcamera_isp_bf_scale_stats46.so','vendor/lib/libmmcamera_isp_bf_stats44.so','vendor/lib/libmmcamera_isp_bg_stats46.so','vendor/lib/libmmcamera_isp_bhist_stats44.so','vendor/lib/libmmcamera_isp_bpc44.so','vendor/lib/libmmcamera_isp_chroma_enhan40.so','vendor/lib/libmmcamera_isp_chroma_suppress40.so','vendor/lib/libmmcamera_isp_clamp_encoder40.so','vendor/lib/libmmcamera_isp_clamp_video40.so','vendor/lib/libmmcamera_isp_clamp_viewfinder40.so','vendor/lib/libmmcamera_isp_clf46.so','vendor/lib/libmmcamera_isp_color_correct46.so','vendor/lib/libmmcamera_isp_color_xform_encoder46.so','vendor/lib/libmmcamera_isp_color_xform_video46.so','vendor/lib/libmmcamera_isp_color_xform_viewfinder46.so','vendor/lib/libmmcamera_isp_cs_stats46.so','vendor/lib/libmmcamera_isp_demosaic44.so','vendor/lib/libmmcamera_isp_demux40.so','vendor/lib/libmmcamera_isp_fovcrop_encoder46.so','vendor/lib/libmmcamera_isp_fovcrop_video46.so','vendor/lib/libmmcamera_isp_fovcrop_viewfinder46.so','vendor/lib/libmmcamera_isp_gamma44.so','vendor/lib/libmmcamera_isp_gic46.so','vendor/lib/libmmcamera_isp_gtm46.so','vendor/lib/libmmcamera_isp_hdr46.so','vendor/lib/libmmcamera_isp_hdr_be_stats46.so','vendor/lib/libmmcamera_isp_ihist_stats46.so','vendor/lib/libmmcamera_isp_linearization40.so','vendor/lib/libmmcamera_isp_ltm44.so','vendor/lib/libmmcamera_isp_mce40.so','vendor/lib/libmmcamera_isp_mesh_rolloff44.so','vendor/lib/libmmcamera_isp_pedestal_correct46.so','vendor/lib/libmmcamera_isp_rs_stats46.so','vendor/lib/libmmcamera_isp_scaler_encoder46.so','vendor/lib/libmmcamera_isp_scaler_video46.so','vendor/lib/libmmcamera_isp_scaler_viewfinder46.so','vendor/lib/libmmcamera_isp_sce40.so','vendor/lib/libmmcamera_isp_sub_module.so','vendor/lib/libmmcamera_isp_wb46.so','vendor/lib/libmmcamera_m24c64s_eeprom.so','vendor/lib/libmmcamera_pdaf.so','vendor/lib/libmmcamera_pdafcamif.so','vendor/lib/libmmcamera_ppbase_module.so','vendor/lib/libmmcamera_sony_imx179_eeprom.so','vendor/lib/libmmcamera_tintless_algo.so','vendor/lib/libmmcamera_tintless_bg_pca_algo.so','vendor/lib/libmmcamera_vpu_module.so','vendor/lib/libmmipl.so','vendor/lib/libmmjpeg.so','vendor/lib/libmmqjpeg_codec.so','vendor/lib/libmmqjpegdma.so','vendor/lib/libnetmgr.so','vendor/lib/liboemcrypto.so','vendor/lib/libqcci_legacy.so','vendor/lib/libqdi.so','vendor/lib/libqmi.so','vendor/lib/libperipheral_client.so','vendor/lib/libqmi_cci.so','vendor/lib/libqmi_client_helper.so','vendor/lib/libqmi_client_qmux.so','vendor/lib/libqmi_csi.so','vendor/lib/libqmi_encdec.so','vendor/lib/libqmiservices.so','vendor/lib/libqomx_jpegdec.so','vendor/lib/libqomx_jpegenc.so','vendor/lib/libqomx_jpegenc_pipe.so','vendor/lib/libqti-perfd-client.so','vendor/lib/libril-qcril-hook-oem.so','vendor/lib/librpmb.so','vendor/lib/librs_adreno.so','vendor/lib/libscale.so','vendor/lib/libsmemlog.so','vendor/lib/libssd.so','vendor/lib/libsystem_health_mon.so','vendor/lib/libthermalclient.so','vendor/lib/libtime_genoff.so','vendor/lib/libtzdrmgenprov.so','vendor/lib/libvoice-svc.so','vendor/lib/libwms.so','vendor/lib/libxml.so','vendor/lib/mediadrm/libwvdrmengine.so','vendor/lib/soundfx/libfmas.so'): blob_fixup()
        .add_needed('liblog.so')
        .clear_symbol_version('__aeabi_memcpy')
        .clear_symbol_version('__aeabi_memset')
        .clear_symbol_version('__aeabi_memmove')
        .clear_symbol_version('__gnu_Unwind_Find_exidx'),
    ('vendor/lib/libvoice-svc.so', 'vendor/lib64/libvoice-svc.so'): blob_fixup()
        .add_needed('libprocessgroup.so'),
    ('vendor/bin/imsqmidaemon', 'vendor/bin/imsdatadaemon', 'vendor/lib64/lib-imsSDP.so', 'vendor/lib64/lib-rtpdaemoninterface.so', 'vendor/bin/cnd', 'vendor/lib64/lib-imsdpl.so', 'vendor/lib/liblowi_client.so', 'vendor/lib64/liblowi_wifihal.so', 'vendor/lib64/liblowi_client.so', 'vendor/lib64/libQSEEComAPI.so', 'vendor/lib64/libcneapiclient.so', 'vendor/lib/libquipc_os_api.so', 'vendor/lib64/libquipc_os_api.so', 'vendor/bin/port-bridge'): blob_fixup()
        .add_needed('liblog.so'),
    ('vendor/lib/libimsmedia_jni.so', 'vendor/lib64/libimsmedia_jni.so'): blob_fixup()
        .add_needed('libgui_shim.so'),
    'vendor/lib64/libril-qc-qmi-1.so': blob_fixup()
        .add_needed('libaudioclient_shim.msm8994.so'),
    ('vendor/lib/hw/sound_trigger.primary.msm8994.so', 'vendor/lib64/hw/sound_trigger.primary.msm8994.so'): blob_fixup()
        .add_needed('liblog.so')
        .clear_symbol_version('__aeabi_memcpy')
        .clear_symbol_version('__aeabi_memset')
        .clear_symbol_version('__aeabi_memmove')
        .clear_symbol_version('__gnu_Unwind_Find_exidx')
        .binary_regex_replace(b'system/etc/sound_trigger_mixer_paths.xml', b'vendor/etc/sound_trigger_mixer_paths.xml')
        .binary_regex_replace(b'/system/etc/sound_trigger_platform_info.xml', b'/vendor/etc/sound_trigger_platform_info.xml'),
    ('vendor/lib/libacdbloader.so', 'vendor/lib64/libacdbloader.so'): blob_fixup()
        .add_needed('liblog.so')
        .clear_symbol_version('__aeabi_memcpy')
        .clear_symbol_version('__aeabi_memset')
        .clear_symbol_version('__aeabi_memmove')
        .clear_symbol_version('__gnu_Unwind_Find_exidx')
        .binary_regex_replace(b'/system/etc/aanc_tuning_mixer.txt', b'/vendor/etc/aanc_tuning_mixer.txt'),
    'vendor/bin/thermal-engine': blob_fixup()
        .binary_regex_replace(b'/system/etc/thermal-engine.conf', b'/vendor/etc/thermal-engine.conf'),
}  # fmt: skip

extract_fns: extract_fns_user_type = {
    pixel_factory_image_regex: extract_pixel_factory_image,
}

module = ExtractUtilsModule(
    'angler',
    'huawei',
    blob_fixups=blob_fixups,
    lib_fixups=lib_fixups,
    namespace_imports=namespace_imports,
    extract_fns=extract_fns,
)

if __name__ == '__main__':
    utils = ExtractUtils.device(module)
    utils.run()