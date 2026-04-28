# 1·2기 신도시 종합평가 연구 (Ⅱ) - 신도시 주민의 삶 - - LLM Bundle

- Slug: `newtown-resident-life-evaluation`
- Status: `complete`
- Source PDF: `../sources/OTKCRK210996.pdf`
- OCR used: `false`
- Text source: embedded PDF text layer, checked against rendered pages by visual/manual review
- PDF processing with Python: `false`
- Visual assets: `../docs/newtown-resident-life-evaluation/assets/pages/` (243 page images)
- Text-layer archive: `../docs/newtown-resident-life-evaluation/text-layer/`

이 파일은 RAG/긴 컨텍스트 입력용 단일 번들이다. 각 섹션은 원본 PDF 페이지 범위를 frontmatter와 본문 주석으로 보존하며, 정리본의 링크는 이 `dist/` 폴더 기준 상대 경로로 조정했다.

## Table of Contents

1. 1·2기 신도시 종합평가 연구 (Ⅱ) - 신도시 주민의 삶 - - `docs/newtown-resident-life-evaluation/index.md`
2. 주요 수치 인덱스 - `docs/newtown-resident-life-evaluation/stats.md`
3. Source Page Index - `docs/newtown-resident-life-evaluation/source-page-index.md`
4. 표지·발간정보·목차 - `docs/newtown-resident-life-evaluation/00-front-matter.md`
5. 연구요약 - `docs/newtown-resident-life-evaluation/01-summary.md`
6. 제1장 연구이슈 및 선행연구 고찰 - `docs/newtown-resident-life-evaluation/02-chapter-1-research-issues.md`
7. 제2장 신도시 주민 만족도 및 영향요인 평가 - `docs/newtown-resident-life-evaluation/03-chapter-2-resident-satisfaction.md`
8. 제3장 비정형데이터를 활용한 신도시 주민활동 및 인식조사 - `docs/newtown-resident-life-evaluation/04-chapter-3-text-mining-resident-perception.md`
9. 제4장 신도시 정책 및 계획의 제언 - `docs/newtown-resident-life-evaluation/05-chapter-4-policy-planning-suggestions.md`
10. 부록 - `docs/newtown-resident-life-evaluation/06-appendix.md`
11. 참고문헌 - `docs/newtown-resident-life-evaluation/07-references.md`
12. PDF 텍스트층 원문 보존본 - `docs/newtown-resident-life-evaluation/text-layer/README.md`

---

<!-- BEGIN docs/newtown-resident-life-evaluation/index.md -->

---
book_title: "1·2기 신도시 종합평가 연구 (Ⅱ) - 신도시 주민의 삶 -"
slug: "newtown-resident-life-evaluation"
source_pdf: "../../sources/OTKCRK210996.pdf"
pdf_pages: 243
status: "complete"
processing:
  ocr_used: false
  visual_assets: "all 243 PDF pages rendered as JPEG page images"
  text_layer_archive: "./text-layer/"
---

# 1·2기 신도시 종합평가 연구 (Ⅱ) - 신도시 주민의 삶 -

- 원본 PDF: [OTKCRK210996.pdf](../sources/OTKCRK210996.pdf)
- 발행: 한국토지주택공사 토지주택연구원, 연구기획 2021-93호
- 저자: 윤정중, 최상희, 최대식, 윤정란, 진규남, 권오준, 송태호
- 처리 방식: OCR 미사용. PDF 내장 텍스트 레이어와 렌더링 페이지 이미지를 대조해 장별 재구성 Markdown을 만들고, 전체 243쪽을 JPEG 이미지로 보존했다.
- LLM 통합본: [newtown-resident-life-evaluation.llm.md](./newtown-resident-life-evaluation.llm.md)

## 빠른 링크

- [주요 수치 인덱스](../docs/newtown-resident-life-evaluation/stats.md)
- [source page index](../docs/newtown-resident-life-evaluation/source-page-index.md)
- [기계처리용 manifest](../docs/newtown-resident-life-evaluation/manifest.yml)
- [전체 페이지 이미지 자산](../docs/newtown-resident-life-evaluation/assets/pages/)
- [텍스트층 원문 보존본](../docs/newtown-resident-life-evaluation/text-layer/)

## 문서 구조

| ID | 파일 | PDF 페이지 | 원문 인쇄 페이지 | 내용 |
|---:|---|---:|---:|---|
| 00 | [표지·발간정보·목차](../docs/newtown-resident-life-evaluation/00-front-matter.md) | 1-4, 15-24 | front, 차례 1-10 | 서지, 연구진, 목차, 표·그림 차례 |
| 01 | [연구요약](../docs/newtown-resident-life-evaluation/01-summary.md) | 5-14 | 연구요약 1-10 | 연구 목적, 설문조사·텍스트마이닝 결과 요약 |
| 02 | [제1장 연구이슈 및 선행연구 고찰](../docs/newtown-resident-life-evaluation/02-chapter-1-research-issues.md) | 25-34 | 3-10 | 연구배경, 이슈, 방법, 선행연구 |
| 03 | [제2장 신도시 주민 만족도 및 영향요인 평가](../docs/newtown-resident-life-evaluation/03-chapter-2-resident-satisfaction.md) | 35-130 | 11-106 | 1,600명 설문, 주거만족도, 통근·생활권, GIS 분석 |
| 04 | [제3장 비정형데이터를 활용한 신도시 주민활동 및 인식조사](../docs/newtown-resident-life-evaluation/04-chapter-3-text-mining-resident-perception.md) | 131-210 | 107-186 | 맘카페·부동산카페·민원·언론 텍스트마이닝 |
| 05 | [제4장 신도시 정책 및 계획의 제언](../docs/newtown-resident-life-evaluation/05-chapter-4-policy-planning-suggestions.md) | 211-226 | 187-202 | 국토·수도권·신도시 정책, 거버넌스, 충족도 개선안 |
| 06 | [부록](../docs/newtown-resident-life-evaluation/06-appendix.md) | 227-240 | 203-214 | 신도시 주민 거주만족도 조사 설문지 |
| 07 | [참고문헌](../docs/newtown-resident-life-evaluation/07-references.md) | 241-243 | 217-219 | 참고문헌 |

## 핵심 관점

이 책은 1·2기 신도시를 공급자 성과가 아니라 **주민의 거주 경험**으로 평가한다. 분당·일산·동탄·운정을 대상으로 설문조사와 텍스트마이닝을 결합해, 신도시가 주거안정·생활권·장소성·공동체·교통·시설 접근성 측면에서 어떤 성과와 한계를 보였는지 정리한다.

## 처리 품질

- 장·절 구조는 Markdown 헤더로 승격했다.
- 핵심 수치와 표는 Markdown 표로 재구성했다.
- 그래프·지도·도식은 캡션만 남기지 않고 원문 대조용 PDF 페이지 이미지를 보존했다.
- 원문 전체 텍스트층 추출본은 `text-layer/`에 보존했다.

<!-- END docs/newtown-resident-life-evaluation/index.md -->

<!-- BEGIN docs/newtown-resident-life-evaluation/stats.md -->

---
book_title: "1·2기 신도시 종합평가 연구 (Ⅱ) - 신도시 주민의 삶 -"
slug: "newtown-resident-life-evaluation"
section_id: "stats"
section_title: "주요 수치 인덱스"
source_pdf: "../../sources/OTKCRK210996.pdf"
status: "complete"
---

# 주요 수치 인덱스

