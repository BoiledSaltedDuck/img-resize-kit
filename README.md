# img-resize-kit 图片批量缩放与压缩工具

[![PyPI version](https://img.shields.io/pypi/v/img-resize-kit)](https://pypi.org/project/img-resize-kit/)
[![Downloads](https://img.shields.io/pypi/dm/img-resize-kit)](https://pypi.org/project/img-resize-kit/)
[![License](https://img.shields.io/pypi/l/img-resize-kit)](https://github.com/BoiledSaltedDuck/img-resize-kit/blob/main/LICENSE)

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

## 支持

如果 img-resize-kit 帮到了您，欢迎打赏支持：

```
USDT (TRC20): TMPQygMkv42QPeyYnkxMkPwsqs7udbD2Aa
```

您的支持是开源项目持续发展的动力 ❤️
