#!/usr/bin/env python3
"""Gera HTML da Aula 1.1 (Análise exploratória e descritiva) a partir do PDF validado — sem alterar textos."""
from __future__ import annotations

from pathlib import Path

from modulo1_aula1_charts import (
    C_CONTROLADA,
    C_NAO_CONTROLADA,
    C_PIE_1,
    C_PIE_2,
    C_PIE_3,
    SINASC_SERIES,
    SINASC_YEARS,
    bar_chart_horizontal,
    bar_chart_vertical,
    cross_table,
    grouped_bar_chart,
    histogram_chart,
    imc_histogram_bins,
    line_chart_multi,
    pie_chart,
    scatter_chart,
    scatter_points_from_imc,
)

ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "modulo1" / "aula1"
MEDIA = "../../media/modulo1/aula1/"
ASSETS = "../../"

COURSE_TITLE = "Análise e Interpretação de Dados em Saúde"
MODULE_NUM = 1
MODULE_TITLE = "Estatística"
AULA_LABEL = "Aula 1"
AULA_TITLE = "Análise exploratória e descritiva"

TOPICS = [
    "Sobre esta aula",
    "Introdução",
    "Tabelas",
    "Gráficos",
    "Referências",
]

FONTE_FICTICIA = (
    "Fonte: Dados fictícios gerados por Inteligência Artificial (Google Gemini), em julho de 2026."
)

IMC_VALORES = (
    "19,82", "20,45", "21,95", "22,74", "23,44", "23,88", "24,12", "24,89", "25,11", "25,63",
    "26,08", "26,37", "27,58", "27,94", "28,19", "28,41", "28,94", "29,18", "29,85", "29,93",
    "30,05", "30,51", "31,25", "31,45", "31,74", "32,16", "32,61", "33,08", "33,25", "33,76",
    "34,02", "34,67", "35,41", "35,62", "36,22", "36,89", "37,54", "38,91", "39,45", "40,13",
)


def table_captioned(caption: str, fonte: str, table_html: str) -> str:
    return row(
        f'<p class="mb-2"><strong>{caption}</strong></p>'
        f'<div class="table-responsive aos-init" data-aos="fade-up" data-aos-easing="ease-out" data-aos-duration="600">'
        f"{table_html}"
        f"</div>"
        f'<p class="figure-caption fonte small mb-0">{fonte}</p>'
    )


def freq_table(headers: list[str], rows: list[list[str]], total: list[str]) -> str:
    thead = "".join(f'<th scope="col">{h}</th>' for h in headers)
    tbody = ""
    for r in rows:
        cells = []
        for i, val in enumerate(r):
            align = ' class="text-end"' if i > 0 else ""
            cells.append(f"<td{align}>{val}</td>")
        tbody += f"<tr>{''.join(cells)}</tr>"
    total_cells = []
    for i, val in enumerate(total):
        align = ' class="text-end"' if i > 0 else ""
        total_cells.append(f"<td{align}><strong>{val}</strong></td>")
    tbody += f'<tr>{"".join(total_cells)}</tr>'
    return (
        '<table class="table table-sm table-bordered table-sides-open align-middle mb-0">'
        f"<thead><tr>{thead}</tr></thead>"
        f"<tbody>{tbody}</tbody></table>"
    )


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


def figure_captioned(src: str, caption: str, fonte: str, alt: str = "") -> str:
    return row(
        f'<p class="mb-2"><strong>{caption}</strong></p>'
        f'<figure class="lightbox aos-init" data-aos="fade-up" data-aos-easing="ease-out" data-aos-duration="600">'
        f'<img class="img-fluid mx-auto d-block mb-3 rounded border" src="{MEDIA}{src}" alt="{alt}" loading="lazy" />'
        f"</figure>"
        f'<p class="figure-caption fonte small mb-0">{fonte}</p>'
    )


def chart_captioned(caption: str, fonte: str, svg: str, alt: str = "") -> str:
    return row(
        f'<p class="mb-2"><strong>{caption}</strong></p>'
        f'<figure class="lightbox aos-init" data-aos="fade-up" data-aos-easing="ease-out" data-aos-duration="600">'
        f"{svg}"
        f"</figure>"
        f'<p class="figure-caption fonte small mb-0">{fonte}</p>'
    )


def figure_plain(src: str, alt: str = "") -> str:
    return row(
        f'<figure class="lightbox aos-init" data-aos="fade-up" data-aos-easing="ease-out" data-aos-duration="600">'
        f'<img class="img-fluid mx-auto d-block mb-3 rounded border" src="{MEDIA}{src}" alt="{alt}" loading="lazy" />'
        f"</figure>"
    )


def ul(items: list[str]) -> str:
    lis = "".join(f'<li class="list-group-item">{item}</li>' for item in items)
    return f'<div class="list"><ul class="list-group">{lis}</ul></div>'