| 주제 | 수치 | 의미 | Source |
|---|---:|---|---|
| PDF 전체 | 243쪽 | 원본 PDF 총 페이지 수 | `OTKCRK210996.pdf`, pdfinfo |
| 조사 대상 신도시 | 4개 | 분당, 일산, 동탄, 운정 | [제2장](../docs/newtown-resident-life-evaluation/03-chapter-2-resident-satisfaction.md), PDF p.35 |
| 설문 표본 | 1,600명 | 만 20세 이상 거주민 조사 | [제2장](../docs/newtown-resident-life-evaluation/03-chapter-2-resident-satisfaction.md), PDF p.35 |
| 설문 방식 | 온라인 1,031명 / 대면 569명 | 코로나 확산으로 온라인·대면 병행 | [제2장](../docs/newtown-resident-life-evaluation/03-chapter-2-resident-satisfaction.md), PDF p.35 |
| 설문 문항 | 3개 영역, 24개 항목 | 사전질문·응답자 일반사항 포함 32개 | [제2장](../docs/newtown-resident-life-evaluation/03-chapter-2-resident-satisfaction.md), PDF p.36 |
| 온라인 조사 기간 | 2020.12.10-2020.12.31 | 온라인 패널 조사 | [제2장](../docs/newtown-resident-life-evaluation/03-chapter-2-resident-satisfaction.md), PDF p.36 |
| 대면 조사 기간 | 2021.01.18-2021.02.05 | 현장 대면 조사 | [제2장](../docs/newtown-resident-life-evaluation/03-chapter-2-resident-satisfaction.md), PDF p.36 |
| 회수 표본 | 분당 500, 일산 500, 동탄 300, 운정 300 | 신도시별 회수 표본 | [제2장](../docs/newtown-resident-life-evaluation/03-chapter-2-resident-satisfaction.md), PDF p.39 |
| 모집단 | 993,780명 | 조사대상 지역 만 20세 이상 인구 | [제2장](../docs/newtown-resident-life-evaluation/03-chapter-2-resident-satisfaction.md), PDF p.37 |
| 신도시별 모집단 | 분당 282,786 / 일산 227,930 / 동탄 142,978 / 운정 261,173명 | 주민등록인구통계 2020년 10월 기준 | [제2장](../docs/newtown-resident-life-evaluation/03-chapter-2-resident-satisfaction.md), PDF p.37 |
| 평균 거주기간 | 분당 9.7년 / 일산 9.9년 / 동탄 4.2년 / 운정 6.6년 | 1기 신도시가 2기보다 장기 거주 | [제2장](../docs/newtown-resident-life-evaluation/03-chapter-2-resident-satisfaction.md), PDF p.54 |
| 동탄 2년 미만 거주 | 34% | 타 신도시보다 짧은 거주기간 | [연구요약](../docs/newtown-resident-life-evaluation/01-summary.md), PDF p.6 |
| 전용면적 만족도 | 분당 61.0 / 일산 66.8 / 동탄 69.2 / 운정 67.8점 | 2기 신도시 주택면적 만족도가 높음 | [제2장](../docs/newtown-resident-life-evaluation/03-chapter-2-resident-satisfaction.md), PDF p.61 |
| 욕실개수 만족도 | 동탄 73.8점 / 분당 63.0점 | 동탄 최고, 분당 최저 | [제2장](../docs/newtown-resident-life-evaluation/03-chapter-2-resident-satisfaction.md), PDF p.59 |
| 분당 주거환경 만족도 최고 항목 | 공원녹지 79.4점 | 보건의료 77.4점, 쇼핑판매 77.3점 | [제2장](../docs/newtown-resident-life-evaluation/03-chapter-2-resident-satisfaction.md), PDF p.62 |
| 일산 주거환경 만족도 최고 항목 | 공원녹지 76.9점 | 쇼핑판매 76.8점, 보건의료 75.4점 | [제2장](../docs/newtown-resident-life-evaluation/03-chapter-2-resident-satisfaction.md), PDF p.63 |
| 동탄 주거환경 만족도 최고 항목 | 학교 73.1점 | 공원녹지 72.4점, 위생청결 71.7점 | [제2장](../docs/newtown-resident-life-evaluation/03-chapter-2-resident-satisfaction.md), PDF p.64 |
| 운정 주거환경 만족도 최고 항목 | 공원녹지 77.6점 | 위생청결 72.7점, 소음먼지 70.3점 | [제2장](../docs/newtown-resident-life-evaluation/03-chapter-2-resident-satisfaction.md), PDF p.65 |
| 통근·통학 비율 | 분당 78.4% / 동탄 73.7% / 운정 72.3% / 일산 68.8% | 통근·통학 수행 비율 | [제2장](../docs/newtown-resident-life-evaluation/03-chapter-2-resident-satisfaction.md), PDF p.83 |
| 거주지역 내 통근·통학 | 약 50% | 신도시 및 모도시 내부 통근·통학 | [제2장](../docs/newtown-resident-life-evaluation/03-chapter-2-resident-satisfaction.md), PDF p.83 |
| 평균 통근·통학 시간 | 43.4분 | 편도 기준 | [제2장](../docs/newtown-resident-life-evaluation/03-chapter-2-resident-satisfaction.md), PDF p.86 |
| 동탄 통근·통학 시간 | 48.8분 | 4개 신도시 중 가장 김 | [제2장](../docs/newtown-resident-life-evaluation/03-chapter-2-resident-satisfaction.md), PDF p.86 |
| 통근수단 | 분당 대중교통 56.9%, 일산 대중교통 48.8%, 동탄 자가용 54.3%, 운정 자가용 50.2% | 1기는 대중교통, 2기는 자가용 비중이 높음 | [제2장](../docs/newtown-resident-life-evaluation/03-chapter-2-resident-satisfaction.md), PDF p.85 |
| 생활필수품 지역 내 이용 | 약 95% 내외 | 대다수 생활필수품은 거주지역에서 해결 | [제2장](../docs/newtown-resident-life-evaluation/03-chapter-2-resident-satisfaction.md), PDF p.87 |
| 문화여가 지역 내 이용 | 80% 이상 | 문화·여가시설의 지역 내 서비스 비율 | [제2장](../docs/newtown-resident-life-evaluation/03-chapter-2-resident-satisfaction.md), PDF p.88 |
| 의료시설 지역 내 이용 | 분당 93.2% / 일산 93.0% / 동탄 91.3% / 운정 76.5% | 운정의 외부 의료 이용 의존도가 높음 | [제2장](../docs/newtown-resident-life-evaluation/03-chapter-2-resident-satisfaction.md), PDF p.89 |
| 쇼핑 지역 내 이용 | 일산 93.2% / 동탄 77.6% | 일산 최고, 동탄 최저 | [제2장](../docs/newtown-resident-life-evaluation/03-chapter-2-resident-satisfaction.md), PDF p.90 |
| 대표 랜드마크 대분류 | 분당 공원녹지 37.9% / 일산 쇼핑판매 34.7% / 동탄 공원녹지 44.2% / 운정 공원녹지 40.4% | 지역별 대표 장소 인식 | [제2장](../docs/newtown-resident-life-evaluation/03-chapter-2-resident-satisfaction.md), PDF p.92 |
| 공동체 소속감 | 분당 65.4% / 일산 71.8% / 동탄 55.3% / 운정 72.3% | 현재 거주지역 구성원 소속감·공동체의식 | [제2장](../docs/newtown-resident-life-evaluation/03-chapter-2-resident-satisfaction.md), PDF p.95 |
| 비정형데이터 분석기간 | 2018.01.01-2020.09.30 | 텍스트마이닝 분석 기간 | [제3장](../docs/newtown-resident-life-evaluation/04-chapter-3-text-mining-resident-perception.md), PDF p.133 |
| 비정형데이터 전체 추출 정보량 | 638,808건 | 언론·카페·민원 총량 | [제3장](../docs/newtown-resident-life-evaluation/04-chapter-3-text-mining-resident-perception.md), PDF p.133 |
| 언론 채널 정보량 | 20,390건 | 네이버 포털 기사 | [제3장](../docs/newtown-resident-life-evaluation/04-chapter-3-text-mining-resident-perception.md), PDF p.133 |
| 카페·민원 정보량 | 618,418건 | 맘카페·부동산카페·민원 게시판 | [제3장](../docs/newtown-resident-life-evaluation/04-chapter-3-text-mining-resident-perception.md), PDF p.133 |
| 2기 신도시 내집마련 이주사유 | 30% 이상 | 2기 신도시의 자가취득 기회 제공 효과 | [제3장](../docs/newtown-resident-life-evaluation/04-chapter-3-text-mining-resident-perception.md), PDF p.203 |
| 2기 신도시 타지역 전입 | 60% 내외 | 최근 조성 신도시의 외부 전입 비율 | [제3장](../docs/newtown-resident-life-evaluation/04-chapter-3-text-mining-resident-perception.md), PDF p.203 |
| 전세·월세에서 자가로 상향이동 | 30% 내외 | 주거안정성 측면의 효과 | [제3장](../docs/newtown-resident-life-evaluation/04-chapter-3-text-mining-resident-perception.md), PDF p.203 |
| 수도권 인구비율 | 1980년 35.5% / 1990년 42.8% / 2000년 46.3% / 2010년 49.1% / 2019년 50% 초과 | 신도시 정책과 국토균형 이슈 | [제4장](../docs/newtown-resident-life-evaluation/05-chapter-4-policy-planning-suggestions.md), PDF p.213 |
| 현행 자족성 기준 | 입주 완료 후 10년 내 직주균형지수 90% | 지속가능한 신도시 계획기준의 자족성 확보 기준 | [제4장](../docs/newtown-resident-life-evaluation/05-chapter-4-policy-planning-suggestions.md), PDF p.218 |

