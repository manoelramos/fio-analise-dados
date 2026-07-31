#!/usr/bin/env python3
"""Gera HTML da Aula 3.5 (Prática SIG II– QGIS e Mapas Temáticos)."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "modulo3" / "aula5"
MEDIA = "../../media/modulo3/aula5/"
ASSETS = "../../"

COURSE_TITLE = "Análise e Interpretação de Dados em Saúde"
MODULE_NUM = 3
MODULE_TITLE = "Análise Espacial"
AULA_LABEL = "Aula 5"
AULA_TITLE = "Prática SIG II– QGIS e Mapas Temáticos"

TOPICS = [
    "Sobre esta aula",
    "Introdução",
    "Simbologia e Classificação de Dados",
    "Principais Métodos de Classificação",
    "Criando um Layout de Impressão",
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
    "BREWER, Cynthia A. ColorBrewer 2.0: color advice for cartography. Disponível em: "
    '<a href="https://colorbrewer2.org/" target="_blank" rel="noopener noreferrer">'
    "https://colorbrewer2.org/</a>. Acesso em: 19 fev. 2026.",
    "PEREIRA, Anderson et al. Modelos de mapas temáticos utilizando o QGIS. OpenGeoOne. "
    "Disponível em: "
    '<a href="https://github.com/OpenGeoOne/mapas-tematicos-qgis" target="_blank" '
    'rel="noopener noreferrer">https://github.com/OpenGeoOne/mapas-tematicos-qgis</a>. '
    "Acesso em: 19 fev. 2026.",
    "SLOCUM, Terry A.; MCMASTER, Robert B.; KESSLER, Fritz C.; HOWARD, Hugh H. "
    "<em>Thematic cartography and geovisualization</em>. 3. ed. Upper Saddle River, NJ: "
    "Pearson Prentice Hall, 2009.",
    "UNIVERSIDADE ESTADUAL DE SANTA CRUZ (UESC). Cartilha básica de geoprocessamento "
    "em saúde. Ilhéus: UESC, 2024. Disponível em: "
    '<a href="https://www.uesc.br/nucleos/bomdevida/2024/Cartilha_Basica_Geoprocessamento_Saude.pdf" '
    'target="_blank" rel="noopener noreferrer">'
    "https://www.uesc.br/nucleos/bomdevida/2024/Cartilha_Basica_Geoprocessamento_Saude.pdf</a>. "
    "Acesso em: 19 fev. 2026.",
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


def ol(items: list[str]) -> str:
    lis = "".join(f'<li class="list-group-item">{item}</li>' for item in items)
    return f'<div class="list"><ol class="list-group list-group-numbered">{lis}</ol></div>'


def box_atencao(body: str, *, raw: bool = False) -> str:
    inner = body if raw else f"<p>{body}</p>"
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
        f"<div>{inner}</div>"
        "</div></div></div>"
    )


def box_saiba(body: str) -> str:
    return row(
        '<div class="box" data-box="Saiba Mais">'
        '<div class="card aos-init" data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="600">'
        '<div class="card-header">'
        '<span class="icone material-symbols-rounded" aria-hidden="true"></span>'
        '<span class="label">Saiba Mais</span>'
        "</div>"
        '<div class="card-body">'
        f"<div><p>{body}</p></div>"
        "</div></div></div>"
    )


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


def icon(src: str, alt: str, size: int = 22) -> str:
    return (
        f'<img src="{MEDIA}{src}" alt="{alt}" width="{size}" height="{size}" '
        'class="align-middle d-inline-block mx-1" style="vertical-align:-4px;" />'
    )


def simple_table(headers: list[str], rows: list[list[str]]) -> str:
    th = "".join(f"<th scope=\"col\">{h}</th>" for h in headers)
    body = ""
    for r in rows:
        tds = "".join(f"<td>{c}</td>" for c in r)
        body += f"<tr>{tds}</tr>"
    return (
        '<div class="table-responsive"><table class="table table-sm table-bordered align-middle mb-0">'
        f"<thead><tr>{th}</tr></thead><tbody>{body}</tbody></table></div>"
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
    else:
        parts.append(
            '<a class="fio-button fio-button-primary" href="../aula6/topico1.html" rel="next">'
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


def a(href: str, label: str | None = None) -> str:
    text = label or href
    return f'<a href="{href}" target="_blank" rel="noopener noreferrer">{text}</a>'


def content_sobre() -> str:
    return (
        heading(1, "Sobre esta aula")
        + row(
            p(
                'Seja bem-vindo e bem-vinda à aula “Prática SIG II– QGIS e Mapas Temáticos”.'
            )
            + p("A seguir, veja algumas informações importantes!")
        )
        + subheading("Objetivos de aprendizagem")
        + row(
            p("Ao final dessa aula, você será capaz de:")
            + ul(
                [
                    "Fazer um mapa temático utilizando simbologia mais adequada",
                    "Conhecer Principais Métodos de Classificação",
                    "Utilizar ferramentas do QGIS para classificação de variáveis",
                    "Fazer um layout do mapa elaborado.",
                ]
            )
        )
        + subheading("Autoria")
        + row(
            p(
                "<strong>Julia Novaes de Barros Peixoto</strong><br />"
                "Mestre em Ciências - Métodos quantitativos em Epidemiologia &amp; Engenheira Cartógrafa."
            )
            + p(
                "<strong>Mônica de Avelar Figueiredo Mafra Magalhães</strong><br />"
                "Doutora em Saúde Coletiva. Mestrado em Geoprocessamento. Tecnologista em Saúde "
                "Pública. Instituto de Comunicação e Informação Científica e Tecnológica em Saúde (Icict) "
                "da Fundação Oswaldo Cruz (Fiocruz)."
            )
            + p(
                "<strong>Diego Ricardo Xavier</strong><br />"
                "Doutor em Epidemiologia. Mestrado em Saúde Pública. Pesquisador em Saúde Pública "
                "Instituto de Comunicação e Informação Científica e Tecnológica em Saúde (Icict) da "
                "Fundação Oswaldo Cruz (Fiocruz).",
                mb0=True,
            )
        )
    )


def content_introducao() -> str:
    return (
        heading(2, "Introdução")
        + row(
            p(
                "Na aula anterior, realizamos o passo fundamental de preparar e unir nossas bases "
                "de dados. Agora, com uma camada vetorial enriquecida com os indicadores de saúde, "
                "podemos avançar para a etapa de visualização e comunicação dos resultados: a "
                "criação de mapas temáticos."
            )
            + p(
                "Um mapa temático bem construído é uma ferramenta de comunicação extremamente eficaz, "
                "capaz de revelar padrões espaciais, destacar desigualdades e subsidiar a tomada de decisão "
                "em saúde pública de forma rápida e intuitiva. Nesta aula, aprenderemos a criar mapas "
                "coropléticos no QGIS, explorando diferentes métodos de classificação de dados e finalizando "
                "com a elaboração de um layout de impressão profissional (PEREIRA et al., [s.d.])."
            )
            + p(
                "Ao seguir estes passos, você será capaz de transformar dados brutos de saúde em mapas "
                "temáticos informativos e profissionais, uma habilidade essencial para a análise e "
                "comunicação de informações em saúde pública. A capacidade de visualizar dados "
                "espacialmente permite a identificação de padrões que seriam invisíveis em uma tabela, "
                "contribuindo para um planejamento mais justo e eficaz das ações de saúde no território "
                "(UESC, 2024).",
                mb0=True,
            )
        )
    )


def content_simbologia() -> str:
    return (
        heading(3, "Simbologia e Classificação de Dados")
        + row(
            p(
                "A simbologia é o conjunto de regras visuais (cores, tamanhos, formas) que usamos para "
                "representar os dados no mapa. Para mapas coropléticos, onde representamos dados "
                "quantitativos agregados por áreas, a escolha da cor e, principalmente, do método de "
                "classificação dos dados é crucial."
            )
        )
        + subheading("Passos para Estilizar a Camada:")
        + row(
            ul(
                [
                    "Abrir o Painel de Estilização: Com a camada unificada da aula anterior selecionada, "
                    "clique com o botão direito sobre ela e vá em Propriedades, ou clique no ícone de "
                    "pincel para abrir o Painel de Estilização de Camada &gt; Simbologia.",
                ]
            )
        )
        + figure_plain(
            "propriedades-simbologia.png",
            "Propriedades da camada e aba Simbologia",
        )
        + row(
            ul(
                [
                    'Mudar de "Símbolo Simples" para "Graduado": No topo do painel, mude o tipo '
                    "de simbologia de Símbolo Simples para Graduado. A simbologia graduada permite "
                    "aplicar uma rampa de cores a uma variável numérica.",
                ]
            )
        )
        + figure_plain(
            "simbolo-graduado.png",
            "Seleção da simbologia Graduado",
        )
        + row(
            p("<strong>Configurar a Simbologia Graduada:</strong>")
            + ul(
                [
                    "Valor: Selecione a coluna (o indicador de saúde) que você deseja mapear "
                    "(ex: taxa_2024).",
                    "Gradiente de cores: Escolha uma paleta de cores adequada. Para dados de "
                    "saúde, rampas de cores sequenciais (que vão de um tom claro a um escuro da "
                    "mesma cor, como amarelos ou azuis) ou divergentes (que usam duas cores para "
                    "extremos opostos e uma cor neutra no meio) são as mais indicadas. Evite rampas "
                    "de cores aleatórias (espectrais), pois elas não possuem uma ordem visual lógica "
                    "(BREWER, [s.d.]).",
                    "Modo (Mode): Aqui você define o método de classificação, ou seja, como os dados "
                    "serão divididos em classes (intervalos).",
                ]
            )
        )
    )


def metodos_table() -> str:
    rows = [
        [
            "Intervalos Iguais<br />(Equal Interval)",
            "A amplitude de cada classe é a mesma.<br />(Ex: 0-10, 10-20, 20-30).",
            "Vantagem: Fácil de entender. Desvantagem: Pode resultar em classes com muitas ou "
            "nenhuma observação se os dados forem assimétricos.",
        ],
        [
            "Quantil<br />(Equal Count)",
            "Cada classe contém o mesmo número de feições (áreas).",
            "Vantagem: Garante que todas as cores sejam usadas no mapa. Desvantagem: Pode agrupar "
            "valores muito diferentes na mesma classe ou separar valores muito semelhantes em classes "
            "diferentes. Os intervalos podem ser confusos (ex: 0-7.3, 7.3-12.1).",
        ],
        [
            "Quebras Naturais<br />(Jenks)",
            'Algoritmo que busca minimizar a variância dentro de cada classe e maximizar a variância '
            'entre as classes. Ele identifica agrupamentos "naturais" nos dados.',
            "Vantagem: Geralmente produz a representação mais fiel da distribuição dos dados. "
            "Desvantagem: Os intervalos são específicos para cada conjunto de dados, dificultando "
            "a comparação entre diferentes mapas.",
        ],
        [
            "Desvio Padrão<br />(Standard Deviation)",
            "As classes são definidas pelo desvio padrão em relação à média dos dados.",
            "Vantagem: Útil para identificar outliers (valores extremos) e ver a relação de cada área "
            "com a média. Desvantagem: Menos intuitivo para um público não estatístico.",
        ],
        [
            "Percentil<br />(Percentile)",
            "As classes são definidas com base em percentis da distribuição dos dados "
            "(ex: 0–25%, 25–50%, 50–75%, 75–100%). Cada classe representa uma posição relativa "
            "do valor dentro do conjunto de dados.",
            "Vantagem: Permite comparar facilmente a posição relativa de cada área dentro da "
            "distribuição. Desvantagem: Assim como o quantil, pode agrupar valores muito diferentes "
            "na mesma classe se houver grande variação nos dados.",
        ],
    ]
    return simple_table(["Método", "Descrição", "Vantagens / Desvantagens"], rows)


def content_metodos() -> str:
    excel_link = (
        f'<a href="{MEDIA}divisão_via_percentil.xlsx" download>'
        '“divisão_via_percentil.xlsx”</a>'
    )
    return (
        heading(4, "Principais Métodos de Classificação")
        + row(
            p(
                "A escolha do método de classificação pode alterar drasticamente a aparência e a "
                "interpretação do mapa (SLOCUM et al., 2009)."
            )
        )
        + row(metodos_table())
        + row(
            p(
                "Após escolher o método e o número de classes desejado (geralmente entre 4 e 6), clique no "
                "botão Classificar. O QGIS irá gerar os intervalos e aplicar as cores ao mapa."
            )
        )
        + subheading("Aprenda a calcular o percentil no Excel:")
        + row(
            ul(
                [
                    "Vamos padronizar as classes da legenda calculando o Percentil, para isso "
                    "disponibilizamos um Excel com cálculo:",
                ]
            )
            + ol(
                [
                    f"No Excel, abra o arquivo {excel_link} disponibilizado na "
                    "plataforma. Ele calcula de forma automática a divisão das classes. Para isso, "
                    "copie os valores das taxas do ano que se deseja fazer o mapa.",
                    "Caso, queira fazer o mapa de mais de um ano para comparação, deve-se colocar "
                    "as taxas uma abaixo da outra na coluna taxa da tabela para o cálculo considerar "
                    "os dados de todos os anos.",
                    "Elimine os valores vazios e zeros, em seguida reordene os valores na "
                    "ordem crescente.",
                ]
            )
            + p("Para o ano de 2024, se desejarmos ter 5 classes a considerar teremos:")
        )
        + figure_plain("percentil-excel.png", "Cálculo de classes por percentil no Excel")
        + row(
            p("Retorne ao QGIS e configure a simbologia utilizando os intervalos calculados:")
        )
        + subheading("1. Abrir as propriedades da camada", "h5")
        + row(
            ul(
                [
                    "No painel Camadas, localize a camada que será utilizada no mapa.",
                    "Clique com o botão direito do mouse sobre a camada.",
                    "Selecione Propriedades.",
                ]
            )
        )
        + subheading("2. Acessar a simbologia da camada", "h5")
        + row(
            ul(
                [
                    "Na janela Propriedades da Camada, clique na aba Simbologia.",
                    "No tipo de simbologia, selecione Graduado.",
                ]
            )
            + p(
                "Esse tipo de simbologia permite representar valores numéricos por classes com "
                "cores diferentes."
            )
        )
        + subheading("3. Escolher o campo de dados", "h5")
        + row(
            ul(
                [
                    "No campo Valor, selecione o atributo que será representado no mapa taxa_24.",
                    "Esse campo será usado para calcular os intervalos das classes.",
                ]
            )
        )
        + subheading("4. Definir o método de classificação", "h5")
        + row(
            ul(
                [
                    "No campo Modo, selecione Intervalo Igual.",
                    "Defina o número de classes desejado de 5 classes.",
                ]
            )
            + p(
                "Vamos preencher os intervalos com os valores das classes de percentil que calculamos "
                "no passo anterior."
            )
        )
        + subheading("5. Escolher a rampa de cores", "h5")
        + row(
            ul(
                [
                    "Clique em Gradiente de cores.",
                    "Escolha uma rampa de cores adequada (por exemplo: amarelo g vermelho).",
                    "Rampas sequenciais são recomendadas para representar intensidade de valores.",
                ]
            )
        )
        + subheading("6. Gerar as classes", "h5")
        + row(
            ul(
                [
                    "Clique no botão Classificar.",
                    "O QGIS irá gerar automaticamente os intervalos de valores para cada classe.",
                ]
            )
            + p("Cada classe representará um intervalo percentual da distribuição dos dados.")
        )
        + subheading("7. Ajustar os limites das classes", "h5")
        + row(
            p("Caso seja necessário:")
            + ul(
                [
                    "Clique duas vezes sobre um intervalo.",
                    "Ajuste o valor inferior ou valor superior.",
                    "Clique em OK.",
                ]
            )
        )
        + subheading("8. Aplicar a simbologia", "h5")
        + row(
            ul(
                [
                    "Clique em Aplicar.",
                    "Depois clique em OK para fechar a janela.",
                ]
            )
            + p("O mapa será atualizado com as cores correspondentes às classes.")
        )
        + figure_plain("mapa-atualizado.png", "Configuração da simbologia graduada no QGIS")
        + row(
            p(
                "Para mais opções de cores clique na seta a direita do Gradiente de cores e clique em Todos "
                "os gradientes de cores."
            )
        )
        + figure_plain("gradientes-cores.png", "Todos os gradientes de cores")
        + row(
            p("O mapa aparecerá com as cores por município e a legenda na lateral com os valores.")
        )
        + figure_plain("mapa-legenda.png", "Mapa com cores por município e legenda")
        + subheading("9. Ajustar o nome da camada para a legenda", "h5")
        + row(
            p("Para melhorar a apresentação da legenda:")
            + ul(
                [
                    "Clique com o botão direito na camada.",
                    "Selecione Renomear Camada.",
                    "Digite um título descritivo.",
                ]
            )
            + p("Exemplo:")
            + p("Taxa de dengue – 2025 (por 100.000 habitantes)")
        )
        + figure_plain("renomear-camada.png", "Renomear camada para a legenda")
    )


def content_layout() -> str:
    return (
        heading(5, "Criando um Layout de Impressão")
        + row(
            p(
                "O passo final é organizar o seu mapa e todos os seus elementos essenciais (título, legenda, "
                "escala, etc.) em um layout formal para exportação como imagem ou PDF."
            )
        )
        + subheading("Passos para Criar o Layout:")
        + row(
            ul(
                [
                    "Novo Compositor de Impressão: Vá no menu Projeto &gt; Novo Layout de Impressão. "
                    "Dê um nome ao seu layout.",
                ]
            )
        )
        + figure_plain("novo-layout.png", "Novo Layout de Impressão")
        + row(
            ul(
                [
                    "Adicionar o Mapa: Na nova janela do compositor, vá em Adicionar Item &gt; Adicionar "
                    "Mapa. Desenhe um retângulo na página para posicionar o seu mapa.",
                ]
            )
        )
        + figure_plain("adicionar-mapa.png", "Adicionar Mapa no layout")
        + row(
            ul(
                [
                    "Adicionar os Elementos Essenciais: Utilizando o menu Adicionar Item, insira os "
                    "seguintes componentes no seu layout:",
                ]
            )
            + ul(
                [
                    "Adicionar Título: Use a ferramenta Adicionar Rótulo. Desenhe o retângulo onde "
                    "deseja posicionar o título do mapa.",
                ]
            )
        )
        + figure_plain("adicionar-rotulo.png", "Adicionar Rótulo para o título")
        + row(
            p(
                "Do lado direito na parte inferior em Propriedades do Item podemos escrever o título e editar "
                "tamanho da fonte."
            )
        )
        + figure_plain("propriedades-titulo.png", "Propriedades do Item para o título")
        + row(
            p(
                "Posicione o alinhamento como central, clique em fonte e coloque o estilo como negrito "
                "e o tamanho da fonte 16. O texto irá alterar de forma automática."
            )
        )
        + figure_plain("titulo-formatado.png", "Formatação da fonte do título")
        + figure_plain("titulo-no-layout.png", "Título posicionado no layout")
        + row(
            p(
                "Adicionar Legenda: Use a ferramenta Adicionar Legenda. Nas Propriedades do Item da "
                "legenda, você pode editar os nomes das camadas e classes para torná-los mais claros."
            )
        )
        + figure_plain("adicionar-legenda.png", "Adicionar Legenda")
        + row(
            ul(
                [
                    "Na aba Propriedades do Item desabilite a Atualização automática para habilitar "
                    "as funções de excluir item da legenda e ordenar os itens.",
                ]
            )
        )
        + figure_plain("legenda-propriedades.png", "Propriedades da legenda")
        + row(
            ul(
                [
                    "Adicionar Barra de Escala: Use a ferramenta Adicionar Barra de Escala.",
                ]
            )
        )
        + figure_plain("adicionar-escala.png", "Adicionar Barra de Escala")
        + row(
            ul(
                [
                    "Adicionar Seta Norte: Use a ferramenta Adicionar Seta Norte.",
                ]
            )
        )
        + figure_plain("adicionar-seta-norte.png", "Adicionar Seta Norte")
        + row(
            ul(
                [
                    "Adicionar Fonte e Informações: Use a ferramenta Adicionar Rótulo para criar caixas "
                    "de texto com a fonte dos dados, o sistema de coordenadas e o nome do autor. "
                    "Na Propriedade do Item é possível escrever o texto e editar a fonte.",
                ]
            )
        )
        + figure_plain("adicionar-fonte.png", "Adicionar fonte e informações")
        + row(
            ul(
                [
                    "Ajustar e Organizar: Mova e redimensione os elementos na página para criar um "
                    "layout balanceado e esteticamente agradável. Use as guias e ferramentas de "
                    "alinhamento para ajudar. Salve o projeto.",
                ]
            )
        )
        + figure_plain("layout-organizado.png", "Layout organizado")
        + row(
            ul(
                [
                    "Exportar o Mapa: Quando o layout estiver pronto, você pode exportá-lo em diferentes "
                    "formatos através do menu Layout:",
                ]
            )
            + ul(
                [
                    "Exportar como Imagem... (PNG, JPG)",
                    "Exportar como SVG... (formato vetorial)",
                    "Exportar como PDF...",
                ]
            )
        )
        + figure_plain("exportar-mapa.png", "Opções de exportação do layout")
        + figure_plain("mapa-final-layout.png", "Mapa temático exportado")
    )


def content_referencias() -> str:
    items = "".join(f'<p class="referencias-item">{ref}</p>' for ref in REFERENCES)
    return heading(6, "Referências") + row(f'<div class="referencias-aula">{items}</div>')


CONTENT_BUILDERS = [
    content_sobre,
    content_introducao,
    content_simbologia,
    content_metodos,
    content_layout,
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
