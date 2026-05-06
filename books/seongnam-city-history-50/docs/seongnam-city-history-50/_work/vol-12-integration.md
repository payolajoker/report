# Vol 12 Integration Note: 제12권 성남의 민속

## 처리 범위

- 담당 범위: 12권 전용 산출물만 생성했다.
- 원천 PDF: `books/seongnam-city-history-50/sources/seongnam-history-50-vol-12.pdf`
- 공식 URL: `https://www.seongnam.go.kr/city/1001112/30566/bbsView.do?idx=378682`
- PDF 쪽수: 128쪽
- OCR 사용: false. `pdftotext -layout`로 임베디드 텍스트층을 추출했다.
- 처리 상태: 전체 1-128쪽 텍스트층 반영. 126쪽과 128쪽은 텍스트층 기준 공백 쪽으로 표시했다.
- 공용 파일 미편집: `README.md`, `.gitattributes`, `index.md`, `manifest.yml`, `stats.md`, `figures.md`, `source-page-index.md`는 건드리지 않았다.

## 생성 파일

- `docs/seongnam-city-history-50/vol-12-folklore.md`
- `dist/seongnam-history-50-vol-12.llm.md`
- `docs/seongnam-city-history-50/assets/pages/vol-12/vol-12-page-*.jpg` 57개
- `docs/seongnam-city-history-50/_work/vol-12-integration.md`

## 공용 인덱스 병합 후보: 목차

| Part | 원문 쪽 | 내용 |
| --- | --- | --- |
| 앞부분 | 1-3 | 표지와 권별 목차 |
| 1 | 4-41 | 의식주 생활: 주생활, 식생활, 의생활 |
| 2 | 42-96 | 평생 의례: 혼례, 상례와 장례, 제례 |
| 3 | 97-125 | 세시풍속과 민간신앙: 월별 세시풍속, 마을신앙, 점복 |
| 뒷부분 | 126-128 | 공백 쪽과 판권 |

## 공용 figures.md 병합 후보