## 신도시별 주변지역 서비스 생활권

| 활동 | 분당 | 일산 | 동탄 | 운정 | Source |
|---|---|---|---|---|---|
| 통근통학 | 강남 | 강남, 파주 | 수원 | 고양 | [제3장](../docs/newtown-resident-life-evaluation/04-chapter-3-text-mining-resident-perception.md), PDF p.206 |
| 생활필수품 | 용인, 강남 | 파주, 마포 | 수원, 용인 | 고양 | [제3장](../docs/newtown-resident-life-evaluation/04-chapter-3-text-mining-resident-perception.md), PDF p.206 |
| 문화여가 | 강남, 종로 | 강남, 마포 | 강남, 수원 | 고양, 마포 | [제3장](../docs/newtown-resident-life-evaluation/04-chapter-3-text-mining-resident-perception.md), PDF p.206 |
| 의료 | 강남, 송파 | 서대문, 종로 | 수원, 강남 | 고양, 서대문 | [제3장](../docs/newtown-resident-life-evaluation/04-chapter-3-text-mining-resident-perception.md), PDF p.206 |
| 쇼핑 | 강남, 용인 | 파주, 강남 | 수원, 용인 | 고양, 중구 | [제3장](../docs/newtown-resident-life-evaluation/04-chapter-3-text-mining-resident-perception.md), PDF p.206 |
| 교육 | 강남, 서초 | 강남, 서대문 | 수원, 강남 | 고양, 서대문 | [제3장](../docs/newtown-resident-life-evaluation/04-chapter-3-text-mining-resident-perception.md), PDF p.206 |

<!-- END docs/newtown-resident-life-evaluation/stats.md -->

<!-- BEGIN docs/newtown-resident-life-evaluation/source-page-index.md -->

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
| 표지·서지·연구진 | [00-front-matter.md](../docs/newtown-resident-life-evaluation/00-front-matter.md) | 1-4 | - | 표지, 판권, 연구진 |
| 연구요약 | [01-summary.md](../docs/newtown-resident-life-evaluation/01-summary.md) | 5-14 | 연구요약 1-10 | 주요 결론 요약 |
| 목차·표차례·그림차례 | [00-front-matter.md](../docs/newtown-resident-life-evaluation/00-front-matter.md) | 15-24 | 차례 1-10 | 목차, 표 차례, 그림 차례 |
| 제1장 | [02-chapter-1-research-issues.md](../docs/newtown-resident-life-evaluation/02-chapter-1-research-issues.md) | 25-34 | 3-10 | 연구이슈 및 선행연구 |
| 제2장 | [03-chapter-2-resident-satisfaction.md](../docs/newtown-resident-life-evaluation/03-chapter-2-resident-satisfaction.md) | 35-130 | 11-106 | 주민 만족도 및 영향요인 |
| 제3장 | [04-chapter-3-text-mining-resident-perception.md](../docs/newtown-resident-life-evaluation/04-chapter-3-text-mining-resident-perception.md) | 131-210 | 107-186 | 비정형데이터 주민 인식 |
| 제4장 | [05-chapter-4-policy-planning-suggestions.md](../docs/newtown-resident-life-evaluation/05-chapter-4-policy-planning-suggestions.md) | 211-226 | 187-202 | 정책 및 계획 제언 |
| 부록 | [06-appendix.md](../docs/newtown-resident-life-evaluation/06-appendix.md) | 227-240 | 203-214 | 설문지 |
| 참고문헌 | [07-references.md](../docs/newtown-resident-life-evaluation/07-references.md) | 241-243 | 217-219 | 참고문헌 |

## 보존된 페이지 이미지

전체 PDF 243쪽을 `assets/pages/` 아래에 PDF 페이지 단위 JPEG로 보존했다. 파일명은 `pdf-page-001.jpg`부터 `pdf-page-243.jpg`까지 이어진다.

| 범위 | 파일 패턴 |
|---|---|
| PDF 1-243쪽 | `assets/pages/pdf-page-001.jpg` ... `assets/pages/pdf-page-243.jpg` |

## 처리 메모

- OCR은 사용하지 않았다.
- 장별 본문은 PDF embedded text layer와 렌더링 페이지 이미지를 대조해 재구성했다.
- 원문 텍스트층 추출본은 [text-layer/](../docs/newtown-resident-life-evaluation/text-layer/)에 보존했다.
- 넓은 설문·통계 표와 그래프는 핵심 수치를 Markdown 표로 옮기고, 원문 전체 대조는 페이지 이미지와 text-layer 보존본으로 연결했다.

<!-- END docs/newtown-resident-life-evaluation/source-page-index.md -->

<!-- BEGIN docs/newtown-resident-life-evaluation/00-front-matter.md -->

---
book_title: "1·2기 신도시 종합평가 연구 (Ⅱ) - 신도시 주민의 삶 -"
slug: "newtown-resident-life-evaluation"
section_id: "00"
section_title: "표지·발간정보·목차"
source_pdf: "../../sources/OTKCRK210996.pdf"
source_pages: "1-4, 15-24"
status: "complete"
---

# 표지·발간정보·목차

## 서지 정보

| 항목 | 내용 |
|---|---|
| 제목 | 1·2기 신도시 종합평가 연구 (Ⅱ) - 신도시 주민의 삶 - |
| 영문 제목 | A Study on the Comprehensive Evaluation of the first and second Phase of New-towns |
| 연구번호 | 연구기획 2021-93호 |
| 발행처 | 한국토지주택공사 토지주택연구원 |
| 발행인 | 허남일 |
| 저자 | 윤정중, 최상희, 최대식, 윤정란, 진규남, 권오준, 송태호 |
| 원본 PDF | [OTKCRK210996.pdf](../sources/OTKCRK210996.pdf) |
| 원문 페이지 이미지 | [assets/pages/](../docs/newtown-resident-life-evaluation/assets/pages/) |
| 텍스트층 보존본 | [text-layer/](../docs/newtown-resident-life-evaluation/text-layer/) |

## 연구진

| 역할 | 인물 |
|---|---|
| 연구총괄 | 윤정중 |
| 연구책임 | 최상희 |
| 공동연구진 | 최대식, 윤정란, 진규남, 권오준, 송태호 |
| 외부원고 집필 | 이창연 |
| 위탁용역 | 케이스탯리서치, 알에스엔 |

## 장별 목차

| 장 | 제목 | 원문 인쇄 페이지 | PDF 페이지 | Markdown |
|---:|---|---:|---:|---|
| 요약 | 연구요약 | 1-10 | 5-14 | [01-summary.md](../docs/newtown-resident-life-evaluation/01-summary.md) |
| 1 | 연구이슈 및 선행연구 고찰 | 3-10 | 25-34 | [02-chapter-1-research-issues.md](../docs/newtown-resident-life-evaluation/02-chapter-1-research-issues.md) |
| 2 | 신도시 주민 만족도 및 영향요인 평가 | 11-106 | 35-130 | [03-chapter-2-resident-satisfaction.md](../docs/newtown-resident-life-evaluation/03-chapter-2-resident-satisfaction.md) |
| 3 | 비정형데이터를 활용한 신도시 주민활동 및 인식조사 | 107-186 | 131-210 | [04-chapter-3-text-mining-resident-perception.md](../docs/newtown-resident-life-evaluation/04-chapter-3-text-mining-resident-perception.md) |
| 4 | 신도시 정책 및 계획의 제언 | 187-202 | 211-226 | [05-chapter-4-policy-planning-suggestions.md](../docs/newtown-resident-life-evaluation/05-chapter-4-policy-planning-suggestions.md) |
| 부록 | 신도시 주민 거주만족도 조사 설문지 | 203-214 | 227-240 | [06-appendix.md](../docs/newtown-resident-life-evaluation/06-appendix.md) |
| 참고문헌 | 참고문헌 | 217-219 | 241-243 | [07-references.md](../docs/newtown-resident-life-evaluation/07-references.md) |

## 표·그림 구성

이 책은 설문조사 표와 통계모형 표가 매우 많다. 최종 Markdown에서는 핵심 통계와 계획적 판단에 필요한 표를 재구성했고, 전체 원문 표·그래프는 다음 방식으로 보존했다.

- 주요 수치는 [stats.md](../docs/newtown-resident-life-evaluation/stats.md)에 별도 색인화했다.
- 모든 원문 페이지는 [assets/pages/](../docs/newtown-resident-life-evaluation/assets/pages/)에 JPEG로 보존했다.
- 텍스트층 원문 표와 그림 차례는 [text-layer/00-front-matter.md](../docs/newtown-resident-life-evaluation/text-layer/00-front-matter.md)에 보존했다.

