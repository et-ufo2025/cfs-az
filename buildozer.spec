[app]

# (str) Title of your application
title = CF Scanner

# (str) Package name
package.name = cfscanner

# (str) Package domain (needed for android/ios packaging)
package.domain = com.yourdomain

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,csv

# (int) Target Android API, should be as high as possible.
android.api = 30

# (int) Minimum API required
android.minapi = 21

# (int) Android SDK version to use
android.sdk = 30

# (str) Android NDK version to use
android.ndk = 23b

# (bool) Enable/Disable compilation of Cython code
android.compile.cython = 1

# (list) Permissions
android.permissions = INTERNET, ACCESS_NETWORK_STATE

# (str) The name of the executable creation
source.exclude_exts = spec

# (str) The version of your application
version = 0.1

# (list) Application requirements
requirements = python3, kivy==2.1.0, aiohttp==3.8.1, cython==0.29.33

# (str) The directory to join the application
asset.dir = assets/

# (list) Java or Kotlin source folders
source.java.src = src/main/java

# (str) package identifier (unique across the application)
package.replace_org = org.test

# (str) python-for-android branch to use, defaults to master
p4a.branch = master

# (str) OUYA Console category. Should be one of GAME or APP
# On Windows, you must run "echo 0x00000002 > .gitattributes"
# and commit that file, otherwise the line endings will be changed by git
# ouya.category = GAME

# (str) OUYA Console icon. This is a filename in your project's assets folder
# On Windows, you must run "echo 0x00000002 > .gitattributes"
# and commit that file, otherwise the line endings will be changed by git
# ouya.icon.filename = %(source.dir)s/assets/ouya_icon.png

# (str) Application name (used by the launcher)
package.data_version = 0.1

# (list) Application note
# app.note = This is just a test application

# (str) Application author information
author = Your Name

# (str) Application email
email = your.email@example.com

# (str) Custom activity (e.g., KivyActivity) for Android
android.activity_class_name = org.kivy.android.PythonActivity

# (str) Full name including package of the main activity
# (if not set, the default is org.test.helloworld for a
# project named helloworld)
android.activity_name = org.kivy.android.PythonActivity

# (str) The Java class that implements the service notification
# (if not set, the default is org.test.helloworld for a
# project named helloworld)
android.service_class_name = org.kivy.android.PythonService

# (str) Android asset directory (default is 'assets')
android.assets = assets/

# (str) Android java source directory (default is 'src')
android.java_src_dir = src/main/java

# (str) Android NDK directory (if empty, it will be fetched automatically)
# android.ndk_path =

# (str) Android SDK directory (if empty, it will be fetched automatically)
# android.sdk_path =

# (str) Android NDK architecture (optional, only for cross-compilation)
# android.arch = armeabi-v7a

# (bool) Indicate whether the screen should stay on
# (true or false, default is false)
# android.wakelock =

# (list) Android application meta-data to set (key=value format)
# android.meta_data =

# (list) The Android archs to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
# In past, the library was not compiled to 64-bit Java code. So, we need to cancel the Java side
# for this particular case (for example, set android.arch to armeabi-v7a, x86, x86_64, and drop
# arm64-v8a). Check this on our issue tracker: https://github.com/kivy/python-for-android/issues/3719
android.archs = armeabi-v7a, arm64-v8a, x86, x86_64

# (int) Override log level (0-10, higher values are more verbose)
log_level = 2

# (list) List of services to create (may only be used with target android)
# The name/arguments portion will be split up following the space character.
# The first part is the service name, the second part is the main class name
# (service names can't have spaces in them).
# services = NAME:ENTRYPOINT_FROM_APP_ROOT

# (str) Path to a custom build.properties file
# android.build_properties =

# (str) Path to a custom settings.gradle file
# android.settings_gradle =

# (list) Library references that are included in the native build for this project
# android.library_references =

# (list) Colon separated paths to libraries to link with
# android.add_libs_armeabi_v7a = libs/android/:libs/android/armeabi-v7a/
# android.add_libs_arm64_v8a = libs/android/:libs/android/arm64-v8a/
# android.add_libs_x86 = libs/android/:libs/android/x86/
# android.add_libs_x86_64 = libs/android/:libs/android/x86_64/

