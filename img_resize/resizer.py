#!/usr/bin/env python3
"""
img-resize-kit - 图片批量缩放与裁剪工具
功能：批量缩放、裁剪、压缩图片
用法：img-resize [输入目录] [宽度] [高度] [输出目录]
      img-resize resize ./图片/ 800 600 ./输出/
      img-resize compress ./图片/ 80
      img-resize info ./图片/
"""
import sys
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    print("正在安装 Pillow...")
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "Pillow", "-q"])
    from PIL import Image


SUPPORTED_EXTS = {'.jpg', '.jpeg', '.png', '.webp', '.bmp', '.tiff'}


def _get_images(input_dir):
    """获取目录下所有支持的图片文件"""
    p = Path(input_dir)
    if not p.exists():
        return None, f"目录 {input_dir} 不存在"

    files = []
    for ext in SUPPORTED_EXTS:
        files.extend(list(p.glob(f"*{ext}")) + list(p.glob(f"*{ext.upper()}")))
    files.sort()

    if not files:
        return None, f"目录 {input_dir} 中没有找到支持的图片文件"

    return files, None


def resize_images(input_dir, width, height, output_dir=None, keep_aspect=True):
    """批量缩放图片"""
    files, error = _get_images(input_dir)
    if error:
        print(f"错误: {error}")
        return False

    if output_dir:
        out_path = Path(output_dir)
    else:
        out_path = Path(input_dir) / f"resized_{width}x{height}"
    out_path.mkdir(parents=True, exist_ok=True)

    print(f"找到 {len(files)} 个图片文件，目标尺寸: {width}x{height}")
    success = 0

    for f in files:
        try:
            img = Image.open(f)

            # 计算新尺寸
            if keep_aspect:
                img.thumbnail((width, height), Image.LANCZOS)
            else:
                img = img.resize((width, height), Image.LANCZOS)

            out_file = out_path / f.name
            # 保持原始格式
            format_map = {'.jpg': 'JPEG', '.jpeg': 'JPEG', '.png': 'PNG', '.webp': 'WEBP', '.bmp': 'BMP', '.tiff': 'TIFF'}
            fmt = format_map.get(f.suffix.lower(), 'JPEG')
            if fmt == 'JPEG' and img.mode in ('RGBA', 'P'):
                img = img.convert('RGB')
            img.save(out_file, format=fmt, quality=95)

            success += 1
            print(f"  ✓ {f.name} ({img.size[0]}x{img.size[1]})")
        except Exception as e:
            print(f"  ✗ {f.name} 处理失败: {e}")

    print(f"\n完成！成功处理 {success}/{len(files)} 个文件")
    print(f"输出目录: {out_path}")
    return success > 0


def compress_images(input_dir, quality=80, output_dir=None):
    """批量压缩图片（降低质量以减小文件大小）"""
    files, error = _get_images(input_dir)
    if error:
        print(f"错误: {error}")
        return False

    if output_dir:
        out_path = Path(output_dir)
    else:
        out_path = Path(input_dir) / f"compressed_q{quality}"
    out_path.mkdir(parents=True, exist_ok=True)

    if not 1 <= quality <= 100:
        print("错误：质量值必须在 1-100 之间")
        return False

    print(f"找到 {len(files)} 个图片文件，压缩质量: {quality}%")
    success = 0
    total_saved = 0

    for f in files:
        try:
            img = Image.open(f)
            original_size = f.stat().st_size

            out_file = out_path / f.name
            format_map = {'.jpg': 'JPEG', '.jpeg': 'JPEG', '.png': 'PNG', '.webp': 'WEBP', '.bmp': 'BMP', '.tiff': 'TIFF'}
            fmt = format_map.get(f.suffix.lower(), 'JPEG')

            if fmt == 'JPEG':
                if img.mode in ('RGBA', 'P'):
                    img = img.convert('RGB')
                img.save(out_file, format=fmt, quality=quality, optimize=True)
            elif fmt == 'PNG':
                img.save(out_file, format=fmt, optimize=True)
            else:
                img.save(out_file, format=fmt)

            new_size = out_file.stat().st_size
            saved = original_size - new_size
            total_saved += saved
            pct = ((original_size - new_size) / original_size * 100) if original_size > 0 else 0

            print(f"  ✓ {f.name} ({original_size//1024}KB → {new_size//1024}KB, 节省 {pct:.0f}%)")
            success += 1
        except Exception as e:
            print(f"  ✗ {f.name} 处理失败: {e}")

    print(f"\n完成！成功处理 {success}/{len(files)} 个文件")
    print(f"总节省空间: {total_saved / 1024:.1f} KB")
    print(f"输出目录: {out_path}")
    return success > 0


