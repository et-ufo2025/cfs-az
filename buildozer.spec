[app]

# (str) 应用名称
title = CloudFlareScanner

# (str) 包名（不要有大写）
package.name = cfs

# (str) 包域名
package.domain = org.example

# (str) 源代码目录
source.dir = .

# (list) 包含的文件类型
source.include_exts = py,png,jpg,kv,atlas

# (str) 版本号
version = 2.2

# (list) 依赖
requirements = python3==3.10,kivy,aiohttp,openssl

# (str) 应用方向
orientation = portrait

# (bool) 是否全屏
fullscreen = 0

# (list) Android 权限
android.permissions = INTERNET,ACCESS_NETWORK_STATE

# ------------------------------
# 关键锁版本区域（解决你所有报错）
# ------------------------------

# Android API 版本（不要改）
android.api = 33

# 最低支持版本
android.minapi = 21

# 锁定 NDK 版本
android.ndk = 25c

# 锁定 Build Tools（防止 37-rc2）
android.build_tools = 33.0.2

# 指定 SDK 版本
android.sdk = 33

# 架构（支持 64 位）
android.arch = arm64-v8a

# ------------------------------

# (bool) 使用 AndroidX
android.enable_androidx = True

# (bool) 允许备份
android.allow_backup = False

# (str) 图标（如果没有就注释掉）
# icon.filename = icon.png

# (str) 启动画面（可选）
# presplash.filename = presplash.png

# 日志等级
log_level = 2

warn_on_root = 1
