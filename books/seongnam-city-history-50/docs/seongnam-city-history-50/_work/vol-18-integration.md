# Vol 18 Integration Note: 제18권 성남의 산업단지와 기업체

## 처리 범위

- 담당 범위: 18권 전용 산출물만 생성했다.
- 원천 PDF: `books/seongnam-city-history-50/sources/seongnam-history-50-vol-18.pdf`
- 공식 URL: `https://www.seongnam.go.kr/city/1001112/30566/bbsView.do?idx=378676`
- PDF 쪽수: 160쪽
- OCR 사용: false. `pdftotext -layout`로 임베디드 텍스트층을 추출했다.
- 처리 상태: 전체 1-160쪽 텍스트층 반영. 완료 범위 밖으로 넘긴 쪽은 없다.
- 페이지 이미지: 1-160쪽 전체를 `docs/seongnam-city-history-50/assets/pages/vol-18-page-*.jpg`로 렌더링했다.
- 공용 파일 미편집: `README.md`, `.gitattributes`, `index.md`, `manifest.yml`, `stats.md`, `figures.md`, `source-page-index.md`는 건드리지 않았다.

## 생성 파일

- `docs/seongnam-city-history-50/vol-18-industrial-complexes-companies.md`
- `dist/seongnam-history-50-vol-18.llm.md`
- `docs/seongnam-city-history-50/assets/pages/vol-18-page-*.jpg` 160개
- `docs/seongnam-city-history-50/_work/vol-18-integration.md`

## 공용 인덱스 병합 후보: 목차

| Part | 원문 쪽 | 내용 |
| --- | --- | --- |
| 앞부분 | 1-3 | 표지와 권별 목차 |
| 1 | 4-24 | 성남시 주요 산업시설 소개: 성남하이테크밸리, 판교테크노밸리, 지식산업센터 |
| 2 | 25-85 | 성남 소재 주요 민간기업체 현황: 두산, HD현대, 안랩, 한글과컴퓨터, SOOP, 카카오, 삼성, SK, 게임·바이오·방산·제조 기업 |
| 3 | 86-113 | 성남 소재 주요 공기업과 공공기관: 한국전자기술연구원, 한국지역난방공사, 한국학중앙연구원, KOICA 등 |
| 4 | 114-123 | 성남시 소재 기업 지원 기관: 상공회의소, 산업단지관리공단, 산업진흥원, 혁신지원센터 등 |
| 부록 | 124-159 | 지식산업센터 현황과 성남하이테크밸리 입주기업 리스트 |
| 뒷부분 | 160 | 판권 |

## 공용 figures.md 병합 후보

- 18권은 모든 쪽을 렌더링했으나, 공용 도판 색인에는 아래 쪽을 우선 병합하면 된다.

