# 投标文件分析与方案设计 Skill

本 skill 提供完整的投标文件分析、疑问梳理和方案设计工作流程。

## 文件结构

```
tender-analysis/
├── SKILL.md                              # 主要技能文件（必读）
├── README.md                             # 本文件
├── pyproject.toml.example                # pyproject.toml 示例文件（推荐使用）
│
├── analysis-template.md                 # 投标文件分析模板
├── question-template.md                  # 疑问梳理模板（按类别）
├── proposal-example.md                   # 方案设计示例
│
├── templates/                            # 模板目录
│   ├── complete-question-list-template.md    # 完整疑问清单模板（类别+职能）
│   └── question-list-by-role.md              # 按职能分类的疑问模板
│
└── scripts/                               # 工具脚本目录
    ├── extract_docx.py                    # Word文档提取脚本（.docx）
    ├── extract_doc.py                     # Word文档提取脚本（.doc/.docx，支持老版本）
    ├── extract_pdf.py                     # PDF文档提取脚本
    └── extract_excel.py                   # Excel文档提取脚本（.xls/.xlsx）
```

## 快速开始

### 1. 环境准备（使用 UV - 最佳实践）

**重要**：统一使用 UV 管理 Python 环境，即使系统已安装其他包管理器。

#### 快速开始

```bash
# 1. 确保 UV 已安装（如未安装）
curl -LsSf https://astral.sh/uv/install.sh | sh
source ~/.local/bin/env  # 添加到 PATH

# 2. 进入项目目录
cd 项目目录

# 3. 创建虚拟环境
uv venv .venv

# 4. 激活环境并安装依赖
source .venv/bin/activate
uv pip install python-docx pdfplumber pytesseract pdf2image tabula-py docx2txt openpyxl xlrd
```

#### 推荐方式：使用项目模式

```bash
# 1. 初始化项目（创建 pyproject.toml）
uv init --no-readme

# 2. 添加依赖到 pyproject.toml（或手动编辑）
# 编辑 pyproject.toml，添加 dependencies

# 3. 同步环境（自动创建 .venv 并安装依赖）
uv sync
```

#### 为什么使用 UV？

- ⚡ **极速**：比 pip 快 10-100 倍
- 🔒 **可靠**：自动锁定依赖版本，确保环境一致性
- 🎯 **精确**：避免依赖冲突和版本问题
- 🚀 **现代**：支持项目级依赖管理（pyproject.toml）
- 🌍 **跨平台**：Windows、macOS、Linux 统一体验

#### 检查 UV 是否已安装

```bash
# 检查版本
uv --version

# 如果未安装，使用官方安装脚本
curl -LsSf https://astral.sh/uv/install.sh | sh

# 更新到最新版本（如已安装）
uv self-update
```

### 2. 提取投标文件内容

```bash
# 激活虚拟环境
source .venv/bin/activate

# 提取 Word 文档（.docx）
python scripts/extract_docx.py 投标文件.docx > content.txt

# 提取 Word 文档（.doc，老版本格式）
python scripts/extract_doc.py 投标文件.doc > content.txt

# 提取 PDF 文档
python scripts/extract_pdf.py 投标文件.pdf > content.txt

# 提取 Excel 文档（工程量清单等）
python scripts/extract_excel.py 工程量清单.xls > content.txt
```

### 3. 分析投标文件

1. 复制 `analysis-template.md` 作为分析报告起点
2. 根据提取的内容填写分析报告
3. 识别重点和难点

### 4. 梳理疑问

1. 复制 `templates/complete-question-list-template.md` 作为疑问清单起点
2. 按类别梳理疑问（参考 `question-template.md`）
3. 按职能梳理疑问（参考 `templates/question-list-by-role.md`）
4. 合并到完整疑问清单中

### 5. 生成方案

1. 根据答疑回复更新分析文档
2. 参考 `proposal-example.md` 的结构生成投标设计方案

## 工作流程

```
投标文件
   ↓
[阶段一] 文件分析 → 提取关键信息
   ↓
[阶段二] 疑问梳理 → 生成疑问清单（答疑会议前）
   ↓
答疑会议 → 获取甲方回复
   ↓
[阶段三] 方案设计 → 基于分析结果和答疑回复生成方案
```

## 关键检查点

