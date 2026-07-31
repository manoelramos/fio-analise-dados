#!/usr/bin/env python3
"""Gera HTML da Aula 3.3 (Fundamentos da Cartografia) a partir do PDF validado."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "modulo3" / "aula3"
MEDIA = "../../media/modulo3/aula3/"
ASSETS = "../../"

COURSE_TITLE = "Análise e Interpretação de Dados em Saúde"
MODULE_NUM = 3
MODULE_TITLE = "Análise Espacial"
AULA_LABEL = "Aula 3"
AULA_TITLE = "Fundamentos da Cartografia"

TOPICS = [
    "Sobre esta aula",
    "Introdução",
    "Sistema geodésico de referência",
    "Sistemas de coordenadas",
    "Projeções cartográficas",
    "Conceito de escala",
    "Cartografia temática e simbologia",
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
    "BREWER, Cynthia A. Color use guidelines for mapping and visualization. "
    "In: MACEACHREN, Alan M.; TAYLOR, D. R. Fraser (org.). "
    "<em>Visualization in modern cartography</em>. Oxford: Pergamon, 1994. p. 123-147.",
    "FITZ, Paulo Roberto. <em>Cartografia básica</em>. São Paulo: Oficina de Textos, 2008.",
    "FOOTE, Kenneth E.; CRUM, Shannon. <em>Cartographic communication</em>. Boulder: "
    "Department of Geography, University of Colorado Boulder, 1995. Disponível em: "
    '<a href="http://www.colorado.edu/geography/gcraft/notes/cartocom/cartocom_f.html" '
    'target="_blank" rel="noopener noreferrer">'
    "http://www.colorado.edu/geography/gcraft/notes/cartocom/cartocom_f.html</a>. "
    "Acesso em: jul. 2014.",
    "INSTITUTO BRASILEIRO DE GEOGRAFIA E ESTATÍSTICA (IBGE). Cartografia. Disponível em: "
    '<a href="https://atlasescolar.ibge.gov.br/cartografia.html" target="_blank" '
    'rel="noopener noreferrer">https://atlasescolar.ibge.gov.br/cartografia.html</a>. '
    "Acesso em: 11 fev. 2026.",
    "INSTITUTO BRASILEIRO DE GEOGRAFIA E ESTATÍSTICA (IBGE). Coordenadas geográficas. "
    "Atlas Escolar. Disponível em: "
    '<a href="https://atlasescolar.ibge.gov.br/cartografia/21730-coordenadas-geograficas.html" '
    'target="_blank" rel="noopener noreferrer">'
    "https://atlasescolar.ibge.gov.br/cartografia/21730-coordenadas-geograficas.html</a>. "
    "Acesso em: 11 fev. 2026.",
    "INSTITUTO BRASILEIRO DE GEOGRAFIA E ESTATÍSTICA (IBGE). <em>Manual técnico de geodésia</em>. "
    "Rio de Janeiro: IBGE, 2015. Disponível em: "
    '<a href="https://biblioteca.ibge.gov.br/visualizacao/livros/liv8595_v1.pdf" target="_blank" '
    'rel="noopener noreferrer">https://biblioteca.ibge.gov.br/visualizacao/livros/liv8595_v1.pdf</a>. '
    "Acesso em: 26 fev. 2026.",
    "INSTITUTO BRASILEIRO DE GEOGRAFIA E ESTATÍSTICA (IBGE). <em>Noções básicas de cartografia</em>. "
    "Rio de Janeiro: IBGE, 1999. (Manuais Técnicos em Geociências, n. 8). Disponível em: "
    '<a href="https://biblioteca.ibge.gov.br/visualizacao/livros/liv81158.pdf" target="_blank" '
    'rel="noopener noreferrer">https://biblioteca.ibge.gov.br/visualizacao/livros/liv81158.pdf</a>. '
    "Acesso em: 26 fev. 2026.",
    "INSTITUTO BRASILEIRO DE GEOGRAFIA E ESTATÍSTICA (IBGE). <em>Revista Ponto de Referência</em>. "
    "Rio de Janeiro: IBGE, 2005. Disponível em: "
    '<a href="https://geoftp.ibge.gov.br/metodos_e_outros_documentos_de_referencia/'
    'outros_documentos_tecnicos/pmrg/revista_ponto_de_referencia.pdf" target="_blank" '
    'rel="noopener noreferrer">'
    "https://geoftp.ibge.gov.br/.../revista_ponto_de_referencia.pdf</a>. Acesso em: 11 fev. 2026.",
    "MENEZES, Paulo Márcio Leal de; FERNANDES, Manoel do Couto. "
    "<em>Roteiro de cartografia</em>. 1. ed. São Paulo: Oficina de Textos, 2013. 288 p.",
    "SNYDER, John P. <em>Map projections: a working manual</em>. Washington, DC: "
    "U.S. Government Printing Office, 1987. (U.S. Geological Survey Professional Paper, 1395).",
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


def figure_captioned(src: str, caption: str, fonte: str, alt: str = "") -> str:
    return row(
        f'<p class="mb-2"><strong>{caption}</strong></p>'
        f'<figure class="lightbox aos-init" data-aos="fade-up" data-aos-easing="ease-out" data-aos-duration="600">'
        f'<img class="img-fluid mx-auto d-block mb-3 rounded border" src="{MEDIA}{src}" alt="{alt or caption}" loading="lazy" />'
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
            '<a class="fio-button fio-button-primary" href="../aula4/topico1.html" rel="next">'
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
                'Seja bem-vindo e bem-vinda à aula <strong>"Fundamentos da Cartografia"</strong>.'
            )
            + p("A seguir, veja algumas informações importantes!")
        )
        + subheading("Objetivos de aprendizagem")
        + row(
            p("Ao final dessa aula, você será capaz de:")
            + ul(
                [
                    "Aprender os conceitos básicos de cartografia;",
                    "Conhecer os principais elementos cartográficos;",
                    "Conhecer os diferentes tipos de produtos cartográficos.",
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
                "A cartografia é um conjunto de técnicas usadas a fim de representar os elementos e "
                "fenômenos reconhecidos no espaço geográfico. Esse conceito derivado da necessidade do "
                "homem conhecer o mundo que ele habita (MENEZES; FERNANDES, 2013)."
            )
            + p(
                "A palavra “cartografia” tem origem na língua portuguesa, tendo sido registrada pela "
                "primeira vez em 1839 em uma correspondência, indicando a ideia de um traçado de mapas "
                "e cartas. Hoje entende Cartografia como a representação geométrica plana, simplificada "
                "e convencional de toda a superfície terrestre ou de parte desta, apresentada por meio "
                "de mapas, cartas ou plantas (IBGE, 2026)."
            )
        )
        + row(
            f'<figure class="lightbox aos-init" data-aos="fade-up" data-aos-easing="ease-out" data-aos-duration="600">'
            f'<img class="img-fluid mx-auto d-block mb-3 rounded border" src="{MEDIA}introducao-mapa.png" '
            f'alt="Mapa antigo com lupa e bússola" loading="lazy" />'
            f"</figure>"
        )
        + row(
            p(
                "Antigos exploradores e estudiosos de povos primitivos evidenciam que povos pré-históricos "
                "dominavam a habilidade do traçado de mapas muito antes de tomarem conhecimento da "
                "escrita textual (MENEZES; FERNANDES, 2013)."
            )
            + p(
                "O processo cartográfico parte da coleta de dados, envolvendo estudo, análise, composição "
                "e representação de observações, de fatos, fenômenos e dados de diferentes campos "
                "científicos associados à superfície terrestre. Ao longo dos séculos as técnicas que compõem "
                "este processo foram se aprimorando facilitando e modificando a produção e apresentação "
                "de informações geográficas."
            )
            + p(
                "O mapa é uma forma de comunicação, um instrumento de visualização de dados. Permite a "
                "comunicação gráfica e visual entre o produtor e o usuário. Porém, para que a comunicação "
                "ocorra de forma efetiva e o mapa seja entendido pelo usuário, é necessário que o mesmo "
                "tenha um conhecimento mínimo cartográfico.",
                mb0=True,
            )
        )
    )


def content_geodesico() -> str:
    return (
        heading(3, "Sistema geodésico de referência")
        + subheading("A forma da Terra")
        + row(
            p(
                "Entender a forma da Terra e as suas diferentes possibilidades de representação é "
                "imprescindível para representá-la da melhor forma em um documento cartográfico e garantir "
                "a precisão espacial dos elementos que se deseja representar. A evolução da tecnologia "
                "permitiu comprovar que a Terra não é perfeitamente redonda, nem elipsoide, mas sim um "
                "geóide que corresponde à superfície do nível médio do mar homogêneo, supostamente "
                "prolongado por sob os continentes."
            )
            + p(
                "O geóide é a forma adotada para a Terra e é sobre ela que são realizadas todas as medições. "
                "A caracterização do geóide não é matemática, porém física, em cada ponto da superfície "
                "terrestre. Sua definição é afetada pela variação das estruturas de massas terrestres."
            )
            + p(
                "Como é uma superfície irregular e de difícil tratamento matemático, foi preciso adotar, para "
                "efeito de cálculo, um modelo mais simples para representar o nosso planeta."
            )
            + p(
                "A forma matemática assumida, então, foi a elipse que ao girar em torno do seu eixo menor "
                "forma um volume, o elipsoide de revolução, achatado nos pólos. O elipsoide é a superfície de "
                "referência utilizada nos cálculos que fornecem subsídios para a elaboração de uma "
                "representação cartográfica (MENEZES; FERNANDES, 2013)."
            )
        )
        + figure_captioned(
            "figura1-geoide.png",
            "Figura 1: Geóide (NASA, CHAMP, GRACE, GFZ, DLR.)",
            'Fonte: Nasa, Earthdata. <a href="https://www.earthdata.nasa.gov/news/feature-articles/precision-behind-sea-level-rise" '
            'target="_blank" rel="noopener noreferrer">https://www.earthdata.nasa.gov/news/feature-articles/precision-behind-sea-level-rise</a>',
            "Modelo 3D do geóide terrestre",
        )
        + figure_captioned(
            "figura2-superficies.png",
            "Figura 2: Esquema de representação das superfícies terrestres (IBGE)",
            "Fonte: Adaptado de Estudo Kids (www.estudokids.com.br), CC BY-SA 4.0, adaptação por IA (Gemini).",
            "Esquema das superfícies terrestre, geóide e elipsoide",
        )
        + subheading("Sistemas geodésicos brasileiros")
        + row(
            p(
                "Os sistemas geodésicos de referência buscam uma melhor correlação entre o geóide e o "
                "elipsoide, elegendo um elipsoide de revolução que melhor se ajuste ao geóide local."
            )
            + p(
                "Alguns sistemas geodésicos de referência já foram usados no Brasil, mas o atualmente "
                "adotado é o SIRGAS 2000, que serve como referencial para América do Sul."
            )
            + p(
                "O SIRGAS 2000 entrou em vigência no ano de 2015 e seu uso obrigatório nas publicações "
                "oficiais de instituições brasileiras. A adoção do SIRGAS facilitou a integração com sistemas "
                "de posicionamento global (GPS) e aumentou a precisão cartográfica. Anteriormente "
                "adotava-se o Sistema Geodésico Sul Americano - SAD 69, que entrou em desuso a partir "
                "desta data (FITZ, 2008)."
            )
            + p(
                "É importante estar atento a essas informações acerca dos sistemas de referência do dado "
                "utilizado, pois ao usar sistemas não compatíveis, como por exemplo SAD 69 e SIRGAS 2000, "
                "onde a distância média para um mesmo ponto em SAD 69 e SIRGAS 2000 é em torno de 65 "
                "metros (IBGE, 2005)."
            )
            + p(
                "Outro sistema comumente conhecido é o sistema geodésico mundial WGS 84, que é o "
                "sistema de referência utilizado pelo GPS/ GNSS.",
                mb0=True,
            )
        )
    )


def coordenadas_table() -> str:
    return (
        '<p class="mb-2"><strong>Tabela 1: Formas de escrita e leitura de coordenadas.</strong></p>'
        '<div class="table-responsive"><table class="table table-sm table-bordered align-middle mb-0">'
        "<thead><tr>"
        '<th scope="col">Forma de escrita</th>'
        '<th scope="col">Exemplo</th>'
        '<th scope="col">Como interpretar</th>'
        "</tr></thead><tbody>"
        "<tr><td><strong>Graus Decimais (DD)</strong></td>"
        "<td>-22.9068º, -43.1729º</td>"
        "<td>O primeiro número é latitude.<br />Negativo → Sul<br />Positivo → Norte<br />"
        "O segundo é longitude.<br />Negativo → Oeste<br />Positivo → Leste</td></tr>"
        "<tr><td><strong>Graus, Minutos e Segundos (DMS)</strong></td>"
        "<td>22°54'24\"S 43°10'22\"W</td>"
        "<td>Cada coordenada tem três partes: Graus (°), Minutos ('), Segundos (\").<br />"
        "A letra final indica o hemisfério: N / S para latitude; E / W para longitude</td></tr>"
        "<tr><td><strong>UTM (Universal Transverse Mercator)</strong></td>"
        "<td>22J, E 754.134 , N 6.947.459</td>"
        "<td>Fuso/Zona: 22J (zona 22, faixa J).<br />"
        "Coordenada Leste (E): 754.134 m (distância em metros para o leste).<br />"
        "Coordenada Norte (N): 6.947.459 m (distância em metros para o norte do Equador).</td></tr>"
        "</tbody></table></div>"
    )


def content_coordenadas() -> str:
    return (
        heading(4, "Sistemas de coordenadas")
        + row(
            p(
                "Os sistemas de coordenadas são responsáveis por criar uma informação única de posição "
                "geográfica na superfície terrestre, esse posicionamento é de grande importância para a "
                "construção de documentos cartográficos. Esse posicionamento está diretamente ligado ao "
                "sistema de referência geodésico utilizado, sendo assim a coordenada determinada para um "
                "posicionamento pode variar de valor de um sistema para o outro."
            )
        )
        + subheading("Sistemas de coordenadas geográficas")
        + row(
            p(
                "Para que cada ponto da superfície da Terra pudesse ser localizado no mapa, foi criado um "
                "sistema de linhas imaginárias chamado Sistema de Coordenadas Geográficas. A coordenada "
                "geográfica de um determinado ponto da superfície da Terra é obtida pela interseção de um "
                "meridiano e um paralelo."
            )
            + p(
                "Os meridianos são linhas imaginárias que cortam a Terra no sentido norte-sul, ligando "
                "um polo ao outro. Os paralelos são linhas imaginárias que circulam a Terra no sentido "
                "leste-oeste. Paralelos e meridianos são definidos por suas dimensões de latitude e "
                "longitude, respectivamente (IBGE, 2026)."
            )
            + p(
                "As coordenadas geográficas são escritas em unidades de medida angular: grau, minuto e "
                "segundo. Inicia-se com latitude de grau zero (0º) no Equador e cada círculo paralelo a ele "
                "recebe um valor em graus que cresce para o norte ou sul. Para o norte varia de 0º a 90º e "
                "para o sul varia de 0º a -90º. Já a longitude tem como referencial inicial o Meridiano de "
                "Greenwich com o valor de zero grau, e cada linha meridiana subsequente cresce em graus "
                "para leste de 0º a 180º e para oeste de 0º a -180º."
            )
        )
        + figure_captioned(
            "figura3-meridianos-paralelos.png",
            "Figura 3: Meridianos e paralelos.",
            "Fonte: Adaptada de Conceitos básicos de sistemas de informação geográfica e cartografia "
            "aplicados à saúde, 2000 por IA Gemini.",
            "Diagramas de meridianos e paralelos",
        )
        + subheading("Sistemas de coordenadas planas")
        + row(
            p(
                "Coordenadas planas são um sistema bidimensional (x,y) usado para mapear a superfície "
                "terrestre em um plano, facilitando medições de distância e áreas. Transformam a superfície "
                "curva da Terra em uma superfície plana com um conjunto de linhas que se intersectam "
                "formando uma malha."
            )
            + p(
                "O sistema funciona através de eixos perpendiculares com uma origem definida (meridiano "
                "e paralelos). As localizações são feitas com base na distância de uma origem (0,0) ao longo "
                "de dois eixos, um eixo x horizontal representando o leste-oeste e um eixo y vertical "
                "representando o norte-sul. As coordenadas planas são convertidas de latitude e longitude "
                "em coordenadas x, y usando uma projeção de mapa (FITZ, 2008)."
            )
        )
        + figure_captioned(
            "figura4-coordenadas-planas.png",
            "Figura 4: Coordenadas planas",
            "Fonte: Elaborado pelas autoras",
            "Sistema de coordenadas planas X e Y sobre mapa",
        )
        + row(
            p(
                "Existem diversas maneiras de escrever um par de coordenadas, cada uma adaptada a "
                "necessidades específicas, como precisão, facilidade de leitura, compatibilidade com "
                "equipamentos ou padrões internacionais."
            )
        )
        + row(coordenadas_table())
    )


def content_projecoes() -> str:
    return (
        heading(5, "Projeções cartográficas")
        + row(
            p(
                "Como vimos na seção anterior, as formas terrestres e suas localizações são usualmente "
                "trabalhadas na sua representação bidimensional plana e associado a um sistema de "
                "coordenadas específicos. O processo de transformação da dimensão tridimensional da terra "
                "para dimensões planas é chamado de projeção cartográfica."
            )
            + p(
                "Um sistema de projeção cartográfica é “qualquer representação sistemática de paralelos e "
                "meridianos retratando a superfície da Terra ou parte dela, considerada como esfera ou "
                "elipsoide, sobre um plano referencial.” (SNYDER, 1987)."
            )
        )
        + figure_captioned(
            "figura5-projecao.png",
            "Figura 5: Projeção cartográfica",
            'Fonte: Adaptada pelo autor de <a href="https://commons.wikimedia.org/" target="_blank" '
            'rel="noopener noreferrer">https://commons.wikimedia.org/</a>',
            "Transformação do globo em mapa plano",
        )
        + row(
            p(
                "Como essa transformação não pode ocorrer sem a introdução de distorções, torna-se "
                "necessário selecionar quais propriedades — como área, forma, distância ou direção — serão "
                "preservadas, implicando a perda parcial de outras. Em representações de grande extensão "
                "territorial, as distorções tornam-se mais evidentes, enquanto em áreas reduzidas podem ser "
                "minimizadas dependendo da projeção adotada. Embora exista um número infinito de "
                "projeções possíveis, apenas algumas centenas foram formalmente desenvolvidas e "
                "publicadas, muitas das quais possuem uso limitado. Além disso, a maioria das projeções pode "
                "ser modificada ao se alterar o ponto central ou o ponto de origem na superfície terrestre, "
                "ampliando ainda mais suas variações (SNYDER, 1987)."
            )
            + p(
                "As projeções cartográficas são classificadas, principalmente, quanto à superfície de projeção "
                "e às propriedades."
            )
            + p(
                "Quanto à superfície de projeção: Podem ser projeções planas, cônicas ou cilíndricas, quando "
                "forem utilizadas as superfícies de um plano, cone ou cilindro como base para planificar a "
                "esfera terrestre (IBGE, 2026)."
            )
        )
        + figure_captioned(
            "figura6-superficies-projecao.png",
            "Figura 6: Superfícies de projeção",
            "Fonte: Adaptada pelo autor de Atlas Escolar IBGE.",
            "Projeções plana, cilíndrica e cônica",
        )
        + row(
            p(
                "As superfícies de projeção podem ser polares (tangentes ao polo), equatoriais (tangentes ao "
                "Equador) ou oblíquas (tangentes a qualquer ponto da Terra). Na planificação da superfície "
                "terrestre ocorrem deformações, podendo preservar apenas ângulos (conforme), áreas "
                "(equivalente) ou distâncias (equidistante). Projeções como Mercator, Miller, Behrmann e "
                "Robinson representam o mundo. No Brasil, destacam-se as projeções Mercator e "
                "policônica, sendo esta utilizada no mapeamento oficial em escala geográfica e a cônica "
                "conforme de Lambert na escala 1:1.000.000."
            )
        )
        + figure_captioned(
            "figura7-preservacoes.png",
            "Figura 7: Tipos de preservações de distorções de projeção.",
            "Fonte: Adaptada pelo autor de Atlas Escolar IBGE.",
            "Projeções conforme, equivalente e equidistante",
        )
        + subheading("Projeção Universal Transversa de Mercator (UTM)")
        + row(
            p(
                "É um sistema de coordenadas cartesianas e métricas utilizado para mapear a superfície "
                "terrestre com alta precisão em escala local. Diferente das coordenadas geográficas "
                "(latitude e longitude), que usam graus, a UTM utiliza metros. Trata-se de uma projeção "
                "cilíndrica e conforme, mantém a forma das pequenas áreas e os ângulos, sendo ideal para "
                "engenharia e topografia. Onde o cilindro é transverso, onde o eixo do cilindro está no eixo "
                "do Equador e tangente ao meridiano (FITZ, 2008)."
            )
        )
        + figure_captioned(
            "figura8-utm.png",
            "Figura 8: Projeção UTM.",
            "Fonte: Adaptado de Manual Técnico de geodésia, IBGE, 1999.",
            "Esquema da projeção UTM e fusos",
        )
        + row(
            p(
                "O planeta Terra é dividido em 60 faixas verticais chamadas fusos, cada uma com 6 graus "
                "de largura em longitude. Esses fusos são numerados de 1 a 60, começando no meridiano "
                "de 180° Oeste e seguindo em direção ao Leste. Cada fuso possui um meridiano central, "
                "que fica bem no meio da faixa e serve como referência para projetar o mapa com menor "
                "distorção (IBGE, 2015)."
            )
            + p(
                "O sistema UTM utiliza uma grade retangular para localizar pontos na superfície terrestre. "
                "Um dos eixos dessa grade acompanha o meridiano central, apontando para o Norte, "
                "enquanto o outro segue a linha do Equador, na direção Leste-Oeste. Com isso, cada ponto "
                "da Terra pode ser identificado por três informações: a zona UTM, a coordenada Leste (E) "
                "e a coordenada Norte (N) (IBGE, 2015)."
            )
            + p(
                "Essa projeção apresenta pequenas distorções de escala. No meridiano central, a escala "
                "é praticamente perfeita, com fator igual a 1. Já nas bordas do fuso, esse fator pode chegar "
                "a aproximadamente 1,0015. Para reduzir essas distorções, o sistema adota um fator "
                "de escala de 0,9996 no meridiano central, fazendo com que o cilindro de projeção corte "
                "a Terra em vez de apenas tocá-la. Isso ajuda a manter a precisão da escala ao longo de "
                "todo o fuso (IBGE, 2015)."
            )
            + p(
                "Cada fuso possui seu próprio sistema de coordenadas. No Equador, a coordenada Leste "
                "começa em 500.000 metros. Já a coordenada Norte começa em 0 metros no hemisfério "
                "norte e em 10.000.000 metros no hemisfério sul. Essa convenção evita que apareçam "
                "valores negativos nas coordenadas (IBGE, 2015)."
            )
            + p(
                "Além disso, cada fuso se estende por 30 minutos de arco sobre os fusos vizinhos, "
                "criando uma faixa de sobreposição de 1 grau. Essa área adicional facilita o trabalho de "
                "campo em regiões próximas às bordas dos fusos (IBGE, 2015)."
            )
            + p(
                "O sistema UTM é utilizado para áreas situadas entre as latitudes 84° Norte e 80° Sul. "
                "Fora desses limites, outras projeções cartográficas são mais adequadas (IBGE, 2015)."
            )
            + p("As componentes de uma coordenada UTM são:")
            + ol(
                [
                    "Zona/Fuso (ex: 23)",
                    "Banda de Latitude ou Hemisfério (ex: S para Sul)",
                    "Coordenada Este (E) em metros",
                    "Coordenada Norte (N) em metros",
                ]
            )
        )
        + figure_captioned(
            "figura9-zonas-utm-global.png",
            "Figura 9: Zonas UTM Globais.",
            'Fonte: <a href="https://www.mensurarjunior.com/post/fusos-utm" target="_blank" '
            'rel="noopener noreferrer">https://www.mensurarjunior.com/post/fusos-utm</a>',
            "Mapa mundial com zonas UTM",
        )
        + row(
            p(
                "Quando utilizamos as coordenadas UTM é fundamental conhecer a numeração do fuso "
                "ou a coordenada do Meridiano Central de origem das coordenadas, pois são os parâmetros "
                "que distinguem os fusos, já que as coordenadas se repetem para cada fuso (IBGE, 1999)."
            )
            + p(
                "Para o Brasil, as coordenadas acima do Equador são contadas crescendo sequencialmente a "
                "partir de 10000000 m, para facilitar os cálculos, já que quase toda a extensão do Brasil está "
                "no hemisfério sul. A simbologia adotada para as coordenadas UTM é: N (para norte-sul) "
                "e E (para leste-oeste) (IBGE, 1999)."
            )
        )
        + figure_captioned(
            "figura10-zonas-utm-brasil.png",
            "Figura 10: Zonas UTM Brazil.",
            "Fonte: Cap. 2 - Sistemas de Informações Geográficas em saúde. Em: CARVALHO, Marilia Sá; "
            "PINA, Maria de Fátima de; SANTOS, Simone Maria dos (org.). Conceitos básicos de sistemas "
            "de informação geográfica e cartografia aplicados à saúde.",
            "Zonas UTM no Brasil e esquema de origem",
        )
    )


def content_escala() -> str:
    return (
        heading(6, "Conceito de escala")
        + row(
            p(
                "A representação espacial se dá através da redução do mundo real, sendo assim a escala "
                "é um elemento essencial para os projetos cartográficos. A escolha da escala influencia "
                "diretamente na interpretação das informações contidas no documento cartográfico e "
                "permite a visualização da informação geográfica em diferentes níveis de detalhamento "
                "(MENEZES; FERNANDES, 2013)."
            )
            + p(
                "A escala é um fator determinante para a delimitação do espaço físico, grau de detalhamento "
                "de uma representação ou identificação de feições. É a razão entre uma medida efetuada no "
                "mapa e sua medida real na superfície terrestre (MENEZES; FERNANDES, 2013)."
            )
            + p(
                "Quando se planeja um mapa tem que se determinar a escala certa considerando a finalidade "
                "do mapa e conveniência da escala que define a sua construção. Portanto, a escala pode ser "
                "entendida como medida que traz a visibilidade ao fenômeno, funcionando como um recorte "
                "espacial dando sentido ao que se deseja observar (MENEZES; FERNANDES, 2013)."
            )
            + p(
                "Uma escala pode ser expressa por uma fração representativa ou numérica, por palavras ou "
                "escrita e por meio de uma escala de barras conhecida como escala gráfica."
            )
        )
        + figure_captioned(
            "figura11-tipos-escalas.png",
            "Figura 11: Tipos de escalas.",
            "Fonte: Adaptada pelo autor de Atlas Escolar IBGE.",
            "Escalas numéricas e gráficas",
        )
        + row(
            p(
                "Quanto maior a escala de um mapa, maior o nível de detalhamento e quantidade de "
                "informação representada, menor a área de abrangência mapeada."
            )
        )
        + figure_captioned(
            "figura12-escala-detalhamento.png",
            "Figura 12: Diferença entre escala e detalhamento.",
            "Fonte: Adaptada pelo autor de Atlas Escolar IBGE.",
            "Mapas em diferentes escalas mostrando detalhamento",
        )
        + row(
            p(
                "A escala é a razão onde o denominador representa o comprimento da distância no "
                "desenho e o denominador o comprimento real no terreno. Sendo assim, quando temos uma "
                "escala 1/50000, podemos interpretar que uma unidade no mapa (cm ou mm) corresponde a "
                "50000 vezes a mesma medida no terreno (MENEZES; FERNANDES, 2013)."
            )
            + p(
                "O uso da escala gráfica auxilia na determinação dessa razão, onde podemos medir sobre ela "
                "com uma régua em cm ou mm quantos km são representados no mapa."
            )
            + p(
                "É importante lembrar que os mapas digitais, ao contrário dos mapas analógicos, são "
                "dinâmicos e não possuem uma escala fixa. Basta uma simples operação de zoom para alterar "
                "a escala do mapa. Isto não significa que não seja importante o conhecimento sobre a escala "
                "original do mapa, que deu origem ao mapa digital. Ao contrário, é fundamental esse "
                "conhecimento, pois a todo mapa está associado um erro gráfico, que é função direta da "
                "escala (MENEZES; FERNANDES, 2013)."
            )
        )
        + subheading("Erro e precisão gráfica")
        + row(
            p(
                "A escala está diretamente ligada à precisão de representação do que está sendo observado. "
                "Quando se adquire dados derivados de um mapeamento, é importante avaliar o erro gráfico já "
                "inerente à sua escala de representação. Uma vez em uma determinada escala o dado só pode "
                "servir para uso da escala que foi adquirido, não podendo ser trabalhado em outras "
                "representações, em outras escalas (IBGE, 2015)."
            )
            + p(
                "A precisão gráfica é a menor grandeza medida no terreno, capaz de ser representada em "
                "desenho na mencionada escala. Um olho humano permite distinguir uma medida linear de "
                "aproximadamente 0,1 mm, e para um ponto em torno de 0,2 mm. Sendo assim, o menor "
                "comprimento gráfico que se pode representar em um desenho é de 0,2 mm, que é a menor "
                "medida que o olho humano é capaz de distinguir. Esse valor foi então adotado como a "
                "precisão gráfica e caracteriza o erro gráfico vinculado à escala de representação "
                "(MENEZES; FERNANDES, 2013)."
            )
            + p(
                "Sabendo que o valor fixo da precisão gráfica de um mapa é 0,2 mm, podemos calcular a "
                "precisão de um dado conhecendo a sua escala da seguinte maneira:"
            )
            + p("E= 1:20.000 ------- 0,2 mm = 4.000 mm = 4 m (E = 0,0002 m × 20.000)")
            + p("E= 1:10.000 ------- 0,2 mm = 2.000 mm = 2 m (E = 0,0002 m × 10.000)")
            + p(
                "Para a escolha da escala mais adequada para um mapeamento usamos esse mesmo cálculo, "
                "mas consideramos o menor elemento que se quer representar e dividimos pelo erro gráfico. "
                "Sendo assim, se quero o menor elemento tendo 10 m, devo calcular 10 m / 0,0002 = 50000 m. "
                "Logo teremos uma escala de 1/50.000.",
                mb0=True,
            )
        )
    )


def content_tematica() -> str:
    return (
        heading(7, "Cartografia temática e simbologia")
        + subheading("Cartografia temática")
        + row(
            p(
                "O objetivo da cartografia temática é representar, utilizando-se símbolos qualitativos "
                "e/ou quantitativos, fenômenos localizáveis de qualquer natureza sobre uma base de "
                "referência, geralmente um mapa topográfico, em quaisquer escalas, em que sobre um "
                "fundo geográfico básico."
            )
            + p(
                "Nesse tipo de mapa são representados os fenômenos geográficos, geológicos, demográficos, "
                "econômicos, agrícolas etc., visando ao estudo, à análise e à pesquisa dos temas, no seu "
                "aspecto espacial. É a combinação de uma base gráfica existente com o tema que se queira "
                "mapear, auxiliado por símbolos."
            )
            + p(
                "A cartografia temática é uma subdivisão da cartografia, que, por sua vez pode ser subdividida "
                "conforme a abordagem e a finalidade do mapeamento. Os Mapas qualitativos mostram "
                "categorias (qualidades), ou seja, mostram a distribuição espacial ou localização de "
                "determinadas características da região mapeada. Não se pode determinar quantidades, nem "
                "criar uma ordem hierárquica de classes. Os mapas quantitativos apresentam a distribuição de "
                "uma determinada variável, ou seja, mostram o quanto de uma determinada variável está "
                "presente em uma área (MENEZES; FERNANDES, 2013)."
            )
        )
        + figure_captioned(
            "figura13-mapas-tematicos.png",
            "Figura 13: Mapas temáticos.",
            "Fonte: Prefeitura do Município do Rio de Janeiro (2009) e IBGE (2010).",
            "Mapas qualitativo e quantitativo",
        )
        + subheading("Simbologia cartográfica")
        + row(
            p(
                "Um mapa ou carta só está completo quando apresenta corretamente seus elementos "
                "cartográficos. Como a escala reduz os elementos do mundo real, muitas vezes é "
                "necessário utilizar simbologias para representar fenômenos geográficos que ficariam "
                "imperceptíveis (IBGE, 1999)."
            )
            + p(
                "A cartografia utiliza um sistema de comunicação visual, que conecta o mundo real, o "
                "cartógrafo e o usuário, buscando facilitar a compreensão das informações representadas. "
                "Os elementos do espaço geográfico são representados por símbolos chamados convenções "
                "cartográficas, pois não é possível desenhar os objetos exatamente como são na realidade. "
                "Esses símbolos são explicados na legenda do mapa (IBGE, 1999)."
            )
            + p(
                "Para que o mapa seja compreendido corretamente, ele deve conter elementos básicos como "
                "título, escala, legenda, corpo do mapa, seta norte, autor, data, projeção, fonte dos dados e "
                "linha de borda. Assim, a simbologia cartográfica permite identificar, localizar e analisar a "
                "distribuição dos fenômenos geográficos representados no mapa (IBGE, 1999)."
            )
        )
        + figure_captioned(
            "figura14-elementos-mapa.png",
            "Figura 14: Elementos de um mapa.",
            "Fonte: Adaptada pelo autor de IBGE.",
            "Elementos cartográficos em um mapa",
        )
        + row(
            p(
                "Os cartógrafos empregam símbolos para representar a localização, direção, distância, "
                "movimento, função, processo e correlação. Estas características do mundo real são abstraídas "
                "e simbolizadas em mapas como pontos, linhas e áreas. Muita prática e habilidade estão "
                "envolvidas na escolha de estratégias eficazes para a simbolização."
            )
            + p(
                "Uma das melhores maneiras de aprender sobre essas estratégias é considerar os tipos "
                "de recursos visuais disponíveis para o cartógrafo (FOOTE; CRUM, 1995)."
            )
            + p(
                "Como os cartógrafos reduzem o mundo a pontos, linhas e áreas, utiliza-se uma variedade de "
                "recursos visuais, utilizando as categorias de tamanho, forma, valor, textura ou padrão, cor e "
                "orientação (FOOTE; CRUM, 1995)."
            )
        )
        + figure_captioned(
            "figura15-recursos-visuais.png",
            "Figura 15: Recursos visuais cartográficos.",
            "Fonte: A Cartografia de Joly F., 2005.",
            "Variáveis visuais pontual, linear e zonal",
        )
        + row(
            p(
                "Além dos símbolos a cor tem um significado no mapa e pode auxiliar na leitura das "
                "informações a ele associadas e devem ser utilizadas com cuidado. Elas devem servir a um "
                "propósito e não ser usadas indiscriminadamente."
            )
            + p(
                "As cores em mapas coropléticos são utilizadas para representar a variação de valores de um "
                "fenômeno em diferentes áreas geográficas, como municípios, estados ou regiões. Nesse tipo "
                "de mapa, as cores funcionam como um recurso visual que facilita a compreensão da "
                "distribuição espacial dos dados, permitindo identificar padrões, diferenças e concentrações "
                "de determinado fenômeno no território."
            )
            + p(
                "Entre os principais tipos de rampas de cores utilizadas em mapas coropléticos destacam-se "
                "as rampas sequenciais e as divergentes. As rampas sequenciais utilizam variações de uma "
                "mesma cor, geralmente do tom mais claro para o mais escuro, indicando respectivamente "
                "valores menores e maiores. Já as rampas divergentes utilizam duas cores que partem de um "
                "ponto central neutro, sendo indicadas quando se deseja evidenciar valores acima ou abaixo de "
                "uma média ou referência (BREWER, 1994)."
            )
        )
        + figure_captioned(
            "figura16-coropleticos.png",
            "Figura 16: Recursos visuais coropléticos.",
            "Fonte: Imagem criada pelo autor com IA ChatGPT.",
            "Exemplos de mapa coroplético e rampas de cores",
        )
    )


def content_referencias() -> str:
    items = "".join(f'<p class="referencias-item">{ref}</p>' for ref in REFERENCES)
    return heading(8, "Referências") + row(f'<div class="referencias-aula">{items}</div>')


CONTENT_BUILDERS = [
    content_sobre,
    content_introducao,
    content_geodesico,
    content_coordenadas,
    content_projecoes,
    content_escala,
    content_tematica,
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
