#!/usr/bin/env python3
"""Gera HTML da Aula 3.2 (Noções básicas de Geoprocessamento e SIG) a partir do PDF validado."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "modulo3" / "aula2"
MEDIA = "../../media/modulo3/aula2/"
ASSETS = "../../"

COURSE_TITLE = "Análise e Interpretação de Dados em Saúde"
MODULE_NUM = 3
MODULE_TITLE = "Análise Espacial"
AULA_LABEL = "Aula 2"
AULA_TITLE = "Noções básicas de Geoprocessamento e Sistema de Informações Geográficas"

TOPICS = [
    "Sobre esta aula",
    "Introdução",
    "Análise Espacial",
    "Geoprocessamento",
    "Dados espaciais",
    "Sistema de Informações Geográficas",
    "Funções e objetivos do SIG",
    "Referências",
]

AULAS = [
    ("1", "Abordagens teóricas da Geografia da Saúde"),
    ("2", "Noções básicas de Geoprocessamento e SIG"),
    ("3", "Fundamentos de Cartografia"),
    ("4", "Prática de SIG I"),
    ("5", "Prática de SIG II"),
    ("6", "Análise espacial – Área"),
    ("7", "Análise espacial – Pontos"),
]

REFERENCES = [
    "ARONOFF, Stan. <em>Geographic Information Systems: a Management Perspective</em>. "
    "WDL Publications, Ottawa, Canada, 1995. 13 p.",
    "BAILEY, T. C.; GATRELL, A. C. <em>Interactive Spatial Data Analysis</em>. "
    "Harlow: Longman Scientific &amp; Technical, 1995. 413 p.",
    "BURROUGH, P. A.; McDONNELL, R. <em>Principles of Geographical Information Systems</em>. "
    "Oxford: Oxford University Press, 1998.",
    "CÂMARA, Gilberto; DAVIS, Clodoveu; MONTEIRO, Antônio Miguel Vieira (org.). "
    "<em>Introdução à ciência da geoinformação</em>. São José dos Campos: INPE, 2001.",
    "CARVALHO, Marilia Sá; PINA, Maria de Fátima de; SANTOS, Simone Maria dos (org.). "
    "<em>Conceitos básicos de sistemas de informação geográfica e cartografia aplicados à saúde</em>. "
    "Brasília: Organização Pan-Americana da Saúde, 2000.",
    "DAVIS JR., C. A.; ALVES, L. L. Infraestruturas de dados espaciais: potencial para uso local. "
    "<em>Informática Pública</em>, Belo Horizonte, v. 8, n. 1, p. 65–80, 2006.",
    "DRUCK, S.; CARVALHO, M. S.; CÂMARA, G.; MONTEIRO, A. V. M. (eds.). "
    "<em>Análise Espacial de Dados Geográficos</em>. Brasília: EMBRAPA, 2004. (ISBN: 85-7383-260-6).",
    "FITZ, P. R. <em>Cartografia básica</em>. São Paulo: Oficina de Textos, 2008. 143 p.",
    "LONGLEY, Paul A. et al. <em>Geographic information systems and science</em>. 4. ed. Hoboken: Wiley, 2015.",
    "MAGALHÃES, M. A. F. M.; MATOS, V. P.; MEDRONHO, R. A. Avaliação do dado sobre endereço no "
    "Sistema de Informação de Agravos de Notificação utilizando georreferenciamento em nível local de "
    "casos de tuberculose por dois métodos no município do Rio de Janeiro. "
    "<em>Cadernos Saúde Coletiva</em>, Rio de Janeiro, v. 22, p. 192–199, 2014.",
    "PINA, M. F. Armazenamento dos dados em SIG. In: CARVALHO, Marilia Sá; PINA, Maria de Fátima de; "
    "SANTOS, Simone Maria dos (org.). <em>Conceitos básicos de sistemas de informação geográfica e "
    "cartografia aplicados à saúde</em>. Brasília: Organização Pan-Americana da Saúde, 2000.",
    "SCHOLTEN, H. J.; STILLWELL, J. C. H. Geographical information systems: the emerging requirements. "
    "In: SCHOLTEN, H. J.; STILLWELL, J. C. H. (org.). <em>Geographical information systems for urban and "
    "regional planning</em>. Dordrecht: Kluwer Academic Publishers, 1990. p. 3–14.",
    "SILVA, José Rafael Marques da; BAESSO, Murilo Mesquita. "
    "<em>Sistema de navegação global por satélite (GNSS): fundamentos e aplicações práticas</em>. "
    "Curitiba: CRV, 2014. Acesso em: 28 fev. 2026.",
    "TOBLER, W. R. A computer movie simulating urban growth in the Detroit region. "
    "<em>Economic Geography</em>, Worcester, v. 46, n. 2, p. 234–240, 1970.",
]


def row(inner: str, mb: str = "mb-5") -> str:
    return (
        f'<div class="row justify-content-center"><div class="col-12 col-md-10 col-lg-8 {mb}">'
        f"{inner}</div></div>\n"
    )


def p(text: str, *, mb0: bool = False) -> str:
    cls = ' class="mb-0"' if mb0 else ""
    return f"<p{cls}>{text}</p>"


def heading(topic_num: int, title: str) -> str:
    return row(
        f'<div class="heading__block"><span class="small">Tópico {topic_num}</span>'
        f'<h3 class="heading__title">{title}</h3></div>',
        "mb-5",
    )


def subheading(title: str, tag: str = "h4") -> str:
    return row(f'<div class="heading__block"><{tag} class="heading__title">{title}</{tag}></div>', "mb-4")


def ul(items: list[str]) -> str:
    lis = "".join(f'<li class="list-group-item">{item}</li>' for item in items)
    return f'<div class="list"><ul class="list-group">{lis}</ul></div>'


def box(kind: str, label: str, body: str, *, raw: bool = False) -> str:
    body_html = body if raw else f'<p class="mb-0">{body}</p>'
    return row(
        f'<div class="box" data-box="{kind}"><div class="card"><div class="card-header">'
        f'<span class="icone material-symbols-rounded" aria-hidden="true"></span>'
        f'<span class="label">{label}</span></div><div class="card-body">'
        f"{body_html}</div></div></div>"
    )


def box_atencao(body: str) -> str:
    """Box Atenção com o markup exigido pelo CSS (shape divider + padding)."""
    return row(
        '<div class="box" data-box="Atenção">'
        '<div class="card aos-init" data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="600">'
        '<div class="card-header">'
        '<span class="icone material-symbols-rounded" aria-hidden="true"></span>'
        '<span class="label">Atenção</span>'
        "</div>"
        '<div class="card-body">'
        '<div class="custom-shape-divider-top-1720289331">'
        '<svg data-name="Layer 1" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 120" preserveAspectRatio="none">'
        '<path d="M1200 120L0 16.48 0 0 1200 0 1200 120z" class="shape-fill"></path>'
        "</svg>"
        "</div>"
        f"<div><p>{body}</p></div>"
        "</div></div></div>"
    )


def figure_captioned(src: str, caption: str, fonte: str, alt: str = "") -> str:
    return row(
        f'<p class="mb-2"><strong>{caption}</strong></p>'
        f'<figure class="lightbox aos-init" data-aos="fade-up" data-aos-easing="ease-out" data-aos-duration="600">'
        f'<img class="img-fluid mx-auto d-block mb-3 rounded border" src="{MEDIA}{src}" alt="{alt}" loading="lazy" />'
        f"</figure>"
        f'<p class="figure-caption fonte small mb-0">{fonte}</p>'
    )


def figure_plain(src: str, alt: str = "") -> str:
    return row(
        f'<figure class="lightbox aos-init" data-aos="fade-up" data-aos-easing="ease-out" data-aos-duration="600">'
        f'<img class="img-fluid mx-auto d-block mb-3 rounded border" src="{MEDIA}{src}" alt="{alt}" loading="lazy" />'
        f"</figure>"
    )


def _figures_row_inner(figures: list[tuple[str, str, str, str]]) -> str:
    """Lista de (src, alt, caption, fonte)."""
    cols = ""
    for src, alt, caption, fonte in figures:
        cols += (
            f'<div class="col-12 col-md-6 mb-4">'
            f'<p class="mb-2"><strong>{caption}</strong></p>'
            f'<figure class="lightbox aos-init" data-aos="fade-up" data-aos-easing="ease-out" data-aos-duration="600">'
            f'<img class="img-fluid mx-auto d-block mb-3 rounded border" src="{MEDIA}{src}" alt="{alt}" loading="lazy" />'
            f"</figure>"
            f'<p class="figure-caption fonte small mb-0">{fonte}</p></div>'
        )
    return f'<div class="row">{cols}</div>'


def figure_row(figures: list[tuple[str, str, str, str]]) -> str:
    return row(_figures_row_inner(figures))


def voce_sabia_toggle(collapse_id: str, body_html: str, *, label: str = "Você sabia?") -> str:
    return row(
        f'<div class="saiba-mais pb-5">'
        f'<div class="row aos-init" data-aos="fade-left" data-aos-easing="ease-out" data-aos-duration="600">'
        f'<div class="col-12 d-flex justify-content-center">'
        f'<button class="saiba-mais fio-button button-md fio-button-secondary collapsed" type="button" '
        f'data-bs-toggle="collapse" data-bs-target="#{collapse_id}" aria-expanded="false" '
        f'aria-controls="{collapse_id}">'
        f'<span class="icone material-symbols-rounded" aria-hidden="true"></span> {label}</button>'
        f"</div>"
        f'<div class="col-12">'
        f'<div class="mt-3 collapse" id="{collapse_id}">{body_html}</div>'
        f"</div></div></div>"
    )


def flipcard(card_id: str, title: str, back_html: str) -> str:
    return (
        f'<div class="col-12 col-md-6 mb-4"><div class="flipcard"><div class="flip-card">'
        f'<input type="checkbox" id="{card_id}" class="more" aria-hidden="true" />'
        f'<div class="flip-card-inner"><div class="card shadow flip-card-front fundo1">'
        f'<div class="h-100 bg-transparent border-0 text-center"><div class="card-body justify-content-center d-flex flex-column">'
        f'<span class="h5 card-title">{title}</span></div>'
        f'<div class="card-footer text-white"><div class="card-btn">'
        f'<label for="{card_id}" class="fio-button fio-button-primary" aria-hidden="true">'
        f'<img src="{ASSETS}media/templates/flipcard-icon-dark.svg" alt="" width="36" /> Confira</label>'
        f"</div></div></div></div>"
        f'<div class="card flip-card-back"><div class="h-100 bg-transparent border-0 text-center">'
        f'<div class="card-body justify-content-center d-flex flex-column">'
        f'<div class="scrollable text-start">{back_html}</div></div>'
        f'<div class="card-footer"><div class="card-btn">'
        f'<label for="{card_id}" class="fio-button fio-button-secondary return" aria-hidden="true">'
        f'<span class="material-symbols-rounded">arrow_back</span></label></div></div></div></div></div></div></div></div>'
    )


def modal_content(modal_id: str, title: str, body_html: str) -> str:
    return (
        f'<div class="modal fade" id="{modal_id}" tabindex="-1" aria-labelledby="{modal_id}-label" aria-hidden="true">'
        '<div class="modal-dialog modal-xl modal-dialog-scrollable">'
        '<div class="modal-content">'
        '<div class="modal-header">'
        f'<h5 class="modal-title" id="{modal_id}-label">{title}</h5>'
        '<button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Fechar"></button>'
        "</div>"
        f'<div class="modal-body">{body_html}</div>'
        '<div class="modal-footer">'
        '<button type="button" class="fio-button fio-button-primary" data-bs-dismiss="modal">Fechar</button>'
        "</div></div></div></div>"
    )


def geo_tiles(items: list[tuple[str, str, str]], *, base: tuple[str, str, str]) -> str:
    """Quadrados clicáveis que abrem modal. items = [(id, label, body)], base = (id, label, body)."""
    tiles = "".join(
        f'<button type="button" class="geo-tiles__item" data-bs-toggle="modal" '
        f'data-bs-target="#{item_id}">{label}</button>'
        for item_id, label, _ in items
    )
    base_id, base_label, _ = base
    grid = (
        f'<div class="geo-tiles">'
        f'<div class="geo-tiles__grid">{tiles}</div>'
        f'<button type="button" class="geo-tiles__base" data-bs-toggle="modal" '
        f'data-bs-target="#{base_id}">{base_label}</button>'
        f"</div>"
    )
    modals = "".join(
        modal_content(item_id, label, body) for item_id, label, body in [*items, base]
    )
    return row(grid) + modals


def accordion(accordion_id: str, items: list[tuple[str, str]], *, first_open: bool = False) -> str:
    parts = [f'<div class="accordion accordion-flush" id="{accordion_id}">']
    for i, (title, body) in enumerate(items):
        hid = f"{accordion_id}-{i}-h"
        cid = f"{accordion_id}-{i}-c"
        collapsed = "" if first_open and i == 0 else "collapsed"
        expanded = "true" if first_open and i == 0 else "false"
        show = " show" if first_open and i == 0 else ""
        parts.append(
            f'<div class="accordion-item"><h5 class="accordion-header" id="{hid}">'
            f'<button class="accordion-button {collapsed}" type="button" data-bs-toggle="collapse" '
            f'data-bs-target="#{cid}" aria-expanded="{expanded}" aria-controls="{cid}">{title}</button></h5>'
            f'<div id="{cid}" class="accordion-collapse collapse{show}" aria-labelledby="{hid}" '
            f'data-bs-parent="#{accordion_id}"><div class="accordion-body">{body}</div></div></div>'
        )
    parts.append("</div>")
    return row("".join(parts))


def topic_list_html(current: int) -> str:
    items = []
    for i, label in enumerate(TOPICS, 1):
        status = ' status="visited"' if i < current else ""
        aria = (
            'aria-label="Tópico concluído"'
            if i < current
            else 'aria-label="Tópico não concluído"'
        )
        items.append(
            f'\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<a href="topico{i}.html" tabindex="0" role="link" '
            f'class="topic-list__item" {aria}{status}>'
            f'<span class="material-symbols-rounded"></span>{label}</a>'
        )
    return "\n".join(items)


def aulas_dropdown() -> str:
    items = []
    for num, title in AULAS:
        items.append(
            f'\t\t\t\t\t\t\t\t\t<li class="dropdown-menu__item">\n'
            f'\t\t\t\t\t\t\t\t\t\t<a class="dropdown-menu__item-link" tabindex="0" role="link" '
            f'href="../aula{num}/topico1.html"><strong>Aula {num}: </strong>{title}</a>\n'
            f"\t\t\t\t\t\t\t\t\t</li>"
        )
    return "\n".join(items)


def page_nav(num: int) -> str:
    parts = []
    if num > 1:
        parts.append(
            f'<a class="fio-button fio-button-primary" href="topico{num - 1}.html" rel="prev">'
            f'<span class="material-symbols-rounded" aria-hidden="true">west</span> Tópico anterior</a>'
        )
    if num < len(TOPICS):
        parts.append(
            f'<a class="fio-button fio-button-primary" href="topico{num + 1}.html" rel="next">'
            f'Próximo tópico <span class="material-symbols-rounded" aria-hidden="true">east</span></a>'
        )
    else:
        parts.append(
            '<a class="fio-button fio-button-primary" href="../aula3/topico1.html" rel="next">'
            'Próxima aula <span class="material-symbols-rounded" aria-hidden="true">east</span></a>'
        )
    return (
        '\t\t\t\t<section>\n'
        '\t\t\t\t\t<div class="container">\n'
        '\t\t\t\t\t\t<div class="row justify-content-center">\n'
        '\t\t\t\t\t\t\t<div class="col-12 col-md-10 col-lg-8">\n'
        '\t\t\t\t\t\t\t\t<div class="page-nav d-flex justify-content-evenly flex-wrap gap-3">'
        f'{"".join(parts)}</div>\n'
        "\t\t\t\t\t\t\t</div>\n"
        "\t\t\t\t\t\t</div>\n"
        "\t\t\t\t\t</div>\n"
        "\t\t\t\t</section>\n"
    )


def build_sidebar(current: int) -> str:
    topics = topic_list_html(current)
    aulas = aulas_dropdown()
    return f"""					<div class="sidebar__group d-lg-none">
						<div class="sidebar__group-item">
							<div class="sidebar__header">
								<span>Curso</span>
								<a class="mobile-toggle-close" tabindex="0" role="button"><span class="icon material-symbols-rounded">read_more</span></a>
							</div>
						</div>
						<div class="sidebar__group-item">
							<div class="sidebar__title">
								<h1>{COURSE_TITLE}</h1>
							</div>
						</div>
						<div class="sidebar__group-item">
							<ul class="nav">
								<li class="nav-item">
									<a href="../../index.html" class="nav-link" tabindex="0"><span class="icon material-symbols-rounded" aria-hidden="true">home</span>Início</a>
								</li>
								<li class="nav-item">
									<a href="#" class="nav-link" tabindex="0" data-bs-toggle="modal" data-bs-target="#modal-creditos"><span class="icon material-symbols-rounded" aria-hidden="true">format_list_bulleted</span>Créditos</a>
								</li>
							</ul>
						</div>
					</div>

					<div class="sidebar__group">
						<div class="sidebar__group-item">
							<div class="dropend">
								<button id="dropdown-modulos" type="button" class="dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false" data-bs-auto-close="outside" data-bs-offset="0,30">
									<span class="icon material-symbols-rounded" aria-hidden="true">grid_view</span>
									<span class="label">Módulos</span>
								</button>
								<ul class="dropdown-menu" aria-labelledby="dropdown-modulos">
									<li class="d-lg-none dropdown-menu__header">
										<a class="dropdown-menu__back-button" tabindex="0" role="button"><span class="icon material-symbols-rounded">chevron_left</span> Voltar</a>
										<a class="mobile-toggle-close" tabindex="0" role="button"><span class="icon material-symbols-rounded">read_more</span></a>
									</li>
									<li class="dropdown-menu__item">
										<a class="dropdown-menu__item-link" tabindex="0" role="link" href="../../modulo1/aula1/topico1.html"><strong>Módulo 1</strong><br />Estatística</a>
									</li>
									<li class="dropdown-menu__item">
										<a class="dropdown-menu__item-link" tabindex="0" role="link" href="../../modulo2/aula1/topico1.html"><strong>Módulo 2</strong><br />Séries Temporais</a>
									</li>
									<li class="dropdown-menu__item">
										<a class="dropdown-menu__item-link" tabindex="0" role="link" href="../../modulo3/aula1/topico1.html"><strong>Módulo 3</strong><br />Análise Espacial</a>
									</li>
								</ul>
							</div>
						</div>
					</div>
					<div class="divider">
						<hr />
					</div>
					<div class="sidebar__group">
						<div class="sidebar__group-item">
							<span class="text module">Módulo <br class="d-none d-lg-block" /><span>{MODULE_NUM}</span></span>
						</div>
						<div class="sidebar__group-item">
							<div class="dropend">
								<button type="button" class="dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false" data-bs-auto-close="outside" data-bs-offset="0,30">
									<span class="icon material-symbols-rounded" aria-hidden="true">apps</span>
									<span class="label">Conteúdo</span>
								</button>
								<ul class="dropdown-menu">
									<li class="d-lg-none dropdown-menu__header">
										<a class="dropdown-menu__back-button" tabindex="0" role="button"><span class="icon material-symbols-rounded">chevron_left</span> Voltar</a>
										<a class="mobile-toggle-close" tabindex="0" role="button"><span class="icon material-symbols-rounded">read_more</span></a>
									</li>
									<li class="dropdown-menu__title">
										<span class="label">Módulo {MODULE_NUM}</span>
										<span class="title">{MODULE_TITLE}</span>
									</li>
{aulas}
								</ul>
							</div>
						</div>
					</div>
					<div class="divider">
						<hr />
					</div>
					<div class="sidebar__group">
						<div class="sidebar__group-item">
							<span class="text class">{AULA_LABEL}</span>
						</div>
						<div class="sidebar__group-item">
							<div class="dropend">
								<button type="button" class="dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false" data-bs-auto-close="outside" data-bs-offset="0,30">
									<span class="icon material-symbols-rounded" aria-hidden="true">format_list_bulleted</span>
									<span class="label">Tópicos</span>
								</button>
								<ul class="dropdown-menu">
									<li class="d-lg-none dropdown-menu__header">
										<a class="dropdown-menu__back-button" tabindex="0" role="button"><span class="icon material-symbols-rounded">chevron_left</span> Voltar</a>
										<a class="mobile-toggle-close" tabindex="0" role="button"><span class="icon material-symbols-rounded">read_more</span></a>
									</li>
									<li class="dropdown-menu__title">
										<span class="label">{AULA_LABEL}</span>
										<span class="title">{AULA_TITLE}</span>
									</li>
									<li class="dropdown-menu__item">
										<nav class="topic-list">
{topics}
										</nav>
									</li>
								</ul>
							</div>
						</div>
					</div>"""


def build_page(num: int, content: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="pt-br">
	<head>
		<meta charset="utf-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no, user-scalable=yes" />
		<meta http-equiv="content-type" content="text/html; charset=utf-8" />
		<meta name="robots" content="noindex" />
		<meta name="author" content="Fiocruz, Campus Virtual" />
		<meta name="description" content="Curso {COURSE_TITLE}" />
		<link rel="apple-touch-icon" sizes="180x180" href="{ASSETS}media/icons/apple-icon-180x180.png" />
		<link rel="icon" type="image/png" sizes="32x32" href="{ASSETS}media/icons/favicon-32x32.png" />
		<link rel="manifest" href="../media/icons/manifest.json" />
		<meta name="theme-color" content="#001833" />
		<title>Curso {COURSE_TITLE} | Mod {MODULE_NUM} | {AULA_LABEL}</title>
		<link rel="stylesheet" href="{ASSETS}source/bootstrap-5.1.3/css/bootstrap.min.css" />
		<link rel="stylesheet" href="{ASSETS}assets/css/style.css" />
	</head>
	<body>
		<header class="header">
			<div class="mobile-toggle-open">
				<a class="mobile-toggle__button" tabindex="0" role="button">
					<span class="icon material-symbols-rounded">read_more</span>
				</a>
			</div>
			<div class="brand">
				<img class="img-fluid logo-black" src="{ASSETS}media/logos/header-fiocruz-campus-virtual.png" alt="Campus Virtual Fiocruz" />
			</div>
			<div class="title">
				<h1>{COURSE_TITLE}</h1>
			</div>
			<ul class="nav nav-pills">
				<li class="nav-item"><a href="{ASSETS}index.html" class="nav-link">Início</a></li>
				<li class="nav-item"><a href="#" class="nav-link" data-bs-toggle="modal" data-bs-target="#modal-creditos">Créditos</a></li>
			</ul>
		</header>
		<div class="main">
			<div class="sidebar" role="navigation">
				<div class="sidebar__inner" style="position: relative">
{build_sidebar(num)}
				</div>
			</div>
			<div class="content">
				<div id="page-title">
					<div class="container">
						<div class="row align-items-center hstify-content-center justify-content-xxl-start ms-lg-5">
							<div class="col-12 col-md-10 col-lg-11">
								<h2 class="title">
									<span class="label">Módulo {MODULE_NUM} | {AULA_LABEL}</span>
									<br />
									{AULA_TITLE}
								</h2>
							</div>
						</div>
					</div>
				</div>
				<div id="page-content" class="">
					<section>
						<div class="container">
{content}						</div>
					</section>
				</div>
{page_nav(num)}
				<footer>
					<div class="container-fluid">
						<div class="row justify-content-center align-items-center linha-de-marcas">
							<div class="col-12 text-center py-3">
								<img class="img-fluid regua-logos" src="{ASSETS}media/logos/regua-de-logos.png" alt="Régua de logos: ICICT, Campus Virtual Fiocruz e Fiocruz" />
							</div>
						</div>
					</div>
				</footer>
			</div>
		</div>
		<script src="{ASSETS}source/bootstrap-5.1.3/js/bootstrap.bundle.min.js"></script>
		<script type="text/javascript" src="{ASSETS}assets/js/ResizeSensor.js"></script>
		<script type="text/javascript" src="{ASSETS}assets/js/sticky-sidebar.js"></script>
		<script type="text/javascript" src="{ASSETS}assets/js/sidebar.js"></script>
		<script type="text/javascript">
			var sidebar = new StickySidebar(".sidebar", {{
				topSpacing: 0, bottomSpacing: 0, containerSelector: ".main",
				innerWrapperSelector: ".sidebar__inner", minWidth: 991,
			}});
		</script>
		<script type="text/javascript" src="{ASSETS}assets/js/scripts.js"></script>
		<script type="text/javascript" src="{ASSETS}assets/js/custom-anime.js"></script>
		<script type="text/javascript" src="{ASSETS}source/animate/aos/dist/aos.js"></script>
		<script>AOS.init();</script>
	</body>
</html>
"""


