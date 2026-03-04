[app]

# 应用名称
title = CF Scanner
# 包名
package.name = cfscan
# 域名
package.domain = org.scanner

# 包含的源文件扩展名
source.include_exts = py,png,jpg,kv,atlas

# 你的应用主入口文件
source.main = main.py

# 版本号
version = 2.2

# 核心：必须明确声明依赖！
# aiohttp 是重点，charset-normalizer 经常作为 aiohttp 的隐性依赖在安卓上报错
requirements = python3,kivy,aiohttp,charset-normalizer

# 核心：网络权限！没有这个无法测速
android.permissions = INTERNET, ACCESS_NETWORK_STATE

# 支持的架构 (默认通常是 armeabi-v7a，建议加上 arm64-v8a 适应新手机)
android.archs = arm64-v8a, armeabi-v7a

# 允许应用在后台运行（可选，针对耗时扫描任务）
android.allow_backup = True

[buildozer]
# 日志级别 (2=debug，遇到报错时方便在 GitHub Actions 查看原因)
log_level = 2
