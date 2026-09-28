# organize-bilingual-literature · 双语文献整理

将论文、PDF、arXiv 链接和课程讲义整理为可在 Obsidian 中阅读的中英对照资料。保留原始文件，逐段翻译正文，保存图片，并添加双语图注和中文读图提示。

由 [Kys75](https://github.com/Kys75) 维护，初始内容整理自作者本机使用的 Skill。仓库根目录就是完整 Skill；核心规则见 [SKILL.md](SKILL.md)。这是独立的 Agent Skill，不是 Obsidian 应用插件。

## 在 Codex 中安装

先确保 Codex 能正常工作，再把下面这段话复制给 Agent。如果仓库为私有，你的 GitHub 账号还需要具备读取权限，并在本机完成相应认证。

```text
请从 https://github.com/Kys75/organize-bilingual-literature 安装 organize-bilingual-literature。
Skill 位于仓库根目录；如果使用 skill-installer，请指定仓库内路径 .，并把安装名称设为 organize-bilingual-literature。
安装到当前用户的 .agents/skills/organize-bilingual-literature 目录。
先阅读仓库说明并检查已有同名 Skill；已有时先比较差异，不要直接覆盖。
保留 SKILL.md、agents 以及仓库附带的 scripts、references、assets 等目录。
完成后报告来源版本和实际安装位置，并检查 Skill 能否被识别。
```

此方式适用于 Mac 和 Windows，由 Agent 根据当前系统处理路径。新 Skill 未出现时，先开一个新对话；仍未出现再重启客户端。

### 手动安装（可选，需要 Git）

Mac 终端：

```sh
mkdir -p "$HOME/.agents/skills"
git clone https://github.com/Kys75/organize-bilingual-literature.git "$HOME/.agents/skills/organize-bilingual-literature"
```

Windows PowerShell：

```powershell
New-Item -ItemType Directory -Force "$HOME/.agents/skills" | Out-Null
git clone https://github.com/Kys75/organize-bilingual-literature.git "$HOME/.agents/skills/organize-bilingual-literature"
```

最终应直接存在 `.agents/skills/organize-bilingual-literature/SKILL.md`。已有同名目录时先比较版本，不要删除或覆盖已有改动。

## 使用示例

```text
请使用 $organize-bilingual-literature，把我提供的这份论文整理到当前项目目录。保留原始文件，按原文逐段制作中英对照笔记，保存图片并添加中文读图提示。先确认能读取哪些材料；不能取得的部分请明确说明。
```

默认产物位于当前工作目录下的 `YY-MM-DD中文标题/`：原始资料、以 `.bilingual.md` 结尾的双语笔记以及 `figures/` 图片目录。默认完整处理实质正文；如果只需要摘要或某一节，请在请求中明确范围。

## 依赖

附带的结构检查脚本需要 Python 3.10 或更新版本，仅使用标准库。下载网页、读取 PDF、提取图片需要当前 Agent 具备相应工具和文件/网络访问能力；这些工具不包含在本仓库中。处理 PDF 时可以另行使用 [OpenAI PDF Skill](https://github.com/openai/skills/tree/main/skills/.curated/pdf)，按实际任务补齐依赖。

## 检查方法与边界

在本仓库或已安装的 Skill 目录中运行；把示例文件路径替换为自己的文件。使用本机有效的 Python 命令：通常 Mac 为 `python3`，Windows 为 `python` 或 `py`。

```sh
python scripts/validate_bilingual_note.py "path/to/note.bilingual.md"
```

退出码 `0` 表示没有检测到所检查的结构错误，仍可能有警告；`1` 表示检查失败。脚本检查部分 Markdown 结构、公式分隔符、图片路径、引文转义与图注/读图提示数量。

**它不验证翻译准确性、全文覆盖率或所有模板占位符。** 发布或交付前仍需对照原文检查完整性，替换模板中的 `{{...}}`，并逐条处理警告；不要只凭 `OK` 宣布全文整理完成。

## 资源

- [输出规范](references/output-spec.md)
- [笔记模板](assets/bilingual-note-template.md)
- [结构检查脚本](scripts/validate_bilingual_note.py)

## 更新

请 Agent 对比已安装版本与本仓库的改动，再更新需要的文件；保留本地定制。维护者在本仓库修改源文件，安装目录只是使用副本。安装或更新后记录使用的提交版本，并做一次小任务验证。

当前发布检查覆盖 Skill 结构、资源链接和本机 Python 脚本行为；没有把这些检查等同于所有模型和所有操作系统上的完整任务验收。
