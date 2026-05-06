# Vol 50 Integration Note: 제50권 길라잡이 성남 사전(事典)

## Processing Summary

- Source PDF: `books/seongnam-city-history-50/sources/seongnam-history-50-vol-50.pdf`
- Official source URL: https://www.seongnam.go.kr/city/1001112/30566/bbsView.do?idx=378640
- Page count: 264
- OCR used: false
- Embedded text extraction: `pdftotext -layout`
- Rendered images: 264 local JPG pages, `docs/seongnam-city-history-50/assets/pages/vol-50/vol-50-page-001.jpg` through `vol-50-page-264.jpg`
- Markdown draft: `docs/seongnam-city-history-50/vol-50-guidebook-seongnam-dictionary.md`
- LLM bundle: `dist/seongnam-history-50-vol-50.llm.md`
- Deferred ranges: none
- Shared files edited: none

## Content Character

50권은 성남의 자연지리, 인문환경, 역사와 문화유산, 인물, 정치·행정·경제·사회, 종교와 문화예술, 교육·체육·민속을 백과사전 형식으로 정리한 사전 권차다. 앞선 본문 권차를 장문 서술 원천으로 삼는다면, 50권은 명칭 통제, alias 정리, 짧은 정의, RAG 검색 진입점으로 쓰기 좋다.

## Key Counts

| 항목 | 값 | 병합 활용 |
| --- | ---: | --- |
| 원문 쪽수 | 264 | 전체 처리 완료 |
| 렌더링 이미지 | 264 | 전체 페이지 감사 가능 |
| `[정의]` 표지 | 1555 | 항목 단위 chunking 기준 |
| `[내용]` 표지 | 1542 | 항목 설명 본문 추출 기준 |
| `[지정 현황]` 표지 | 90 | 문화유산 지정 정보 구조화 후보 |
| 대분류 | 7 | Part 1-7 |
| 세부 절 | 20 | 목차 기준 |

## Sections To Merge Into Common Indexes

| 범위 | 제목 | 병합 후보 |
| --- | --- | --- |
| 1-3 | 앞부분 | 표지, 권별 목차 |
| 4-5 | Part 1 / 제1절 | 자연지리: 산(山) |
| 6-7 | Part 1 / 제2절 | 자연지리: 고개와 들판 |
| 8-12 | Part 1 / 제3절 | 자연지리: 하천, 저수지, 습지 |
| 13-21 | Part 1 / 제4절 | 자연지리: 공원과 위락 시설 |
| 22-24 | Part 1 / 제5절 | 자연지리: 보호수 |
| 25-56 | Part 2 / 제1절 | 인문환경: 행정구역과 역사 지명 |
| 57-78 | Part 2 / 제2절 | 인문환경: 도로와 교통 |
| 79-86 | Part 3 / 제1절 | 역사와 문화유산: 역사적 사건과 단체 |
| 87-107 | Part 3 / 제2절 | 역사와 문화유산: 문화유산 |
| 108-148 | Part 4 / 제1절 | 인물: 전통시대 인물 |
| 149-159 | Part 4 / 제2절 | 인물: 근현대인물 |
| 160-170 | Part 5 / 제1절 | 정치·행정·경제·사회: 공공기관과 시설 |
| 171-178 | Part 5 / 제2절 | 정치·행정·경제·사회: 경제와 산업 |
| 179-187 | Part 5 / 제3절 | 정치·행정·경제·사회: 시민사회 기관과 단체 |
| 188-196 | Part 5 / 제4절 | 정치·행정·경제·사회: 보건 의료 및 복지시설과 단체 |
| 197-205 | Part 6 / 제1절 | 종교와 문화예술: 종교 기관과 시설 |
| 206-224 | Part 6 / 제2절 | 종교와 문화예술: 문학, 문화예술, 축제 |
| 225-254 | Part 7 / 제1절 | 교육·체육·민속: 교육기관과 시설 및 단체 |
| 255-259 | Part 7 / 제2절 | 교육·체육·민속: 체육 시설과 단체 |
| 260-263 | Part 7 / 제3절 | 교육·체육·민속: 생활과 민속 |
| 264 | 판권 | 발행일, 발행처, 집필, 디자인·인쇄 정보 |

## Stats / Entities To Merge

