from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.uix.scrollview import ScrollView
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.utils import platform
from kivy.lang import Builder
import asyncio
import aiohttp
import socket
import ssl
import time
import csv
import os
import random
import ipaddress
from datetime import datetime
from threading import Thread
import json

# 设置窗口大小以适应移动设备
Window.size = (dp(400), dp(600))

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
    "FRA": "法兰克福", "MUC": "慕尼黑", "TXL": "柏林",
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

PORT_OPTIONS = ["443", "2053", "2083", "2087", "2096", "8443"]

# 内置CF IP段
BACKUP_CF_IPV4_CIDRS = [
    "173.245.48.0/20",
    "103.21.244.0/22",
    "103.22.200.0/22",
    "103.31.4.0/22",
    "141.101.64.0/18",
    "108.162.192.0/18",
    "190.93.240.0/20",
    "188.114.96.0/20",
    "197.234.240.0/22",
    "198.41.128.0/17",
    "162.158.0.0/15",
    "104.16.0.0/12",
    "172.64.0.0/13",
    "131.0.72.0/22"
]

BACKUP_CF_IPV6_CIDRS = [
    "2400:cb00::/32",
    "2606:4700::/32",
    "2803:f800::/32",
    "2405:b500::/32",
    "2405:8100::/32",
    "2a06:98c0::/29",
    "2c0f:f248::/32"
]

async def safe_open_connection(host, port, timeout=3):
    try:
        return await asyncio.wait_for(
            asyncio.open_connection(host, port),
            timeout=timeout
        )
    except:
        return None

async def get_iata_code_async(session: aiohttp.ClientSession, ip: str, timeout: int = 3):
    test_host = "speed.cloudflare.com"
    
    if ':' in ip:
        urls = [
            f"https://[{ip}]/cdn-cgi/trace",
            f"http://[{ip}]/cdn-cgi/trace",
        ]
    else:
        urls = [
            f"https://{ip}/cdn-cgi/trace",
            f"http://{ip}/cdn-cgi/trace",
        ]
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; Mobile) AppleWebKit/537.36",
        "Host": test_host
    }
    
    ssl_ctx = ssl.create_default_context()
    ssl_ctx.check_hostname = False
    ssl_ctx.verify_mode = ssl.CERT_NONE
    
    for url in urls:
        try:
            use_ssl = url.startswith('https://')
            ssl_context = ssl_ctx if use_ssl else None
            
            async with session.get(
                url,
                headers=headers,
                ssl=ssl_context,
                timeout=aiohttp.ClientTimeout(total=timeout),
                allow_redirects=False
            ) as response:
                if response.status == 200:
                    text = await response.text()
                    
                    for line in text.strip().split('\n'):
                        if line.startswith('colo='):
                            colo_value = line.split('=', 1)[1].strip()
                            if colo_value and colo_value.upper() != 'UNKNOWN':
                                return colo_value.upper()
                    
                    if 'CF-RAY' in response.headers:
                        cf_ray = response.headers['CF-RAY']
                        if '-' in cf_ray:
                            parts = cf_ray.split('-')
                            for part in parts[-2:]:
                                if len(part) == 3 and part.isalpha():
                                    return part.upper()
                
        except:
            continue
    
    return None

def get_iata_translation(iata_code: str):
    if iata_code in AIRPORT_CODES:
        return AIRPORT_CODES[iata_code]
    return iata_code

