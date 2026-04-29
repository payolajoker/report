# 평촌신도시 개발사

이 폴더는 스캔본 PDF `OTKLEC010215.pdf`를 OCR 없이 육안 전사하여 GitHub와 LLM/RAG에서 읽기 좋게 정리한 책 폴더다.

## 바로가기

- [작업 인덱스](index.md)
- [전사 배치 목록](transcription/README.md)
- [원본 페이지 색인](source-page-index.md)
- [주요 통계 색인](stats.md)
- [처리 매니페스트](manifest.yml)
- [LLM 번들](../../dist/pyeongchon-newtown-development-history.llm.md)

## 처리 원칙

- OCR, 이미지 자동문자인식, Python 변환 스크립트는 사용하지 않았다.
- 각 PDF 페이지는 `assets/pages/pdf-page-xxx.jpg` 원본 이미지 링크로 감사 가능하게 남겼다.
- 표는 가능한 Markdown table로 옮겼고, 의미 있는 사진·도표는 이미지 자산으로 보존했다.
- 스캔 품질상 확정하기 어려운 글자는 `[일부 판독 어려움]`으로 표시했다.
