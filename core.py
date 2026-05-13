import requests
from config import *
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class ScanCore:
    def __init__(self, target_url):
        self.target_url = target_url.strip()
        self.base_url = self.target_url.rstrip("/")

    def check_alive(self):
        try:
            resp = requests.get(
                url=self.target_url,
                headers=HEADERS,
                timeout=TIMEOUT,
                verify=False
            )
            return {
                "status": True,
                "code": resp.status_code,
                "html": resp.text[:3000],
                "msg": f"[+] 目标存活 状态码：{resp.status_code}"
            }
        except:
            return {"status": False, "msg": "[-] 目标连接失败"}

    def scan_dir(self):
        result = []
        try:
            for path in DIR_LIST:
                url = f"{self.base_url}/{path}"
                r = requests.get(url, headers=HEADERS, timeout=TIMEOUT, verify=False)
                if r.status_code == 200:
                    result.append(f"[发现] {url}")
            return {"status": True, "data": result, "msg": "目录扫描完成"}
        except:
            return {"status": False, "msg": "扫描失败"}

    def check_xss(self):
        res = []
        try:
            for p in XSS_PAYLOADS:
                r = requests.get(f"{self.base_url}?q={p}", headers=HEADERS, timeout=TIMEOUT, verify=False)
                if p in r.text:
                    res.append(f"[XSS] {p}")
            return {"status": True, "data": res, "msg": "XSS检测完成"}
        except:
            return {"status": False, "msg": "XSS检测失败"}

    def check_sql(self):
        res = []
        try:
            r = requests.get(f"{self.base_url}?id=1'", headers=HEADERS, timeout=TIMEOUT, verify=False)
            t = r.text.lower()
            for rule in SQL_ERROR_RULES:
                if rule in t:
                    res.append(f"[SQL注入] 命中特征：{rule}")
                    break
            return {"status": True, "data": res, "msg": "SQL注入检测完成"}
        except:
            return {"status": False, "msg": "SQL检测失败"}