class IPv4Scanner:
    def __init__(self, log_callback=None, progress_callback=None, result_callback=None, port=443, ipv4_cidrs=None):
        self.max_workers = 20  # 减少并发数以适应移动设备
        self.timeout = 3
        self.user_agent = "Mozilla/5.0 (Linux; Android 10; Mobile) AppleWebKit/537.36"
        self.running = True
        self.log_callback = log_callback
        self.progress_callback = progress_callback
        self.result_callback = result_callback
        self.port = port
        self.ipv4_cidrs = ipv4_cidrs or BACKUP_CF_IPV4_CIDRS
        
    def generate_ips_from_cidrs(self):
        ip_list = []
        for cidr in self.ipv4_cidrs:
            try:
                network = ipaddress.ip_network(cidr, strict=False)
                
                for subnet in network.subnets(new_prefix=24):
                    if subnet.num_addresses > 2:
                        hosts = list(subnet.hosts())
                        if hosts:
                            sample_size = min(1, len(hosts))
                            selected_ips = random.sample(hosts, sample_size)
                            for ip in selected_ips:
                                ip_list.append(str(ip))
                            
            except ValueError as e:
                if self.log_callback:
                    self.log_callback(f"处理CIDR {cidr} 时出错: {e}")
                continue
        
        return ip_list
    
    async def test_ip_latency(self, session: aiohttp.ClientSession, ip: str):
        if not self.running:
            return None
            
        start_time = time.monotonic()
        try:
            result = await safe_open_connection(ip, self.port, self.timeout)
            if result is None:
                return None
                
            reader, writer = result
            latency = (time.monotonic() - start_time) * 500
            writer.close()
            await writer.wait_closed()
            return round(latency, 2)
        except Exception as e:
            return None
    
    async def test_single_ip(self, session: aiohttp.ClientSession, ip: str):
        if not self.running:
            return None
        
        latency = await self.test_ip_latency(session, ip)
        
        if latency is not None and latency < 350:
            iata_code = None
            if self.running:
                try:
                    iata_code = await get_iata_code_async(session, ip, self.timeout)
                except Exception as e:
                    if self.log_callback:
                        self.log_callback(f"获取地区码失败 {ip}: {str(e)}")
                    iata_code = None
                    
            return {
                'ip': ip,
                'latency': latency,
                'iata_code': iata_code,
                'chinese_name': get_iata_translation(iata_code) if iata_code else "未知地区",
                'success': True,
                'ip_version': 4,
                'scan_time': datetime.now().strftime("%H:%M:%S"),
                'port': self.port
            }
        else:
            return None
    
    async def batch_test_ips(self, ip_list):
        semaphore = asyncio.Semaphore(self.max_workers)
        
        async def test_with_semaphore(session: aiohttp.ClientSession, ip: str):
            async with semaphore:
                return await self.test_single_ip(session, ip)
        
        connector = aiohttp.TCPConnector(
            limit=self.max_workers,
            force_close=True,
            enable_cleanup_closed=True,
            limit_per_host=0,
            ttl_dns_cache=300,
            use_dns_cache=True
        )
        
        successful_results = []
        start_time = time.time()
        
        async with aiohttp.ClientSession(connector=connector) as session:
            tasks = []
            for ip in ip_list:
                if not self.running:
                    break
                task = asyncio.create_task(test_with_semaphore(session, ip))
                tasks.append(task)
            
            completed = 0
            total = len(tasks)
            
            for future in asyncio.as_completed(tasks):
                if not self.running:
                    for task in tasks:
                        if not task.done():
                            task.cancel()
                    break
                
                try:
                    result = await future
                    completed += 1
                    
                    if result:
                        successful_results.append(result)
                    
                    if self.progress_callback:
                        self.progress_callback(completed, total, len(successful_results))
                except:
                    completed += 1
        
        return successful_results
    
    async def run_scan_async(self):
        try:
            if self.log_callback:
                self.log_callback(f"正在从 {len(self.ipv4_cidrs)} 个IPv4 IP段生成随机IP... (端口: {self.port})")
            ip_list = self.generate_ips_from_cidrs()
            
            if not ip_list:
                if self.log_callback:
                    self.log_callback("错误: 未能生成IPv4 IP列表")
                return None
            
            if self.log_callback:
                self.log_callback(f"已生成 {len(ip_list)} 个随机IPv4 IP")
                self.log_callback(f"开始测试 {len(ip_list)} 个IPv4 IP的延迟和地区码...")
            
            results = await self.batch_test_ips(ip_list)
            
            if not self.running:
                if self.log_callback:
                    self.log_callback("IPv4扫描被用户中止")
                return None
            
            return results
            
        except Exception as e:
            if self.log_callback:
                self.log_callback(f"IPv4扫描过程中出现错误: {str(e)}")
            return None
    
    def stop(self):
        self.running = False

