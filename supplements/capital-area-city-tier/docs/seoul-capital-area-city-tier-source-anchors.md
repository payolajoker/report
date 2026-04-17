# 수도권 도시등급 source anchors v1.0

이 문서는 실제 점수 계산에 바로 넣을 exact source anchor를 모아둔 문서다.

## 1. population

- 주민등록인구 / 1세별 주민등록인구
  - source: KOSIS
  - table_id: `DT_1B04006`
  - table_name: 행정구역(시군구)별/1세별 주민등록인구
  - unit_level: 시군구
  - latest_confirmed: 2026
  - use:
    - 총인구
    - 청년비율 파생
    - 고령비율 파생

- 주민등록 인구 및 세대현황
  - source: MOIS
  - url: https://jumin.mois.go.kr/statMonth.do
  - unit_level: 시군구 조회 가능
  - latest_confirmed: 2026.03
  - use:
    - 월말 기준 population cross-check

- 평균연령
  - source: KOSIS / e-지방지표
  - table_id: `INH_1IN1503_02`
  - unit_level: 시도/시/군/구
  - latest_confirmed: 2024

- 1인가구비율
  - source: e-지방지표
  - table_id: `DT_1YL21161`
  - unit_level: 시도/시/군/구
  - latest_confirmed: 2024

## 2. migration

- 이동자수
  - source: KOSIS
  - table_id: `DT_1B26001`
  - table_name: 시군구/성/연령(5세)별 이동자수
  - unit_level: 시군구
  - latest_confirmed: 2026.02
  - use:
    - 전입/전출
    - 청년 전입/전출 파생

- 순이동자수
  - source: KOSIS
  - table_id: `DT_1B26002`
  - table_name: 시군구/성/연령(5세)별 순이동자수
  - unit_level: 시군구
  - latest_confirmed: 2026.02
  - use:
    - 순이동
    - 청년순이동 파생

- 순이동인구
  - source: e-지방지표
  - table_id: `INH_1B26001_A021`

- 전입인구
  - source: e-지방지표
  - table_id: `INH_1B26001_A022`

- 전출인구
  - source: e-지방지표
  - table_id: `INH_1B26001_A023`

- 청년순이동률
  - source: e-지방지표
  - table_id: `DT_1YL20642`
  - latest_confirmed: 2025

## 3. employment

- 고용률 / 취업자수
  - source: KOSIS 지역별고용조사
  - table_id: `DT_1ES3A03_A01S`
  - table_name: 시군구/연령별 취업자 및 고용률(전체)
  - unit_level: 시군구
  - latest_confirmed: 2025 하반기

- 실업률 / 경제활동참가율
  - source: KOSIS 지역별고용조사
  - table_id: `DT_1ES3A01S`
  - table_name: 시군구 경제활동인구 총괄
  - unit_level: 시군구

- 청년고용률
  - source: KOSIS / e-지방지표 layer
  - table_id: `INH_1ES3A03_A01S`
  - unit_level: 시군구

## 4. commuting / centrality

- 상주·주간 인구
  - source: KOSIS 인구총조사
  - table_id: `DT_1PA2020`
  - table_name: 성별/연령별 상주(야간)·주간 인구-시군구
  - unit_level: 시군구
  - latest_confirmed: 2020
  - primary_field: `T40 주간 인구 지수`
  - secondary_fields:
    - `T11 유입 인구-통근`
    - `T21 유출 인구-통근`

- 수도권 OD 통근통학
  - source: KOSIS 인구총조사 통근통학
  - table_id: `DT_1PA2005`
  - table_name: 현 거주지별/성별/통근통학지별 통근통학 인구(서울, 인천, 경기)-시군구
  - unit_level: 시군구 OD
  - latest_confirmed: 2020

## 5. fiscal

- 재정자립도
  - source: e-나라지표 / MOIS
  - idx_cd: `2458`
  - url: https://www.index.go.kr/unity/potal/main/EachDtlPageDetail.do?idx_cd=2458

- 재정자주도
  - source: e-나라지표 / MOIS
  - idx_cd: `2857`
  - url: https://www.index.go.kr/unity/potal/main/EachDtlPageDetail.do?idx_cd=2857

- 지방세 과징 실적
  - source: e-나라지표 / MOIS
  - idx_cd: `1050`
  - url: https://www.index.go.kr/unity/potal/main/EachDtlPageDetail.do?idx_cd=1050

- 지방공무원 정원
  - source: e-나라지표 / MOIS
  - idx_cd: `1042`
  - url: https://www.index.go.kr/unity/potal/main/EachDtlPageDetail.do?idx_cd=1042

## 6. housing

- 총주택수
  - source: KOSIS
  - table_id: `DT_1JU1501`
  - table_name: 주택의 종류별 주택
  - unit_level: 시군구
  - latest_confirmed: 2024

- 빈집수
  - source: KOSIS
  - table_id: `DT_1JU1512`
  - table_name: 건축연도 및 주택의 종류별 미거주 주택(빈집)
  - unit_level: 시군구
  - latest_confirmed: 2024

- 빈집비율
  - formula: `DT_1JU1512 / DT_1JU1501`

## 7. urban_form

- 도시지역 인구현황
  - source: KOSIS / LX
  - table_id: `TX_315_2009_H1001`
  - unit_level: 시군구
  - latest_confirmed: 2024

- 행정구역 현황
  - source: KOSIS / LX
  - table_id: `TX_315_2009_H1009`
  - unit_level: 시군구 또는 상위단위 확인 필요

- 지가변동률
  - source: KOSIS / 한국부동산원
  - table_id: `DT_PLCAHTUSE`
  - unit_level: 시군구
  - latest_confirmed: 2026.02

## 8. business

- 사업체수 / 종사자수
  - source: KOSIS 전국사업체조사
  - table_id: `DT_1K52F03`
  - table_name: 시도·산업·종사자규모별 사업체수, 종사자수(’20~)
  - unit_level: 시도
  - latest_confirmed: 2024
  - note:
    - unified nationwide exact source로는 시도 레벨까지만 확인
    - 66개 시군구 main ladder core source로는 아직 부족
