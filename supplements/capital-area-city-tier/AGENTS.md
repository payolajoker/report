# AGENTS - capital-area-city-tier

## 폴더 목적
수도권 66개 기초지자체 도시등급 평가의 방법론·지표·계산 결과 보관소.

## 진입 순서
1. `docs/seoul-capital-area-city-tier-methodology.md` - 전체 프레임
2. `docs/seoul-capital-area-city-tier-indicator-registry.md` - 차원별 지표
3. `docs/seoul-capital-area-city-tier-source-anchors.md` - exact source
4. `docs/seoul-capital-area-run1-final-report.md` - 실제 계산 결과
5. `docs/수도권_도시등급_최종전달본.md` - 공개 전달본

## 수정 시 규칙
- methodology의 가중치·차원 구성을 바꿀 경우, run-1 이후의 새 run 번호를 부여하고 별도 final-report를 생성한다. run-1 파일은 변경하지 않는다.
- source anchors를 변경할 때는 exact table ID와 시점을 함께 기록한다.
- 지표 레지스트리의 production status는 함부로 승격시키지 않는다. 실제 exact pull이 66개 단위 전체에 대해 작동할 때만 production-ready로 올린다.

## 금지
- 사용자 홈 디렉터리나 임시 작업 폴더를 가리키는 절대경로를 repo 내 문서에 추가하지 말 것. 저장소 안에 있는 파일은 repo 상대경로로 쓰고, 저장소에 없는 원본 작업 폴더는 경로 대신 자료명이나 공식 URL만 남긴다.
- methodology의 특정 결정(예: 사업체 차원을 supplementary로 처리)을 "잘못된 것"으로 취급하지 말 것. 이 결정들은 exact source 확보 현황을 반영한 의식적 선택이다.
