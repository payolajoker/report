# LLM 작업 색인

이 파일은 LLM이 저장소를 빠르게 탐색하기 위한 작업용 색인이다. 사람에게 보여주는 설명은 `README.md`가 담당하고, 이 파일은 질문, ingest, 보고서 수정, lint 작업을 시작할 때 읽는 기계적 지도 역할을 한다.

마지막 정리: 2026-05-06

## 빠른 진입

| 목적 | 먼저 볼 곳 | 이어서 볼 곳 |
|---|---|---|
| 전체 구조 파악 | `README.md` | 이 파일의 "주제별 앵커" |
| 보고서 작성 규칙 확인 | `REPORT_STYLE.md` | 관련 하위 `AGENTS.md` |
| 최근 작업 이력 확인 | `log.md` | git history |
| 원문 PDF 재구성 자료 확인 | `books/*/docs/*/index.md` | `stats.md`, `manifest.yml`, `source-page-index.md` |
| 통계/방법론 확인 | `supplements/*/docs/` | `supplements/*/data/` |
| 지도/이미지 확인 | `assets/`, `supplements/*/images/` | 관련 보고서 본문 |

## 공개 보고서

| 문서 | 역할 | 주요 연결 |
|---|---|---|
| [대한민국 신도시의 역사](./대한민국-신도시의-역사.md) | 전근대 계획도시부터 산업·행정 계획도시, 목동·상계, 1·2·3기 신도시, 노후계획도시 정비까지 잇는 총괄 서사 | 성남시사 50년사, 분당·평촌 개발사, 한국형 신도시 가이드라인 |
| [1기·2기·3기 신도시의 근본적 차이](./1기-2기-3기-신도시의-근본적-차이.md) | 세대별 신도시 정책 문제의식과 공간 전략 비교 | 1기 신도시, 3기 신도시 개발전략, 철도망 계획 비교 |
| [위례선 트램 보고서](./위례선-트램-보고서.md) | 위례선, 트램, 환승 구조, 서울 트램 부활의 의미 | 환승저항, 서울 동남부 연담화, 철도 리서치 |
| [서울 동남부 도시 연담화 세부사례 근거정리](./서울-동남부-도시-연담화-세부사례-근거정리.md) | 미사·감일·교산·위례 등 서울 동남권 연담화 사례 정리 | 서울 1963 확장, 위례선, 성남시사, 3기 신도시 |
| [1963년 서울 대확장 연구보고서](./서울-1963-확장-연구보고서.md) | 서울 행정구역 대확장의 공개 논의, 법적 절차, 주민 반응 분석 | `supplements/seoul-1963-expansion/`, REPORT_STYLE |
| [국가철도망 구축계획과 도시철도망 구축계획 비교](./국가철도망-구축계획과-도시철도망-구축계획-비교.md) | 국가철도망과 도시철도망 법정계획의 제도적 차이 | 철도 리서치, 위례선, 환승저항 |
| [수도권 도시등급 평가 보고서](./수도권-도시등급-평가-보고서.md) | 수도권 66개 기초지자체 도시 기능 위계 평가 | `supplements/capital-area-city-tier/` |
| [1기 신도시 연구보고서](./1기-신도시-연구보고서.md) | 1기 신도시의 정책 배경, 공급 규모, 입주 시기, 교통축, 구조적 쟁점 | 1기 자료 정리 메모, 보류 서술 메모 |
| [국가별 개발밀도 규제 비교 보고서](./국가별-개발밀도-규제-비교-보고서.md) | 한국·일본·미국·중국 및 주요 고밀도 도시의 용적률·건폐율·고도제한 비교 | 신도시사, 도시계획 제도 비교 |
| [환승저항 보고서](./환승저항-보고서.md) | 대중교통 환승을 일반화비용 관점에서 정리 | 위례선, 철도망 계획 비교 |

## 원문 재구성 도서

각 `books/*` 폴더는 대체로 `sources/`, `docs/`, `dist/`의 세 층으로 구성된다. 원본 PDF는 `sources/`, 사람이 읽는 재구성 Markdown은 `docs/`, LLM 단일 번들은 `dist/`에 둔다.

