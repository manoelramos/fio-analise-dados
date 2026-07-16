#!/usr/bin/env python3
"""Gera HTML da Aula 1.2 (Estatística Básica) a partir do PDF validado — sem alterar textos."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "modulo1" / "aula2"
MEDIA = "../../media/modulo1/aula2/"
ASSETS = "../../"

COURSE_TITLE = "Análise e Interpretação de Dados em Saúde"
MODULE_NUM = 1
MODULE_TITLE = "Estatística"
AULA_LABEL = "Aula 2"
AULA_TITLE = "Estatística Básica"

TOPICS = [
    "Sobre esta aula",
    "Introdução",
    "Medidas de tendência central",
    "Medidas de dispersão ou de variabilidade",
    "Referências",
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
        f"<p class=\"mb-2\"><strong>{caption}</strong></p>"
        f'<figure class="lightbox aos-init" data-aos="fade-up" data-aos-easing="ease-out" data-aos-duration="600">'
        f'<img class="img-fluid mx-auto d-block mb-3 rounded border" src="{MEDIA}{src}" alt="{alt}" loading="lazy" />'
        f"</figure>"
        f'<p class="figure-caption fonte small mb-0">{fonte}</p>'
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
								<img class="img-fluid regua-logos" src="{ASSETS}media/logos/regua-de-logos.png" alt="Régua de logos: Campus Virtual Fiocruz, Fiocruz, SUS Digital, SUS 35 Anos, Ministério da Saúde e Governo do Brasil" />
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
            p('Seja bem-vindo e bem-vinda à aula “Estatística Básica”.')
            + p("A seguir, veja algumas informações importantes!")
        )
        + subheading("Objetivos de aprendizagem")
        + row(
            p("Ao final dessa aula, você será capaz de:")
            + '<div class="list"><ul class="list-group">'
            + '<li class="list-group-item">Conhecer o conceito de medidas descritivas e utilização</li>'
            + '<li class="list-group-item">Conhecer o conceito de medidas de tendência central</li>'
            + '<li class="list-group-item">Compreender as medidas de variabilidade</li>'
            + '<li class="list-group-item">Compreender o conceito de percentis</li>'
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
                "Nesta aula, como continuação da sobre análise exploratória dos dados, vamos aprender "
                "como calcular as medidas descritivas e entender para que servem. Vale ressaltar que "
                "todos os cálculos a seguir referem-se à amostra."
            )
            + p(
                "Bem, outra forma de trabalhar com os dados é calcular medidas que sejam sintéticas "
                "e de fácil entendimento. Pensando em um conjunto de dados com muitas variáveis "
                "e observações fica praticamente impossível interpretar os dados sem a ajuda de alguns "
                "recursos. Quando as variáveis são quantitativas, sejam discretas ou contínuas, podemos "
                "calcular as medidas descritivas, que se dividem em medidas de tendência central "
                "e de variabilidade."
            )
        )
        + row(
            f'<figure class="lightbox aos-init" data-aos="fade-up" data-aos-easing="ease-out" data-aos-duration="600">'
            f'<img class="img-fluid mx-auto d-block mb-3 rounded" src="{MEDIA}intro-dados.jpeg" '
            f'alt="Pessoa analisando gráficos em um notebook" loading="lazy" /></figure>'
        )
        + row(
            p(
                "As medidas de tendência central que têm por objetivo caracterizar o conjunto de dados por "
                "valores que representem todos os outros valores da amostra ou população. É uma forma de "
                "resumir o conjunto de dados em um único valor, como média, mediana e moda."
            )
            + p(
                "Além da informação do valor representativo do conjunto de valores da amostra (medidas de "
                "tendência central), é importante expressar a variabilidade desses valores em relação a uma "
                "determinada referência como amplitude, variância, desvio padrão e coeficiente de variação."
            )
            + p(
                "Como aplicação para o cálculo das medidas descritivas vamos retomar o conjunto de dados "
                "fictícios da aula sobre análise exploratória dos dados, dos empregados de uma empresa. "
                "Nesse conjunto de dados temos três variáveis quantitativas: número de filhos, salário "
                "(expresso como fração do salário-mínimo) e a idade (medida em anos e meses).",
                mb0=True,
            )
        )
    )


def content_tendencia() -> str:
    return (
        heading(3, "Medidas de tendência central")
        + subheading("Média", "h5")
        + row(
            p(
                "Leva em conta todos os n elementos da amostra. Para seu cálculo somamos todos os "
                "valores e dividimos pelo total de observações na amostra."
            )
            + p("Estatisticamente, podemos representar o cálculo da média como:")
        )
        + formula("formula-media.png", "Fórmula da média")
        + row(
            p(
                "Vejamos um exemplo com a variável salário. Somamos todas as 36 observações e dividimos "
                "por 36. Temos que a média é igual a"
            )
        )
        + formula("formula-media-salario.png", "Cálculo da média de salário", wide=True)
        + row(p("Significa que a média de salário dessa empresa é de 11,12 salários-mínimos."))
        + subheading("Mediana", "h5")
        + row(
            p(
                "É o valor que divide a distribuição ao meio. Então, 50% das observações estão abaixo "
                "desse valor e 50% estão acima. A mediana é uma medida robusta, pois é menos sensível "
                "a valores atípicos."
            )
            + p(
                "Para o cálculo da mediana é preciso ordenar do menor para o maior valor os dados "
                "da variável."
            )
            + p("A posição da mediana é dada pelo elemento de ordem:")
        )
        + formula("formula-mediana-impar.png", "Posição da mediana para n ímpar")
        + row(p("se o tamanho da amostra (n) for um número ímpar e, pelo elemento de ordem"))
        + formula("formula-mediana-par.png", "Posição da mediana para n par")
        + row(
            p("quando o tamanho da amostra for um número par.")
            + p(
                "Assim, considerando a nossa variável salário (com 36 observações – número par), "
                "a mediana é dada por"
            )
        )
        + formula("formula-mediana-par.png", "Posição da mediana para n par")
        + row(p("que é igual a:"))
        + formula("formula-mediana-exemplo-posicao.png", "Cálculo da posição da mediana")
        + row(
            p(
                "Com a ordenação dos valores, temos que a mediana é igual a média das posições 18 e 19. "
                "Assim,"
            )
            + p("Posição 18 = 9,80;")
            + p("Posição 19 = 10,53")
        )
        + formula("formula-mediana-exemplo-valor.png", "Cálculo do valor da mediana")
        + row(
            p(
                "Logo, podemos dizer que 50% dos valores estão abaixo de 10,16 e 50% estão acima "
                "desse valor."
            )
            + p(
                "Importante ressaltar que quando estamos em face de um conjunto de dados devemos, "
                "sempre, calcular a média, a mediana e outras medidas que ainda vamos aprender aqui. "
                "Porém, é fato que é mais comum usarmos a média em detrimento da mediana. Por quê? "
                "Talvez porque seja mais simples de calcular a média do que a mediana."
            )
            + p(
                "Outro ponto que merece atenção é que quando temos distribuições simétricas tanto "
                "faz usarmos uma ou outra (pois serão aproximadamente iguais), mas se a distribuição "
                "por assimétrica (à direita ou à esquerda) é recomendado que se use a mediana, "
                "por ser uma medida mais robusta."
            )
        )
        + subheading("Moda", "h5")
        + row(
            p(
                "É o valor mais frequente da variável. Pode ser que uma variável tenha mais de uma moda "
                "ou, até mesmo, não ter moda (amodal)."
            )
            + p("A variável salário, por exemplo, é amodal.", mb0=True)
        )
    )


def content_dispersao() -> str:
    return (
        heading(4, "Medidas de dispersão ou de variabilidade")
        + subheading("Amplitude total", "h5")
        + row(
            p(
                "É a diferença entre o valor máximo e o valor mínimo da variável. É uma medida que não "
                "demanda cálculo, mas é muito ‘grosseira’, pouco sensível."
            )
            + '<p class="text-center"><strong>Amplitude = maior valor – menor valor</strong></p>'
            + p(
                "Vamos continuar com a nossa variável salário-mínimo dos 36 funcionários. O menor valor "
                "(ou valor mínimo) é 4,00 e, o valor máximo é 23,30."
            )
            + p("Assim, a amplitude é a diferença do valor máximo e do valor mínimo.")
            + '<p class="text-center"><strong>Amplitude = 23,30 – 4,00 = 19,3</strong></p>'
            + p(
                "O salário-mínimo, no caso dos funcionários, tem uma amplitude (uma variação) "
                "de 19,3 salários-mínimos."
            )
        )
        + subheading("Variância", "h5")
        + row(
            p(
                "Mede a variabilidade em relação à média. Calcula-se com o somatório da diferença entre cada "
                "observação e a média elevado ao quadrado dividido pelo tamanho da amostra menos um."
            )
        )
        + formula("formula-variancia.png", "Fórmula da variância")
        + subheading("Desvio-padrão", "h5")
        + row(p("O desvio padrão é a raiz quadrada da variância."))
        + formula("formula-desvio-padrao.png", "Fórmula do desvio-padrão")
        + row(
            p(
                "Vamos alterar o nosso exemplo para os dados de pressão arterial sistólica (em mmHg) de "
                "sete observações (dados fictícios) para calcular a variância e o desvio padrão dessa variável. "
                "Primeiro, calcula-se a média e, em seguida calculamos a diferença entre cada observação "
                "em relação à média. Para que o somatório dessas diferenças não seja nulo elevaremos ao "
                "quadrado cada diferença, dessa forma:"
            )
        )
        + formula("tabela-pas-variancia.png", "Tabela e cálculos da pressão arterial sistólica", wide=True)
        + row(
            p(
                "Logo, a média de pressão arterial sistólica nessa amostra é de 130,14 mmHg, variância "
                "de 40 mmHg2 e desvio-padrão de 6,34 mmHg."
            )
        )
        + subheading("Coeficiente de variação", "h5")
        + row(
            p(
                "É uma medida que expressa a variabilidade sem a influência da ordem de grandeza da "
                "variável, ou seja, é uma medida adimensional. Quanto menor é esse valor (próximo de zero) "
                "em um conjunto de dados menor é a sua variabilidade. Também pode ser expresso em "
                "percentual. Para calcular o coeficiente de variação divide-se o desvio padrão da variável pela "
                "sua média multiplicando-se por 100."
            )
        )
        + formula("formula-cv.png", "Fórmula do coeficiente de variação")
        + row(
            p(
                "No exemplo anterior da pressão arterial sistólica a média é 130,14 mmHg e o desvio padrão "
                "é 6,34."
            )
        )
        + formula("formula-cv-exemplo.png", "Cálculo do coeficiente de variação", wide=True)
        + row(
            p(
                "O coeficiente de variação é igual a 4,87% indicando uma baixa variabilidade dos dados (valor "
                "próximo de zero)."
            )
        )
        + subheading("Percentis", "h5")
        + row(
            p(
                "O percentil de ordem k (onde k é qualquer valor entre 0 e 100), denotado por Pk, é o valor tal "
                "que k% dos valores da variável são menores ou iguais a ele."
            )
            + p(
                "Assim, se quisermos calcular os quartis, que são medidas bem conhecidas, podemos "
                "calcular os percentis 25 (P25 = primeiro quartil = Q1), 50 (P50 = mediana = Q2) e 75 (P75 = "
                "terceiro quartil = Q3)."
            )
            + p(
                "Outro percentil importante é o decil (P10, P20, P30, ... , P90). Uma aplicação prática do uso "
                "dos decis é o cálculo de um indicador desigualdade de renda é a razão entre os 10% mais "
                "ricos (P90) e os 10% mais pobres (P10)."
            )
            + p(
                "Para calcular os percentis podemos seguir como apontado em Triola (2008) por meio da "
                "figura 1."
            )
        )
        + figure_captioned(
            "figura1-percentil.png",
            "Figura 1. Determinação do percentil de ordem k.",
            "Fonte: Triola (2008).",
            "Fluxograma para determinação do percentil de ordem k",
        )
        + row(
            p(
                "Continuando no nosso exemplo da pressão arterial vamos calcular o primeiro quartil, "
                "que é o P25."
            )
            + p("De acordo com a figura 1,")
        )
        + formula("formula-percentil-l.png", "Cálculo de L para o percentil")
        + row(
            p("Onde: k = 25 e n = 7.")
            + p(
                "Logo, L não é um número inteiro. De acordo com a figura, P25 é o segundo valor ordenado "
                "(arredonda para o inteiro mais próximo, ou seja, L = 2), sendo igual a 125. Significa que 25% "
                "dos valores estão abaixo de 125 mmHg e 75% estão acima."
            )
            + p("Antes da ordenação crescente")
        )
        + formula("pas-antes-ordenacao.png", "Dados antes da ordenação", wide=True)
        + row(p("Dados já ordenados"))
        + formula("pas-ordenados.png", "Dados já ordenados", wide=True)
    )


def content_referencias() -> str:
    return (
        heading(5, "Referências")
        + row(
            '<div class="referencias-aula">'
            '<p class="referencias-item">Triola, MF. <strong>Introdução à estatística</strong>. '
            "Rio de Janeiro: LTC, 2008.</p>"
            "</div>"
        )
    )


CONTENT_BUILDERS = [
    content_sobre,
    content_introducao,
    content_tendencia,
    content_dispersao,
    content_referencias,
]


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for i, builder in enumerate(CONTENT_BUILDERS, 1):
        path = OUT_DIR / f"topico{i}.html"
        path.write_text(build_page(i, builder()), encoding="utf-8")
        print("wrote", path.relative_to(ROOT))

    # Remove leftover topic files beyond the current set
    for path in OUT_DIR.glob("topico*.html"):
        num = int(path.stem.replace("topico", ""))
        if num > len(TOPICS):
            path.unlink()
            print("removed", path.relative_to(ROOT))


if __name__ == "__main__":
    main()
