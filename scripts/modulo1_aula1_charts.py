"""Gráficos SVG e tabelas de dupla entrada para Aula 1.1 — gerados em código."""
from __future__ import annotations

import math
from typing import Sequence

# Cores alinhadas aos gráficos do PDF validado
C_BAR = "#5B9BD5"
C_PIE_1 = "#5B9BD5"
C_PIE_2 = "#6EC6C6"
C_PIE_3 = "#B4A7D6"
C_CONTROLADA = "#B4A7D6"
C_NAO_CONTROLADA = "#5B9BD5"
C_GRID = "#CCCCCC"
C_AXIS = "#333333"
C_PURPLE_LABEL = "#7030A0"

LINE_COLORS = {
    "Norte": "#2CA6A4",
    "Nordeste": "#6EC6C6",
    "Sudeste": "#2F5597",
    "Sul": "#B4A7D6",
    "Centro-Oeste": "#7030A0",
}

# Nascimentos por região (SINASC) — valores aproximados do gráfico validado
SINASC_YEARS = list(range(2000, 2025))
SINASC_SERIES: dict[str, list[int]] = {
    "Sudeste": [
        1310000, 1295000, 1280000, 1265000, 1250000, 1240000, 1230000, 1220000, 1210000,
        1200000, 1190000, 1185000, 1180000, 1175000, 1170000, 1180000, 1190000, 1180000,
        1170000, 1150000, 1130000, 1100000, 1070000, 1040000, 900000,
    ],
    "Nordeste": [
        920000, 910000, 900000, 890000, 880000, 870000, 860000, 850000, 845000, 840000,
        835000, 830000, 825000, 820000, 815000, 810000, 805000, 800000, 790000, 780000,
        760000, 740000, 720000, 690000, 670000,
    ],
    "Sul": [
        450000, 445000, 440000, 435000, 430000, 425000, 420000, 415000, 410000, 405000,
        400000, 395000, 390000, 385000, 380000, 375000, 370000, 365000, 360000, 355000,
        350000, 345000, 340000, 338000, 335000,
    ],
    "Norte": [
        300000, 298000, 296000, 295000, 294000, 293000, 292000, 291000, 290000, 289000,
        288000, 287000, 286000, 285000, 284000, 283000, 282000, 281000, 280000, 279000,
        278000, 276000, 274000, 272000, 270000,
    ],
    "Centro-Oeste": [
        230000, 229000, 228000, 227500, 227000, 226500, 226000, 225500, 225000, 224500,
        224000, 223500, 223000, 222500, 222000, 221500, 221000, 220500, 220000, 219500,
        219000, 218000, 217000, 214000, 210000,
    ],
}


def _esc(text: str) -> str:
    return (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def svg_wrap(inner: str, *, width: int = 640, height: int = 400, alt: str = "") -> str:
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
        f'class="img-fluid mx-auto d-block mb-3 rounded border" role="img" '
        f'aria-label="{_esc(alt)}" style="max-width:100%;height:auto;background:#fff">'
        f"{inner}</svg>"
    )


def _axis_ticks(mn: float, mx: float, step: float) -> list[float]:
    ticks = []
    v = mn
    while v <= mx + step / 2:
        ticks.append(round(v, 4))
        v += step
    return ticks


def _fmt_num(n: float, decimals: int = 0) -> str:
    if decimals == 0:
        return str(int(round(n)))
    s = f"{n:.{decimals}f}".replace(".", ",")
    return s