| 파일 | 원문 쪽 | 내용 | 처리 상태 |
| --- | --- | --- | --- |
| [vol-18-page-001.jpg](../assets/pages/vol-18-page-001.jpg) | 1 | 표지와 권명: 산업단지·기업체 권의 범위 확인 | rendered-page |
| [vol-18-page-002.jpg](../assets/pages/vol-18-page-002.jpg) | 2 | 권별 목차 1: 성남시 주요 산업시설 소개와 민간기업체 목차 | rendered-page |
| [vol-18-page-003.jpg](../assets/pages/vol-18-page-003.jpg) | 3 | 권별 목차 2: 공공기관·기업지원기관·부록 목차 | rendered-page |
| [vol-18-page-006.jpg](../assets/pages/vol-18-page-006.jpg) | 6 | 성남하이테크밸리 연혁 표 | rendered-page |
| [vol-18-page-007.jpg](../assets/pages/vol-18-page-007.jpg) | 7 | 성남하이테크밸리 입지 여건 표 | rendered-page |
| [vol-18-page-008.jpg](../assets/pages/vol-18-page-008.jpg) | 8 | 성남하이테크밸리 교통 여건과 조성면적 표 | rendered-page |
| [vol-18-page-009.jpg](../assets/pages/vol-18-page-009.jpg) | 9 | 성남하이테크밸리 입주업체 현황 | rendered-page |
| [vol-18-page-010.jpg](../assets/pages/vol-18-page-010.jpg) | 10 | 성남하이테크밸리 업종별 입주 현황과 비중 | rendered-page |
| [vol-18-page-011.jpg](../assets/pages/vol-18-page-011.jpg) | 11 | 성남하이테크밸리 최근 20년 업종 변화 비교 | rendered-page |
| [vol-18-page-012.jpg](../assets/pages/vol-18-page-012.jpg) | 12 | 성남하이테크밸리 종업원·생산 실적 | rendered-page |
| [vol-18-page-013.jpg](../assets/pages/vol-18-page-013.jpg) | 13 | 성남하이테크밸리 수출 실적 | rendered-page |
| [vol-18-page-014.jpg](../assets/pages/vol-18-page-014.jpg) | 14 | 판교테크노밸리 조성 목적과 연혁 시작 | rendered-page |
| [vol-18-page-017.jpg](../assets/pages/vol-18-page-017.jpg) | 17 | 제2판교테크노밸리 입지 여건 | rendered-page |
| [vol-18-page-018.jpg](../assets/pages/vol-18-page-018.jpg) | 18 | 판교테크노밸리와 제2판교테크노밸리 조성 면적 | rendered-page |
| [vol-18-page-019.jpg](../assets/pages/vol-18-page-019.jpg) | 19 | 판교테크노밸리 입주업체·법정 유형·업종 현황 | rendered-page |
| [vol-18-page-020.jpg](../assets/pages/vol-18-page-020.jpg) | 20 | 판교테크노밸리 종업원·매출 실적 | rendered-page |
| [vol-18-page-022.jpg](../assets/pages/vol-18-page-022.jpg) | 22 | 성남하이테크밸리 지식산업센터 현황 시작 | rendered-page |
| [vol-18-page-023.jpg](../assets/pages/vol-18-page-023.jpg) | 23 | 성남하이테크밸리 지식산업센터 현황 계속 | rendered-page |
| [vol-18-page-024.jpg](../assets/pages/vol-18-page-024.jpg) | 24 | 제2판교테크노밸리·개별 입지 지식산업센터 현황 | rendered-page |
| [vol-18-page-026.jpg](../assets/pages/vol-18-page-026.jpg) | 26 | 두산디지털이노베이션 기업 개요 | rendered-page |
| [vol-18-page-031.jpg](../assets/pages/vol-18-page-031.jpg) | 31 | HD현대 기업 개요 | rendered-page |
| [vol-18-page-038.jpg](../assets/pages/vol-18-page-038.jpg) | 38 | 안랩 기업 개요 | rendered-page |
| [vol-18-page-040.jpg](../assets/pages/vol-18-page-040.jpg) | 40 | 한글과컴퓨터 기업 개요 | rendered-page |
| [vol-18-page-041.jpg](../assets/pages/vol-18-page-041.jpg) | 41 | SOOP 기업 개요 | rendered-page |
| [vol-18-page-044.jpg](../assets/pages/vol-18-page-044.jpg) | 44 | 카카오 판교 아지트 기업 개요 | rendered-page |
| [vol-18-page-050.jpg](../assets/pages/vol-18-page-050.jpg) | 50 | 삼성SDS 판교 IT 캠퍼스·판교 물류 캠퍼스 | rendered-page |
| [vol-18-page-052.jpg](../assets/pages/vol-18-page-052.jpg) | 52 | SK C&C와 SK디스커버리 | rendered-page |
| [vol-18-page-061.jpg](../assets/pages/vol-18-page-061.jpg) | 61 | 스마일게이트 기업 개요 | rendered-page |
| [vol-18-page-063.jpg](../assets/pages/vol-18-page-063.jpg) | 63 | NC소프트 기업 개요 | rendered-page |
| [vol-18-page-065.jpg](../assets/pages/vol-18-page-065.jpg) | 65 | 넥슨코리아 기업 개요 | rendered-page |
| [vol-18-page-069.jpg](../assets/pages/vol-18-page-069.jpg) | 69 | 네이버 기업 개요 | rendered-page |
| [vol-18-page-070.jpg](../assets/pages/vol-18-page-070.jpg) | 70 | 차병원·바이오그룹 기업 개요 | rendered-page |
| [vol-18-page-074.jpg](../assets/pages/vol-18-page-074.jpg) | 74 | 한화에어로스페이스 판교 R&D 캠퍼스 | rendered-page |
| [vol-18-page-078.jpg](../assets/pages/vol-18-page-078.jpg) | 78 | LIG넥스원 연구소 | rendered-page |
| [vol-18-page-080.jpg](../assets/pages/vol-18-page-080.jpg) | 80 | 한국타이어앤테크놀로지 | rendered-page |
| [vol-18-page-085.jpg](../assets/pages/vol-18-page-085.jpg) | 85 | NS홈쇼핑 | rendered-page |
| [vol-18-page-087.jpg](../assets/pages/vol-18-page-087.jpg) | 87 | 한국전자기술연구원 | rendered-page |
| [vol-18-page-090.jpg](../assets/pages/vol-18-page-090.jpg) | 90 | 한국지역난방공사 | rendered-page |
| [vol-18-page-098.jpg](../assets/pages/vol-18-page-098.jpg) | 98 | 한국학중앙연구원 | rendered-page |
| [vol-18-page-101.jpg](../assets/pages/vol-18-page-101.jpg) | 101 | 한국국제협력단 | rendered-page |
| [vol-18-page-103.jpg](../assets/pages/vol-18-page-103.jpg) | 103 | 한국디자인진흥원 | rendered-page |
| [vol-18-page-111.jpg](../assets/pages/vol-18-page-111.jpg) | 111 | 한국정보통신기술협회 | rendered-page |
| [vol-18-page-115.jpg](../assets/pages/vol-18-page-115.jpg) | 115 | 성남상공회의소 | rendered-page |
| [vol-18-page-116.jpg](../assets/pages/vol-18-page-116.jpg) | 116 | 성남산업단지관리공단 | rendered-page |
| [vol-18-page-117.jpg](../assets/pages/vol-18-page-117.jpg) | 117 | 성남산업진흥원 | rendered-page |
| [vol-18-page-119.jpg](../assets/pages/vol-18-page-119.jpg) | 119 | 경기창조경제혁신센터 | rendered-page |
| [vol-18-page-120.jpg](../assets/pages/vol-18-page-120.jpg) | 120 | 소상공인시장진흥공단 성남센터 | rendered-page |
| [vol-18-page-121.jpg](../assets/pages/vol-18-page-121.jpg) | 121 | 메타버스 허브 | rendered-page |
| [vol-18-page-122.jpg](../assets/pages/vol-18-page-122.jpg) | 122 | 성남시혁신지원센터 | rendered-page |
| [vol-18-page-124.jpg](../assets/pages/vol-18-page-124.jpg) | 124 | 성남시 지식산업센터 현황 부록 1 | rendered-page |
| [vol-18-page-125.jpg](../assets/pages/vol-18-page-125.jpg) | 125 | 성남시 지식산업센터 현황 부록 2 | rendered-page |
| [vol-18-page-126.jpg](../assets/pages/vol-18-page-126.jpg) | 126 | 성남하이테크밸리 입주기업 리스트 시작 | rendered-page |
| [vol-18-page-159.jpg](../assets/pages/vol-18-page-159.jpg) | 159 | 성남하이테크밸리 입주기업 리스트 마지막 쪽 | rendered-page |
| [vol-18-page-160.jpg](../assets/pages/vol-18-page-160.jpg) | 160 | 판권 | rendered-page |

