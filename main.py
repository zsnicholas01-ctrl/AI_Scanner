import tkinter as tk
from core import ScanCore
from ai_detector import AIDetector

class AIVulnScanner:
    def __init__(self, root):
        self.root = root
        self.root.title("AI智能漏洞扫描器")
        self.root.geometry("950x650")
        self.init_ui()

    def init_ui(self):
        # URL 输入
        f_top = tk.Frame(self.root, padx=10, pady=10)
        f_top.pack(fill=tk.X)
        tk.Label(f_top, text="目标URL：").pack(side=tk.LEFT)
        self.entry = tk.Entry(f_top, font=("微软雅黑", 10))
        self.entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=10)

        # 按钮
        f_btn = tk.Frame(self.root, padx=10)
        f_btn.pack(fill=tk.X)

        tk.Button(f_btn, text="存活检测", width=10, command=self.run_alive).pack(side=tk.LEFT, padx=4)
        tk.Button(f_btn, text="目录扫描", width=10, command=self.run_dir).pack(side=tk.LEFT, padx=4)
        tk.Button(f_btn, text="XSS检测", width=10, command=self.run_xss).pack(side=tk.LEFT, padx=4)
        tk.Button(f_btn, text="SQL注入检测", width=12, command=self.run_sql).pack(side=tk.LEFT, padx=4)
        tk.Button(f_btn, text="AI智能分析", width=14, command=self.run_ai).pack(side=tk.LEFT, padx=10)
        tk.Button(f_btn, text="清空日志", width=10, command=self.clear).pack(side=tk.LEFT)

        # 日志
        tk.Label(self.root, text="扫描日志", font=("黑体", 12, "bold")).pack(anchor="w", padx=15)
        self.log_box = tk.Text(self.root, font=("Consolas", 10))
        self.log_box.pack(padx=15, pady=5, fill=tk.BOTH, expand=True)

    def log(self, msg):
        self.log_box.insert("end", f"{msg}\n")
        self.log_box.see("end")

    def get_url(self):
        u = self.entry.get().strip()
        if not u:
            self.log("[!] 请输入URL")
            return None
        return u

    def run_alive(self):
        u = self.get_url()
        if not u: return
        self.log("[+] 检测存活...")
        res = ScanCore(u).check_alive()
        self.log(res["msg"])

    def run_dir(self):
        u = self.get_url()
        if not u: return
        self.log("[+] 扫描目录...")
        res = ScanCore(u).scan_dir()
        self.log(res["msg"])
        for i in res["data"]: self.log(i)

    def run_xss(self):
        u = self.get_url()
        if not u: return
        self.log("[+] 检测XSS...")
        res = ScanCore(u).check_xss()
        self.log(res["msg"])
        for i in res["data"]: self.log(i)

    def run_sql(self):
        u = self.get_url()
        if not u: return
        self.log("[+] 检测SQL注入...")
        res = ScanCore(u).check_sql()
        self.log(res["msg"])
        for i in res["data"]: self.log(i)

    def run_ai(self):
        u = self.get_url()
        if not u: return
        self.log("\n[AI] 正在智能分析页面漏洞...")

        scanner = ScanCore(u)
        page = scanner.check_alive()
        if not page["status"]:
            self.log("[AI] 目标无法访问")
            return

        ai = AIDetector()
        result = ai.analyze(u, page["html"])

        self.log("=" * 60)
        self.log("[AI 分析结果]")
        self.log(f"风险等级：{result.get('level', '未知')}")
        self.log(f"漏洞类型：{result.get('type', '无')}")
        self.log(f"是否漏洞：{result.get('has_vuln', '否')}")
        self.log(f"修复建议：{result.get('advice', '无')}")
        self.log("=" * 60 + "\n")

    def clear(self):
        self.log_box.delete(1.0, "end")

if __name__ == "__main__":
    root = tk.Tk()
    AIVulnScanner(root)
    root.mainloop()