def image_info(input_dir):
    """查看图片信息"""
    files, error = _get_images(input_dir)
    if error:
        print(f"错误: {error}")
        return False

    print(f"{'文件名':30s} {'格式':8s} {'尺寸':14s} {'大小':10s}")
    print("-" * 62)

    total_size = 0
    for f in files:
        try:
            img = Image.open(f)
            size = f.stat().st_size
            total_size += size
            dim = f"{img.size[0]}x{img.size[1]}"
            print(f"{f.name:30s} {img.format:8s} {dim:14s} {size//1024:4d}KB")
        except Exception as e:
            print(f"{f.name:30s} {'ERROR':8s}")

    print("-" * 62)
    print(f"{'总计':30s} {len(files):3d} 个文件{'':8s} {total_size//1024:4d}KB")
    return True


def _show_promotion():
    print("\n" + "=" * 55)
    print("  🔧 img-resize-kit - 图片批量缩放与压缩工具")
    print("  📦 pip install img-resize-kit")
    print("  ☕ 如果帮到了您，欢迎打赏支持:")
    print("     USDT(TRC20): TMPQygMkv42QPeyYnkxMkPwsqs7udbD2Aa")
    print("  ⭐ https://github.com/BoiledSaltedDuck/img-resize-kit")
    print("=" * 55)


def main():
    if len(sys.argv) < 2:
        print("用法:")
        print("  缩放图片: img-resize resize [输入目录] [宽度] [高度] [输出目录(可选)]")
        print("  压缩图片: img-resize compress [输入目录] [质量1-100] [输出目录(可选)]")
        print("  查看信息: img-resize info [输入目录]")
        print()
        print("示例:")
        print("  img-resize resize ./图片/ 800 600 ./输出/")
        print("  img-resize compress ./图片/ 80")
        print("  img-resize info ./图片/")
        sys.exit(1)

    command = sys.argv[1].lower()

    if command == "resize":
        if len(sys.argv) < 5:
            print("用法: img-resize resize [输入目录] [宽度] [高度] [输出目录(可选)]")
            sys.exit(1)
        try:
            width = int(sys.argv[3])
            height = int(sys.argv[4])
        except ValueError:
            print("错误：宽度和高度必须为整数")
            sys.exit(1)
        output = sys.argv[5] if len(sys.argv) > 5 else None
        success = resize_images(sys.argv[2], width, height, output)

    elif command == "compress":
        if len(sys.argv) < 4:
            print("用法: img-resize compress [输入目录] [质量1-100] [输出目录(可选)]")
            sys.exit(1)
        try:
            quality = int(sys.argv[3])
        except ValueError:
            print("错误：质量必须为整数（1-100）")
            sys.exit(1)
        output = sys.argv[4] if len(sys.argv) > 4 else None
        success = compress_images(sys.argv[2], quality, output)

    elif command == "info":
        if len(sys.argv) < 3:
            print("用法: img-resize info [输入目录]")
            sys.exit(1)
        success = image_info(sys.argv[2])

    else:
        print(f"错误：不支持的命令 '{command}'，仅支持 resize/compress/info")
        sys.exit(1)

    if success:
        _show_promotion()
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