## 육안 확인 페이지

- [PDF page 001](../docs/newtown-resident-life-evaluation/assets/pages/pdf-page-001.jpg): 표제
- [PDF page 015](../docs/newtown-resident-life-evaluation/assets/pages/pdf-page-015.jpg): 목차 시작
- [PDF page 035](../docs/newtown-resident-life-evaluation/assets/pages/pdf-page-035.jpg): 제2장 시작과 설문조사 개요

<!-- END docs/newtown-resident-life-evaluation/00-front-matter.md -->

<!-- BEGIN docs/newtown-resident-life-evaluation/01-summary.md -->

---
book_title: "1·2기 신도시 종합평가 연구 (Ⅱ) - 신도시 주민의 삶 -"
slug: "newtown-resident-life-evaluation"
section_id: "01"
section_title: "연구요약"
source_pdf: "../../sources/OTKCRK210996.pdf"
source_pages: "5-14"
status: "complete"
---

# 연구요약

## 연구 목적

이 권은 1·2기 신도시를 공급량, 집값, 정책목표 달성률만으로 보지 않고 **실제로 거주하는 주민의 삶**으로 평가한다. 핵심 질문은 신도시가 주민에게 어떤 지역성·장소성·거주만족·공동체 경험을 만들었는가이다.

연구는 이용후평가(POE) 관점을 확장해 다음을 본다.

| 질문 | 의미 |
|---|---|
| 이주 이후 주거환경은 개선되었는가 | 신도시가 주거안정과 삶의 질을 높였는지 확인 |
| 주민은 어떤 생활권을 형성했는가 | 서울·모도시·인접 신도시와의 연결을 확인 |
| 어떤 시설이 만족도에 영향을 주는가 | 공원, 학교, 체육시설, 치안방범, 문화시설 등 시설별 영향 확인 |
| 온라인 담론은 무엇을 말하는가 | 맘카페·부동산카페·민원·언론에서 나타난 주민 인식 확인 |

## 조사 방법

| 방법 | 대상·규모 | 주요 내용 |
|---|---:|---|
| 설문조사 | 분당, 일산, 동탄, 운정 주민 총 1,600명 | 주거만족도, 이주특성, 통근통학, 생활권, 랜드마크, 공동체 의식 |
| GIS 연계 분석 | 설문 응답자 위치와 도시계획시설 접근성 | 시설 접근성과 만족도 간 관계 |
| 텍스트마이닝 | 언론, 맘카페, 부동산카페, 민원게시판 | 주요 현안, 주거만족, 이주사유, 랜드마크, 공동체 |

## 설문조사 주요 결과

| 항목 | 요약 |
|---|---|
| 거주기간 | 분당·일산은 평균 9.6년 수준으로 오래 거주하고, 동탄 4.2년·운정 6.6년은 상대적으로 짧다. |
| 주거만족도 | 1기는 공원녹지 등 도시환경 만족도가 높고, 2기는 주택면적 등 주택 자체 만족도가 높다. |
| 낮은 만족 항목 | 1기는 소음·먼지, 2기는 문화예술 만족도가 낮게 나타난다. |
| 이주 특성 | 분양·내집마련 목적, 전세에서 자가로의 점유형태 변화가 주요 흐름이다. |
| 통근·통학 | 분당 78.4%, 동탄 73.7%, 운정 72.3%, 일산 68.8%가 통근·통학을 한다. |
| 생활권 | 생필품은 대부분 거주지역 내부에서 해결되며, 1기는 서울 의존, 2기는 경기지역 의존이 상대적으로 높다. |
| 랜드마크 | 분당 중앙공원, 일산 호수공원, 동탄 호수공원, 운정 호수공원 등 공원녹지가 대표 장소로 인식된다. |
| 공동체 | 50% 이상이 현재 거주지역 구성원으로서 소속감과 공동체 의식을 가진다. |

## 접근성과 만족도

주택만족도는 가족 수와 소득이 높을수록 올라가는 경향이 있고, 자가 소유자의 만족도가 높다. 시설 접근성과 만족도는 모든 시설에서 단순한 정비례가 아니다.

| 시설·조건 | 해석 |
|---|---|
| 학교 | 보행권 내 입지하면 만족도가 높아진다. |
| 체육시설 | 가까울수록 만족도가 올라가는 경향이 있다. |
| 치안방범 | 설치기준 내에 있으면 만족도가 높아진다. |
| 문화시설 | 2기 신도시는 접근성이 좋아도 만족도는 낮게 나타난다. |
| 병원 | 접근성보다 서비스 질 관리가 더 중요할 수 있다. |

## 텍스트마이닝 주요 결과

온라인 커뮤니티와 민원·언론 데이터는 설문조사가 잘 잡지 못하는 생활 감각을 보여준다.

| 주제 | 결과 |
|---|---|
| 주요 언급 주제 | 주거환경시설, 생활활동, 주택구조, 주택유형, 점유형태, 주거환경 순 |
| 3기 신도시 발표 반응 | 부동산카페와 민원게시판에서 교통·부동산가격 관련 언급이 증가 |
| 주택구조 불만 | 분당·일산은 곰팡이, 누수, 결로, 난방 등 노후주택 문제가 많이 언급 |
| 이주사유 | 부동산 가치, 맞벌이·영유아 양육, 학군, 신혼·내집마련이 반복적으로 등장 |
| 공동체 | 맘카페는 보육·쇼핑·공원여가·생활정보 공유와 지역문화 형성의 장으로 기능 |

## 계획적 시사점

1기 신도시는 노후주택 리모델링, 주차·소음·먼지 등 생활환경 개선이 중요하다. 2기 신도시는 대중교통 접근성, 문화시설, 학교·복지시설, 초기 입주 불편의 보완이 중요하다.

향후 3기 신도시와 신규택지 계획에서는 다음이 필요하다.

| 방향 | 내용 |
|---|---|
| 수요자 맞춤형 공급 | 내집마련, 양육, 학군, 출퇴근, 가족돌봄을 함께 고려 |
| 주변지역 연계 | 신도시 주변 1·2기 신도시와 기반시설·기능을 분담 |
| 생활 SOC 선공급 | 단지와 외부환경을 초기부터 완성도 있게 조성 |
| 공원녹지 고도화 | 공원 접근성과 여가·상업·전시 등 복합 이용 패턴 반영 |
| 시설 접근성과 서비스 병행 | 학교·체육·치안은 접근성, 병원·문화는 서비스 질까지 관리 |

## 관련 원문 이미지

- [PDF page 005](../docs/newtown-resident-life-evaluation/assets/pages/pdf-page-005.jpg): 연구요약 시작
- [PDF page 006](../docs/newtown-resident-life-evaluation/assets/pages/pdf-page-006.jpg): 거주특성·만족도 요약
- [PDF page 009](../docs/newtown-resident-life-evaluation/assets/pages/pdf-page-009.jpg): 텍스트마이닝 결과 요약
- [PDF page 013](../docs/newtown-resident-life-evaluation/assets/pages/pdf-page-013.jpg): 계획적 시사점

<!-- END docs/newtown-resident-life-evaluation/01-summary.md -->

<!-- BEGIN docs/newtown-resident-life-evaluation/02-chapter-1-research-issues.md -->

---
book_title: "1·2기 신도시 종합평가 연구 (Ⅱ) - 신도시 주민의 삶 -"
slug: "newtown-resident-life-evaluation"
section_id: "02"
section_title: "제1장 연구이슈 및 선행연구 고찰"
source_pdf: "../../sources/OTKCRK210996.pdf"
source_pages: "25-34"
status: "complete"
---

# 제1장 연구이슈 및 선행연구 고찰

## 1. 연구배경 및 목적

기존 신도시 평가는 정책목표 달성도, 주택공급 효과, 집값 안정, 주변지역 파급효과처럼 공급자·거시 지표에 집중했다. 이 장은 그런 접근만으로는 신도시 주민의 실제 삶을 설명하기 어렵다고 본다.

이 연구의 목적은 다음과 같다.

| 목적 | 설명 |
|---|---|
| 주민 관점 평가 | 신도시에 사는 사람의 만족도, 장소성, 지역성, 공동체를 평가한다. |
| 이용후평가 확장 | 건설 후 실제 거주 경험을 통해 계획의 성과와 한계를 본다. |
| 3기 신도시 환류 | 1·2기 신도시 경험을 3기 신도시 계획기준과 운영방안에 반영한다. |

## 2. 연구의 이슈 및 범위

