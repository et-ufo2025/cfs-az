# main.py - Kivy GUI Application for CF IP Scanning
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

# --- Core Scanning Logic ---

# Airport code mapping for location
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

# Backup CF IP ranges
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
                # Simulate getting location (in real app, you'd use an API)
                iata_code = "SJC"  # Placeholder
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
                self.log_callback(f"Generated {len(ip_list)} random IPs, starting scan...")

            tasks = [self.test_single_ip(ip) for ip in ip_list]
            results = await asyncio.gather(*tasks)
            
            successful_results = [r for r in results if r is not None]
            successful_results.sort(key=lambda x: x['latency'])

            if self.result_callback:
                self.result_callback(successful_results)
            
            return successful_results
        except Exception as e:
            if self.log_callback:
                self.log_callback(f"Error during scan: {str(e)}")
            return []

    def stop(self):
        self.running = False

class MainApp(App):
    def build(self):
        Window.size = (dp(400), dp(600))
        
        layout = BoxLayout(orientation='vertical', padding=dp(10), spacing=dp(10))

        title = Label(
            text='[b][color=#ff7a18]CloudFlare[/color] [color=#111827]Scan[/color]\n[color=#6B7280]v2.2 - GitHub CI[/color][/b]',
            markup=True,
            size_hint_y=None,
            height=dp(60)
        )
        layout.add_widget(title)

        self.scan_button = Button(text='开始扫描 (端口 443)', size_hint_y=None, height=dp(50))
        self.scan_button.bind(on_press=self.start_scan)
        layout.add_widget(self.scan_button)

        self.stop_button = Button(text='停止扫描', size_hint_y=None, height=dp(50), disabled=True)
        self.stop_button.bind(on_press=self.stop_scan)
        layout.add_widget(self.stop_button)

        log_label = Label(text='日志:', size_hint_y=None, height=dp(30))
        layout.add_widget(log_label)

        scroll = ScrollView(size_hint_y=0.4)
        self.log_output = Label(text='等待扫描...', markup=True, size_hint_y=None, halign='left', valign='top')
        self.log_output.bind(texture_size=lambda instance, value: setattr(instance, 'height', value[1]))
        scroll.add_widget(self.log_output)
        layout.add_widget(scroll)

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
        self.log_output.text += "\n[INFO] Starting scan..."
        
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
            result_text = "[b]Found IPs:[/b]\n"
            for r in results[:10]: # Show top 10 fastest
                result_text += f"{r['ip']} | {r['chinese_name']} | {r['latency']}ms\n"
            self.result_output.text = result_text
            self.log_output.text += f"\n[SUCCESS] Scan complete. Found {len(results)} IPs."
        else:
            self.log_output.text += "\n[ERROR] Scan complete. No IPs found."

    def update_log(self, message):
        Clock.schedule_once(lambda dt: setattr(self.log_output, 'text', self.log_output.text + f"\n{message}"), 0)

    def stop_scan(self, instance):
        if self.scanner:
            self.scanner.stop()
            self.log_output.text += "\n[INFO] User requested to stop scan..."
            self.scan_button.disabled = False
            self.stop_button.disabled = True

if __name__ == '__main__':
    MainApp().run()