def content_sobre() -> str:
    return (
        heading(1, "Sobre esta aula")
        + row(
            p(
                'Seja bem-vindo e bem-vinda à aula <strong>"Noções básicas de Geoprocessamento e '
                'Sistema de Informações Geográficas"</strong>.'
            )
            + p("A seguir, veja algumas informações importantes!")
        )
        + subheading("Objetivos de aprendizagem")
        + row(
            p("Ao final dessa aula, você será capaz de:")
            + ul(
                [
                    "Compreender o Conceito de Análise Espacial;",
                    "Compreender o conceito de Geoprocessamento;",
                    "Enumerar as técnicas de Geoprocessamento;",
                    "Definir Sistemas de Informações Geográficas;",
                    "Enumerar as funções e objetivos de utilização de SIG na Saúde.",
                ]
            )
        )
        + subheading("Autoria")
        + row(
            p(
                "<strong>Mônica de Avelar Figueiredo Mafra Magalhães</strong><br />"
                "Doutora em Saúde Coletiva. Mestrado em Geoprocessamento. Tecnologista em Saúde "
                "Pública. Instituto de Comunicação e Informação Científica e Tecnológica em Saúde (Icict) "
                "da Fundação Oswaldo Cruz (Fiocruz)."
            )
            + p(
                "<strong>Julia Novaes de Barros Peixoto</strong><br />"
                "Mestre em Ciências - Métodos quantitativos em Epidemiologia &amp; Engenheira Cartógrafa."
            )
        )
    )


