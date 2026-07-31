#!/usr/bin/env python3
"""Gera HTML da Aula 3.6 (Análise Espacial de Dados – Área)."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "modulo3" / "aula6"
MEDIA = "../../media/modulo3/aula6/"
ASSETS = "../../"

COURSE_TITLE = "Análise e Interpretação de Dados em Saúde"
MODULE_NUM = 3
MODULE_TITLE = "Análise Espacial"
AULA_LABEL = "Aula 6"
AULA_TITLE = "Análise Espacial de Dados – Área"

TOPICS = [
    "Sobre esta aula",
    "Introdução",
    "O que são Dados de Área?",
    "Autocorrelação Espacial",
    "Matriz de Vizinhança",
    "Índice de Moran Global (I)",
    "Análise Local: Clusters (LISA)",
    "Instabilidade de Taxas",
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

CLUSTER_POPOVER = (
    "Na saúde podemos dizer que um cluster descreve um padrão de não aleatoriedade, "
    "onde os casos de uma doença não estão distribuídos de forma homogênea ou ao "
    "acaso em um território, mas sim concentrados em regiões específicas."
)

REFERENCES = [
    "CÂMARA, G.; CARVALHO, M. S.; CRUZ, O. G.; CORREA, V. Análise Espacial de Áreas. "
    "In: DRUCK, S.; CARVALHO, M. S.; CÂMARA, G.; MONTEIRO, A. V. M. (org.). "
    "<em>Análise Espacial de Dados Geográficos</em>. Brasília: EMBRAPA, 2004.",
    "CARVALHO, M. S.; SOUZA‑SANTOS, R. Análise de dados espaciais em saúde pública: "
    "métodos, problemas, perspectivas. <em>Cadernos de Saúde Pública</em>, v. 21, n. 2, "
    "p. 361‑378, 2005.",
    "DILÉLIO, A. S.; NATIVIDADE, M.; FACCHINI, L. A.; PEREIRA, M.; TOMASI, E. Estrutura "
    "e processo na atenção primária à saúde das crianças e distribuição espacial da "
    "mortalidade infantil. <em>Revista de Saúde Pública</em>, v. 58, p. 21, 2024. Disponível em: "
    '<a href="https://rsp.fsp.usp.br/pt-br/article/estrutura-e-processo-na-atencao-primaria-a-saude-das-criancas-e-distribuicaoespacial-da-mortalidade-infantil/" '
    'target="_blank" rel="noopener noreferrer">'
    "https://rsp.fsp.usp.br/pt-br/article/estrutura-e-processo-na-atencao-primaria-a-saude-das-criancas-e-distribuicaoespacial-da-mortalidade-infantil/</a>.",
    "MARSICANO, J. A.; SOUSA, G. C. M.; TOLEDO, G. S.; SILVA, A. M.; LEMOS, C. A.; "
    "CORDEIRO, R. C. L.; SILVA, R. A. Análise espacial da mortalidade por câncer de boca "
    "e determinantes de saúde. <em>Revista de Odontologia da UNESP</em>, v. 54, p. e20250001, "
    "2025. Disponível em: "
    '<a href="https://www.scielo.br/j/rounesp/a/bJJsnSBYxHVpfPLFZQmsRzQ/?format=html&amp;lang=pt" '
    'target="_blank" rel="noopener noreferrer">'
    "https://www.scielo.br/j/rounesp/a/bJJsnSBYxHVpfPLFZQmsRzQ/?format=html&amp;lang=pt</a>.",
    "SANTOS, E. G. O.; BARBOSA, I. R. Conglomerados espaciais da mortalidade por suicídio "
    "no nordeste do Brasil e sua relação com indicadores socioeconômicos. "
    "<em>Cadernos de Saúde Coletiva</em>, v. 25, n. 3, p. 361‑367, 2017.",
    "SANTOS, S. M.; SOUZA, W. V. (orgs.). <em>Introdução à Estatística Espacial para a "
    "Saúde Pública</em>. Brasília: Ministério da Saúde/Fiocruz, 2007.",
    "SANTOS, S. M.; BARCELLOS, C. (Orgs.). <em>Série B. Abordagens espaciais na saúde "
    "pública</em>. Brasília: Ministério da Saúde; Fundação Oswaldo Cruz, 2006. v. 1.",
    "SOUZA, W. V.; BARCELLOS, C. C.; CARVALHO, M. S.; CRUZ, O. G.; ALBUQUERQUE, M. F. P. M.; "
    "ALVES, K. R.; LAPA, T. M. Aplicação de modelo bayesiano empírico na análise espacial "
    "da ocorrência de hanseníase. <em>Revista de Saúde Pública</em>, v. 35, n. 5, "
    "p. 474‑480, 2001.",
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


def box_atencao(body: str, *, raw: bool = False, label: str = "Atenção") -> str:
    inner = body if raw else f"<p>{body}</p>"
    return row(
        '<div class="box" data-box="Atenção">'
        '<div class="card aos-init" data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="600">'
        '<div class="card-header">'
        '<span class="icone material-symbols-rounded" aria-hidden="true"></span>'
        f'<span class="label">{label}</span>'
        "</div>"
        '<div class="card-body">'
        '<div class="custom-shape-divider-top-1720289331">'
        '<svg data-name="Layer 1" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 120" preserveAspectRatio="none">'
        '<path d="M1200 120L0 16.48 0 0 1200 0 1200 120z" class="shape-fill"></path>'
        "</svg>"
        "</div>"
        f"<div>{inner}</div>"
        "</div></div></div>"
    )


def importante_toggle(collapse_id: str, body_html: str) -> str:
    """Box IMPORTANTE! expansível: conteúdo só aparece após clicar no botão."""
    return row(
        f'<div class="saiba-mais pb-5">'
        f'<div class="row aos-init" data-aos="fade-left" data-aos-easing="ease-out" data-aos-duration="600">'
        f'<div class="col-12 d-flex justify-content-center">'
        f'<button class="saiba-mais fio-button button-md fio-button-secondary collapsed" type="button" '
        f'data-bs-toggle="collapse" data-bs-target="#{collapse_id}" aria-expanded="false" '
        f'aria-controls="{collapse_id}">'
        f'<span class="icone material-symbols-rounded" aria-hidden="true"></span> IMPORTANTE!</button>'
        f"</div>"
        f'<div class="col-12">'
        f'<div class="mt-3 collapse" id="{collapse_id}">{body_html}</div>'
        f"</div></div></div>"
    )


def box_azul(body: str) -> str:
    return row(
        '<div class="p-4 rounded aos-init" data-aos="fade-up" data-aos-easing="ease-out" '
        'data-aos-duration="600" style="background-color:#d7f3f8;">'
        f"{body}</div>"
    )


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


def figure_captioned(src: str, caption: str, fonte: str, alt: str = "") -> str:
    return row(
        f'<p class="mb-2"><strong>{caption}</strong></p>'
        f'<figure class="lightbox aos-init" data-aos="fade-up" data-aos-easing="ease-out" data-aos-duration="600">'
        f'<img class="img-fluid mx-auto d-block mb-3 rounded border" src="{MEDIA}{src}" alt="{alt or caption}" loading="lazy" />'
        f"</figure>"
        f'<p class="figure-caption fonte small mb-0">{fonte}</p>'
    )


def figure_plain(src: str, alt: str) -> str:
    return row(
        f'<figure class="lightbox aos-init" data-aos="fade-up" data-aos-easing="ease-out" data-aos-duration="600">'
        f'<img class="img-fluid mx-auto d-block mb-3 rounded border" src="{MEDIA}{src}" alt="{alt}" loading="lazy" />'
        f"</figure>"
    )


def simple_table(headers: list[str], rows: list[list[str]], *, note: str = "") -> str:
    th = "".join(f'<th scope="col">{h}</th>' for h in headers)
    body = ""
    for r in rows:
        tds = "".join(f"<td>{c}</td>" for c in r)
        body += f"<tr>{tds}</tr>"
    note_html = f'<p class="small mt-2 mb-0">{note}</p>' if note else ""
    return (
        '<div class="table-responsive"><table class="table table-sm table-bordered align-middle mb-0">'
        f"<thead><tr>{th}</tr></thead><tbody>{body}</tbody></table></div>{note_html}"
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


def popover_link(text: str, title: str, content: str, *, placement: str = "top") -> str:
    esc = content.replace('"', "&quot;")
    return (
        f'<a tabindex="0" role="button" data-bs-toggle="popover" data-bs-trigger="focus" '
        f'data-bs-placement="{placement}" data-bs-html="true" data-bs-title="{title}" '
        f'data-bs-content="<p>{esc}</p>"><strong>{text}</strong></a>'
    )


def a(href: str, label: str | None = None) -> str:
    text = label or href
    return f'<a href="{href}" target="_blank" rel="noopener noreferrer">{text}</a>'


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
            '<a class="fio-button fio-button-primary" href="../aula7/topico1.html" rel="next">'
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
            p('Seja bem-vindo e bem-vinda à aula “Análise Espacial de Dados – Área”.')
            + p("A seguir, veja algumas informações importantes!")
        )
        + subheading("Objetivos de aprendizagem")
        + row(
            p("Ao final dessa aula, você será capaz de:")
            + ul(
                [
                    "Compreender o que são dados de área e reconhecer suas particularidades "
                    "no contexto da saúde pública.",
                    "Interpretar mapas coropléticos e identificar limitações da análise "
                    "exclusivamente visual.",
                    "Entender o conceito de autocorrelação espacial e suas implicações para "
                    "a análise de indicadores de saúde.",
                    "Interpretar o Índice de Moran Global e Local",
                    "Reconhecer o problema da instabilidade das taxas em áreas com pequenas "
                    "populações.",
                    "Compreender o propósito da suavização de taxas, especialmente por meio "
                    "do Estimador Bayesiano Empírico.",
                ]
            )
        )
        + subheading("Autoria")
        + row(
            p(
                "<strong>Diego Ricardo Xavier</strong><br />"
                "Doutor em Epidemiologia. Mestrado em Saúde Pública. Pesquisador em Saúde Pública<br />"
                "Instituto de Comunicação e Informação Científica e Tecnológica em Saúde (Icict) "
                "da Fundação Oswaldo Cruz (Fiocruz)"
            )
            + p(
                "<strong>Mônica de Avelar Figueiredo Mafra Magalhães</strong><br />"
                "Doutora em Saúde Coletiva. Mestrado em Geoprocessamento. Tecnologista em Saúde "
                "Pública. Instituto de Comunicação e Informação Científica e Tecnológica em Saúde (Icict) "
                "da Fundação Oswaldo Cruz (Fiocruz)."
            )
            + p(
                "<strong>Julia Novaes de Barros Peixoto</strong><br />"
                "Mestre em Ciências - Métodos quantitativos em Epidemiologia &amp; Engenheira Cartógrafa.",
                mb0=True,
            )
        )
    )


def content_introducao() -> str:
    clusters = popover_link("clusters", "Clusters", CLUSTER_POPOVER)
    return (
        heading(2, "Introdução")
        + row(
            p(
                "A partir do que você explorou anteriormente e do mapa temático elaborado nas últimas "
                "aulas, avançaremos agora para a base conceitual da análise de dados organizados "
                "por áreas geográficas. Esse tipo de análise utiliza informações agregadas em polígonos "
                "territoriais como municípios, bairros, setores censitários ou estados e é amplamente "
                "empregada no contexto do Sistema Único de Saúde (SUS)."
            )
            + p(
                "Isso porque grande parte dos dados provenientes de sistemas de informação, como o "
                "SINAN (Sistema de Informação de Agravos de Notificação), o SIM (Sistema de Informações "
                "sobre Mortalidade) e os dados demográficos do IBGE, é disponibilizada de forma agregada "
                "segundo unidades administrativas (Carvalho &amp; Souza-Santos, 2005; Câmara, et al., 2004)."
            )
            + p(
                "Essa abordagem permite investigar como doenças, fatores de risco e serviços de saúde "
                "se distribuem no território e é especialmente útil para:"
            )
            + ul(
                [
                    "Identificar padrões espaciais de doenças, observando onde há maior ou menor ocorrência.",
                    f"Detectar áreas de risco ({clusters}), revelando regiões prioritárias para intervenção.",
                    "Relacionar saúde com fatores socioambientais, como saneamento, renda, densidade "
                    "populacional e condições de moradia.",
                    "Apoiar o planejamento dos serviços de saúde, contribuindo para definir a localização "
                    "de hospitais, postos e ações de vacinação.",
                    "Monitorar e prever surtos, acompanhando a evolução espacial e temporal das doenças.",
                    "Reduzir desigualdades em saúde, ao evidenciar desigualdades territoriais de acesso "
                    "e vulnerabilidade.",
                ]
            )
            + p(
                "Em síntese, a análise de área é investigar padrões espaciais na distribuição de taxas ou "
                "indicadores de saúde, como taxas de mortalidade, coeficientes de incidência ou indicadores "
                "socioeconômicos. A questão central é entender se as áreas com valores altos (ou baixos) "
                "de um indicador tendem a se agrupar no espaço, ou se sua distribuição é aleatória "
                "(Câmara, et al., 2004)."
            )
        )
        + figure_captioned(
            "figura1-padroes.png",
            "Figura 1 - Padrões Espaciais Comuns em Mapas Coropléticos.",
            "Fonte: Elaborado pelos autores (2026).",
        )
        + row(
            p(
                "Ao elaborar mapas que mostram como eventos de saúde se distribuem no território, "
                "podemos observar diferentes padrões espaciais. A figura apresenta três exemplos fictícios "
                "que ilustram situações comuns."
            )
            + p(
                "No primeiro quadro, à esquerda, vemos que as taxas mais altas — indicadas pelas cores "
                "mais intensas — se concentram ao redor de uma única área. Esse tipo de padrão sugere a "
                "presença de uma fonte específica de exposição, como uma indústria que libera poluentes."
            )
            + p(
                "No segundo quadro, ao centro, as maiores taxas aparecem alinhadas, formando uma faixa "
                "contínua. Esse formato linear pode indicar que a exposição segue o traçado de algum "
                "elemento geográfico, como uma estrada ou um rio."
            )
            + p(
                "Já no terceiro quadro, observamos um padrão em mosaico: as áreas com taxas mais "
                "elevadas se distribuem em vários pontos, formando diversos aglomerados (clusters). "
                "Esse comportamento pode estar associado a múltiplas fontes de exposição espalhadas "
                "pelo território, refletindo características sociais e organizacionais das cidades "
                "(Santos &amp; Barcellos, 2006).",
                mb0=True,
            )
        )
    )


def content_dados_area() -> str:
    return (
        heading(3, "O que são Dados de Área?")
        + row(
            p(
                "Dados de área são valores (contagens, taxas ou proporções) associados a uma unidade de "
                "área geográfica definida. Por exemplo, a taxa de mortalidade infantil de um município, a "
                "proporção de domicílios com saneamento básico em um bairro, ou o número de casos de "
                "leishmaniose por setor censitário. A forma mais comum de visualização desses dados é "
                "através de mapas coropléticos, que você já estudou nas aulas anteriores, onde cada área é "
                "colorida de acordo com o valor da variável de interesse (Câmara, et al., 2004)."
            )
            + p(
                "Embora sejam visualmente informativos e úteis em uma primeira etapa de análise visual "
                "e exploratória, os mapas coropléticos podem levar a interpretações equivocadas. "
                "A observação inicial pode sugerir a existência de padrões espaciais, porém nossos olhos "
                "podem ser induzidos a perceber agrupamentos ou tendências que não são, necessariamente, "
                "estatisticamente significativos. Por essa razão, após essa etapa exploratória, torna-se "
                "fundamental empregar ferramentas de estatística espacial, para testar formalmente a "
                "existência de padrões espaciais.",
                mb0=True,
            )
        )
    )


def content_autocorrelacao() -> str:
    return (
        heading(4, "Autocorrelação Espacial")
        + row(
            p(
                "Lembra da Primeira Lei da Geografia de Tobler: “tudo está relacionado com todo o resto, "
                "mas as coisas mais próximas estão mais relacionadas do que as coisas distantes” que "
                "tratamos na aula 1 deste módulo? Então, o conceito autocorrelação espacial, fundamental "
                "na análise de dados de área, é o termo que descreve a correlação de uma variável com ela "
                "mesma através do espaço."
            )
            + p(
                "Em saúde pública, a autocorrelação espacial significa que o valor de um indicador de saúde "
                "em uma determinada área (por exemplo, um município) não é independente dos valores "
                "nas áreas vizinhas."
            )
        )
        + row(
            '<div class="row g-4">'
            + flipcard(
                "m3a6-auto-pos",
                "Autocorrelação Positiva",
                "<p><strong>Autocorrelação Positiva</strong></p>"
                "<p>Áreas vizinhas tendem a ter valores semelhantes. Municípios com altas taxas de uma "
                "doença estão próximos de outros municípios com altas taxas. Isso sugere a ação de "
                "fatores de risco subjacentes que também estão espacialmente concentrados.</p>",
            )
            + flipcard(
                "m3a6-auto-neg",
                "Autocorrelação Negativa",
                "<p><strong>Autocorrelação Negativa</strong></p>"
                "<p>Áreas vizinhas tendem a ter valores diferentes. Um município com alta taxa está "
                "cercado por municípios com baixas taxas. Este padrão é menos comum em fenômenos "
                "de saúde.</p>",
            )
            + flipcard(
                "m3a6-auto-aus",
                "Ausência de Autocorrelação (Aleatoriedade Espacial)",
                "<p><strong>Ausência de Autocorrelação (Aleatoriedade Espacial)</strong></p>"
                "<p>O valor do indicador em uma área é independente dos valores em seus vizinhos.</p>",
            )
            + "</div>"
        )
    )


def _vizinhanca_desc(texto: str, img: str, alt: str, extra: str = "") -> str:
    extra_html = f'<p class="small mt-2 mb-0">{extra}</p>' if extra else ""
    return (
        f'<p class="mb-3">{texto}</p>'
        f'<figure class="lightbox mb-0">'
        f'<img class="img-fluid mx-auto d-block" src="{MEDIA}{img}" alt="{alt}" loading="lazy" />'
        f"</figure>{extra_html}"
    )


def content_matriz() -> str:
    rows = [
        (
            "Contiguidade (Rainha)",
            _vizinhanca_desc(
                "Duas áreas são vizinhas se compartilharem qualquer porção de sua fronteira "
                "(incluindo apenas um vértice). É o critério mais comum.",
                "vizinhanca-rainha.png",
                "Esquema de contiguidade rainha",
            ),
        ),
        (
            "Contiguidade (Torre)",
            _vizinhanca_desc(
                "Duas áreas são vizinhas apenas se compartilharem um segmento de fronteira "
                "(não apenas um vértice).",
                "vizinhanca-torre.png",
                "Esquema de contiguidade torre",
            ),
        ),
        (
            "Distância",
            _vizinhanca_desc(
                "Duas áreas são vizinhas se a distância entre seus centroides (ou pontos centrais) "
                "for menor que um determinado raio.",
                "vizinhanca-distancia.png",
                "Esquema de vizinhança por distância",
                "Neste exemplo, considerando que os vizinhos são as áreas onde o centroide estão "
                "dentro do raio (R), a área E tem como vizinhos apenas a área F.",
            ),
        ),
        (
            "k-Vizinhos Mais Próximos",
            _vizinhanca_desc(
                "Para cada área, seus vizinhos são as 'k' áreas mais próximas a ela. Exemplo: k=3",
                "vizinhanca-k.png",
                "Esquema de k-vizinhos mais próximos",
            ),
        ),
    ]
    body = "".join(
        f"<tr><td class=\"align-middle\"><strong>{criterio}</strong></td><td>{desc}</td></tr>"
        for criterio, desc in rows
    )
    tabela = (
        '<div class="table-responsive">'
        '<table class="table table-bordered align-middle mb-0">'
        "<thead><tr>"
        '<th scope="col" style="width:28%">Critério</th>'
        '<th scope="col">Descrição</th>'
        "</tr></thead>"
        f"<tbody>{body}</tbody></table></div>"
        '<p class="figure-caption fonte small mt-2 mb-0">Fonte: Elaborado pelos autores (2026)</p>'
    )
    return (
        heading(5, "Matriz de Vizinhança")
        + row(
            p(
                "Para medir a autocorrelação espacial, primeiro precisamos definir formalmente o que "
                "significa “ser vizinho”. Isso é feito através de uma matriz de proximidade espacial ou matriz "
                "de pesos espaciais (W). Esta matriz (n x n, onde n é o número de áreas) especifica a relação "
                "de vizinhança para cada par de áreas (Câmara, et al., 2004)."
            )
            + p("Existem vários critérios para definir a vizinhança:")
            + tabela
        )
        + row(
            p(
                "A escolha da matriz é crucial porque diferentes definições de vizinhança podem produzir "
                "resultados distintos na identificação de padrões espaciais, autocorrelação ou clusters. "
                "Em outras palavras, a maneira como a vizinhança é definida influencia diretamente a "
                "interpretação dos padrões espaciais observados. Por esse motivo, essa decisão não deve ser "
                "arbitrária, mas sim fundamentada nas características do fenômeno estudado e nos processos "
                "que geram a dependência espacial."
            )
            + p(
                "Nas doenças transmitidas por vetores, como a Dengue, a utilização de matrizes baseadas em "
                "contiguidade costuma ser adequada, pois a transmissão tende a ocorrer entre áreas "
                "geograficamente adjacentes. Já em doenças associadas à mobilidade populacional, como a "
                "COVID-19, critérios baseados em distância ou proximidade entre centroides podem "
                "representar melhor as interações espaciais, uma vez que o contágio pode ocorrer entre "
                "regiões conectadas por fluxos de deslocamento. Por outro lado, em estudos de exposição "
                "ambiental, como os que investigam doenças respiratórias relacionadas à poluição do ar, "
                "como a Asma, matrizes baseadas em distância podem ser mais apropriadas, já que os efeitos "
                "ambientais frequentemente ultrapassam limites administrativos.",
                mb0=True,
            )
        )
    )


def content_moran() -> str:
    doi = a("https://doi.org/10.1590/1414-462X201700030015")
    return (
        heading(6, "Medidas Globais de Autocorrelação: Índice de Moran Global (I)")
        + row(
            p(
                "As medidas globais fornecem um único valor que resume o grau de agrupamento espacial "
                "para toda a área de estudo. O indicador mais utilizado é o Índice de Moran Global (I) "
                "(Câmara, et al., 2004; Santos &amp; Souza, 2004)."
            )
            + p("O Índice de Moran varia de -1 a +1:")
            + ul(
                [
                    "I &gt; 0: Indica autocorrelação espacial positiva (tendência à formação de clusters "
                    "de valores similares).",
                    "I &lt; 0: Indica autocorrelação espacial negativa (tendência à formação de clusters "
                    "de valores dissimilares).",
                    "I ≈ 0: Indica ausência de padrão espacial (distribuição aleatória).",
                ]
            )
            + p(
                "Vamos utilizar um estudo sobre a mortalidade por suicídio no Nordeste brasileiro utilizou o "
                "Índice de Moran para avaliar o padrão geral da distribuição dos casos (Santos &amp; Barbosa, "
                f"2017) para embasar nossa discussão: {doi}"
            )
            + p(
                "Neste estudo o índice de Moran Global foi de I=0,2608, o que significa que existe "
                "autocorrelação espacial positiva, isto é, com tendência à formação de clusters de valores "
                "similares. Juntamente com o índice, é calculado um p-valor, que testa a hipótese nula de que "
                "os dados são espacialmente aleatórios. Um p-valor baixo (ex: p &lt; 0,05) nos permite concluir "
                "que existe uma autocorrelação espacial estatisticamente significativa.",
                mb0=True,
            )
        )
    )


def content_lisa() -> str:
    doi = a("https://doi.org/10.1590/1414-462X201700030015")
    return (
        heading(7, "Análise Local: Identificação de Clusters (LISA)")
        + row(
            p(
                "Um índice global como o de Moran pode mascarar padrões locais importantes. "
                "A autocorrelação pode ser forte em uma parte do mapa e fraca em outra. Para superar isso, "
                "utilizamos os Indicadores Locais de Associação Espacial (LISA - Local Indicators of Spatial "
                "Association) (Câmara et.al, 2004; Santos &amp; Souza, 2007)."
            )
            + p(
                "A forma mais comum de LISA é o Índice de Moran Local. Ele calcula um valor de Moran "
                "para cada área individualmente, permitindo identificar a contribuição de cada área para o "
                "padrão global e localizar os clusters."
            )
            + p(
                "A análise LISA classifica as áreas com autocorrelação local significativa em quatro "
                "categorias, que são frequentemente visualizadas em um Mapa de Clusters LISA e no "
                "Diagrama de Espalhamento de Moran:"
            )
        )
        + figure_captioned(
            "figura2-moran-scatter.png",
            "Figura 2 - Diagrama de Espalhamento de Moran (Moran Scatterplot).",
            "Fonte: Elaborado pelos autores (2026).",
        )
        + box_azul(
            "<p>A figura explica visualmente como o Diagrama de Moran separa diferentes tipos "
            "de padrões espaciais:</p>"
            "<p>Clusters Alto-Alto e Baixo-Baixo → valores semelhantes agrupados.</p>"
            "<p>Outliers Alto-Baixo e Baixo-Alto → valores contrastantes posicionados lado a lado.</p>"
            '<p class="mb-0">A inclinação da reta indica grau de dependência espacial do indicador.</p>'
        )
        + row(
            '<p class="mb-2"><strong>Figura 5 - Mapa de Clusters LISA.</strong></p>'
            '<div class="row align-items-start g-4">'
            '<div class="col-12 col-md-7">'
            '<figure class="lightbox mb-0 aos-init" data-aos="fade-up" data-aos-easing="ease-out" data-aos-duration="600">'
            f'<img class="img-fluid mx-auto d-block rounded border" src="{MEDIA}figura-lisa-mapa.png" '
            'alt="Figura 5 - Mapa de Clusters LISA." loading="lazy" />'
            "</figure>"
            "</div>"
            '<div class="col-12 col-md-5">'
            '<div class="border p-3 h-100">'
            "<p>A figura ilustra um cenário típico de análise LISA:</p>"
            "<p><strong>Dois grandes clusters:</strong></p>"
            "<ul>"
            "<li>um de <strong>alto risco</strong> (vermelho)</li>"
            "<li>um de <strong>baixo risco</strong> (azul)</li>"
            "</ul>"
            "<p><strong>Outliers</strong> espalhados (laranja e verde), representando áreas que "
            "contrastam com seus vizinhos.</p>"
            '<p class="mb-0"><strong>A maior parte do mapa é não significativa</strong>, indicando '
            "ausência de padrões espaciais relevantes nessas células.</p>"
            "</div>"
            "</div>"
            "</div>"
            '<p class="figure-caption fonte small mt-3 mb-0">Fonte: Elaborado pelos autores (2026).</p>'
        )
        + row(
            simple_table(
                ["Categoria", "Descrição", "Interpretação em Saúde"],
                [
                    [
                        "Alto-Alto",
                        "Uma área com alto valor do indicador, cercada por vizinhos que também têm "
                        "altos valores.",
                        "Cluster de Risco: Aglomerado de áreas com alta prioridade para intervenção.",
                    ],
                    [
                        "Baixo-Baixo",
                        "Uma área com baixo valor do indicador, cercada por vizinhos que também têm "
                        "baixos valores.",
                        "Cluster de Baixo Risco: Aglomerado de áreas com bons indicadores de saúde.",
                    ],
                    [
                        "Alto-Baixo",
                        "Uma área com alto valor, ercada por vizinhos com baixos valores.",
                        'Outlier Espacial: Uma "ilha" de alto risco em uma "vizinhança" de baixo risco.',
                    ],
                    [
                        "Baixo-Alto",
                        "Uma área com baixo valor, cercada por vizinhos com altos valores.",
                        'Outlier Espacial: Uma "ilha" de baixo risco em uma "vizinhança" de alto risco.',
                    ],
                ],
            )
            + p(
                "Essa técnica é poderosa para a vigilância em saúde, pois permite identificar não apenas os "
                "clusters de risco (Alto-Alto), mas também áreas que podem ter fatores de proteção "
                "(Baixo-Baixo) ou que representam transições abruptas no espaço (Alto-Baixo e Baixo-Alto)."
            )
            + p(
                "Voltando ao estudo sobre mortalidade por suicídio no Nordeste brasileiro trabalhando acima, "
                "temos uma análise de Moran Local com identificação dos clusters das Taxas de Mortalidade "
                "por suicídio, com LISA estatisticamente significativo (MoranMap)."
            )
        )
        + row(
            '<div class="border p-3">'
            '<div class="row align-items-start g-4">'
            '<div class="col-12 col-md-7">'
            '<figure class="lightbox mb-0 aos-init" data-aos="fade-up" data-aos-easing="ease-out" data-aos-duration="600">'
            f'<img class="img-fluid mx-auto d-block" src="{MEDIA}mapa-suicidio-lisa.png" '
            'alt="Mapa LISA de mortalidade por suicídio no Nordeste" loading="lazy" />'
            "</figure>"
            "</div>"
            '<div class="col-12 col-md-5">'
            '<div class="border p-3 h-100">'
            '<p class="mb-0">No mapa podemos observar verifica-se a presença de um aglomerado de alta taxa '
            "de mortalidade por suicídio entre os municípios dos Estados do Ceará e Piauí (municípios "
            "coloridos de preto).</p>"
            "</div>"
            "</div>"
            "</div>"
            "</div>"
            f'<p class="figure-caption fonte small mt-3 mb-0">Fonte: Cadernos de Saúde Coletiva. Disponível em: {doi}</p>'
        )
        + row(
            p(
                "Outros estudos recentes no Brasil têm usado LISA para identificar clusters de mortalidade "
                "infantil (Dilélio, et.al, 2024) e para analisar a distribuição espacial do câncer de boca e sua "
                "relação com determinantes de saúde (Marsicano et al., 2025).",
                mb0=True,
            )
        )
    )


def content_instabilidade() -> str:
    return (
        heading(8, "Instabilidade de Taxas")
        + row(
            p(
                "Um dos maiores desafios ao trabalhar com dados de área, especialmente quando as áreas "
                "são pequenas (como bairros ou setores censitários), é o problema dos pequenos números, "
                "que leva à instabilidade das taxas (Carvalho &amp;Souza-Santos, 2005; Câmara et al., 2004)."
            )
        )
        + importante_toggle(
            "m3a6-importante-taxas",
            "<p class=\"mb-0\">Áreas com populações pequenas podem apresentar taxas de mortalidade ou "
            "incidência extremamente altas ou baixas devido ao acaso. Por exemplo, em um "
            "bairro com apenas 10 nascimentos em um ano, um único óbito infantil resultaria "
            "em uma taxa altíssima (100 por mil), enquanto a ausência de óbitos resultaria "
            "em uma taxa de zero. Esses valores extremos muitas vezes não refletem o risco "
            "real, mas sim a flutuação aleatória.</p>",
        )
        + row(
            p("<strong>Tabela 1: Taxa de Mortalidade de municípios</strong>")
            + simple_table(
                ["Município (fictício)", "População", "Nº de óbitos", "Tx. Mortalidade"],
                [
                    ["Lirandópolis", "4.565", "1", "4,4"],
                    ["Taguarana", "30.113", "1", "0,7"],
                    ["Iraporé", "9.797", "2", "4,1"],
                    ["Vargem Serena", "49.038", "2", "0,8"],
                    ["Serra do Cedro", "18.854", "11", "11,7"],
                    ["Campos do Jatobá", "130.154", "11", "1,7"],
                ],
                note="Nota: Os nomes acima são fictícios e usados apenas para fins didáticos.",
            )
            + p(
                "Observando os dados da tabela, verificamos que os municípios de Lirandópolis e "
                "Taguarana tiveram o mesmo número de óbitos, mas como a população do primeiro é "
                "pequena, a taxa acaba sendo alta. A mesma coisa acontece para os municípios de Serra "
                "de cedro e Campos do Jatobá, ambos tiveram 11 óbitos, mas por causa da população "
                "as taxas são bem diferentes."
            )
            + p(
                "Ignorar esse problema pode levar a uma alocação inadequada de recursos, direcionando a "
                "atenção para áreas que parecem ter um problema grave, mas que na verdade são apenas "
                "estatisticamente instáveis. A solução para isso é a suavização de taxas, sendo o método "
                "mais comum o Estimador Bayesiano Empírico (Carvalho &amp;Souza-Santos, 2005; "
                "Câmara et al., 2004)."
            )
            + p(
                "A ideia do estimador bayesiano é “corrigir” a taxa observada em uma área, levando em "
                "consideração sua própria estabilidade (ou seja, o tamanho de sua população) e a informação "
                "de seus vizinhos. A taxa suavizada é uma média ponderada entre a taxa observada na área "
                "e uma taxa de referência (que pode ser a média global ou a média dos vizinhos). "
                "O peso dado à taxa observada é proporcional ao tamanho da população da área. Assim:"
            )
        )
        + accordion(
            "m3a6-areas",
            [
                (
                    "Áreas populosas:",
                    "<p class=\"mb-0\">Têm taxas estáveis. O estimador dá muito peso à taxa observada, e o valor "
                    "suavizado será muito próximo do original.</p>",
                ),
                (
                    "Áreas pouco populosas:",
                    "<p class=\"mb-0\">Têm taxas instáveis. O estimador dá pouco peso à taxa observada e “puxa” "
                    "o valor em direção à média de referência, resultando em uma estimativa de risco "
                    "mais robusta e confiável.</p>",
                ),
            ],
        )
        + figure_captioned(
            "figura5-suavizacao.png",
            "Figura 5 - Efeito da Suavização Bayesiana na Instabilidade de Taxas.",
            "Fonte: Elaborado pelos autores (2026).",
        )
        + box_azul(
            "<p>A figura mostra dois gráficos de barras, cada um representando diferentes formas "
            "de calcular taxas de mortalidade em municípios fictícios (tabela 1).</p>"
            "<p>No gráfico da esquerda (A) que mostra as taxas brutas, a distribuição é dispersa e "
            "irregular. As diferenças entre municípios refletem a instabilidade das taxas, "
            "especialmente em locais com pouca população.</p>"
            "<p>No gráfico da direita (B) apresenta as taxas suavizadas, calculadas por método "
            "bayesiano empírico. São os mesmos seis municípios, com cores seguindo a mesma "
            "lógica do painel A.</p>"
            "<p>Observamos claramente:</p>"
            "<ul>"
            "<li>Como taxas brutas podem ser instáveis, principalmente em municípios com "
            "pouca população.</li>"
            "<li>Como a suavização bayesiana reduz essa instabilidade, gerando valores mais "
            "coerentes e menos dependentes de flutuações aleatórias.</li>"
            "</ul>"
        )
        + row(
            p(
                "Nos mapas abaixo, retirado de um artigo sobre hanseníase em Recife, o método foi utilizado "
                "para corrigir as taxas permitindo uma identificação mais precisa dos bairros prioritários para a "
                "vigilância (Souza, et.al, 2001; Carvalho e Souza-Santos, 2005)."
            )
        )
        + figure_captioned(
            "figura6-hansenias.png",
            "Figura 6: Mapa com as taxas brutas e alisadas de hanseníase. Recife, 1993 – 1997.",
            "Fonte: Souza et al., 2001.",
        )
        + row(
            p(
                "Observando os mapas pode-se observar que após a suavização, os mapas tornaram-se "
                "menos fragmentados, evidenciando bolsões/áreas com maior gravidade para a ocorrência "
                "da doença. O modelo bayesiano, usando a vizinhança por adjacência, permitiu reestimar os "
                "indicadores epidemiológicos por bairro, suavizando as taxas, reduzindo a flutuação aleatória "
                "dos valores e revelando padrões reais (inclusive sugerindo sub-registro) e orientou a "
                "priorização territorial das ações de controle.",
                mb0=True,
            )
        )
    )


def content_referencias() -> str:
    items = "".join(f'<p class="referencias-item">{ref}</p>' for ref in REFERENCES)
    return heading(9, "Referências") + row(f'<div class="referencias-aula">{items}</div>')


CONTENT_BUILDERS = [
    content_sobre,
    content_introducao,
    content_dados_area,
    content_autocorrelacao,
    content_matriz,
    content_moran,
    content_lisa,
    content_instabilidade,
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
