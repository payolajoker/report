#!/usr/bin/env python3
"""
위례선 트램 보고서용 지도 5종 생성
좌표 근거:
  ■ OSM Overpass 확정: 마천역·덕수고·위례호수공원·위례중앙광장·위례역사공원·남위례역·복정역
  ■ 그림3 공식 노선도 비례 보간: 북위례·위례솔·위례별·위례트램스퀘어·위례스마트시티
"""

from staticmap import StaticMap, Line, CircleMarker
from PIL import Image, ImageDraw, ImageFont

IMGDIR = "supplements/rail-research/images"
TILE   = "https://tile.openstreetmap.org/{z}/{x}/{y}.png"

def p(lat, lon):   return (lon, lat)

def load_font(size):
    try:    return ImageFont.truetype("/System/Library/Fonts/AppleSDGothicNeo.ttc", size)
    except: return ImageFont.load_default()

def credit(img):
    ImageDraw.Draw(img).text((10, img.height - 20),
        "© OpenStreetMap contributors (ODbL)", fill="#444", font=load_font(13))
    return img

# ── 정류장 좌표 (OSM Overpass 확정 + 그림3 비례 보간) ─────────────
# (lat,          lon,       이름,           환승)
STOPS = [
  (37.494953, 127.152724, "마천",          "5호선"),        # OSM 확정
  (37.491800, 127.150300, "북위례",        ""),             # 101→104 1/3 보간
  (37.488600, 127.148000, "위례솔",        ""),             # 101→104 2/3 보간
  (37.485322, 127.146259, "덕수고등학교",  ""),             # OSM 확정
  (37.480962, 127.143162, "위례호수공원",  ""),             # OSM 확정
  (37.477300, 127.144200, "위례별",        ""),             # 105→107 중간 보간
  (37.473586, 127.142168, "위례중앙광장",  "(장래 위례신사선)"), # OSM 확정
  # ── 분기점 ──
  (37.470567, 127.141962, "위례역사공원",  "분기"),         # OSM 확정  ← 본선+지선 공유
  # 지선 (보라): 역사공원 → 남위례
  (37.466400, 127.140200, "위례트램스퀘어",""),             # 108→110 보간
  (37.462772, 127.139216, "남위례",        "8호선"),        # OSM 확정
  # 본선 계속 (파랑): 역사공원 → 복정
  (37.470500, 127.134300, "위례스마트시티",""),             # 108→112 보간
  (37.470577, 127.126713, "복정",          "8호선·수인분당선"), # OSM 확정
]

# 본선: 101-108, 111-112
MAIN_LINE   = [p(lat,lon) for lat,lon,*_ in STOPS[:8]] \
            + [p(STOPS[10][0], STOPS[10][1]), p(STOPS[11][0], STOPS[11][1])]
# 지선: 108-110
BRANCH_LINE = [p(STOPS[7][0], STOPS[7][1])] \
            + [p(lat,lon) for lat,lon,*_ in STOPS[8:10]]

MAIN_C   = "#1565C0"   # 파랑
BRANCH_C = "#7B1FA2"   # 보라
XFER_C   = "#D32F2F"   # 빨강

# ═══════════════════════════════════════════════
# 1. 광역 위치 지도 (§3)
# ═══════════════════════════════════════════════
print("1/5 광역 위치 지도…")
m = StaticMap(1200, 900, url_template=TILE)
BOX = [p(37.498,127.118),p(37.498,127.161),
       p(37.458,127.161),p(37.458,127.118),p(37.498,127.118)]
m.add_line(Line(BOX,        "#E65100", 3))
m.add_line(Line(MAIN_LINE,  MAIN_C,   3))
m.add_line(Line(BRANCH_LINE,BRANCH_C, 3))
for lat,lon in [(37.494953,127.152724),(37.470577,127.126713),(37.462772,127.139216)]:
    m.add_marker(CircleMarker(p(lat,lon),"white",14))
    m.add_marker(CircleMarker(p(lat,lon),XFER_C, 9))

img = m.render(zoom=13, center=[127.140, 37.480])
draw = ImageDraw.Draw(img)
bx,by = 18,18
draw.rectangle([bx,by,bx+320,by+110], fill=(255,255,255,220), outline="#AAA")
draw.rectangle([bx+10,by+12,bx+34,by+24], fill="#E65100")
draw.text((bx+42,by+8),  "위례신도시 범위", fill="#111", font=load_font(16))
draw.rectangle([bx+10,by+40,bx+34,by+50], fill=MAIN_C)
draw.text((bx+42,by+36), "위례선 본선",     fill="#111", font=load_font(16))
draw.rectangle([bx+10,by+68,bx+34,by+78], fill=BRANCH_C)
draw.text((bx+42,by+64), "위례선 지선",     fill="#111", font=load_font(16))
credit(img).save(f"{IMGDIR}/wirye-context-map.png")
print("   저장 완료")

# ═══════════════════════════════════════════════
# 2. 전체 노선도 (§4)
# ═══════════════════════════════════════════════
print("2/5 전체 노선 지도…")
m = StaticMap(1200, 1000, url_template=TILE)
m.add_line(Line(MAIN_LINE,  MAIN_C,   5))
m.add_line(Line(BRANCH_LINE,BRANCH_C, 5))
for lat,lon,name,xfer in STOPS:
    is_xfer = bool(xfer and xfer not in ("분기",))
    c = XFER_C if is_xfer else MAIN_C
    m.add_marker(CircleMarker(p(lat,lon),"white",16))
    m.add_marker(CircleMarker(p(lat,lon),c,11))

