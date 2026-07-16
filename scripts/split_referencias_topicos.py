#!/usr/bin/env python3
"""Move referências from last tópico into a new dedicated tópico per aula."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

AULAS = [
    {"dir": "modulo1/aula1", "old": 7, "new": 8, "prev_next_label": "Referências"},
    {"dir": "modulo1/aula2", "old": 7, "new": 8, "prev_next_label": "Referências"},
    {"dir": "modulo2/aula1", "old": 4, "new": 5, "prev_next_label": "Referências"},
    {"dir": "modulo2/aula2", "old": 4, "new": 5, "prev_next_label": "Referências"},
    {"dir": "modulo2/aula3", "old": 5, "new": 6, "prev_next_label": "Referências"},
    {"dir": "modulo3/aula1", "old": 6, "new": 7, "prev_next_label": "Referências"},
    {"dir": "modulo3/aula2", "old": 5, "new": 6, "prev_next_label": "Referências"},
    {"dir": "modulo3/aula3", "old": 4, "new": 5, "prev_next_label": "Referências"},
    {"dir": "modulo3/aula4", "old": 5, "new": 6, "prev_next_label": "Referências"},
    {"dir": "modulo3/aula5", "old": 4, "new": 5, "prev_next_label": "Referências"},
]

REF_SECTION_RE = re.compile(
    r"\t\t\t<section>\s*\n"
    r"\t\t\t\t<div class=\"container\">\s*\n"
    r"\t\t\t\t\t<div class=\"row justify-content-center\">\s*\n"
    r"\t\t\t\t\t\t<div class=\"col-12 col-md-10 col-lg-8 mb-5 referencias-aula\">.*?"
    r"\t\t\t\t\t</div>\s*\n"
    r"\t\t\t\t\t</div>\s*\n"
    r"\t\t\t\t</div>\s*\n"
    r"\t\t\t</section>\s*\n",
    re.S,
)

TOPIC_LIST_ENTRY = (
    '\n\t\t\t\t\t\t\t<a href="topico{num}.html" tabindex="0" role="link" class="topic-list__item" '
    'aria-label="Tópico não concluído"><span class="material-symbols-rounded"></span>Referências</a>'
)


def extract_ref_section(content: str):
    m = REF_SECTION_RE.search(content)
    if not m:
        return None, None, content
    section = m.group(0)
    inner = re.search(
        r'<div class="heading__block">.*?</div>\s*\n((?:\t\t\t\t\t\t\t<p class="referencias-item.*?</p>\s*\n)+)',
        section,
        re.S,
    )
    items = inner.group(1) if inner else ""
    cleaned = REF_SECTION_RE.sub("", content, count=1)
    return section, items, cleaned


def build_content_block(old_num: int, new_num: int, ref_items: str) -> str:
    return f"""			<div id="page-content" class="">
				<section>
					<div class="container">
						<div class="row justify-content-center">
							<div class="col-12 col-md-10 col-lg-8 mb-5 referencias-aula">
								<div class="heading__block">
									<span class="small">Tópico {new_num}</span>
									<h3 class="heading__title">Referências</h3>
								</div>
{ref_items}							</div>
						</div>
					</div>
				</section>
			</div>
"""


def fix_old_file_nav(content: str, old: int, new: int, label: str) -> str:
    """Point last content topic's next button to new referências tópico."""
    patterns = [
        (
            rf'(<a class="fio-button fio-button-primary" href=")topico{old}\.html(" rel="next">)([^<]*)(<span)',
            rf'\1topico{new}.html\2{label} \4',
        ),
        (
            rf'(<a class="fio-button fio-button-primary" href=")topico{old}\.html(" rel="next">)([^<]*)(</a>)',
            rf'\1topico{new}.html\2{label}\4',
        ),
    ]
    # Only update if next pointed to external (no change) - update prev topic pointing to old as final
    # Update topico{old-1} next -> topico{new} when it pointed to mod next from old last
    prev = old - 1
    if prev >= 1:
        content = re.sub(
            rf'(href="topico{old}\.html" rel="next">)([^<]+)',
            rf'href="topico{new}.html" rel="next">{label}',
            content,
            count=0,
        )
    # For file that IS old (activity): add next to referências if missing
    if f'topico{old}.html" rel="next"' not in content and 'rel="next"' not in content:
        content = re.sub(
            r'(<div class="page-nav[^"]*">.*?rel="prev"[^>]*>[^<]*</a>)',
            rf'\1<a class="fio-button fio-button-primary" href="topico{new}.html" rel="next">{label} <span class="material-symbols-rounded" aria-hidden="true">east</span></a>',
            content,
            count=1,
            flags=re.S,
        )
    return content


