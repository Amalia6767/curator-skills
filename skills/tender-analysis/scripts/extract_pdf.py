#!/usr/bin/env python3
"""
提取 PDF 文档内容
"""
import sys
import pdfplumber

def extract_pdf(file_path):
    """提取 PDF 文档的所有文本内容"""
    try:
        with pdfplumber.open(file_path) as pdf:
            content = []
            for page in pdf.pages:
                text = page.extract_text()
                if text and text.strip():
                    content.append(text)
            
            # 尝试提取表格
            for page in pdf.pages:
                tables = page.extract_tables()
                for table in tables:
                    if table:
                        for row in table:
                            if row:
                                row_text = [str(cell) if cell else '' for cell in row]
                                if any(row_text):
                                    content.append(" | ".join(row_text))
            
            return "\n".join(content)
    except Exception as e:
        print(f"错误: {e}", file=sys.stderr)
        return None

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法: python extract_pdf.py <文件路径>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    content = extract_pdf(file_path)
    
    if content:
        print(content)
    else:
        sys.exit(1)
