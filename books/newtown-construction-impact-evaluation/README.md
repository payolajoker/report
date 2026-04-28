# 1·2기 신도시 종합평가 연구 (Ⅰ) - 신도시 건설의 영향 -

PDF 원문을 LLM이 읽고 인용하기 쉬운 Markdown 구조로 재구성한 책 폴더다. OCR은 사용하지 않았고, PDF 내장 텍스트층과 480쪽 전체 페이지 이미지를 함께 보존했다.

## 빠른 링크

- [문서 인덱스](./docs/newtown-construction-impact-evaluation/index.md)
- [주요 수치](./docs/newtown-construction-impact-evaluation/stats.md)
- [source page index](./docs/newtown-construction-impact-evaluation/source-page-index.md)
- [기계처리용 manifest](./docs/newtown-construction-impact-evaluation/manifest.yml)
- [LLM 단일 번들](./dist/newtown-construction-impact-evaluation.llm.md)
- [JSON manifest](./dist/newtown-construction-impact-evaluation.manifest.json)
- [원본 PDF](./sources/OTKCRK210995.pdf)
- [전체 페이지 이미지](./docs/newtown-construction-impact-evaluation/assets/pages/)
- [텍스트층 원문 보존본](./docs/newtown-construction-impact-evaluation/text-layer/)

## 구성

| 경로 | 설명 |
|---|---|
| `docs/newtown-construction-impact-evaluation/` | 장별 Markdown, 통계 인덱스, source page index, manifest |
| `docs/newtown-construction-impact-evaluation/assets/pages/` | PDF 1-480쪽 JPEG 보존본 |
| `docs/newtown-construction-impact-evaluation/text-layer/` | OCR이 아닌 PDF 내장 텍스트층 페이지별 보존본 |
| `dist/` | RAG·긴 컨텍스트용 단일 Markdown 번들 및 JSON manifest |
| `sources/` | 원본 PDF |

## 처리 메모

- OCR 미사용.
- Python을 PDF 처리·변환에 사용하지 않음.
- 장·절 제목은 Markdown 헤더로 승격.
- 핵심 수치와 중요 표는 Markdown 표로 정리.
- 넓은 표·그래프·지도는 원문 페이지 이미지로 대조 가능하게 보존.
