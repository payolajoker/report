# 평촌신도시 개발사

PDF 원문을 LLM이 읽고 GitHub에서 관리하기 쉬운 Markdown 책 구조로 재구성한 완성본이다. 스캔본이라 OCR을 사용하지 않았고, 693쪽 전체 페이지 이미지를 육안으로 대조해 장·절, 표, 사진·도표 참조, 주요 수치, 추진일지를 정리했다.

> 상태: `complete`  
> 원본: `OTKLEC010215.pdf`, 693쪽  
> 발행: 한국토지개발공사  
> 주제: 평촌신도시 계획, 보상, 개발, 용지공급, 주택건설, 기반시설, 문화유적, 사업준공, 평가, 추진일지

## 바로가기

- [문서 인덱스](./docs/pyeongchon-newtown-development-history/index.md)
- [주요 수치 인덱스](./docs/pyeongchon-newtown-development-history/stats.md)
- [Source page index](./docs/pyeongchon-newtown-development-history/source-page-index.md)
- [Manifest](./docs/pyeongchon-newtown-development-history/manifest.yml)
- [LLM 단일 번들](./dist/pyeongchon-newtown-development-history.llm.md)
- [원본 PDF](./sources/OTKLEC010215.pdf)
- [전체 페이지 이미지](./docs/pyeongchon-newtown-development-history/assets/pages/)

## 구성

| 구분 | 내용 |
|---|---|
| `docs/pyeongchon-newtown-development-history/` | 최종 Markdown 전사본, 인덱스, 통계, source page index |
| `docs/pyeongchon-newtown-development-history/transcription/` | PDF 1-693쪽을 69개 배치로 나눈 육안 전사본 |
| `docs/pyeongchon-newtown-development-history/assets/pages/` | PDF 1-693쪽 전체 JPEG 페이지 이미지 |
| `docs/pyeongchon-newtown-development-history/assets/images/` | 본문 이해에 필요한 사진·도표 보존 이미지 |
| `dist/` | LLM 통합본과 JSON manifest |
| `sources/` | 원본 PDF |

## 검수 메모

- PDF 693쪽 전체를 배치별 Markdown으로 전사했다.
- 장 제목과 주요 절 제목은 Markdown 헤더로 승격했다.
- 핵심 표와 추진일지는 Markdown 표로 재구성했다.
- OCR 없이 페이지 이미지를 육안 대조했고, 원문 확인용 페이지 이미지를 모두 보존했다.