class SpeedTestWorker:
    def __init__(self, results, region_code=None, current_port=443):
        self.results = results
        self.region_code = region_code.upper() if region_code else None
        self.download_time_limit = 3
        self.test_host = "speed.cloudflare.com"
        self.running = True
        self.current_port = current_port
        self.log_callback = None
        
    def set_log_callback(self, callback):
        self.log_callback = callback
    
    async def download_speed(self, ip: str, port: int):
        try:
            ctx = ssl.create_default_context()
            ctx.check_hostname = False
            ctx.verify_mode = ssl.CERT_NONE

            req = (
                "GET /__down?bytes=5000000 HTTP/1.1\r\n"  # 减少下载量以适应移动网络
                f"Host: {self.test_host}\r\n"
                "User-Agent: Mozilla/5.0 (Linux; Android 10; Mobile)\r\n"
                "Accept: */*\r\n"
                "Connection: close\r\n\r\n"
            ).encode()

            if ':' in ip:
                addrinfo = socket.getaddrinfo(ip, port, socket.AF_INET6, socket.SOCK_STREAM)
                family, socktype, proto, canonname, sockaddr = addrinfo[0]
                sock = socket.socket(family, socktype, proto)
                sock.settimeout(3)
                sock.connect(sockaddr)
            else:
                sock = socket.create_connection((ip, port), timeout=3)
                
            ss = ctx.wrap_socket(sock, server_hostname=self.test_host)
            ss.sendall(req)

            start = time.time()
            data = b""
            header_done = False
            body = 0

            while time.time() - start < self.download_time_limit:
                try:
                    buf = ss.recv(8192)
                    if not buf:
                        break
                    if not header_done:
                        data += buf
                        if b"\r\n\r\n" in data:
                            header_done = True
                            body += len(data.split(b"\r\n\r\n", 1)[1])
                    else:
                        body += len(buf)
                except:
                    break

            ss.close()
            dur = time.time() - start
            return round((body / 1024 / 1024) / max(dur, 0.1), 2)

        except Exception as e:
            if self.log_callback:
                self.log_callback(f"测速失败 {ip}: {str(e)}")
            return 0.0
    
    async def run_async(self):
        try:
            if not self.results:
                if self.log_callback:
                    self.log_callback("错误：没有可用的IP进行测速")
                return []
            
            if self.region_code:
                filtered_results = [r for r in self.results if r.get('iata_code') and r['iata_code'].upper() == self.region_code]
                if self.log_callback:
                    self.log_callback(f"开始地区测速：{self.region_code} ({get_iata_translation(self.region_code)}) (端口: {self.current_port})")
                    self.log_callback(f"找到 {len(filtered_results)} 个 {self.region_code} 地区的IP")
            else:
                filtered_results = self.results
                if self.log_callback:
                    self.log_callback(f"开始完全测速 (端口: {self.current_port})")
            
            if not filtered_results:
                if self.log_callback:
                    self.log_callback(f"没有找到可用的IP进行测速")
                return []
            
            filtered_results.sort(key=lambda x: x.get('latency', float('inf')))
            target_ips = filtered_results[:min(3, len(filtered_results))]  # 减少测速数量以适应移动设备
            
            test_type = "地区测速" if self.region_code else "完全测速"
            if self.log_callback:
                self.log_callback(f"{test_type}：将对 {len(target_ips)} 个IP进行测速")
            
            speed_results = []
            
            for i, ip_info in enumerate(target_ips):
                if not self.running:
                    break
                
                ip = ip_info['ip']
                latency = ip_info.get('latency', 0)
                
                if self.log_callback:
                    self.log_callback(f"[{i+1}/{len(target_ips)}] 正在测速 {ip} (延迟: {latency}ms) (端口: {self.current_port})")
                
                download_speed = await self.download_speed(ip, self.current_port)
                
                speed_result = {
                    'ip': ip,
                    'latency': latency,
                    'download_speed': download_speed,
                    'iata_code': ip_info.get('iata_code', 'UNKNOWN'),
                    'chinese_name': ip_info.get('chinese_name', '未知地区'),
                    'test_type': test_type,
                    'port': self.current_port  
                }
                
                speed_results.append(speed_result)
                
                if self.log_callback:
                    self.log_callback(f"  测速结果: {download_speed} MB/s, 地区: {speed_result['chinese_name']}")
            
            speed_results.sort(key=lambda x: x['download_speed'], reverse=True)
            
            if speed_results:
                if self.log_callback:
                    self.log_callback(f"测速完成！成功测速 {len(speed_results)}/{len(target_ips)} 个IP")
            else:
                if self.log_callback:
                    self.log_callback(f"所有IP测速失败")
            
            return speed_results
            
        except Exception as e:
            if self.log_callback:
                self.log_callback(f"测速过程中出现错误: {str(e)}")
            return []
    
    def stop(self):
        self.running = False