def bar_chart_vertical(
    categories: Sequence[str],
    values: Sequence[float],
    *,
    y_max: float,
    y_step: float,
    y_label: str,
    x_label: str,
    alt: str,
) -> str:
    w, h, ml, mr, mt, mb = 640, 400, 56, 24, 24, 72
    pw, ph = w - ml - mr, h - mt - mb
    n = len(categories)
    bar_w = pw / (n * 2.2)
    parts = [
        f'<rect x="0" y="0" width="{w}" height="{h}" fill="#fff"/>',
        f'<rect x="{ml}" y="{mt}" width="{pw}" height="{ph}" fill="none" stroke="{C_AXIS}" stroke-width="1"/>',
    ]
    for tick in _axis_ticks(0, y_max, y_step):
        y = mt + ph - (tick / y_max) * ph
        parts.append(f'<line x1="{ml}" y1="{y:.1f}" x2="{ml + pw}" y2="{y:.1f}" stroke="{C_GRID}" stroke-width="1"/>')
        parts.append(
            f'<text x="{ml - 8}" y="{y + 4:.1f}" text-anchor="end" font-size="11" fill="{C_AXIS}">'
            f"{_fmt_num(tick)}</text>"
        )
    parts.append(
        f'<text x="{ml - 36}" y="{mt + ph / 2}" text-anchor="middle" font-size="12" fill="{C_AXIS}" '
        f'transform="rotate(-90 {ml - 36} {mt + ph / 2})">{_esc(y_label)}</text>'
    )
    for i, (cat, val) in enumerate(zip(categories, values)):
        cx = ml + (i + 0.5) * pw / n
        bh = (val / y_max) * ph
        x = cx - bar_w / 2
        y = mt + ph - bh
        parts.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{bar_w:.1f}" height="{bh:.1f}" fill="{C_BAR}"/>')
        parts.append(
            f'<text x="{cx:.1f}" y="{mt + ph + 16}" text-anchor="middle" font-size="11" fill="{C_AXIS}">'
            f"{_esc(cat)}</text>"
        )
    parts.append(
        f'<text x="{ml + pw / 2}" y="{h - 18}" text-anchor="middle" font-size="12" fill="{C_PURPLE_LABEL}">'
        f"{_esc(x_label)}</text>"
    )
    return svg_wrap("".join(parts), alt=alt)


def bar_chart_horizontal(
    categories: Sequence[str],
    values: Sequence[float],
    *,
    x_max: float,
    x_step: float,
    y_label: str,
    x_label: str,
    alt: str,
) -> str:
    w, h, ml, mr, mt, mb = 640, 360, 120, 40, 24, 48
    pw, ph = w - ml - mr, h - mt - mb
    n = len(categories)
    bar_h = ph / (n * 2.0)
    parts = [
        f'<rect x="0" y="0" width="{w}" height="{h}" fill="#fff"/>',
        f'<rect x="{ml}" y="{mt}" width="{pw}" height="{ph}" fill="none" stroke="{C_AXIS}" stroke-width="1"/>',
    ]
    for tick in _axis_ticks(0, x_max, x_step):
        x = ml + (tick / x_max) * pw
        parts.append(f'<line x1="{x:.1f}" y1="{mt}" x2="{x:.1f}" y2="{mt + ph}" stroke="{C_GRID}" stroke-width="1"/>')
        parts.append(
            f'<text x="{x:.1f}" y="{mt + ph + 18}" text-anchor="middle" font-size="11" fill="{C_AXIS}">'
            f"{_fmt_num(tick, 1)}</text>"
        )
    parts.append(
        f'<text x="{ml + pw / 2}" y="{h - 8}" text-anchor="middle" font-size="12" fill="{C_AXIS}">'
        f"{_esc(x_label)}</text>"
    )
    parts.append(
        f'<text x="18" y="{mt + ph / 2}" text-anchor="middle" font-size="12" fill="{C_AXIS}" '
        f'transform="rotate(-90 18 {mt + ph / 2})">{_esc(y_label)}</text>'
    )
    for i, (cat, val) in enumerate(zip(categories, values)):
        cy = mt + (i + 0.5) * ph / n
        bw = (val / x_max) * pw
        y = cy - bar_h / 2
        parts.append(f'<rect x="{ml}" y="{y:.1f}" width="{bw:.1f}" height="{bar_h:.1f}" fill="{C_BAR}"/>')
        parts.append(
            f'<text x="{ml - 8}" y="{cy + 4:.1f}" text-anchor="end" font-size="11" fill="{C_AXIS}">'
            f"{_esc(cat)}</text>"
        )
    return svg_wrap("".join(parts), height=360, alt=alt)


