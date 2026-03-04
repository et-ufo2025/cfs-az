[app]

# 应用的基本信息
title = CloudFlare Scanner
package.name = cloudflarescanner
package.domain = com.yourdomain

# 源代码目录
source.dir = .

# 源代码包含的文件
source.include_exts = py,png,jpg,kv,atlas,csv

# 版本信息
version = 1.0
requirements = python3, kivy==2.1.0, aiohttp==3.8.1, cython==0.29.33

# 应用图标和启动画面
android.permissions = INTERNET, ACCESS_NETWORK_STATE, ACCESS_WIFI_STATE
android.api = 30
android.minapi = 21
android.ndk = 23b
android.sdk = 30

# 编译选项
android.add_compile_options = --no-color

# 应用信息
package.datafiles = 

# 禁用某些功能以减小APK体积
android.accept_sdk_license = True

[buildozer]

# 构建目录
log_level = 2

# 临时目录
bin_dir = bin

# 项目目录
platform_dir = .buildozerandroidplatform

# SDK路径（根据你的系统调整）
android.accept_sdk_license = True
android.accept_ndk_license = True