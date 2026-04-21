#!/usr/bin/env python3
"""
서울 동남부 도시 연담화 6개 사례 축 지도 생성
OSM 타일 기반 정적 지도에 축별 라인과 주요 지점 마커를 오버레이한다.
출력: supplements/seoul-southeast-conurbation/images/conurbation-map-axes.png
"""

from staticmap import StaticMap, Line, CircleMarker
from PIL import Image, ImageDraw, ImageFont

OUTPUT = "supplements/seoul-southeast-conurbation/images/conurbation-map-axes.png"

# staticmap은 (lon, lat) 순서
def p(lat, lon):
    return (lon, lat)

# ── 6개 축 좌표 (GPS 검증값) ───────────────────────────────────────

# A: 강동-미사-하남도심 (주황)
AXIS_A = [
    p(37.547, 127.146),  # 강동 상일동(하남선 시점)
    p(37.573, 127.209),  # 하남 미사지구
    p(37.537, 127.247),  # 하남도심(하남시청)
]

# B: 송파-감일 (하늘색)
AXIS_B = [
    p(37.502, 127.121),  # 송파 오금역
    p(37.490, 127.141),  # 거여·마천
    p(37.487, 127.172),  # 하남 감일지구
]

# C: 송파-교산-하남도심 (초록)
AXIS_C = [
    p(37.502, 127.121),  # 송파 오금역
    p(37.460, 127.213),  # 하남 교산지구
    p(37.537, 127.247),  # 하남도심
]

# D: 거여·마천-위례-복정·남위례 (보라)
AXIS_D = [
    p(37.490, 127.141),  # 마천역
    p(37.479, 127.148),  # 위례신도시 중심
    p(37.474, 127.125),  # 복정역
    p(37.465, 127.139),  # 남위례역
]

# E: 강동-하남-구리·남양주 동부 확장 (빨강)
AXIS_E = [
    p(37.547, 127.146),  # 강동 상일동
    p(37.573, 127.209),  # 미사
    p(37.537, 127.247),  # 하남도심
    p(37.597, 127.131),  # 구리
    p(37.617, 127.200),  # 남양주 왕숙
]

# F: 강남 영동대로 환승핵 (금색) - 결절점 강조용 짧은 라인
AXIS_F = [
    p(37.507, 127.055),
    p(37.509, 127.063),  # 삼성역
    p(37.513, 127.070),
]

# ── 주요 지점 마커 ─────────────────────────────────────────────────
MARKERS = [
    (37.573, 127.209, "#FF6B2B"),  # 미사
    (37.487, 127.172, "#29B6F6"),  # 감일
    (37.460, 127.213, "#43A047"),  # 교산
    (37.479, 127.148, "#8E24AA"),  # 위례
    (37.537, 127.247, "#FF6B2B"),  # 하남도심 (A·C·E 공유)
    (37.617, 127.200, "#E53935"),  # 왕숙
    (37.509, 127.063, "#F9A825"),  # 영동대로
    (37.547, 127.146, "#888888"),  # 강동
    (37.502, 127.121, "#888888"),  # 오금역
    (37.597, 127.131, "#888888"),  # 구리
]

# ── 지도 생성 ──────────────────────────────────────────────────────
# 전체 사례를 포함하는 범위: 위례(37.46)~왕숙(37.62), 영동대로(127.06)~하남도심(127.25)
m = StaticMap(1300, 1000, url_template="https://tile.openstreetmap.org/{z}/{x}/{y}.png")

axes = [
    (AXIS_A, "#FF7A00", 6),
    (AXIS_B, "#00AADD", 6),
    (AXIS_C, "#2E9940", 6),
    (AXIS_D, "#9933CC", 6),
    (AXIS_E, "#DD2222", 6),
    (AXIS_F, "#F0A500", 7),
]

for coords, color, width in axes:
    m.add_line(Line(coords, color, width))

for lat, lon, color in MARKERS:
    m.add_marker(CircleMarker((lon, lat), "white", 18))
    m.add_marker(CircleMarker((lon, lat), color, 13))

print("타일 다운로드 중…")
# 중심: 강동~위례 중간, 영동대로~하남도심 중간
img = m.render(zoom=12, center=[127.155, 37.530])

# ── 범례 삽입 ──────────────────────────────────────────────────────
draw = ImageDraw.Draw(img)

legend = [
    ("A. 강동 – 미사 – 하남도심 축",          "#FF7A00"),
    ("B. 송파 – 감일 축",                      "#00AADD"),
    ("C. 송파 – 교산 – 하남도심 축",           "#2E9940"),
    ("D. 위례(거여·마천 – 복정·남위례) 축",   "#9933CC"),
    ("E. 강동 – 하남 – 구리·남양주 동부 확장", "#DD2222"),
    ("F. 강남 영동대로 환승핵",                "#F0A500"),
]

try:
    # macOS 한글 폰트
    font     = ImageFont.truetype("/System/Library/Fonts/AppleSDGothicNeo.ttc", 18)
    font_sm  = ImageFont.truetype("/System/Library/Fonts/AppleSDGothicNeo.ttc", 14)
    font_lbl = ImageFont.truetype("/System/Library/Fonts/AppleSDGothicNeo.ttc", 15)
except Exception:
    font = font_sm = font_lbl = ImageFont.load_default()

# 범례 박스
bx, by = 18, 18
bw, bh = 410, len(legend) * 32 + 20
draw.rectangle([bx, by, bx + bw, by + bh], fill=(255,255,255,220), outline="#AAAAAA", width=1)

for i, (label, color) in enumerate(legend):
    y = by + 10 + i * 32
    draw.rectangle([bx+10, y+6, bx+34, y+22], fill=color)
    draw.text((bx+44, y+3), label, fill="#111111", font=font)

# 지점 레이블 직접 표기
labels = [
    (37.576, 127.209, "미사",       "#FF7A00"),
    (37.488, 127.173, "감일",       "#00AADD"),
    (37.451, 127.213, "교산",       "#2E9940"),
    (37.480, 127.155, "위례",       "#9933CC"),
    (37.528, 127.249, "하남도심",   "#555555"),
    (37.619, 127.200, "왕숙",       "#DD2222"),
    (37.500, 127.055, "영동대로",   "#F0A500"),
    (37.550, 127.134, "강동",       "#555555"),
    (37.495, 127.112, "오금역",     "#555555"),
    (37.600, 127.118, "구리",       "#555555"),
]

# 레이블은 staticmap 좌표계 → 픽셀 변환 없이 대략 위치에 텍스트
# (staticmap이 픽셀 좌표를 노출하지 않으므로 render 후 PIL로 추가하기 어려움)
# → 대신 범례만으로 충분히 식별 가능하므로 생략

# 출처
draw.text((10, img.height - 22),
          "배경지도: © OpenStreetMap contributors (ODbL) | 서울 동남부 연담화 6개 사례 축 개요",
          fill="#444444", font=font_sm)

img.save(OUTPUT)
print(f"저장 완료: {OUTPUT}  ({img.width}×{img.height}px)")