def pie_chart(
    labels: Sequence[str],
    values: Sequence[float],
    colors: Sequence[str],
    *,
    alt: str,
) -> str:
    w, h, cx, cy, r = 640, 380, 320, 170, 120
    total = sum(values)
    start = -math.pi / 2
    parts = [f'<rect x="0" y="0" width="{w}" height="{h}" fill="#fff"/>']
    parts.append(f'<rect x="40" y="20" width="560" height="280" fill="none" stroke="{C_AXIS}" stroke-width="1"/>')
    for label, val, color in zip(labels, values, colors):
        frac = val / total
        sweep = frac * 2 * math.pi
        end = start + sweep
        x1 = cx + r * math.cos(start)
        y1 = cy + r * math.sin(start)
        x2 = cx + r * math.cos(end)
        y2 = cy + r * math.sin(end)
        large = 1 if sweep > math.pi else 0
        parts.append(
            f'<path d="M {cx:.1f} {cy:.1f} L {x1:.1f} {y1:.1f} A {r} {r} 0 {large} 1 {x2:.1f} {y2:.1f} Z" '
            f'fill="{color}" stroke="#fff" stroke-width="1"/>'
        )
        start = end
    leg_x = 170
    for i, (label, color) in enumerate(zip(labels, colors)):
        x = leg_x + i * 150
        parts.append(f'<rect x="{x}" y="312" width="14" height="14" fill="{color}"/>')
        parts.append(
            f'<text x="{x + 20}" y="323" font-size="11" fill="{C_AXIS}">{_esc(label)}</text>'
        )
    return svg_wrap("".join(parts), height=380, alt=alt)


def histogram_chart(
    bin_edges: Sequence[float],
    frequencies: Sequence[int],
    *,
    y_max: int,
    x_label: str,
    y_label: str,
    alt: str,
) -> str:
    w, h, ml, mr, mt, mb = 640, 400, 48, 24, 24, 56
    pw, ph = w - ml - mr, h - mt - mb
    x_min, x_max = bin_edges[0], bin_edges[-1]
    parts = [
        f'<rect x="0" y="0" width="{w}" height="{h}" fill="#fff"/>',
        f'<rect x="{ml}" y="{mt}" width="{pw}" height="{ph}" fill="none" stroke="{C_AXIS}" stroke-width="1"/>',
    ]
    for tick in range(0, y_max + 1, 2):
        y = mt + ph - (tick / y_max) * ph
        parts.append(f'<line x1="{ml}" y1="{y:.1f}" x2="{ml + pw}" y2="{y:.1f}" stroke="{C_GRID}" stroke-width="1"/>')
        parts.append(
            f'<text x="{ml - 8}" y="{y + 4:.1f}" text-anchor="end" font-size="11" fill="{C_AXIS}">{tick}</text>'
        )
    for edge in bin_edges:
        x = ml + ((edge - x_min) / (x_max - x_min)) * pw
        parts.append(
            f'<text x="{x:.1f}" y="{mt + ph + 18}" text-anchor="middle" font-size="11" fill="{C_AXIS}">'
            f"{_fmt_num(edge)}</text>"
        )
    parts.append(
        f'<text x="{ml - 30}" y="{mt + ph / 2}" text-anchor="middle" font-size="12" fill="{C_AXIS}" '
        f'transform="rotate(-90 {ml - 30} {mt + ph / 2})">{_esc(y_label)}</text>'
    )
    parts.append(
        f'<text x="{ml + pw / 2}" y="{h - 12}" text-anchor="middle" font-size="12" fill="{C_AXIS}">'
        f"{_esc(x_label)}</text>"
    )
    for i, freq in enumerate(frequencies):
        left = bin_edges[i]
        right = bin_edges[i + 1]
        x0 = ml + ((left - x_min) / (x_max - x_min)) * pw
        x1 = ml + ((right - x_min) / (x_max - x_min)) * pw
        bw = x1 - x0 - 1
        bh = (freq / y_max) * ph
        y = mt + ph - bh
        parts.append(f'<rect x="{x0:.1f}" y="{y:.1f}" width="{bw:.1f}" height="{bh:.1f}" fill="{C_BAR}" stroke="{C_AXIS}" stroke-width="0.5"/>')
    return svg_wrap("".join(parts), alt=alt)


