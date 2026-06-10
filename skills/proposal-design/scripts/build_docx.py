#!/usr/bin/env python3
"""
可选：将 Markdown（母版/对外版）转换为 docx。

依赖（建议用 uv/venv 安装）：
  pip install pypandoc python-docx

备注：
- 若系统未安装 pandoc，此脚本会提示安装方式。
- 适合“先写 Markdown，再转 Word”的工作流。
"""

import shutil
import sys


def main() -> int:
    if len(sys.argv) < 3:
        print("用法: python build_docx.py <input.md> <output.docx>")
        return 2

    in_md = sys.argv[1]
    out_docx = sys.argv[2]

    if shutil.which("pandoc") is None:
        print(
            "错误: 未找到 pandoc。\n"
            "macOS 可用: brew install pandoc\n"
            "或从官网安装: https://pandoc.org/installing.html",
            file=sys.stderr,
        )
        return 1

    try:
        import pypandoc  # type: ignore
    except Exception as e:
        print(f"错误: 缺少依赖 pypandoc: {e}", file=sys.stderr)
        return 1

    try:
        pypandoc.convert_file(in_md, "docx", outputfile=out_docx)
    except Exception as e:
        print(f"转换失败: {e}", file=sys.stderr)
        return 1

    print(f"已生成: {out_docx}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

