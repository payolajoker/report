---
book_title: "도시·공간 트렌드 2024 : 서울메트로폴리탄을 중심으로"
slug: "city-space-trends-2024"
section_id: "source-page-index"
section_title: "Source Page Index"
source_pdf: "../../sources/OTKCRK240315.pdf"
status: "complete"
---

# Source Page Index

PDF 페이지와 원문 인쇄 페이지는 본문 기준으로 32쪽 차이가 난다. 예를 들어 원문 인쇄 페이지 1쪽은 PDF 33쪽이다.

| 구간 | Markdown | PDF 페이지 | 원문 인쇄 페이지 | 비고 |
|---|---|---:|---:|---|
| 표지·서지 | [00-front-matter.md](./00-front-matter.md) | 1-4 | - | 표지, 판권, 연구진 |
| 목차·표차례·그림차례 | [00-front-matter.md](./00-front-matter.md) | 23-32 | xix-xxvii | 목차, 표 차례, 그림 차례 |
| 연구요약 | [01-summary.md](./01-summary.md) | 5-21 | i-xvii | 주요 결론 요약 |
| 제1장 | [02-chapter-1-introduction.md](./02-chapter-1-introduction.md) | 33-42 | 1-10 | 서론 |
| 제2장 | [03-chapter-2-social-urban-growth.md](./03-chapter-2-social-urban-growth.md) | 43-60 | 11-28 | 사회 및 도시성장 변화 |
| 제3장 | [04-chapter-3-institutional-trends-lh.md](./04-chapter-3-institutional-trends-lh.md) | 61-108 | 29-76 | 제도기반 트렌드와 LH |
| 제4장 | [05-chapter-4-seoul-metropolitan-trend-change.md](./05-chapter-4-seoul-metropolitan-trend-change.md) | 109-148 | 77-116 | 서울메트로폴리탄 변화 분석 |
| 제5장 | [06-chapter-5-trends-2024.md](./06-chapter-5-trends-2024.md) | 149-174 | 117-142 | 2024 트렌드 키워드 |
| 제6장 | [07-chapter-6-lh-application.md](./07-chapter-6-lh-application.md) | 175-200 | 143-168 | LH사업 적용방안 |
| 제7장 | [08-chapter-7-conclusion.md](./08-chapter-7-conclusion.md) | 201-206 | 169-174 | 결론 |
| 참고문헌·부록 | [09-references-appendix.md](./09-references-appendix.md) | 207-215 | 175-183 | 참고문헌, 건축상 부록 |

## 보존된 페이지 이미지

전체 PDF 215쪽을 `assets/pages/` 아래에 PDF 페이지 단위 JPEG로 보존했다. 파일명은 `pdf-page-001.jpg`부터 `pdf-page-215.jpg`까지 이어진다. 장별 재구성 Markdown은 핵심 그림 페이지만 직접 링크하고, 전체 원문 시각 확인은 이 페이지 이미지 자산을 사용한다.

| 범위 | 파일 패턴 |
|---|---|
| PDF 1-215쪽 | `assets/pages/pdf-page-001.jpg` ... `assets/pages/pdf-page-215.jpg` |

## 처리 메모

- OCR은 사용하지 않았다.
- 장별 본문은 PDF embedded text layer와 렌더링 페이지 이미지를 대조해 재구성했다.
- 원문 텍스트층 추출본은 [text-layer/](./text-layer/)에 보존했다.
- 표는 본문에서 핵심 내용을 Markdown 표로 재정리하고, 넓은 원문 표는 페이지 이미지와 text-layer 보존본에서 대조할 수 있게 했다.