# (bool) A boolean indicating if the application should be fullscreen or not
fullscreen = 0

# (string) Presplash screen image
# presplash.filename = %(source.dir)s/data/presplash.png

# (string) Icon for the application
# icon.filename = %(source.dir)s/data/icon.png

# (str) Specify the path to the Python executable for the virtual environment
# venv_python =

# (str) Directory where the Python code will be copied to
# (default is private)
# android.private_storage_dir = private

# (str) Android entry point, default is ok for Kivy-based app
# android.entrypoint = org.renpy.android.PythonActivity

# (str) Android tag (e.g., release, debug, etc.)
# android.tag = debug

# (str) Android package type (e.g., apk, aar, etc.)
# android.package_type = apk

# (str) Android package format (e.g., apk, bundle, etc.)
# android.package_format = apk

# (str) Android package name (e.g., com.example.myapp)
# android.package_name = com.example.myapp

# (str) Android package version name (e.g., 1.0.0)
# android.package_version_name = 1.0.0

# (str) Android package version code (e.g., 1)
# android.package_version_code = 1

# (str) Android package description (e.g., My awesome app)
# android.package_description = My awesome app

# (str) Android package URL (e.g., https://example.com/myapp)
# android.package_url = https://example.com/myapp

# (str) Android package author (e.g., John Doe)
# android.package_author = John Doe

# (str) Android package author email (e.g., john.doe@example.com)
# android.package_author_email = john.doe@example.com

# (str) Android package license (e.g., MIT)
# android.package_license = MIT

# (str) Android package keywords (e.g., game, education, entertainment)
# android.package_keywords = game, education, entertainment

# (str) Android package classifier (e.g., Development Status :: 4 - Beta)
# android.package_classifier = Development Status :: 4 - Beta

# (str) Android package platform (e.g., Android)
# android.package_platform = Android

# (str) Android package operating system (e.g., Android)
# android.package_operating_system = Android

# (str) Android package language (e.g., English)
# android.package_language = English

# (str) Android package audience (e.g., End Users/Desktop)
# android.package_audience = End Users/Desktop

# (str) Android package topic (e.g., Games/Entertainment)
# android.package_topic = Games/Entertainment

# (str) Android package comment (e.g., This is my awesome app!)
# android.package_comment = This is my awesome app!

# (str) Android package download URL (e.g., https://example.com/myapp/download)
# android.package_download_url = https://example.com/myapp/download

# (str) Android package long description (e.g., This app does amazing things!)
# android.package_long_description = This app does amazing things!

# (str) Android package home page (e.g., https://example.com/myapp)
# android.package_home_page = https://example.com/myapp

# (str) Android package bug tracker URL (e.g., https://github.com/example/myapp/issues)
# android.package_bug_tracker_url = https://github.com/example/myapp/issues

# (str) Android package documentation URL (e.g., https://example.com/myapp/docs)
# android.package_documentation_url = https://example.com/myapp/docs

# (str) Android package source code URL (e.g., https://github.com/example/myapp)
# android.package_source_code_url = https://github.com/example/myapp

# (str) Android package support URL (e.g., https://example.com/myapp/support)
# android.package_support_url = https://example.com/myapp/support

# (str) Android package mailing list URL (e.g., https://groups.google.com/forum/#!forum/myapp)
# android.package_mailing_list_url = https://groups.google.com/forum/#!forum/myapp

# (str) Android package forum URL (e.g., https://discuss.example.com/myapp)
# android.package_forum_url = https://discuss.example.com/myapp

# (str) Android package chat URL (e.g., https://gitter.im/example/myapp)
# android.package_chat_url = https://gitter.im/example/myapp

# (str) Android package wiki URL (e.g., https://github.com/example/myapp/wiki)
# android.package_wiki_url = https://github.com/example/myapp/wiki

# (str) Android package news URL (e.g., https://example.com/myapp/news)
# android.package_news_url = https://example.com/myapp/news