연구는 공급자 관점의 물량·계획 성과가 아니라 주민의 생활 경험을 통해 신도시를 본다. 주요 이슈는 주거안정, 이주, 만족도, 시설 접근성, 생활권, 장소성, 공동체, 온라인 인식이다.

| 연구이슈 | 조사 내용 |
|---|---|
| 주거 안정성 | 신도시 이주가 전세·월세에서 자가로의 상향이동을 만들었는지 |
| 거주 만족도 | 주택, 주거환경, 시설 만족도가 지역·가구특성에 따라 어떻게 다른지 |
| 접근성 | 학교, 공원, 병원, 쇼핑, 문화, 체육, 치안방범 시설 접근성이 만족도에 미치는 영향 |
| 생활권 | 통근·통학, 생필품, 의료, 쇼핑, 교육, 문화여가의 지역 내외 이용 |
| 장소성 | 주민이 대표 랜드마크로 인식하는 장소 |
| 공동체 | 지역 활동 참여, 소속감, 온라인 커뮤니티의 역할 |

## 2.1 연구방법 및 범위

연구 대상은 1기 신도시 분당·일산, 2기 신도시 동탄·운정이다. 각 신도시는 입지 특성과 조성시기를 고려해 선정되었다.

방법은 크게 두 갈래다.

| 방법 | 역할 |
|---|---|
| 설문조사 | 정량적으로 주거만족도, 이주특성, 생활활동, 공동체 의식을 파악 |
| 비정형데이터 분석 | 맘카페, 부동산카페, 민원게시판, 언론 데이터로 주민 인식과 지역 이슈를 파악 |

이 조합의 장점은 설문이 잡는 공식적 응답과 온라인 담론이 드러내는 생활 감각을 함께 볼 수 있다는 점이다.

## 3. 선행연구 고찰 및 차별성

선행연구는 주거만족도, 도시환경, 신도시 성과, 거주자 특성 등을 다루었지만, 대체로 설문 중심이거나 시설·주택 단위의 만족도에 머물렀다. 이 연구는 여기에 비정형데이터와 GIS 접근성 분석을 더해, 주거만족도를 주민 생활권과 온라인 공동체까지 넓혀 본다.

| 차별점 | 의미 |
|---|---|
| 주민 관점 | 정책효과를 주민의 체감과 삶의 질로 재해석 |
| 설문 + 텍스트마이닝 | 정량 응답과 온라인 담론을 함께 분석 |
| GIS 접근성 | 시설의 물리적 거리와 만족도 관계를 실증 |
| 3기 신도시 연결 | 기존 신도시 평가를 신규택지 계획으로 환류 |

## 관련 원문 이미지

- [PDF page 025](../docs/newtown-resident-life-evaluation/assets/pages/pdf-page-025.jpg): 제1장 표지
- [PDF page 027](../docs/newtown-resident-life-evaluation/assets/pages/pdf-page-027.jpg): 연구배경 및 목적
- [PDF page 029](../docs/newtown-resident-life-evaluation/assets/pages/pdf-page-029.jpg): 연구이슈 정의와 조사내용
- [PDF page 030](../docs/newtown-resident-life-evaluation/assets/pages/pdf-page-030.jpg): 설문조사와 비정형데이터 분석방법

<!-- END docs/newtown-resident-life-evaluation/02-chapter-1-research-issues.md -->

<!-- BEGIN docs/newtown-resident-life-evaluation/03-chapter-2-resident-satisfaction.md -->

---
book_title: "1·2기 신도시 종합평가 연구 (Ⅱ) - 신도시 주민의 삶 -"
slug: "newtown-resident-life-evaluation"
section_id: "03"
section_title: "제2장 신도시 주민 만족도 및 영향요인 평가"
source_pdf: "../../sources/OTKCRK210996.pdf"
source_pages: "35-130"
status: "complete"
---

# 제2장 신도시 주민 만족도 및 영향요인 평가

## 1. 조사내용 및 분석방법론

이 장은 분당·일산·동탄·운정 주민 1,600명을 대상으로 한 설문조사와 GIS 연계분석을 통해 신도시 주민의 만족도와 영향요인을 평가한다.

| 항목 | 내용 |
|---|---|
| 조사 대상 | 만 20세 이상 분당·일산·동탄·운정 거주민 |
| 표본 | 총 1,600명 |
| 방식 | 온라인 1,031명, 대면 569명 |
| 기간 | 온라인 2020.12.10-2020.12.31, 대면 2021.01.18-2021.02.05 |
| 문항 | 3개 영역 24개 항목, 사전질문·일반사항 포함 32개 |

### 표본 구성

| 신도시 | 회수 표본 | 성격 |
|---|---:|---|
| 분당 | 500명 | 1기, 성남권 |
| 일산 | 500명 | 1기, 고양권 |
| 동탄 | 300명 | 2기, 화성권 |
| 운정 | 300명 | 2기, 파주권 |

## 2. 주택 및 주거환경

### 2.1 거주특성

1기 신도시인 분당·일산은 오래 거주한 주민 비중이 높고, 2기 신도시인 동탄·운정은 상대적으로 거주기간이 짧다.

| 신도시 | 평균 거주기간 | 해석 |
|---|---:|---|
| 분당 | 9.7년 | 장기 거주·성숙도 높음 |
| 일산 | 9.9년 | 장기 거주·성숙도 높음 |
| 동탄 | 4.2년 | 최근 입주·정착 진행 중 |
| 운정 | 6.6년 | 2기 중 상대적으로 긴 거주 |

동탄은 거주 2년 미만 비율이 34%로 높아, 초기 입주와 정착의 불편이 만족도에 영향을 줄 가능성이 크다.

### 2.2 주택 만족도

주택 자체 만족도는 2기 신도시가 높게 나타난다. 특히 동탄은 욕실개수와 전용면적 만족도가 높고, 분당은 상대적으로 낮다. 이는 1기 신도시의 주택 노후와 2기 신도시의 새 주택 효과를 함께 보여준다.

| 항목 | 분당 | 일산 | 동탄 | 운정 | 해석 |
|---|---:|---:|---:|---:|---|
| 전용면적 만족도 | 61.0 | 66.8 | 69.2 | 67.8 | 2기 신도시가 높음 |
| 욕실개수 만족도 | 63.0 | - | 73.8 | - | 동탄 최고, 분당 최저 |

### 2.3 주거환경 만족도

도시환경 만족도는 1기 신도시가 상대적으로 높다. 특히 공원녹지는 모든 지역에서 강한 만족 요소로 반복된다.

| 신도시 | 높은 만족 항목 | 낮은 만족 항목·특징 |
|---|---|---|
| 분당 | 공원녹지 79.4, 보건의료 77.4, 쇼핑판매 77.3 | 소음·먼지 만족도 낮음 |
| 일산 | 공원녹지 76.9, 쇼핑판매 76.8, 보건의료 75.4 | 노후주택 관련 불만 존재 |
| 동탄 | 학교 73.1, 공원녹지 72.4, 위생청결 71.7 | 문화예술 58.9로 낮음 |
| 운정 | 공원녹지 77.6, 위생청결 72.7, 소음먼지 70.3 | 문화·학교·체육 접근성 보완 필요 |

## 3. 주거 이동성

이주사유는 분양·내집마련, 시설·설비 개선, 직장·학교 변동, 결혼·세대독립 등이 주요하게 나타난다. 2기 신도시는 내집마련 목적이 더 강하고, 타지역에서 들어온 비율도 높다.

핵심 해석은 다음과 같다.

| 관점 | 결과 |
|---|---|
| 주거안정 | 전세·월세에서 자가로의 상향이동 비율이 나타남 |
| 지역 내 이주 | 1기 신도시는 지역 내 이주 비율이 높음 |
| 외부 전입 | 2기 신도시는 타지역 전입 비율이 높음 |
| 주변지역 관계 | 분당은 성남·용인, 일산은 고양·서울 은평, 동탄은 수원·화성, 운정은 파주·고양과 연결 |

## 4. 생활활동과 네트워크

### 4.1 통근·통학

| 신도시 | 통근·통학 비율 | 주된 특징 |
|---|---:|---|
| 분당 | 78.4% | 서울, 특히 강남 연결 강함 |
| 동탄 | 73.7% | 경기도 내 다른 시·군, 특히 수원 연결 강함 |
| 운정 | 72.3% | 고양 연결 강함 |
| 일산 | 68.8% | 서울·파주 연결 |

통근·통학 수단은 1기와 2기의 차이가 분명하다.

