# 성남시사 50년사 Markdown Index

성남시 공식 `성남시사(50년사)` 게시판에서 내려받은 Index 및 제1-50권 PDF를 OCR 없이 PDF 내장 텍스트층 중심으로 Markdown화한 컬렉션이다. 각 권은 원문 쪽 번호, 페이지 이미지, LLM 단일 번들을 함께 보존한다.

## 처리 상태

- 전권 Markdown: 50/50
- 전권 LLM 번들: 50/50
- 렌더링 페이지 이미지: 5,864개
- OCR 사용: false
- 공용 병합 방식: 1-4권은 직접 변환·검수, 5-50권은 보조 에이전트 권별 초안과 통합 메모를 coordinator가 병합

| 권 | 제목 | 원본 PDF | 쪽수 | 이미지 | 상태 | 산출물 |
|---:|---|---|---:|---:|---|---|
| Index | 성남시사(Index) | `../../sources/seongnam-history-50-index.pdf` | 72 | - | source-downloaded | - |
| 1 | 제1권 성남의 자연환경 | `../../sources/seongnam-history-50-vol-01.pdf` | 112 | 10 | text-layer-reviewed | [vol-01-natural-environment.md](vol-01-natural-environment.md) / [LLM](../../dist/seongnam-history-50-vol-01.llm.md) |
| 2 | 제2권 성남의 인구 및 성씨와 토지 이용의 변화 | `../../sources/seongnam-history-50-vol-02.pdf` | 160 | 41 | text-layer-reviewed | [vol-02-population-clans-landuse.md](vol-02-population-clans-landuse.md) / [LLM](../../dist/seongnam-history-50-vol-02.llm.md) |
| 3 | 제3권 옛 지도와 지리지로 보는 성남 | `../../sources/seongnam-history-50-vol-03.pdf` | 120 | 50 | text-layer-reviewed | [vol-03-old-maps-geographies-toponyms.md](vol-03-old-maps-geographies-toponyms.md) / [LLM](../../dist/seongnam-history-50-vol-03.llm.md) |
| 4 | 제4권 성남의 교통로와 장시의 발달 | `../../sources/seongnam-history-50-vol-04.pdf` | 152 | 80 | text-layer-reviewed | [vol-04-transport-routes-markets.md](vol-04-transport-routes-markets.md) / [LLM](../../dist/seongnam-history-50-vol-04.llm.md) |
| 5 | 제5권 역사① 선사시대부터 고려시대까지의 성남 | `../../sources/seongnam-history-50-vol-05.pdf` | 120 | 54 | text-layer-reviewed | [vol-05-history-prehistory-to-goryeo.md](vol-05-history-prehistory-to-goryeo.md) / [LLM](../../dist/seongnam-history-50-vol-05.llm.md) |
| 6 | 제6권 역사② 조선시대의 성남 | `../../sources/seongnam-history-50-vol-06.pdf` | 112 | 45 | text-layer-reviewed | [vol-06-joseon-era-seongnam.md](vol-06-joseon-era-seongnam.md) / [LLM](../../dist/seongnam-history-50-vol-06.llm.md) |
| 7 | 제7권 역사③ 성남의 의병 항쟁과 독립투쟁사 | `../../sources/seongnam-history-50-vol-07.pdf` | 120 | 40 | text-layer-reviewed | [vol-07-righteous-army-independence-struggle.md](vol-07-righteous-army-independence-struggle.md) / [LLM](../../dist/seongnam-history-50-vol-07.llm.md) |
| 8 | 제8권 역사④ 광주대단지와 8·10성남(광주대단지)항쟁 | `../../sources/seongnam-history-50-vol-08.pdf` | 112 | 86 | text-layer-reviewed | [vol-08-gwangju-daedanji-8-10-uprising.md](vol-08-gwangju-daedanji-8-10-uprising.md) / [LLM](../../dist/seongnam-history-50-vol-08.llm.md) |
| 9 | 제9권 역사⑤ 성남시 승격과 도시개발 50년 | `../../sources/seongnam-history-50-vol-09.pdf` | 136 | 103 | text-layer-reviewed | [vol-09-cityhood-urban-development-50-years.md](vol-09-cityhood-urban-development-50-years.md) / [LLM](../../dist/seongnam-history-50-vol-09.llm.md) |
| 10 | 제10권 성남 역사 인물 50선 | `../../sources/seongnam-history-50-vol-10.pdf` | 144 | 107 | text-layer-reviewed | [vol-10-historical-figures-50.md](vol-10-historical-figures-50.md) / [LLM](../../dist/seongnam-history-50-vol-10.llm.md) |
| 11 | 제11권 성남의 문화유산 | `../../sources/seongnam-history-50-vol-11.pdf` | 160 | 160 | text-layer-reviewed | [vol-11-cultural-heritage.md](vol-11-cultural-heritage.md) / [LLM](../../dist/seongnam-history-50-vol-11.llm.md) |
| 12 | 제12권 성남의 민속 | `../../sources/seongnam-history-50-vol-12.pdf` | 128 | 57 | text-layer-reviewed | [vol-12-folklore.md](vol-12-folklore.md) / [LLM](../../dist/seongnam-history-50-vol-12.llm.md) |
| 13 | 제13권 성남시 선거와 지방자치 30년 | `../../sources/seongnam-history-50-vol-13.pdf` | 160 | 119 | text-layer-reviewed | [vol-13-elections-local-autonomy.md](vol-13-elections-local-autonomy.md) / [LLM](../../dist/seongnam-history-50-vol-13.llm.md) |
| 14 | 제14권 성남시 자치행정과 지방재정 | `../../sources/seongnam-history-50-vol-14.pdf` | 184 | 184 | text-layer-reviewed | [vol-14-local-administration-finance.md](vol-14-local-administration-finance.md) / [LLM](../../dist/seongnam-history-50-vol-14.llm.md) |
| 15 | 제15권 성남 지역 시민운동과 참여 자치 | `../../sources/seongnam-history-50-vol-15.pdf` | 136 | 90 | text-layer-reviewed | [vol-15-civic-movement-participatory-governance.md](vol-15-civic-movement-participatory-governance.md) / [LLM](../../dist/seongnam-history-50-vol-15.llm.md) |
| 16 | 제16권 성남시 경제와 산업 | `../../sources/seongnam-history-50-vol-16.pdf` | 144 | 144 | text-layer-reviewed | [vol-16-economy-industry.md](vol-16-economy-industry.md) / [LLM](../../dist/seongnam-history-50-vol-16.llm.md) |
| 17 | 제17권 성남의 산업구조 | `../../sources/seongnam-history-50-vol-17.pdf` | 160 | 160 | text-layer-reviewed | [vol-17-industrial-structure.md](vol-17-industrial-structure.md) / [LLM](../../dist/seongnam-history-50-vol-17.llm.md) |
| 18 | 제18권 성남의 산업단지와 기업체 | `../../sources/seongnam-history-50-vol-18.pdf` | 160 | 160 | text-layer-reviewed | [vol-18-industrial-complexes-companies.md](vol-18-industrial-complexes-companies.md) / [LLM](../../dist/seongnam-history-50-vol-18.llm.md) |
| 19 | 제19권 성남 교육의 역사와 학교 교육 | `../../sources/seongnam-history-50-vol-19.pdf` | 104 | 104 | text-layer-reviewed | [vol-19-education-history-school-education.md](vol-19-education-history-school-education.md) / [LLM](../../dist/seongnam-history-50-vol-19.llm.md) |
| 20 | 제20권 성남시 청소년의 삶과 문화 | `../../sources/seongnam-history-50-vol-20.pdf` | 136 | 136 | text-layer-reviewed | [vol-20-youth-life-culture.md](vol-20-youth-life-culture.md) / [LLM](../../dist/seongnam-history-50-vol-20.llm.md) |
| 21 | 제21권 평생교육과 성남 | `../../sources/seongnam-history-50-vol-21.pdf` | 136 | 136 | text-layer-reviewed | [vol-21-lifelong-education-seongnam.md](vol-21-lifelong-education-seongnam.md) / [LLM](../../dist/seongnam-history-50-vol-21.llm.md) |
| 22 | 제22권 성남의 문화와 예술 | `../../sources/seongnam-history-50-vol-22.pdf` | 116 | 116 | text-layer-reviewed | [vol-22-culture-and-arts.md](vol-22-culture-and-arts.md) / [LLM](../../dist/seongnam-history-50-vol-22.llm.md) |
| 23 | 제23권 성남의 축제와 관광 | `../../sources/seongnam-history-50-vol-23.pdf` | 160 | 160 | text-layer-reviewed | [vol-23-festivals-tourism.md](vol-23-festivals-tourism.md) / [LLM](../../dist/seongnam-history-50-vol-23.llm.md) |
| 24 | 제24권 성남 시민의 종교와 신앙생활 | `../../sources/seongnam-history-50-vol-24.pdf` | 104 | 104 | text-layer-reviewed | [vol-24-religion-faith-life.md](vol-24-religion-faith-life.md) / [LLM](../../dist/seongnam-history-50-vol-24.llm.md) |
| 25 | 제25권 성남의 체육 | `../../sources/seongnam-history-50-vol-25.pdf` | 120 | 120 | text-layer-reviewed | [vol-25-sports.md](vol-25-sports.md) / [LLM](../../dist/seongnam-history-50-vol-25.llm.md) |
| 26 | 제26권 사회복지와 성남 | `../../sources/seongnam-history-50-vol-26.pdf` | 106 | 106 | text-layer-reviewed | [vol-26-social-welfare-seongnam.md](vol-26-social-welfare-seongnam.md) / [LLM](../../dist/seongnam-history-50-vol-26.llm.md) |
| 27 | 제27권 성남의 보건 의료와 정책 | `../../sources/seongnam-history-50-vol-27.pdf` | 104 | 104 | text-layer-reviewed | [vol-27-healthcare-policy.md](vol-27-healthcare-policy.md) / [LLM](../../dist/seongnam-history-50-vol-27.llm.md) |
| 28 | 제28권 성남의 지역 언론과 매체 | `../../sources/seongnam-history-50-vol-28.pdf` | 104 | 104 | text-layer-reviewed | [vol-28-local-media-and-press.md](vol-28-local-media-and-press.md) / [LLM](../../dist/seongnam-history-50-vol-28.llm.md) |
| 29 | 제29권 성남의 공간구조와 생활권 | `../../sources/seongnam-history-50-vol-29.pdf` | 144 | 144 | text-layer-reviewed | [vol-29-spatial-structure-living-areas.md](vol-29-spatial-structure-living-areas.md) / [LLM](../../dist/seongnam-history-50-vol-29.llm.md) |
| 30 | 제30권 성남 본시가지 일대의 변천 | `../../sources/seongnam-history-50-vol-30.pdf` | 136 | 136 | text-layer-reviewed | [vol-30-main-city-area-transformation.md](vol-30-main-city-area-transformation.md) / [LLM](../../dist/seongnam-history-50-vol-30.llm.md) |
| 31 | 제31권 상대원과 성남하이테크밸리 일대의 변천 | `../../sources/seongnam-history-50-vol-31.pdf` | 112 | 112 | text-layer-reviewed | [vol-31-sangdaewon-seongnam-high-tech-valley.md](vol-31-sangdaewon-seongnam-high-tech-valley.md) / [LLM](../../dist/seongnam-history-50-vol-31.llm.md) |
| 32 | 제32권 여수동·도촌동·야탑동 일대의 변천 | `../../sources/seongnam-history-50-vol-32.pdf` | 128 | 128 | text-layer-reviewed | [vol-32-yeosu-dochon-yatap-area-transformation.md](vol-32-yeosu-dochon-yatap-area-transformation.md) / [LLM](../../dist/seongnam-history-50-vol-32.llm.md) |
| 33 | 제33권 1기 신도시 분당의 변천① | `../../sources/seongnam-history-50-vol-33.pdf` | 112 | 112 | text-layer-reviewed | [vol-33-bundang-new-town-transition-1.md](vol-33-bundang-new-town-transition-1.md) / [LLM](../../dist/seongnam-history-50-vol-33.llm.md) |
| 34 | 제34권 1기 신도시 분당의 변천② | `../../sources/seongnam-history-50-vol-34.pdf` | 112 | 112 | text-layer-reviewed | [vol-34-first-newtown-bundang-transition-2.md](vol-34-first-newtown-bundang-transition-2.md) / [LLM](../../dist/seongnam-history-50-vol-34.llm.md) |
| 35 | 제35권 판교 일대의 변천 | `../../sources/seongnam-history-50-vol-35.pdf` | 152 | 152 | text-layer-reviewed | [vol-35-pangyo-area-transformation.md](vol-35-pangyo-area-transformation.md) / [LLM](../../dist/seongnam-history-50-vol-35.llm.md) |
| 36 | 제36권 운중동·대장동 일대의 변천 | `../../sources/seongnam-history-50-vol-36.pdf` | 112 | 112 | text-layer-reviewed | [vol-36-unjung-daejang-area-transformation.md](vol-36-unjung-daejang-area-transformation.md) / [LLM](../../dist/seongnam-history-50-vol-36.llm.md) |
| 37 | 제37권 위례신도시 일대의 변천 | `../../sources/seongnam-history-50-vol-37.pdf` | 112 | 112 | text-layer-reviewed | [vol-37-wirye-new-town-area-transformation.md](vol-37-wirye-new-town-area-transformation.md) / [LLM](../../dist/seongnam-history-50-vol-37.llm.md) |
| 38 | 제38권 고등·신촌지구 일대의 변천 | `../../sources/seongnam-history-50-vol-38.pdf` | 136 | 136 | text-layer-reviewed | [vol-38-godeung-sinchon-district-transformation.md](vol-38-godeung-sinchon-district-transformation.md) / [LLM](../../dist/seongnam-history-50-vol-38.llm.md) |
| 39 | 제39권 성남 콘텐츠 50선 | `../../sources/seongnam-history-50-vol-39.pdf` | 152 | 152 | text-layer-reviewed | [vol-39-seongnam-content-50.md](vol-39-seongnam-content-50.md) / [LLM](../../dist/seongnam-history-50-vol-39.llm.md) |
| 40 | 제40권 토박이와 이주민의 성남살이 | `../../sources/seongnam-history-50-vol-40.pdf` | 152 | 152 | text-layer-reviewed | [vol-40-natives-migrants-seongnam-life.md](vol-40-natives-migrants-seongnam-life.md) / [LLM](../../dist/seongnam-history-50-vol-40.llm.md) |
| 41 | 제41권 모란 상설시장과 민속5일장 | `../../sources/seongnam-history-50-vol-41.pdf` | 120 | 120 | text-layer-reviewed | [vol-41-moran-permanent-market-folk-five-day-market.md](vol-41-moran-permanent-market-folk-five-day-market.md) / [LLM](../../dist/seongnam-history-50-vol-41.llm.md) |
| 42 | 제42권 성남의 전통 민속놀이 | `../../sources/seongnam-history-50-vol-42.pdf` | 120 | 120 | text-layer-reviewed | [vol-42-traditional-folk-games.md](vol-42-traditional-folk-games.md) / [LLM](../../dist/seongnam-history-50-vol-42.llm.md) |
| 43 | 제43권 판교 테크노컬처밸리 | `../../sources/seongnam-history-50-vol-43.pdf` | 128 | 128 | text-layer-reviewed | [vol-43-pangyo-techno-culture-valley.md](vol-43-pangyo-techno-culture-valley.md) / [LLM](../../dist/seongnam-history-50-vol-43.llm.md) |
| 44 | 제44권 판교 게임·콘텐츠특구 | `../../sources/seongnam-history-50-vol-44.pdf` | 104 | 104 | text-layer-reviewed | [vol-44-pangyo-game-content-special-zone.md](vol-44-pangyo-game-content-special-zone.md) / [LLM](../../dist/seongnam-history-50-vol-44.llm.md) |
| 45 | 제45권 성남 주택의 변화상과 특색 건축물 | `../../sources/seongnam-history-50-vol-45.pdf` | 136 | 136 | text-layer-reviewed | [vol-45-housing-change-distinctive-architecture.md](vol-45-housing-change-distinctive-architecture.md) / [LLM](../../dist/seongnam-history-50-vol-45.llm.md) |
| 46 | 제46권 한 권으로 읽는 어린이 성남시사 | `../../sources/seongnam-history-50-vol-46.pdf` | 136 | 136 | text-layer-reviewed | [vol-46-childrens-seongnam-history.md](vol-46-childrens-seongnam-history.md) / [LLM](../../dist/seongnam-history-50-vol-46.llm.md) |
| 47 | 성남시사 50년사 제47권 한 권으로 읽는 청소년 성남시사 | `../../sources/seongnam-history-50-vol-47.pdf` | 144 | 144 | text-layer-reviewed | [vol-47-youth-seongnam-city-history.md](vol-47-youth-seongnam-city-history.md) / [LLM](../../dist/seongnam-history-50-vol-47.llm.md) |
| 48 | 제48권 포토에세이, 성남 ALIGN | `../../sources/seongnam-history-50-vol-48.pdf` | 128 | 128 | text-layer-reviewed | [vol-48-photo-essay-seongnam-align.md](vol-48-photo-essay-seongnam-align.md) / [LLM](../../dist/seongnam-history-50-vol-48.llm.md) |
| 49 | 제49권 자료로 보는 성남 | `../../sources/seongnam-history-50-vol-49.pdf` | 144 | 144 | text-layer-reviewed | [vol-49-data-for-seongnam.md](vol-49-data-for-seongnam.md) / [LLM](../../dist/seongnam-history-50-vol-49.llm.md) |
| 50 | 제50권 길라잡이 성남 사전(事典) | `../../sources/seongnam-history-50-vol-50.pdf` | 264 | 264 | text-layer-reviewed | [vol-50-guidebook-seongnam-dictionary.md](vol-50-guidebook-seongnam-dictionary.md) / [LLM](../../dist/seongnam-history-50-vol-50.llm.md) |

## 보조 파일

- [source-page-index.md](source-page-index.md)
- [stats.md](stats.md)
- [figures.md](figures.md)
- [toponyms.md](toponyms.md)
- [transport-markets.md](transport-markets.md)
- [manifest.yml](manifest.yml)
- [collection manifest](../../dist/seongnam-city-history-50.manifest.json)