| 파일 | 원문 쪽 | 내용 | 처리 상태 |
| --- | --- | --- | --- |
| [vol-12-page-007.jpg](../assets/pages/vol-12/vol-12-page-007.jpg) | 7 | 성남 오리뜰 농악 공연 | rendered-page |
| [vol-12-page-009.jpg](../assets/pages/vol-12/vol-12-page-009.jpg) | 9 | 전통 살림집 배치도 | rendered-page |
| [vol-12-page-011.jpg](../assets/pages/vol-12/vol-12-page-011.jpg) | 11 | 판교동 연안이씨 이곤 불천위 사당 | rendered-page |
| [vol-12-page-012.jpg](../assets/pages/vol-12/vol-12-page-012.jpg) | 12 | 수내동가옥 | rendered-page |
| [vol-12-page-013.jpg](../assets/pages/vol-12/vol-12-page-013.jpg) | 13 | 1970년대 분당구 수내동 전경 | rendered-page |
| [vol-12-page-017.jpg](../assets/pages/vol-12/vol-12-page-017.jpg) | 17 | 판교동 개나리마을 | rendered-page |
| [vol-12-page-019.jpg](../assets/pages/vol-12/vol-12-page-019.jpg) | 19 | 취락구조개선사업과 농촌표준주택 수치 | rendered-page |
| [vol-12-page-020.jpg](../assets/pages/vol-12/vol-12-page-020.jpg) | 20 | 1978년 농촌표준주택 25평형 평면도 | rendered-page |
| [vol-12-page-021.jpg](../assets/pages/vol-12/vol-12-page-021.jpg) | 21 | 도시형 다세대주택 | rendered-page |
| [vol-12-page-024.jpg](../assets/pages/vol-12/vol-12-page-024.jpg) | 24 | 정자동 초고층 아파트단지와 단독주택 | rendered-page |
| [vol-12-page-025.jpg](../assets/pages/vol-12/vol-12-page-025.jpg) | 25 | 아파트 주생활 변화 | rendered-page |
| [vol-12-page-029.jpg](../assets/pages/vol-12/vol-12-page-029.jpg) | 29 | 단대동 닭죽촌 | rendered-page |
| [vol-12-page-031.jpg](../assets/pages/vol-12/vol-12-page-031.jpg) | 31 | 여수동 갈매기살촌 | rendered-page |
| [vol-12-page-033.jpg](../assets/pages/vol-12/vol-12-page-033.jpg) | 33 | 백현동 카페거리 | rendered-page |
| [vol-12-page-037.jpg](../assets/pages/vol-12/vol-12-page-037.jpg) | 37 | 전통 돌복과 개량 한복 돌복 | rendered-page |
| [vol-12-page-038.jpg](../assets/pages/vol-12/vol-12-page-038.jpg) | 38 | 전통 혼례복과 과도기 혼례복 | rendered-page |
| [vol-12-page-039.jpg](../assets/pages/vol-12/vol-12-page-039.jpg) | 39 | 현대 서양식 혼례복 | rendered-page |
| [vol-12-page-040.jpg](../assets/pages/vol-12/vol-12-page-040.jpg) | 40 | 상복 변화 | rendered-page |
| [vol-12-page-041.jpg](../assets/pages/vol-12/vol-12-page-041.jpg) | 41 | 제례복과 참사자 복장 | rendered-page |
| [vol-12-page-045.jpg](../assets/pages/vol-12/vol-12-page-045.jpg) | 45 | 결혼제도 인식 통계청 조사 | rendered-page |
| [vol-12-page-047.jpg](../assets/pages/vol-12/vol-12-page-047.jpg) | 47 | 혼인 건수 변동 추이 | rendered-page |
| [vol-12-page-048.jpg](../assets/pages/vol-12/vol-12-page-048.jpg) | 48 | 결혼식 형태 통계청 조사 | rendered-page |
| [vol-12-page-049.jpg](../assets/pages/vol-12/vol-12-page-049.jpg) | 49 | 성남시 예식장 현황 | rendered-page |
| [vol-12-page-051.jpg](../assets/pages/vol-12/vol-12-page-051.jpg) | 51 | 1990년대 결혼 준비 대행업체 기사 목록 | rendered-page |
| [vol-12-page-052.jpg](../assets/pages/vol-12/vol-12-page-052.jpg) | 52 | 결혼 비용과 웨딩 서비스 성장 | rendered-page |
| [vol-12-page-053.jpg](../assets/pages/vol-12/vol-12-page-053.jpg) | 53 | 인터넷 결혼 준비 기사 | rendered-page |
| [vol-12-page-054.jpg](../assets/pages/vol-12/vol-12-page-054.jpg) | 54 | 결혼정보회사 기사 | rendered-page |
| [vol-12-page-055.jpg](../assets/pages/vol-12/vol-12-page-055.jpg) | 55 | 중매 시장 급팽창 기사 | rendered-page |
| [vol-12-page-057.jpg](../assets/pages/vol-12/vol-12-page-057.jpg) | 57 | 작은 결혼식 설문 그래프 | rendered-page |
| [vol-12-page-059.jpg](../assets/pages/vol-12/vol-12-page-059.jpg) | 59 | 청계서당 전통 혼례 | rendered-page |
| [vol-12-page-061.jpg](../assets/pages/vol-12/vol-12-page-061.jpg) | 61 | 결혼 유형과 예상 비용 조사 | rendered-page |
| [vol-12-page-062.jpg](../assets/pages/vol-12/vol-12-page-062.jpg) | 62 | 결혼 비용·결혼식 문화 인식·비혼 이유 통계 | rendered-page |
| [vol-12-page-063.jpg](../assets/pages/vol-12/vol-12-page-063.jpg) | 63 | 혼전 동거 인식 변화 | rendered-page |
| [vol-12-page-064.jpg](../assets/pages/vol-12/vol-12-page-064.jpg) | 64 | 향후 결혼계획과 결혼생활 조사 | rendered-page |
| [vol-12-page-068.jpg](../assets/pages/vol-12/vol-12-page-068.jpg) | 68 | 성남시화장장과 화장로 수골 시설 | rendered-page |
| [vol-12-page-069.jpg](../assets/pages/vol-12/vol-12-page-069.jpg) | 69 | 성남시장례식장 원스톱 구호 | rendered-page |
| [vol-12-page-070.jpg](../assets/pages/vol-12/vol-12-page-070.jpg) | 70 | 장례식장 시설·용품 안내 | rendered-page |
| [vol-12-page-071.jpg](../assets/pages/vol-12/vol-12-page-071.jpg) | 71 | 장례 정보와 제례 안내 | rendered-page |
| [vol-12-page-072.jpg](../assets/pages/vol-12/vol-12-page-072.jpg) | 72 | 하늘추모원 실내와 위패 표기 | rendered-page |
| [vol-12-page-077.jpg](../assets/pages/vol-12/vol-12-page-077.jpg) | 77 | 개별 장례 사례 사진 | rendered-page |
| [vol-12-page-078.jpg](../assets/pages/vol-12/vol-12-page-078.jpg) | 78 | 개별 장례 절차 | rendered-page |
| [vol-12-page-079.jpg](../assets/pages/vol-12/vol-12-page-079.jpg) | 79 | 하관·회다지·평토제 | rendered-page |
| [vol-12-page-081.jpg](../assets/pages/vol-12/vol-12-page-081.jpg) | 81 | 덕양군 비위 영가군부인 기신제 개관 | rendered-page |
| [vol-12-page-082.jpg](../assets/pages/vol-12/vol-12-page-082.jpg) | 82 | 덕양군 비위 기신제 진설 | rendered-page |
| [vol-12-page-083.jpg](../assets/pages/vol-12/vol-12-page-083.jpg) | 83 | 기신제 출주·분향강신·홀기 | rendered-page |
| [vol-12-page-085.jpg](../assets/pages/vol-12/vol-12-page-085.jpg) | 85 | 기신제 독축·축문·첨작 | rendered-page |
| [vol-12-page-086.jpg](../assets/pages/vol-12/vol-12-page-086.jpg) | 86 | 기신제 사신례·합문·분축례·음복 | rendered-page |
| [vol-12-page-087.jpg](../assets/pages/vol-12/vol-12-page-087.jpg) | 87 | 새벽 기신제의 기원 | rendered-page |
| [vol-12-page-092.jpg](../assets/pages/vol-12/vol-12-page-092.jpg) | 92 | 전주이씨 덕양군파 세일제 절차 1 | rendered-page |
| [vol-12-page-094.jpg](../assets/pages/vol-12/vol-12-page-094.jpg) | 94 | 전주이씨 덕양군파 세일제 절차 2 | rendered-page |
| [vol-12-page-095.jpg](../assets/pages/vol-12/vol-12-page-095.jpg) | 95 | 전주이씨 덕양군파 세일제 운영 | rendered-page |
| [vol-12-page-096.jpg](../assets/pages/vol-12/vol-12-page-096.jpg) | 96 | 세일제 제관 분방기와 종중 기반 | rendered-page |
| [vol-12-page-121.jpg](../assets/pages/vol-12/vol-12-page-121.jpg) | 121 | 고등동 산제사 상차림과 주민 잔치 | rendered-page |
| [vol-12-page-122.jpg](../assets/pages/vol-12/vol-12-page-122.jpg) | 122 | 판교 회나무 고사 | rendered-page |
| [vol-12-page-123.jpg](../assets/pages/vol-12/vol-12-page-123.jpg) | 123 | 회나무 고사 절차 | rendered-page |
| [vol-12-page-124.jpg](../assets/pages/vol-12/vol-12-page-124.jpg) | 124 | 8·10 성남항쟁 신문 기사 | rendered-page |
| [vol-12-page-125.jpg](../assets/pages/vol-12/vol-12-page-125.jpg) | 125 | 수정구·중원구 점집 분포 | rendered-page |

