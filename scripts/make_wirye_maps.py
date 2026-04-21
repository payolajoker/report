#!/usr/bin/env python3
"""
위례선 트램 보고서용 지도 5종 생성 (OSM Overpass/Nominatim 검증 좌표 사용)

확정 좌표 출처:
  마천역·복정역·남위례역 → Overpass API (railway=station)
  덕수고·위례호수공원·위례중앙광장·위례역사공원 → Overpass API (노드)
  중간 정류장 → 위례대로/위례북로 도로 중심축 기반 보간
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

# ── OSM 검증 정류장 좌표 ──────────────────────────────────────────
# (lat, lon, 이름, 환승)
STOPS = [
    (37.494953, 127.152724, "마천",         "5호선"),          # Overpass 확정
    (37.490100, 127.150600, "북위례",        ""),               # 위례북로 축 보간
    (37.487000, 127.148200, "위례솔",        ""),               # 위례북로 남단 보간
    (37.485322, 127.146259, "덕수고등학교",  ""),               # Overpass 확정
    (37.480962, 127.143162, "위례호수공원",  ""),               # Overpass 확정
    (37.479500, 127.148200, "위례별",        ""),               # 스타필드시티 인근 보간
    (37.473586, 127.142168, "위례중앙광장",  "(장래 위례신사선)"), # Overpass 확정
    (37.470567, 127.141962, "위례역사공원",  "분기점"),         # Overpass 확정
    # 지선 (보라)
    (37.466200, 127.139500, "위례트램스퀘어",""),               # 위례대로 축 보간
    (37.462772, 127.139216, "남위례",        "8호선"),          # Overpass 확정
    # 본선 계속 (파랑)
    (37.470300, 127.132800, "위례스마트시티",""),               # 역사공원→복정 보간
    (37.470577, 127.126713, "복정",          "8호선·수인분당선"), # Overpass 확정
]

# 본선: 마천→역사공원→위례스마트시티→복정
MAIN_LINE = [p(lat,lon) for lat,lon,*_ in STOPS[:8]] \
          + [p(STOPS[10][0], STOPS[10][1]), p(STOPS[11][0], STOPS[11][1])]

# 지선: 역사공원→위례트램스퀘어→남위례
BRANCH_LINE = [p(STOPS[7][0], STOPS[7][1])] \
            + [p(lat,lon) for lat,lon,*_ in STOPS[8:10]]

MAIN_COLOR   = "#1565C0"
BRANCH_COLOR = "#7B1FA2"
XFER_COLOR   = "#D32F2F"


# ══════════════════════════════════════════════════════════
# 1. 광역 위치 지도 (§3)
# ══════════════════════════════════════════════════════════
print("1. 광역 위치 지도…")
m = StaticMap(1200, 900, url_template=TILE)

# 위례신도시 외곽 박스
WIRYE_BOX = [
    p(37.497, 127.118), p(37.497, 127.160),
    p(37.458, 127.160), p(37.458, 127.118),
    p(37.497, 127.118),
]
m.add_line(Line(WIRYE_BOX, "#E65100", 3))
m.add_line(Line(MAIN_LINE,   MAIN_COLOR,   3))
m.add_line(Line(BRANCH_LINE, BRANCH_COLOR, 3))

for lat, lon in [(37.494953,127.152724),(37.470577,127.126713),(37.462772,127.139216)]:
    m.add_marker(CircleMarker(p(lat,lon), "white", 14))
    m.add_marker(CircleMarker(p(lat,lon), XFER_COLOR, 9))

img = m.render(zoom=13, center=[127.138, 37.480])
draw = ImageDraw.Draw(img)
f16 = load_font(16)

bx, by = 18, 18
draw.rectangle([bx,by,bx+320,by+110], fill=(255,255,255,220), outline="#AAAAAA")
draw.rectangle([bx+10,by+12,bx+34,by+24], fill="#E65100")
draw.text((bx+42, by+8),  "위례신도시 범위",    fill="#111", font=f16)
draw.rectangle([bx+10,by+40,bx+34,by+50], fill=MAIN_COLOR)
draw.text((bx+42, by+36), "위례선 본선",        fill="#111", font=f16)
draw.rectangle([bx+10,by+68,bx+34,by+78], fill=BRANCH_COLOR)
draw.text((bx+42, by+64), "위례선 지선",        fill="#111", font=f16)

add_credit(img)
img.save(f"{IMGDIR}/wirye-context-map.png")
print(f"   저장 완료 ({img.width}×{img.height})")


# ══════════════════════════════════════════════════════════
# 2. 전체 노선도 (§4)
# ══════════════════════════════════════════════════════════
print("2. 전체 노선 지도…")
m = StaticMap(1200, 1000, url_template=TILE)
m.add_line(Line(MAIN_LINE,   MAIN_COLOR,   5))
m.add_line(Line(BRANCH_LINE, BRANCH_COLOR, 5))

for lat, lon, name, xfer in STOPS:
    is_xfer = bool(xfer and xfer not in ("분기점",))
    color = XFER_COLOR if is_xfer else MAIN_COLOR
    m.add_marker(CircleMarker(p(lat,lon), "white", 16))
    m.add_marker(CircleMarker(p(lat,lon), color, 11))

img = m.render(zoom=14, center=[127.140, 37.479])
draw = ImageDraw.Draw(img)
f15 = load_font(15)

bx, by = 18, 18
draw.rectangle([bx,by,bx+340,by+148], fill=(255,255,255,220), outline="#AAAAAA")
draw.rectangle([bx+10,by+12,bx+34,by+24], fill=MAIN_COLOR)
draw.text((bx+42, by+8),  "위례선 본선 (마천→복정)",        fill="#111", font=f15)
draw.rectangle([bx+10,by+42,bx+34,by+54], fill=BRANCH_COLOR)
draw.text((bx+42, by+38), "위례선 지선 (역사공원→남위례)",   fill="#111", font=f15)
draw.ellipse([bx+14,by+73,bx+30,by+87],  fill="white", outline=XFER_COLOR, width=2)
draw.ellipse([bx+17,by+76,bx+27,by+84],  fill=XFER_COLOR)
draw.text((bx+42, by+70), "환승역 (5·8호선·수인분당선)",     fill="#111", font=f15)
draw.ellipse([bx+14,by+102,bx+30,by+116],fill="white", outline=MAIN_COLOR, width=2)
draw.ellipse([bx+17,by+105,bx+27,by+113],fill=MAIN_COLOR)
draw.text((bx+42, by+99), "일반 정류장",                     fill="#111", font=f15)

add_credit(img)
img.save(f"{IMGDIR}/wirye-full-route-map.png")
print(f"   저장 완료 ({img.width}×{img.height})")


# ══════════════════════════════════════════════════════════
# 3. 마천역 근접 (§5-4)
# ══════════════════════════════════════════════════════════
print("3. 마천역 근접 지도…")
m = StaticMap(1000, 800, url_template=TILE)
# 마천역→북위례 구간
m.add_line(Line([p(37.494953,127.152724), p(37.490100,127.150600)], MAIN_COLOR, 6))
m.add_marker(CircleMarker(p(37.494953,127.152724), "white", 22))
m.add_marker(CircleMarker(p(37.494953,127.152724), XFER_COLOR, 15))
m.add_marker(CircleMarker(p(37.490100,127.150600), "white", 14))
m.add_marker(CircleMarker(p(37.490100,127.150600), MAIN_COLOR, 9))

img = m.render(zoom=16, center=[127.151, 37.493])
draw = ImageDraw.Draw(img)
bx, by = 18, 18
draw.rectangle([bx,by,bx+320,by+80], fill=(255,255,255,220), outline="#AAAAAA")
draw.text((bx+12, by+10), "마천역 일대",            fill="#111",    font=load_font(17))
draw.text((bx+12, by+38), "● 마천역 (5호선 환승)",  fill=XFER_COLOR,font=load_font(15))
draw.text((bx+12, by+60), "● 위례선 남서행 →",      fill=MAIN_COLOR,font=load_font(15))
add_credit(img)
img.save(f"{IMGDIR}/wirye-macheon-area.png")
print(f"   저장 완료 ({img.width}×{img.height})")


# ══════════════════════════════════════════════════════════
# 4. 복정역 근접 (§5-2)
# ══════════════════════════════════════════════════════════
print("4. 복정역 근접 지도…")
m = StaticMap(1000, 800, url_template=TILE)
# 위례스마트시티→복정 구간
m.add_line(Line([p(37.470300,127.132800), p(37.470577,127.126713)], MAIN_COLOR, 6))
m.add_marker(CircleMarker(p(37.470577,127.126713), "white", 22))
m.add_marker(CircleMarker(p(37.470577,127.126713), XFER_COLOR, 15))
m.add_marker(CircleMarker(p(37.470300,127.132800), "white", 14))
m.add_marker(CircleMarker(p(37.470300,127.132800), MAIN_COLOR, 9))

img = m.render(zoom=16, center=[127.129, 37.471])
draw = ImageDraw.Draw(img)
bx, by = 18, 18
draw.rectangle([bx,by,bx+370,by+80], fill=(255,255,255,220), outline="#AAAAAA")
draw.text((bx+12, by+10), "복정역 일대",                      fill="#111",    font=load_font(17))
draw.text((bx+12, by+38), "● 복정역 (8호선·수인분당선 환승)", fill=XFER_COLOR,font=load_font(15))
draw.text((bx+12, by+60), "← 위례스마트시티 방향",            fill=MAIN_COLOR,font=load_font(15))
add_credit(img)
img.save(f"{IMGDIR}/wirye-bokjeong-area.png")
print(f"   저장 완료 ({img.width}×{img.height})")


# ══════════════════════════════════════════════════════════
# 5. 남위례역 근접 (§5-3)
# ══════════════════════════════════════════════════════════
print("5. 남위례역 근접 지도…")
m = StaticMap(1000, 800, url_template=TILE)
# 위례역사공원→위례트램스퀘어→남위례
m.add_line(Line([p(37.470567,127.141962),
                 p(37.466200,127.139500),
                 p(37.462772,127.139216)], BRANCH_COLOR, 6))
m.add_marker(CircleMarker(p(37.462772,127.139216), "white", 22))
m.add_marker(CircleMarker(p(37.462772,127.139216), XFER_COLOR, 15))
m.add_marker(CircleMarker(p(37.466200,127.139500), "white", 14))
m.add_marker(CircleMarker(p(37.466200,127.139500), BRANCH_COLOR, 9))
m.add_marker(CircleMarker(p(37.470567,127.141962), "white", 14))
m.add_marker(CircleMarker(p(37.470567,127.141962), "#888888", 9))

img = m.render(zoom=16, center=[127.140, 37.466])
draw = ImageDraw.Draw(img)
bx, by = 18, 18
draw.rectangle([bx,by,bx+360,by+98], fill=(255,255,255,220), outline="#AAAAAA")
draw.text((bx+12, by+10), "남위례역 일대",              fill="#111",       font=load_font(17))
draw.text((bx+12, by+38), "● 남위례역 (8호선 환승)",    fill=XFER_COLOR,   font=load_font(15))
draw.text((bx+12, by+60), "● 위례트램스퀘어",           fill=BRANCH_COLOR, font=load_font(15))
draw.text((bx+12, by+80), "↑ 위례역사공원(분기점) 방향",fill="#555555",    font=load_font(14))
add_credit(img)
img.save(f"{IMGDIR}/wirye-namwirye-area.png")
print(f"   저장 완료 ({img.width}×{img.height})")

print("\n전체 완료.")
