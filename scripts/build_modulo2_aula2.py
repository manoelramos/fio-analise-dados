#!/usr/bin/env python3
"""Gera HTML da Aula 2.2 (Introdução aos Modelos) a partir do PDF — sem alterar textos."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "modulo2" / "aula2"
MEDIA = "../../media/modulo2/aula2/"
ASSETS = "../../"

COURSE_TITLE = "Análise e Interpretação de Dados em Saúde"
MODULE_NUM = 2
MODULE_TITLE = "Séries Temporais"
AULA_LABEL = "Aula 2"
AULA_TITLE = "Séries Temporais - Introdução aos Modelos"

TOPICS = [
    "Sobre esta aula",
    "Introdução",
    "Modelos de Decomposição",
    "Suavização por Médias Móveis",
    "Séries Temporais Interrompidas (STI)",
    "Conclusão",
    "REFERÊNCIAS",
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


def box(kind: str, label: str, body: str) -> str:
    return row(
        f'<div class="box" data-box="{kind}"><div class="card"><div class="card-header">'
        f'<span class="icone material-symbols-rounded" aria-hidden="true"></span>'
        f'<span class="label">{label}</span></div><div class="card-body">'
        f'<p class="mb-0">{body}</p></div></div></div>'
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


def accordion(accordion_id: str, items: list[tuple[str, str]]) -> str:
    parts = [f'<div class="accordion accordion-flush" id="{accordion_id}">']
    for i, (title, body) in enumerate(items):
        hid = f"{accordion_id}-{i}-h"
        cid = f"{accordion_id}-{i}-c"
        parts.append(
            f'<div class="accordion-item"><h5 class="accordion-header" id="{hid}">'
            f'<button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" '
            f'data-bs-target="#{cid}" aria-expanded="false" aria-controls="{cid}">{title}</button></h5>'
            f'<div id="{cid}" class="accordion-collapse collapse" aria-labelledby="{hid}" '
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
										<a class="dropdown-menu__item-link" tabindex="0" role="link" href="../aula1/topico1.html"><strong>Aula 1: </strong>Análise exploratória</a>
									</li>
									<li class="dropdown-menu__item">
										<a class="dropdown-menu__item-link" tabindex="0" role="link" href="../aula2/topico1.html"><strong>Aula 2: </strong>Introdução aos modelos</a>
									</li>
									<li class="dropdown-menu__item">
										<a class="dropdown-menu__item-link" tabindex="0" role="link" href="../aula3/topico1.html"><strong>Aula 3: </strong>Análise de série histórica - prática</a>
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
            p('Seja bem-vindo e bem-vinda à aula “Séries Temporais - Introdução aos Modelos”.')
            + p("A seguir, veja algumas informações importantes!")
        )
        + subheading("Objetivos de aprendizagem")
        + row(
            p("Ao final dessa aula, você será capaz de:")
            + '<div class="list"><ul class="list-group">'
            + '<li class="list-group-item">Diferenciar os modelos de decomposição aditivo e multiplicativo.</li>'
            + '<li class="list-group-item">Aplicar a técnica de suavização por médias móveis para estimar a tendência de uma série.</li>'
            + '<li class="list-group-item">Compreender o desenho de estudo de Séries Temporais Interrompidas (STI) e sua '
            "aplicação na avaliação de intervenções em saúde pública.</li>"
            + "</ul></div>"
        )
        + subheading("Autoria")
        + row(
            p("<strong>Diego Ricardo Xavier</strong>")
            + p("Doutor em Epidemiologia. Mestrado em Saúde Pública. Pesquisador em Saúde Pública")
            + p(
                "Instituto de Comunicação e Informação Científica e Tecnológica em Saúde (Icict) "
                "da Fundação Oswaldo Cruz (Fiocruz)"
            )
            + p("<strong>Julia Novaes de Barros Peixoto</strong>")
            + p(
                "Mestre em Ciências - Métodos quantitativos em Epidemiologia &amp; Engenheira Cartógrafa.",
                mb0=True,
            )
        )
    )


def content_introducao() -> str:
    return (
        heading(2, "Introdução")
        + row(
            p(
                "Após a análise exploratória, que nos permite identificar os componentes de uma série "
                "temporal (tendência, sazonalidade, ciclo e ruído), o passo seguinte é a aplicação de modelos "
                "para descrever, explicar e prever o comportamento do fenômeno em estudo. Os modelos "
                "de séries temporais são ferramentas estatísticas que formalizam os padrões observados, "
                "permitindo-nos separar os componentes e avaliar o impacto de eventos externos "
                "(LATORRE; CARDOSO, 2001)."
            )
        )
        + figure_plain("intro-tablet.png", "Pessoa analisando gráficos em um tablet")
        + row(
            p(
                "Nesta aula, introduziremos três abordagens fundamentais: os modelos de decomposição, "
                "a técnica de suavização por médias móveis e o desenho de estudo de séries temporais "
                "interrompidas, um método poderoso para a avaliação de intervenções em saúde pública.",
                mb0=True,
            )
        )
    )


def content_decomposicao() -> str:
    table = (
        '<div class="table-responsive"><table class="table table-sm table-bordered align-middle mb-0">'
        "<thead><tr>"
        '<th scope="col">Modelo</th>'
        '<th scope="col">Característica Principal</th>'
        '<th scope="col">Quando Usar</th>'
        "</tr></thead><tbody>"
        "<tr><td><strong>Aditivo</strong></td>"
        "<td>A amplitude das flutuações sazonais é constante ao longo do tempo, não dependendo "
        "do nível da série.</td>"
        "<td>Use quando a variação sazonal parece ser a mesma, independentemente de a "
        "tendência ser alta ou baixa.</td></tr>"
        "<tr><td><strong>Multiplicativo</strong></td>"
        "<td>A amplitude das flutuações sazonais é proporcional ao nível da série. A variação "
        "sazonal aumenta quando a tendência sobe.</td>"
        "<td>Use quando a variação sazonal parece ser um percentual do nível da série. "
        "Ex: uma série de casos de gripe onde o pico de inverno representa um aumento de "
        "50% em relação à média.</td></tr>"
        "</tbody></table></div>"
    )
    return (
        heading(3, "Modelos de Decomposição")
        + row(
            p(
                "A decomposição de uma série temporal consiste em separar a série original em seus "
                "componentes constituintes. O objetivo é isolar a tendência, a sazonalidade e o componente "
                "irregular (ruído) para analisá-los separadamente. Existem dois modelos clássicos de "
                "decomposição (ANTUNES; CARDOSO, 2015) (ZHANG et al., 2014):"
            )
            + '<div class="list"><ul class="list-group">'
            + '<li class="list-group-item">Modelo Aditivo: Y(t) = T(t) + S(t) + R(t)</li>'
            + '<li class="list-group-item">Modelo Multiplicativo: Y(t) = T(t) * S(t) * R(t)</li>'
            + "</ul></div>"
            + p(
                'Visualmente, a escolha entre os modelos pode ser feita observando o gráfico da série. '
                'Se a "largura" do padrão sazonal se expande ou se contrai junto com a tendência, '
                "o modelo multiplicativo é provavelmente mais adequado. Este é o caso mais comum "
                "em dados epidemiológicos (ANTUNES; CARDOSO, 2015). A Figura 1 ilustra essa "
                "diferença fundamental."
            )
        )
        + figure_captioned(
            "figura1-decomposicao.png",
            "Figura 1 – Comparação entre os modelos de decomposição Aditivo e Multiplicativo",
            "Fonte: Elaborado pelo autor (2026).",
            "Comparação gráfica entre modelo aditivo e multiplicativo",
        )
        + row(table)
    )


def content_medias_moveis() -> str:
    return (
        heading(4, "Suavização por Médias Móveis")
        + row(
            p(
                "As médias móveis são uma das técnicas mais simples e eficazes para suavizar uma "
                "série temporal. O objetivo é remover o ruído (flutuações de curto prazo) para tornar os "
                "componentes de tendência e ciclo mais visíveis (LATORRE; CARDOSO, 2001). O método "
                "consiste em substituir cada observação da série por uma média das observações ao "
                "seu redor. Por exemplo:"
            )
            + '<div class="list"><ul class="list-group">'
            + '<li class="list-group-item">Média móvel de 7 dias = média dos últimos 7 dias</li>'
            + '<li class="list-group-item">Média móvel de 14 dias = média dos últimos 14 dias</li>'
            + "</ul></div>"
            + p("Isso “suaviza” picos e quedas abruptas.")
        )
        + box(
            "Importante",
            "IMPORTANTE!",
            "Para dados mensais com sazonalidade, uma média móvel centrada "
            "de 12 termos é frequentemente usada para estimar a tendência, "
            "pois ao calcular a média de um período de 12 meses, as flutuações "
            "sazonais tendem a se cancelar (ZHANG et al., 2014).",
        )
        + figure_captioned(
            "figura2-medias-moveis.png",
            "Figura 2 – Exemplo de suavização por média móvel em uma série de casos de dengue",
            "Fonte: Elaborado pelo autor (2026).",
            "Gráfico de suavização por média móvel em casos de dengue",
        )
        + row(
            p(
                "A Figura 2 apresenta um gráfico de linhas que compara a série original de casos mensais "
                "de dengue (dados simulados) com a série suavizada por uma média móvel centrada "
                "de 12 meses."
            )
            + '<div class="list"><ul class="list-group">'
            + '<li class="list-group-item">A linha azul clara, mais irregular, representa os valores mensais observados. '
            "Ela apresenta fortes oscilações, com picos altos que se repetem anualmente, "
            "caracterizando a sazonalidade típica da dengue.</li>"
            + '<li class="list-group-item">A linha vermelha, mais suave e contínua, corresponde à média móvel de 12 meses, '
            "que elimina flutuações de curto prazo. Essa suavização evidencia o comportamento "
            "de tendência-ciclo da série: períodos de aumento e queda nos casos ao longo dos anos.</li>"
            + "</ul></div>"
            + p(
                "O gráfico mostra que, embora os valores mensais tenham grande variabilidade, a média "
                "móvel revela padrões mais estruturados, como ciclos epidêmicos e mudanças graduais ao "
                "longo do tempo."
            )
        )
        + subheading("Por que isso é importante na saúde pública?")
        + row(
            p(
                "Dados em saúde pública, como casos de doenças, internações ou mortes, costumam "
                "apresentar variações artificiais por vários motivos:"
            )
            + '<div class="list"><ul class="list-group">'
            + '<li class="list-group-item">Atrasos na notificação (ex: menos registros no fim de semana)</li>'
            + '<li class="list-group-item">Flutuações aleatórias</li>'
            + '<li class="list-group-item">Problemas administrativos ou de coleta</li>'
            + "</ul></div>"
            + p(
                "A média móvel ajuda a revelar a tendência real, reduzindo o “ruído” desses fatores.",
                mb0=True,
            )
        )
    )


def content_sti() -> str:
    return (
        heading(5, "Séries Temporais Interrompidas (STI)")
        + row(
            p(
                "A Análise de Séries Temporais Interrompidas (STI), ou Interrupted Time Series (ITS) analysis, "
                "é um dos desenhos de estudo quase-experimentais mais fortes para avaliar o impacto "
                "de intervenções em nível populacional (SCHIAVON et al., 2019) (SILVA et al., 2020). "
                "Este método é particularmente útil em saúde pública para responder a perguntas como: "
                '"A introdução de uma nova vacina reduziu a incidência da doença?"'
            )
            + p(
                "As séries temporais interrompidas são fundamentais na saúde pública porque permitem "
                "avaliar intervenções que não podem ser estudadas por ensaios clínicos randomizados. "
                "Esse método analisa como um indicador se comporta antes e depois de uma mudança "
                "específica, sendo útil para avaliar impactos de vacinas, políticas regulatórias e medidas "
                "adotadas em emergências sanitárias, como na pandemia de COVID-19."
            )
            + p(
                "Também é amplamente usado para examinar efeitos de mudanças na organização dos "
                "serviços de saúde e para apoiar a vigilância epidemiológica, ajudando a identificar surtos "
                "ou medir resultados de ações de controle."
            )
            + p(
                "Apesar de sua utilidade, a interpretação dos resultados exige cautela, pois outros eventos "
                "simultâneos podem influenciar as tendências. No conjunto, as séries temporais "
                "interrompidas transformam dados rotineiros em evidências robustas para planejar, "
                "monitorar e avaliar políticas e intervenções em saúde pública (WORLD HEALTH "
                "ORGANIZATION, 2010)."
            )
            + p(
                "O desenho da STI utiliza uma série de observações ao longo do tempo, coletadas antes e "
                "depois de uma intervenção em um ponto bem definido (a \"interrupção\"). A análise avalia "
                "se houve uma mudança estatisticamente significativa na série após a intervenção, testando "
                "duas possíveis mudanças:"
            )
        )
        + accordion(
            "m2a2-sti-mudancas",
            [
                (
                    "Mudança de Nível (efeito imediato):",
                    "<p class=\"mb-0\">Um salto ou queda imediata no valor da série logo após a intervenção.</p>",
                ),
                (
                    "Mudança de Tendência (efeito gradual):",
                    "<p class=\"mb-0\">Uma mudança na inclinação (aceleração ou desaceleração) da série após a intervenção.</p>",
                ),
            ],
        )
        + figure_captioned(
            "figura3-sti.png",
            "Figura 3 – Representação esquemática de uma Análise de Série Temporal Interrompida",
            "Fonte: Elaborado pelo autor (2026).",
            "Gráfico esquemático de série temporal interrompida",
        )
        + row(
            p(
                "A Figura 3 simula o impacto de uma intervenção (como a introdução de uma vacina) na taxa "
                "de mortalidade por uma doença. Os pontos representam os valores observados da taxa de "
                "mortalidade por 100.000 habitantes ao longo de aproximadamente 100 meses."
            )
            + p(
                "Antes da intervenção (à esquerda da linha vertical tracejada), a linha azul mostra que a "
                "taxa de mortalidade já apresentava uma tendência de queda gradual. Isso representa o "
                "comportamento esperado da série se nada tivesse mudado."
            )
            + p(
                "A linha vertical preta indica o ponto exato em que ocorreu a intervenção — por exemplo, "
                "o início de uma campanha de vacinação. É o marco que divide a série em período "
                "pré-intervenção e período pós-intervenção."
            )
            + p(
                "Imediatamente após, observa-se uma queda abrupta na taxa de mortalidade. Esse salto "
                "para baixo é chamado de mudança de nível, indicando um efeito imediato."
            )
            + p(
                "Após a intervenção, a linha vermelha mostra que a taxa de mortalidade continua caindo, "
                "mas agora com inclinação mais acentuada do que antes. Ou seja, além da queda imediata, "
                "a tendência se torna mais forte."
            )
            + p(
                "A diferença entre a inclinação pré-intervenção (azul) e pós-intervenção (vermelha) representa "
                "a mudança de tendência. Isso indica que a intervenção não só gerou um efeito imediato, "
                "mas também alterou o ritmo da redução ao longo do tempo. A grande vantagem da STI é "
                "sua capacidade de controlar a tendência pré-existente, tornando a inferência sobre o efeito "
                "da intervenção mais robusta (SCHIAVON et al., 2019) (SILVA et al., 2020).",
                mb0=True,
            )
        )
    )


def content_conclusao() -> str:
    return (
        heading(6, "Conclusão")
        + row(
            p(
                "Os modelos apresentados são a base para análises mais complexas. A decomposição nos "
                "ajuda a entender a estrutura da série, as médias móveis nos permitem visualizar a tendência "
                "de forma clara, e a STI nos fornece uma ferramenta robusta para a avaliação de impacto, uma "
                "das tarefas mais importantes em saúde pública.",
                mb0=True,
            )
        )
    )


def content_referencias() -> str:
    return (
        heading(7, "REFERÊNCIAS")
        + row(
            '<div class="referencias-aula">'
            '<p class="referencias-item">ANTUNES, José Leopoldo Ferreira; CARDOSO, Maria Regina Alves. '
            "Uso da análise de séries temporais em estudos epidemiológicos. "
            "<em>Epidemiologia e Serviços de Saúde</em>, v. 24, n. 3, p. 565-576, 2015.</p>"
            '<p class="referencias-item">LATORRE, Maria do Rosário Dias de Oliveira; CARDOSO, Maria Regina Alves. '
            "Análise de séries temporais em epidemiologia: uma introdução sobre os aspectos metodológicos. "
            "<em>Revista Brasileira de Epidemiologia</em>, v. 4, n. 3, p. 145-152, 2001.</p>"
            '<p class="referencias-item">SCHIAVON, J. P.; NOGUEIRA-DA-SILVA, G.; ABEBE, E. C. et al. '
            "Efetividade do serviço móvel de urgência (Samu): uso de séries temporais interrompidas. "
            "<em>Revista de Saúde Pública</em>, v. 53, p. 99, 2019.</p>"
            '<p class="referencias-item">SILVA, D. A. S.; MOURA, L.; SOUZA, M. R. et al. '
            "Mortalidade prematura por câncer de colo uterino: estudo de séries temporais interrompidas. "
            "<em>Revista de Saúde Pública</em>, v. 54, p. 139, 2020.</p>"
            '<p class="referencias-item">WORLD HEALTH ORGANIZATION. '
            "<em>Evaluation of public health interventions: a guide for practitioners</em>. "
            "Geneva: WHO, 2010.</p>"
            '<p class="referencias-item">ZHANG, X.; ZHANG, T.; YOUNG, A. A.; LI, X. '
            "Applications and comparisons of four time series models in epidemiological surveillance data. "
            "<em>PLoS One</em>, v. 9, n. 2, e88075, 2014.</p>"
            "</div>"
        )
    )


CONTENT_BUILDERS = [
    content_sobre,
    content_introducao,
    content_decomposicao,
    content_medias_moveis,
    content_sti,
    content_conclusao,
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

    media = ROOT / "media" / "modulo2" / "aula2"
    for junk in media.glob("_preview-page-*.png"):
        junk.unlink()
    for junk in media.glob("embedded-p*"):
        junk.unlink()


if __name__ == "__main__":
    main()
