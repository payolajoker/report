# 판교신도시 마스터 플랜 및 디자인 총람

PDF 원문을 LLM이 읽고 GitHub에서 관리하기 쉬운 Markdown 책 구조로 재구성한 완성본이다. 이미지 PDF라 OCR을 사용하지 않았고, 331쪽 전체 페이지 이미지를 10쪽 단위로 육안 검토해 표지·목차, 판교신도시 개요, 동판교 마스터 플랜, 건축계획안, 현상설계·국제설계경기·턴키·민간사업 프로젝트, 개발 현황을 정리했다.

> 상태: `complete`  
> 원본: `OTKNTC070432.pdf`, 331쪽  
> 발행: 대한주택공사  
> 주제: 판교신도시, 동판교 마스터 플랜, 건축계획안, 현상설계, 국제설계경기, 턴키 프로젝트, 민간사업, 개발 현황

## 바로가기

- [문서 인덱스](./docs/pangyo-newtown-master-plan-design-book/index.md)
- [주요 수치 인덱스](./docs/pangyo-newtown-master-plan-design-book/stats.md)
- [Source page index](./docs/pangyo-newtown-master-plan-design-book/source-page-index.md)
- [Manifest](./docs/pangyo-newtown-master-plan-design-book/manifest.yml)
- [LLM 단일 번들](./dist/pangyo-newtown-master-plan-design-book.llm.md)
- [원본 PDF](./sources/OTKNTC070432.pdf)
- [전체 페이지 이미지](./docs/pangyo-newtown-master-plan-design-book/assets/pages/)

## 구성

| 구분 | 내용 |
|---|---|
| `docs/pangyo-newtown-master-plan-design-book/` | 10쪽 단위 Markdown 검토본, 인덱스, 통계, source page index |
| `docs/pangyo-newtown-master-plan-design-book/transcription/` | PDF 1-331쪽을 34개 배치로 나눈 육안 검토본 |
| `docs/pangyo-newtown-master-plan-design-book/assets/pages/` | PDF 1-331쪽 전체 JPEG 페이지 이미지 |
| `dist/` | LLM 통합본과 JSON manifest |
| `sources/` | 원본 PDF |

## 검수 메모

- PDF 331쪽 전체를 10쪽 단위 배치별 Markdown으로 정리했다.
- 표, 도면, 단지별 수치, 단위세대 계획은 각 배치의 `Stats Candidates`와 `Key Figures And Tables`에 보존했다.
- OCR 없이 페이지 이미지를 육안 대조했고, 판독이 어려운 미세문자는 배치별 검증 노트에 표시했다.
