# 일산신도시 개발사

PDF 원문을 LLM이 읽고 GitHub에서 관리하기 쉬운 Markdown 책 구조로 재구성한 완성본이다. 스캔본이라 OCR을 사용하지 않았고, 927쪽 전체 페이지 이미지를 육안으로 대조해 장·절, 표, 사진·도표 참조, 주요 수치, 추진일지를 정리했다.

> 상태: `complete`
> 원본: `OTKLEC010118.pdf`, 927쪽
> 발행: 한국토지공사
> 발행일: 1997년 1월
> 주제: 일산신도시 계획, 보상, 개발, 용지공급, 주택건설, 기반시설, 호수공원, 문화유적, 사업준공, 평가, 추진일지

## 바로가기

- [문서 인덱스](./docs/ilsan-newtown-development-history/index.md)
- [주요 수치 인덱스](./docs/ilsan-newtown-development-history/stats.md)
- [Source page index](./docs/ilsan-newtown-development-history/source-page-index.md)
- [Manifest](./docs/ilsan-newtown-development-history/manifest.yml)
- [LLM 단일 번들](./dist/ilsan-newtown-development-history.llm.md)
- [원본 PDF](./sources/OTKLEC010118.pdf)
- [전체 페이지 이미지](./docs/ilsan-newtown-development-history/assets/pages/)

## 구성

| 구분 | 내용 |
|---|---|
| `docs/ilsan-newtown-development-history/` | 최종 Markdown 전사본, 인덱스, 통계, source page index |
| `docs/ilsan-newtown-development-history/transcription/` | PDF 1-927쪽을 93개 배치로 나눈 육안 전사본 |
| `docs/ilsan-newtown-development-history/assets/pages/` | PDF 1-927쪽 전체 JPEG 페이지 이미지 |
| `dist/` | LLM 통합본과 JSON manifest |
| `sources/` | 원본 PDF |

## 검수 메모

- PDF 927쪽 전체를 배치별 Markdown으로 전사했다.
- 장 제목과 주요 절 제목은 Markdown 헤더로 승격했다.
- 핵심 표, 추진일지, 공사목록, 협약목록, 참여자 도표는 Markdown 표 또는 요약표로 재구성했다.
- OCR 없이 페이지 이미지를 육안 대조했고, 원문 확인용 페이지 이미지를 모두 보존했다.