def content_introducao() -> str:
    return (
        heading(2, "Introdução")
        + row(
            p(
                "Na aula anterior, você explorou os fundamentos teóricos da Geografia da Saúde, seus "
                "conceitos, história, relevância e os primeiros estudos que demonstraram que a distribuição "
                "das doenças no território não ocorre de forma aleatória, mas seguem padrões "
                "relacionados às condições ambientais, sociais e econômicas."
            )
            + p(
                "Dessa forma, atuar no contexto da Geografia da Saúde exige, fundamentalmente, "
                "o domínio e a aplicação da Análise Espacial. Essa abordagem fornece ferramentas "
                "metodológicas que permitem mensurar propriedades e analisar os relacionamentos entre "
                "fenômenos presentes na superfície terrestre, considerando explicitamente sua localização e "
                "incorporando o espaço como elemento central do estudo (Druck et al., 2004)."
            )
            + p(
                "Neste sentido, nesta e nas próximas aulas você será introduzido aos princípios "
                "e as tecnologias que sustentam as abordagens da análise espacial, entendendo como "
                "eles contribuem para a formulação de diagnósticos situacionais, identificação de "
                "vulnerabilidades e planejamento de ações mais eficientes e equitativas nos territórios.",
                mb0=True,
            )
        )
    )


