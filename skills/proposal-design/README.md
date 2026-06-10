# 方案设计与投标输出 Skill

本 skill 用于在完成 `tender-analysis`（投标文件分析与疑问梳理）后，结合**会议纪要 / 甲方新增需求 / 书面答疑 / 更明确的边界条件**等增量信息，生成可直接用于投标的方案输出（Word / PPT / 网页）。

## 文件结构

```
proposal-design/
├── SKILL.md
├── README.md
├── templates/
│   ├── proposal-outline.md              # 方案大纲（通用）
│   ├── proposal-word-outline.md         # Word 版章节结构与写作要点
│   ├── proposal-ppt-outline.md          # PPT 版页结构与叙事节奏
│   └── proposal-web-outline.md          # 网页/Markdown 版信息架构
└── scripts/
    ├── build_docx.py                    # 可选：将 Markdown/结构化数据生成 docx
    └── build_pptx.py                    # 可选：将结构化数据生成 pptx
```

## 输入（强约定）

来自 `tender-analysis` 的两份对内核心文档（必需）：
- `投标文件分析报告.md`
- `完整疑问清单_类别+职能.md`

增量材料（可选但强烈建议）：
- `会议纪要_*.md`（如第一轮答疑会议纪要）
- `答疑回复_*.docx/.pdf/.md`（甲方书面答疑）
- `新增需求_*.md`（甲方临时新增、范围调整、工期调整、界面确认等）
- `提疑模板_已回复.xlsx`（如果甲方要求按模板回填）

## 输出（按交付形态）

至少产出一个“对外可投标版本”（通常 Word 或 PPT）：
- Word：`投标方案.docx`（建议）或 `投标方案.md`
- PPT：`投标方案汇报.pptx`
- 网页：`投标方案.html` 或 `投标方案.md`

并建议同时产出一个“对内母版”：
- `投标方案_母版.md`：包含所有细节、风险与备选方案，用于内部评审与快速裁剪不同交付形态。

