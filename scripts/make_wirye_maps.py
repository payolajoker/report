#!/usr/bin/env python3
"""
위례선 트램 보고서용 지도 5종 생성
1. wirye-context-map.png        - 위례신도시 광역 위치 (§3)
2. wirye-full-route-map.png     - 12개 정류장 전체 노선 (§4)
3. wirye-macheon-area.png       - 마천역 일대 근접 (§5-4)
4. wirye-bokjeong-area.png      - 복정역 일대 근접 (§5-2)
5. wirye-namwirye-area.png      - 남위례역 일대 근접 (§5-3)
"""

from staticmap import StaticMap, Line, CircleMarker
from PIL import Image, ImageDraw, ImageFont

IMGDIR = "supplements/rail-research/images"
TILE   = "https://tile.openstreetmap.org/{z}/{x}/{y}.png"

def p(lat, lon):
    return (lon, lat)

def load_font(size):
    try:
        return ImageFont.truetype("/System/Library/Fonts/AppleSDGothicNeo.ttc", size)
    except Exception:
        return ImageFont.load_default()

def add_credit(img):
    draw = ImageDraw.Draw(img)
    draw.text((10, img.height - 20),
              "© OpenStreetMap contributors (ODbL)",
              fill="#444444", font=load_font(13))
    return img

# ── 위례선 정류장 좌표 ────────────────────────────────────────────
STOPS = [
    # (lat,   lon,     이름,          환승)
    (37.4915, 127.1435, "마천",        "5호선"),
    (37.4875, 127.1465, "북위례",      ""),
    (37.4840, 127.1490, "위례솔",      ""),
    (37.4805, 127.1510, "덕수고등학교",""),
    (37.4775, 127.1510, "위례호수공원",""),
    (37.4745, 127.1498, "위례별",      ""),
    (37.4718, 127.1470, "위례중앙광장","(장래 위례신사선)"),
    (37.4690, 127.1405, "위례역사공원","분기점"),
    # 지선
    (37.4655, 127.1368, "위례트램스퀘어",""),
    (37.4615, 127.1318, "남위례",      "8호선"),
    # 본선
    (37.4672, 127.1300, "위례스마트시티",""),
    (37.4725, 127.1238, "복정",        "8호선·수인분당선"),
]

MAIN_LINE = [p(lat,lon) for lat,lon,*_ in STOPS[:8]] + [p(STOPS[10][0], STOPS[10][1]), p(STOPS[11][0], STOPS[11][1])]
BRANCH_LINE = [p(STOPS[7][0], STOPS[7][1])] + [p(lat,lon) for lat,lon,*_ in STOPS[8:10]]

MAIN_COLOR   = "#1565C0"   # 파랑  (본선)
BRANCH_COLOR = "#7B1FA2"   # 보라  (지선)
XFER_COLOR   = "#D32F2F"   # 빨강  (환승역)
STOP_COLOR   = "#FFFFFF"   # 흰색  (일반역)


# ══════════════════════════════════════════════════════════
# 1. 광역 위치 지도 (§3): 위례신도시가 서울·성남·하남 어디에 있나
# ══════════════════════════════════════════════════════════
print("1. 광역 위치 지도 생성 중…")
m = StaticMap(1200, 900, url_template=TILE)

# 위례신도시 영역 박스를 라인으로 표시
WIRYE_BOX = [
    p(37.495, 127.118), p(37.495, 127.155),
    p(37.457, 127.155), p(37.457, 127.118),
    p(37.495, 127.118),
]
m.add_line(Line(WIRYE_BOX, "#E65100", 3))

# 위례선 전체 노선 (얇게)
m.add_line(Line(MAIN_LINE,   MAIN_COLOR,   3))
m.add_line(Line(BRANCH_LINE, BRANCH_COLOR, 3))

# 주변 주요역 마커
for lat, lon in [(37.4915, 127.1435), (37.4725, 127.1238), (37.4615, 127.1318)]:
    m.add_marker(CircleMarker(p(lat, lon), "white", 14))
    m.add_marker(CircleMarker(p(lat, lon), XFER_COLOR, 9))

img = m.render(zoom=13, center=[127.135, 37.490])

draw = ImageDraw.Draw(img)
f16 = load_font(16)
f14 = load_font(14)