def content_analise_espacial() -> str:
    return (
        heading(3, "Análise Espacial")
        + row(
            p(
                "Conceitualmente Análise Espacial “é um conjunto de técnicas estatísticas e analíticas "
                "especificamente desenvolvidas para dados que possuem referência espacial, considerando "
                "explicitamente a localização, a dependência espacial e a estrutura espacial dos fenômenos” "
                "(Bailey, 1995)."
            )
        )
        + figure_plain(
            "figura-analise-espacial.png",
            "Profissional analisando mapas e dados espaciais em monitores",
        )
        + row(
            p(
                "Esta definição dada por Trevor Bailey, um estatístico britânico reconhecido por seu trabalho "
                "em análise espacial e geoestatística, buscou instrumentalizar um princípio básico que "
                "sustenta a análise espacial conhecido como Primeira Lei da Geografia de Waldo Tobler que "
                "é: “Tudo está relacionado com tudo, mas coisas próximas estão mais relacionadas do que "
                "coisas distantes” (Tobler, 1970)."
            )
            + p(
                "Sem essa lei, não haveria base teórica sólida para afirmar que a proximidade espacial "
                "influencia padrões de saúde e doença.",
                mb0=True,
            )
        )
        + box_atencao(
            "É importante dizer que a análise espacial não se resume ao simples mapeamento "
            "de eventos de saúde. Não é uma mera localização dos eventos! Ela também "
            "engloba o estudo das características particulares dos dados espaciais com toda "
            "a sua complexidade (Kaluzny et al., 1996)."
        )
        + row(
            p(
                "Uma das vantagens da abordagem espacial é permitir representar dados epidemiológicos "
                "em um plano geométrico, considerando que os fenômenos espaciais próximos compartilham "
                "condições ambientais, sociais, históricas, culturais e econômicas semelhantes. "
                "Na interpretação dos mapas gerados como resultado da análise espacial é importante "
                "conhecer os principais mecanismos envolvidos na produção do agravo, as representações "
                "sociais da doença e o modo como ela é tratada pelos serviços de saúde (Pina et al., 2006; "
                "Magalhães, 2014)."
            )
            + p(
                "Pode-se dizer que, a análise espacial envolve raciocínio teórico e interpretação crítica "
                "dos resultados obtidos, sendo necessário uma dimensão operacional e técnica para tratar "
                "a informação geográfica. Aqui entra o Geoprocessamento que disponibiliza e executa "
                "procedimentos técnicos permitindo identificar padrões, relações, tendências e distribuições "
                "no território.",
                mb0=True,
            )
        )
    )


