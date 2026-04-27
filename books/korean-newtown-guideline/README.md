# PDF Markdown Knowledge Base

이 저장소는 PDF 자료를 LLM이 읽기 쉬운 Markdown 지식 구조로 정리하기 위한 작업 공간입니다.

## 현재 정리 완료 문서

- [한국형 신도시 가이드라인 연구](./docs/korean-newtown-guideline/index.md)

## 저장소 구조

```text
docs/
  korean-newtown-guideline/
    index.md                 # LLM/사람용 문서 목차
    manifest.yml             # 섹션 메타데이터
    stats.md                 # 주요 수치 인덱스
    source-page-index.md     # 전체 페이지 이미지 대조용 인덱스
    assets/pages/            # PDF 페이지 이미지
sources/
  OTKCRK170383.pdf           # 원본 PDF
dist/
  korean-newtown-guideline.llm.md
  korean-newtown-guideline.manifest.json
```

## 작성 원칙

- OCR 미사용.
- 페이지 이미지를 육안으로 확인해 문서 구조를 재작성.
- 표는 가능한 Markdown table로 정리.
- 그림은 원문 이미지 링크와 함께 해석 설명을 제공.
- 각 Markdown 파일에는 YAML frontmatter로 출처, 페이지 범위, 섹션 ID, OCR 미사용 여부를 기록.

## GitHub 관리 메모

PDF와 페이지 이미지는 용량이 커질 수 있으므로 Git LFS 사용을 권장합니다. `.gitattributes`에는 PDF, JPG, PNG를 LFS 대상으로 지정해 두었습니다.
