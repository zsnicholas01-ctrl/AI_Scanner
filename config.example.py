# 请求头
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    "Accept": "*/*",
    "Connection": "keep-alive"
}

TIMEOUT = 5

# 目录字典
DIR_LIST = [
    "admin", "login", "robots.txt", "phpinfo.php",
    "backup", "data", "config"
]

# XSS 测试 payload
XSS_PAYLOADS = [
    "<script>alert(1)</script>",
    "\"onmouseover=alert(1)//",
    "<img src=x onerror=alert(1)>"
]

# SQL 注入特征
SQL_ERROR_RULES = [
    "mysql", "syntax", "ora-", "mssql",
    "数据库错误", "sql语法", "warning"
]

# ==================== AI 配置 ====================
AI_API_KEY = "这里填你自己的 sk-xxxx"
AI_API_URL = "https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions"