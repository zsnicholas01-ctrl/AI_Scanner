# AI 智能漏洞扫描器

这是一个基于 Python Tkinter 开发的简易 AI 智能漏洞扫描器，支持目标存活检测、目录扫描、XSS 检测、SQL 注入错误特征检测，并结合大模型接口对页面内容进行智能漏洞分析。

## 功能

- 目标存活检测
- 常见目录扫描
- XSS 反射检测
- SQL 注入错误特征检测
- AI 智能漏洞分析
- Tkinter 图形化界面

## 项目结构

```text
main.py          # 图形界面入口
core.py          # 扫描核心逻辑
ai_detector.py   # AI 分析模块
config.py        # 配置文件