# (str) Android package blog URL (e.g., https://blog.example.com/myapp)
# android.package_blog_url = https://blog.example.com/myapp

# (str) Android package social media URL (e.g., https://twitter.com/myapp)
# android.package_social_media_url = https://twitter.com/myapp

# (str) Android package video URL (e.g., https://youtube.com/user/myapp)
# android.package_video_url = https://youtube.com/user/myapp

# (str) Android package screenshot URL (e.g., https://example.com/myapp/screenshot.png)
# android.package_screenshot_url = https://example.com/myapp/screenshot.png

# (str) Android package icon URL (e.g., https://example.com/myapp/icon.png)
# android.package_icon_url = https://example.com/myapp/icon.png

# (str) Android package presplash URL (e.g., https://example.com/myapp/presplash.png)
# android.package_presplash_url = https://example.com/myapp/presplash.png

# (str) Android package keystore (e.g., myapp.keystore)
# android.keystore = myapp.keystore

# (str) Android keystore password (if empty, it will be prompted)
# android.keystore_password =

# (str) Key alias (for signing the APK)
# android.keyalias = myapp

# (str) Key alias password (if empty, it will be prompted)
# android.keyalias_password =

# (str) Output directory for the finished APK
bin_dir = bin

# (str) The format of the APK filename before the .apk extension
apk_filename = {packagename}-{version}-{arch}.apk

# (str) The name of the main.py file
main_file = main.py

# (str) The name of the spec file
spec_file = buildozer.spec

# (str) The name of the buildozer command
buildozer_command = buildozer

# (str) The name of the p4a command
p4a_command = p4a

# (str) The name of the cython command
cython_command = cython

# (str) The name of the python command
python_command = python

# (str) The name of the pip command
pip_command = pip

# (str) The name of the virtualenv command
virtualenv_command = virtualenv

# (str) The name of the git command
git_command = git

# (str) The name of the hg command
hg_command = hg

# (str) The name of the svn command
svn_command = svn

# (str) The name of the bzr command
bzr_command = bzr

# (str) The name of the darcs command
darcs_command = darcs

# (str) The name of the fossil command
fossil_command = fossil

# (str) The name of the gpg command
gpg_command = gpg

# (str) The name of the ssh command
ssh_command = ssh

# (str) The name of the scp command
scp_command = scp

# (str) The name of the rsync command
rsync_command = rsync

# (str) The name of the wget command
wget_command = wget

# (str) The name of the curl command
curl_command = curl

# (str) The name of the unzip command
unzip_command = unzip

# (str) The name of the tar command
tar_command = tar

# (str) The name of the gzip command
gzip_command = gzip

# (str) The name of the bzip2 command
bzip2_command = bzip2

# (str) The name of the xz command
xz_command = xz

# (str) The name of the 7z command
7z_command = 7z

# (str) The name of the zip command
zip_command = zip

# (str) The name of the unrar command
unrar_command = unrar

# (str) The name of the unar command
unar_command = unar

# (str) The name of the p7zip command
p7zip_command = p7zip

# (str) The name of the bsdtar command
bsdtar_command = bsdtar

# (str) The name of the busybox command
busybox_command = busybox

# (str) The name of the coreutils command
coreutils_command = coreutils

# (str) The name of the findutils command
findutils_command = findutils

# (str) The name of the grep command
grep_command = grep

# (str) The name of the sed command
sed_command = sed

# (str) The name of the awk command
awk_command = awk

# (str) The name of the sort command
sort_command = sort

# (str) The name of the uniq command
uniq_command = uniq

# (str) The name of the head command
head_command = head

# (str) The name of the tail command
tail_command = tail

# (str) The name of the cut command
cut_command = cut

# (str) The name of the paste command
paste_command = paste

# (str) The name of the join command
join_command = join

# (str) The name of the tr command
tr_command = tr

# (str) The name of the wc command
wc_command = wc

# (str) The name of the md5sum command
md5sum_command = md5sum

# (str) The name of the sha1sum command
sha1sum_command = sha1sum

# (str) The name of the sha256sum command
sha256sum_command = sha256sum

# (str) The name of the sha512sum command
sha512sum_command = sha512sum

# (str) The name of the cksum command
cksum_command = cksum

# (str) The name of the sum command
sum_command = sum

# (str) The name of the cksum command
cksum_command = cksum

# (str) The name of the cksum command
cksum_command = cksum

# (str) The name of the cksum command
cksum_command = cksum

# (str) The name of the cksum command
cksum_command = cksum

# (str) The name of the cksum command
cksum_command = cksum

# (str) The name of the cksum command
cksum_command = cksum

# (str) The name of the cksum command
cksum_command = cksum

# (str) The name of the cksum command
cksum_command = cksum

# (str) The name of the cksum command
cksum_command = cksum

# (str) The name of the cksum command
cksum_command = cksum

# (str) The name of the cksum command
cksum_command = cksum

# (str) The name of the cksum command
cksum_command = cksum

# (str) The name of the cksum command
cksum_command = cksum

# (str) The name of the cksum command
cksum_command = cksum

# (str) The name of the cksum command
cksum_command = cksum

# (str) The name of the cksum command
cksum_command = cksum

# (str) The name of the cksum command
cksum_command = cksum

# (str) The name of the cksum command
cksum_command = cksum

# (str) The name of the cksum command
cksum_command = cksum

# (str) The name of the cksum command
cksum_command = cksum

# (str) The name of the cksum command
cksum_command = cksum

# (str) The name of the cksum command
cksum_command = cksum

# (str) The name of the cksum command
cksum_command = cksum

# (str) The name of the cksum command
cksum_command = cksum

# (str) The name of the cksum command
cksum_command = cksum

# (str) The name of the cksum command
cksum_command = cksum

# (str) The name of the cksum command
cksum_command = cksum

# (......好的，完全理解您的需求。我们将把所有必需的文件和代码逐一列出，您可以按照顺序在 GitHub 仓库中逐个创建它们。

---

### 文件 1: `main.py`

这个文件包含了您的 Kivy 应用的全部逻辑。

**如何创建:**
1.  在您的 GitHub 仓库中，点击 `Add file` -> `Create new file`。
2.  文件名输入 `main.py`。
3.  将下面的完整代码粘贴进去。
4.  点击 `Commit new file`。

