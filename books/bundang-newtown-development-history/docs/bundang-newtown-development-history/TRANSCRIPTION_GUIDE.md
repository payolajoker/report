# 분당신도시 개발사 전사 가이드

이 문서는 병렬 작업자가 `transcription/` 배치 파일을 만들 때 따르는 규칙이다.

## 범위

- 원본: `sources/OTKLEC010078.pdf`
- 렌더링 페이지 이미지: `docs/bundang-newtown-development-history/assets/pages/pdf-page-0001.jpg` through `pdf-page-1094.jpg`
- OCR, Tesseract, OCRmyPDF, Apple Live Text, Google Vision, 이미지 자동 전사 도구 사용 금지
- PDF embedded text가 있더라도 최종 내용은 페이지 이미지와 대조한다

## 파일명

배치 파일은 다음 형식을 따른다.

```text
transcription/batch-001-pages-0001-0010.md
transcription/batch-002-pages-0011-0020.md
...
transcription/batch-110-pages-1091-1094.md
```

## 배치 파일 템플릿

```markdown
# 분당신도시 개발사 - 전사 배치 001

- PDF 페이지: 0001-0010
- 전사 방식: 렌더링 이미지 육안 판독
- OCR 사용: 없음

---

## PDF p.0001

![PDF page 0001](../assets/pages/pdf-page-0001.jpg)

내용을 Markdown 구조로 전사한다.
```

## 전사 규칙

- 페이지마다 `## PDF p.####` 제목과 원본 이미지 링크를 둔다.
- 제목, 장, 절, 표 제목, 그림 제목은 Markdown 헤더로 승격한다.
- 표가 읽히면 Markdown 표로 옮긴다. 너무 복잡하면 핵심 열과 행을 우선하고, 나머지는 `[일부 판독 어려움]`으로 표시한다.
- 지도, 사진, 도면, 신문 스크랩처럼 시각 자체가 의미 있는 페이지는 텍스트 설명과 함께 `[그림/사진]` 표기를 남긴다.
- 확신할 수 없는 글자는 추측하지 말고 `[판독 어려움]` 또는 `[일부 판독 어려움]`으로 표시한다.
- 중요한 수치(면적, 인구, 세대, 사업비, 연장, 용량, 연도)는 그대로 보존하고 단위를 함께 적는다.
- 작업자는 공유 파일(`index.md`, `manifest.yml`, `stats.md`, `source-page-index.md`, `dist/`)을 수정하지 않는다.