# 범례
bx, by = 18, 18
draw.rectangle([bx,by,bx+320,by+110], fill=(255,255,255,220), outline="#AAAAAA")
draw.rectangle([bx+10,by+12,bx+34,by+24], fill="#E65100")
draw.text((bx+42, by+8),  "위례신도시 범위",    fill="#111", font=f16)
draw.rectangle([bx+10,by+40,bx+34,by+50], fill=MAIN_COLOR)
draw.text((bx+42, by+36), "위례선 본선",        fill="#111", font=f16)
draw.rectangle([bx+10,by+68,bx+34,by+78], fill=BRANCH_COLOR)
draw.text((bx+42, by+64), "위례선 지선",        fill="#111", font=f16)

# 행정구역 레이블
for (lat,lon,label) in [
    (37.510, 127.090, "서울 송파구"),
    (37.455, 127.120, "경기 성남시"),
    (37.460, 127.165, "경기 하남시"),
]:
    draw.text(p(0,0), "", fill="white", font=f14)   # dummy

add_credit(img)
img.save(f"{IMGDIR}/wirye-context-map.png")
print(f"   저장: wirye-context-map.png ({img.width}×{img.height})")


# ══════════════════════════════════════════════════════════
# 2. 전체 노선도 (§4): 12개 정류장 모두 표시
# ══════════════════════════════════════════════════════════
print("2. 전체 노선 지도 생성 중…")
m = StaticMap(1200, 1000, url_template=TILE)
m.add_line(Line(MAIN_LINE,   MAIN_COLOR,   5))
m.add_line(Line(BRANCH_LINE, BRANCH_COLOR, 5))

for lat, lon, name, xfer in STOPS:
    is_xfer = bool(xfer and xfer not in ("분기점",))
    color = XFER_COLOR if is_xfer else "#1565C0"
    m.add_marker(CircleMarker(p(lat, lon), "white", 16))
    m.add_marker(CircleMarker(p(lat, lon), color, 11))

img = m.render(zoom=15, center=[127.138, 37.477])
draw = ImageDraw.Draw(img)
f15 = load_font(15)
f13 = load_font(13)

# 범례
bx, by = 18, 18
draw.rectangle([bx,by,bx+320,by+145], fill=(255,255,255,220), outline="#AAAAAA")
draw.rectangle([bx+10,by+12,bx+34,by+24], fill=MAIN_COLOR)
draw.text((bx+42, by+8),  "위례선 본선 (마천→복정)",     fill="#111", font=f15)
draw.rectangle([bx+10,by+42,bx+34,by+54], fill=BRANCH_COLOR)
draw.text((bx+42, by+38), "위례선 지선 (역사공원→남위례)",fill="#111", font=f15)
draw.ellipse([bx+14,by+72,bx+30,by+86],  fill="white", outline=XFER_COLOR, width=2)
draw.ellipse([bx+17,by+75,bx+27,by+83],  fill=XFER_COLOR)
draw.text((bx+42, by+69), "환승역 (5·8호선·수인분당선)", fill="#111", font=f15)
draw.ellipse([bx+14,by+100,bx+30,by+114],fill="white", outline=MAIN_COLOR, width=2)
draw.ellipse([bx+17,by+103,bx+27,by+111],fill=MAIN_COLOR)
draw.text((bx+42, by+97), "일반 정류장",                 fill="#111", font=f15)

add_credit(img)
img.save(f"{IMGDIR}/wirye-full-route-map.png")
print(f"   저장: wirye-full-route-map.png ({img.width}×{img.height})")


# ══════════════════════════════════════════════════════════
# 3. 마천역 일대 근접 (§5-4)
# ══════════════════════════════════════════════════════════
print("3. 마천역 근접 지도 생성 중…")
m = StaticMap(1000, 800, url_template=TILE)

# 마천역에서 북위례까지 구간만 표시
m.add_line(Line([p(37.4915,127.1435), p(37.4875,127.1465)], MAIN_COLOR, 6))

# 마천역 마커 (크게)
m.add_marker(CircleMarker(p(37.4915, 127.1435), "white", 22))
m.add_marker(CircleMarker(p(37.4915, 127.1435), XFER_COLOR, 15))

# 북위례 마커 (작게)
m.add_marker(CircleMarker(p(37.4875, 127.1465), "white", 14))
m.add_marker(CircleMarker(p(37.4875, 127.1465), MAIN_COLOR, 9))