| 신도시 | 자가용 | 대중교통 | 해석 |
|---|---:|---:|---|
| 분당 | 36.0% | 56.9% | 대중교통 중심 |
| 일산 | 39.8% | 48.8% | 대중교통 비중 높음 |
| 동탄 | 54.3% | 39.4% | 자가용 중심 |
| 운정 | 50.2% | 45.2% | 자가용 비중 높음 |

평균 통근·통학 시간은 43.4분이며, 동탄이 48.8분으로 가장 길다.

### 4.2 생활권

생활필수품은 약 95% 내외가 거주지역 안에서 해결된다. 문화여가와 쇼핑도 대체로 지역 내 이용 비중이 높지만, 의료·쇼핑·교육은 지역별 차이가 크다.

| 활동 | 주요 결과 |
|---|---|
| 생활필수품 | 대부분 거주지역 내부에서 해결 |
| 문화여가 | 지역 내 서비스 비율 80% 이상 |
| 의료 | 분당 93.2%, 일산 93.0%, 동탄 91.3%, 운정 76.5% |
| 쇼핑 | 일산 93.2%로 높고, 동탄 77.6%로 낮음 |
| 교육 | 1기는 서울 이용, 2기는 주변 경기 도시 이용이 상대적으로 많음 |

## 5. 랜드마크와 공동체 의식

주민이 떠올리는 신도시 대표 장소는 공원녹지, 쇼핑판매시설, 문화여가시설이다. 특히 공원은 단순 기반시설이 아니라 도시 정체성과 장소성을 만드는 핵심 자산으로 읽힌다.

| 신도시 | 대표 랜드마크 대분류 | 대표 장소 예시 |
|---|---:|---|
| 분당 | 공원녹지 37.9% | 분당중앙공원, 율동공원, 탄천 |
| 일산 | 쇼핑판매시설 34.7%, 공원녹지 33.3% | 호수공원, 킨텍스, 라페스타 |
| 동탄 | 공원녹지 44.2% | 호수공원, 메타폴리스, 동탄센트럴파크 |
| 운정 | 공원녹지 40.4% | 운정호수공원, 헤이리 예술마을, 이마트 |

공동체 소속감은 지역별로 차이가 있다.

| 신도시 | 소속감·공동체의식 있음 |
|---|---:|
| 분당 | 65.4% |
| 일산 | 71.8% |
| 동탄 | 55.3% |
| 운정 | 72.3% |

## 6. GIS 연계분석

응답자 위치와 시설 접근성을 결합해 만족도와의 관계를 분석했다. 결론은 “가까우면 무조건 만족도가 높다”가 아니라, 시설 유형별로 접근성의 의미가 다르다는 것이다.

| 시설 | 분석 해석 |
|---|---|
| 학교 | 보행권 내 입지할 때 만족도 상승 |
| 체육시설 | 접근성이 높을수록 만족도 상승 경향 |
| 치안방범 | 설치기준 내 입지 시 만족도 상승 |
| 문화시설 | 접근성이 좋아도 만족도가 낮은 경우 있음 |
| 병원 | 접근성보다 서비스 질·이용 경험 관리가 중요 |

## 관련 원문 이미지

- [PDF page 035](../docs/newtown-resident-life-evaluation/assets/pages/pdf-page-035.jpg): 설문조사 개요
- [PDF page 039](../docs/newtown-resident-life-evaluation/assets/pages/pdf-page-039.jpg): 목표표본 및 회수표본
- [PDF page 059](../docs/newtown-resident-life-evaluation/assets/pages/pdf-page-059.jpg): 욕실개수 만족도
- [PDF page 062](../docs/newtown-resident-life-evaluation/assets/pages/pdf-page-062.jpg): 분당 주거환경 만족도
- [PDF page 083](../docs/newtown-resident-life-evaluation/assets/pages/pdf-page-083.jpg): 통근·통학 여부 및 지역
- [PDF page 092](../docs/newtown-resident-life-evaluation/assets/pages/pdf-page-092.jpg): 신도시별 랜드마크 표
- [PDF page 100](../docs/newtown-resident-life-evaluation/assets/pages/pdf-page-100.jpg): 응답자 GIS 정보 연계 분석
- [PDF page 122](../docs/newtown-resident-life-evaluation/assets/pages/pdf-page-122.jpg): 시설 접근성과 만족도 분석

<!-- END docs/newtown-resident-life-evaluation/03-chapter-2-resident-satisfaction.md -->

<!-- BEGIN docs/newtown-resident-life-evaluation/04-chapter-3-text-mining-resident-perception.md -->

---
book_title: "1·2기 신도시 종합평가 연구 (Ⅱ) - 신도시 주민의 삶 -"
slug: "newtown-resident-life-evaluation"
section_id: "04"
section_title: "제3장 비정형데이터를 활용한 신도시 주민활동 및 인식조사"
source_pdf: "../../sources/OTKCRK210996.pdf"
source_pages: "131-210"
status: "complete"
---

# 제3장 비정형데이터를 활용한 신도시 주민활동 및 인식조사

## 1. 분석개요

이 장은 설문조사만으로는 보이지 않는 주민의 일상 언어와 지역 이슈를 비정형데이터로 분석한다. 대상 매체는 언론, 맘카페, 부동산카페, 지자체 민원게시판이다.

| 항목 | 내용 |
|---|---|
| 분석 대상 | 분당, 일산, 동탄, 운정 |
| 분석 기간 | 2018.01.01-2020.09.30 |
| 전체 추출 정보량 | 638,808건 |
| 언론 채널 | 20,390건 |
| 카페·민원게시판 | 618,418건 |

### 분석 항목

| 대분류 | 세부항목 |
|---|---|
| 신도시 주요 현안 | 매체별 정보량, 감성, 신도시 관심 현안, 지역별 언급 주제 |
| 주거만족도와 이주이유 | 주거만족도 언급 주제, 이주 사유, 주거지 선택요인 |
| 랜드마크와 공동체 | 주요 장소, 주변지역 네트워크, 공동체·연대의식 |

## 2. 신도시 주요 현안 분석

온라인 정보량은 1기보다 2기 신도시에서 상대적으로 많고, 특히 동탄의 정보량이 많다. 4개 지역 모두 맘카페 정보량이 많으며, 2020년에는 코로나19로 정보공유 활동이 증가했다.

3기 신도시 발표 이후에는 부동산카페와 민원게시판에서 정보량이 늘었다. 반면 맘카페는 정책 발표보다는 생활정보, 육아, 시설 이용, 지역 일상과 더 밀접한 흐름을 보인다.

| 매체 | 특징 |
|---|---|
| 언론 | 정책 발표와 부동산 이슈에 민감 |
| 부동산카페 | 3기 신도시, 가격, 교통호재, 개발 이슈 반응이 큼 |
| 맘카페 | 생활정보, 보육, 쇼핑, 공원여가, 공동체 활동 중심 |
| 민원게시판 | 교통·시설·개발 갈등 이슈가 직접적으로 표출 |

## 3. 주거만족도와 이주이유 분석

주거만족 관련 온라인 언급은 주거환경시설, 생활활동, 주택구조, 주택유형, 점유형태, 주거환경 순으로 많이 나타난다.

### 주택구조와 주거환경

| 주제 | 주요 인식 |
|---|---|
| 부대복리시설·단지면적·수납공간 | 상대적으로 긍정적 |
| 욕실·주택환경 | 부정 언급이 많음 |
| 분당·일산 | 곰팡이, 누수, 결로, 난방, 리모델링 등 노후주택 이슈 |
| 동탄·운정 | 교통, 초기 생활인프라, 학교·복지시설 보완 이슈 |

### 이주사유 LDA 토픽

| 토픽 | 주요 키워드 | 지역별 특징 |
|---|---|---|
| 부동산 가치 중시 | 매수, 역세권, 인프라, 상권, 재건축, 학군 | 모든 지역에서 반복 |
| 맞벌이·영유아 양육 | 보육, 등하원, 서울출퇴근, 직장맘, 전셋값 | 일산·동탄·운정에서 중요 |
| 학군 중시 | 초등학생, 전학, 배정학교, 중학생, 교육환경 | 분당·일산·동탄에서 도출 |
| 신혼·내집마련 | 신혼, 결혼, 전세만기, 출산, 집매매 | 분당·일산·운정에서 도출 |

## 4. 랜드마크와 지역 간 연계

온라인 텍스트에서도 병원, 학교, 공원, 마트처럼 일상생활과 밀접한 장소가 많이 거론된다. 그러나 지역을 대표하는 이미지로는 공원녹지가 강하게 작동한다.

### 주변지역 서비스 생활권

