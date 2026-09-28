# Bilingual Obsidian output specification

## Folder layout

```text
<current-workspace>/
└── YY-MM-DD中文标题/
    ├── <original scholarly source>.pdf
    ├── <English title>.bilingual.md
    └── figures/
        ├── Fig1.png
        ├── Fig2.png
        └── ...
```

Keep non-PDF originals in their native format. If the input is an HTML lecture and a stable PDF can be generated without losing content, save both the source URL in frontmatter and the PDF snapshot.

## Frontmatter

Use only fields supported by known metadata. Quote string values.

```yaml
---
source: "canonical URL or source description"
arxiv: "2607.19295"
format: "English paragraph followed by Chinese paragraph"
note: "正文与附录主体逐段中英对照；参考文献列表从略；已嵌入原始图片并附中文读图提示"
---
```

For a non-arXiv source, omit `arxiv`. For Chinese-first material, change `format` accordingly.

## Opening block

```markdown
# Full English Title（完整中文标题）

arXiv:... | Subject or venue（中文）| Date

Author One, Author Two, and Author Three
```

Use one title heading, one metadata line, and one author line. Keep personal names in their original spelling.

## Headings and paragraphs

Use one bilingual heading node:

```markdown
## Abstract（摘要）

English source paragraph.

对应的完整中文翻译。

### 2.2 Experiments（实验）
```

Do not write two adjacent headings such as `## Abstract` and `## 摘要`. Preserve the source heading levels and numbering. For Chinese-first material, use `中文（English）`.

Do not label ordinary paragraphs with “English” or “中文”. Preserve paragraph boundaries unless a source artifact makes the boundary genuinely ambiguous. Do not reduce complete paragraphs to summaries.

## Equations, citations, and links

- Use `$...$` for inline math and paired `$$` blocks for display math.
- Preserve equation numbers with `\tag{n}` where supported.
- Explain symbols only when the source explains them; translation may add a minimal parenthetical clarification for an unavoidable beginner-facing term.
- Escape numeric citations: `\[1\]`, `\[3,4\]`, `\[10-13\]`.
- Use normal Markdown image links, not Obsidian wiki embeds:

  ```markdown
  ![Figure 2 / 图 2](figures/Fig2.png)
  ```

- Preserve a user-added Obsidian width hint inside image alt text if editing an existing note.

## Figures

Each figure block has four parts:

```markdown
![Figure 2 / 图 2](figures/Fig2.png)

**Figure 2.** Faithful English caption.

**图 2。** 忠实的中文图注。

**读图提示。** 用一段连续中文先说明这幅图在讲什么，再带初学者完成适合这幅图的观察动作，并解释理解它所必需的“图像特征—含义”联系。
```

The reading guide must not merely paraphrase the caption or list what appears in the image. There is no universal sequence of experimental control, measurement, calibration, inference, and confirmation. Choose the smallest reading path that fits the figure.

Apply these universal principles selectively:

1. **Role:** Identify what the figure contributes in context: a definition, structure, mechanism, procedure, comparison, trend, spatial pattern, classification, parameter regime, derivation aid, or evidence for a claim.
2. **Vocabulary:** Explain only the panels, labels, symbols, colors, line styles, annotations, scales, or other encodings needed to follow that contribution. Resolve ambiguous notation from the source rather than from appearance alone.
3. **Viewing actions:** Tell the reader what to do with the image—such as trace a path, match components, compare cases, locate a boundary or feature, follow a trend, count objects, or inspect scale and contrast. Use only actions that the figure supports.
4. **Interpretive bridge:** Explain any non-obvious link between a visible feature and its meaning. Distinguish what is drawn or plotted from what the authors infer when an inference is involved. If the figure is descriptive or definitional, explain correspondence, organization, or function instead of forcing a causal argument.
5. **Structure:** Connect panels when one supplies context, input, calibration, continuation, or confirmation for another. If the panels are parallel examples or independent views, say so or treat them separately.
6. **Takeaway:** End with the main understanding the reader should retain. This may be a conclusion, a way to use the diagram, a structural relationship, or a recognition cue; it need not be an experimental claim.

Select a figure-appropriate route rather than filling every category:

- **Experimental or observational data:** explain axes and encodings, identify the meaningful comparison or trend, and state what the data support. Discuss controls, calibration, uncertainty, or confounders only when present.
- **Theory or simulation:** explain assumptions or varied parameters, outputs, regimes, limiting behavior, and what relation or prediction the plot demonstrates.
- **Schematic, apparatus, or workflow:** explain components, connections, direction or sequence, information or material flow, and the purpose of the arrangement.
- **Microscopy, spatial image, field map, or photograph:** explain scale, color or contrast, annotations, spatial features, and what pattern or object the reader is meant to recognize.
- **Phase diagram or parameter map:** explain axes, regions, boundaries, trajectories, and how moving through the map changes the regime.
- **Mathematical, geometric, or conceptual diagram:** explain the objects and constraints, their relationships, and the role the picture plays in the definition, construction, or argument.

These routes are examples, not an exhaustive taxonomy. Never invent a control variable, measured quantity, calibration, causal mechanism, uncertainty, or panel dependency merely to make the paragraph look complete.

If a figure is purely decorative or a title-page logo, do not treat it as a scientific figure.

## Tables

For a compact table, translate headers within the same cell:

```markdown
| Quantity（物理量） | Value（数值） |
|---|---|
```

For a large or layout-sensitive table, embed a high-resolution image, then add an English caption, Chinese caption, and a short `**读表提示。**` paragraph.

## Papers versus lectures

Papers normally contain title, metadata, authors, abstract, numbered body, conclusions, appendices, and references note.

Lectures may omit abstract, authors, venue, citations, or bibliography. Preserve pedagogical structures:

- `Definition 2（定义 2）`
- `Theorem 1（定理 1）`
- `Example（例题）`
- `Exercise 3（习题 3）`
- `Solution（解答）`

Do not fabricate missing paper metadata for a lecture. Do not omit exercises merely because they are not prose.

## References ending

When the original source is stored locally:

```markdown
## References（参考文献）

The full reference list is omitted here; citation numbers are retained in the bilingual text. See the accompanying original source for complete bibliographic information.

完整参考文献列表在此从略，但双语正文保留引用编号；完整书目信息请参见同目录原始文件。
```

Include the full bibliography only if the user asks or if omitting it would prevent identification of sources.