def box(kind: str, label: str, body: str) -> str:
    return row(
        f'<div class="box" data-box="{kind}"><div class="card"><div class="card-header">'
        f'<span class="icone material-symbols-rounded" aria-hidden="true"></span>'
        f'<span class="label">{label}</span></div><div class="card-body">'
        f'<p class="mb-0">{body}</p></div></div></div>'
    )


def quotation(text: str, autor: str) -> str:
    """Componente de citação com aspas decorativas (.quotation)."""
    return row(
        '<div class="quotation"><blockquote><div class="quotation-body">'
        '<span class="quotation-mark fa1"></span>'
        f"<p>{text}</p>"
        f'<span class="quotation-autor">{autor}</span>'
        "</div>"
        '<span class="quotation-mark fa2"></span>'
        "</blockquote></div>"
    )


def box_atencao(body: str) -> str:
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


def box_destaque(body: str) -> str:
    return row(
        f'<div class="card border-0 rounded overflow-hidden aos-init" data-aos="fade-up" '
        f'data-aos-easing="ease-out" data-aos-duration="600" '
        f'style="background-color:var(--fio-sys-color-primary-extra-dark);'
        f"background-image:url('{ASSETS}media/templates/fundo-flipcard.jpg');"
        f'background-size:cover;background-position:center;">'
        f'<div class="card-body p-4 p-md-5" style="color:#fff;">'
        f'<p class="mb-0" style="color:#fff;">{body}</p>'
        f"</div></div>"
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
            '<a class="fio-button fio-button-primary" href="../aula2/topico1.html" rel="next">'
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
									<li class="dropdown-menu__item">
										<a class="dropdown-menu__item-link" tabindex="0" role="link" href="../aula1/topico1.html"><strong>Aula 1: </strong>Análise exploratória e descritiva</a>
									</li>
									<li class="dropdown-menu__item">
										<a class="dropdown-menu__item-link" tabindex="0" role="link" href="../aula2/topico1.html"><strong>Aula 2: </strong>Estatística básica</a>
									</li>
									<li class="dropdown-menu__item">
										<a class="dropdown-menu__item-link" tabindex="0" role="link" href="../aula3/topico1.html"><strong>Aula 3: </strong>Estatística avançada</a>
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
		<meta name="keywords" content="Fiocruz Curso {COURSE_TITLE}" />
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
			var sidebar = new StickySidebar('.sidebar', {{
				topSpacing: 0,
				bottomSpacing: 0,
				containerSelector: '.main',
				innerWrapperSelector: '.sidebar__inner',
				minWidth: 991,
			}});

			function refreshSidebarSticky() {{
				if (sidebar && typeof sidebar.updateSticky === 'function') {{
					sidebar.updateSticky();
				}}
			}}

			window.addEventListener('load', refreshSidebarSticky);
			window.addEventListener('resize', refreshSidebarSticky);
			document.querySelectorAll('.content img').forEach(function (img) {{
				if (!img.complete) {{
					img.addEventListener('load', refreshSidebarSticky);
					img.addEventListener('error', refreshSidebarSticky);
				}}
			}});
		</script>
		<script type="text/javascript" src="{ASSETS}assets/js/scripts.js"></script>
		<script type="text/javascript" src="{ASSETS}assets/js/custom-anime.js"></script>
		<script type="text/javascript" src="{ASSETS}source/animate/aos/dist/aos.js"></script>
		<script>
			AOS.init();
		</script>
	</body>
</html>
"""


def content_sobre() -> str:
    return (
        heading(1, "Sobre esta aula")
        + row(
            p('Seja bem-vindo e bem-vinda à aula “Análise exploratória e descritiva”.')
            + p("A seguir, veja algumas informações importantes!")
        )
        + subheading("Objetivos de aprendizagem")
        + row(
            p("Ao final dessa aula, você será capaz de:")
            + ul(
                [
                    "Compreender o conceito de Estatística e seu alcance;",
                    "Conhecer os conceitos de população e amostra;",
                    "Entender a diferença entre variável e dados;",
                    "Diferenciar os tipos de variáveis;",
                    "Reconhecer a descrição de dados na representação tabular e gráfica;",
                    "Interpretar de tabelas e gráficos.",
                ]
            )
        )
        + subheading("Autoria")
        + row(
            p("<strong>Carla Lourenço Tavares de Andrade.</strong>")
            + p(
                "Estatístico. Escola Nacional de Saúde Pública Sergio Arouca (ENSP) da Fundação "
                "Oswaldo Cruz.",
                mb0=True,
            )
        )
    )


def content_introducao() -> str:
    return (
        heading(2, "Introdução")
        + row(p("Vamos conversar sobre Estatística? Você sabe o que é?"))
        + quotation(
            "“Estatística é a ciência que fornece os princípios e a metodologia para coleta, "
            "organização, apresentação, resumo, análise e interpretação de dados”.",
            "Segundo Vieira (2015)",
        )
        + row(
            p(
                "A Estatística pode ser dividida em descritiva e inferencial. Na primeira, leva-se em "
                "consideração o levantamento, organização e descrição dos dados em tabelas, gráficos "
                "ou outros recursos visuais e as estatísticas descritivas. A Estatística Descritiva auxilia o(a) "
                "pesquisador(a) a entender a informação que os dados fornecem por meio de um resumo. "
                "Complementarmente, a Estatística Inferencial serve para tirar conclusões para a população da "
                "qual a amostra foi extraída, tendo sua estrutura fundamentada na teoria das probabilidades."
            )
        )
        + figure_plain("intro-dados.png", "Notebook com gráficos de dados em ambiente de trabalho")
        + row(
            p(
                "Na Estatística, temos alguns conceitos importantes. Por exemplo, você sabe o que é "
                "população, amostra, variável e dado?"
            )
        )
        + subheading("População", "h5")
        + row(
            p(
                "É o conjunto de elementos que compartilham pelo menos uma característica em comum."
            )
        )
        + subheading("Amostra", "h5")
        + row(
            p(
                "Uma amostra é parte dessa população. Cabe mencionar que a amostra deve ser selecionada "
                "de forma aleatória e, também, ser representativa da população, conservando suas "
                "propriedades. No entanto, como selecionar a amostra ou como calcular o tamanho da "
                "amostra não faz parte do escopo dessa aula. Para maiores informações veja no livro do "
                "Barbetta (2002)."
            )
        )
        + subheading("Variável", "h5")
        + row(
            p(
                "É a característica de interesse que é medida em cada elemento da amostra ou população, "
                "podendo ter resultados numéricos ou não. É a quantificação ou categorização de interesse "
                "do estudo."
            )
        )
        + box_atencao(
            "Quando a gente conhece os tipos de variáveis do nosso estudo, "
            "conseguimos determinar os métodos de análise apropriados!"
        )
        + row(
            p(
                "As variáveis são classificadas em qualitativas e quantitativas. As variáveis qualitativas, "
                "por sua vez, são classificadas em nominais e ordinais. As variáveis quantitativas são "
                "divididas em discretas e contínuas."
            )
            + p(
                "As variáveis qualitativas nominais são àquelas que têm uma ordenação natural. "
                "Essas podem ser dicotômicas (duas categorias) ou multinomiais (várias categorias). "
                "Por exemplo, tabagismo, pensando se a pessoa fuma ou não (variável nominal - dicotômica). "
                "Porém, a variável tabagismo for composta pelas categorias fumante, ex-fumante e nunca "
                "fumou, é uma variável nominal multinomial."
            )
            + p(
                "As variáveis nominais ordinais se enquadram nas categorias com uma ordenação natural "
                "ou estabelecida."
            )
            + p(
                "Por exemplo, o estadiamento de um tumor primário, que varia de T0 a T4 ou a faixa etária "
                "(menor de um ano, 1 a 4 anos, 5 a 9, 10 a 14, 15 a 19 etc.)."
            )
            + p(
                "As variáveis quantitativas discretas são àquelas que podem assumir apenas valores inteiros. "
                "Pensando, por exemplo, que uma cidade não tem uma clínica e meia de olhos. Ou a cidade "
                "não tem clínica ou tem uma ou tem duas etc. Da mesma forma, podemos dizer para número "
                "de leitos. Não existe três leitos e uma metade; ou nenhum ou dois ou três ou quatro etc. "
                "Assim, quando podemos contar, podemos dizer que é uma variável quantitativa discreta."
            )
            + p(
                "As variáveis quantitativas contínuas se diferem por serem mensuráveis e que assumem "
                "valores em uma escala contínua, para os quais valores fracionários fazem sentido. "
                "Usualmente, devem ser medidas por meio de instrumento. Assim, precisamos de uma "
                "balança, por exemplo, para medir o peso (em kg) de uma pessoa como precisamos de um "
                "aparelho de pressão para medir a pressão arterial (em mmHg). Outra variável relevante "
                "é a renda (expressos em valores monetários), que é utilizada em várias pesquisas."
            )
        )
        + subheading("Dado", "h5")
        + row(
            p(
                "Dado é qualquer característica passível de observação em uma população ou amostra."
            )
        )
        + box_destaque(
            "Nesse sentido, podemos afirmar que a qualidade das informações "
            "depende da qualidade dos dados!"
        )
        + row(
            p(
                "Os dados podem ser classificados em primários ou secundários. Vocês sabem qual é "
                "a diferença?"
            )
            + p(
                "Dados primários é quando o(a) pesquisador(a) coleta junto com sua equipe. Em contrapartida, "
                "os dados secundários não foram coletados pelo(a) pesquisador(a) e sua equipe. Exemplos "
                "do nosso dia a dia de dados secundários são os sistemas de informação em saúde "
                "disponibilizados pelo DATASUS. Os dados de óbitos (Sistema de Informações sobre "
                "Mortalidade - SIM), os de nascidos vivos (Sistema de Informações sobre Nascidos Vivos - "
                "SINASC), os de internação (Sistema de Informações Hospitalares do SUS – SIH/SUS), os de "
                "produção ambulatorial (Sistema de Informações Ambulatoriais do SUS - SIA/SUS), dentre "
                "outros são considerados dados secundários.",
                mb0=True,
            )
        )
    )


def content_tabelas() -> str:
    ibge = (
        '<a href="https://biblioteca.ibge.gov.br/visualizacao/monografias/GEBIS%20-%20RJ/normastabular.pdf" '
        'target="_blank" rel="noopener noreferrer">'
        "http://biblioteca.ibge.gov.br/visualizacao/monografias/GEBIS%20-%20RJ/normastabular.pdf</a>"
    )
    unesp = (
        '<a href="https://www.foa.unesp.br/#!/instituicao/biblioteca/normas-tecnicas/normas-de-apresentacao-de-tabelas/" '
        'target="_blank" rel="noopener noreferrer">'
        "https://www.foa.unesp.br/#!/instituicao/biblioteca/normas-tecnicas/normas-de-apresentacao-de-tabelas/</a>"
    )
    return (
        heading(3, "Tabelas")
        + row(
            p(
                "Mas como tratamos esses dados? De três maneiras, principalmente. A primeira é por meio "
                "de tabelas, em segundo, com a construção de gráficos e não menos importante o cálculo "
                "de medidas-resumo. Essa última veremos na aula subsequente."
            )
            + p(
                "Começando pelas tabelas, a gente não faz tabela como a gente quer. Existem normas e "
                "essas foram publicadas em 1991 pelo Instituto Brasileiro de Geografia e Estatística (IBGE), "
                f'sob o título “Normas de apresentação tabular” (disponível em: {ibge}).'
            )
            + p(
                "Basicamente, uma tabela deve ser simples, clara e objetiva. Ou seja, ela deve ser "
                "autoexplicativa! Quando vemos uma tabela devemos, por si só, interpretá-la sem auxílio de "
                "um texto com a explicação."
            )
            + p(
                "A seguir estão os elementos que compõem uma tabela, como apresentado na figura 1:"
            )
            + ul(
                [
                    "Corpo: conjunto das informações que aparecem no sentido vertical e horizontal.",
                    "Coluna indicadora: divisão em sentido vertical onde aparece a designação da natureza do conteúdo da linha.",
                    "Cabeçalho: indica a natureza do conteúdo de cada coluna.",
                    "Célula: são divisões que aparecem no corpo da tabela.",
                    "Rodapé.",
                ]
            )
            + p(
                "Fonte: é a indicação da entidade responsável pela elaboração da tabela. Deve ser colocada no "
                "rodapé, no final da tabela."
            )
            + p(
                "Notas: também devem ser colocadas no rodapé, depois da fonte, de forma sintética."
            )
        )
        + figure_captioned(
            "figura1-elementos-tabela.png",
            "Figura 1: Elementos de uma tabela.",
            f"Fonte: Disponível em {unesp}.",
            "Esquema dos elementos de uma tabela",
        )
        + row(
            p("Pelas normas de apresentação tabular:")
            + ul(
                [
                    "As tabelas devem ser numeradas, quando temos várias em um texto.",
                    "Nenhuma célula da tabela deve ficar em branco, apresentando, sempre, um número ou símbolo. Entende-se por célula qualquer divisão que aparece na tabela.",
                    "As tabelas devem ser fechadas no alto e embaixo com linhas horizontais. Muito importante: não feche as tabelas nas laterais! Porém, as linhas verticais internas são opcionais.",
                    "Uniformize o número de casas decimais. Ora com uma casa ora com duas ora com nenhuma não é bom. Escolha, por exemplo, uma casa decimal e aplique em todos os valores com decimais.",
                    "Os totais e subtotais devem ser destacados.",
                    "Os títulos devem responder às seguintes perguntas: O quê? Quem? Onde? Quando?",
                    "Incluir a fonte dos dados no rodapé da tabela.",
                    "No rodapé devem conter a fonte e, em sequência, se necessário, as notas, que são observações sucintas da tabela.",
                ]
            )
            + p(
                "Para construir uma tabela devemos considerar a frequência com que cada observação "
                "ocorre. Então, frequência absoluta é o número observado em cada classe ou categoria. "
                "Frequência relativa é a divisão entre a frequência absoluta da classe e a frequência absoluta "
                "total. Geralmente, usamos o símbolo % no cabeçalho da tabela. A frequência acumulada, que "
                "pode ser a absoluta ou a relativa (em percentual), é obtida por meio da soma da frequência "
                "daquela classe mais as frequências de todas as classes anteriores. Usualmente, a frequência "
                "acumulada é apresentada nas saídas dos softwares de estatística."
            )
        )
        + box_atencao(
            "Chama atenção que no cálculo do percentual precisa, sempre, fechar 100%! "
            "Caso não aconteça orienta-se usar as regras de arredondamento, podendo "
            "a frequência de maior valor ser utilizada para esse fim."
        )
        + row(
            p(
                "A partir desse momento, vamos usar um pequeno conjunto de dados hipotéticos com "
                "40 observações gerado por meio de ferramenta de inteligência artificial (Google Gemini). "
                "O conjunto de dados contém informações sobre controle do Diabetes tipo 2 em pacientes "
                "acompanhados por uma clínica médica. Variáveis como glicemia (controlada / não controlada); "
                "adesão à dieta (baixa / moderada / alta); prática de exercício físico (rara / moderada / diária); "
                "Idade do paciente (em anos); número de meses de descoberta do diabetes e IMC (Índice de "
                "Massa Corporal) foram abordadas."
            )
            + p(
                "Como exemplo de variável qualitativa nominal (dicotômica), apresenta-se na tabela 1 "
                "o resultado da glicemia (controlada ou não) dos pacientes de uma clínica médica. "
                "É nítido o predomínio de pacientes com a glicemia não controlada (72,5%)."
            )
        )
        + table_captioned(
            "Tabela 1: Glicemia de pacientes acompanhados em uma clínica médica.",
            FONTE_FICTICIA,
            freq_table(
                ["Glicemia", "Frequência", "Percentual", "Frequência acumulada", "Percentual acumulado"],
                [
                    ["Controlada", "11", "27,5", "11", "27,5"],
                    ["Não Controlada", "29", "72,5", "40", "100"],
                ],
                ["Total", "40", "100,0", "-", "-"],
            ),
        )
        + row(
            p(
                "Considerando uma variável qualitativa com mais de duas categorias (multinomial) observa-se a "
                "tabela 2, com a variável exercício físico (se pratica raramente, moderado ou diariamente). A maioria "
                "pratica exercício físico de forma rara (55,0%). Nesse caso, é um exemplo de uma variável "
                "qualitativa ordinal. Recomenda-se apresentar as categorias na ordem natural já estabelecida."
            )
        )
        + table_captioned(
            "Tabela 2: Prática de exercício físico dos pacientes de uma clínica médica.",
            FONTE_FICTICIA,
            freq_table(
                [
                    "Prática exercício físico",
                    "Frequência",
                    "Percentual",
                    "Frequência acumulada",
                    "Percentual acumulado",
                ],
                [
                    ["Rara", "22", "55,0", "22", "55,0"],
                    ["Moderada", "12", "30,0", "34", "85,0"],
                    ["Diária", "6", "15,0", "40", "100,0"],
                ],
                ["Total", "40", "100,0", "-", "-"],
            ),
        )
        + row(
            p(
                "No caso das variáveis quantitativas discretas é possível apresentar uma tabela (desde que "
                "não haja muita variação entre os dados."
            )
            + p(
                "Na tabela 3 estão os dados da variável há quantos meses o paciente descobriu o diabetes. "
                "Aqui, particularmente observa-se uma situação muito comum, que é a ausência de dados. "
                "Como lidar? Bem, quando estamos nessa fase exploratória dos dados recomenda-se "
                "considerar todos os dados justamente para identificar a quantidade (percentual) de dados "
                "faltantes. Se for muito elevado o ideal é não utilizar essa variável no estudo. Alguns "
                "softwares de estatística calculam o percentual sem esses dados, outros apresentam os dois "
                "percentuais (com e sem os dados faltantes)."
            )
        )
        + table_captioned(
            "Tabela 3: Número de meses de descoberta do diabetes dos pacientes da clínica médica.",
            FONTE_FICTICIA,
            freq_table(
                ["Meses", "Frequência", "Percentual"],
                [
                    ["1", "7", "17,5"],
                    ["2", "7", "17,5"],
                    ["3", "5", "12,5"],
                    ["4", "7", "17,5"],
                    ["5", "6", "15,0"],
                    ["6", "6", "15,0"],
                    ["Sem informação", "2", "5,0"],
                ],
                ["Total", "40", "100,0"],
            ),
        )
        + row(
            p("No caso em questão, o percentual de dados faltantes (5,0) é muito pequeno.")
            + p(
                "Quando as variáveis são quantitativas contínuas a apresentação tabular talvez não seja a "
                "melhor forma por conter muitos valores. Nesse caso, a ideia de sumarização fica perdida, "
                "pois a tabela de tão longa por conta da variabilidade pode apresentar páginas e páginas de "
                "dados, o que em vez de ajudar acaba prejudicando a análise. Para resolver esse problema, "
                "sugere-se transformar a variável quantitativa contínua em uma variável qualitativa ordinal. "
                "É verdade que podemos “perder” informação, mas é a maneira mais simples de "
                "apresentação tabular. Então, surge a pergunta, como devo categorizar a variável? "
                "Existe um cálculo específico, porém podemos basear na literatura para definir as classes "
                "de acordo com o objeto a ser estudado."
            )
            + p(
                "Voltando para os nossos dados, uma tabela com a frequência da variável índice de massa "
                "corpórea (IMC) não nos diz muita coisa, pois os valores não se repetem, tendo, então, uma "
                "tabela com 40 linhas (número de observações). Veja na tabela 4."
            )
        )
        + table_captioned(
            "Tabela 4: Índice de Massa Corpórea (IMC) dos pacientes da clínica médica.",
            FONTE_FICTICIA,
            freq_table(
                ["IMC", "Frequência", "Percentual"],
                [[imc, "1", "2,50"] for imc in IMC_VALORES],
                ["Total", "40", "100,0"],
            ),
        )
        + row(
            p(
                "Podemos, então, categorizar essa variável. De acordo com Nuttall (2015), o IMC é dividido "
                "em seis categorias: abaixo do peso (IMC &lt; 20,0); peso normal (20,0 &lt;= IMC &lt;= 24,9); "
                "sobrepeso (IMC 25,0 &lt;= IMC &lt;= 29,9); obesidade grau I (30,0 &lt;= IMC &lt;= 34,9); obesidade "
                "grau II (35,0 &lt;= IMC &lt;= 39,9) e obesidade grau III (IMC &gt;= 40,0). Assim, os dados de IMC "
                "para os pacientes da clínica médica do nosso exemplo estão apresentados na tabela 5. "
                "Observa-se que 60,0% dos pacientes apresentam sobrepeso ou obesidade de grau I."
            )
        )
        + table_captioned(
            "Tabela 5: Índice de Massa Corpórea (IMC) dos pacientes da clínica médica.",
            FONTE_FICTICIA,
            freq_table(
                ["Índice de Massa Corpórea (IMC)", "Frequência", "Percentual"],
                [
                    ["Abaixo do peso", "1", "2,5"],
                    ["Peso normal", "7", "17,5"],
                    ["Sobrepeso", "12", "30,0"],
                    ["Obesidade grau I", "12", "30,0"],
                    ["Obesidade grau II", "7", "17,5"],
                    ["Obesidade grau III", "1", "2,5"],
                ],
                ["Total", "40", "100,0"],
            ),
        )
    )


def content_graficos() -> str:
    yt = (
        '<a href="https://www.youtube.com/watch?v=1YGxwM6qgGQ" target="_blank" rel="noopener noreferrer">'
        "Acesse o link aqui</a>"
    )
    return (
        heading(4, "Gráficos")
        + row(
            p(
                "Outra forma de sumarização dos dados é o gráfico. Da mesma forma que as tabelas, existem "
                "regras para sua construção. Assim:"
            )
            + ul(
                [
                    "Devem ser autoexplicativos.",
                    "Devem responder às perguntas: O quê? Quem? Onde? Quando?",
                    "Devem ter os títulos dos eixos horizontal e vertical, juntamente com as unidades de medida.",
                    "Uniformize o número de casa decimais.",
                    "Evite o uso de efeitos 3D, pois torna mais difícil para estimar os valores representados.",
                ]
            )
            + p(
                "Como dito anteriormente, o tipo de variável determina o tipo de técnica a ser utilizada. Isso "
                "vale, também, para os gráficos."
            )
            + p(
                "Nos gráficos, temos dois tipos mais apropriados para variáveis qualitativas (nominais "
                "e ordinais), que são o gráfico de barras e o gráfico de setores, também chamado "
                "de “pizza” ou “torta”."
            )
            + p(
                "Nas variáveis qualitativas, as barras do gráfico podem ser verticais ou horizontais. "
                "Entretanto, para as variáveis quantitativas discretas somente devemos usar as barras "
                "verticais. Pode-se empregar tanto a frequência absoluta quanto a frequência relativa "
                "(em percentual). Vejamos alguns exemplos."
            )
            + p(
                "No gráfico 1, temos a variável glicemia (controlada / não controlada), que é classificada como "
                "variável qualitativa nominal. É um gráfico de barras verticais, com os valores expressos em "
                "percentuais, mostrando que os pacientes com glicemia não controlada são maioria."
            )
        )
        + chart_captioned(
            "Gráfico 1: Glicemia de pacientes acompanhados em uma clínica médica.",
            FONTE_FICTICIA,
            bar_chart_vertical(
                ["Controlada", "Não controlada"],
                [27.5, 72.5],
                y_max=80,
                y_step=10,
                y_label="%",
                x_label="Glicemia",
                alt="Gráfico de barras da glicemia",
            ),
            "Gráfico de barras da glicemia",
        )
        + row(
            p(
                "A variável qualitativa ordinal (prática de exercício físico) está apresentada no gráfico 2 por "
                "meio de um gráfico de setores, que serve para caracterizar a participação de cada categoria "
                "(rara / moderada / diária) em relação ao total. Observa-se, nesse caso, que os pacientes com "
                "frequência diária de exercício físico prevalecem em relação às outras categorias."
            )
        )
        + chart_captioned(
            "Gráfico 2: Prática de exercício físico dos pacientes de uma clínica médica.",
            FONTE_FICTICIA,
            pie_chart(
                ["Rara", "Moderada", "Diária"],
                [55, 30, 15],
                [C_PIE_3, C_PIE_2, C_PIE_1],
                alt="Gráfico de setores da prática de exercício físico",
            ),
            "Gráfico de setores da prática de exercício físico",
        )
        + row(
            p(
                "No gráfico 3, apresenta-se a variável adesão à dieta (baixa / moderada / alta) para controle "
                "da glicemia dos pacientes da clínica médica por meio do gráfico de barras horizontais. "
                "Observe que é uma variável qualitativa ordinal. Chama atenção que menos de 20% dos "
                "pacientes têm alta adesão à dieta."
            )
        )
        + chart_captioned(
            "Gráfico 3: Adesão à dieta para controle de glicemia dos pacientes de uma clínica médica.",
            FONTE_FICTICIA,
            bar_chart_horizontal(
                ["Alta", "Moderada", "Baixa"],
                [17.5, 37.5, 45.0],
                x_max=50,
                x_step=10,
                y_label="Adesão à dieta",
                x_label="%",
                alt="Gráfico de barras horizontais da adesão à dieta",
            ),
            "Gráfico de barras horizontais da adesão à dieta",
        )
        + row(
            p(
                "No caso das variáveis quantitativas discretas é possível apresentar um gráfico de barras, mas "
                "somente verticais. Veja no exemplo no gráfico 4."
            )
        )
        + chart_captioned(
            "Gráfico 4: Número de meses de descoberta do diabetes dos pacientes da clínica médica.",
            "Fonte: Dados fictícios gerados por Inteligência Artificial (Google Gemini), em julho de 2026",
            bar_chart_vertical(
                ["1", "2", "3", "4", "5", "6", "Sem informação"],
                [7, 7, 5, 7, 6, 6, 2],
                y_max=10,
                y_step=1,
                y_label="N",
                x_label="Número de meses",
                alt="Gráfico de barras do número de meses de descoberta do diabetes",
            ),
            "Gráfico de barras do número de meses de descoberta do diabetes",
        )
        + row(
            p(
                "A quantidade de pacientes que tem pouco tempo que descobriu a doença é semelhante "
                "àqueles que têm cinco ou seis meses de descoberta do diabetes."
            )
            + p(
                "Para as variáveis quantitativas contínuas, o ideal é construir um histograma. Existem "
                "diversos vídeos na internet sobre como construir um histograma. O link é somente um "
                f"exemplo. {yt}."
            )
            + p(
                "Nosso exemplo é com a variável IMC (índice de massa corpórea) dos pacientes de uma "
                "clínica médica, apresentada no gráfico 5."
            )
            + p(
                "Observa-se que a maioria tem IMC entre 25 e 35, classificados como sobrepeso e obesidade "
                "de grau I."
            )
        )
        + chart_captioned(
            "Gráfico 5: Índice de Massa Corpórea dos pacientes de uma clínica médica.",
            FONTE_FICTICIA,
            histogram_chart(
                *imc_histogram_bins(IMC_VALORES),
                y_max=12,
                x_label="IMC",
                y_label="Frequência",
                alt="Histograma do IMC",
            ),
            "Histograma do IMC",
        )
        + row(
            p(
                "Até esse momento, tratamos de tabelas e gráficos com uma variável. Para duas variáveis, "
                "temos uma tabela de dupla entrada. Com relação aos gráficos, podemos construir um "
                "diagrama de barras ou um diagrama de dispersão. O gráfico de linhas deve ser usado quando "
                "queremos mostrar a evolução no tempo de um evento."
            )
            + p(
                "Vamos começar com uma tabela de dupla entrada com as variáveis estado civil e região de "
                "procedência, por exemplo (Tabela 6)."
            )
        )
        + table_captioned(
            "Tabela 6: Glicemia segundo adesão à dieta dos pacientes de uma clínica médica.",
            FONTE_FICTICIA,
            cross_table(
                "Glicemia",
                "Adesão à dieta",
                ["Controlada", "Não controlada"],
                ["Baixa", "Moderada", "Alta"],
                [
                    [("7", "63,6"), ("3", "27,3"), ("1", "9,1"), ("11", "100,0")],
                    [("11", "37,9"), ("12", "41,4"), ("6", "20,7"), ("29", "100,0")],
                ],
                [("18", "45,0"), ("15", "37,5"), ("7", "17,5"), ("40", "100,0")],
            ),
        )
        + row(
            p(
                "É importante destacar que os percentuais foram calculados em relação à linha, ou seja, em "
                "relação à variável glicemia. A interpretação é, por exemplo, dentre os pacientes com glicemia "
                "controlada, 63,6% têm baixa adesão à dieta."
            )
            + p(
                "Na tabela 7, o percentual está calculado em relação à coluna, ou seja, em relação à variável "
                "adesão à dieta. Observem que a interpretação é diferente. Vejam."
            )
        )
        + table_captioned(
            "Tabela 7: Glicemia segundo adesão à dieta dos pacientes de uma clínica médica.",
            FONTE_FICTICIA,
            cross_table(
                "Glicemia",
                "Adesão à dieta",
                ["Controlada", "Não controlada"],
                ["Baixa", "Moderada", "Alta"],
                [
                    [("7", "38,9"), ("3", "20,0"), ("1", "14,3"), ("11", "27,5")],
                    [("11", "61,1"), ("12", "80,0"), ("6", "85,7"), ("29", "72,5")],
                ],
                [("18", "100,0"), ("15", "100,0"), ("7", "100,0"), ("40", "100,0")],
            ),
        )
        + row(
            p(
                "Dentre aqueles pacientes que têm baixa adesão à dieta, 38,9% apresentam glicemia "
                "controlada."
            )
            + p(
                "É importante ressaltar que não existe certo ou errado, pois depende do enfoque que "
                "queremos, análise pela variável que estiver na linha ou na coluna."
            )
            + p(
                "Podemos visualizar as variáveis glicemia e adesão à dieta em um gráfico de barras verticais "
                "(gráfico 6)."
            )
        )
        + chart_captioned(
            "Gráfico 6: Glicemia segundo adesão à dieta dos pacientes de uma clínica médica.",
            FONTE_FICTICIA,
            grouped_bar_chart(
                ["Baixa", "Moderada", "Alta"],
                {"Controlada": [7, 3, 1], "Não controlada": [11, 12, 6]},
                {"Controlada": C_CONTROLADA, "Não controlada": C_NAO_CONTROLADA},
                y_max=14,
                y_step=2,
                x_label="Adesão à dieta",
                y_label="N",
                alt="Gráfico de barras de glicemia segundo adesão à dieta",
            ),
            "Gráfico de barras de glicemia segundo adesão à dieta",
        )
        + row(
            p(
                "Quando se tem duas variáveis quantitativas (discretas ou contínuas) usamos o diagrama de "
                "dispersão, que é uma representação gráfica realizada no sistema de coordenadas, em que "
                "uma variável é representada no eixo das abscissas (eixo horizontal) e a outra variável no eixo "
                "das ordenadas (eixo vertical). Assim, podemos interpretar o relacionamento entre essas duas "
                "variáveis na sua forma, direção e intensidade de relacionamento."
            )
        )
        + chart_captioned(
            "Gráfico 7: Idade segundo salário (expresso como fração do salário-mínimo) de "
            "36 empregados da seção de orçamento da Companhia MB.",
            FONTE_FICTICIA,
            scatter_chart(
                scatter_points_from_imc(IMC_VALORES),
                x_min=30,
                x_max=80,
                y_min=15,
                y_max=45,
                x_step=10,
                y_step=5,
                x_label="Idade",
                y_label="IMC",
                alt="Diagrama de dispersão",
            ),
            "Diagrama de dispersão",
        )
        + row(
            p(
                "Podemos observar que à medida que aumenta a idade dos pacientes o índice de massa "
                "corpórea também aumenta."
            )
            + p(
                "O gráfico de linhas é usado na escala temporal, que é apresentada no eixo horizontal (eixo "
                "X). No eixo das ordenadas é a variável a ser estudada. Uma vantagem desse tipo de gráfico é "
                "que várias séries temporais podem ser representadas em um único gráfico 6."
            )
        )
        + chart_captioned(
            "Gráfico 8: Número de nascimentos por região, Brasil, 2000-2024.",
            "Fonte: MS/SVSA/CGIAE - Sistema de Informações sobre Nascidos Vivos – SINASC",
            line_chart_multi(
                SINASC_YEARS,
                SINASC_SERIES,
                y_max=1400000,
                y_step=200000,
                y_label="Número de nascimentos",
                alt="Gráfico de linhas de nascimentos por região",
            ),
            "Gráfico de linhas de nascimentos por região",
        )
        + row(
            p(
                "O gráfico 8 mostra o número de nascimentos por região do Brasil. Observa-se que, "
                "mesmo com tendência de declínio, a região Sudeste é a que possui a maior quantidade de "
                "nascimentos ao longo do período.",
                mb0=True,
            )
        )
    )


def content_referencias() -> str:
    return (
        heading(5, "Referências")
        + row(
            '<div class="referencias-aula">'
            '<p class="referencias-item">Google Gemini. Simulação de dados hipotéticos sobre controle de '
            "Diabetes Tipo 2. Versão de julho de 2026. Disponível em: inteligência artificial generativa da Google. "
            "Acesso em: 14 jul. 2026. Conjunto de dados fictícios gerado para fins de validação estatística.</p>"
            '<p class="referencias-item">Nuttall FQ. Body Mass Index: Obesity, BMI, and Health: A Critical Review. '
            "Nutr Today. 2015 May;50(3):117-128. doi: 10.1097/NT.0000000000000092. Epub 2015 Apr 7. PMID: "
            "27340299; PMCID: PMC4890841.</p>"
            '<p class="referencias-item">Vieira, Sonia. Estatística básica. São Paulo: Cengage Learning, 2015.</p>'
            "</div>"
        )
    )


CONTENT_BUILDERS = [
    content_sobre,
    content_introducao,
    content_tabelas,
    content_graficos,
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