| 활동 | 분당 | 일산 | 동탄 | 운정 |
|---|---|---|---|---|
| 통근통학 | 강남 | 강남, 파주 | 수원 | 고양 |
| 생활필수품 | 용인, 강남 | 파주, 마포 | 수원, 용인 | 고양 |
| 문화여가 | 강남, 종로 | 강남, 마포 | 강남, 수원 | 고양, 마포 |
| 의료 | 강남, 송파 | 서대문, 종로 | 수원, 강남 | 고양, 서대문 |
| 쇼핑 | 강남, 용인 | 파주, 강남 | 수원, 용인 | 고양, 중구 |
| 교육 | 강남, 서초 | 강남, 서대문 | 수원, 강남 | 고양, 서대문 |

이 표는 신도시가 행정구역 안에서만 작동하지 않고, 생활서비스별로 주변 도시와 다른 방식으로 연결된다는 점을 보여준다.

## 5. 공동체 의식

설문조사에서는 공동체 활동 미참여 비율이 높지만, 온라인에서는 정보 공유와 지역 연대가 활발하게 나타난다. 부동산카페는 정책·개발·가격 이슈에 집단적으로 반응하고, 맘카페는 육아, 생활정보, 플리마켓, 지역 인증 활동처럼 일상 공동체를 만든다.

| 공동체 형태 | 특징 |
|---|---|
| 맘카페 | 생활정보, 보육, 쇼핑, 공원여가, 집콕 인증, 플리마켓 |
| 부동산카페 | 가격, 교통호재, 3기 신도시, 개발 대응 |
| 민원게시판 | 교통, 시설, 환경, 갈등 사안의 공식 표출 |

## 6. 설문조사와 텍스트마이닝 비교

설문조사는 주민의 평균적 만족도와 시설별 차이를 보여주고, 텍스트마이닝은 구체적인 불편·욕구·갈등 언어를 보여준다. 두 방법을 함께 보면 다음이 보인다.

| 비교 항목 | 해석 |
|---|---|
| 주거환경 | 설문에서는 공원녹지 만족도가 높고, 텍스트에서는 공세권·숲세권 등 부동산 가치 언어와 연결됨 |
| 주택 | 2기 주택 자체 만족도는 높지만, 층간소음·냄새·하자 등 생활문화 이슈가 등장 |
| 생활권 | 신도시 내부 충족도가 높지만, 의료·문화·교육·쇼핑은 주변 도시와 분담 |
| 공동체 | 공식 활동 참여는 낮아도 온라인 기반 공동체와 여론 형성은 활발 |

## 7. 계획적 시사점

신규택지와 3기 신도시는 단순 공급량이 아니라 주민 이주목적과 생활권을 함께 설계해야 한다. 특히 보육, 대중교통, 주변지역 기반시설 연계, 공원녹지 이용 패턴, 층간소음과 냄새 같은 주거문화 문제가 계획·운영 단계에서 다뤄져야 한다.

## 관련 원문 이미지

- [PDF page 131](../docs/newtown-resident-life-evaluation/assets/pages/pdf-page-131.jpg): 제3장 시작과 분석항목
- [PDF page 133](../docs/newtown-resident-life-evaluation/assets/pages/pdf-page-133.jpg): 분석기간 및 채널
- [PDF page 136](../docs/newtown-resident-life-evaluation/assets/pages/pdf-page-136.jpg): 매체별 정보량 추이
- [PDF page 144](../docs/newtown-resident-life-evaluation/assets/pages/pdf-page-144.jpg): 주제별 언급비중
- [PDF page 168](../docs/newtown-resident-life-evaluation/assets/pages/pdf-page-168.jpg): 이주연관이유 LDA 토픽
- [PDF page 173](../docs/newtown-resident-life-evaluation/assets/pages/pdf-page-173.jpg): 랜드마크 분석
- [PDF page 206](../docs/newtown-resident-life-evaluation/assets/pages/pdf-page-206.jpg): 주변지역 서비스 생활권

<!-- END docs/newtown-resident-life-evaluation/04-chapter-3-text-mining-resident-perception.md -->

<!-- BEGIN docs/newtown-resident-life-evaluation/05-chapter-4-policy-planning-suggestions.md -->

---
book_title: "1·2기 신도시 종합평가 연구 (Ⅱ) - 신도시 주민의 삶 -"
slug: "newtown-resident-life-evaluation"
section_id: "05"
section_title: "제4장 신도시 정책 및 계획의 제언"
source_pdf: "../../sources/OTKCRK210996.pdf"
source_pages: "211-226"
status: "complete"
---

# 제4장 신도시 정책 및 계획의 제언

## 1. 개요

제4장은 앞선 분석을 바탕으로 향후 신도시 정책과 계획기준을 어떻게 보완할지 제안한다. 핵심은 기존 신도시의 성과를 인정하되, 수도권 집중, 주변지역과의 관계, 주민 갈등, 자족성 개념, 주택·시설 운영의 한계를 함께 다루자는 것이다.

## 2. 국토 및 지역 관련 제언

### 2.1 국토-수도권-신도시 차원의 종합 공간정책

수도권 신도시는 수도권 주택문제를 해결하는 수단이지만, 동시에 비수도권에서 수도권으로 인구이동을 촉진할 수 있다. 따라서 신도시 정책은 국토균형발전 정책과 분리할 수 없다.

| 연도 | 수도권 인구비율 |
|---:|---:|
| 1980 | 35.5% |
| 1990 | 42.8% |
| 2000 | 46.3% |
| 2010 | 49.1% |
| 2019 | 50% 초과 |

정책 제언은 명확하다. 수도권 주택시장 안정은 수도권에 주택을 계속 공급하는 것만으로 해결되지 않고, 비수도권에서 수도권으로 이동하는 압력을 줄이는 국토균형 전략과 함께 다뤄야 한다.

### 2.2 기존도시와 공간적·기능적 연계

분당·일산은 기존 성남·고양 시가지와 섬처럼 분리된 측면이 있고, 판교도 서울과의 연결은 강하지만 성남시 구성원이라는 의식은 약한 편이다. 신도시가 기존 도시와 경쟁하거나 정서적으로 분리되지 않도록 기반시설, 생활권, 공동체 프로그램을 함께 설계해야 한다.

## 3. 신도시 개발 관련 제언

### 3.1 주변지역 연계 계획

신도시는 주변지역에서 인구와 기능을 끌어오기도 하고, 주변지역의 생활서비스를 이용하기도 한다. 특히 2기 신도시는 주변 도시에서 유입된 인구가 많고 아직 진행형이므로, 완료 이후 추가 평가가 필요하다.

| 과제 | 내용 |
|---|---|
| 산업·고용 연계 | 주변지역과 산업·고용 창출 전략을 함께 설계 |
| 기반시설 연계 | 주변 1·2기 신도시와 신규 신도시의 시설 분담 |
| 빨대효과 완화 | 주변지역 기능 약화를 막는 보완전략 필요 |

### 3.2 개발 거버넌스

신도시 개발은 수도권과 지방, 신도시 입지 도시와 비입지 도시, 기존 신도시 주민과 신규 신도시 주민, 원도심과 신도시 사이의 갈등을 만든다. 단기 민원 대응보다 사업단계별 거버넌스를 구축해야 한다.

필요한 거버넌스는 다음과 같다.

| 단계 | 필요 장치 |
|---|---|
| 정책 방향 | 국토균형발전과 주택공급의 상시 논의기구 |
| 개발이익 | 개발이익 환수와 활용방안 논의기구 |
| 사업 단계 | 신도시별 협의체와 이해관계자 소통 구조 |
| 운영 단계 | 주민 의견 모니터링과 시설·서비스 개선 환류 |

## 4. 자족성 개념 개선

기존 자족성은 일자리 중심의 경제적 자족성에 치우쳐 있다. 이 연구는 신도시 주민의 수요가 신도시 안에서 얼마나 충족되는지를 보는 **충족도** 개념을 제안한다.

| 구분 | 현행 | 개선 방향 |
|---|---|---|
| 평가 초점 | 직주균형, 종사자수, 자족용지 | 경제부문과 생활기반부문의 수요 충족 |
| 기준 | 입주 완료 후 10년 내 직주균형지수 90% | 충족도, 의존도, 지역기여효과를 함께 평가 |
| 계획 수단 | 자족용지 공급 | 자족용지 활성화, 유치업종, 생활편의시설 확충 |

충족도 관점은 일자리뿐 아니라 쇼핑·여가·생활서비스가 주민 수요를 얼마나 채우는지 본다. 이는 앞 장의 생활권 분석과 직접 연결된다.