- 전체: 264쪽 — 성남시 정치·경제·사회·문화·지리·역사 전 영역을 백과사전식 항목으로 압축한 길라잡이 권차.
- 전체: 1555개 [정의] 표지 — 항목 단위 RAG chunking과 사전형 질의응답의 기준점으로 쓸 수 있다.
- 전체: 1542개 [내용] 표지 — 정의 뒤의 설명 본문이 대부분 보존되어 항목별 요약·관계 추출에 적합하다.
- 전체: 90개 [지정 현황] 표지 — 문화유산·무형유산·향토유산의 지정일·보유자·소재지 색인 후보.
- p.4-6: 검단산 534.7m, 국사봉 약 540m, 남한산 522.1m, 청계산 약 618m, 청량산 약 497m — 성남 산지·남한산성·청계산권 지형 노드의 기본 수치.
- p.8-12: 탄천 성남시 구간 31.4km, 운중천 제방 15.96km·유역 24.91㎢, 창곡천 3.37km·유역 5.05㎢ — 하천·습지·신도시 개발 전후 수계 설명과 연결.
- p.13-21: 단대공원 21만 700㎡, 단대공원 산책로 10개 노선 3,273m, 수진습지생태원 1만 6,000㎡ — 공원·생태복원·도시 휴식 공간 색인 후보.
- p.25-56: 법정동·행정동·역사 지명 항목군 — 성남 3구 44법정동/50행정동 계보와 마을명·자연마을 유래 추적에 유용.
- p.57-78: 도로·교통 항목군 — 산성대로, 성남대로, 분당수서로, 신분당선·분당선 등 교통망 지식그래프 후보.
- p.79-86: 3·1운동, 광주대단지 사건, 6월민주항쟁 등 사건 항목 — 도시 형성 갈등·독립운동·민주화운동과 다른 역사 권차의 교차 색인.
- p.87-107: 문화유산 항목군, 지정 현황 다수 — 국가·경기도·성남시 문화유산과 비지정 유산의 명칭 통제 사전으로 활용 가능.
- p.108-159: 전통시대·근현대 인물 항목군 — Vol10 인물 50선과 결합해 인물명·본관·생몰년·활동 영역을 정규화할 수 있다.
- p.171-178: AK플라자, 게임인재단, 판교테크노밸리·성남하이테크밸리 관련 항목군 — 경제·산업 권차의 기업·상권·테크노밸리 노드 보강.
- p.197-224: 종교기관, 문화예술단체, 축제 항목군 — 종교·문화예술·축제 권차의 기관명 색인과 약칭 정규화.
- p.225-263: 교육기관, 체육 시설과 단체, 생활·민속 항목군 — 학교·수련시설·체육단체·민속 신앙 항목의 사전형 요약.
- p.264: 2025-12-29 발행 — 성남시 시사편찬위원회 발행, 경동현·김정미 집필, 홍익문화사 디자인·인쇄.

## Figure Pages To Merge