def _cartografia_figures() -> str:
    return _figures_row_inner(
        [
            (
                "figura1-mapa-digital.png",
                "Mapa em formato digital",
                "Figura 1: Mapa em formato digital",
                "Fonte: Foto de autoria de Mônica Magalhaes",
            ),
            (
                "figura2-mapa-analogico.png",
                "Mapa em formato analógico (em papel)",
                "Figura 2: Mapa em formato analógico (em papel)",
                'Fonte: IBGE. Disponível em: <a href="https://biblioteca.ibge.gov.br" '
                'target="_blank" rel="noopener noreferrer">https://biblioteca.ibge.gov.br</a>',
            ),
        ]
    )


def content_geoprocessamento() -> str:
    cartografia_back = (
        "<p>Cartografia digital – se refere à técnica que desenha ou delimita os objetos geográficos "
        "naturais ou artificiais, visíveis na paisagem, unidades de análise e/ou divisões político-"
        "administrativas, criando mapas em formato digital. Atualmente, poucos mapas são "
        "confeccionados em formato analógico ou em papel. Em geral, são mapas digitais "
        "que podem ser editados no computador e impressos, posteriormente, se necessário "
        "(Magalhães, 2014).</p>"
        + _cartografia_figures()
    )
    sensoriamento_back = (
        "<p>Sensoriamento Remoto – compreende um conjunto de técnicas "
        "para obter informações sobre a superfície da Terra sem contato "
        "direto. Ou seja, em vez de medir algo “tocando” o objeto, utiliza-se "
        "instrumentos que detectam e registram radiação eletromagnética "
        "refletida ou emitida pelo alvo (Pina e Madureira, 2000). Normalmente "
        "usado na saúde para coletar dados sobre fatores ambientais que "
        "influenciam a ocorrência de doenças.</p>"
        '<p class="mb-2"><strong>Figura 3: Ilustração de satélites imageando a superfície terrestre.</strong></p>'
        f'<figure class="mb-3"><img class="img-fluid mx-auto d-block rounded border" '
        f'src="{MEDIA}figura3-satelites.png" alt="Satélites imageando a superfície terrestre" loading="lazy" /></figure>'
        '<p class="figure-caption fonte small mb-0">Fonte: David Ducros – CNES, 2002. Disponível em: '
        '<a href="https://phototheque.cnes.fr/cnes/media/2791" target="_blank" rel="noopener noreferrer">'
        "https://phototheque.cnes.fr/cnes/media/2791</a></p>"
    )
    gnss_back = (
        "<p>Global Navigation Satellite System (Sistema Global de Navegação por Satélite) – "
        "sistema baseado em satélites artificiais que transmitem sinais contendo informações "
        "de tempo e posição orbital, permitindo que receptores em terra, no ar ou no mar "
        "determinem sua localização por meio de cálculos matemáticos. Constitui um dos "
        "avanços tecnológicos mais relevantes das últimas décadas, ao possibilitar o "
        "posicionamento preciso de objetos e pessoas em escala global. A precisão obtida "
        "pode variar conforme o tipo de equipamento e as técnicas utilizadas, podendo alcançar "
        "níveis centimétricos em aplicações geodésicas e topográficas.</p>"
        '<p class="mb-2"><strong>Figura 4: Esquema do funcionamento do Sistema Global de Navegação por Satélite</strong></p>'
        f'<figure class="mb-3"><img class="img-fluid mx-auto d-block rounded border" '
        f'src="{MEDIA}figura4-gnss.png" alt="Esquema do funcionamento do GNSS" loading="lazy" /></figure>'
        '<p class="figure-caption fonte small mb-3">Fonte: Elaborado por IA - Copilot</p>'
        "<p class=\"mb-0\"><strong>Popularmente se chama de GPS, mas diferentemente do que se "
        "pensa, o GPS é apenas um dos sistemas que compõem o GNSS, ao lado do GLONASS (Rússia), "
        "Galileo (União Europeia) e BeiDou (China) (Silva &amp; Baesso, 2014).</strong></p>"
    )
    estatistica_back = (
        "<p>Estatística Espacial – não é uma técnica de coleta de dados (como o GPS ou o "
        "sensoriamento remoto), mas uma técnica analítica do Geoprocessamento, "
        "fundamental para interpretar os dados espaciais e gerar conhecimento (Longley, 2015). "
        "Ramo da Estatística que permite analisar a localização espacial de eventos e, além "
        "de localizar e visualizar a ocorrência de fenômenos que se materializam no espaço "
        "geográfico, auxiliar também na geração de modelos da ocorrência destes fenômenos, "
        "incorporando, por exemplo, fatores determinantes, a estrutura de distribuição espacial "
        "ou a identificação de padrões (Santos, 2007).</p>"
    )
    sig_tecnica_back = (
        "<p>Sistema de Informação Geográfica (SIG) – é um ambiente integrado que permite "
        "armazenar, organizar, manipular, analisar e representar dados espaciais. Um SIG envolve "
        "não apenas softwares, mas também hardware, banco de dados, metodologias e "
        "profissionais capacitados (Aronoff, 1995; Câmara, 2001). Trata-se, portanto, da "
        "infraestrutura tecnológica e metodológica que viabiliza o trabalho com informações "
        "geográficas.</p>"
        "<p>O SIG se destaca, dentre as técnicas de Geoprocessamento porque é ele que integra, "
        "organiza, analisa e apresenta dados espaciais de forma estruturada e inteligente. "
        "Enquanto outras técnicas (como as citadas anteriormente) coletam ou produzem dados, o "
        "SIG é o sistema que transforma esses dados em informação útil para tomada de decisão. "
        "Sua capacidade em reunir uma grande quantidade de dados convencionais, de expressão "
        "espacial, estruturando-os adequadamente, tornou o SIG uma ferramenta essencial para a "
        "manipulação de informações geográficas (Carvalho et al., 2000).</p>"
    )
    return (
        heading(4, "Geoprocessamento")
        + row(
            p(
                "O geoprocessamento corresponde ao conjunto de técnicas e procedimentos "
                "computacionais voltados à coleta, tratamento, manipulação e apresentação de dados "
                "espaciais (Câmara, 2001). O geoprocessamento nos possibilita construir mapas de maneira "
                "muito mais simples e rápida do que na época de John Snow, ampliando significativamente "
                "a capacidade analítica nas investigações espaciais. Não à toa seu uso tem se intensificado a "
                "cada década, principalmente devido, especialmente a três fatores:"
            )
            + ul(
                [
                    "Redução do custo de computadores e softwares;",
                    "Desenvolvimento de interfaces mais intuitivas e acessíveis e;",
                    "Crescente disponibilização de dados, favorecida pelo uso ampliado da internet.",
                ]
            )
            + p(
                "Cada uma das técnicas de geoprocessamento tem funções bem específicas. Conheça um "
                "pouco algumas delas:",
                mb0=True,
            )
        )
        + geo_tiles(
            [
                ("modal-m3a2-cartografia", "Cartografia Digital", cartografia_back),
                ("modal-m3a2-sensoriamento", "Sensoriamento Remoto", sensoriamento_back),
                ("modal-m3a2-gnss", "GNSS", gnss_back),
                ("modal-m3a2-estatistica", "Estatística Espacial", estatistica_back),
            ],
            base=(
                "modal-m3a2-sig-tecnica",
                "Sistema de Informações Geográficas - SIG",
                sig_tecnica_back,
            ),
        )
    )