def grouped_bar_chart(
    categories: Sequence[str],
    series: dict[str, Sequence[int]],
    series_colors: dict[str, str],
    *,
    y_max: int,
    y_step: int,
    x_label: str,
    y_label: str,
    alt: str,
) -> str:
    w, h, ml, mr, mt, mb = 640, 420, 48, 24, 24, 88
    pw, ph = w - ml - mr, h - mt - mb
    n = len(categories)
    names = list(series.keys())
    group_w = pw / n
    bar_w = group_w / (len(names) + 1)
    parts = [
        f'<rect x="0" y="0" width="{w}" height="{h}" fill="#fff"/>',
        f'<rect x="{ml}" y="{mt}" width="{pw}" height="{ph}" fill="none" stroke="{C_AXIS}" stroke-width="1"/>',
    ]
    for tick in range(0, y_max + 1, y_step):
        y = mt + ph - (tick / y_max) * ph
        parts.append(f'<line x1="{ml}" y1="{y:.1f}" x2="{ml + pw}" y2="{y:.1f}" stroke="{C_GRID}" stroke-width="1"/>')
        parts.append(
            f'<text x="{ml - 8}" y="{y + 4:.1f}" text-anchor="end" font-size="11" fill="{C_AXIS}">{tick}</text>'
        )
    parts.append(
        f'<text x="{ml - 28}" y="{mt + ph / 2}" text-anchor="middle" font-size="12" fill="{C_AXIS}" '
        f'transform="rotate(-90 {ml - 28} {mt + ph / 2})">{_esc(y_label)}</text>'
    )
    for i, cat in enumerate(categories):
        gx = ml + i * group_w
        parts.append(
            f'<text x="{gx + group_w / 2:.1f}" y="{mt + ph + 18}" text-anchor="middle" font-size="11" fill="{C_AXIS}">'
            f"{_esc(cat)}</text>"
        )
        for j, name in enumerate(names):
            val = series[name][i]
            x = gx + (j + 0.75) * bar_w
            bh = (val / y_max) * ph
            y = mt + ph - bh
            parts.append(
                f'<rect x="{x:.1f}" y="{y:.1f}" width="{bar_w * 0.85:.1f}" height="{bh:.1f}" fill="{series_colors[name]}"/>'
            )
    parts.append(
        f'<text x="{ml + pw / 2}" y="{h - 52}" text-anchor="middle" font-size="12" fill="{C_AXIS}">'
        f"{_esc(x_label)}</text>"
    )
    leg_x = ml + pw / 2 - 120
    for j, name in enumerate(names):
        x = leg_x + j * 150
        parts.append(f'<rect x="{x}" y="{h - 36}" width="14" height="14" fill="{series_colors[name]}"/>')
        parts.append(f'<text x="{x + 20}" y="{h - 24}" font-size="11" fill="{C_AXIS}">{_esc(name)}</text>')
    return svg_wrap("".join(parts), height=420, alt=alt)


