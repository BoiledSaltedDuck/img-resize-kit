# img-resize-kit 图片批量缩放与压缩工具

[![PyPI version](https://img.shields.io/pypi/v/img-resize-kit)](https://pypi.org/project/img-resize-kit/)
[![Downloads](https://img.shields.io/pypi/dm/img-resize-kit)](https://pypi.org/project/img-resize-kit/)
[![License](https://img.shields.io/pypi/l/img-resize-kit)](https://github.com/BoiledSaltedDuck/img-resize-kit/blob/main/LICENSE)

> **Office Tools Kit 系列** — 用AI写代码，用工具提效。一行命令搞定日常办公与开发杂务。

## 安装

```bash
pip install img-resize-kit
```

## 用法

```bash
# 批量缩放图片（保持宽高比）
img-resize resize ./图片/ 800 600 ./输出/

# 批量压缩图片
img-resize compress ./图片/ 80

# 查看图片信息
img-resize info ./图片/
```

## 功能

### 缩放 (resize)
- 批量调整图片到指定尺寸
- 默认保持宽高比
- 使用 LANCZOS 高质量重采样算法

### 压缩 (compress)
- 批量压缩 JPEG 图片（调整质量参数）
- PNG 图片自动优化
- 显示压缩前后的文件大小对比

### 信息 (info)
- 扫描目录中所有图片
- 显示格式、尺寸、文件大小

## 🧰 Office Tools Kit 系列工具

本工具属于 **Office Tools Kit 系列**，同类工具推荐：

| 工具 | 功能 | 安装 |
|------|------|------|
| [office-tools-kit](https://pypi.org/project/office-tools-kit/) | Excel合并拆分、PDF合并 | `pip install office-tools-kit` |
| [file-org-kit](https://pypi.org/project/file-org-kit/) | 文件智能分类整理 | `pip install file-org-kit` |
| [img-convert-kit](https://pypi.org/project/img-convert-kit/) | 图片格式批量转换 | `pip install img-convert-kit` |
| [img-resize-kit](https://pypi.org/project/img-resize-kit/) | 图片批量缩放与压缩 | `pip install img-resize-kit` |
| [json-tool-kit](https://pypi.org/project/json-tool-kit/) | JSON 文件处理 | `pip install json-tool-kit` |
| [markdown-kit](https://pypi.org/project/markdown-kit/) | Markdown 文档辅助 | `pip install markdown-kit` |
| [qr-code-kit](https://pypi.org/project/qr-code-kit/) | 二维码生成与解析 | `pip install qr-code-kit` |
| [text-clean-kit](https://pypi.org/project/text-clean-kit/) | 文本文件清洗处理 | `pip install text-clean-kit` |
| [unit-convert-kit](https://pypi.org/project/unit-convert-kit/) | 单位换算 | `pip install unit-convert-kit` |

> 📚 更多工具请访问 [BoiledSaltedDuck 工具主页](https://boiledsaltedduck.github.io/)

## 支持

如果 img-resize-kit 帮到了您，欢迎打赏支持：

```
USDT (TRC20): TMPQygMkv42QPeyYnkxMkPwsqs7udbD2Aa
```

您的支持是开源项目持续发展的动力 ❤️
