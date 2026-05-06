# 수도권 도시등급 run-1 최종 결과 보고서

- 기준 버전: run-1 yicai-proxy pooled score + distribution-based regrading
- 범위: 수도권 66개 기초지자체
- 최종 등급 컬럼: `regraded_final_grade`

## 1. 최종 산식

이번 최종본은 **전 단위를 한 풀(pool)에서 같이 경쟁**시키는 방식으로 계산했다. 즉 서울 자치구, 인천 구·군, 경기 시·군을 따로 백분위화하지 않고, 66개 전체를 하나의 경쟁 집합으로 놓았다.

### 1-1. 입력 축

- population: 주민등록인구
- migration: 이동자수(T10 전입)
- employment: 고용률 / 취업자수
- commuting: T40 주간 인구 지수
- fiscal: 재정자립도, 재정자주도
- urban_form: 도시지역 인구비율(행정구역 기준)
- supplementary: 2025 평균지가변동률 최신 비영(非零) 월 값

### 1-2. Yicai proxy 차원 구성

| 차원 | 구성 방식 | 가중치 |
|---|---|---:|
| commercial_resources_score | percentile(employed_thousand), percentile(fiscal_self_reliance), percentile(land_price_value)의 평균 | 30 |
| hubness_score | percentile(commuting_value), percentile(employed_thousand)의 평균 | 25 |
| human_activity_score | percentile(migration_value), percentile(employment_rate)의 평균 | 15 |
| new_economy_score | percentile(fiscal_autonomy), percentile(employment_rate), percentile(land_price_value)의 평균 | 15 |
| future_plasticity_score | percentile(population), percentile(fiscal_autonomy), percentile(urban_population_ratio_admin)의 평균 | 15 |

### 1-3. 총점 계산식

`total_score = commercial_resources_score*0.30 + hubness_score*0.25 + human_activity_score*0.15 + new_economy_score*0.15 + future_plasticity_score*0.15`

### 1-4. 등급 산정 방식

기존 절대 점수 컷은 1등급 공석 문제가 있었기 때문에, 최종 발표용 등급은 **실제 순위 분포 기반 재등급**을 사용했다.

| 순위 구간 | 최종 등급 |
|---|---:|
| 1~2위 | 1 |
| 3~6위 | 2 |
| 7~11위 | 3 |
| 12~18위 | 4 |
| 19~27위 | 5 |
| 28~37위 | 6 |
| 38~47위 | 7 |
| 48~57위 | 8 |
| 58~66위 | 9 |

## 2. 최종 순위 및 등급