img = m.render(zoom=17, center=[127.143, 37.491])
draw = ImageDraw.Draw(img)
f17 = load_font(17)

# 레이블 박스
bx, by = 18, 18
draw.rectangle([bx,by,bx+330,by+80], fill=(255,255,255,220), outline="#AAAAAA")
draw.text((bx+12, by+10), "마천역 일대",            fill="#111", font=f17)
draw.text((bx+12, by+38), "● 마천역 (5호선 환승)",  fill=XFER_COLOR, font=load_font(15))
draw.text((bx+12, by+60), "● 위례선 남행 방향 →",   fill=MAIN_COLOR, font=load_font(15))

add_credit(img)
img.save(f"{IMGDIR}/wirye-macheon-area.png")
print(f"   저장: wirye-macheon-area.png ({img.width}×{img.height})")


# ══════════════════════════════════════════════════════════
# 4. 복정역 일대 근접 (§5-2)
# ══════════════════════════════════════════════════════════
print("4. 복정역 근접 지도 생성 중…")
m = StaticMap(1000, 800, url_template=TILE)

# 위례스마트시티→복정 구간
m.add_line(Line([p(37.4672,127.1300), p(37.4725,127.1238)], MAIN_COLOR, 6))

m.add_marker(CircleMarker(p(37.4725, 127.1238), "white", 22))
m.add_marker(CircleMarker(p(37.4725, 127.1238), XFER_COLOR, 15))
m.add_marker(CircleMarker(p(37.4672, 127.1300), "white", 14))
m.add_marker(CircleMarker(p(37.4672, 127.1300), MAIN_COLOR, 9))

img = m.render(zoom=17, center=[127.127, 37.473])
draw = ImageDraw.Draw(img)

bx, by = 18, 18
draw.rectangle([bx,by,bx+370,by+80], fill=(255,255,255,220), outline="#AAAAAA")
draw.text((bx+12, by+10), "복정역 일대",                         fill="#111",    font=load_font(17))
draw.text((bx+12, by+38), "● 복정역 (8호선·수인분당선 환승)",    fill=XFER_COLOR,font=load_font(15))
draw.text((bx+12, by+60), "← 위례스마트시티 방향",               fill=MAIN_COLOR,font=load_font(15))

add_credit(img)
img.save(f"{IMGDIR}/wirye-bokjeong-area.png")
print(f"   저장: wirye-bokjeong-area.png ({img.width}×{img.height})")


# ══════════════════════════════════════════════════════════
# 5. 남위례역 일대 근접 (§5-3)
# ══════════════════════════════════════════════════════════
print("5. 남위례역 근접 지도 생성 중…")
m = StaticMap(1000, 800, url_template=TILE)

# 위례트램스퀘어→남위례 지선
m.add_line(Line([p(37.4690,127.1405), p(37.4655,127.1368), p(37.4615,127.1318)], BRANCH_COLOR, 6))

m.add_marker(CircleMarker(p(37.4615, 127.1318), "white", 22))
m.add_marker(CircleMarker(p(37.4615, 127.1318), XFER_COLOR, 15))
m.add_marker(CircleMarker(p(37.4655, 127.1368), "white", 14))
m.add_marker(CircleMarker(p(37.4655, 127.1368), BRANCH_COLOR, 9))
m.add_marker(CircleMarker(p(37.4690, 127.1405), "white", 14))
m.add_marker(CircleMarker(p(37.4690, 127.1405), "#888888", 9))

img = m.render(zoom=17, center=[127.133, 37.463])
draw = ImageDraw.Draw(img)

bx, by = 18, 18
draw.rectangle([bx,by,bx+370,by+98], fill=(255,255,255,220), outline="#AAAAAA")
draw.text((bx+12, by+10), "남위례역 일대",              fill="#111",       font=load_font(17))
draw.text((bx+12, by+38), "● 남위례역 (8호선 환승)",    fill=XFER_COLOR,   font=load_font(15))
draw.text((bx+12, by+60), "● 위례트램스퀘어",           fill=BRANCH_COLOR, font=load_font(15))
draw.text((bx+12, by+80), "↑ 위례역사공원(분기) 방향",  fill="#555555",    font=load_font(14))

add_credit(img)
img.save(f"{IMGDIR}/wirye-namwirye-area.png")
print(f"   저장: wirye-namwirye-area.png ({img.width}×{img.height})")

print("\n완료.")