| 컬렉션 | 경로 | 작업 진입점 | 주로 쓰는 맥락 |
|---|---|---|---|
| 한국형 신도시 가이드라인 연구 | `books/korean-newtown-guideline/` | [index](./books/korean-newtown-guideline/docs/korean-newtown-guideline/index.md), [stats](./books/korean-newtown-guideline/docs/korean-newtown-guideline/stats.md), [manifest](./books/korean-newtown-guideline/docs/korean-newtown-guideline/manifest.yml) | 신도시 계획 기준, 기반시설, BRT·트램, 스마트시티, 경관 |
| 도시·공간 트렌드 2024 | `books/city-space-trends-2024/` | [index](./books/city-space-trends-2024/docs/city-space-trends-2024/index.md), [stats](./books/city-space-trends-2024/docs/city-space-trends-2024/stats.md), [manifest](./books/city-space-trends-2024/docs/city-space-trends-2024/manifest.yml) | 서울메트로폴리탄, 수도권 공간구조, 삶터·일터·놀터·돌봄터·링크 |
| 1·2기 신도시 주민의 삶 | `books/newtown-resident-life-evaluation/` | [index](./books/newtown-resident-life-evaluation/docs/newtown-resident-life-evaluation/index.md), [stats](./books/newtown-resident-life-evaluation/docs/newtown-resident-life-evaluation/stats.md), [manifest](./books/newtown-resident-life-evaluation/docs/newtown-resident-life-evaluation/manifest.yml) | 주민만족, 통근·생활권, 동탄·운정, 거주 경험 |
| 1·2기 신도시 건설의 영향 | `books/newtown-construction-impact-evaluation/` | [index](./books/newtown-construction-impact-evaluation/docs/newtown-construction-impact-evaluation/index.md), [stats](./books/newtown-construction-impact-evaluation/docs/newtown-construction-impact-evaluation/stats.md), [manifest](./books/newtown-construction-impact-evaluation/docs/newtown-construction-impact-evaluation/manifest.yml) | 1·2기 신도시 효과, 주택시장, 공간구조, 생활 SOC |
| 3기 신도시 개발전략 및 계획기준 | `books/third-newtown-development-strategy/` | [index](./books/third-newtown-development-strategy/docs/third-newtown-development-strategy/index.md), [stats](./books/third-newtown-development-strategy/docs/third-newtown-development-strategy/stats.md), [manifest](./books/third-newtown-development-strategy/docs/third-newtown-development-strategy/manifest.yml) | 3기 신도시, 교산·창릉·왕숙·계양·대장, 자족·광역교통 |
| 성남시사 50년사 | `books/seongnam-city-history-50/` | [index](./books/seongnam-city-history-50/docs/seongnam-city-history-50/index.md), [stats](./books/seongnam-city-history-50/docs/seongnam-city-history-50/stats.md), [toponyms](./books/seongnam-city-history-50/docs/seongnam-city-history-50/toponyms.md), [transport-markets](./books/seongnam-city-history-50/docs/seongnam-city-history-50/transport-markets.md) | 광주대단지, 성남·분당·판교·위례 지역사, 동남권 연담화 |
| 평촌신도시 개발사 | `books/pyeongchon-newtown-development-history/` | [index](./books/pyeongchon-newtown-development-history/docs/pyeongchon-newtown-development-history/index.md), [stats](./books/pyeongchon-newtown-development-history/docs/pyeongchon-newtown-development-history/stats.md), [manifest](./books/pyeongchon-newtown-development-history/docs/pyeongchon-newtown-development-history/manifest.yml) | 평촌 사업시행, 보상, 교통영향평가, 기반시설 |
| 분당신도시 개발사 | `books/bundang-newtown-development-history/` | [index](./books/bundang-newtown-development-history/docs/bundang-newtown-development-history/index.md), [stats](./books/bundang-newtown-development-history/docs/bundang-newtown-development-history/stats.md), [manifest](./books/bundang-newtown-development-history/docs/bundang-newtown-development-history/manifest.yml) | 분당 사업시행, 기반시설, 1기 신도시 계획사 |
| 판교신도시 마스터 플랜 및 디자인 총람 | `books/pangyo-newtown-master-plan-design-book/` | [index](./books/pangyo-newtown-master-plan-design-book/docs/pangyo-newtown-master-plan-design-book/index.md), [stats](./books/pangyo-newtown-master-plan-design-book/docs/pangyo-newtown-master-plan-design-book/stats.md), [manifest](./books/pangyo-newtown-master-plan-design-book/docs/pangyo-newtown-master-plan-design-book/manifest.yml) | 판교 개발, 동판교 마스터 플랜, 주거단지·건축계획 |