## 공용 stats.md 병합 후보

| 원문 쪽 | 유형 | 대상 | 값 | 비고 |
| --- | --- | --- | --- | --- |
| 5 | 산업단지 체계 | 2024년 현재 성남시 산업단지 및 인프라 | 성남하이테크밸리, 판교테크노밸리, 제2판교테크노밸리 등 4개 산업단지 및 관련 인프라 | 제2판교테크노밸리는 2024년 완공으로 서술 |
| 5 | 산업단지 계획 | 추가 조성 계획 | 제3판교테크노밸리, 정자동 제 첨단 클러스터, 시스템반도체 허브 등 3개 산업단지 | 제3판교테크노밸리는 2025년 완공 예정으로 서술 |
| 6 | 면적 | 성남하이테크밸리 규모 | 151만 2,886㎡, 45만 7,648평 | 상대원동 일대 총면적 |
| 6 | 연혁 | 성남하이테크밸리 주요 연혁 | 1968.5.7 광주대단지 조성 계획 인가, 1974.9.7 1·2공단 준공, 1976.11.12 3공단 준공, 2009.7.1 성남하이테크밸리 명칭 변경 | 성남공업단지에서 성남산업단지, 성남하이테크밸리로 이어지는 명칭 변화 |
| 8 | 토지이용 | 성남하이테크밸리 조성 면적 | 2공단 1,330,054㎡, 3공단 152,943㎡, 준공업지 29,889㎡ | 산업시설 1,164,639㎡, 지원시설 20,223㎡, 공공시설 241,336㎡, 녹지 86,688㎡ |
| 9 | 입주업체 | 성남하이테크밸리 입주업체 | 2023.12.31 기준 3,668개, 가동 2,950개, 미가동 718개 | 일반공장 278개, 지식산업센터 3,390개 |
| 10 | 업종 | 성남하이테크밸리 업종별 입주업체 | 전기·전자 1,067개, 지식·정보통신 501개, 기계 306개, 음식료 289개, 섬유·의복 272개 | 2023.12.31 기준 |
| 11 | 산업구조 변화 | 성남하이테크밸리 입주업체 변화 | 2004년 661개, 2013년 3,300개, 2023년 3,668개 | 20년간 5.5배 이상 성장으로 서술 |
| 11 | 산업구조 변화 | 성남하이테크밸리 전기·전자 비중 | 2004년 46.3%, 2013년 29.8%, 2023년 29.1% | 업종 다변화 해석의 핵심 수치 |
| 12 | 고용 | 성남하이테크밸리 종업원 | 2023년 42,682명 | 2019년 42,816명, 2021년 42,965명 최고점 |
| 12 | 생산 | 성남하이테크밸리 생산 실적 | 2023년 9조 2,248억 원 | 2000년 3조 6,046억 원 대비 156% 증가, 2010년 9조 7,016억 원 최고점 |
| 13 | 수출 | 성남하이테크밸리 수출 실적 | 2023년 7억 2,398만 7,000달러 | 표 기준 723,987천 달러, 2009년 952,670천 달러 최고점 |
| 17 | 입지 | 제2판교테크노밸리 입지 | 43만 460㎡, 13만 214평 | 시흥동·금토동 일원, 2015.12-2024 조성 |
| 18 | 면적 | 판교테크노밸리 조성 면적 | 454,964㎡, 137,621평 | 초청연구용지 48,147㎡, 일반연구용지 267,450㎡, 연구지원용지 117,651㎡, 주차장 21,716㎡ |
| 18 | 면적 | 제2판교테크노밸리 조성 면적 | 430,460㎡, 130,214평 | 산업용지 129,904㎡, 공공용지 151,840㎡ 등 |
| 19 | 입주업체 | 판교테크노밸리·제2판교테크노밸리 입주업체 | 2024.9 기준 총 1,803개 사 | 판교 1,241개 사, 제2판교 562개 사 |
| 19 | 기업규모 | 판교테크노밸리·제2판교테크노밸리 법정 유형 | 대기업 65개, 중견기업 129개, 중소기업 1,520개, 기타 89개 | 총 1,803개 사 |
| 19 | 업종 | 판교테크노밸리·제2판교테크노밸리 업종 | IT 1,172개, BT 222개, CT 162개, 기타 247개 | 2024.9 기준 |
| 20 | 고용 | 판교테크노밸리·제2판교테크노밸리 종업원 | 총 78,872명 | 판교 67,334명, 제2판교 11,538명 |
| 20 | 매출 | 판교테크노밸리·제2판교테크노밸리 매출 | 총 202조 4,000억 원 | 판교 162조 3,000억 원, 제2판교 40조 1,000억 원 |
| 21 | 제도 | 지식산업센터 법적 기준 | 3층 이상, 6개 업체 이상 입주 가능한 집합건축물 | 2009년 법률 개정으로 아파트형 공장에서 지식산업센터로 명칭 변경 |
| 22 | 지식산업센터 | 성남시 지식산업센터 | 2024.12.31 기준 총 56개소, 입주업체 3,788개 사 | 성남하이테크밸리 44개소, 제2판교테크노밸리 8개소, 개별 단지 4개소 |
| 22 | 지식산업센터 | 성남하이테크밸리 내 지식산업센터 | 44개소, 입주업체 3,284개 사 | SK엔테크노파크 입주업체 424개 사로 최다 |
| 24 | 지식산업센터 | 제2판교테크노밸리 지식산업센터 | 8개소, 입주업체 337개 사 | 경기기업성장센터 121개 사로 최다 |
| 24 | 지식산업센터 | 개별 입지 지식산업센터 | 4개소, 입주업체 167개 사 | 분당테크노파크 139개 사로 최다 |
| 46 | 기업 지배구조 | 카카오 주요 지분 설명 | 김범수 13.32%, 케이큐브홀딩스 10.51%, 국민연금 6.36%, MAXIMO PTE 6.30%, 홍은택 0.22%, 자기주식 3.16% | 본문은 총 39.87% 지분율로 설명 |
| 61 | 게임산업 | 스마일게이트 매출 규모 | 2020년 연 매출 약 1조 73억 원 | 국내 Top 5 게임 회사로 서술 |
| 124-125 | 지식산업센터 부록 | 성남시 지식산업센터 현황 | 개별 입지 4개, 제2판교테크노밸리 8개, 성남하이테크밸리 44개 항목 | 각 센터의 위치, 건축연면적, 승인일, 입주업체 수를 수록 |
| 126-159 | 기업체 목록 | 성남하이테크밸리 입주기업 리스트 | 2024.6 기준 연번 1-2831 | 회사명과 주생산품을 3단 배열로 수록 |
| 160 | 서지 | 발행 정보 | 2025년 12월 29일 발행 | 성남시 시사편찬위원회 발행, 집필 이호영·정세일 |

