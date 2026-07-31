#!/usr/bin/env python3
"""Gera HTML da Aula 3.4 (Prática SIG I – QGIS e adequação de base de dados)."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "modulo3" / "aula4"
MEDIA = "../../media/modulo3/aula4/"
ASSETS = "../../"

COURSE_TITLE = "Análise e Interpretação de Dados em Saúde"
MODULE_NUM = 3
MODULE_TITLE = "Análise Espacial"
AULA_LABEL = "Aula 4"
AULA_TITLE = "Prática SIG I – QGIS e adequação de base de dados"

TOPICS = [
    "Sobre esta aula",
    "Introdução",
    "Baixar e instalar o QGIS",
    "Fontes de dados espaciais vetoriais",
    "Preparando os dados para o QGIS",
    "Unindo as Bases de Dados no QGIS (Join)",
    "Navegação e salvar projeto",
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
    "INSTITUTO BRASILEIRO DE GEOGRAFIA E ESTATÍSTICA (IBGE). Resolução da Presidência "
    "n.º 1, de 25 de fevereiro de 2005. Dispõe sobre a adoção do SIRGAS2000 como novo sistema "
    "de referência geodésico para o Sistema Geodésico Brasileiro. Rio de Janeiro: IBGE, 2005. "
    "Disponível em: "
    '<a href="https://geoftp.ibge.gov.br/metodos_e_outros_documentos_de_referencia/'
    'normas/resolucao_pr_01_25fev2005.pdf" target="_blank" rel="noopener noreferrer">'
    "https://geoftp.ibge.gov.br/.../resolucao_pr_01_25fev2005.pdf</a>. Acesso em: 19 fev. 2026.",
    "PROGRAMMING HISTORIAN. Geocodificando dados históricos com o QGIS. Disponível em: "
    '<a href="https://programminghistorian.org/pt/licoes/geocodificando-qgis" target="_blank" '
    'rel="noopener noreferrer">https://programminghistorian.org/pt/licoes/geocodificando-qgis</a>. '
    "Acesso em: 19 fev. 2026.",
    "QGIS DEVELOPMENT TEAM. QGIS Geographic Information System. Open Source Geospatial "
    "Foundation. Disponível em: "
    '<a href="https://qgis.org" target="_blank" rel="noopener noreferrer">https://qgis.org</a>. '
    "Acesso em: 19 fev. 2026.",
    "QGIS DOCUMENTATION. Unindo e relacionando dados. QGIS Documentation 3.40. Disponível em: "
    '<a href="https://docs.qgis.org/3.40/pt_BR/docs/user_manual/working_with_vector/'
    'joins_relations.html" target="_blank" rel="noopener noreferrer">'
    "https://docs.qgis.org/3.40/pt_BR/docs/user_manual/working_with_vector/joins_relations.html</a>. "
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
            '<a class="fio-button fio-button-primary" href="../aula5/topico1.html" rel="next">'
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
                'Seja bem-vindo e bem-vinda à aula <strong>"Prática SIG I – QGIS e adequação de base de dados"</strong>.'
            )
            + p("A seguir, veja algumas informações importantes!")
        )
        + subheading("Objetivos de aprendizagem")
        + row(
            p("Ao final dessa aula, você será capaz de:")
            + ul(
                [
                    "Baixar e instalar o QGIS;",
                    "Conhecer algumas fontes de dados espaciais vetoriais;",
                    "Adicionar os dados no QGIS;",
                    "Visualizar dados (ordenação, cores e clarificação);",
                    "Utilizar ferramentas básicas de navegação QGIS;",
                    "Salvar um projeto.",
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
                "no Instituto de Comunicação e Informação Científica e Tecnológica em Saúde (Icict) "
                "da Fundação Oswaldo Cruz (Fiocruz).",
                mb0=True,
            )
        )
    )


def content_introducao() -> str:
    return (
        heading(2, "Introdução")
        + row(
            p(
                "Após entendermos os conceitos teóricos da análise espacial, é hora de iniciarmos a parte "
                "prática utilizando um Sistema de Informação Geográfica (SIG). Nesta e na próxima aula, "
                "utilizaremos o QGIS, um software de SIG profissional, gratuito e de código aberto, que se "
                "tornou uma das principais ferramentas para geoprocessamento no mundo, inclusive na área "
                "da saúde (QGIS DEVELOPMENT TEAM, [s.d.])."
            )
            + p(
                "O sucesso de qualquer análise espacial depende fundamentalmente da qualidade e da "
                "correta preparação dos dados. Dados mal formatados, com erros ou em sistemas de "
                "coordenadas diferentes, são a principal fonte de problemas em projetos de SIG."
            )
            + p(
                "Portanto, esta primeira aula prática é dedicada à adequação de bases de dados, um passo "
                "crucial e muitas vezes subestimado. Para esta aula, nosso objetivo é preparar dois tipos "
                "de dados para que possam ser unidos e analisados: uma base de dados de saúde (atributos) "
                "e uma base cartográfica (espacial).",
                mb0=True,
            )
        )
    )


def content_instalar() -> str:
    return (
        heading(3, "Baixar e instalar o QGIS")
        + row(
            p(
                f"Acesse {a('https://qgis.org/pt_BR/site/', 'https://qgis.org/pt_BR/site/')} e clique em "
                "<strong>Baixe agora</strong>."
            )
            + p(
                "Instalaremos a última versão mais estável, a <strong>3.40 - Bratislava</strong>."
            )
        )
        + box_atencao(
            "Existem outras versões muito parecidas, mas dê preferência por esta para "
            "acompanhar melhor a prática."
        )
        + row(
            ol(
                [
                    "Clique em <strong>Download</strong> na barra superior.",
                    "Na caixa flutuante à direita clique em <strong>“Skip it and go to download”</strong>.",
                    "Em seguida clique na opção de versão <strong>“Download LTR 3.40”</strong> e o "
                    "processo de download irá se iniciar automaticamente.",
                ]
            )
        )
        + figure_captioned(
            "figura1-download-qgis.png",
            "Figura 1: Acesso ao download do QGIS.",
            "Fonte: Site QGIS — https://www.qgis.org/",
            "Telas do site QGIS destacando Download, Skip e LTR 3.40",
        )
        + row(
            p(
                "O executável do programa ficará salvo no download do computador. Clique duas vezes "
                "e inicie a instalação."
            )
        )
        + figure_captioned(
            "figura2-arquivo-baixado.png",
            "Figura 2: Localizando o arquivo do programa baixado.",
            "Fonte: Site QGIS — https://www.qgis.org/",
            "Arquivo instalador do QGIS na pasta Downloads",
        )
        + row(
            p(
                "Após a instalação, vá ao “Iniciar do Windows” e busque por QGIS. Se não encontrar, vá na "
                "“Pesquisa” e escreva QGIS. Para abrir o programa, basta clicar no ícone para o aplicativo. "
                "Pronto, podemos iniciar!"
            )
        )
        + figure_captioned(
            "figura3-iniciando-qgis.png",
            "Figura 3: Iniciando o QGIS.",
            "Fonte: Site QGIS — https://www.qgis.org/",
            "Tela inicial do QGIS 3.40 Bratislava",
        )
    )


def fontes_tables() -> str:
    geo = simple_table(
        ["Fonte", "Tipo de Dados", "Link"],
        [
            [
                "IBGE",
                "Cartografia oficial, malhas territoriais, dados censitários",
                a("https://www.ibge.gov.br/"),
            ],
            [
                "INPE",
                "Imagens de satélite, monitoramento ambiental",
                a("https://www.gov.br/inpe/pt-br/acesso-a-informacao/dados-abertos"),
            ],
            [
                "INDE",
                "Catálogo de geosserviços (WMS, WFS, metadados)",
                a("https://inde.gov.br/CatalogoGeosservicos"),
            ],
        ],
    )
    amb = simple_table(
        ["Fonte", "Tipo de Dados", "Link"],
        [
            [
                "IBAMA",
                "Fiscalização e dados ambientais federais",
                a("https://dadosabertos.ibama.gov.br/"),
            ],
            [
                "INEA",
                "Dados ambientais estaduais (RJ)",
                a("http://www.inea.rj.gov.br/"),
            ],
            [
                "Observatório Clima &amp; Saúde (Fiocruz)",
                "Relação entre clima e saúde",
                a("https://climaesaude.icict.fiocruz.br/"),
            ],
        ],
    )
    saude = simple_table(
        ["Fonte", "Tipo de Dados", "Link"],
        [
            [
                "DATASUS (TABNET)",
                "Estatísticas e indicadores do SUS",
                a("http://tabnet.datasus.gov.br/"),
            ],
            [
                "PCDAS",
                "Conjuntos de dados aplicados à saúde",
                a("https://pcdas.icict.fiocruz.br/conjunto-de-dados/"),
            ],
            [
                "PROADESS",
                "Avaliação do desempenho do SUS",
                a("https://www.proadess.icict.fiocruz.br/"),
            ],
            [
                "SISAP-Idoso",
                "Indicadores de saúde da população idosa",
                a("https://sisapidoso.icict.fiocruz.br/"),
            ],
            [
                "RIPSA",
                "Indicadores estratégicos de saúde",
                a("https://www.ripsa.org.br/"),
            ],
        ],
    )
    socio = simple_table(
        ["Fonte", "Tipo de Dados", "Link"],
        [
            [
                "Atlas do Desenvolvimento Humano no Brasil",
                "IDH, renda, educação, vulnerabilidade social",
                a("http://www.atlasbrasil.org.br/"),
            ],
            [
                "Portal Brasileiro de Dados Abertos",
                "Conjuntos de dados governamentais diversos",
                a("https://dados.gov.br/dados/conjuntos-dados"),
            ],
            [
                "Base de dados",
                "ONG – plataforma pública de dados",
                a("https://basedosdados.org/search"),
            ],
        ],
    )
    return (
        subheading("Fontes nacionais de dados")
        + subheading("1. Dados geoespaciais e cartográficos", "h5")
        + row(geo)
        + subheading("2. Dados ambientais", "h5")
        + row(amb)
        + subheading("3. Dados em saúde pública", "h5")
        + row(saude)
        + subheading("4. Dados socioeconômicos e governamentais", "h5")
        + row(socio)
        + box_atencao(
            "<p>Antes de iniciar a busca de um dado geoespacial é importante definir a escala de "
            "análise do seu projeto: nacional, estadual ou municipal. Para dados municipais, "
            "acesse os sites da prefeitura para verificar a disponibilidade de dados ou solicite "
            "à secretaria de urbanismo.</p>"
            f'<figure class="mt-3 mb-0">'
            f'<img class="img-fluid mx-auto d-block rounded border bg-white" '
            f'src="{MEDIA}atencao-escala.png" '
            f'alt="Diagrama de escalas nacional, estadual e municipal" loading="lazy" />'
            f"</figure>",
            raw=True,
        )
    )


def content_fontes() -> str:
    return (
        heading(4, "Conhecendo algumas fontes de dados espaciais vetoriais")
        + row(
            p(
                "O formato de arquivo vetorial padrão usado no QGIS é o arquivo de forma ESRI chamado "
                "<strong>shapefile</strong>. Um shapefile consiste, na verdade, de um conjunto de vários "
                "arquivos. Os três seguintes são necessários:"
            )
            + ul(
                [
                    "<strong>.shp</strong> — arquivo que contém as formas vetoriais;",
                    "<strong>.dbf</strong> — arquivo que contém os atributos no formato dBase;",
                    "<strong>.shx</strong> — arquivos index.",
                ]
            )
            + p(
                "Shapefiles também podem incluir um arquivo com a extensão <strong>.prj</strong> que "
                "contém as informações de projeção. Embora seja muito útil um arquivo de projeção, "
                "não é obrigatório."
            )
        )
        + figure_captioned(
            "figura4-estrutura-shapefile.png",
            "Figura 4: Estrutura de um shapefile.",
            "Fonte: Elaborado pelas autoras.",
            "Componentes de um shapefile",
        )
        + row(
            p(
                "Você lembra que o dado vetorial possui a estrutura geométrica de ponto, linha ou área?"
            )
        )
        + figure_captioned(
            "figura5-formas-vetoriais.png",
            "Figura 5: Formas de dados vetoriais.",
            "Fonte: Site QGIS — https://www.qgis.org/",
            "Exemplos de ponto, linha e polígono",
        )
        + fontes_tables()
    )


def content_base_cartografica() -> str:
    return (
        heading(5, "Preparando os dados para o QGIS")
        + subheading("Base cartográfica (espacial)")
        + row(
            p(
                "A base cartográfica, também chamada de shapefile (.shp), contém a geometria das unidades "
                "de análise (ex.: os polígonos dos municípios do Brasil). Malhas municipais, estaduais e de "
                "setores censitários podem ser baixadas gratuitamente do site do IBGE."
            )
            + p(
                "Para a prática dessa aula vamos utilizar o arquivo: <strong>BR_Municipios_2024</strong>. "
                "Este arquivo foi construído e disponibilizado pelo IBGE e já está organizado para este exercício. "
                "Baixe o arquivo no Educare: "
                + a("https://educare.fiocruz.br/resource/show?id=AyVQ0laQ")
                + "."
            )
            + p(
                "Mas você pode ter acesso a ele no link: "
                + a("https://www.ibge.gov.br/geociencias/downloads-geociencias.html")
                + "."
            )
            + p(
                "<strong>organização_do_território</strong> &gt; <strong>malhas-territoriais</strong> &gt; "
                "<strong>malhas_municipais</strong> &gt; <strong>município_2024</strong> &gt; "
                "<strong>Brasil</strong> &gt; <strong>BR_Municipios_2024.zip</strong>"
            )
        )
        + box_atencao(
            'Crie um diretório na sua máquina chamado <strong>“PraticaQGIS”</strong> (sem espaço) em um '
            "caminho que você memorize."
        )
        + row(
            p(
                "Normalmente, o Windows baixa o arquivo na pasta de Download. Repasse o arquivo "
                "baixado para a pasta que você criou “PraticaQGIS”, clique com o botão direito no arquivo "
                "e vá na opção extrair."
            )
        )
        + figure_plain("pasta-pratica-qgis.png", "Pasta PraticaQGIS com o shapefile extraído")
        + subheading("Adicionando os dados no QGIS")
        + row(
            ul(
                [
                    "Inicie o QGIS.",
                    "Abra um novo projeto em branco.",
                ]
            )
        )
        + figure_plain(
            "adicionar-camada-menu.png",
            "Interface do QGIS com destaque para Novo Projeto",
        )
        + row(
            ul(
                [
                    "Para abrir os arquivos, vá na barra superior e clique em "
                    "<strong>Camada &gt; Adicionar Camada &gt; Adicionar Camada Vetorial</strong>. "
                    "Busque o diretório onde o arquivo foi salvo clicando nos três pontos em "
                    "<strong>Fonte &gt; Base de vetores</strong>. Configure o formato de dado que está "
                    "buscando adicionar, neste caso será ‘shapefile’.",
                ]
            )
        )
        + figure_plain(
            "adicionar-camada-vetorial.png",
            "Menu Camada > Adicionar Camada Vetorial e seleção do shapefile",
        )
        + row(
            ul(
                [
                    "Clique no dado &gt; abrir. Depois clique em <strong>Adicionar</strong> "
                    "na parte inferior da janela.",
                ]
            )
        )
        + figure_plain(
            "selecionar-shapefile.png",
            "Botão Adicionar no Gerenciador de Fonte de Dados",
        )
        + row(
            p(
                "Antes de começar a trabalhar com os dados é importante verificar a tabela de atributos "
                "do dado, que é a componente <strong>.dbf</strong> da base de dados."
            )
            + p(
                "Vamos explorar a tabela da camada dos municípios, clicando com o botão direito na camada "
                "e clique em <strong>Abrir tabela de atributos</strong>."
            )
            + p("<strong>Botão direito no dado &gt; Abrir tabela de atributos</strong>")
            + p(
                "Nela, conseguimos saber quais informações temos de cada registro. Neste caso, cada "
                "linha da tabela é referente a um município do Brasil com seu código único, nome, estado, "
                "região e área."
            )
        )
        + figure_plain(
            "camada-municipios.png",
            "Menu de contexto com Abrir tabela de atributos",
        )
        + figure_plain("tabela-atributos.png", "Tabela de atributos dos municípios")
        + row(
            p(
                "Antes de começar a trabalhar com os dados, é importante verificar o sistema de "
                "coordenadas e se possui alguma projeção atribuída ao dado. Para dados oficiais brasileiros, "
                "os dados devem estar em <strong>SIRGAS 2000</strong>."
            )
            + p(
                'Na janela “Camadas”, selecione a shape <strong>BR_Municipios_2024</strong> e com '
                "<strong>Botão direito &gt; Propriedades &gt; Informações</strong>."
            )
        )
        + figure_plain("propriedades-menu.png", "Menu de propriedades da camada")
        + figure_plain("propriedades-informacoes.png", "Aba Informações com o sistema de coordenadas")
        + subheading("A Base de Dados de Saúde (Atributos)")
        + row(
            p(
                'Para este exercício, usaremos o arquivo: '
                f'<a href="{MEDIA}taxa_dengue.xlsx" download>taxa_dengue.xlsx</a>.'
            )
            + p(
                "Mas você pode baixá-lo como já viu na disciplina Fontes de dados, pelo TabNet do "
                "DATASUS como tabelas em formato .csv ou planilhas Excel (.xls, .xlsx)."
            )
            + ul(
                [
                    "Acesse o Tabnet "
                    + a("https://datasus.saude.gov.br/informacoes-de-saude-tabnet/")
                    + ";",
                    "Epidemiológicas e Morbidade &gt; Doenças e Agravos de Notificação - 2007 em diante "
                    "(SINAN) &gt; Dengue 2014 em diante;",
                    "Vá até o rodapé da página e selecione a Abrangência Geográfica &gt; "
                    "<strong>BR por Região, UF e Município</strong>;",
                    "Para linha selecione os municípios de notificação e para as colunas os anos "
                    "observados de 2024 a 2025;",
                    "Vá no final da página e clique em <strong>Mostrar</strong> para ter uma pré-visualização "
                    "da tabela antes de baixar. No final da página clique em "
                    "<strong>‘Cópia como .csv’</strong>. Salve o dado baixado na pasta PraticaQGIS.",
                ]
            )
        )
        + figure_plain("tabnet-dengue.png", "Seleção de Dengue no TabNet")
        + row(
            p(
                "Anteriormente, baixamos a tabela de número de casos de dengue notificados por ano para "
                "os municípios do BR. Suponhamos que você queira calcular a taxa anual de dengue para "
                "cada município e para isso precise adicionar à sua tabela a população."
            )
            + p(
                "Dados de população são gerados pelo IBGE. Para obter dados da população por município "
                "de anos não censitários basta ir em "
                + a("https://sidra.ibge.gov.br")
                + ", selecionar os anos que deseja (no caso da prática selecionamos 2024 e 2025 e "
                "municípios como nível territorial)."
            )
        )
        + figure_plain(
            "tabnet-abrangencia.png",
            "Seleção de população e municípios no SIDRA/IBGE",
        )
        + subheading("Passos para Adequação")
        + row(
            p(
                "<strong>Limpeza da Tabela:</strong> Abra o arquivo em um editor de planilhas (Excel, "
                "LibreOffice Calc). Remova linhas de cabeçalho e rodapé desnecessárias, mesclagens de "
                "células e caracteres especiais dos nomes das colunas. A primeira linha da tabela deve "
                "conter os nomes das colunas (variáveis), e as linhas seguintes, os dados."
            )
            + p(
                "<strong>Salvar em Formato Adequado:</strong> O formato mais compatível para importação "
                "no QGIS é o CSV (Comma-Separated Values). Ao salvar, escolha a opção "
                "“CSV (separado por vírgulas)” ou “CSV (UTF-8)”. O UTF-8 é recomendado para garantir que "
                "caracteres como acentos e “ç” sejam preservados (PROGRAMMING HISTORIAN, [s.d.])."
            )
        )
        + figure_plain(
            "planilha-taxa-dengue.png",
            "Limpeza da tabela, verificação do código e salvamento em CSV",
        )
        + figure_plain(
            "tabela-taxa-dengue.png",
            "Tabela taxa_dengue após a limpeza",
        )
        + row(
            p(
                'Para acompanhar como tratar o dado por completo e o cálculo da taxa, '
                '<a href="https://educare.fiocruz.br/resource/show?id=ROaNyzAU" '
                'target="_blank" rel="noopener noreferrer">clique aqui</a>!'
            )
        )
        + row(
            ul(
                [
                    "Para adicionar os dados tabulares no QGIS, na barra superior vá em "
                    "<strong>Camada &gt; Adicionar Camada &gt; Adicionar Camada de Texto Delimitado</strong>. "
                    "Clique no arquivo dentro do diretório e Abrir.",
                ]
            )
        )
        + figure_plain(
            "menu-texto-delimitado.png",
            "Menu Camada > Adicionar Camada de Texto Delimitado",
        )
        + figure_plain(
            "selecionar-csv.png",
            "Seleção do arquivo taxa_dengue.csv",
        )
        + row(
            ul(
                [
                    "Antes de adicionar o dado, configure a entrada com delimitação por "
                    "<strong>ponto e vírgula</strong>, tipo de dado <strong>sem geometria</strong> e o "
                    "código do município no formato <strong>string</strong> (texto). Os demais campos de "
                    "casos, população e taxa como numérico.",
                ]
            )
        )
        + figure_plain(
            "configurar-texto-delimitado.png",
            "Configuração da camada de texto delimitado no QGIS",
        )
        + subheading("Adequando a tabela de atributos dos dados")
        + row(
            p(
                "<strong>Verificação do Código de Ligação:</strong> Para unir a tabela de saúde a um mapa, "
                "precisamos de um campo chave (ou código de ligação) comum a ambas as bases. Para dados "
                "municipais no Brasil, o código ideal é o código do município de 6 ou 7 dígitos do IBGE. "
                "Verifique se sua tabela de saúde possui essa coluna e se os códigos estão formatados "
                "como número ou texto, sem pontos ou traços."
            )
        )
        + figure_plain(
            "tabela-comparacao-codigos.png",
            "Comparação dos códigos de município nas duas tabelas",
        )
        + row(
            p(
                "Criar um novo campo com <strong>CD_MUN</strong> reduzido para 6 dígitos na tabela de "
                "atributos no dado espacial <strong>BR_Municipios_2024</strong>:"
            )
            + ul(
                [
                    "Abra a tabela de atributos: Clique com o botão direito na camada &gt; "
                    "Abrir Tabela de Atributos;",
                    "Abra a Calculadora de Campos: Ícone da calculadora &gt; Abrir Calculadora de Campos.",
                ]
            )
        )
        + figure_plain("calculadora-campos-icone.png", "Ícone da Calculadora de Campos")
        + row(
            p("Configure o novo campo:")
            + ol(
                [
                    "Marque <strong>Criar um novo campo</strong>;",
                    "Nome do campo: <strong>CD_MUN6</strong>;",
                    "Tipo: <strong>Texto (string)</strong>;",
                    "Comprimento: <strong>6</strong>.",
                ]
            )
            + p('Use esta expressão: <code>left("CD_MUN", 6)</code>')
            + ul(
                [
                    "Clique em <strong>OK</strong>;",
                    "Isso pega apenas os 6 primeiros caracteres do código de 7 dígitos.",
                ]
            )
        )
        + figure_plain("calculadora-campos-config.png", "Configuração da Calculadora de Campos")
        + row(
            p(
                "O novo campo é criado de forma temporária. Para salvá-lo na tabela de atributos, vá na "
                "barra superior e clique em <strong>Salvar alterações</strong> "
                + icon("icone-salvar-alteracoes.png", "Ícone Salvar alterações")
                + ". Depois saia do modo de edição clicando ao lado em "
                "<strong>Alternar modo de edição</strong> "
                + icon("icone-alternar-edicao.png", "Ícone Alternar modo de edição")
                + "."
            )
            + p("Observe que a coluna do novo campo aparece no final da tabela de atributos.")
        )
        + figure_plain("salvar-edicao.png", "Salvar alterações e alternar modo de edição")
        + figure_plain("campo-cdmun6.png", "Novo campo CD_MUN6 na tabela de atributos")
    )


def content_join() -> str:
    return (
        heading(6, "Unindo as Bases de Dados no QGIS (Join)")
        + row(
            p(
                "Com as duas bases de dados gráfica (mapa) e não gráfica (tabela) adequadas, o próximo "
                "passo é realizar a união das duas (Join). Essa operação irá vincular os dados da sua "
                "tabela de saúde (.csv) aos polígonos do seu mapa (.shp) com base no campo chave comum "
                "(QGIS DOCUMENTATION, [s.d.])."
            )
        )
        + subheading("Passos para o Join")
        + row(
            p(
                "<strong>Abrir as Propriedades da Camada Vetorial:</strong> Clique com o botão direito na "
                "camada do mapa (o shapefile) e vá em <strong>Propriedades</strong>."
            )
            + ul(
                [
                    'Acessar a aba <strong>"Uniões" (Joins)</strong>: no menu à esquerda da janela de '
                    "propriedades, selecione a aba Uniões;",
                    'Criar uma Nova União: clique no ícone de "+" (ou "Adicionar nova união"). '
                    "Uma nova janela se abrirá;",
                    "<strong>Unir Camada:</strong> selecione a sua tabela .csv;",
                    "<strong>Unir Campo:</strong> selecione a coluna com o código do município na sua "
                    "tabela .csv;",
                    "<strong>Campo Alvo:</strong> selecione a coluna com o código do município na tabela "
                    "de atributos do shapefile;",
                    "Clique em <strong>OK</strong>.",
                ]
            )
        )
        + figure_plain("propriedades-unioes.png", "Aba Uniões nas propriedades da camada")
        + figure_plain("nova-uniao.png", "Janela Adicionar união de vetor")
        + row(
            p(
                "<strong>Verificar o resultado:</strong> Após confirmar a união, abra novamente a tabela "
                "de atributos do shapefile. As colunas da sua tabela de saúde agora devem aparecer ao "
                "lado das colunas originais do mapa. A união é temporária. Para torná-la permanente, "
                "você deve salvar a camada com um novo nome."
            )
            + p(
                "Para salvar um shapefile com um novo nome de forma segura é recomendado exportá-lo "
                "com um novo nome; dessa maneira todos os arquivos que o compõem também receberão o "
                "mesmo nome."
            )
            + ul(
                [
                    "Clique com botão direito na camada e vá em "
                    "<strong>Exportar &gt; Guardar elementos como</strong>;",
                    "Selecione o tipo de dado que deseja salvar ‘shapefile’ e o local onde deseja salvar "
                    "o shapefile em <strong>Nome do arquivo</strong>;",
                    "Clique <strong>Salvar</strong> e <strong>OK</strong>.",
                ]
            )
        )
        + figure_plain("exportar-shapefile.png", "Menu Exportar > Guardar elementos como")
        + figure_plain("guardar-elementos.png", "Janela Guardar elementos vetoriais como")
        + figure_plain("resultado-join.png", "Tabela de atributos após o Join")
        + row(
            p(
                "Ao final desta aula, você terá um único arquivo shapefile contendo tanto a informação "
                "espacial (geometria dos municípios) quanto os atributos de saúde que você deseja analisar. "
                "Esta camada de dados unificada é a matéria-prima para a criação de mapas temáticos, que "
                "será o foco da nossa próxima aula prática.",
                mb0=True,
            )
        )
        + figure_plain("mapa-final.png", "Mapa com a camada unificada no QGIS")
    )


def content_navegacao() -> str:
    return (
        heading(7, "Navegação e salvar projeto")
        + subheading("Ferramentas básicas de navegação QGIS")
        + row(
            p("Agora que ajustamos a camada, vamos explorar algumas ferramentas de navegação.")
            + ul(
                [
                    "Movendo o scroll do mouse você pode dar zoom + ou −. Essas opções também estão "
                    "disponíveis na barra superior de ferramentas nos ícones:",
                ]
            )
        )
        + figure_plain("ferramentas-zoom.png", "Ícones de zoom no QGIS")
        + row(p("O ícone <strong>Ver tudo</strong> permite retornar à visualização total do projeto."))
        + row(
            ul(
                [
                    "Outra opção é deslocar o mapa de um lado para outro usando o ícone:",
                ]
            )
        )
        + figure_plain("ferramenta-deslocar.png", "Ícone de deslocar mapa")
        + row(
            ul(
                [
                    "Caso esteja testando o melhor zoom de visualização, você pode comparar o antes "
                    "com o depois usando esses ícones:",
                ]
            )
        )
        + figure_plain("ferramentas-zoom-anterior.png", "Ícones de zoom anterior e seguinte")
        + row(
            ul(
                [
                    "Podemos também identificar feições usando o ícone "
                    + icon("icone-identificar.png", "Ícone Identificar feições")
                    + " e clicando no mapa. Vai aparecer um box com os atributos da feição. Observe que "
                    "a informação do box é referente à camada que está ativa; caso queira mudar, clique "
                    "na camada de interesse antes de selecionar a feição no mapa.",
                ]
            )
        )
        + subheading("Salvando um projeto")
        + row(
            p(
                "Para finalizar vamos salvar o projeto iniciado, para visualizações futuras. Salvar um "
                "projeto garante que a visualização editada fique salva para ser vista novamente, mas "
                "isso não impede que o shapefile seja usado e visualizado em outro projeto ou em outro "
                "programa de Sistema de Informação Geográfica (SIG) que aceite o shapefile como dados "
                "de visualização."
            )
            + p(
                "Podemos usar o ícone "
                + icon("icone-salvar-projeto.png", "Ícone Salvar projeto")
                + " ou ir em <strong>Projeto &gt; Salvar</strong>. O projeto "
                "do QGIS tem o formato <strong>.qgz</strong>; vamos salvá-lo como "
                "<strong>Aula 1</strong> na pasta do curso."
            )
        )
    )


def content_referencias() -> str:
    items = "".join(f'<p class="referencias-item">{ref}</p>' for ref in REFERENCES)
    return heading(8, "Referências") + row(f'<div class="referencias-aula">{items}</div>')


CONTENT_BUILDERS = [
    content_sobre,
    content_introducao,
    content_instalar,
    content_fontes,
    content_base_cartografica,
    content_join,
    content_navegacao,
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