- p.001: `title-page` — 표지와 권명, 발간등록번호, 시리즈명; image `assets/pages/vol-50/vol-50-page-001.jpg`
- p.002: `toc` — Part 1-4 권별 목차; image `assets/pages/vol-50/vol-50-page-002.jpg`
- p.003: `toc` — Part 5-7 권별 목차; image `assets/pages/vol-50/vol-50-page-003.jpg`
- p.004: `dictionary-section` — Part 1 자연지리와 산 항목 시작; image `assets/pages/vol-50/vol-50-page-004.jpg`
- p.008: `dictionary-section` — 하천·저수지·습지 항목 시작; image `assets/pages/vol-50/vol-50-page-008.jpg`
- p.013: `dictionary-section` — 공원과 위락 시설 항목 시작; image `assets/pages/vol-50/vol-50-page-013.jpg`
- p.025: `dictionary-section` — Part 2 인문환경과 행정구역·역사 지명 시작; image `assets/pages/vol-50/vol-50-page-025.jpg`
- p.057: `dictionary-section` — 도로와 교통 항목 시작; image `assets/pages/vol-50/vol-50-page-057.jpg`
- p.079: `dictionary-section` — Part 3 역사와 문화유산, 역사적 사건과 단체 시작; image `assets/pages/vol-50/vol-50-page-079.jpg`
- p.087: `dictionary-section` — 문화유산 항목 시작; image `assets/pages/vol-50/vol-50-page-087.jpg`
- p.108: `dictionary-section` — Part 4 인물, 전통시대 인물 시작; image `assets/pages/vol-50/vol-50-page-108.jpg`
- p.149: `dictionary-section` — 근현대인물 항목 시작; image `assets/pages/vol-50/vol-50-page-149.jpg`
- p.160: `dictionary-section` — Part 5 정치·행정·경제·사회, 공공기관과 시설 시작; image `assets/pages/vol-50/vol-50-page-160.jpg`
- p.171: `dictionary-section` — 경제와 산업 항목 시작; image `assets/pages/vol-50/vol-50-page-171.jpg`
- p.179: `dictionary-section` — 시민사회 기관과 단체 항목 시작; image `assets/pages/vol-50/vol-50-page-179.jpg`
- p.188: `dictionary-section` — 보건 의료 및 복지시설과 단체 항목 시작; image `assets/pages/vol-50/vol-50-page-188.jpg`
- p.197: `dictionary-section` — Part 6 종교와 문화예술, 종교 기관과 시설 시작; image `assets/pages/vol-50/vol-50-page-197.jpg`
- p.206: `dictionary-section` — 문학, 문화예술, 축제 항목 시작; image `assets/pages/vol-50/vol-50-page-206.jpg`
- p.225: `dictionary-section` — Part 7 교육·체육·민속, 교육기관과 시설 및 단체 시작; image `assets/pages/vol-50/vol-50-page-225.jpg`
- p.255: `dictionary-section` — 체육 시설과 단체 항목 시작; image `assets/pages/vol-50/vol-50-page-255.jpg`
- p.260: `dictionary-section` — 생활과 민속 항목 시작; image `assets/pages/vol-50/vol-50-page-260.jpg`
- p.264: `colophon` — 판권: 발행일·발행처·집필·디자인·인쇄; image `assets/pages/vol-50/vol-50-page-264.jpg`

## Keyword Page Map

| 키워드 | 출현 쪽 | 병합 메모 |
| --- | --- | --- |
| 광주대단지 | 9, 39, 40, 42, 44, 45, 51, 52, 53, 80, 81, 83, 160, 161, 163, 168, 174, 180, 186, 193 ... | 25쪽 출현 |
| 분당신도시 | 8, 10, 12, 13, 28, 32, 33, 34, 35, 37, 40, 41, 42, 47, 49, 52, 53, 55, 56, 58 ... | 54쪽 출현 |
| 판교신도시 | 13, 15, 17, 18, 20, 21, 24, 34, 36, 38, 39, 56, 61, 63, 67, 71, 72, 75, 76, 77 ... | 29쪽 출현 |
| 위례신도시 | 12, 19, 22, 44, 48, 52, 53, 57, 58, 63, 72, 73, 74, 75, 78, 86, 203, 204, 219 | 19쪽 출현 |
| 판교테크노밸리 | 12, 15, 38, 39, 42, 67, 173, 175, 177, 178, 179, 208 | 12쪽 출현 |
| 성남하이테크밸리 | 7, 9, 21, 34, 42, 52, 63, 66, 175 | 9쪽 출현 |
| 모란시장 | 9, 15, 40, 41, 63, 69, 83, 179, 209, 220, 261 | 11쪽 출현 |
| 모란민속5일장 | 172, 176, 209 | 3쪽 출현 |
| 성남시청 | 6, 8, 9, 13, 17, 47, 53, 57, 64, 72, 78, 80, 84, 107, 161, 162, 163, 164, 167, 168 ... | 46쪽 출현 |
| 성남시의료원 | 47, 53, 191, 195, 196, 218 | 6쪽 출현 |
| 남한산성 | 4, 5, 6, 7, 9, 12, 13, 14, 18, 20, 22, 23, 24, 27, 28, 30, 31, 35, 38, 40 ... | 79쪽 출현 |
| 천림산봉수 | 5, 6, 56, 57, 106 | 5쪽 출현 |
| 탄천 | 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 16, 20, 22, 27, 28, 32, 33, 35, 36, 37 ... | 69쪽 출현 |
| 성남FC | 255, 256, 259 | 3쪽 출현 |

## Validation Notes

- Check local links for `vol-50-guidebook-seongnam-dictionary.md` and `seongnam-history-50-vol-50.llm.md`.
- Verify source markers and page headers equal 264 in both files.
- Verify no unresolved work markers remain.
- Verify image count equals 264 and sample pages are nonblank.
