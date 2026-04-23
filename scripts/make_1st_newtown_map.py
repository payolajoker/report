#!/usr/bin/env python3
"""
1기 신도시 5곳 위치 지도 생성

- staticmap + Pillow 기반
- 출력: supplements/1st-newtown/images/1st-newtown-location-map.png
"""

from math import cos, log, pi, radians, tan
from pathlib import Path

from PIL import ImageDraw, ImageFont
from staticmap import CircleMarker, StaticMap

WIDTH = 1200
HEIGHT = 900
ZOOM = 10
TILE = "https://tile.openstreetmap.org/{z}/{x}/{y}.png"
OUTPUT = Path("supplements/1st-newtown/images/1st-newtown-location-map.png")
CENTER = (37.483, 126.906)

# CODEX_TASKS.md Task 4에 제시된 'OSM 기준 도심부' 좌표를 사용한 참고점.
# 법정 경계나 행정중심점이 아니라, 단순 위치 참고도용 마커 좌표다.
POINTS = [
    {"name": "분당", "lat": 37.3595, "lon": 127.1052, "color": "#D32F2F", "dx": 14, "dy": -18},
    {"name": "일산", "lat": 37.6560, "lon": 126.7770, "color": "#1976D2", "dx": 14, "dy": -18},
    {"name": "평촌", "lat": 37.3896, "lon": 126.9526, "color": "#388E3C", "dx": 14, "dy": -18},
    {"name": "산본", "lat": 37.3600, "lon": 126.9320, "color": "#F57C00", "dx": 14, "dy": 10},
    {"name": "중동", "lat": 37.5025, "lon": 126.7652, "color": "#7B1FA2", "dx": 14, "dy": -18},
]


def p(lat: float, lon: float):
    return (lon, lat)


def load_font(size: int):
    try:
        return ImageFont.truetype("/System/Library/Fonts/AppleSDGothicNeo.ttc", size)
    except Exception:
        return ImageFont.load_default()


def lon_to_world_x(lon: float, zoom: int) -> float:
    scale = 256 * (2**zoom)
    return (lon + 180.0) / 360.0 * scale


def lat_to_world_y(lat: float, zoom: int) -> float:
    scale = 256 * (2**zoom)
    lat_rad = radians(lat)
    return (1.0 - log(tan(lat_rad) + 1 / cos(lat_rad)) / pi) / 2.0 * scale


def world_to_pixel(lat: float, lon: float, center_lat: float, center_lon: float, zoom: int, width: int, height: int):
    center_x = lon_to_world_x(center_lon, zoom)
    center_y = lat_to_world_y(center_lat, zoom)
    x = lon_to_world_x(lon, zoom) - center_x + width / 2
    y = lat_to_world_y(lat, zoom) - center_y + height / 2
    return x, y


def add_credit(draw, img_height: int, font):
    draw.text((12, img_height - 22), "© OpenStreetMap contributors (ODbL)", fill="#444", font=font)


def add_legend(draw, font, font_sm):
    box_x, box_y = 18, 18
    box_w = 230
    box_h = 34 + len(POINTS) * 28
    draw.rectangle([box_x, box_y, box_x + box_w, box_y + box_h], fill=(255, 255, 255, 225), outline="#AAA")
    draw.text((box_x + 12, box_y + 8), "1기 신도시 위치", fill="#111", font=font)
    for idx, point in enumerate(POINTS):
        y = box_y + 38 + idx * 28
        draw.ellipse([box_x + 12, y + 4, box_x + 24, y + 16], fill=point["color"], outline="#FFF")
        draw.text((box_x + 34, y), point["name"], fill="#111", font=font_sm)


def main():
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)

    m = StaticMap(WIDTH, HEIGHT, url_template=TILE)
    for point in POINTS:
        m.add_marker(CircleMarker(p(point["lat"], point["lon"]), "white", 16))
        m.add_marker(CircleMarker(p(point["lat"], point["lon"]), point["color"], 11))

    img = m.render(zoom=ZOOM, center=[CENTER[1], CENTER[0]])
    draw = ImageDraw.Draw(img)
    font = load_font(18)
    font_sm = load_font(16)

    add_legend(draw, font, font_sm)

    for point in POINTS:
        x, y = world_to_pixel(point["lat"], point["lon"], CENTER[0], CENTER[1], ZOOM, WIDTH, HEIGHT)
        label_x = x + point["dx"]
        label_y = y + point["dy"]
        bbox = draw.textbbox((label_x, label_y), point["name"], font=font_sm)
        draw.rounded_rectangle([bbox[0] - 6, bbox[1] - 3, bbox[2] + 6, bbox[3] + 3], radius=4, fill=(255, 255, 255, 215), outline="#BBB")
        draw.text((label_x, label_y), point["name"], fill="#111", font=font_sm)

    add_credit(draw, img.height, load_font(13))
    img.save(OUTPUT)
    print(f"saved: {OUTPUT}")


if __name__ == "__main__":
    main()
