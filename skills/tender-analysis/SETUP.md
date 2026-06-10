# 环境准备（Python / UV）

本文档说明 tender-analysis 脚本的运行环境配置。首次使用前阅读一次即可。

### Python 环境管理（最佳实践：使用 UV）

**重要原则**：
1. **必须使用虚拟环境**：避免污染系统基础环境
2. **统一使用 UV**：即使系统已安装其他包管理器，也统一使用 UV 管理项目环境
3. **项目级管理**：每个项目独立环境，互不干扰

UV 是 2025 年推荐的 Python 包管理最佳实践，具有以下优势：
- ⚡ **极速**：比 pip 快 10-100 倍
- 🔒 **可靠**：自动锁定依赖版本，确保环境一致性
- 🎯 **精确**：避免依赖冲突和版本问题
- 🚀 **现代**：支持项目级依赖管理（pyproject.toml）

#### 标准工作流程

**第一步：确保 UV 已安装并可用**

```bash
# 检查 UV 是否已安装
uv --version

# 如果未安装，使用官方安装脚本（推荐）
curl -LsSf https://astral.sh/uv/install.sh | sh

# 将 UV 添加到 PATH（如果尚未添加）
source ~/.local/bin/env  # macOS/Linux
# 或添加到 ~/.zshrc / ~/.bashrc: export PATH="$HOME/.local/bin:$PATH"

# 更新 UV 到最新版本（如已安装）
uv self-update
```

**第二步：创建项目虚拟环境**

```bash
# 进入项目目录
cd 项目目录

# 使用 UV 创建虚拟环境（推荐方式）
uv venv .venv

# 或者使用 UV 项目模式（更推荐，自动管理依赖）
uv init --no-readme  # 创建 pyproject.toml
uv venv
```

**第三步：安装依赖**

```bash
# 方式1：直接使用 uv pip install（简单快速）
source .venv/bin/activate
uv pip install python-docx pdfplumber pytesseract pdf2image tabula-py docx2txt openpyxl xlrd

# 方式2：使用项目模式（推荐，更规范）
# 在项目根目录创建 pyproject.toml，然后：
uv sync  # 自动安装 pyproject.toml 中的依赖
```

**第四步：使用环境运行脚本**

```bash
# 激活虚拟环境
source .venv/bin/activate

# 运行脚本
python scripts/extract_docx.py 文件路径.docx

# 或使用 uv run（无需激活环境）
uv run python scripts/extract_docx.py 文件路径.docx
```

#### 推荐的项目结构（使用 pyproject.toml）

在项目根目录创建 `pyproject.toml`：

```toml
[project]
name = "tender-analysis"
version = "0.1.0"
description = "投标文件分析工具"
requires-python = ">=3.10"
dependencies = [
    "python-docx>=1.0.0",
    "pdfplumber>=0.10.0",
    "docx2txt>=0.8",
    "openpyxl>=3.1.0",
    "xlrd>=2.0.0",
]

[project.optional-dependencies]
ocr = [
    "pytesseract>=0.3.10",
    "pdf2image>=1.16.0",
]
pdf-tables = [
    "tabula-py>=2.5.0",
]

[tool.uv]
dev-dependencies = []
```

然后使用：
```bash
# 安装基础依赖
uv sync

# 安装可选依赖（如需要 OCR）
uv sync --extra ocr --extra pdf-tables
```

#### 依赖说明

**必需依赖**：
- `python-docx`: 处理 .docx 文件
- `docx2txt`: 处理 .doc 和 .docx 文件（备用方案）
- `pdfplumber`: 处理 PDF 文件（推荐，支持表格提取）
- `openpyxl`: 处理 .xlsx 文件
- `xlrd`: 处理 .xls 文件

**可选依赖**：
- `pytesseract`, `pdf2image`: OCR 识别（用于图片型 PDF）
- `tabula-py`: PDF 表格提取（备用方案）

#### 常用 UV 命令

```bash
# 创建虚拟环境
uv venv .venv

# 激活环境（传统方式）
source .venv/bin/activate

# 使用 uv run（无需激活）
uv run python script.py

# 安装包
uv pip install package-name

# 查看已安装包
uv pip list

# 更新包
uv pip install --upgrade package-name

# 同步项目依赖（使用 pyproject.toml）
uv sync

# 更新 UV 自身
uv self-update
```

#### 为什么统一使用 UV？

1. **一致性**：所有项目使用相同的工具，减少学习成本
2. **速度**：比 pip 快 10-100 倍，节省时间
3. **可靠性**：自动处理依赖冲突，减少环境问题
4. **现代化**：支持最新的 Python 包管理标准
5. **跨平台**：Windows、macOS、Linux 统一体验