## source-page-index.md 병합 후보

| 원문 쪽 | 표·자료 | 활용 |
| --- | --- | --- |
| 1-3 | 표지·권별 목차 | 권명, 발간등록번호, 4개 Part와 부록 구성 확인 |
| 5-13 | 성남하이테크밸리 | 광주대단지와 공업단지 형성, 면적, 입주업체, 업종, 고용, 생산, 수출 실적 |
| 14-20 | 판교테크노밸리·제2판교테크노밸리 | 국가전략산업 클러스터, 입지, 면적, 입주기업, 종업원, 매출 실적 |
| 21-24 | 지식산업센터 | 법적 정의, 성남시 센터 수, 위치, 연면적, 입주업체 수 |
| 26-85 | 주요 민간기업체 | 두산·HD현대·안랩·한컴·SOOP·카카오·삼성·SK·게임·바이오·방산 기업 개요와 연혁 |
| 87-113 | 공기업과 공공기관 | KETI, 지역난방공사, 한국학중앙연구원, KOICA, 디자인진흥원, TTA 등 |
| 115-123 | 기업 지원 기관 | 성남상공회의소, 성남산업단지관리공단, 성남산업진흥원, 경기창조경제혁신센터, 성남시혁신지원센터 등 |
| 124-125 | 지식산업센터 부록 | 성남시 지식산업센터 56개소 현황 |
| 126-159 | 성남하이테크밸리 입주기업 리스트 | 2024.6 기준 회사명·주생산품 목록, 연번 1-2831 |
| 160 | 판권 | 발행일, 발행처, 집필자, 디자인·인쇄 정보 |

## 확인 메모

- 18권은 원문 전체에 텍스트층이 있어 OCR을 사용하지 않았다.
- 표와 부록 목록은 PDF 텍스트층에서 줄바꿈이 복잡하므로 본문에는 페이지별 `text` 코드 블록과 렌더링 이미지를 함께 보존했다.
- 부록의 성남하이테크밸리 입주기업 리스트는 126-159쪽에 걸쳐 있고 2024년 6월 기준 연번 1-2831까지 이어진다.
- 중앙 병합 시 `stats.md`에는 산업단지 면적, 입주업체, 업종, 고용, 생산, 수출, 판교 매출, 지식산업센터 수치를 우선 반영하는 것이 좋다.
- 중앙 병합 시 `figures.md`에는 6-13쪽, 17-24쪽, 124-125쪽, 126쪽과 159쪽을 우선 넣고, 필요하면 민간기업·공공기관 대표 페이지를 확장하면 된다.