## 공용 stats.md 병합 후보

| 원문 쪽 | 유형 | 대상 | 값 | 비고 |
| --- | --- | --- | --- | --- |
| 6 | 인구/세대 | 성남 인구와 세대 변화 | 2003년 약 97만 명·35만 세대, 2013년 약 98만 명·38.5만 세대, 2024년 말 약 91만 명·41만 세대 | 인구는 감소, 세대는 약 20% 증가 |
| 8 | 주거 | 해방 이전 성남 지역 살림집 잔존 사례 | 12채 | 1999년 경기문화재단 조사, 안채는 ㄱ자형 또는 역ㄱ자형 |
| 12 | 주거/집성촌 | 수내동가옥과 수내리 집성촌 | 가옥 약 150-200년 추정, 총 70여 호 중 한산이씨 30여 호 | 1934년 자료에는 한산이씨 28호, 김해김씨 15호 |
| 13-16 | 주거 | 판교 연안이씨 종가 개량 사례 | 1942년 건축, 안채 6칸, 1987년 개량기와, 1990년대 초 기름보일러 | 전통 살림집의 단계적 현대화 사례 |
| 18 | 주거/개발 | 판교동 개나리마을 | 1978년 조성, 1km 강제 이주, 약 8,000평, 25평 2층 양옥과 10평 창고 | 전국 최초 취락구조개선 시범 마을로 설명 |
| 19 | 주거정책 | 1978년 경기도 취락구조개선사업 | A형 6개 마을, B형 70개 마을, 총 76개 마을 | 2km 이내 불량 독립주택 10동 이상이면 새 마을 조성 기준 |
| 19-20 | 주거정책 | 농촌표준주택 | 택지 50-120평, 주택 15·18·25평형, 총 12종류 | 25평형은 가족원 6-8명, 건축비 약 300만 원 |
| 21-23 | 도시주택 | 분당신도시 주택 공급 | 약 540만 평, 9만 7,000호 | 도시형 주택과 대단위 아파트단지 형성 |
| 23 | 주택통계 | 성남시 주택 중 아파트 비중 | 2022년 전체 약 346,170호 중 아파트 193,092호 | 전체 주택의 절반 이상 |
| 30 | 외식 | 단대동 닭죽촌 | 1980-1990년대 전성기 약 50여 호, 2003년 11개 동 22개소, 2023년 17개 식당·1개 커피숍 | 남한산성 정비 사업 이후 현 위치 정착 |
| 31 | 외식 | 여수동 갈매기살촌 | 전성기 식당 30여 곳, 약 20여 년 성업 | 분당 개발과 시청 이전·공공주택 조성으로 해체 |
| 45 | 혼례통계 | 결혼제도 인식 조사 | 700개 조사구, 12,000가구 표본, 응답자 14,149명, 동의 약 28%, 비동의 약 71.9% | 2021년 통계청 조사 |
| 46 | 혼례통계 | 1977년 경기도 혼례 방식 조사 | 171개 마을, 구식결혼 77건, 신식결혼 82건 | 1970년대가 현대 혼례문화의 분수령 |
| 47-48 | 혼례통계 | 혼인 건수와 결혼식 형태 | 1980-1995년 약 40만 건 유지, 2021년 192,507건; 2000년 현대식 결혼식 90.9% | 2000년 결혼식 형태 조사 응답자 637명 |
| 49 | 시설 | 성남시 예식장 | 1980년대 27개소, 2024년 12곳 | 2024년 분당구 8곳, 수정구 3곳, 중원구 1곳, 하객 보증 인원 대부분 150명 이상 |
| 51-52 | 웨딩산업 | 결혼 준비 대행업과 비용 | 1985년 평균 결혼 비용 882만 원, 1992년 1,769만 원 | 1990년대 초 웨딩 대행업 성장과 결혼박람회 확산 |
| 52 | 웨딩산업 | 판교 현대백화점 웨딩박람회 | 2023년 2월부터 누적 방문객 3,000쌍 이상 | 성남 지역 웨딩 산업 사례 |
| 55 | 결혼정보업 | 결혼정보업계 매출과 회원 수 | 1990년 50억 원 -> 1998년 500억 원; 회원 65명 -> 1,233명 -> 3,938명 -> 7,950명 | 1990년대 결혼정보회사 급성장 |
| 56-57 | 혼례인식 | 작은 결혼식 선호 | 미혼남녀 286명 중 남성 61.0%, 여성 48.8% | 2012년 설문조사 |
| 61 | 혼례통계 | 결혼 유형 | 연애결혼 57.0%, 연애+중매 19.5%, 중매 23.5% | 2000년 통계청 설문조사 |
| 61-62 | 혼례비용 | 적정 결혼 비용 인식 | 2011년 1,000만-5,000만 원 41.8%; 2015년 1,000만-3,000만 원 46.2% | 예식비용 1,000만-3,000만 원 고려 48.2% |
| 62 | 혼례비용 | 결혼식 문화 과도성 인식 | 2016년 약 75.4%, 2022년 약 73.1%가 과도하다고 응답 | 약간 과도+매우 과도 합산 |
| 62 | 비혼요인 | 결혼하지 않는 이유 | 2022년 결혼자금 부족 28.7%, 고용 불안 14.6%; 2024년 결혼자금 부족 31.3%, 고용 불안 12.9% | 경제적 이유가 가장 큰 범주 |
| 63 | 가족인식 | 혼전 동거 인식 | 2008년 동의 약 42%, 2024년 약 67.5% | 2018년을 기점으로 찬성이 반대를 앞섬 |
| 64 | 결혼의향 | 향후 결혼계획 | 2019년 64.8%, 2022년 61.8%; 남성 68.7%, 여성 54.2% | 2022년 조사 기준 |
| 64 | 결혼생활 | 남편과의 결혼생활 조사 | 여성 9,997명 대상, 남편 신뢰 92.7%, 만족 관련 응답 약 75% 이상 | 2022년 통계청 조사 |
| 66-67 | 장례 | 현대 장례 환경 | 2024년 화장률 93%, 2023년 전국 장례식장 1,117개소 | 도시 장례식장 중심의 장례문화 |
| 67 | 장례시설 | 성남시 장례식장 | 총 8개소, 공영 2개소 | 성남시장례식장과 성남시의료원 장례식장 |
| 68 | 화장시설 | 성남시화장장 | 1982년 화장로 3기 출발, 2024년 화장로 15기·관망실 15개 | 화장장·장례식장·봉안당 원스톱 구조 |
| 69 | 장례비용 | 성남시화장장·추모원 사용료 | 화장장 15세 이상 관내 5만 원·관외 100만 원; 추모원 관내 10만 원·관외 100만 원 | 관내/관외 차등 |
| 70 | 장례시설 | 성남시장례식장 빈소 | 110평형 1호실 28테이블 112석, 24시간 관내 48만 원·관외 96만 원 | 안치실 관내 4.5만 원·관외 6만 원, 영결식장 관내 3만 원·관외 6만 원 |
| 81-82 | 제례 | 덕양군 비위 영가군부인 기신제 | 덕양군 1524-1581, 영가군부인 1521-1593, 2024년 431주기, 종중 성원 20여 명 | 10월 19일 새벽 3시 준비, 4시 봉행 |
| 87-90 | 제례시간 | 궐명행사 시간 해석 | 자시 23-01시, 축시 01-03시, 인시 03-05시, 질명은 대략 4시경 | 새벽 기신제의 예학적 근거 |
| 90-93 | 제례 | 덕양군파 세일제 | 17위(17실) 합동 세일제, 분방기 제관 91명 | 1-7실 개별 독축, 8-17실 합동 독축 |
| 119 | 마을신앙 | 2003년 성남 동제 전승 현황 | 총 23개 마을 중 13개 단절, 10개 전승 | 분당구 12개소 중 4개소, 중원구 4개소 중 1개소 전승으로 서술 |
| 120 | 마을신앙 | 고등동 산신도와 산제사 | 산신도 130cm x 93cm, 2001년부터 용천사 위탁, 음력 11월 1일 새벽 6시 | 과거 100근 돼지를 메고 산제당에 올랐다는 제보 |
| 121 | 마을신앙 | 고등동 산제사 원주민 기반 | 원주민 50여 명, 주민의 절반 정도 | 산제사의 지속 배경 |
| 122-123 | 재현민속 | 판교 쌍용거줄다리기와 회나무 고사 | 1980년 재현, 1984년부터 민속예술제 참가, 2001년부터 주민 추진위 재현, 2024년 오전 9시 30분 시작·약 30분 진행 | 정월 보름 당산나무 고사의 현대적 재현 |
| 124 | 도시민속 | 광주대단지 이주민 생활 조건 | 1971년 6월 기준 직업 보유 약 5% | 점집 거리 형성 맥락으로 제시 |
| 125 | 점복 | 수정구·중원구 점집 | 2024년 155개 | Naver 지도 등록 점집·운세·사주 기준, 미등록 포함 시 더 많을 가능성 |

