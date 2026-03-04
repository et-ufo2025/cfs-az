[app]
# 应用基本信息
title = CloudFlare Scanner
package.name = cfs
package.domain = org.example

# 源代码目录与版本
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
version.regex = __version__ = ['"](.*)['"]
version.filename = %(source.dir)s/main.py

# 依赖库 (关键！必须包含 aiohttp)
requirements = python3,kivy==2.2.0,aiohttp==3.8.4

# 屏幕方向
orientation = portrait
fullscreen = 0

[build]
# 可选的构建参数
# android.ndk = 25b        # 可以在 [android] 段指定

[android]
# Android 最低和目标 API
api = 33
minapi = 21
ndk = 25b

# 权限
android.permissions = INTERNET,ACCESS_NETWORK_STATE,ACCESS_WIFI_STATE

# 架构 (可选，默认是 armeabi-v7a, arm64-v8a)
android.arch = arm64-v8a

# 自动接受 SDK 许可证
android.accept_sdk_license = True

# 如果需要 OpenSSL (aiohttp 间接依赖)，但通常会自动处理
# android.add_src =

# 日志级别 (调试时可设为 2)
log_level = 2