## 5. 주택 계획 및 공급 관련 제언

신도시 공급은 물량 중심에서 수요자 맞춤형으로 이동해야 한다. 내집마련, 신혼, 양육, 학군, 맞벌이, 가족돌봄, 재택수요가 주택과 단지계획에 반영되어야 한다.

| 과제 | 내용 |
|---|---|
| 가구원수 반영 | 방 개수와 면적 기준을 가구원수·생애주기에 맞게 조정 |
| 재택수요 | 주택 내부의 다기능 공간 수요 반영 |
| 1기 신도시 | 리모델링, 노후주택, 주차, 소음, 결로 등 개선 |
| 2기 신도시 | 초기 교통·학교·복지·문화시설 보완 |

## 6. 도시계획시설 관련 제언

시설 계획은 단순 설치가 아니라 접근성과 서비스 품질을 함께 관리해야 한다.

| 시설 | 계획 방향 |
|---|---|
| 공원녹지 | 신도시 정체성과 장소성을 만드는 핵심시설로 접근성·복합이용 강화 |
| 학교 | 보행권 내 배치와 통학 안전성 확보 |
| 체육시설 | 접근성이 만족도와 연결되므로 생활권 단위 배치 |
| 치안방범 | 설치기준과 주민 체감 안전을 함께 관리 |
| 병원·문화시설 | 거리보다 서비스 질과 운영 프로그램 중요 |

## 7. 맺음말

이 책의 제언은 신도시를 “주택을 많이 넣는 공간”이 아니라 **주민의 생활권과 공동체가 작동하는 도시**로 보라는 데 모인다. 3기 신도시와 신규택지는 기존 1·2기 신도시의 교통, 자족성, 문화시설, 공원녹지, 노후화, 공동체 경험을 계획 초기부터 반영해야 한다.

## 관련 원문 이미지

- [PDF page 211](../docs/newtown-resident-life-evaluation/assets/pages/pdf-page-211.jpg): 제4장 개요
- [PDF page 213](../docs/newtown-resident-life-evaluation/assets/pages/pdf-page-213.jpg): 수도권 인구비율과 지역균형 이슈
- [PDF page 216](../docs/newtown-resident-life-evaluation/assets/pages/pdf-page-216.jpg): 신도시 개발 거버넌스
- [PDF page 217](../docs/newtown-resident-life-evaluation/assets/pages/pdf-page-217.jpg): 갈등관리를 위한 신도시 거버넌스 도식
- [PDF page 218](../docs/newtown-resident-life-evaluation/assets/pages/pdf-page-218.jpg): 자족성 확보 기준 개선안

<!-- END docs/newtown-resident-life-evaluation/05-chapter-4-policy-planning-suggestions.md -->

<!-- BEGIN docs/newtown-resident-life-evaluation/06-appendix.md -->

---
book_title: "1·2기 신도시 종합평가 연구 (Ⅱ) - 신도시 주민의 삶 -"
slug: "newtown-resident-life-evaluation"
section_id: "06"
section_title: "부록"
source_pdf: "../../sources/OTKCRK210996.pdf"
source_pages: "227-240"
status: "complete"
---

# 부록

## 신도시 주민 거주만족도 조사 설문지

부록은 설문조사 원문이다. 개인정보와 통계 비밀 보호 안내 뒤, 신도시 주민의 주택·주거환경, 주거 이동, 생활활동, 공동체, 응답자 일반사항을 묻는다.

| 영역 | 주요 문항 |
|---|---|
| 주택 및 주거환경 | 현재 주택 거주 시점, 주택유형, 점유형태, 방·욕실·면적 만족도, 공원·학교·쇼핑·의료·복지·문화·체육·치안·위생·소음 만족도 |
| 주거 이동 | 이전 거주지, 이전 주택유형·점유형태, 이주 이유, 거주여건 개선도, 향후 5년 계속 거주 의향 |
| 생활활동 | 통근·통학 여부, 직장·학교 위치, 교통수단, 통근시간, 랜드마크, 생필품·문화여가·의료·쇼핑·교육 이용지역 |
| 공동체 | 지역공동체 활동 참여 정도, 참여 방식, 소속감과 공동체 의식 |
| 응답자 일반사항 | 학력, 가구원수, 혼인상태, 자녀, 가구소득 |

이 부록은 본문 분석의 변수 설계를 확인할 때 중요하다. 예를 들어 주거환경 만족도는 시설 접근성 분석과 연결되고, 생활활동 문항은 주변지역 서비스 생활권 분석과 연결된다.

## 관련 원문 이미지

- [PDF page 227](../docs/newtown-resident-life-evaluation/assets/pages/pdf-page-227.jpg): 부록 표지
- [PDF page 229](../docs/newtown-resident-life-evaluation/assets/pages/pdf-page-229.jpg): 설문지 안내문
- [PDF page 231](../docs/newtown-resident-life-evaluation/assets/pages/pdf-page-231.jpg): 주택 및 주거환경 문항
- [PDF page 233](../docs/newtown-resident-life-evaluation/assets/pages/pdf-page-233.jpg): 주거 이동 문항
- [PDF page 235](../docs/newtown-resident-life-evaluation/assets/pages/pdf-page-235.jpg): 생활활동 문항
- [PDF page 237](../docs/newtown-resident-life-evaluation/assets/pages/pdf-page-237.jpg): 공동체 문항

<!-- END docs/newtown-resident-life-evaluation/06-appendix.md -->

<!-- BEGIN docs/newtown-resident-life-evaluation/07-references.md -->

---
book_title: "1·2기 신도시 종합평가 연구 (Ⅱ) - 신도시 주민의 삶 -"
slug: "newtown-resident-life-evaluation"
section_id: "07"
section_title: "참고문헌"
source_pdf: "../../sources/OTKCRK210996.pdf"
source_pages: "241-243"
status: "complete"
---

# 참고문헌

참고문헌은 주거만족도, 주거환경평가, 신도시 주민 만족, 도시계획시설, 공공임대주택 만족도, 신도시 거주가치 관련 연구로 구성된다.

원문 참고문헌 전문은 텍스트층 보존본 [text-layer/07-references.md](../docs/newtown-resident-life-evaluation/text-layer/07-references.md)와 PDF 페이지 이미지 [PDF page 241](../docs/newtown-resident-life-evaluation/assets/pages/pdf-page-241.jpg)-[PDF page 243](../docs/newtown-resident-life-evaluation/assets/pages/pdf-page-243.jpg)에서 확인할 수 있다.

## 주요 참고문헌 주제

| 주제 | 예시 |
|---|---|
| 주거만족도 이론 | Weidemann and Anderson, residential satisfaction 관련 연구 |
| 공공임대·주택유형 만족 | 공공임대주택 유형별 만족도 영향요인 |
| 신도시 거주만족 | 분당 등 서울 근교 신도시 거주자 만족 연구 |
| 주거환경 평가 | 주택규모, 주거환경, 가구특성별 평가 |
| 도시시설 접근성 | 시설 접근성과 만족도의 관계 |

## 보존 방식

- OCR은 사용하지 않았다.
- 참고문헌 원문 텍스트는 PDF 내장 텍스트층으로 보존했다.
- 페이지 이미지는 원문 대조용으로 함께 남겼다.

<!-- END docs/newtown-resident-life-evaluation/07-references.md -->

<!-- BEGIN docs/newtown-resident-life-evaluation/text-layer/README.md -->

---
book_title: "1·2기 신도시 종합평가 연구 (Ⅱ) - 신도시 주민의 삶 -"
slug: "newtown-resident-life-evaluation"
section_id: "text-layer"
section_title: "PDF 텍스트층 원문 보존본"
source_pdf: "../../../sources/OTKCRK210996.pdf"
source_pages: "1-243"
status: "source-archive"
---

# PDF 텍스트층 원문 보존본

이 폴더는 OCR이 아니라 PDF에 포함된 텍스트 레이어를 추출해 장별로 보존한 감사용 원문 아카이브다. 최종 독서용 Markdown은 한 단계 위의 `00-front-matter.md`부터 `07-references.md`까지의 파일이다.

- 원문 표현과 페이지 흐름을 나중에 대조할 수 있게 남긴다.
- 최종 재구성 Markdown에서 요약·표·수치가 어디에서 왔는지 역추적할 수 있게 한다.
- LLM 입력용 정리본과 원문 텍스트층을 분리해 관리한다.

전체 PDF 243쪽의 렌더링 이미지는 `../assets/pages/`에 함께 보존되어 있다.

<!-- END docs/newtown-resident-life-evaluation/text-layer/README.md -->
