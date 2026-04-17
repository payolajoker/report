# 수도권 도시등급 지표 레지스트리 v1.0

이 문서는 실제 점수표를 만들 때 어떤 지표를 어떤 필드명으로 넣을지 고정하는 레지스트리다.

## 현재 계산 범위

- run-1 main universe: 수도권 기초지자체 66개
- 제외: 경기도 일반구 sub-layer

## 메인 래더 공통 차원

### 1. population
- 대표값: 주민등록인구
- 보조값: 인구밀도, 청년인구비율, 고령인구비율, 1인가구비율
- source_family: MOIS 주민등록인구통계, KOSIS, e-지방지표
- exact_core_tables:
  - `DT_1B04006` 행정구역(시군구)별/1세별 주민등록인구
  - MOIS 행정동별 주민등록 인구 및 세대현황
- preferred_rule:
  - 주민등록인구는 KOSIS `DT_1B04006` 또는 MOIS 월말 기준값 사용
  - 청년비율과 고령비율은 `DT_1B04006`에서 파생 계산 우선
  - e-지방지표 direct 비율은 보조 검증용

### 2. migration
- 대표값: 순이동인구 또는 청년순이동률
- 보조값: 전입인구, 전출인구, 인구증가율
- source_family: KOSIS 국내인구이동통계, e-지방지표
- exact_core_tables:
  - `DT_1B26001` 시군구/성/연령(5세)별 이동자수
  - `DT_1B26002` 시군구/성/연령(5세)별 순이동자수
  - `INH_1B26001_A021` 순이동인구(시도/시/군/구)
  - `INH_1B26001_A022` 전입인구(시도/시/군/구)
  - `INH_1B26001_A023` 전출인구(시도/시/군/구)
  - `DT_1YL20642` 청년순이동률(시도/시/군/구)
- preferred_rule:
  - 월별 core는 `DT_1B26001`, `DT_1B26002`
  - 연간 supplement는 e-지방지표 `청년순이동률`
  - 혼합 사용 시 최근 12개월 합계 또는 최근 연간 확정치 사용

### 3. employment
- 대표값: 고용률
- 보조값: 실업률, 취업자수, 경제활동참가율, 청년고용률
- source_family: 지역별고용조사, e-지방지표
- exact_core_tables:
  - `DT_1ES3A03_A01S` 시군구/연령별 취업자 및 고용률(전체)
  - `DT_1ES3A01S` 시군구 경제활동인구 총괄
  - `INH_1ES3A03_A01S` 청년고용률(시/군/구)
- preferred_rule:
  - 고용률 대표값은 `DT_1ES3A03_A01S`
  - 실업률과 경제활동참가율은 `DT_1ES3A01S`
  - 청년고용은 `INH_1ES3A03_A01S` 또는 `DT_1ES3A03_A01S`의 15~29세 slice 사용

### 4. business
- 대표값: 인구 천명당 사업체수
- 보조값: 인구 천명당 종사자수, 사업체수, 종사자수, 창업기업수
- source_family: 전국사업체조사, e-지방지표
- exact_core_tables:
  - `DT_1K52F03` 시도·산업·종사자규모별 사업체수, 종사자수(’20~)
- limitation:
  - unified KOSIS nationwide family로 확인된 exact table은 **시도 레벨만 확정**
  - 66개 시군구 전체에 대해 단일 전국사업체조사 family exact pull은 미확정
- preferred_rule:
  - 메인 래더 공식 core score에서는 business 차원을 일단 `supplementary/partial`로 처리
  - 차후 지방기초통계 또는 municipality-specific KOSIS tables를 붙여 확장 가능

### 5. commuting
- 대표값: 거주지내 통근 취업자 비중 또는 통근 흡입 관련 공식표
- 보조값: 타지역 통근 취업자 비중
- source_family: 인구총조사 통근통학, e-지방지표
- exact_core_tables:
  - `DT_1PA2020` 성별/연령별 상주(야간)·주간 인구-시군구
  - `DT_1PA2005` 현 거주지별/성별/통근통학지별 통근통학 인구(서울, 인천, 경기)-시군구
- primary_indicator:
  - `DT_1PA2020`의 `T40 주간 인구 지수`
- secondary_indicators:
  - `DT_1PA2020`의 `T11 유입 인구-통근`
  - `DT_1PA2020`의 `T21 유출 인구-통근`
- preferred_rule:
  - 통근 축은 인구총조사 기반 구조지표로 취급
  - census 갱신 전까지는 동일 지표를 고정 사용하고, 연간 노동지표만 갱신
  - mobility proxy로 민간 데이터를 섞지 않음

### 6. fiscal
- 대표값: 재정자립도
- 보조값: 재정자주도, 지방세 과징 실적, 지방공무원 정원/인구
- source_family: e-나라지표, e-지방지표, MOIS
- exact_core_tables:
  - e-나라지표 `idx_cd=2458` 지방자치단체 재정자립도
  - e-나라지표 `idx_cd=2857` 자치단체 재정자주도
  - e-나라지표 `idx_cd=1050` 자치단체별 지방세 과징 실적
  - e-나라지표 `idx_cd=1042` 지방자치단체 공무원 정원

### 7. housing
- 대표값: 총주택수 또는 빈집비율
- 보조값: 주택보급률, 노후주택비율, 빈집수, 일반가구 주택소유율
- source_family: KOSIS 주택 관련 표, MOLIT, e-지방지표
- exact_core_tables:
  - `DT_1JU1501` 주택의 종류별 주택
  - `DT_1JU1512` 건축연도 및 주택의 종류별 미거주 주택(빈집)
- preferred_rule:
  - 빈집비율 = `DT_1JU1512 / DT_1JU1501`
  - 주택보급률은 시군구 extraction이 완전히 확정되기 전까지 보조지표

### 8. urban_form
- 대표값: 도시지역 인구비율
- 보조값: 도시지역 인구, 도시지역면적, 지가변동률
- source_family: KOSIS 도시계획현황, 한국부동산원, MOLIT
- exact_core_tables:
  - `TX_315_2009_H1001` 도시지역 인구현황(시군구)
  - `TX_315_2009_H1009` 행정구역 현황
  - `DT_PLCAHTUSE` 시군구별/용도지역별/이용상황별 지가변동률

### 9. supplementary
- 대표값: 교육/보건/안전/문화 지표 중 1~2개 선택
- 보조값: 도서관 수, 병상수, 의사수, 범죄, 공원면적
- source_family: e-지방지표, KOSIS

## 점수화 필드 원칙

모든 지표는 아래 순서대로 처리한다.

1. raw_value 기록
2. unit 기록
3. reference_period 기록
4. source_url 또는 source_family 기록
5. direction 기록
   - high_is_good
   - low_is_good
6. normalized_value 계산
7. indicator_score 계산
8. dimension_score 계산

## provisional 표시 규칙

- 실제 raw_value가 입력되기 전까지 모든 grade는 provisional
- raw_value가 8개 차원 중 6개 이상 채워지면 provisional-low
- raw_value가 8개 차원 모두 채워지고 대체지표 비율이 20% 미만이면 provisional-high
- 2회차 업데이트까지 반복되면 stable 검토 가능

## 현재 production status

- population: production-ready
- migration: production-ready
- employment: production-ready
- commuting: production-ready
- fiscal: production-ready
- housing: production-ready with minor optional gaps
- urban_form: production-ready
- business: partial, unified nationwide exact table confirmed only at 시도 level
