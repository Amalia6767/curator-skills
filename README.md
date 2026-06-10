# 🏛️ Curator Skills｜策展人 AI 技能套件

> 一套覆盖展厅/展馆投标全流程的 Claude Code Skills：从招标文件分析、疑问梳理，到主题推导、方案设计、画册撰写、PPT 排版、交互交付，最后用双盲交叉验证守住内容质量。

![Skill Type](https://img.shields.io/badge/Skills-Claude%20Code%20Skills-5B67CA)
![Language](https://img.shields.io/badge/Language-%E4%B8%AD%E6%96%87-orange)
![Domain](https://img.shields.io/badge/Domain-Exhibition%20Bidding%20%26%20Curation-0F766E)
![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)

## 🎯 这是什么

这是一名策展人在真实投标项目中淌出来的工作系统，不是教学框架。九个技能对应展陈投标的九个真实工序，互相衔接成一条生产线：

- **拿到标书** → 自动提取关键信息、识别废标点、生成答疑疑问清单
- **构思方案** → 用「策展五力」模型和「九层递进法」推导主题与方案
- **输出交付物** → 投标方案母版、画册页面说明、PPT 排版指南、交互组任务书
- **质量兜底** → 对 AI 生成内容做溯源标注 + 独立交叉验证，拦截幻觉

所有案例均已脱敏，方法论保留完整。适合策展人、展陈设计公司、投标团队，以及任何需要把"一堆甲方资料"变成"能中标的方案"的人。

## ✨ 核心方法论

| 模型 | 所在技能 | 一句话 |
| --- | --- | --- |
| **策展五力** | proposal-design | 价值闭环力 / 精准角色力 / 分层叙事力 / 场域应变力 / 进化工具力——方案构思阶段的五项硬指标 |
| **九层递进法** | exhibition-theme-brainstorm | 从宏观理念（哲学）逐层推到设计元素（视觉），主题不再靠"找感觉" |
| **评分点→证据映射** | proposal-design / tender-analysis | 每个评分项都写出"方案写什么、附什么证明、怎么可视化" |
| **口径优先级基线** | proposal-design | 书面澄清 > SRM 公告 > 口头纪要 > 初版标书，多轮答疑不再口径混乱 |
| **双盲交叉验证** | verify-content | 两个独立轮次核查 AI 生成内容，两轮都中才算高置信度问题 |

## 🧩 技能列表与工作流

```
招标文件 ──→ tender-analysis（投标分析 + 疑问梳理）
                │
                ├──→ proposal-design（方案设计 · 策展五力）
                │        ├──→ exhibition-theme-brainstorm（主题推导 · 九层递进）
                │        ├──→ proposal-interpretation（内部讲解版）
                │        ├──→ exhibition-outline（展陈大纲 · 3页PPT格式）
                │        ├──→ ppt-layout（PPT 排版指南）
                │        └──→ interaction-team-deliverables（交互组交付指南）
                │
                └──→ tender-booklet-writing（投标画册页面说明）

任何生成内容 ──→ verify-content（防幻觉验证）
```

| 阶段 | 技能 | 说明 |
| --- | --- | --- |
| 投标 | [tender-analysis](skills/tender-analysis/) | 分析招标文件（PDF/Word/Excel），提取要求与评分标准，按类别+职能双维度梳理答疑疑问 |
| 投标 | [tender-booklet-writing](skills/tender-booklet-writing/) | 为投标画册撰写页面说明，供汇报讲解与甲方阅读 |
| 策划 | [proposal-design](skills/proposal-design/) | 基于分析结果与答疑增量，按策展五力生成投标方案（Word/PPT/网页三形态） |
| 策划 | [proposal-interpretation](skills/proposal-interpretation/) | 方案转内部讲解文档：一句话核心 + 三大核心 + 5分钟讲解脚本 |
| 策划 | [exhibition-theme-brainstorm](skills/exhibition-theme-brainstorm/) | 九层递进法推导展陈主题、空间命名与设计元素 |
| 设计 | [exhibition-outline](skills/exhibition-outline/) | 生成 3 页 PPT 格式展陈大纲（主题→诠释→大纲要点） |
| 设计 | [ppt-layout](skills/ppt-layout/) | 方案转 PPT 排版指南，逐页给出标题层级、内容组织与视觉建议 |
| 设计 | [interaction-team-deliverables](skills/interaction-team-deliverables/) | 方案转交互组可执行的设计交付指南，对齐招标技术评分 |
| 质保 | [verify-content](skills/verify-content/) | 溯源标注 + 独立交叉验证，输出带评级的验证报告 |

## 🚀 安装

### Claude Code

个人技能放 `~/.claude/skills/`，团队项目技能放项目内 `.claude/skills/`。

```bash
git clone https://github.com/Amalia6767/curator-skills.git
mkdir -p ~/.claude/skills
cp -R curator-skills/skills/* ~/.claude/skills/
```

只想要某一个技能，就只拷那一个文件夹（每个技能自带 `SKILL.md`，相互独立可用）。

### 其他支持本地 skills 目录的工具

把 `skills/` 下的技能文件夹复制到对应工具的技能目录即可（如 `~/.codex/skills/`）。

### tender-analysis 的脚本环境（可选）

仅 tender-analysis 的文件提取脚本需要 Python 环境，安装方法见 [skills/tender-analysis/SETUP.md](skills/tender-analysis/SETUP.md)。其余技能开箱即用。

## 💬 使用示例

```text
你：请分析这份招标文件：xx展厅设计施工一体化-招标文件.pdf，并梳理答疑疑问
→ 触发 tender-analysis，输出分析报告 + 按类别/职能分类的疑问清单

你：基于分析结果，按策展五力出投标方案
→ 触发 proposal-design，输出方案母版 + 评分点证据映射表

你：验证
→ 触发 verify-content，对刚生成的文档做双盲交叉核查
```

## 🔒 关于脱敏

仓库内所有案例片段（能源集团主题推导、消费金融展厅棱镜理念等）均来自真实中标/投标项目，已统一做匿名化处理：企业名称、项目全称、专有系统名、可识别的具体数据均已替换或泛化。方法论与推导过程保持原样。

向本仓库贡献内容时请遵守同样规则，详见 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 📄 许可证

[MIT License](LICENSE)

## 🙋 作者

**斗转Xingyi**（小红书同名）——策展人 / AI 产品经理，20+ 展览项目经验。本套件是「策展人 AI 赋能实验室」系列的开源部分：把策展行业里"只可意会"的投标与前策经验，拆成可复用、可协作、可迭代的工具。
