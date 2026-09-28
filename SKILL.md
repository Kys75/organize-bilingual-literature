---
name: organize-bilingual-literature
description: Archive academic papers, arXiv links, literature URLs, PDFs, lecture notes, and similar scholarly sources into the current workspace as complete bilingual Obsidian notes. Use when Codex needs to download or copy a source, create a date-plus-Chinese-title folder, preserve the original file, translate the full body paragraph by paragraph, extract every figure, add bilingual captions and beginner-friendly Chinese reading guides, and validate Obsidian Markdown.
---

# Organize Bilingual Literature

Turn one scholarly source into a self-contained bilingual reading folder in the active workspace. Treat papers and lectures as variants of the same workflow; preserve their native structure instead of forcing one into the other's schema.

## Required resources

Read [references/output-spec.md](references/output-spec.md) before drafting the note. Use [assets/bilingual-note-template.md](assets/bilingual-note-template.md) as the starting skeleton when useful. Run `scripts/validate_bilingual_note.py` before completion.

## Workflow

1. **Resolve the destination.**
   - Use the current working directory as the archive root. Never hardcode a previous workspace.
   - Inspect a small sample of nearby literature folders and bilingual notes for local naming conventions. Do not change unrelated files.
   - Use the local date and create `YY-MM-DD中文标题`. Translate the source title faithfully and compactly. Replace path separators with safe punctuation.
   - Reuse the same folder if it already represents this source; do not create numbered duplicates.

2. **Acquire and verify the source.**
   - Accept a local file, arXiv abstract/PDF link, DOI landing page, ordinary literature URL, or lecture URL.
   - For arXiv, resolve the canonical abstract page, record the arXiv ID/version and metadata, download the PDF, and obtain TeX source when available.
   - For other URLs, prefer the author/publisher's downloadable original. Preserve the source filename unless a clear English title filename is more useful.
   - For local files, copy the source into the new folder unless it is already there.
   - Verify file type, page count, title, and integrity before translation. Do not invent inaccessible text.

3. **Classify the material.**
   - Paper: preserve abstract, numbered sections, appendices, acknowledgements/data statements, equations, tables, and in-text citation numbers.
   - Lecture or course note: preserve the learning order, definitions, propositions/theorems, derivations, examples, warnings, exercises, and solutions if present.
   - Primarily English source: place each English unit first and its Chinese translation immediately after it.
   - Primarily Chinese source: place each Chinese unit first and its English translation immediately after it, unless the user requests English-first.

4. **Extract every figure.**
   - Prefer original figure assets from TeX/source archives. Otherwise extract or crop from the PDF at high resolution.
   - Preserve each complete figure as composed by the author, including multi-panel figures. Include main-text and appendix/supplementary figures.
   - Store images under `figures/` with stable descriptive names. Inspect every output visually for cropping, blur, or missing labels.
   - Keep rendered previews, source archives, and extraction intermediates in an operating-system temporary directory. Remove them after inspection; do not leave preview or scratch folders in the archive root.
   - Preserve complex tables as Markdown when practical; use a high-resolution image when faithful reconstruction would be worse.

5. **Write the full bilingual note.**
   - Follow [references/output-spec.md](references/output-spec.md) exactly.
   - Translate the complete substantive text paragraph by paragraph. Do not silently summarize, merge, or omit paragraphs.
   - Keep each heading on one line as `English（中文）`; never create separate English and Chinese heading nodes.
   - List authors once in their original spelling. Do not add a translated duplicate.
   - Preserve equations in renderable LaTeX and retain equation numbers when present.
   - Escape numeric citations as `\[1\]`, `\[3,4\]`, or `\[10-13\]` so Obsidian displays them as plain text.
   - After every Chinese figure caption, add exactly one Chinese paragraph beginning `**读图提示。**`. Make it a guided reading of that particular figure, not an inventory of visible elements or a paraphrase of the caption.
   - First determine the figure's actual job in its source context—for example, defining notation, showing a setup or process, comparing cases, displaying a trend or spatial pattern, mapping regimes, illustrating a derivation, or presenting evidence. Do not force an experimental-data template onto other kinds of figures.
   - Decode only the labels and visual encodings needed for the main reading path. Resolve ambiguous notation from the caption and surrounding text rather than guessing from typography.
   - Give the beginner concrete, figure-appropriate viewing actions: trace, match, compare, locate, follow, count, or inspect scale and contrast as relevant. Whenever the meaning of a visible feature is not self-evident, explain the source-supported link between the feature and its interpretation. If the figure is descriptive or definitional rather than inferential, explain its organization, correspondence, or function instead of inventing a causal claim.
   - Connect panels only when the source makes them logically dependent; otherwise explain their distinct roles without manufacturing a single chain. Mention controls, measured quantities, calibration, uncertainty, or confounders only when they actually exist and matter to the reading.
   - End with the smallest useful takeaway: what the reader should now understand, recognize, or be able to infer from this figure. Ground every interpretation in the figure, caption, and surrounding source text, and mark genuine ambiguity instead of inventing a mechanism.
   - Omit the full bibliography by default when the original file is saved locally, but retain all in-text citation numbers and add a short references note.

6. **Validate and inspect.**
   - Run:

     ```bash
     python3 scripts/validate_bilingual_note.py "/absolute/path/to/note.bilingual.md"
     ```

   - Resolve every error. Review warnings instead of ignoring them.
   - Confirm the number of embedded figures equals the number intended from the source, including appendix figures.
   - Check formula delimiters, image links, heading hierarchy, citation escaping, caption/reading-guide counts, and source-file presence.
   - Audit each reading guide for fit: remove any control, measurement, calibration, comparison, causal link, or cross-panel dependency that the figure does not contain. For every non-obvious interpretation that remains, confirm that the visible feature and the source context support it.
   - Open the finished note or inspect representative sections to ensure it reads correctly in Obsidian.

7. **Report the result.**
   - Link the new folder, source file, bilingual note, and figures directory.
   - State the verified page count and figure count. Mention any unavailable source component or deliberate omission.

## Quality bar

- Be faithful before being elegant: technical meaning, qualifiers, units, symbols, and uncertainty must survive translation.
- Define specialized terms naturally on first use; do not turn the translation into a separate lecture.
- Make reading guides genuinely instructional but brief: one coherent paragraph per figure, using the reading path appropriate to that figure rather than a fixed template.
- Never claim “complete translation” if substantive source passages were summarized or omitted.
- Do not add speculative research commentary unless the user asks.
