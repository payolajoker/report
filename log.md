# 작업 로그

이 파일은 저장소의 중요한 ingest, query, update, lint 작업을 시간순으로 남기는 append-only 로그다. 자세한 변경 diff는 git history를 보고, 이 파일에는 "무엇을 왜 반영했는지"와 "다음에 확인할 점"을 짧게 기록한다.

## 기록 형식

새 항목은 다음 형식을 따른다.

```markdown
## [YYYY-MM-DD] type | 제목

- 범위: 수정하거나 검토한 주요 파일/폴더.
- 이유: 작업 배경.
- 결과: 반영된 내용.
- 남은 점검: 있으면 기록.
```

권장 type: `setup`, `ingest`, `query`, `update`, `lint`, `data`, `report`, `style`.

## [2026-05-06] setup | LLM Wiki 운영층 추가

- 범위: `AGENTS.md`, `index.md`, `log.md`, `README.md`.
- 이유: 저장소가 루트 보고서, 원문 재구성 도서, 보조 자료, 이미지, 데이터로 커지면서 LLM이 매번 README와 폴더 구조를 재해석해야 하는 부담이 커졌다.
- 결과: 루트 운영 규칙, LLM 작업 색인, append-only 작업 로그를 추가하고 README 상단에 운영 파일 진입 링크를 붙였다. 폴더는 새로 만들지 않고 루트에 직접 배치했다.
- 남은 점검: 이후 새 자료 ingest나 보고서 핵심 수정이 있을 때 `index.md`와 이 로그를 함께 갱신하는 습관을 유지해야 한다.

## [2026-05-06] update | 성남시사 페이지 이미지 디렉터리 폭 축소

- 범위: `books/seongnam-city-history-50/docs/seongnam-city-history-50/assets/pages/`, 성남시사 Markdown/LLM 번들, `README.md`, `AGENTS.md`.
- 이유: 성남시사 렌더링 페이지 이미지 5,864개가 단일 `assets/pages/` 디렉터리에 몰려 있어 장기 GitHub 운영에 불리했다.
- 결과: 페이지 이미지를 `assets/pages/vol-01/`-`assets/pages/vol-50/` 권별 하위 디렉터리로 이동하고, 관련 Markdown 링크와 설명을 새 경로로 갱신했다.
- 남은 점검: 향후 새 대형 PDF 컬렉션도 페이지 이미지가 3,000개를 넘기 전에 권별·장별 하위 디렉터리로 분산한다.