def content_dados_espaciais() -> str:
    grafica_back = (
        "<p>Descreve a localização, as feições geográficas e os relacionamentos espaciais entre "
        "as feições, ou seja, a descrição gráfica do objeto como simbolizado num mapa.</p>"
    )
    nao_grafica_back = (
        "<p>Descreve os fatos e fenômenos, sociais e naturais, representados no mapa, "
        "representa as características, qualidades, ou relacionamentos de feições na "
        "representação cartográfica.</p>"
    )
    return (
        heading(5, "Dados espaciais")
        + row(
            p(
                "Ao longo desta disciplina tem-se destacado de que a Análise Espacial se dedica "
                "ao tratamento de dados espaciais. Mas afinal, qual a diferença de dado espacial para "
                "o dado comum?"
            )
            + p(
                "Dados espaciais são aqueles que possuem uma localização geográfica definida, também "
                "denominados georreferenciados. Esses tipos de dados diferem dos demais, pois possuem "
                "uma posição espacial, isto é, podem ser referenciados ao local de ocorrência na superfície "
                "terrestre (Druck, 2004)."
            )
            + p("Essa posição geográfica pode ser identificada através:")
            + ul(
                [
                    "de um par de coordenadas;",
                    "de seu endereço;",
                    "relacionado a unidades espaciais – bairros, setores censitários, bacias hidrográficas.",
                ]
            )
            + p(
                "Dentro de ambiente de SIG, trabalhamos com dados espaciais. Eles têm como característica "
                "básica o fato de serem compostos por duas componentes distintas (Carvalho et al., 2000):"
            )
        )
        + accordion(
            "m3a2-componentes-dados",
            [
                ("Gráfica (mapas)", grafica_back),
                ("Não-Gráfica (tabelas)", nao_grafica_back),
            ],
        )
        + row(
            p(
                "As componentes gráficas e não gráficas dos dados espaciais possuem características "
                "distintas, o que demanda técnicas específicas para otimizar seu gerenciamento. Na maioria "
                "dos programas de SIG, essas duas componentes são armazenadas em bases de dados "
                "separadas: os dados gráficos são manipulados diretamente pelo software de SIG, "
                "enquanto os dados não gráficos são gerenciados por Sistemas Gerenciadores de Bancos "
                "de Dados (SGBD) convencionais (Câmara et al., 2001)."
            )
        )
        + subheading("Armazenamento dos dados")
        + row(
            p(
                "As componentes gráficas são estruturadas em forma de planos de informação (layers), "
                "organizados como um conjunto de camadas. Cada camada representa um tema e a seleção "
                "dos temas que comporão a base de dados integra o processo de modelagem do sistema e "
                "depende diretamente dos objetivos do projeto. Já as componentes não gráficas são "
                "armazenadas em tabelas organizadas em campos (colunas) e registros (linhas), e geralmente "
                "são gerenciadas por Sistemas Gerenciadores de Banco de Dados (SGBD) (Câmara, 2001)."
            )
        )
        + figure_captioned(
            "figura5-camadas.png",
            "Figura 5: Camadas de armazenamento da componente gráfica",
            "Fonte: Elaborado pelas autoras",
            "Camadas de armazenamento da componente gráfica",
        )
        + box_atencao(
            "É possível realizar operações gráficas entre as camadas, e não apenas combiná-las visualmente."
        )
        + subheading("Integração das componentes")
        + row(
            p(
                "A integração entre as duas componentes dos dados espaciais é uma característica básica dos "
                "SIG e se dá através de códigos comuns que identifiquem univocamente a entidade nas duas "
                "bases, chamados geocódigo.",
                mb0=True,
            )
        )
        + voce_sabia_toggle(
            "m3a2-saiba-mais-ibge",
            "<p>Quando a análise é realizada em nível municipal — ou em unidades territoriais "
            "derivadas dos municípios — utiliza‑se, na maioria das vezes, o código de "
            "município do IBGE, que identifica cada município de forma única. "
            "Esse mesmo código também está presente nas bases gráficas disponibilizadas "
            "pelo DATASUS.</p>",
            label="SAIBA MAIS!",
        )
        + figure_captioned(
            "figura6-geocodigo.png",
            "Figura 6: Esquema didático da representação de geocódigo - ligação entre a componente gráfica e não gráfica.",
            "Fonte: Elaborado pelas autoras",
            "Esquema de geocódigo ligando componente gráfica e não gráfica",
        )
        + row(
            p(
                "Apesar dessa estrutura complexa, tais distinções permanecem completamente imperceptíveis "
                "para o usuário comum.",
                mb0=True,
            )
        )
    )


