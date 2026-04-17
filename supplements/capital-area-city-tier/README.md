# 수도권 도시등급 - 보조 자료

공개 보고서 [수도권 도시등급 평가 보고서](../../수도권-도시등급-평가-보고서.md)의 방법론·지표·계산 결과를 담는 폴더.

## 문서

### 방법론
- [`docs/seoul-capital-area-city-tier-methodology.md`](./docs/seoul-capital-area-city-tier-methodology.md) - v1.0. 중국식 1선·신1선 체계의 한국 수도권 적용 논리, 8차원 지표 프레임, 가중치 선정, 1~9등급 운영 규칙, 재판별 절차. 이 프로젝트의 최상위 운영 문서.

### 지표 및 source anchor
- [`docs/seoul-capital-area-city-tier-indicator-registry.md`](./docs/seoul-capital-area-city-tier-indicator-registry.md) - 차원별 대표값/보조값/source family와 production status
- [`docs/seoul-capital-area-city-tier-source-anchors.md`](./docs/seoul-capital-area-city-tier-source-anchors.md) - exact KOSIS table ID, e-나라지표 idx_cd, 필드명까지 고정한 source anchor
- [`docs/kosis-capital-area-region-codes-DT_1B26001.md`](./docs/kosis-capital-area-region-codes-DT_1B26001.md) - KOSIS DT_1B26001 기준 수도권 66개 단위 행정구역 코드 맵

### 계산 결과
- [`docs/seoul-capital-area-run1-final-report.md`](./docs/seoul-capital-area-run1-final-report.md) - run-1 최종 점수표 및 차원별 분해
- [`docs/수도권_도시등급_최종전달본.md`](./docs/수도권_도시등급_최종전달본.md) - 원천 지표까지 포함한 전체 66개 단위 표

### 데이터 파일
- [`data/`](./data/) - baseline, merged, scored, ranking CSV가 이미 정리되어 있는 데이터 폴더

## 재현성

현재 단계에서 다음이 보장된다.

1. 지표 정의와 시점은 methodology 및 source anchors 문서에 고정되어 있다.
2. 66개 단위 행정구역 코드는 KOSIS DT_1B26001 트리에서 직접 추출해 고정했다.
3. `data/` 폴더에 baseline, merged, scored, ranking CSV가 함께 보관되어 있다.
4. 1차 계산(run-1)의 가중치와 등급 컷은 final-report에 명시되어 있다.

## 버전

- v1.0: 2026-04-13 기준 run-1. 메인 비교군은 수도권 66개 기초지자체. 경기 일반구는 보조 래더로 분리하되 이번 run에서는 제외.
