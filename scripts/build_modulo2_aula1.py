#!/usr/bin/env python3
"""Gera HTML da Aula 2.1 (Análise Exploratória) a partir do PDF — sem alterar textos."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "modulo2" / "aula1"
MEDIA = "../../media/modulo2/aula1/"
ASSETS = "../../"

COURSE_TITLE = "Análise e Interpretação de Dados em Saúde"
MODULE_NUM = 2
MODULE_TITLE = "Séries Temporais"
AULA_LABEL = "Aula 1"
AULA_TITLE = "Análise Exploratória"

TOPICS = [
    "Sobre esta aula",
    "Introdução",
    "Análise Visual: o primeiro passo",
    "Os Componentes de uma série temporal",
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


def box_atencao(body: str) -> str:
    """Box ATENÇÃO com o layout diagonal do design system."""
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


def box_destaque(title: str, body: str) -> str:
    """Box escuro com padrão de quadrados (estilo do PDF)."""
    return row(
        f'<div class="card border-0 rounded overflow-hidden aos-init" data-aos="fade-up" '
        f'data-aos-easing="ease-out" data-aos-duration="600" '
        f'style="background-color:var(--fio-sys-color-primary-extra-dark);'
        f"background-image:url('{ASSETS}media/templates/fundo-flipcard.jpg');"
        f'background-size:cover;background-position:center;">'
        f'<div class="card-body p-4 p-md-5" style="color:#fff;">'
        f'<p style="color:#fff;"><strong style="color:#fff;">{title}</strong></p>'
        f'<p class="mb-0" style="color:#fff;">{body}</p>'
        f"</div></div>"
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
            p('Seja bem-vindo e bem-vinda à aula “Análise Exploratória”.')
            + p("A seguir, veja algumas informações importantes!")
        )
        + subheading("Objetivos de aprendizagem")
        + row(
            p("Ao final dessa aula, você será capaz de:")
            + '<div class="list"><ul class="list-group">'
            + '<li class="list-group-item">Compreender o que é uma série temporal e sua importância para a saúde pública;</li>'
            + '<li class="list-group-item">Realizar uma análise visual de uma série temporal utilizando gráficos de linhas;</li>'
            + '<li class="list-group-item">Identificar e interpretar os quatro componentes clássicos de uma série temporal: '
            "tendência, sazonalidade, ciclo e ruído;</li>"
            + '<li class="list-group-item">Reconhecer a importância da análise exploratória como passo fundamental para a '
            "modelagem de dados temporais em saúde.</li>"
            + "</ul></div>"
        )
        + subheading("Autoria")
        + row(
            p("<strong>Diego Ricardo Xavier</strong>")
            + p("Doutor em Epidemiologia. Mestrado em Saúde Pública. Pesquisador em Saúde Pública")
            + p(
                "Instituto de Comunicação e Informação Científica e Tecnológica em Saúde (Icict) da "
                "Fundação Oswaldo Cruz (Fiocruz)"
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
                "Uma série temporal, também conhecida como série histórica, é uma sequência de "
                "observações de uma variável, coletadas em intervalos de tempo regulares (dias, semanas, "
                "meses, anos) (LATORRE; CARDOSO, 2001)."
            )
            + p(
                "Em saúde pública, a análise de séries temporais é uma ferramenta poderosa para monitorar "
                "doenças, avaliar o impacto de intervenções e prever cenários futuros. Por exemplo, podemos "
                "analisar a série histórica de casos de dengue para entender seu comportamento ao longo "
                "dos anos e identificar períodos de maior risco (ANTUNES; CARDOSO, 2015)."
            )
        )
        + figure_plain("intro-tablet.png", "Pessoa analisando gráficos em um tablet")
        + row(
            p(
                "O primeiro passo em qualquer análise de série temporal é a análise exploratória. "
                "Esta etapa consiste em visualizar e descrever os dados para identificar suas principais "
                "características e padrões, o que guiará a escolha dos modelos estatísticos mais adequados "
                "em etapas posteriores (BRASIL, 2005).",
                mb0=True,
            )
        )
    )


def content_analise_visual() -> str:
    return (
        heading(3, "Análise Visual: o primeiro passo")
        + row(
            p(
                "A forma mais direta e intuitiva de iniciar a análise exploratória é através de gráficos. "
                "O gráfico de linhas é a principal ferramenta para visualizar uma série temporal, onde o "
                "eixo horizontal (X) representa o tempo e o eixo vertical (Y) representa os valores da variável "
                "observada (ANTUNES; CARDOSO, 2015)."
            )
        )
        + figure_captioned(
            "figura1-grafico-linhas.png",
            "Figura 1 – Exemplo de Gráfico de Linhas para uma Série Temporal.",
            "Fonte: Elaborado pelo autor (2026).",
            "Gráfico de linhas de série temporal de casos de dengue",
        )
        + subheading("Interpretando um Gráfico de Linhas")
        + row(
            p(
                "Ao observar um gráfico de linha de uma série temporal como o da Figura 1, podemos extrair "
                "informações valiosas:"
            )
        )
        + '<div class="row justify-content-center">'
        + '<div class="col-12 col-md-10 col-lg-8"><div class="row">'
        + flipcard(
            "m2a1fc-periodos",
            "Comparação entre Períodos:",
            "<p>É possível comparar o comportamento da variável em diferentes momentos. "
            "No gráfico, podemos ver que o número de casos em 2024 foi "
            "significativamente maior do que nos anos anteriores.</p>",
        )
        + flipcard(
            "m2a1fc-picos",
            "Identificação de Picos e Vales:",
            "<p>O gráfico revela os pontos de máximo (picos) e mínimo (vales) da série, que "
            "podem corresponder a epidemias, surtos ou períodos de baixa "
            "ocorrência de um evento. O pico em 2024 é claramente visível.</p>",
        )
        + flipcard(
            "m2a1fc-variacao",
            "Análise de Variação:",
            '<p>A "rugosidade" da linha indica a '
            "variabilidade dos dados. Uma linha muito irregular sugere alta variação "
            "de um período para o outro.</p>",
        )
        + "</div></div></div>\n"
        + box_atencao(
            "Um exemplo clássico é a análise da série histórica de mortalidade por doenças "
            "do aparelho circulatório, onde o gráfico de linhas pode revelar uma tendência "
            "de queda ao longo das décadas, mas com picos de mortalidade nos meses "
            "de inverno de cada ano (ANTUNES; CARDOSO, 2015)."
        )
    )


def content_componentes() -> str:
    table = (
        '<div class="table-responsive"><table class="table table-sm table-bordered align-middle mb-0">'
        "<thead><tr>"
        "<th scope=\"col\">Componente</th>"
        "<th scope=\"col\">Descrição</th>"
        "<th scope=\"col\">Exemplo em Saúde Pública</th>"
        "</tr></thead><tbody>"
        "<tr><td><strong>Tendência (T)</strong></td>"
        "<td>Movimento de longa duração da série, representando o aumento, a diminuição ou a "
        "estabilidade da variável ao longo de todo o período observado.</td>"
        "<td>A tendência de queda da mortalidade infantil no Brasil nas últimas décadas; a "
        "tendência de aumento da prevalência de obesidade.</td></tr>"
        "<tr><td><strong>Sazonalidade (S)</strong></td>"
        "<td>Flutuações periódicas que se repetem em intervalos fixos e conhecidos de tempo, "
        "geralmente dentro de um ano (meses, trimestres).</td>"
        "<td>O aumento de casos de doenças respiratórias no inverno; o pico de acidentes "
        "com animais peçonhentos no verão.</td></tr>"
        "<tr><td><strong>Ciclo (C)</strong></td>"
        "<td>Flutuações periódicas com duração variável, geralmente superior a um ano, que não "
        "possuem um intervalo fixo de repetição. Estão frequentemente associadas a ciclos "
        "econômicos ou ambientais mais amplos.</td>"
        "<td>Ciclos de epidemias de dengue que ocorrem a cada 3-5 anos, relacionados a "
        "fatores como a introdução de novos sorotipos virais e flutuações na imunidade "
        "da população.</td></tr>"
        "<tr><td><strong>Ruído (R)</strong></td>"
        "<td>Também chamado de componente aleatório ou irregular, representa as variações "
        "na série que não podem ser explicadas pelos outros três componentes. "
        "É o resíduo que sobra após a remoção da tendência, sazonalidade e ciclo.</td>"
        "<td>Variações diárias no número de atendimentos em uma emergência que "
        "não seguem um padrão previsível.</td></tr>"
        "</tbody></table></div>"
    )
    return (
        heading(4, "Os Componentes de uma série temporal")
        + row(
            p(
                "Uma série temporal pode ser decomposta em quatro componentes principais que, juntos, "
                "explicam o comportamento da variável ao longo do tempo. A análise exploratória busca "
                "identificar a presença e a força de cada um desses componentes (LATORRE; CARDOSO, "
                "2001) (BRASIL, 2005). A Figura 2 ilustra esquematicamente cada um deles."
            )
        )
        + figure_captioned(
            "figura2-componentes.png",
            "Figura 2 – Representação esquemática dos quatro componentes de uma série temporal.",
            "Fonte: Elaborado pelo autor (2026).",
            "Quatro gráficos esquemáticos: tendência, sazonalidade, ciclo e ruído",
        )
        + row(table)
        + figure_captioned(
            "figura3-decomposicao.png",
            "Figura 3 – Exemplo de decomposição de uma série temporal de casos de dengue.",
            "Fonte: Elaborado pelo autor (2026).",
            "Decomposição de série temporal de casos de dengue",
        )
        + box_destaque(
            "Como cada componente ajuda a explicar o comportamento geral da "
            "série de casos de dengue?",
            "Note como a soma da tendência, sazonalidade e ruído reconstrói a série "
            "original observada. Cada componente da série temporal contribui para explicar "
            "o comportamento dos casos de dengue ao longo do tempo. A tendência "
            "mostra o aumento gradual dos casos, indicando um crescimento estrutural. "
            "A sazonalidade revela o padrão anual recorrente, com oscilações semelhantes "
            "a cada ciclo. O ruído representa variações imprevisíveis decorrentes de fatores "
            "pontuais. Quando somados a tendência + sazonalidade + ruído esses "
            "componentes reconstroem a série observada, explicando seus picos, vales "
            "e irregularidades de forma integrada.",
        )
        + subheading("Cronologia: a ordem importa")
        + row(
            p(
                "A cronologia é a própria essência da série temporal: a ordem sequencial das observações. "
                "A dependência entre uma observação e as anteriores é uma característica fundamental. "
                "A análise busca entender como o valor de hoje se relaciona com o valor de ontem, da "
                "semana passada ou do ano passado. Essa dependência temporal é o que diferencia a análise "
                "de séries temporais de outras análises estatísticas (LATORRE; CARDOSO, 2001)."
            )
        )
        + subheading("Tendência: a direção geral")
        + row(
            p(
                "A tendência é o componente mais suave da série. Ela pode ser identificada visualmente "
                "no gráfico de linhas como a direção geral da série, como a clara tendência de queda na "
                "mortalidade infantil (Figura 4). Matematicamente, pode ser estimada ajustando-se uma "
                "reta (regressão linear) ou uma curva aos dados. A identificação correta da tendência é "
                "crucial, pois ela representa a mudança estrutural de longo prazo no fenômeno estudado "
                "(ANTUNES; CARDOSO, 2015)."
            )
        )
        + figure_captioned(
            "figura4-mortalidade.png",
            "Figura 4 – Exemplo de Tendência de Queda na Taxa de Mortalidade Infantil.",
            "Fonte: Elaborado pelo autor (2026), com base em dados do IBGE/ONU.",
            "Gráfico de tendência de queda na taxa de mortalidade infantil",
        )
        + subheading("Sazonalidade: o padrão anual")
        + row(
            p(
                "A sazonalidade é um padrão previsível que se repete a cada ano. Para identificá-la, podemos "
                "usar gráficos específicos, como o gráfico sazonal (ou de perfil), que sobrepõe os dados de "
                "cada ano em um único gráfico (de janeiro a dezembro). Se as linhas de cada ano tiverem um "
                "formato semelhante, como na Figura 5, há forte evidência de sazonalidade (BRASIL, 2005)."
            )
        )
        + figure_captioned(
            "figura5-sazonal.png",
            "Figura 5 – Gráfico Sazonal para Casos de Dengue",
            "Fonte: Elaborado pelo autor (2026).",
            "Gráfico sazonal de casos de dengue com sobreposição de anos",
        )
        + subheading("Ciclos: as ondas de longo prazo")
        + row(
            p(
                "Os ciclos são mais difíceis de identificar do que a sazonalidade, pois não têm um período fixo. "
                "Eles representam oscilações de mais longo prazo. Em saúde pública, os ciclos epidêmicos de "
                "doenças como sarampo ou coqueluche antes da vacinação em massa são exemplos clássicos. "
                "A identificação de ciclos geralmente requer séries históricas longas e métodos estatísticos "
                "mais avançados (ANTUNES; CARDOSO, 2015)."
            )
        )
        + subheading("Ruído: o imprevisível")
        + row(
            p(
                'O ruído é, por definição, imprevisível. Em um modelo ideal, o ruído deve ser puramente '
                'aleatório, sem padrões, como visto no painel "Ruído" da Figura 3. Se, após a modelagem, '
                "o ruído (resíduo) ainda apresentar algum padrão (como autocorrelação), isso indica que "
                "o modelo não capturou toda a estrutura dos dados e precisa ser refinado "
                "(LATORRE; CARDOSO, 2001)."
            )
        )
        + subheading("Conclusão")
        + row(
            p(
                "A análise exploratória é um passo investigativo essencial. Ao visualizar os dados e identificar "
                "a tendência, a sazonalidade, os ciclos e o ruído, o analista de saúde ganha uma compreensão "
                "profunda do comportamento do evento de saúde ao longo do tempo, o que é fundamental "
                "para a etapa seguinte de modelagem e previsão.",
                mb0=True,
            )
        )
    )


def content_referencias() -> str:
    return (
        heading(5, "REFERÊNCIAS")
        + row(
            '<div class="referencias-aula">'
            '<p class="referencias-item">ANTUNES, José Leopoldo Ferreira; CARDOSO, Maria Regina Alves. '
            "Uso da análise de séries temporais em estudos epidemiológicos. "
            "<em>Epidemiologia e Serviços de Saúde</em>, Brasília, v. 24, n. 3, p. 565-576, jul./set. 2015.</p>"
            '<p class="referencias-item">BRASIL. Ministério da Saúde. Secretaria de Vigilância em Saúde. '
            "<strong>Análise de situação de saúde</strong>. Brasília: Ministério da Saúde, 2005. v. 1.</p>"
            '<p class="referencias-item">LATORRE, Maria do Rosário Dias de Oliveira; CARDOSO, Maria Regina Alves. '
            "Análise de séries temporais em epidemiologia: uma introdução sobre os aspectos metodológicos. "
            "<em>Revista Brasileira de Epidemiologia</em>, São Paulo, v. 4, n. 3, p. 145-152, 2001.</p>"
            "</div>"
        )
    )


CONTENT_BUILDERS = [
    content_sobre,
    content_introducao,
    content_analise_visual,
    content_componentes,
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

    media = ROOT / "media" / "modulo2" / "aula1"
    for junk in media.glob("_preview-page-*.png"):
        junk.unlink()
    for junk in media.glob("embedded-p*"):
        junk.unlink()


if __name__ == "__main__":
    main()
