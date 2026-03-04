[app]
# 应用基本信息
title = CloudFlare Scanner
package.name = cfs
package.domain = org.example

# 源代码目录与扩展
source.dir = .
source.include_exts = py,png,jpg,kv,atlas

# 使用静态版本号（删除 version.regex 和 version.filename）
version = 0.1

# 依赖库（aiohttp 及其必需依赖）
requirements = python3,kivy==2.2.0,aiohttp==3.8.4

# 屏幕方向
orientation = portrait
fullscreen = 0

[build]
# 可选的构建参数

[android]
# Android 最低和目标 API
api = 33
minapi = 21
ndk = 25b

# 权限
android.permissions = INTERNET,ACCESS_NETWORK_STATE,ACCESS_WIFI_STATE

# 架构 (可选，默认 armeabi-v7a, arm64-v8a)
android.arch = arm64-v8a

# 自动接受 SDK 许可证
android.accept_sdk_license = True

# 日志级别
log_level = 2
