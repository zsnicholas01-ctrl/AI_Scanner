import requests
import json
from config import AI_API_KEY, AI_API_URL


class AIDetector:
    def __init__(self):
        self.api_key = AI_API_KEY
        self.api_url = AI_API_URL

    def analyze(self, url, html_content):
        prompt = f"""
你是专业网络安全工程师，只检测漏洞。
严格返回JSON，不要多余内容。

分析目标URL：{url}
网页内容：{html_content[:2500]}

请返回：
{{
    "has_vuln": true 或 false,
    "level": "高/中/低",
    "type": "漏洞类型",
    "advice": "修复建议"
}}
"""

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        data = {
            "model": "qwen-turbo",
            "messages": [{"role": "user", "content": prompt}]
        }

        try:
            resp = requests.post(self.api_url, json=data, headers=headers, timeout=20)
            result = resp.json()

            # 兼容通义千问格式
            if "choices" in result:
                content = result["choices"][0]["message"]["content"]
                return json.loads(content)

            return json.loads(resp.text)

        except Exception as e:
            print("AI错误：", e)
            return {
                "has_vuln": False,
                "level": "解析失败",
                "type": "解析失败",
                "advice": "请重试"
            }