def vetorial_matricial_table() -> str:
    return (
        '<div class="table-responsive"><table class="table table-sm table-bordered align-middle mb-0">'
        "<thead><tr>"
        "<th scope=\"col\">Modelo</th>"
        "<th scope=\"col\">Descrição</th>"
        "<th scope=\"col\">Representação</th>"
        "<th scope=\"col\">Exemplos em Saúde</th>"
        "</tr></thead><tbody>"
        "<tr><td><strong>Vetorial</strong></td>"
        "<td>Representa o espaço através de entidades geométricas discretas: pontos, linhas e "
        "polígonos. É ideal para representar objetos com limites bem definidos.</td>"
        "<td><strong>Ponto:</strong> Um par de coordenadas (X,Y).<br />"
        "<strong>Linha:</strong> Uma sequência de pontos conectados.<br />"
        "<strong>Polígono:</strong> Uma sequência de linhas que forma uma área fechada.</td>"
        "<td><strong>Pontos:</strong> Residência de um caso, localização de um hospital, um "
        "poste com foco de Aedes aegypti.<br />"
        "<strong>Linhas:</strong> Ruas, rios, rotas de ambulâncias.<br />"
        "<strong>Polígonos:</strong> Municípios, bairros, setores censitários, áreas "
        "de abrangência de uma UBS.</td></tr>"
        "<tr><td><strong>Matricial (Raster)</strong></td>"
        "<td>Representa o espaço como uma grade contínua de células ou pixels, onde cada célula "
        "possui um valor. É ideal para representar fenômenos que variam continuamente no espaço.</td>"
        "<td>Uma matriz de células, onde cada célula tem um valor numérico.</td>"
        "<td>Imagens de satélite, modelos de elevação do terreno, mapas de temperatura, superfícies "
        "de densidade de casos (mapas de calor).</td></tr>"
        "</tbody></table></div>"
    )


def content_sig() -> str:
    return (
        heading(6, "Sistema de Informações Geográficas")
        + row(
            p(
                "Sistema de Informação Geográfica (SIG) – é um ambiente integrado que permite "
                "armazenar, organizar, manipular, analisar e representar dados espaciais. Um SIG envolve "
                "não apenas softwares, mas também hardware, banco de dados, metodologias e "
                "profissionais capacitados (Aronoff, 1995; Câmara, 2001). Trata-se, portanto, da "
                "infraestrutura tecnológica e metodológica que viabiliza o trabalho com informações "
                "geográficas."
            )
        )
        + subheading("Estrutura dos dados gráficos")
        + row(
            p(
                "As duas principais formas de representação de dados gráficos em meio digital são o modelo "
                "matricial e o modelo vetorial. Cada uma delas apresenta vantagens e limitações específicas "
                "conforme a finalidade analítica ou operacional a que se destinam."
            )
            + p(
                "Não há um formato melhor que outro. A maior parte dos Sistemas de Informação "
                "Geográfica (SIG) é capaz de operar simultaneamente com essas duas estruturas, permitindo "
                "ao usuário realizar conversões entre elas de acordo com as demandas do processamento "
                "espacial (Pina, 2000)."
            )
        )
        + row(vetorial_matricial_table())
        + figure_captioned(
            "figura7-vetorial.png",
            "Figura 7: Esquema didático da representação de do modelo vetorial",
            "Fonte: Elaborado pelas autoras com auxílio de IA - ChatGPT",
            "Esquema do modelo vetorial",
        )
        + figure_captioned(
            "figura8-matricial.png",
            "Figura 8: Esquema didático da representação de do modelo matricial",
            "Fonte: Elaborado pelas autoras com auxílio de IA - ChatGPT",
            "Esquema do modelo matricial",
        )
        + row(
            p(
                "É possível realizar operações gráficas entre as camadas, e não apenas "
                "combiná-las visualmente.",
                mb0=True,
            )
        )
    )


def analise_dados_table() -> str:
    return (
        '<div class="table-responsive"><table class="table table-sm table-bordered align-middle mb-0">'
        "<thead><tr>"
        "<th scope=\"col\">Tipo de análise</th>"
        "<th scope=\"col\">Descrição</th>"
        "<th scope=\"col\">Exemplo de aplicação</th>"
        "</tr></thead><tbody>"
        "<tr><td><strong>Pontos no polígono</strong></td>"
        "<td>Identifica a interseção entre pontos e a área (polígono) em que eles se localizam</td>"
        "<td>Identificar e quantificar casos de determinada doença nos bairros de um município</td></tr>"
        "<tr><td><strong>Linhas no polígono</strong></td>"
        "<td>Identifica a interseção entre linhas e a áreas (polígono) em que elas se cruzam</td>"
        "<td>Identificar trechos de rio que cruzam determinados municípios</td></tr>"
        "<tr><td><strong>Áreas de Influência (buffer)</strong></td>"
        "<td>Construção de zonas de largura específica ao redor de pontos, linhas ou áreas. "
        "Utilizado para análise de proximidade</td>"
        "<td>Definir áreas de exposição em torno de uma fonte de exposição, por exemplo uma "
        "indústria poluidora</td></tr>"
        "<tr><td><strong>Interpolação</strong></td>"
        "<td>Estimação de valores em locais não amostrados. Usado muito também para analisar "
        "concentração e densidade de pontos. Usualmente chamados de mapas de calor</td>"
        "<td>Estimar áreas favoráveis à proliferação de vetores com base em armadilhas ou "
        "pontos de coleta.</td></tr>"
        "<tr><td><strong>Sobreposição (overlay)</strong></td>"
        "<td>Ela consiste em combinar duas ou mais camadas espaciais para gerar uma nova camada "
        "contendo a integração das informações. Pode auxiliar em um diagnóstico mais fiel em "
        "relação ao fenômeno estudado</td>"
        "<td>Identificar áreas com baixa cobertura assistencial com a combinação de camadas "
        "contendo: distribuição da população, localização de unidades de saúde e rede viária.</td></tr>"
        "</tbody></table></div>"
    )