### 疑问梳理检查点
- [ ] 所有模糊条款都已识别
- [ ] 所有不利于乙方的条款都已标注
- [ ] 疑问已按重要性分类（关键/重要/一般）
- [ ] 疑问已按类别和职能双重分类
- [ ] 疑问表述清晰，有具体引用
- [ ] 疑问清单已准备好，可在答疑会议使用

### 方案设计检查点
- [ ] 所有★必须满足的要求都已响应
- [ ] 所有+加分项都已体现
- [ ] 时间节点符合招标要求
- [ ] 技术方案满足所有技术规格
- [ ] 商务条款符合招标要求
- [ ] 方案结构完整、逻辑清晰
- [ ] 已根据答疑回复调整方案

## 常见问题

### Q: 如何提取 Word 文档中的表格？
A: `extract_docx.py` 脚本会自动提取表格内容，格式为 "单元格1 | 单元格2 | 单元格3"。

### Q: 如何处理老版本的 .doc 文件？
A: 使用 `extract_doc.py` 脚本，它会尝试多种方法：
1. 首先尝试 `docx2txt`（支持 .doc 和 .docx）
2. 如果是 .docx，使用 `python-docx`
3. 如果是 .doc，在 macOS 上使用系统工具 `textutil`
如果都失败，建议将 .doc 文件转换为 .docx 格式。

### Q: 如何提取 PDF 中的表格？
A: `extract_pdf.py` 脚本使用 `pdfplumber`，会自动提取 PDF 中的表格内容。

### Q: 为什么必须使用 UV？系统已经安装了 pip/conda。
A: UV 是 2025 年推荐的 Python 包管理最佳实践，具有以下优势：
- **极速**：比 pip 快 10-100 倍
- **可靠**：自动锁定依赖版本，确保环境一致性
- **精确**：避免依赖冲突和版本问题
- **现代化**：支持项目级依赖管理（pyproject.toml）
- **统一性**：所有项目使用相同工具，减少学习成本

即使系统已安装其他包管理器，也统一使用 UV 管理项目环境，确保一致性和可维护性。

### Q: 如何使用 pyproject.toml 管理依赖？
A: 
1. 复制 `pyproject.toml.example` 到项目根目录，重命名为 `pyproject.toml`
2. 编辑 `pyproject.toml`，添加或修改依赖
3. 运行 `uv sync` 自动创建虚拟环境并安装依赖
4. 使用 `uv run python script.py` 运行脚本（无需手动激活环境）

### Q: UV 和 pip 可以混用吗？
A: 不推荐。在同一个项目中，统一使用 UV 管理依赖。如果必须使用 pip，建议在 UV 创建的虚拟环境中使用 `uv pip install` 而不是系统的 `pip`。

### Q: 疑问清单应该提交多少条？
A: 建议提交所有关键疑问和重要疑问。一般疑问可选提交。

### Q: 如何确保疑问不遗漏？
A: 使用双重分类方法：
1. 按类别逐一检查（项目信息、技术要求、商务要求等）
2. 按职能逐一检查（项目负责人、空间设计师、策展人、平面设计师）

### Q: 方案设计应该在答疑前还是答疑后？
A: 应该在答疑后。先梳理疑问，获取答疑回复，再根据回复调整方案设计。

## 更新日志

### v2.3 (2026-01-25)
- 完善 UV 使用说明，明确 UV 为最佳实践
- 添加 pyproject.toml 示例文件，支持项目级依赖管理
- 统一使用 UV 管理环境，即使已安装其他包管理器

### v2.2 (2026-01-25)
- 新增 Excel 提取脚本（`extract_excel.py`，支持 .xls/.xlsx）
- 完善疑问清单模板，增加工程量清单具体项目疑问类型

### v2.1 (2026-01-25)
- 新增支持 .doc 文件提取（老版本 Word 格式）
- 新增 PDF 提取脚本（`extract_pdf.py`）
- 新增 Excel 文件支持说明（.xls/.xlsx）
- 更新依赖列表（添加 docx2txt, openpyxl, xlrd）
- 完善文件格式支持说明

### v2.0 (2026-01-25)
- 新增按职能角色分类的疑问梳理功能
- 新增完整疑问清单模板
- 新增按职能分类的疑问模板
- 新增工具脚本目录和提取脚本
- 更新 SKILL.md 引用新模板

### v1.0 (2026-01-25)
- 初始版本
- 基础的分析模板和疑问模板
- 方案设计示例

---

**维护者**：AI助手  
**最后更新**：2026年1月25日