## source-page-index.md 병합 후보

| 원문 쪽 | 표·자료 | 활용 |
| --- | --- | --- |
| 5-7 | 민속 서술의 전제 | 성남 민속을 산업화 이전 잔존보다 수도권 확장과 개발 이후 생활양식 변화로 설정 |
| 8-12 | 전통 살림집과 수내동가옥 | 한옥 구조, 사당, 장독대, 수내동 한산이씨 집성촌, 수내동가옥 보존 사례 |
| 13-20 | 20세기 개량 주택과 판교 개나리마을 | 새마을운동·취락구조개선사업·농촌표준주택의 성남 적용 |
| 21-26 | 도시형 주택·아파트·오피스텔 | 광주대단지 이후 도시형 주거, 분당 아파트, 1-2인 거주 공간 변화 |
| 27-34 | 성남 외식문화 | 단대동 닭죽촌, 여수동 갈매기살촌, 분당 근린주구형 외식권, 판교 파인 다이닝 |
| 35-41 | 의생활과 의례복 | 출생복·돌복·혼례복·상복·제례복의 현대적 변화 |
| 45-65 | 혼례 변화와 통계 | 1970년대 신식 결혼식, 웨딩 산업, 결혼정보회사, 스드메, 결혼 비용·동거·결혼 의향 통계 |
| 66-80 | 상례와 장례 | 장례식장·화장장·봉안당 서비스, 장례 정보의 예학적 비판, 개별 장례 사례 |
| 81-96 | 덕양군파 기신제와 세일제 | 새벽 궐명행사, 기신제 절차, 17실 세일제, 종중 기반 의례 운영 |
| 98-117 | 월별 세시풍속 | 설, 대보름, 봄·여름·가을·겨울 풍속과 도시화 이후 잔존 양상 |
| 118-125 | 민간신앙 | 마을신앙 전승 현황, 고등동 산제사, 회나무 고사, 광주대단지와 점집 분포 |

## 확인 메모

- 12권은 원문 전체에 텍스트층이 있어 OCR을 사용하지 않았다.
- 도판·그래프·신문 지면·사진이 의미를 갖는 쪽은 페이지 단위 이미지로 보존했다.
- 전통 살림집 배치도처럼 도판 내부 라벨이 텍스트층에서 깨지는 쪽은 렌더링 이미지가 원문 감사의 기준이다.
- 혼례 통계 표와 장례 사용료·시설 수치, 마을신앙 전승 현황은 중앙 `stats.md`에 병합할 가치가 높다.
- 완료 범위 밖으로 넘긴 쪽은 없다.