def content_funcoes_sig() -> str:
    fig9 = (
        '<p class="mb-2"><strong>Figura 9: Mapa de rendimento médio domiciliar no Brasil - 2010</strong></p>'
        '<div class="row align-items-center">'
        '<div class="col-12 col-md-6 mb-3 mb-md-0">'
        f'<figure class="mb-0"><img class="img-fluid mx-auto d-block rounded border" '
        f'src="{MEDIA}figura9-renda.png" alt="Mapa de rendimento médio domiciliar no Brasil 2010" loading="lazy" /></figure>'
        "</div>"
        '<div class="col-12 col-md-6">'
        "<p class=\"mb-0\">Este mapa temático apresenta a variável “renda média domiciliar”, "
        "representada por meio de diferentes classes de cor. Cada município é categorizado "
        "conforme a faixa de renda a que pertence.</p>"
        "</div></div>"
        '<p class="figure-caption fonte small mt-3 mb-0">Fonte: IBGE, Censo Demográfico 2000/2010. Disponível em: '
        '<a href="https://biblioteca.ibge.gov.br/visualizacao/livros/liv64529_cap8_pt1.pdf" '
        'target="_blank" rel="noopener noreferrer">'
        "https://biblioteca.ibge.gov.br/visualizacao/livros/liv64529_cap8_pt1.pdf</a></p>"
    )
    fig10 = (
        '<p class="mb-2"><strong>Figura 10: Mapa de crescimento populacional do Brasil 2000 - 2010</strong></p>'
        '<div class="row align-items-center">'
        '<div class="col-12 col-md-6 mb-3 mb-md-0">'
        f'<figure class="mb-0"><img class="img-fluid mx-auto d-block rounded border" '
        f'src="{MEDIA}figura10-crescimento.png" alt="Mapa de crescimento populacional do Brasil 2000-2010" loading="lazy" /></figure>'
        "</div>"
        '<div class="col-12 col-md-6">'
        "<p class=\"mb-0\">Este mapa temático utiliza múltiplas simbologias para representar diferentes "
        "informações: (1) a taxa média geométrica de crescimento demográfico anual, apresentada por "
        "meio de classes de cor; (2) o percentual de urbanização, representado por círculos em tons "
        "de azul; e (3) o tamanho populacional, indicado por círculos pretos de diferentes dimensões.</p>"
        "</div></div>"
        '<p class="figure-caption fonte small mt-3 mb-2">Fonte: IBGE, Censo Demográfico 2000/2010. Disponível em: '
        '<a href="https://biblioteca.ibge.gov.br/visualizacao/livros/liv64529_cap3.pdf" '
        'target="_blank" rel="noopener noreferrer">'
        "https://biblioteca.ibge.gov.br/visualizacao/livros/liv64529_cap3.pdf</a></p>"
        "<p class=\"small mb-0\"><strong>Notas:</strong> 1) A taxa média geométrica de crescimento "
        "demográfico anual corresponde ao incremento médio anual da população entre 2000 e 2010. "
        "2) Dados organizados por microrregião</p>"
    )
    return (
        heading(7, "Funções e objetivos do SIG")
        + row(
            p(
                "Os Sistemas de Informações Geográficas permitem a realização de análises espaciais complexas "
                "por meio da rápida construção e modificação de cenários, oferecendo aos gestores subsídios "
                "essenciais para o planejamento e a tomada de decisões. Seu uso tem se ampliado "
                "significativamente em razão de diversos benefícios (Burrough, 1998):"
            )
            + ul(
                [
                    "maior eficiência no armazenamento e na atualização das bases de dados;",
                    "recuperação de informações de maneira mais ágil e organizada;",
                    "produção de resultados com maior precisão;",
                    "rapidez na comparação de alternativas e simulações;",
                    "possibilidade de decisões mais rápidas e fundamentadas.",
                ]
            )
            + p(
                "Os SIG disponibilizam um amplo conjunto de funcionalidades que, dependendo do projeto, "
                "podem atender a finalidades distintas. Entre seus principais objetivos, destacam‑se (Scholten "
                "&amp; Stillwell, 1990):"
            )
            + ul(
                [
                    "a organização e o georreferenciamento dos dados;",
                    "a integração de informações provenientes de múltiplas fontes;",
                    "a visualização estruturada das informações;",
                    "análises espaciais em diferentes níveis de complexidade;",
                    "a predição ou modelagem de ocorrências.",
                ]
            )
            + p("Vamos conhecer um pouco mais de cada um deles.", mb0=True)
        )
        + row(
            '<div class="row g-4 justify-content-center">'
            + flipcard(
                "m3a2-organizacao",
                "Organização e georreferenciamento dos dados",
                "<p class=\"mb-0\">O SIG constitui um instrumento robusto para a organização e o gerenciamento de "
                "informações espacialmente referenciadas. No ambiente do SIG, é possível integrar "
                "diferentes tipos de dados, como limites de bairros, localização pontual de unidades "
                "de saúde, fluxos de pacientes e diversos outros temas permitindo sua visualização "
                "conjunta e de forma coerente no espaço geográfico.</p>",
            )
            + flipcard(
                "m3a2-integracao",
                "Integração de dados provenientes de diversas fontes",
                "<p class=\"mb-0\">O SIG é capaz de integrar informações oriundas de múltiplas fontes, em diferentes "
                "formatos, escalas e sistemas de projeção. Os mapas armazenados no sistema podem ser "
                "continuamente associados a novos conjuntos de dados, permitindo agregar informações "
                "produzidas por diferentes órgãos e instituições e ampliando a consistência das "
                "análises espaciais.</p>",
            )
            + flipcard(
                "m3a2-visualizacao",
                "Visualização das informações",
                "<p class=\"mb-0\">O SIG oferece ao usuário múltiplas possibilidades de apresentação dos dados, "
                "por meio da combinação de diferentes simbologias e técnicas de representação "
                "cartográfica, o que facilita a interpretação espacial. Nas figuras a seguir podemos ver "
                "diferentes tipos de representações cartográficas.</p>",
            )
            + "</div>"
        )
        + row(fig9)
        + row(fig10)
        + row(
            p(
                "<strong>Análise de dados:</strong> trata‑se da principal função de um SIG, pois permite "
                "realizar operações, extrair informações e gerar novos conhecimentos sobre o espaço "
                "geográfico a partir de critérios definidos pelo próprio usuário. Essa capacidade torna "
                "o SIG extremamente útil para o gerenciamento, o planejamento e a execução de projetos, "
                "independentemente do campo de aplicação."
            )
            + p(
                "Nas análises relacionadas especificamente aos componentes geográficos dos dados, "
                "destacam‑se as seguintes operações:"
            )
            + analise_dados_table()
        )
        + row(
            p(
                "<strong>Predição de ocorrências:</strong> A partir da análise de séries históricas, "
                "o mapeamento dos eventos ao longo de diferentes períodos permite identificar em quais "
                "áreas ocorreram modificações, bem como a natureza dessas alterações. Em estudos "
                "conduzidos ao longo de extensos períodos de acompanhamento, torna‑se possível "
                "reconhecer tendências espaciais e antecipar como determinadas áreas podem se "
                "configurar nos anos subsequentes.",
                mb0=True,
            )
        )
    )


def content_referencias() -> str:
    items = "".join(f'<p class="referencias-item">{ref}</p>' for ref in REFERENCES)
    return heading(8, "Referências") + row(f'<div class="referencias-aula">{items}</div>')


CONTENT_BUILDERS = [
    content_sobre,
    content_introducao,
    content_analise_espacial,
    content_geoprocessamento,
    content_dados_espaciais,
    content_sig,
    content_funcoes_sig,
    content_referencias,
]


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for i, builder in enumerate(CONTENT_BUILDERS, 1):
        path = OUT_DIR / f"topico{i}.html"
        path.write_text(build_page(i, builder()), encoding="utf-8")
        print("wrote", path.relative_to(ROOT))

    for path in OUT_DIR.glob("topico*.html"):
        num = int(path.stem.replace("topico", ""))
        if num > len(TOPICS):
            path.unlink()
            print("removed", path.relative_to(ROOT))


if __name__ == "__main__":
    main()
