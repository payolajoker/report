---
book_title: "1·2기 신도시 종합평가 연구 (Ⅱ) - 신도시 주민의 삶 -"
slug: "newtown-resident-life-evaluation"
section_id: "source-page-index"
section_title: "Source Page Index"
source_pdf: "../../sources/OTKCRK210996.pdf"
status: "complete"
---

# Source Page Index

본문 기준으로 원문 인쇄 페이지와 PDF 페이지는 대체로 24쪽 차이가 난다. 예를 들어 원문 인쇄 페이지 11쪽은 PDF 35쪽이다. 연구요약·차례·부록은 별도 구간으로 관리한다.

| 구간 | Markdown | PDF 페이지 | 원문 인쇄 페이지 | 비고 |
|---|---|---:|---:|---|
| 표지·서지·연구진 | [00-front-matter.md](./00-front-matter.md) | 1-4 | - | 표지, 판권, 연구진 |
| 연구요약 | [01-summary.md](./01-summary.md) | 5-14 | 연구요약 1-10 | 주요 결론 요약 |
| 목차·표차례·그림차례 | [00-front-matter.md](./00-front-matter.md) | 15-24 | 차례 1-10 | 목차, 표 차례, 그림 차례 |
| 제1장 | [02-chapter-1-research-issues.md](./02-chapter-1-research-issues.md) | 25-34 | 3-10 | 연구이슈 및 선행연구 |
| 제2장 | [03-chapter-2-resident-satisfaction.md](./03-chapter-2-resident-satisfaction.md) | 35-130 | 11-106 | 주민 만족도 및 영향요인 |
| 제3장 | [04-chapter-3-text-mining-resident-perception.md](./04-chapter-3-text-mining-resident-perception.md) | 131-210 | 107-186 | 비정형데이터 주민 인식 |
| 제4장 | [05-chapter-4-policy-planning-suggestions.md](./05-chapter-4-policy-planning-suggestions.md) | 211-226 | 187-202 | 정책 및 계획 제언 |
| 부록 | [06-appendix.md](./06-appendix.md) | 227-240 | 203-214 | 설문지 |
| 참고문헌 | [07-references.md](./07-references.md) | 241-243 | 217-219 | 참고문헌 |

## 보존된 페이지 이미지

전체 PDF 243쪽을 `assets/pages/` 아래에 PDF 페이지 단위 JPEG로 보존했다. 파일명은 `pdf-page-001.jpg`부터 `pdf-page-243.jpg`까지 이어진다.

| 범위 | 파일 패턴 |
|---|---|
| PDF 1-243쪽 | `assets/pages/pdf-page-001.jpg` ... `assets/pages/pdf-page-243.jpg` |

## 처리 메모

- OCR은 사용하지 않았다.
- 장별 본문은 PDF embedded text layer와 렌더링 페이지 이미지를 대조해 재구성했다.
- 원문 텍스트층 추출본은 [text-layer/](./text-layer/)에 보존했다.
- 넓은 설문·통계 표와 그래프는 핵심 수치를 Markdown 표로 옮기고, 원문 전체 대조는 페이지 이미지와 text-layer 보존본으로 연결했다.