| rank | region | unit_name | unit_type | total_score | old_grade | final_grade |
|---:|---|---|---|---:|---:|---:|
| 1 | Gyeonggi | 화성시 | city | 88.6956 | 2 | 1 |
| 2 | Gyeonggi | 성남시 | city | 82.0148 | 2 | 1 |
| 3 | Seoul | 강남구 | autonomous_district | 80.0064 | 3 | 2 |
| 4 | Gyeonggi | 수원시 | city | 75.5511 | 3 | 2 |
| 5 | Gyeonggi | 용인시 | city | 73.8164 | 4 | 2 |
| 6 | Gyeonggi | 안산시 | city | 73.5962 | 4 | 2 |
| 7 | Seoul | 영등포구 | autonomous_district | 73.4009 | 4 | 3 |
| 8 | Gyeonggi | 평택시 | city | 73.3282 | 4 | 3 |
| 9 | Gyeonggi | 시흥시 | city | 69.2490 | 4 | 3 |
| 10 | Gyeonggi | 안양시 | city | 69.0893 | 4 | 3 |
| 11 | Seoul | 송파구 | autonomous_district | 69.0888 | 4 | 3 |
| 12 | Seoul | 서초구 | autonomous_district | 68.8408 | 4 | 4 |
| 13 | Seoul | 마포구 | autonomous_district | 62.6677 | 5 | 4 |
| 14 | Gyeonggi | 고양시 | city | 62.3012 | 5 | 4 |
| 15 | Incheon | 서구 | autonomous_district | 61.5672 | 5 | 4 |
| 16 | Gyeonggi | 파주시 | city | 61.3065 | 5 | 4 |
| 17 | Gyeonggi | 부천시 | city | 59.9280 | 5 | 4 |
| 18 | Gyeonggi | 하남시 | city | 59.8666 | 5 | 4 |
| 19 | Seoul | 성동구 | autonomous_district | 59.7426 | 5 | 5 |
| 20 | Seoul | 용산구 | autonomous_district | 59.4649 | 5 | 5 |
| 21 | Gyeonggi | 남양주시 | city | 58.3272 | 5 | 5 |
| 22 | Gyeonggi | 김포시 | city | 58.2235 | 5 | 5 |
| 23 | Gyeonggi | 이천시 | city | 57.5379 | 6 | 5 |
| 24 | Gyeonggi | 광명시 | city | 57.0036 | 6 | 5 |
| 25 | Seoul | 강서구 | autonomous_district | 55.5299 | 6 | 5 |
| 26 | Seoul | 중구 | autonomous_district | 55.0620 | 6 | 5 |
| 27 | Gyeonggi | 광주시 | city | 53.9823 | 6 | 5 |
| 28 | Seoul | 동작구 | autonomous_district | 53.9246 | 6 | 6 |
| 29 | Seoul | 강동구 | autonomous_district | 53.8106 | 6 | 6 |
| 30 | Gyeonggi | 과천시 | city | 53.6741 | 6 | 6 |
| 31 | Seoul | 광진구 | autonomous_district | 52.5311 | 6 | 6 |
| 32 | Gyeonggi | 오산시 | city | 52.2598 | 6 | 6 |
| 33 | Seoul | 구로구 | autonomous_district | 51.0185 | 6 | 6 |
| 34 | Seoul | 동대문구 | autonomous_district | 50.0701 | 6 | 6 |
| 35 | Seoul | 종로구 | autonomous_district | 49.6675 | 7 | 6 |
| 36 | Incheon | 중구 | autonomous_district | 49.6181 | 7 | 6 |
| 37 | Gyeonggi | 의왕시 | city | 48.7026 | 7 | 6 |
| 38 | Seoul | 양천구 | autonomous_district | 47.1656 | 7 | 7 |
| 39 | Seoul | 서대문구 | autonomous_district | 46.4187 | 7 | 7 |
| 40 | Gyeonggi | 안성시 | city | 45.8639 | 7 | 7 |
| 41 | Seoul | 관악구 | autonomous_district | 44.1461 | 7 | 7 |
| 42 | Seoul | 성북구 | autonomous_district | 43.9274 | 7 | 7 |
| 43 | Gyeonggi | 군포시 | city | 43.8606 | 7 | 7 |
| 44 | Incheon | 연수구 | autonomous_district | 43.6112 | 7 | 7 |
| 45 | Seoul | 은평구 | autonomous_district | 42.5921 | 7 | 7 |
| 46 | Incheon | 남동구 | autonomous_district | 42.3790 | 7 | 7 |
| 47 | Seoul | 금천구 | autonomous_district | 42.3561 | 7 | 7 |
| 48 | Gyeonggi | 양주시 | city | 42.2103 | 7 | 8 |
| 49 | Gyeonggi | 포천시 | city | 41.9590 | 8 | 8 |
| 50 | Gyeonggi | 의정부시 | city | 41.4355 | 8 | 8 |
| 51 | Gyeonggi | 여주시 | city | 41.1193 | 8 | 8 |
| 52 | Seoul | 노원구 | autonomous_district | 41.0381 | 8 | 8 |
| 53 | Gyeonggi | 구리시 | city | 41.0114 | 8 | 8 |
| 54 | Incheon | 부평구 | autonomous_district | 40.1775 | 8 | 8 |
| 55 | Incheon | 미추홀구 | autonomous_district | 34.5561 | 8 | 8 |
| 56 | Seoul | 중랑구 | autonomous_district | 33.7168 | 9 | 8 |
| 57 | Gyeonggi | 가평군 | county | 32.1997 | 9 | 8 |
| 58 | Seoul | 도봉구 | autonomous_district | 30.5519 | 9 | 9 |
| 59 | Incheon | 강화군 | county | 29.7383 | 9 | 9 |
| 60 | Gyeonggi | 양평군 | county | 29.1705 | 9 | 9 |
| 61 | Incheon | 계양구 | autonomous_district | 28.9652 | 9 | 9 |
| 62 | Gyeonggi | 연천군 | county | 27.3423 | 9 | 9 |
| 63 | Incheon | 옹진군 | county | 27.2834 | 9 | 9 |
| 64 | Seoul | 강북구 | autonomous_district | 26.7708 | 9 | 9 |
| 65 | Incheon | 동구 | autonomous_district | 24.9188 | 9 | 9 |
| 66 | Gyeonggi | 동두천시 | city | 19.5276 | 9 | 9 |

## 3. 차원별 점수 확인용 상위 10개

| rank | region | unit_name | commercial | hubness | human_activity | new_economy | future_plasticity | total_score | final_grade |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | Gyeonggi | 화성시 | 89.2266 | 85.2181 | 97.4616 | 89.0428 | 84.3159 | 88.6956 | 1 |
| 2 | Gyeonggi | 성남시 | 93.2008 | 77.7577 | 61.9231 | 72.0864 | 96.7583 | 82.0148 | 1 |
| 3 | Seoul | 강남구 | 90.3858 | 85.6488 | 57.3846 | 66.3636 | 86.1081 | 80.0064 | 2 |
| 4 | Gyeonggi | 수원시 | 79.0181 | 67.2131 | 85.0000 | 61.1158 | 87.5000 | 75.5511 | 2 |
| 5 | Gyeonggi | 용인시 | 89.7818 | 63.0592 | 57.2308 | 59.2377 | 90.9787 | 73.8164 | 2 |
| 6 | Gyeonggi | 안산시 | 73.8360 | 71.9644 | 65.5384 | 69.7611 | 87.7289 | 73.5962 | 2 |
| 7 | Seoul | 영등포구 | 71.5858 | 77.2020 | 79.0769 | 73.7962 | 64.6246 | 73.4009 | 3 |
| 8 | Gyeonggi | 평택시 | 63.1794 | 79.2582 | 88.8461 | 62.3446 | 79.2081 | 73.3282 | 3 |
| 9 | Gyeonggi | 시흥시 | 72.1313 | 66.0878 | 65.1539 | 65.8608 | 76.2363 | 69.2490 | 3 |
| 10 | Gyeonggi | 안양시 | 71.6053 | 63.6010 | 69.9231 | 61.3866 | 80.0733 | 69.0893 | 3 |

## 4. 저장 파일

- 점수 상세: `../data/seoul-capital-area-run1-scored-yicai-proxy.csv`
- 순위/최종등급: `../data/seoul-capital-area-run1-ranking-yicai-proxy-regraded.csv`
- 본 보고서: `./seoul-capital-area-run1-final-report.md`