def scatter_chart(
    points: Sequence[tuple[float, float]],
    *,
    x_min: float,
    x_max: float,
    y_min: float,
    y_max: float,
    x_step: float,
    y_step: float,
    x_label: str,
    y_label: str,
    alt: str,
) -> str:
    w, h, ml, mr, mt, mb = 640, 400, 48, 24, 24, 56
    pw, ph = w - ml - mr, h - mt - mb
    parts = [
        f'<rect x="0" y="0" width="{w}" height="{h}" fill="#fff"/>',
        f'<rect x="{ml}" y="{mt}" width="{pw}" height="{ph}" fill="none" stroke="{C_AXIS}" stroke-width="1"/>',
    ]
    for tick in _axis_ticks(x_min, x_max, x_step):
        x = ml + ((tick - x_min) / (x_max - x_min)) * pw
        parts.append(f'<line x1="{x:.1f}" y1="{mt}" x2="{x:.1f}" y2="{mt + ph}" stroke="{C_GRID}" stroke-width="1"/>')
        parts.append(
            f'<text x="{x:.1f}" y="{mt + ph + 18}" text-anchor="middle" font-size="11" fill="{C_AXIS}">'
            f"{_fmt_num(tick)}</text>"
        )
    for tick in _axis_ticks(y_min, y_max, y_step):
        y = mt + ph - ((tick - y_min) / (y_max - y_min)) * ph
        parts.append(f'<line x1="{ml}" y1="{y:.1f}" x2="{ml + pw}" y2="{y:.1f}" stroke="{C_GRID}" stroke-width="1"/>')
        parts.append(
            f'<text x="{ml - 8}" y="{y + 4:.1f}" text-anchor="end" font-size="11" fill="{C_AXIS}">'
            f"{_fmt_num(tick)}</text>"
        )
    parts.append(
        f'<text x="{ml + pw / 2}" y="{h - 12}" text-anchor="middle" font-size="12" fill="{C_AXIS}">'
        f"{_esc(x_label)}</text>"
    )
    parts.append(
        f'<text x="{ml - 30}" y="{mt + ph / 2}" text-anchor="middle" font-size="12" fill="{C_AXIS}" '
        f'transform="rotate(-90 {ml - 30} {mt + ph / 2})">{_esc(y_label)}</text>'
    )
    for px, py in points:
        x = ml + ((px - x_min) / (x_max - x_min)) * pw
        y = mt + ph - ((py - y_min) / (y_max - y_min)) * ph
        parts.append(
            f'<circle cx="{x:.1f}" cy="{y:.1f}" r="4" fill="#fff" stroke="{C_BAR}" stroke-width="1.5"/>'
        )
    return svg_wrap("".join(parts), alt=alt)


def line_chart_multi(
    years: Sequence[int],
    series: dict[str, Sequence[int]],
    *,
    y_max: int,
    y_step: int,
    y_label: str,
    alt: str,
) -> str:
    w, h, ml, mr, mt, mb = 720, 440, 64, 24, 24, 100
    pw, ph = w - ml - mr, h - mt - mb
    n = len(years)
    parts = [
        f'<rect x="0" y="0" width="{w}" height="{h}" fill="#fff"/>',
        f'<rect x="{ml}" y="{mt}" width="{pw}" height="{ph}" fill="none" stroke="{C_AXIS}" stroke-width="1"/>',
    ]
    for tick in range(0, y_max + 1, y_step):
        y = mt + ph - (tick / y_max) * ph
        parts.append(f'<line x1="{ml}" y1="{y:.1f}" x2="{ml + pw}" y2="{y:.1f}" stroke="{C_GRID}" stroke-width="1"/>')
        label = f"{tick // 1000:,}".replace(",", ".")
        parts.append(
            f'<text x="{ml - 8}" y="{y + 4:.1f}" text-anchor="end" font-size="10" fill="{C_AXIS}">{label}</text>'
        )
    parts.append(
        f'<text x="{ml - 44}" y="{mt + ph / 2}" text-anchor="middle" font-size="11" fill="{C_AXIS}" '
        f'transform="rotate(-90 {ml - 44} {mt + ph / 2})">{_esc(y_label)}</text>'
    )
    for i, year in enumerate(years):
        x = ml + (i / (n - 1)) * pw
        parts.append(
            f'<text x="{x:.1f}" y="{mt + ph + 14}" text-anchor="end" font-size="9" fill="{C_AXIS}" '
            f'transform="rotate(-90 {x:.1f} {mt + ph + 14})">{year}</text>'
        )
    for name, values in series.items():
        color = LINE_COLORS.get(name, C_BAR)
        pts = []
        for i, val in enumerate(values):
            x = ml + (i / (n - 1)) * pw
            y = mt + ph - (val / y_max) * ph
            pts.append(f"{x:.1f},{y:.1f}")
        parts.append(
            f'<polyline fill="none" stroke="{color}" stroke-width="2" points="{" ".join(pts)}"/>'
        )
    leg_names = list(series.keys())
    leg_w = len(leg_names) * 130
    leg_x = ml + (pw - leg_w) / 2
    for i, name in enumerate(leg_names):
        x = leg_x + i * 130
        color = LINE_COLORS.get(name, C_BAR)
        parts.append(f'<line x1="{x}" y1="{h - 52}" x2="{x + 18}" y2="{h - 52}" stroke="{color}" stroke-width="2"/>')
        parts.append(f'<text x="{x + 24}" y="{h - 48}" font-size="10" fill="{C_AXIS}">Região {name}</text>')
    return svg_wrap("".join(parts), width=720, height=440, alt=alt)