## 보조 자료

| 폴더 | 역할 | 진입점 |
|---|---|---|
| `supplements/capital-area-city-tier/` | 수도권 66개 기초지자체 도시등급 평가의 방법론, 지표, source anchor, run 결과 | [AGENTS](./supplements/capital-area-city-tier/AGENTS.md), [README](./supplements/capital-area-city-tier/README.md) |
| `supplements/rail-research/` | 국가철도망·도시철도망 공식 링크, PIMAC 철도 예타 조사 메모 | [README](./supplements/rail-research/README.md), [notes AGENTS](./supplements/rail-research/notes/AGENTS.md) |
| `supplements/seoul-1963-expansion/` | 1963년 서울 대확장 연구의 원본 작업 자료와 이미지 | [AGENTS](./supplements/seoul-1963-expansion/AGENTS.md), [README](./supplements/seoul-1963-expansion/README.md) |
| `supplements/1st-newtown/` | 1기 신도시 이미지 보조 자료 | `supplements/1st-newtown/images/` |
| `supplements/new-town-generations/` | 신도시 세대 비교 시각자료 | `supplements/new-town-generations/images/` |
| `supplements/seoul-southeast-conurbation/` | 서울 동남부 연담화 지도와 사례 이미지 | `supplements/seoul-southeast-conurbation/images/` |

## 주제별 앵커

| 주제 | 우선 문서 | 보조 근거 |
|---|---|---|
| 신도시 세대 비교 | [1기·2기·3기 신도시의 근본적 차이](./1기-2기-3기-신도시의-근본적-차이.md) | 1기 신도시 보고서, 3기 신도시 개발전략, 한국형 신도시 가이드라인 |
| 한국 신도시사 총괄 | [대한민국 신도시의 역사](./대한민국-신도시의-역사.md) | 성남시사 50년사, 분당·평촌 개발사, 판교 총람 |
| 1기 신도시 | [1기 신도시 연구보고서](./1기-신도시-연구보고서.md) | [자료 정리 메모](./1기-신도시-자료-정리-메모.md), [보류 서술 메모](./1기-신도시-보류-서술-메모.md), 분당·평촌 개발사 |
| 서울 동남부·성남·위례 | [서울 동남부 도시 연담화 세부사례 근거정리](./서울-동남부-도시-연담화-세부사례-근거정리.md) | 서울 1963 확장, 위례선, 성남시사 50년사 |
| 철도망 계획 | [국가철도망 구축계획과 도시철도망 구축계획 비교](./국가철도망-구축계획과-도시철도망-구축계획-비교.md) | 철도 리서치 notes, 위례선, 환승저항 |
| 환승과 트램 | [환승저항 보고서](./환승저항-보고서.md) | 위례선 트램 보고서, 철도망 계획 비교 |
| 도시 기능 위계 | [수도권 도시등급 평가 보고서](./수도권-도시등급-평가-보고서.md) | capital-area-city-tier 방법론·지표·데이터 |
| 개발밀도 규제 | [국가별 개발밀도 규제 비교 보고서](./국가별-개발밀도-규제-비교-보고서.md) | 신도시사, 한국형 신도시 가이드라인 |

## 갱신 규칙

- 새 루트 보고서가 생기면 "공개 보고서"와 "주제별 앵커"를 갱신한다.
- 새 `books/*` 컬렉션이 생기면 "원문 재구성 도서"에 진입점과 용도를 추가한다.
- 새 `supplements/*` 주제가 생기면 "보조 자료"에 추가한다.
- 중요 작업 뒤에는 `log.md`에 `## [YYYY-MM-DD] type | 제목` 형식으로 append한다.
