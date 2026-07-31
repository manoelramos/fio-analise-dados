#!/usr/bin/env python3
"""Gera HTML da Aula 1.3 (Estatística Avançada) a partir do PDF validado — sem alterar textos."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "modulo1" / "aula3"
MEDIA = "../../media/modulo1/aula3/"
ASSETS = "../../"

COURSE_TITLE = "Análise e Interpretação de Dados em Saúde"
MODULE_NUM = 1
MODULE_TITLE = "Estatística"
AULA_LABEL = "Aula 3"
AULA_TITLE = "Estatística Avançada"

TOPICS = [
    "Sobre esta aula",
    "Introdução",
    "Inferência Estatística",
    "Intervalo de confiança",
    "Modelos de Regressão",
    "REFERÊNCIA",
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


def formula(src: str, alt: str = "", *, wide: bool = False) -> str:
    cls = "img-fluid img-formula"
    if wide:
        cls += " img-formula--wide"
    return row(
        f'<figure class="text-center my-3 formula-figure">'
        f'<img class="{cls}" src="{MEDIA}{src}" alt="{alt}" loading="lazy" />'
        f"</figure>",
        "mb-4",
    )


def figure_captioned(src: str, caption: str, fonte: str, alt: str = "") -> str:
    return row(
        f'<p class="mb-2"><strong>{caption}</strong></p>'
        f'<figure class="lightbox aos-init" data-aos="fade-up" data-aos-easing="ease-out" data-aos-duration="600">'
        f'<img class="img-fluid mx-auto d-block mb-3 rounded border" src="{MEDIA}{src}" alt="{alt}" loading="lazy" />'
        f"</figure>"
        f'<p class="figure-caption fonte small mb-0">{fonte}</p>'
    )


def box(kind: str, label: str, body: str) -> str:
    return row(
        f'<div class="box" data-box="{kind}"><div class="card"><div class="card-header">'
        f'<span class="icone material-symbols-rounded" aria-hidden="true"></span>'
        f'<span class="label">{label}</span></div><div class="card-body">'
        f'<p class="mb-0">{body}</p></div></div></div>'
    )


def saiba_mais_toggle(collapse_id: str, label: str, body: str) -> str:
    """Saiba Mais interativo: botão primeiro; conteúdo só após o clique."""
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
        f'<div class="mt-3 collapse" id="{collapse_id}">'
        f'<p class="mb-0">{body}</p>'
        f"</div></div></div></div>"
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
            '<a class="fio-button fio-button-primary" href="../../modulo2/aula1/topico1.html" rel="next">'
            'Próximo módulo <span class="material-symbols-rounded" aria-hidden="true">east</span></a>'
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
            p('Seja bem-vindo e bem-vinda à aula “Estatística Avançada”.')
            + p("A seguir, veja algumas informações importantes!")
        )
        + subheading("Objetivos de aprendizagem")
        + row(
            p("Ao final dessa aula, você será capaz de:")
            + '<div class="list"><ul class="list-group">'
            + '<li class="list-group-item">Compreender sobre Estatística Inferencial</li>'
            + '<li class="list-group-item">Entender o conceito de Intervalo de confiança</li>'
            + '<li class="list-group-item">Apreender os conceitos de regressão linear e de regressão logística</li>'
            + "</ul></div>"
        )
        + subheading("Autoria")
        + row(
            p("<strong>Carla Lourenço Tavares de Andrade.</strong>")
            + p(
                "Estatístico. Escola Nacional de Saúde Pública Sergio Arouca (ENSP) da Fundação Oswaldo Cruz.",
                mb0=True,
            )
        )
    )


def content_introducao() -> str:
    return (
        heading(2, "Introdução")
        + row(
            p(
                "Nessa aula sobre inferência estatística e modelos de regressão, é importante frisar que "
                "ela será mais informativa do que mostrar como fazer. Requereríamos duas disciplinas de um "
                "semestre cada para aprofundarmos esse conteúdo. A ideia aqui é mostrar por meio de artigos "
                "científicos o ‘caminho das pedras’. Então, vamos lá!",
                mb0=True,
            )
        )
    )


def content_inferencia() -> str:
    return (
        heading(3, "Inferência Estatística")
        + row(
            p(
                "A inferência estatística parte do pressuposto que temos uma amostra, de preferência "
                "aleatória, da população. Por quê? Quando a população que desejamos estudar é muito "
                "grande, de difícil acesso a todas as unidades de observação (por exemplo, todas as pessoas "
                "do Brasil), selecionamos uma amostra dessa população. A partir dessa amostra que fazemos "
                "inferência para a população com base na teoria das probabilidades."
            )
            + p(
                "Então, a inferência estatística é um conjunto de técnicas que permitem fazer afirmações "
                "(extrapolações) sobre características de uma população tomando como base os resultados "
                "observados na amostra (figura 1)."
            )
        )
        + figure_captioned(
            "figura1-inferencia.png",
            "Figura 1: Ilustração sobre inferência estatística.",
            "Fonte: Adaptado de Barbetta (2002).",
            "Ilustração sobre inferência estatística: população e amostra",
        )
        + row(
            p(
                "Relembrando os conceitos apresentados na aula sobre análise exploratória, população é o "
                "conjunto de indivíduos (observações), tendo pelo menos uma variável em comum e, amostra "
                "é qualquer subconjunto dessa população."
            )
            + p(
                "Adicionalmente, temos mais três conceitos importantes: parâmetro, estimador e estimativa."
            )
        )
        + '<div class="row justify-content-center">'
        + '<div class="col-12 col-md-10 col-lg-8"><div class="row">'
        + flipcard(
            "flip-parametro",
            "Parâmetro",
            "<p>É uma medida usada para descrever uma característica da população.</p>",
        )
        + flipcard(
            "flip-estimador",
            "Estimador",
            "<p>O estimador de um parâmetro populacional é uma variável aleatória, que é função dos "
            "elementos amostrais.</p>",
        )
        + flipcard(
            "flip-estimativa",
            "Estimativa",
            "<p>É o valor numérico obtido pelo estimador (ou estatística) em uma certa amostra.</p>",
        )
        + "</div></div></div>\n"
        + row(
            p(
                "Em referência à figura 1, os eleitores brasileiros com 16 anos ou mais formam a população. "
                "Para realizar uma pesquisa com todos os eleitores brasileiros ficaria inviável. Então, nesse "
                "caso, faz sentido selecionar uma amostra dessa população. Poderíamos estar interessados "
                "em saber, por exemplo, a média de idade dos eleitores. Assim, o parâmetro é a média "
                "populacional e estimativa é a média na amostra.",
                mb0=True,
            )
        )
    )


def content_intervalo() -> str:
    return (
        heading(4, "Intervalo de confiança")
        + row(
            p(
                "A estimação é o processo que usa os resultados extraídos da amostra para produzir "
                "inferências sobre a população da qual a amostra foi extraída aleatoriamente."
            )
            + p(
                "A estimação pode ocorrer de forma pontual ou intervalar. Voltando ao exemplo, a estimativa "
                "pontual é a média calculada na amostra e a intervalar, é o intervalo de confiança para a "
                "média populacional de eleitores brasileiros."
            )
            + p(
                "Um intervalo de confiança incorpora à estimativa pontual do parâmetro informações "
                "a respeito de sua variabilidade e o grau de confiança associado à essa estimativa."
            )
            + p(
                "A estimação por intervalo de confiança consiste no estabelecimento de limites inferior "
                "e superior para o parâmetro que se deseja estimar."
            )
            + p(
                "Necessário, portanto, associar um grau de “risco (ou erro)” denominado nível de "
                "significância, que é uma probabilidade (variando entre zero e um). Assim, a precisão "
                "esperada do intervalo de confiança é obtida pelo complementar do nível de significância, "
                "que é o grau de confiança (um menos o nível de significância)."
            )
            + p(
                "Dizemos que o intervalo tem, por exemplo, 95% de confiança de conter o verdadeiro "
                "valor da média populacional, ou seja, estamos 95% confiantes de que esse intervalo "
                "contenha a média verdadeira. E não que a média tem 95% de chance ou probabilidade "
                "de estar no intervalo."
            )
            + p(
                "No caso da média populacional, o intervalo de confiança é calculado da seguinte maneira."
            )
        )
        + formula("formula-ic-definicao.png", "Fórmula do intervalo de confiança", wide=True)
        + saiba_mais_toggle(
            "saiba-mais-ic",
            "SAIBA MAIS!",
            "Para mais informações sobre o cálculo do intervalo de confiança consultar, "
            "por exemplo, o livro do Barbetta (2002) ou qualquer outro livro de Estatística "
            "que contemple esse conteúdo",
        )
        + row(
            p("Vejamos um exemplo sobre intervalo de confiança.")
            + p(
                "Considere uma amostra de 10 bebês selecionada de uma população de bebês que recebe "
                "antiácidos com presença de alumínio, que são usados frequentemente para tratar distúrbios "
                "digestivos. O nível médio de alumínio no plasma para a amostra dos 10 bebês é 37,2 μg/l "
                "e o desvio-padrão é 7,13 μg/l. Calcule um intervalo com 95% de confiança para a média "
                "populacional."
            )
        )
        + formula("formula-ic-exemplo.png", "Fórmula do intervalo de confiança para o exemplo", wide=True)
        + row(
            p(
                "Como grau de confiança de 95% temos que o nível de significância é de 5% (100% - 95%)."
            )
        )
        + formula("valores-ic-exemplo.png", "Valores do exemplo de intervalo de confiança", wide=True)
        + row(
            p(
                "Então, o intervalo de confiança para a média do nível de alumínio nos 10 bebês é:"
            )
        )
        + formula("calculo-ic-exemplo.png", "Cálculo do intervalo de confiança", wide=True)
        + row(
            p(
                "Dizemos que estamos 95% confiantes de que a média populacional (concentração de "
                "alumínio no plasma em bebês) pertence ao intervalo [32,1; 42,3].",
                mb0=True,
            )
        )
    )


def content_regressao() -> str:
    return (
        heading(5, "Modelos de Regressão")
        + row(
            p(
                "Análise de regressão é uma metodologia estatística que utiliza a relação entre duas ou mais "
                "variáveis quantitativas (ou qualitativas) de tal forma que uma variável pode ser predita a "
                "partir da outra ou outras."
            )
            + p(
                "Outra forma de apresentação gráfica de duas variáveis quantitativas é por meio do diagrama "
                "de dispersão. É uma representação gráfica feita no mesmo sistema de coordenadas, em que "
                "uma das variáveis é colocada no eixo x e outra no eixo y."
            )
            + p(
                "O gráfico de dispersão é utilizado para interpretar o relacionamento entre duas variáveis "
                "(direção, forma e intensidade do relacionamento)."
            )
            + p(
                "Podemos identificar uma relação entre as variáveis dispostas no gráfico. A essa possível "
                "relação é chamada de correlação, que é a medida do grau de associação ou relação linear entre "
                "duas variáveis aleatórias contínuas."
            )
            + p(
                "O fato de duas variáveis apresentarem-se associadas não implica, necessariamente, que "
                "existe uma relação causa entre elas."
            )
        )
        + box("Importante", "IMPORTANTE!", "Uma correlação mostra uma tendência!")
        + row(
            p(
                "Em modelagem estatística estamos interessados em aprender quais variáveis explicativas "
                "ou independentes estão associadas (ou ajudam a explicar) uma variável de interesse, "
                "que é a variável resposta ou dependente. Esse relacionamento pode ser por uma função "
                "linear ou não."
            )
            + p(
                "Por exemplo, se estamos interessados em explicar a variável peso do recém-nascido "
                "(variável dependente) possíveis variáveis independentes seriam a idade da mãe (em anos), "
                "se fez pré-natal, renda da família, idade gestacional (em semanas), escolaridade da mãe "
                "(sem instrução, ensino fundamental, ensino médio, superior) etc."
            )
            + p(
                "Observe que a variável dependente é uma variável quantitativa contínua, que é necessário "
                "para que usemos um modelo de regressão linear. Nesse caso, as variáveis independentes "
                "podem ser quantitativas (idade da mãe (em anos), renda da família, idade gestacional "
                "(em semanas)) ou qualitativas (se fez pré-natal (sim ou não), escolaridade da mãe "
                "(sem instrução, ensino fundamental, ensino médio, superior))."
            )
            + p(
                "Quando a variável dependente é qualitativa nominal com duas categorias (dicotômica) "
                "a regressão linear não é mais adequada. Com o mesmo intuito de explicar uma variável "
                "(dependente) em função de outra(s), para esse caso especificamente, usamos, então "
                "uma regressão logística. As variáveis independentes podem ser quantitativas ou "
                "qualitativas, igual forma."
            )
            + p(
                "Por exemplo, podemos estar interessados na relação entre idade e doença cardíaca "
                "(ter ou não). Queremos entender a presença da doença cardíaca (variável dependente) em "
                "função da idade dos pacientes (variável independente)."
            )
            + p(
                "Como informado no início desta aula, precisaríamos de muito mais tempo e conteúdo para "
                "aplicarmos esses conceitos. Deixo com vocês, então, três exemplos de artigos, dentre muitos, "
                "publicados nos Cadernos de Saúde Pública que abordam o que vimos aqui e até outros "
                "conceitos."
            )
            + p("<strong>Artigos:</strong>")
            + '<div class="list"><ul class="list-group">'
            + '<li class="list-group-item"><a href="https://doi.org/10.1590/S0102-311X2006000200009" '
            'target="_blank" rel="noopener noreferrer">Fatores associados ao uso de preservativo masculino e ao '
            "conhecimento sobre DST/AIDS em adolescentes de escolas públicas e privadas do Município de "
            "São Paulo, Brasil</a></li>"
            + '<li class="list-group-item"><a href="https://doi.org/10.1590/S0102-311X2004000700010" '
            'target="_blank" rel="noopener noreferrer">Estudo de validação das informações de peso e estatura em '
            "gestantes atendidas em maternidades municipais no Rio de Janeiro, Brasil</a></li>"
            + '<li class="list-group-item"><a href="https://doi.org/10.1590/S0102-311X2007000800015" '
            'target="_blank" rel="noopener noreferrer">Vitalidade do recém-nascido por tipo de parto no Estado de '
            "São Paulo, Brasil</a></li>"
            + "</ul></div>"
        )
    )


def content_referencias() -> str:
    return (
        heading(6, "REFERÊNCIA")
        + row(
            '<div class="referencias-aula">'
            '<p class="referencias-item">Barbetta, Pedro A. <strong>Estatística aplicada às Ciências Sociais</strong>. '
            "Florianópolis: Ed. da UFSC, 2002.</p>"
            "</div>"
        )
    )


CONTENT_BUILDERS = [
    content_sobre,
    content_introducao,
    content_inferencia,
    content_intervalo,
    content_regressao,
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

    media = ROOT / "media" / "modulo1" / "aula3"
    for junk in media.glob("_preview-page-*.png"):
        junk.unlink()
    for junk in media.glob("embedded-p*"):
        junk.unlink()


if __name__ == "__main__":
    main()
