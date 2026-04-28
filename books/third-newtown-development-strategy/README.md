# 3기 신도시 개발전략 및 계획기준 수립 연구

PDF 원문을 LLM이 읽고 GitHub에서 관리하기 쉬운 Markdown 책 구조로 재구성한 완성본이다. OCR은 사용하지 않았고, PDF 내장 텍스트층과 렌더링 페이지 이미지를 대조해 장·절, 표, 주요 수치, 그림 참조를 정리했다.

> 상태: `complete`  
> 원본: `OTKCRK200194.pdf`, 491쪽  
> 발행: 한국토지주택공사 토지주택연구원, 연구지원 2020-16호  
> 저자: 윤정중, 김두환, 최상희, 윤은주, 윤정란, 권오준, 송태호, 박성용, 김동근

## 바로가기

- [문서 인덱스](./docs/third-newtown-development-strategy/index.md)
- [주요 수치 인덱스](./docs/third-newtown-development-strategy/stats.md)
- [Source page index](./docs/third-newtown-development-strategy/source-page-index.md)
- [Manifest](./docs/third-newtown-development-strategy/manifest.yml)
- [LLM 단일 번들](./dist/third-newtown-development-strategy.llm.md)
- [원본 PDF](./sources/OTKCRK200194.pdf)
- [전체 페이지 이미지](./docs/third-newtown-development-strategy/assets/pages/)
- [PDF 텍스트층 원문 보존본](./docs/third-newtown-development-strategy/text-layer/)

## 구성

| 구분 | 내용 |
|---|---|
| `docs/third-newtown-development-strategy/` | 최종 장별 Markdown, 인덱스, 통계, source page index |
| `docs/third-newtown-development-strategy/assets/pages/` | PDF 1-491쪽 전체 JPEG 페이지 이미지 |
| `docs/third-newtown-development-strategy/text-layer/` | OCR이 아닌 PDF 내장 텍스트층 추출 보존본 |
| `dist/` | LLM 통합본과 JSON manifest |
| `sources/` | 원본 PDF |

## 검수 메모

- 장 제목과 절 제목은 Markdown 헤더로 승격했다.
- 핵심 기준표와 통계치는 Markdown 표 또는 수치 인덱스로 재구성했다.
- 그림·도표는 캡션만 남기지 않고 원문 대조용 페이지 이미지를 보존했다.
- 491쪽 전체 페이지 이미지를 보존해 PDF 원문과 Markdown 재구성본을 상호 검증할 수 있게 했다.