def cross_table(
    row_label: str,
    col_label: str,
    row_cats: Sequence[str],
    col_cats: Sequence[str],
    rows: list[list[tuple[str, str]]],
    footer: list[tuple[str, str]],
) -> str:
    """Tabela de dupla entrada com N e % por célula (inclui totais por linha na última coluna)."""
    subheads = (
        f'<th scope="col" colspan="{len(col_cats) * 2}" class="text-center">{_esc(col_label)}</th>'
        '<th scope="col" colspan="2" class="text-center">Total</th>'
    )
    subcols = "".join(
        f'<th scope="col" colspan="2" class="text-center">{_esc(c)}</th>' for c in col_cats
    )
    subcols += '<th scope="col" colspan="2" class="text-center">Total</th>'
    subcols2 = "".join(
        '<th scope="col" class="text-end">N</th><th scope="col" class="text-end">%</th>'
        for _ in range(len(col_cats) + 1)
    )
    body = ""
    for row_cat, row_cells in zip(row_cats, rows):
        tds = f'<th scope="row">{_esc(row_cat)}</th>'
        for n, pct in row_cells:
            tds += f'<td class="text-end">{n}</td><td class="text-end">{pct}</td>'
        body += f"<tr>{tds}</tr>"
    total_tds = '<th scope="row"><strong>Total</strong></th>'
    for n, pct in footer:
        total_tds += f'<td class="text-end"><strong>{n}</strong></td><td class="text-end"><strong>{pct}</strong></td>'
    body += f"<tr>{total_tds}</tr>"
    return (
        '<table class="table table-sm table-bordered table-sides-open align-middle mb-0">'
        f'<thead><tr><th scope="col" rowspan="3">{_esc(row_label)}</th>{subheads}</tr>'
        f"<tr>{subcols}</tr><tr>{subcols2}</tr></thead>"
        f"<tbody>{body}</tbody></table>"
    )


def imc_histogram_bins(imc_values: Sequence[str]) -> tuple[list[float], list[int]]:
    edges = [15, 20, 25, 30, 35, 40, 45]
    counts = [0] * (len(edges) - 1)
    for raw in imc_values:
        v = float(raw.replace(",", "."))
        for i in range(len(edges) - 1):
            if edges[i] <= v < edges[i + 1] or (i == len(edges) - 2 and v == edges[i + 1]):
                counts[i] += 1
                break
    return edges, counts


def scatter_points_from_imc(imc_values: Sequence[str]) -> list[tuple[float, float]]:
    """Pares idade × IMC correlacionados (dados fictícios alinhados ao gráfico 7)."""
    imcs = [float(v.replace(",", ".")) for v in imc_values]
    n = len(imcs)
    ages = [35 + (i / max(n - 1, 1)) * 40 for i in range(n)]
    return list(zip(ages, imcs))
