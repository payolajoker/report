# Pangyo Transcription Guide

Book title: 판교신도시 마스터 플랜 및 디자인 총람

Source PDF: `sources/OTKNTC070432.pdf`

Slug: `pangyo-newtown-master-plan-design-book`

Method: visual review only. Do not use OCR tools. `pdftotext` confirms the PDF has no useful embedded text layer.

## Shared Rules

- Write only the assigned batch file and, if useful, one assigned note file.
- Do not edit `index.md`, `manifest.yml`, `stats.md`, `source-page-index.md`, `dist/*`, or another worker's batch.
- Use source markers for every page or small group of pages: `## PDF p.XXX`.
- Link page images with the Markdown image pattern shown in code: `![PDF page 001]` plus `(../assets/pages/pdf-page-001.jpg)` from a batch file.
- Capture readable headings, project names, captions, maps, diagrams, schedule dates, block names, household counts, floor counts, area figures, and other quantitative facts.
- For dense diagrams or unreadable microtext, describe the visible purpose and mark details as visually dense rather than guessing.
- Keep Korean titles as shown where legible. English labels may be retained when printed.
- This is an LLM/RAG archive, so prefer accurate structure and source references over ornamental prose.

## Main Structure From Contents

- `00` front matter: PDF pp.001-009
- `01` 판교신도시 개요: PDF pp.010-037
- `02` 동판교 마스터 플랜: PDF pp.038-055
- `03` 판교신도시 건축계획안: PDF pp.056-331
  - 건축계획의 방향: starts p.056
  - 현상설계 프로젝트: starts p.060
  - 국제설계경기 프로젝트: starts p.182
  - 턴키 프로젝트: starts p.228
  - 민간사업 프로젝트: starts p.322
  - 판교신도시 개발 현황: starts p.328

## Batch File Pattern

Use this frontmatter:

```yaml
---
book_title: "판교신도시 마스터 플랜 및 디자인 총람"
slug: "pangyo-newtown-master-plan-design-book"
section_id: "batch-XXX"
section_title: "<range title>"
source_pdf: "../../../sources/OTKNTC070432.pdf"
source_pages: "AAA-BBB"
status: "visual-reviewed"
ocr: false
---
```

Then add:

- `# <range title>`
- short coverage note
- page-by-page or project-by-project notes
- `## Key Figures And Tables`
- `## Stats Candidates`
- `## Validation Notes`

## Assigned Batches

Each batch covers 10 PDF pages except the final one.

| Batch | Pages | File |
|---|---:|---|
| batch-001 | 001-010 | `transcription/batch-001-pages-001-010.md` |
| batch-002 | 011-020 | `transcription/batch-002-pages-011-020.md` |
| batch-003 | 021-030 | `transcription/batch-003-pages-021-030.md` |
| batch-004 | 031-040 | `transcription/batch-004-pages-031-040.md` |
| batch-005 | 041-050 | `transcription/batch-005-pages-041-050.md` |
| batch-006 | 051-060 | `transcription/batch-006-pages-051-060.md` |
| batch-007 | 061-070 | `transcription/batch-007-pages-061-070.md` |
| batch-008 | 071-080 | `transcription/batch-008-pages-071-080.md` |
| batch-009 | 081-090 | `transcription/batch-009-pages-081-090.md` |
| batch-010 | 091-100 | `transcription/batch-010-pages-091-100.md` |
| batch-011 | 101-110 | `transcription/batch-011-pages-101-110.md` |
| batch-012 | 111-120 | `transcription/batch-012-pages-111-120.md` |
| batch-013 | 121-130 | `transcription/batch-013-pages-121-130.md` |
| batch-014 | 131-140 | `transcription/batch-014-pages-131-140.md` |
| batch-015 | 141-150 | `transcription/batch-015-pages-141-150.md` |
| batch-016 | 151-160 | `transcription/batch-016-pages-151-160.md` |
| batch-017 | 161-170 | `transcription/batch-017-pages-161-170.md` |
| batch-018 | 171-180 | `transcription/batch-018-pages-171-180.md` |
| batch-019 | 181-190 | `transcription/batch-019-pages-181-190.md` |
| batch-020 | 191-200 | `transcription/batch-020-pages-191-200.md` |
| batch-021 | 201-210 | `transcription/batch-021-pages-201-210.md` |
| batch-022 | 211-220 | `transcription/batch-022-pages-211-220.md` |
| batch-023 | 221-230 | `transcription/batch-023-pages-221-230.md` |
| batch-024 | 231-240 | `transcription/batch-024-pages-231-240.md` |
| batch-025 | 241-250 | `transcription/batch-025-pages-241-250.md` |
| batch-026 | 251-260 | `transcription/batch-026-pages-251-260.md` |
| batch-027 | 261-270 | `transcription/batch-027-pages-261-270.md` |
| batch-028 | 271-280 | `transcription/batch-028-pages-271-280.md` |
| batch-029 | 281-290 | `transcription/batch-029-pages-281-290.md` |
| batch-030 | 291-300 | `transcription/batch-030-pages-291-300.md` |
| batch-031 | 301-310 | `transcription/batch-031-pages-301-310.md` |
| batch-032 | 311-320 | `transcription/batch-032-pages-311-320.md` |
| batch-033 | 321-330 | `transcription/batch-033-pages-321-330.md` |
| batch-034 | 331-331 | `transcription/batch-034-pages-331-331.md` |