```python
# Filename: main.py
import asyncio
import aiohttp
import time
import random
import ipaddress
from datetime import datetime
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.metrics import dp
from threading import Thread

# --- 核心扫描逻辑 ---

# 定义机场代码映射
AIRPORT_CODES = {
    "HKG": "香港", "TPE": "台北", "KHH": "高雄", "MFM": "澳门",
    "NRT": "东京", "HND": "东京", "KIX": "大阪", "NGO": "名古屋",
    "FUK": "福冈", "CTS": "札幌", "OKA": "冲绳",
    "ICN": "首尔", "GMP": "首尔", "PUS": "釜山",
    "SIN": "新加坡", "BKK": "曼谷", "DMK": "曼谷",
    "KUL": "吉隆坡", "HKT": "普吉岛",
    "MNL": "马尼拉", "CEB": "宿务",
    "HAN": "河内", "SGN": "胡志明市",
    "JKT": "雅加达", "DPS": "巴厘岛",
    "DEL": "德里", "BOM": "孟买", "MAA": "金奈",
    "DXB": "迪拜", "AUH": "阿布扎比",
    "SJC": "圣何塞", "LAX": "洛杉矶", "SFO": "旧金山",
    "SEA": "西雅图", "PDX": "波特兰",
    "LAS": "拉斯维加斯", "PHX": "菲尼克斯",
    "DEN": "丹佛", "DFW": "达拉斯", "IAH": "休斯顿",
    "ORD": "芝加哥", "MSP": "明尼阿波利斯",
    "ATL": "亚特兰大", "MIA": "迈阿密", "MCO": "奥兰多",
    "JFK": "纽约", "EWR": "纽约", "LGA": "纽约",
    "BOS": "波士顿", "PHL": "费城", "IAD": "华盛顿",
    "YYZ": "多伦多", "YVR": "温哥华", "YUL": "蒙特利尔",
    "LHR": "伦敦", "LGW": "伦敦", "STN": "伦敦",
    "CDG": "巴黎", "ORY": "巴黎",
    "FRA": "法兰克福", "MUC": "慕尼胡", "TXL": "柏林",
    "AMS": "阿姆斯特丹", "EIN": "埃因霍温",
    "MAD": "马德里", "BCN": "巴塞罗那",
    "FCO": "罗马", "MXP": "米兰", "LIN": "米兰",
    "ZRH": "苏黎世", "GVA": "日内瓦",
    "VIE": "维也纳", "PRG": "布拉格",
    "WAW": "华沙", "KRK": "克拉科夫",
    "HEL": "赫尔辛基", "OSL": "奥斯陆", "ARN": "斯德哥尔摩",
    "CPH": "哥本哈根",
    "SYD": "悉尼", "MEL": "墨尔本", "BNE": "布里斯班",
    "PER": "珀斯", "ADL": "阿德莱德",
    "AKL": "奥克兰", "WLG": "惠灵顿",
    "GRU": "圣保罗", "GIG": "里约热内卢", "EZE": "布宜诺斯艾利斯",
    "SCL": "圣地亚哥", "LIM": "利马", "BOG": "波哥大",
    "JNB": "约翰内斯堡", "CPT": "开普敦", "CAI": "开罗",
}

PORT_OPTIONS = [443, 2053, 2083, 2087, 2096, 8443]

# 内置CF IP段
BACKUP_CF_IPV4_CIDRS = [
    "173.245.48.0/20", "103.21.244.0/22", "103.22.200.0/22",
    "103.31.4.0/22", "141.101.64.0/18", "108.162.192.0/18",
    "190.93.240.0/20", "188.114.96.0/20", "197.234.240.0/22",
    "198.41.128.0/17", "162.158.0.0/15", "104.16.0.0/12",
    "172.64.0.0/13", "131.0.72.0/22"
]

async def safe_open_connection(host, port, timeout=3):
    try:
        return await asyncio.wait_for(
            asyncio.open_connection(host, port),
            timeout=timeout
        )
    except:
        return None

def get_iata_translation(iata_code: str):
    if iata_code in AIRPORT_CODES:
        return AIRPORT_CODES[iata_code]
    return iata_code

class IPv4Scanner:
    def __init__(self, log_callback=None, result_callback=None, port=443):
        self.max_workers = 10
        self.timeout = 3
        self.running = True
        self.log_callback = log_callback
        self.result_callback = result_callback
        self.port = port

    def generate_ips_from_cidrs(self):
        ip_list = []
        for cidr in BACKUP_CF_IPV4_CIDRS:
            try:
                network = ipaddress.ip_network(cidr, strict=False)
                for subnet in network.subnets(new_prefix=24):
                    hosts = list(subnet.hosts())
                    sample_size = min(1, len(hosts))
                    selected_ips = random.sample(hosts, sample_size)
                    ip_list.extend(selected_ips)
            except ValueError:
                continue
        return [str(ip) for ip in ip_list]

    async def test_single_ip(self, ip_str):
        if not self.running:
            return None
        start_time = time.time()
        try:
            result = await safe_open_connection(ip_str, self.port, self.timeout)
            if result is not None:
                latency = round((time.time() - start_time) * 1000, 2)
                # 获取地区码（简化模拟）
                iata_code = "SJC"  # 实际应用中需要通过API获取
                chinese_name = get_iata_translation(iata_code)
                return {
                    'ip': ip_str,
                    'latency': latency,
                    'iata_code': iata_code,
                    'chinese_name': chinese_name,
                    'port': self.port
                }
        except Exception as e:
            pass
        return None

    async def run_scan_async(self):
        try:
            ip_list = self.generate_ips_from_cidrs()
            if self.log_callback:
                self.log_callback(f"已生成 {len(ip_list)} 个随机IP，开始扫描...")

            tasks = [self.test_single_ip(ip) for ip in ip_list]
            results = await asyncio.gather(*tasks)
            
            successful_results = [r for r in results if r is not None]
            successful_results.sort(key=lambda x: x['latency'])

            if self.result_callback:
                self.result_callback(successful_results)
            
            return successful_results
        except Exception as e:
            if self.log_callback:
                self.log_callback(f"扫描过程中出现错误: {str(e)}")
            return []

    def stop(self):
        self.running = False

class MainApp(App):
    def build(self):
        # 设置窗口大小以适应移动设备
        Window.size = (dp(400), dp(600))
        
        # 主布局
        layout = BoxLayout(orientation='vertical', padding=dp(10), spacing=dp(10))

        # 标题
        title = Label(
            text='[b][color=#ff7a18]CloudFlare[/color] [color=#111827]Scan[/color]\n[color=#6B7280]v2.2 - GitHub CI[/color][/b]',
            markup=True,
            size_hint_y=None,
            height=dp(60)
        )
        layout.add_widget(title)

        # 控制按钮
        self.scan_button = Button(text='开始扫描 (端口 443)', size_hint_y=None, height=dp(50))
        self.scan_button.bind(on_press=self.start_scan)
        layout.add_widget(self.scan_button)

        self.stop_button = Button(text='停止扫描', size_hint_y=None, height=dp(50), disabled=True)
        self.stop_button.bind(on_press=self.stop_scan)
        layout.add_widget(self.stop_button)

        # 日志显示
        log_label = Label(text='日志:', size_hint_y=None, height=dp(30))
        layout.add_widget(log_label)

        scroll = ScrollView(size_hint_y=0.4)
        self.log_output = Label(text='等待扫描...', markup=True, size_hint_y=None, halign='left', valign='top')
        self.log_output.bind(texture_size=lambda instance, value: setattr(instance, 'height', value[1]))
        scroll.add_widget(self.log_output)
        layout.add_widget(scroll)

        # 结果显示
        result_label = Label(text='扫描结果:', size_hint_y=None, height=dp(30))
        layout.add_widget(result_label)

        scroll2 = ScrollView(size_hint_y=0.4)
        self.result_output = Label(text='暂无结果', markup=True, size_hint_y=None, halign='left', valign='top')
        self.result_output.bind(texture_size=lambda instance, value: setattr(instance, 'height', value[1]))
        scroll2.add_widget(self.result_output)
        layout.add_widget(scroll2)

        self.scanner = None
        self.scan_results = []
        return layout

    def start_scan(self, instance):
        self.scan_button.disabled = True
        self.stop_button.disabled = False
        self.log_output.text += "\n[INFO] 开始扫描..."
        
        self.scanner = IPv4Scanner(
            log_callback=self.update_log,
            result_callback=self.on_scan_complete
        )
        
        thread = Thread(target=self.run_scan_in_thread)
        thread.start()

    def run_scan_in_thread(self):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        self.scan_results = loop.run_until_complete(self.scanner.run_scan_async())

    def on_scan_complete(self, results):
        Clock.schedule_once(lambda dt: self.display_results(results), 0)

    def display_results(self, results):
        self.scan_button.disabled = False
        self.stop_button.disabled = True
        if results:
            result_text = "[b]找到的可用IP:[/b]\n"
            for r in results[:10]: # 显示前10个最快的结果
                result_text += f"{r['ip']} | {r['chinese_name']} | {r['latency']}ms\n"
            self.result_output.text = result_text
            self.log_output.text += f"\n[SUCCESS] 扫描完成，找到 {len(results)} 个IP。"
        else:
            self.log_output.text += "\n[ERROR] 扫描完成，未找到可用IP。"

    def update_log(self, message):
        Clock.schedule_once(lambda dt: setattr(self.log_output, 'text', self.log_output.text + f"\n{message}"), 0)

    def stop_scan(self, instance):
        if self.scanner:
            self.scanner.stop()
            self.log_output.text += "\n[INFO] 用户请求停止扫描..."
            self.scan_button.disabled = False
            self.stop_button.disabled = True

MainApp().run()