class CloudFlareScannerApp(App):
    def build(self):
        # 主布局
        root = BoxLayout(orientation='vertical', padding=dp(10), spacing=dp(10))
        
        # 标题
        title = Label(
            text='[b][color=#ff7a18]CloudFlare[/color] [color=#111827]Scan[/color]\n[color=#6B7280]v2.2 - 移动版[/color][/b]',
            markup=True,
            size_hint_y=None,
            height=dp(60)
        )
        root.add_widget(title)
        
        # 控制按钮区域
        controls = GridLayout(cols=3, spacing=dp(5), size_hint_y=None, height=dp(100))
        
        self.btn_ipv4 = Button(text='IPv4 扫描', background_color=(0.23, 0.51, 0.94, 1))
        self.btn_ipv4.bind(on_press=self.start_ipv4_scan)
        controls.add_widget(self.btn_ipv4)
        
        self.btn_ipv6 = Button(text='IPv6 扫描', background_color=(0.13, 0.77, 0.36, 1))
        self.btn_ipv6.bind(on_press=self.start_ipv6_scan)
        controls.add_widget(self.btn_ipv6)
        
        self.btn_stop = Button(text='停止任务', background_color=(0.94, 0.26, 0.26, 1), disabled=True)
        self.btn_stop.bind(on_press=self.stop_all_tasks)
        controls.add_widget(self.btn_stop)
        
        self.btn_area = Button(text='地区测速', background_color=(0.93, 0.28, 0.61, 1), disabled=True)
        self.btn_area.bind(on_press=self.start_region_speed_test)
        controls.add_widget(self.btn_area)
        
        self.btn_full = Button(text='完全测速', background_color=(0.97, 0.45, 0.10, 1), disabled=True)
        self.btn_full.bind(on_press=self.start_full_speed_test)
        controls.add_widget(self.btn_full)
        
        self.btn_export = Button(text='导出结果', background_color=(0.55, 0.36, 0.98, 1), disabled=True)
        self.btn_export.bind(on_press=self.export_results)
        controls.add_widget(self.btn_export)
        
        root.add_widget(controls)
        
        # 输入区域
        input_row = GridLayout(cols=3, spacing=dp(5), size_hint_y=None, height=dp(50))
        
        self.input_region = TextInput(hint_text='输入地区码', multiline=False)
        input_row.add_widget(self.input_region)
        
        self.combo_port = Spinner(
            text='443',
            values=PORT_OPTIONS,
            size_hint_x=None,
            width=dp(80)
        )
        input_row.add_widget(self.combo_port)
        
        placeholder = Label(text='')
        input_row.add_widget(placeholder)
        
        root.add_widget(input_row)
        
        # 进度条
        self.progress_bar = Label(
            text='进度: 0%',
            size_hint_y=None,
            height=dp(30),
            color=(0, 0, 0, 1)
        )
        root.add_widget(self.progress_bar)
        
        # 状态标签
        status_layout = GridLayout(cols=2, spacing=dp(5), size_hint_y=None, height=dp(30))
        self.status_label = Label(text='就绪', color=(0.4, 0.4, 0.4, 1))
        self.speed_label = Label(text='IP段: 加载中...', color=(0.4, 0.4, 0.4, 1))
        status_layout.add_widget(self.status_label)
        status_layout.add_widget(self.speed_label)
        root.add_widget(status_layout)
        
        # 日志显示区域
        log_label = Label(text='扫描状态和统计信息', size_hint_y=None, height=dp(30))
        root.add_widget(log_label)
        
        self.log_display = ScrollView()
        self.log_content = Label(text='', markup=True, size_hint_y=None, halign='left', valign='top')
        self.log_content.bind(texture_size=lambda instance, value: setattr(instance, 'height', value[1]))
        self.log_display.add_widget(self.log_content)
        root.add_widget(self.log_display)
        
        # 结果表格
        result_label = Label(text='测速结果', size_hint_y=None, height=dp(30))
        root.add_widget(result_label)
        
        self.result_display = ScrollView()
        self.result_content = Label(text='暂无结果', markup=True, size_hint_y=None, halign='left', valign='top')
        self.result_content.bind(texture_size=lambda instance, value: setattr(instance, 'height', value[1]))
        self.result_display.add_widget(self.result_content)
        root.add_widget(self.result_display)
        
        # 初始化变量
        self.scanner = None
        self.speed_tester = None
        self.scan_results = []
        self.speed_results = []
        self.scanning = False
        self.speed_testing = False
        self.cf_ipv4_cidrs = BACKUP_CF_IPV4_CIDRS
        self.cf_ipv6_cidrs = BACKUP_CF_IPV6_CIDRS
        
        # 开始加载IP列表
        Clock.schedule_once(self.start_ip_list_update, 0.1)
        
        return root
    
    def start_ip_list_update(self, dt):
        self.log_content.text += "[color=#0000FF]程序启动，开始更新IP地址段...[/color]\n"
        self.speed_label.text = "IP段: 已加载"
    
    def start_ipv4_scan(self, instance):
        if self.scanning or self.speed_testing:
            return
        
        self.scanning = True
        self.update_ui_state(task_started=True)
        
        self.scan_results = []
        self.result_content.text = "暂无结果"
        self.log_content.text += "[color=#00AA00]正在开始IPv4扫描...[/color]\n"
        
        port = int(self.combo_port.text)
        self.current_scan_port = port
        
        # 创建扫描器
        self.scanner = IPv4Scanner(
            log_callback=self.update_log,
            progress_callback=self.update_progress,
            result_callback=None,
            port=port,
            ipv4_cidrs=self.cf_ipv4_cidrs
        )
        
        # 在新线程中运行扫描
        thread = Thread(target=self.run_ipv4_scan_thread)
        thread.start()
    
    def run_ipv4_scan_thread(self):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        
        try:
            results = loop.run_until_complete(self.scanner.run_scan_async())
            if results is not None:
                Clock.schedule_once(lambda dt: self.scan_finished(results), 0)
        finally:
            loop.close()
    
    def start_ipv6_scan(self, instance):
        self.log_content.text += "[color=#FF0000]IPv6扫描功能待实现[/color]\n"
    
    def update_progress(self, current, total, success_count):
        if total > 0:
            progress = int((current / total) * 100)
            Clock.schedule_once(lambda dt: setattr(self.progress_bar, 'text', f'进度: {progress}% ({current}/{total}, 成功: {success_count})'), 0)
    
    def update_log(self, message):
        Clock.schedule_once(lambda dt: setattr(self.log_content, 'text', self.log_content.text + f"{message}\n"), 0)
    
    def scan_finished(self, results):
        self.scan_results = results
        self.scanning = False
        self.update_ui_state(task_started=False)
        
        if results:
            self.btn_full.disabled = False
            self.btn_area.disabled = False
            self.btn_export.disabled = False
            self.status_label.text = f"扫描完成: {len(results)} 个IP可用"
            
            # 显示摘要
            ipv4_count = sum(1 for r in results if ':' not in r['ip'])
            ipv6_count = sum(1 for r in results if ':' in r['ip'])
            
            summary = f"[color=#00AA00]扫描完成！找到 {len(results)} 个可用IP:\n"
            if ipv4_count > 0:
                summary += f"  IPv4: {ipv4_count} 个\n"
            if ipv6_count > 0:
                summary += f"  IPv6: {ipv6_count} 个\n"
            summary += f"  端口: {self.current_scan_port}[/color]\n"
            
            self.log_content.text += summary
        else:
            self.status_label.text = "扫描完成: 未找到可用IP"
            self.log_content.text += "[color=#FF0000]扫描完成，未找到任何可用IP[/color]\n"
    
    def start_full_speed_test(self, instance):
        if self.speed_testing or self.scanning or not self.scan_results:
            return
        
        self.speed_testing = True
        self.update_ui_state(task_started=True)
        
        self.result_content.text = "正在测速...\n"
        
        port = int(self.combo_port.text)
        self.speed_tester = SpeedTestWorker(self.scan_results, current_port=port)
        self.speed_tester.set_log_callback(self.update_log)
        
        # 在新线程中运行测速
        thread = Thread(target=self.run_speed_test_thread)
        thread.start()
    
    def start_region_speed_test(self, instance):
        region_code = self.input_region.text.strip().upper()
        if not region_code:
            self.log_content.text += "[color=#FF0000]请输入地区码（如SJC、SIN等）[/color]\n"
            return
        
        if self.speed_testing or self.scanning or not self.scan_results:
            return
        
        self.speed_testing = True
        self.update_ui_state(task_started=True)
        
        self.result_content.text = f"正在对 {region_code} 地区进行测速...\n"
        
        port = int(self.combo_port.text)
        self.speed_tester = SpeedTestWorker(self.scan_results, region_code=region_code, current_port=port)
        self.speed_tester.set_log_callback(self.update_log)
        
        # 在新线程中运行测速
        thread = Thread(target=self.run_speed_test_thread)
        thread.start()
    
    def run_speed_test_thread(self):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        
        try:
            results = loop.run_until_complete(self.speed_tester.run_async())
            if results is not None:
                Clock.schedule_once(lambda dt: self.speed_test_finished(results), 0)
        finally:
            loop.close()
    
    def speed_test_finished(self, results):
        self.speed_results = results
        self.speed_testing = False
        self.update_ui_state(task_started=False)
        
        if results:
            self.btn_export.disabled = False
            self.status_label.text = f"测速完成: {len(results)} 个结果"
            
            # 更新结果显示
            result_text = "[b]测速结果:[/b]\n"
            for i, result in enumerate(results, 1):
                result_text += f"{i}. [color=#00AA00]{result['ip']}[/color] | "
                result_text += f"{result['chinese_name']} | "
                result_text += f"延迟: {result['latency']}ms | "
                result_text += f"速度: {result['download_speed']:.2f}MB/s\n"
            
            self.result_content.text = result_text
        else:
            self.status_label.text = "测速完成: 无有效结果"
            self.result_content.text = "测速完成，但没有有效结果"
    
    def export_results(self, instance):
        if not self.speed_results:
            self.log_content.text += "[color=#FF0000]错误：没有测速结果可以导出！[/color]\n"
            return
        
        try:
            filename = f"cfs_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
            with open(filename, 'w', newline='', encoding='utf-8-sig') as csvfile:
                fieldnames = ['排名', 'IP地址', '地区码', '地区', '延迟', '下载速度', '端口', '测速类型']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                
                writer.writeheader()
                
                for i, result in enumerate(self.speed_results, 1):
                    writer.writerow({
                        '排名': i,
                        'IP地址': result['ip'],
                        '地区码': result.get('iata_code', ''),
                        '地区': result.get('chinese_name', ''),
                        '延迟': f"{result['latency']:.2f}",
                        '下载速度': f"{result['download_speed']:.2f}",
                        '端口': result.get('port', 443),
                        '测速类型': result.get('test_type', '未知')
                    })
            
            self.log_content.text += f"[color=#00AA00]结果已导出到: {filename}[/color]\n"
        except Exception as e:
            self.log_content.text += f"[color=#FF0000]导出失败: {str(e)}[/color]\n"
    
    def stop_all_tasks(self, instance):
        if self.scanner and self.scanning:
            self.scanner.stop()
            self.log_content.text += "[color=#FF6600]用户请求停止扫描...[/color]\n"
            self.scanning = False
        
        if self.speed_tester and self.speed_testing:
            self.speed_tester.stop()
            self.log_content.text += "[color=#FF6600]用户请求停止测速...[/color]\n"
            self.speed_testing = False
        
        self.update_ui_state(task_started=False)
    
    def update_ui_state(self, task_started=False):
        if task_started:
            self.btn_stop.disabled = False
            self.btn_ipv4.disabled = True
            self.btn_ipv6.disabled = True
            self.btn_full.disabled = True
            self.btn_area.disabled = True
        else:
            self.btn_stop.disabled = True
            self.btn_ipv4.disabled = False
            self.btn_ipv6.disabled = False
            if self.scan_results:
                self.btn_full.disabled = False
                self.btn_area.disabled = False
            else:
                self.btn_full.disabled = True
                self.btn_area.disabled = True

if __name__ == '__main__':
    CloudFlareScannerApp().run()