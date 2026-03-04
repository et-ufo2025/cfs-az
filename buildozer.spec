# Filename: buildozer.spec
[app]

# 应用的基本信息
title = CF Scanner
package.name = cfscanner
package.domain = com.yourdomain

# 源代码目录
source.dir = .

# 源代码包含的文件
source.include_exts = py,png,jpg,kv,atlas,csv

# 版本信息
version = 0.1
requirements = python3, kivy==2.1.0, aiohttp==3.8.1, cython==0.29.33

# 应用图标和启动画面
android.permissions = INTERNET, ACCESS_NETWORK_STATE
android.api = 30
android.minapi = 21
android.ndk = 23b
android.sdk = 30

[buildozer]

# 构建日志级别
log_level = 2
