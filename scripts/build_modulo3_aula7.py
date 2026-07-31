#!/usr/bin/env python3
"""Gera HTML da Aula 3.7 (Análise Espacial de Dados – Pontos)."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "modulo3" / "aula7"
MEDIA = "../../media/modulo3/aula7/"
ASSETS = "../../"

COURSE_TITLE = "Análise e Interpretação de Dados em Saúde"
MODULE_NUM = 3
MODULE_TITLE = "Análise Espacial"
AULA_LABEL = "Aula 7"
AULA_TITLE = "Análise Espacial de Dados – Pontos"

TOPICS = [
    "Sobre esta aula",
    "Introdução à Análise de Padrões Pontuais",
    "O que são Dados Pontuais?",
    "Padrões Espaciais Básicos",
    "Mapas de Calor (KDE)",
    "Diferença entre Intensidade e Risco",
    "Clusters Espaciais",
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

AEDE_POPOVER = (
    "Análise exploratória de dados espaciais é um conjunto de técnicas para "
    "visualizar, descrever e identificar padrões, clusters (agrupamentos) e "
    "anomalias (outliers) em dados geográficos."
)

REFERENCES = [
    "CARVALHO, M. S.; SOUZA-SANTOS, R. Análise de dados espaciais em saúde pública: "
    "métodos, problemas, perspectivas. <em>Cadernos de Saúde Pública</em>, v. 21, n. 2, "
    "p. 361‑378, 2005.",
    "CÂMARA, G.; CARVALHO, M. S. Análise espacial de eventos. In: DRUCK, S.; CARVALHO, M. S.; "
    "CÂMARA, G.; MONTEIRO, A. V. M. (org.). <em>Análise espacial de dados geográficos</em>. "
    "Brasília: EMBRAPA, 2004.",
    "SANTOS, S. M.; SOUZA, W. V. (org.). <em>Introdução à estatística espacial para a saúde "
    "pública</em>. Brasília: Ministério da Saúde/Fiocruz, 2007.",
    "CARNEIRO, D. D.; Bavia M. E.; Rocha, W. J.; Tavares, A.C.; Cardim, L.L.; Alemayehu, B. "
    "Application of spatio-temporal scan statistics for the detection of areas with increased "
    "risk for American visceral leishmaniasis in the state of Bahia, Brazil. "
    "<em>Geospatial Health</em>, v. 2, n. 1, p. 115‑127, 2007.",
    "KULLDORFF, M. SaTScan™ software for spatial, temporal and space-time scan statistics: "
    "User guide. [S.l.: s.n.], 2024. Disponível em: "
    '<a href="https://www.satscan.org" target="_blank" rel="noopener noreferrer">'
    "https://www.satscan.org</a>. Acesso em: 10 mar. 2026.",
    "MELO, A. C. O.; MELO, J. C. S.; MORAES, R. Epidemiologia espacial e a detecção de "
    "aglomerados espaciais do dengue na Paraíba: uma comparação entre os métodos Scan "
    "flexível e Scan circular. <em>Cadernos Saúde Coletiva</em>, v. 30, n. 1, p. 69‑79, 2022. "
    "Disponível em: "
    '<a href="https://www.scielo.br/j/cadsc/a/HGjB9yBPzHSxL5XLGngmNGB/?lang=pt" '
    'target="_blank" rel="noopener noreferrer">'
    "https://www.scielo.br/j/cadsc/a/HGjB9yBPzHSxL5XLGngmNGB/?lang=pt</a>.",
    "YAMAMURA, M.; FREITAS, I. M.; SANTO NETO, M.; CHIARAVALLOTI NETO, F. Análise "
    "espacial das internações evitáveis por tuberculose em Ribeirão Preto, SP (2006‑2012). "
    "<em>Revista de Saúde Pública</em>, v. 50, p. 20, 2016. Disponível em: "
    '<a href="https://www.scielo.br/j/rsp/a/St4S8zXDjKwP7gsrC89x8Rx/?format=pdf&amp;lang=pt" '
    'target="_blank" rel="noopener noreferrer">'
    "https://www.scielo.br/j/rsp/a/St4S8zXDjKwP7gsrC89x8Rx/?format=pdf&amp;lang=pt</a>.",
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


def importante_toggle(collapse_id: str, body_html: str) -> str:
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


def simple_table(headers: list[str], rows: list[list[str]]) -> str:
    th = "".join(f'<th scope="col">{h}</th>' for h in headers)
    body = ""
    for r in rows:
        tds = "".join(f"<td>{c}</td>" for c in r)
        body += f"<tr>{tds}</tr>"
    return (
        '<div class="table-responsive"><table class="table table-sm table-bordered align-middle mb-0">'
        f"<thead><tr>{th}</tr></thead><tbody>{body}</tbody></table></div>"
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


def figure_with_side_text(
    src: str,
    caption: str,
    fonte: str,
    side_html: str,
    *,
    alt: str = "",
    outer_border: bool = False,
) -> str:
    wrap_open = '<div class="border p-3">' if outer_border else ""
    wrap_close = "</div>" if outer_border else ""
    return row(
        f'<p class="mb-2"><strong>{caption}</strong></p>'
        f"{wrap_open}"
        '<div class="row align-items-start g-4">'
        '<div class="col-12 col-md-7">'
        '<figure class="lightbox mb-0 aos-init" data-aos="fade-up" data-aos-easing="ease-out" data-aos-duration="600">'
        f'<img class="img-fluid mx-auto d-block rounded border" src="{MEDIA}{src}" alt="{alt or caption}" loading="lazy" />'
        "</figure>"
        "</div>"
        '<div class="col-12 col-md-5">'
        f'<div class="border p-3 h-100">{side_html}</div>'
        "</div>"
        "</div>"
        f"{wrap_close}"
        f'<p class="figure-caption fonte small mt-3 mb-0">{fonte}</p>'
    )


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
            p('Seja bem-vindo e bem-vinda à aula “Análise Espacial de Dados – Pontos”.')
            + p("A seguir, veja algumas informações importantes!")
        )
        + subheading("Objetivos de aprendizagem")
        + row(
            p("Ao final dessa aula, você será capaz de:")
            + ul(
                [
                    "Compreender os conceitos básicos da análise espacial de dados pontuais;",
                    "Identificar padrões espaciais (regular, aleatório e aglomerado);",
                    "Compreender o princípio do Estimador de Densidade de Kernel (KDE);",
                    "Diferenciar os conceitos de intensidade e risco em representações espaciais;",
                    "Entender a lógica de detecção de clusters por estatística de varredura.",
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
    return (
        heading(2, "Introdução à Análise de Padrões Pontuais em Saúde")
        + row(
            p(
                "Na última aula, exploramos os fundamentos da análise de dados organizados por áreas "
                "geográficas, utilizando informações agregadas em polígonos territoriais, como municípios, "
                "bairros, setores censitários ou estados. Nesta aula, avançamos para outro tipo de "
                "abordagem bastante utilizado na saúde pública: a análise espacial de dados pontuais. "
                "Esse método é essencial para compreender a distribuição geográfica de doenças e outros "
                "eventos de saúde."
            )
            + p(
                "Um processo pontual corresponde a um conjunto de ocorrências localizadas no espaço, por "
                "exemplo, a residência de indivíduos com determinada doença, a localização de óbitos ou "
                "mesmo a ocorrência de crimes (Carvalho &amp; Souza-Santos, 2005; Câmara, 2004). O objetivo "
                "central desse tipo de análise é ir além da simples listagem de casos e investigar se o padrão "
                "espacial observado é aleatório, se os eventos tendem a se concentrar em determinadas "
                "áreas ou se apresentam uma distribuição mais regular do que o esperado (Câmara, 2004)."
            )
            + p(
                "Essa abordagem permite identificar padrões espaciais e apoiar a tomada de decisões e é "
                "especialmente útil para:"
            )
        )
        + row(
            '<div class="row g-4">'
            + flipcard(
                "m3a7-clusters",
                "Identificar clusters de doenças",
                "<p><strong>Identificar clusters de doenças</strong></p>"
                "<p>Identificação de áreas onde há concentração anormal de casos de uma doença. "
                "Por meio do mapeamento dos endereços ou coordenadas dos pacientes, é possível "
                "verificar se os casos estão distribuídos aleatoriamente ou se se concentram em "
                "determinadas regiões. Por exemplo, estudos sobre Dengue frequentemente mostram "
                "clusters em bairros com maior presença do mosquito vetor, permitindo que as "
                "autoridades sanitárias direcionem ações de controle nesses locais.</p>",
            )
            + flipcard(
                "m3a7-surtos",
                "Detectar surtos",
                "<p><strong>Detectar surtos</strong></p>"
                "<p>Permite detectar rapidamente possíveis surtos ao observar aumentos localizados no "
                "número de casos. Quando vários registros de uma mesma doença aparecem próximos "
                "espacialmente e em curto período de tempo, isso pode indicar um foco de transmissão ativo. "
                "Durante a pandemia de COVID-19, mapas com dados georreferenciados foram "
                "utilizados para acompanhar a expansão da doença e identificar regiões com crescimento "
                "acelerado de casos, permitindo a adoção de medidas específicas de controle.</p>",
            )
            + flipcard(
                "m3a7-servicos",
                "Planejar serviços de saúde",
                "<p><strong>Planejar serviços de saúde</strong></p>"
                "<p>Ao analisar a localização da população, dos casos de doenças e das unidades de "
                "atendimento, é possível identificar áreas com baixa cobertura ou difícil acesso aos serviços. "
                "No Brasil, esse tipo de análise auxilia o planejamento do Sistema Único de Saúde, "
                "contribuindo para definir onde instalar novas unidades básicas de saúde ou reforçar "
                "a oferta de atendimento.</p>",
            )
            + flipcard(
                "m3a7-ambiente",
                "Estudar fatores ambientais",
                "<p><strong>Estudar fatores ambientais</strong></p>"
                "<p>Permite investigar a relação entre doenças e fatores ambientais. Ao sobrepor a localização "
                "dos casos com variáveis como poluição, condições climáticas ou características do "
                "território, estudos conseguem identificar possíveis associações. Por exemplo, estudos "
                "podem relacionar a ocorrência de Asma com áreas de maior poluição do ar, ou casos de "
                "Malária com regiões próximas a corpos d’água que favorecem a proliferação de mosquitos.</p>",
            )
            + flipcard(
                "m3a7-vigilancia",
                "Melhorar a vigilância epidemiológica",
                "<p><strong>Melhorar a vigilância epidemiológica</strong></p>"
                "<p>Permite o monitoramento contínuo da distribuição das doenças no território. "
                "A partir do registro georreferenciado dos casos, é possível acompanhar tendências, "
                "identificar áreas prioritárias e planejar intervenções de prevenção e controle. Um exemplo é "
                "o monitoramento de casos de Febre Amarela para definir regiões onde campanhas de "
                "vacinação devem ser intensificadas.</p>",
            )
            + "</div>"
        )
        + row(
            p(
                "Assim, a análise espacial de dados pontuais contribui significativamente para a "
                "compreensão da dinâmica das doenças e para o desenvolvimento de políticas públicas "
                "mais eficientes, orientadas pelas características geográficas e sociais de cada região",
                mb0=True,
            )
        )
    )


def content_dados_pontuais() -> str:
    return (
        heading(3, "O que são Dados Pontuais?")
        + row(
            p(
                "Dados pontuais em saúde referem-se a eventos cuja localização geográfica pode ser "
                "representada por uma coordenada (latitude e longitude) em um mapa, entretanto a origem "
                "da localização pode ser o endereço do evento. Um aspecto fundamental é que, nessa "
                "abordagem, a área física do evento não é o elemento principal da análise. O interesse está "
                "na posição espacial do evento dentro do espaço de estudo (Câmara, 2004)."
            )
            + p(
                "Em epidemiologia, um exemplo clássico é a representação da residência de casos de uma "
                "doença. Outros exemplos incluem a localização de nascimentos, óbitos, ou a ocorrência "
                "de acidentes. Mesmo em estudos de cidades, estas podem ser consideradas como um ponto "
                "no espaço, dependendo da escala da análise (Câmara, 2004)."
            )
            + p("Os dados de distribuições pontuais possuem duas características principais:")
        )
        + accordion(
            "m3a7-caracteristicas",
            [
                (
                    "Localização:",
                    "<p class=\"mb-0\">A informação primária é a coordenada geográfica de cada evento.</p>",
                ),
                (
                    "Atributos (Opcional):",
                    "<p class=\"mb-0\">Frequentemente, os pontos estão associados a atributos adicionais. Por exemplo, "
                    "um ponto representando um caso de tuberculose pode ter atributos como idade do "
                    "paciente, sexo, data de diagnóstico e desfecho do tratamento. Quando os pontos "
                    "possuem esses atributos, o processo é denominado processo pontual marcado [2].</p>",
                ),
            ],
        )
    )


def content_padroes() -> str:
    return (
        heading(4, "Padrões Espaciais Básicos")
        + row(
            p(
                "O primeiro passo na análise de um conjunto de dados pontuais é determinar se os eventos "
                "observados seguem algum padrão sistemático, em oposição a uma distribuição puramente "
                "aleatória. Existem três padrões teóricos básicos:"
            )
        )
        + figure_captioned(
            "figura1-padroes-espaciais.png",
            "Figura 1: Padrão de espacialização de eventos no território.",
            "Fonte: Elaborado pelos autores (2026).",
        )
        + row(
            simple_table(
                ["Padrão", "Descrição", "Exemplo em Saúde Pública"],
                [
                    [
                        "Regular (Disperso)",
                        "Os eventos estão mais uniformemente espaçados do que seria esperado "
                        "pelo acaso. A presença de um ponto diminui a probabilidade de encontrar "
                        "outros pontos nas proximidades.",
                        "É um padrão raro em epidemiologia, mas poderia teoricamente ocorrer em "
                        "cenários de competição por recursos ou em processos de exclusão, como a "
                        "distribuição de unidades de saúde que seguem uma lógica de distanciamento mínimo.",
                    ],
                    [
                        "Aleatório (Random)",
                        "A posição de um evento não tem qualquer influência sobre a posição "
                        "de outro. Este padrão serve como uma hipótese nula (ausência de padrão) "
                        "em muitos testes estatísticos.",
                        "A distribuição de uma doença não infecciosa rara, sem fatores de risco "
                        "geográficos conhecidos.",
                    ],
                    [
                        "Aglomerado (Clustered)",
                        "Os eventos estão mais próximos uns dos outros do que seria esperado "
                        "pelo acaso. A presença de um ponto aumenta a probabilidade de "
                        "encontrar outros pontos nas proximidades.",
                        "Um surto de doença infecciosa em um bairro específico; casos de câncer "
                        "próximos a uma fonte de poluição ambiental.",
                    ],
                ],
            )
        )
        + row(
            p(
                "O modelo de referência para um padrão aleatório é o de Completa Aleatoriedade "
                "Espacial (CSR - Complete Spatial Randomness). Sob o CSR, qualquer ponto tem a mesma "
                "probabilidade de ocorrer em qualquer lugar dentro da área de estudo, e a posição de um "
                "ponto é independente dos outros (Câmara, 2004). A maioria das técnicas de análise de "
                "padrões pontuais visa testar se os dados observados se desviam significativamente deste "
                "modelo de aleatoriedade."
            )
            + p(
                "Apesar de suas vantagens analíticas, o uso de dados pontuais em saúde exige cuidados "
                "importantes, especialmente relacionados à privacidade e confidencialidade dos indivíduos, "
                "já que a localização exata pode permitir a identificação indireta de pessoas. Por isso, em "
                "muitos estudos, as coordenadas são deslocadas, agregadas ou anonimizadas antes da "
                "divulgação dos resultados.",
                mb0=True,
            )
        )
    )


def content_kde() -> str:
    aede = popover_link("AEDE", "AEDE", AEDE_POPOVER)
    scielo = a(
        "https://www.scielo.br/j/rsp/a/St4S8zXDjKwP7gsrC89x8Rx/?format=pdf&lang=pt"
    )
    return (
        heading(5, "Mapas de Calor (Estimador de Densidade de Kernel)")
        + row(
            p(
                "Uma das técnicas mais populares e visualmente intuitivas para analisar padrões pontuais "
                "é a criação de mapas de calor, tecnicamente conhecida como Estimador de Densidade "
                "de Kernel (Kernel Density Estimation - KDE). Este método permite estimar a intensidade "
                "do processo em toda a área de estudo, gerando uma superfície contínua que representa a "
                f"densidade de eventos (Carvalho &amp; Souza-Santos, 2005; Santos et al., 2007). É bastante "
                f"utilizado na análise exploratória de dados espaciais ({aede})."
            )
        )
        + figure_captioned(
            "figura2-mapa-pontos-kernel.png",
            "Figura 2 - Do Mapa de Pontos ao Mapa de Calor (Kernel).",
            "Fonte: Elaborado pelos autores (2026).",
        )
        + box_azul(
            "<p class=\"mb-0\">A figura compara um mapa de pontos com um mapa de calor gerado por Kernel. "
            "No mapa de pontos, cada caso aparece como um ponto vermelho, mas a visualização "
            "fica dispersa e dificulta perceber padrões. Já o mapa de calor utiliza o estimador "
            "de densidade de Kernel para suavizar os pontos e destacar áreas com maior "
            "concentração de eventos: cores quentes indicam alta densidade e cores frias, "
            "baixa densidade. Essa técnica evidencia agrupamentos (hotspots) e facilita a "
            "interpretação espacial, revelando padrões que não são facilmente identificáveis "
            "no mapa de pontos.</p>"
        )
        + row(
            p(
                "O KDE funciona posicionando uma função tridimensional (o kernel) sobre cada ponto "
                "do mapa. A função atribui o maior valor ao local exato do ponto, com valores decrescentes "
                "à medida que a distância do ponto aumenta, até chegar a zero em um raio de influência (τ) "
                "definido. A superfície de densidade final é a soma de todas as funções de kernel individuais. "
                "O resultado é um mapa de gradientes de cor, onde as áreas “mais quentes” (geralmente em "
                "vermelho) representam maior concentração de eventos (Câmara, 2004, Santos et al., 2007)."
            )
            + p("Observando a figura, ficará mais fácil compreender:")
        )
        + figure_captioned(
            "figura3-funcionamento-kde.png",
            "Figura 3 - Como Funciona o Estimador de Densidade de Kernel (KDE).",
            "Fonte: Elaborado pelos autores (2026).",
        )
        + row(
            p(
                "A figura mostra o funcionamento do Estimador de Densidade de Kernel (KDE) ao "
                "transformar eventos pontuais em uma curva contínua de densidade. Cada ponto preto "
                "representa um evento no espaço, sobre o qual é aplicada uma função kernel — as curvas "
                "suaves tracejadas — que distribui sua influência ao redor. O raio (τ) determina até onde "
                "essa influência se estende. A soma dessas funções gera a curva azul, que representa a "
                "densidade estimada: quanto maior a sobreposição das curvas individuais, maior a densidade "
                "naquele local. Assim, o KDE converte pontos isolados em uma superfície contínua que "
                "facilita visualizar concentrações e identificar áreas com maior ocorrência de eventos."
            )
        )
        + importante_toggle(
            "m3a7-importante-kernel",
            "<p class=\"mb-0\">A aplicação do estimador de Kernel é uma alternativa para analisar o "
            "comportamento de padrões de pontos e estimar a intensidade pontual do "
            "processo em toda a região de estudo. Para isto, pode-se ajustar uma função "
            "bidimensional sobre os eventos considerados, compondo uma superfície cujo valor "
            "será proporcional à intensidade de amostras por unidade de área (Câmara, 2004).</p>",
        )
        + row(
            p(
                "É muito usada em estudos de saúde para identificar concentrações espaciais de eventos de "
                "saúde. Ela transforma pontos, como casos, óbitos, focos etc., em um mapa de densidade, "
                "revelando as áreas com maior intensidade do evento estudado, chamado de hotspots "
                "ou áreas quentes. Foi utilizada, por exemplo, para descrever a distribuição espacial de "
                "internações evitáveis por tuberculose em Ribeirão Preto-SP, ajudando a identificar áreas "
                f"com maior concentração de casos que demandavam atenção prioritária (Yamamura, 2016). "
                f"Acesse em: {scielo}"
            )
        )
        + figure_captioned(
            "figura-kernel-tuberculose.png",
            "Figura 1. Mapa de Kernel das internações evitáveis por tuberculose. Ribeirão Preto, SP, "
            "Brasil, 2006-2012.",
            f"Fonte: {scielo}",
        )
        + row(
            p(
                "Neste estudo, os mapas gerados com a aplicação da técnica de Kernel mostram os locais "
                "com maior densidade de casos por quilômetro quadrado (km²) representados em vermelho. "
                "Observa-se distribuição heterogênea, com a formação de dois possíveis grandes "
                "aglomerados, concentrados principalmente nas zonas oeste e norte do município. "
                "Áreas sem ocorrência de internações foram predominantes na zona sul do município.",
                mb0=True,
            )
        )
    )


def content_intensidade_risco() -> str:
    return (
        heading(6, "Diferença entre Intensidade e Risco")
        + row(
            p(
                "É fundamental distinguir os conceitos de intensidade e risco, embora ambos possam ser "
                "visualizados em mapas. Como aponta Carvalho (2005), a análise de risco pode ser mais "
                "complexa, envolvendo a modelagem simultânea de aspectos individuais e socioambientais, "
                "tratando o espaço como uma superfície contínua, como em um desenho de caso-controle "
                "onde as coordenadas geográficas são analisadas."
            )
        )
        + row(
            '<div class="row g-4">'
            + flipcard(
                "m3a7-intensidade",
                "Intensidade",
                "<p><strong>Intensidade</strong></p>"
                "<p>Refere-se à contagem de eventos por unidade de área. Um mapa de calor (KDE) "
                "é um mapa de intensidade. Ele mostra onde os eventos estão espacialmente concentrados. "
                "No entanto, um mapa de alta intensidade pode simplesmente refletir uma área com "
                "alta densidade populacional. Se há mais pessoas vivendo em uma área, é natural "
                "que haja mais eventos de saúde ali, mesmo que o risco individual não seja maior.</p>",
            )
            + flipcard(
                "m3a7-risco",
                "Risco",
                "<p><strong>Risco</strong></p>"
                "<p>Refere-se à probabilidade de um indivíduo sofrer um determinado evento. Para estimar "
                "o risco, a contagem de casos (numerador) deve ser dividida pela população sob risco "
                "(denominador). Um mapa de risco, portanto, mostra a probabilidade de ocorrência "
                "do evento, ajustada pela distribuição da população. Uma área pode ter baixa "
                "intensidade (poucos casos), mas um risco muito alto se a população residente "
                "for muito pequena.</p>",
            )
            + "</div>"
        )
        + figure_captioned(
            "figura4-intensidade-vs-risco.png",
            "Figura 4 - Intensidade vs. Risco: Por que a distinção importa?",
            "Fonte: Elaborado pelos autores (2026).",
        )
        + box_azul(
            "<p class=\"mb-0\">Na figura, a Região A aparece com mais casos no mapa de intensidade, sugerindo "
            "maior gravidade. No entanto, ao observar o mapa de risco, percebe-se que a "
            "Região B é mais preocupante proporcionalmente, pois possui menos habitantes e, "
            "ainda assim, apresenta alta incidência.</p>"
        )
    )


def content_clusters() -> str:
    scielo = a("https://www.scielo.br/j/cadsc/a/HGjB9yBPzHSxL5XLGngmNGB/?lang=pt")
    return (
        heading(7, "Clusters Espaciais")
        + row(
            p(
                "Um cluster espacial é um aglomerado de eventos em uma área geográfica que é maior "
                "do que o esperado pelo acaso. A detecção de clusters é um dos principais objetivos da "
                "análise espacial em epidemiologia. Existem diferentes métodos para identificar clusters, "
                "sendo um dos mais conhecidos a estatística de varredura espacial (scan statistic), "
                "implementada em softwares como o SaTScan™ (Carneiro et al., 2007)"
            )
            + p(
                "Nesta aula, não buscamos nos aprofundar na técnica nem no uso de softwares "
                "específicos, mas sim apresentar seu funcionamento e ilustrá-la com um exemplo prático."
            )
        )
        + figure_captioned(
            "figura5-scan-statistic.png",
            "Figura 5 - Estatística de varredura espacial (Scan Statistic) para detecção de clusters.",
            "Fonte: Elaborado pelos autores (2026).",
        )
        + row(
            p(
                "A figura demonstra o uso da estatística de varredura espacial (Scan Statistic) para identificar "
                "clusters. Os pontos vermelhos indicam casos dentro de um cluster significativo, destacado "
                "pelo círculo vermelho (p &lt; 0,05), onde há concentração de eventos maior que o esperado "
                "ao acaso. Os círculos tracejados cinza representam janelas testadas sem significância "
                "estatística. Assim, a imagem mostra como o método varre o espaço com diferentes janelas "
                "e identifica apenas as regiões com evidência real de agrupamento espacial."
            )
        )
        + figure_with_side_text(
            "figura5b-esquema-scan.png",
            "Figura 5: Esquema de varredura scan",
            "Fonte: KULLDORFF, M. SaTScan™ software for spatial, temporal and space-time scan statistics",
            "<p class=\"mb-0\">Esta figura mostra a estatística scan que se baseia em um "
            "algoritmo que percorre a área de estudo como um cilindro, "
            "com variados tamanhos, que se move no espaço (base do "
            "cilindro) e no tempo (altura do cilindro) em busca de áreas "
            "cuja ocorrência de um fenômeno seja significativamente "
            "mais provável.</p>",
        )
        + row(
            p(
                "Este método funciona “varrendo” a área de estudo com janelas de diferentes tamanhos "
                "(geralmente circulares). Para cada janela, o software compara o número de casos "
                "observados dentro dela com o número de casos que seria esperado se a distribuição fosse "
                "aleatória. Quando uma janela apresenta um excesso de casos estatisticamente significativo, "
                "ela é identificada como um cluster (Carneiro et al., 2007, Melo et al., 2023)."
            )
            + p(
                "Essa abordagem tem sido amplamente utilizada no Brasil para investigar a distribuição de "
                "diversas doenças, como a detecção de clusters de dengue na Paraíba (Melo et al., 2023). "
                f"Acesse em: {scielo}"
            )
        )
        + figure_with_side_text(
            "figura6-rie-dengue.png",
            "Figura 6: Mapas da Razão de Incidências Espacial (RIE) do dengue na Paraíba, "
            "Scan flex e Scan circular para 2013.",
            "Fonte: Melo et al. 2022. Cadernos Saúde Coletiva, v. 30, n. 1, p. 69‑79",
            "<p class=\"mb-0\">Os mapas revelam que o maior número de "
            "municípios que possuem risco elevado em 2013 "
            "encontra-se ao oeste, havendo uma pequena "
            "concentração na parte central do estado. As "
            "regiões do extremo leste e centro-sul possuem "
            "incidência relativamente baixa em comparação com "
            "as demais áreas do mapa.</p>",
        )
        + row(
            p(
                "A identificação desses clusters permite uma alocação mais precisa de recursos e "
                "a investigação de fatores de risco locais que possam estar contribuindo para a "
                "concentração de casos.",
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
    content_dados_pontuais,
    content_padroes,
    content_kde,
    content_intensidade_risco,
    content_clusters,
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