def build_nav_block(prev: int, next_html: str | None, compact: bool) -> str:
    if compact:
        prev_a = f'<a class="fio-button fio-button-primary" href="topico{prev}.html" rel="prev"><span class="material-symbols-rounded" aria-hidden="true">west</span> Tópico anterior</a>'
        next_a = next_html or ""
        inner = prev_a + next_a
        return (
            f'\t\t\t<section><div class="container"><div class="row justify-content-center">'
            f'<div class="col-12 col-md-10 col-lg-8"><div class="page-nav d-flex justify-content-evenly flex-wrap gap-3">'
            f"{inner}</div></div></div></div></section>\n"
        )
    prev_a = (
        f'\t\t\t\t\t\t\t<a class="fio-button fio-button-primary" href="topico{prev}.html" rel="prev">'
        f'<span class="material-symbols-rounded" aria-hidden="true">west</span> Tópico Anterior</a>\n'
    )
    next_a = ""
    if next_html:
        next_a = f"\t\t\t\t\t\t\t{next_html}\n"
    return (
        "\t\t\t<!-- Navegação da aula -->\n"
        "\t\t\t<section>\n"
        "\t\t\t\t<div class=\"container\">\n"
        "\t\t\t\t\t<div class=\"row justify-content-center\">\n"
        "\t\t\t\t\t\t<div class=\"col-12 col-md-10 col-lg-8\">\n"
        "\t\t\t\t\t\t\t<div class=\"page-nav d-flex justify-content-evenly\">\n"
        f"{prev_a}{next_a}"
        "\t\t\t\t\t\t\t</div>\n"
        "\t\t\t\t\t\t</div>\n"
        "\t\t\t\t\t</div>\n"
        "\t\t\t\t</div>\n"
        "\t\t\t</section>\n"
    )


def create_new_topic(old_path: Path, new_path: Path, old: int, new_num: int, ref_items: str, next_full: str | None):
    content = old_path.read_text(encoding="utf-8")
    compact = '<div id="page-title"><div class="container">' in content

    # Shell: everything before page-content
    start = content.find('<div id="page-content"')
    if start == -1:
        start = content.find('<div id="page-content"')
    end_marker = content.find('<!-- Navegação da aula -->')
    if end_marker == -1:
        end_marker = content.find('<section><div class="container"><div class="row justify-content-center"><div class="col-12 col-md-10 col-lg-8"><div class="page-nav')
    footer_start = content.find("<footer>", end_marker if end_marker != -1 else 0)

    head = content[:start]
    footer = content[footer_start:]

    # Normalize ref item indentation (inside content block)
    ref_items = ref_items.replace("\t\t\t\t\t\t\t", "\t\t\t\t\t\t\t")

    page = build_content_block(old, new_num, ref_items)
    nav = build_nav_block(old, next_full, compact)
    new_content = head + page + "\n" + nav + footer
    new_path.write_text(new_content, encoding="utf-8")


def update_topic_lists(aula_dir: Path, new: int):
    entry = TOPIC_LIST_ENTRY.format(num=new)
    for html in aula_dir.glob("topico*.html"):
        text = html.read_text(encoding="utf-8")
        if f'topico{new}.html' in text and "Referências</a>" in text:
            continue
        if 'class="topic-list"' not in text:
            continue
        text = re.sub(
            r'(</nav>)',
            entry + r"\1",
            text,
            count=1,
        )
        html.write_text(text, encoding="utf-8")


def process_aula(cfg):
    aula_dir = ROOT / cfg["dir"]
    old = cfg["old"]
    new = cfg["new"]
    old_path = aula_dir / f"topico{old}.html"
    new_path = aula_dir / f"topico{new}.html"

    content = old_path.read_text(encoding="utf-8")
    section, ref_items, cleaned = extract_ref_section(content)
    if not section:
        print(f"SKIP {cfg['dir']}: no ref section in topico{old}")
        return

    next_match = re.search(
        r'<a class="fio-button fio-button-primary" href="([^"]+)" rel="next">([^<]*)',
        content,
    )
    next_full = None
    if next_match and "topico" not in next_match.group(1):
        label = next_match.group(2).strip()
        next_full = (
            f'<a class="fio-button fio-button-primary" href="{next_match.group(1)}" rel="next">'
            f'{label} <span class="material-symbols-rounded" aria-hidden="true">east</span></a>'
        )

    cleaned = cleaned  # already stripped refs

    compact = "flex-wrap gap-3" in cleaned
    refs_btn = (
        f'<a class="fio-button fio-button-primary" href="topico{new}.html" rel="next">'
        f'{cfg["prev_next_label"]} <span class="material-symbols-rounded" aria-hidden="true">east</span></a>'
    )

    if next_full:
        cleaned = re.sub(
            r'<a class="fio-button fio-button-primary" href="[^"]+" rel="next">[^<]+(?:<span[^>]*></span>)?</a>',
            refs_btn,
            cleaned,
            count=1,
        )
    elif 'rel="next"' not in cleaned:
        if compact:
            cleaned = re.sub(
                r'(<div class="page-nav[^"]*">.*?rel="prev"[^>]*>.*?</a>)',
                rf'\1{refs_btn}',
                cleaned,
                count=1,
                flags=re.S,
            )
        else:
            cleaned = re.sub(
                r'(rel="prev"[^>]*>.*?</a>\s*\n)',
                rf'\1\t\t\t\t\t\t\t{refs_btn}\n',
                cleaned,
                count=1,
                flags=re.S,
            )

    old_path.write_text(cleaned, encoding="utf-8")
    create_new_topic(old_path, new_path, old, new, ref_items, next_full)
    update_topic_lists(aula_dir, new)
    print(f"OK {cfg['dir']}: topico{old} -> topico{new} Referências")


def main():
    for cfg in AULAS:
        process_aula(cfg)


if __name__ == "__main__":
    main()