img = m.render(zoom=14, center=[127.140, 37.479])
draw = ImageDraw.Draw(img)
bx,by = 18,18
draw.rectangle([bx,by,bx+350,by+150], fill=(255,255,255,220), outline="#AAA")
draw.rectangle([bx+10,by+12,bx+34,by+24], fill=MAIN_C)
draw.text((bx+42,by+8),  "위례선 본선 (마천→복정)",       fill="#111", font=load_font(15))
draw.rectangle([bx+10,by+42,bx+34,by+54], fill=BRANCH_C)
draw.text((bx+42,by+38), "위례선 지선 (역사공원→남위례)", fill="#111", font=load_font(15))
draw.ellipse([bx+14,by+73,bx+30,by+87],  fill="white",outline=XFER_C,width=2)
draw.ellipse([bx+17,by+76,bx+27,by+84],  fill=XFER_C)
draw.text((bx+42,by+70), "환승역",                        fill="#111", font=load_font(15))
draw.ellipse([bx+14,by+102,bx+30,by+116],fill="white",outline=MAIN_C,width=2)
draw.ellipse([bx+17,by+105,bx+27,by+113],fill=MAIN_C)
draw.text((bx+42,by+99), "일반 정류장",                   fill="#111", font=load_font(15))
credit(img).save(f"{IMGDIR}/wirye-full-route-map.png")
print("   저장 완료")

# ═══════════════════════════════════════════════
# 3. 마천역 근접 (§5-4)
# ═══════════════════════════════════════════════
print("3/5 마천역 근접…")
m = StaticMap(1000, 800, url_template=TILE)
m.add_line(Line([p(37.494953,127.152724), p(37.491800,127.150300)], MAIN_C, 6))
m.add_marker(CircleMarker(p(37.494953,127.152724),"white",22))
m.add_marker(CircleMarker(p(37.494953,127.152724),XFER_C,15))
m.add_marker(CircleMarker(p(37.491800,127.150300),"white",14))
m.add_marker(CircleMarker(p(37.491800,127.150300),MAIN_C,9))

img = m.render(zoom=16, center=[127.152, 37.493])
draw = ImageDraw.Draw(img)
bx,by = 18,18
draw.rectangle([bx,by,bx+320,by+80], fill=(255,255,255,220), outline="#AAA")
draw.text((bx+12,by+10), "마천역 일대",           fill="#111",  font=load_font(17))
draw.text((bx+12,by+38), "● 마천역 (5호선 환승)", fill=XFER_C,  font=load_font(15))
draw.text((bx+12,by+60), "● 위례선 남서행 →",     fill=MAIN_C,  font=load_font(15))
credit(img).save(f"{IMGDIR}/wirye-macheon-area.png")
print("   저장 완료")

# ═══════════════════════════════════════════════
# 4. 복정역 근접 (§5-2)
# ═══════════════════════════════════════════════
print("4/5 복정역 근접…")
m = StaticMap(1000, 800, url_template=TILE)
m.add_line(Line([p(37.470500,127.134300), p(37.470577,127.126713)], MAIN_C, 6))
m.add_marker(CircleMarker(p(37.470577,127.126713),"white",22))
m.add_marker(CircleMarker(p(37.470577,127.126713),XFER_C,15))
m.add_marker(CircleMarker(p(37.470500,127.134300),"white",14))
m.add_marker(CircleMarker(p(37.470500,127.134300),MAIN_C,9))

img = m.render(zoom=16, center=[127.130, 37.471])
draw = ImageDraw.Draw(img)
bx,by = 18,18
draw.rectangle([bx,by,bx+380,by+80], fill=(255,255,255,220), outline="#AAA")
draw.text((bx+12,by+10), "복정역 일대",                       fill="#111",  font=load_font(17))
draw.text((bx+12,by+38), "● 복정역 (8호선·수인분당선 환승)", fill=XFER_C,  font=load_font(15))
draw.text((bx+12,by+60), "← 위례스마트시티 방향",             fill=MAIN_C,  font=load_font(15))
credit(img).save(f"{IMGDIR}/wirye-bokjeong-area.png")
print("   저장 완료")

# ═══════════════════════════════════════════════
# 5. 남위례역 근접 (§5-3)
# ═══════════════════════════════════════════════
print("5/5 남위례역 근접…")
m = StaticMap(1000, 800, url_template=TILE)
m.add_line(Line([p(37.470567,127.141962),
                 p(37.466400,127.140200),
                 p(37.462772,127.139216)], BRANCH_C, 6))
m.add_marker(CircleMarker(p(37.462772,127.139216),"white",22))
m.add_marker(CircleMarker(p(37.462772,127.139216),XFER_C,15))
m.add_marker(CircleMarker(p(37.466400,127.140200),"white",14))
m.add_marker(CircleMarker(p(37.466400,127.140200),BRANCH_C,9))
m.add_marker(CircleMarker(p(37.470567,127.141962),"white",14))
m.add_marker(CircleMarker(p(37.470567,127.141962),"#888",9))

img = m.render(zoom=16, center=[127.140, 37.466])
draw = ImageDraw.Draw(img)
bx,by = 18,18
draw.rectangle([bx,by,bx+360,by+98], fill=(255,255,255,220), outline="#AAA")
draw.text((bx+12,by+10), "남위례역 일대",               fill="#111",    font=load_font(17))
draw.text((bx+12,by+38), "● 남위례역 (8호선 환승)",     fill=XFER_C,    font=load_font(15))
draw.text((bx+12,by+60), "● 위례트램스퀘어",            fill=BRANCH_C,  font=load_font(15))
draw.text((bx+12,by+80), "↑ 위례역사공원(분기점) 방향", fill="#555",    font=load_font(14))
credit(img).save(f"{IMGDIR}/wirye-namwirye-area.png")
print("   저장 완료")

print("\n완료.")
