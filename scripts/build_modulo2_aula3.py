#!/usr/bin/env python3
"""Gera HTML da Aula 2.3 (Prática com Excel e Joinpoint) a partir do PDF validado — sem alterar textos."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "modulo2" / "aula3"
MEDIA = "../../media/modulo2/aula3/"
ASSETS = "../../"

COURSE_TITLE = "Análise e Interpretação de Dados em Saúde"
MODULE_NUM = 2
MODULE_TITLE = "Séries Temporais"
AULA_LABEL = "Aula 3"
AULA_TITLE = "Análise de Série Histórica - Prática com Excel e Joinpoint"

TOPICS = [
    "Sobre esta aula",
    "Introdução",
    "Análise de Tendência com Microsoft Excel",
    "Interpretando os Resultados do Excel",
    "Análise de Tendência com Joinpoint",
    "Conclusão",
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


def figure_captioned(src: str, caption: str, fonte: str, alt: str = "") -> str:
    return row(
        f'<p class="mb-2"><strong>{caption}</strong></p>'
        f'<figure class="lightbox aos-init" data-aos="fade-up" data-aos-easing="ease-out" data-aos-duration="600">'
        f'<img class="img-fluid mx-auto d-block mb-3 rounded border" src="{MEDIA}{src}" alt="{alt}" loading="lazy" />'
        f"</figure>"
        f'<p class="figure-caption fonte small mb-0">{fonte}</p>'
    )


def figure_plain(src: str, alt: str = "", *, caption: str = "") -> str:
    cap = f'<p class="mb-2"><strong>{caption}</strong></p>' if caption else ""
    return row(
        cap
        + f'<figure class="lightbox aos-init" data-aos="fade-up" data-aos-easing="ease-out" data-aos-duration="600">'
        f'<img class="img-fluid mx-auto d-block mb-3 rounded border" src="{MEDIA}{src}" alt="{alt}" loading="lazy" />'
        f"</figure>"
    )


def box(kind: str, label: str, body: str) -> str:
    return row(
        f'<div class="box" data-box="{kind}"><div class="card"><div class="card-header">'
        f'<span class="icone material-symbols-rounded" aria-hidden="true"></span>'
        f'<span class="label">{label}</span></div><div class="card-body">'
        f"{body}</div></div></div>"
    )


def saiba_mais_toggle(collapse_id: str, label: str, body: str) -> str:
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
        f"{body}"
        f"</div></div></div></div>"
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
            '<a class="fio-button fio-button-primary" href="../../modulo3/aula1/topico1.html" rel="next">'
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
            p('Seja bem-vindo e bem-vinda à aula “Análise de Série Histórica - Prática com Excel e Joinpoint”.')
            + p("A seguir, veja algumas informações importantes!")
        )
        + subheading("Objetivos de aprendizagem")
        + row(
            p("Ao final dessa aula, você será capaz de:")
            + '<div class="list"><ul class="list-group">'
            + '<li class="list-group-item">Organizar uma base de dados de série temporal para análise;</li>'
            + '<li class="list-group-item">Realizar uma análise de tendência linear simples utilizando o Microsoft Excel;</li>'
            + '<li class="list-group-item">Interpretar os resultados de uma linha de tendência do Excel, incluindo a equação '
            "da reta e o R²;</li>"
            + '<li class="list-group-item">Compreender o conceito de regressão por pontos de inflexão (joinpoint) e suas vantagens;</li>'
            + '<li class="list-group-item">Interpretar os resultados de uma análise do software Joinpoint, incluindo o APC e o AAPC.</li>'
            + "</ul></div>"
        )
        + subheading("Autoria")
        + row(
            p("<strong>Diego Ricardo Xavier</strong>")
            + p(
                "Doutor em Epidemiologia. Mestrado em Saúde Pública. Pesquisador em Saúde Pública "
                "no Instituto de Comunicação e Informação Científica e Tecnológica em Saúde (Icict) da "
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
    importante_body = (
        "<p class=\"mb-0\">Para esta aula prática, utilizaremos uma base de dados simulada "
        "de taxas de mortalidade por uma doença fictícia entre os anos 2000 e "
        "2020. Baixe o arquivo em formato de Excel: "
        f'<a href="{MEDIA}dados_aula2_3.xlsx" download>dados_aula2_3.xlsx</a>.</p>'
    )
    return (
        heading(2, "Introdução")
        + row(
            p(
                "Nesta aula, exploraremos duas abordagens complementares para a análise de tendências: "
                "uma utilizando um software de ampla disponibilidade, o Microsoft Excel, e outra com um "
                "software estatístico especializado e gratuito, o Joinpoint, desenvolvido pelo Instituto "
                "Nacional do Câncer dos EUA (NATIONAL CANCER INSTITUTE, 2026). Aqui, nosso foco "
                "não será a execução técnica detalhada dos softwares, mas sim a interpretação dos "
                "resultados e as possibilidades de aplicação de cada método."
            )
        )
        + figure_plain("intro-notebook.png", "Pessoa utilizando notebook")
        + row(
            p(
                "Enquanto o Excel permite uma análise de tendência linear simples e rápida, o Joinpoint "
                "oferece um método mais sofisticado, a regressão por pontos de inflexão, que identifica "
                "mudanças significativas na tendência ao longo do tempo (KIM et al., 2000)."
            )
        )
        + box("Importante", "IMPORTANTE!", importante_body)
    )


def content_excel() -> str:
    return (
        heading(3, "Análise de Tendência com Microsoft Excel")
        + row(
            p(
                "O Excel é uma ferramenta poderosa para uma análise exploratória inicial da tendência de "
                "uma série temporal. O processo é visual e baseado na inserção de uma linha de tendência "
                "em um gráfico."
            )
        )
        + subheading("Passo a Passo no Excel")
        + row(
            p(
                '<strong>1 Organizar os Dados:</strong> Abra o arquivo dados_aula2_3.xlsx no Excel. Você terá '
                'duas colunas: "Ano" e "Taxa de Mortalidade".'
            )
            + p(
                'Observe que cada célula da coluna “Ano” deve estar formatada como texto ou '
                'precedido de apóstrofo e “Taxa de Mortalidade” como número com duas casas decimais.'
            )
        )
        + figure_plain("excel-passo1-dados.png", "Planilha Excel com anos formatados como texto")
        + row(
            p('Deixe as colunas “Ano e “Taxa de Mortalidade” selecionadas (ficam em cinza).')
        )
        + figure_plain("excel-passo1-selecao.png", "Seleção das colunas Ano e Taxa de Mortalidade")
        + row(
            p(
                "<strong>2 Criar o Gráfico:</strong> Mantenha todos os dados selecionados (incluindo os cabeçalhos). "
                "Vá em Inserir &gt; Gráficos &gt; Linhas &gt; Linhas com Marcadores."
            )
        )
        + figure_plain("excel-passo2-grafico.png", "Inserir gráfico de linhas com marcadores no Excel")
        + row(
            p("<strong>3 Adicionar Linha de Tendência:</strong>")
            + '<div class="list"><ul class="list-group">'
            + '<li class="list-group-item">Clique com o botão direito sobre a linha de dados no gráfico.</li>'
            + '<li class="list-group-item">Selecione a opção "Adicionar Linha de Tendência".</li>'
            + "</ul></div>"
        )
        + figure_plain("excel-passo3-menu-tendencia.png", "Menu Adicionar Linha de Tendência")
        + row(
            p(
                "Para modificar a cor ou a espessura das linhas. Clique duas vezes em cima da "
                "linha dentro do gráfico. No painel de formatação que se abrirá, escolha a opção "
                "Linha de Preenchimento (botão do “baldinho”). Neste exemplo, modificou-se a "
                "cor da linha de tendência para vermelho."
            )
        )
        + figure_plain("excel-passo3-cor.png", "Formatação da cor da linha de tendência")
        + row(
            p(
                "Para colocar um contorno na caixa da Equação no gráfico. Primeiro clique na caixa "
                "dentro do gráfico, depois em Formatar e por último em contorno da forma."
            )
        )
        + figure_plain("excel-passo3-contorno.png", "Formatação do contorno da caixa da equação")
        + row(
            p('No painel de formatação que se abrirá, escolha a opção Linear.')
        )
        + figure_plain("excel-passo3-linear.png", "Opção Linear no painel de formatação")
        + row(
            p("<strong>4 Exibir a Equação e o R²:</strong>")
            + '<div class="list"><ul class="list-group">'
            + '<li class="list-group-item">Ainda no mesmo painel, role para baixo e marque as caixas de seleção '
            '"Exibir Equação no gráfico" e "Exibir valor de R-quadrado no gráfico".</li>'
            + "</ul></div>"
        )
        + figure_plain("excel-passo4-equacao.png", "Exibir equação e R-quadrado no gráfico")
        + row(
            p("<strong>5 Incluir elementos do Gráfico:</strong>")
            + '<div class="list"><ul class="list-group">'
            + '<li class="list-group-item">Selecione o gráfico e clique no botão .</li>'
            + '<li class="list-group-item">Selecione os itens: Títulos dos eixos e Legenda (neste exemplo, na parte inferior) '
            "para inserir no gráfico.</li>"
            + '<li class="list-group-item">Para nomear os Títulos dos eixos basta clicar na caixa de cada item e escrever '
            "o título do eixo.</li>"
            + "</ul></div>"
        )
        + figure_plain("excel-passo5-elementos.png", "Elementos do gráfico no Excel")
        + figure_plain("excel-passo5-eixos.png", "Títulos dos eixos no gráfico")
        + row(
            p("<strong>6 Formatar o Gráfico:</strong>")
            + '<div class="list"><ul class="list-group">'
            + '<li class="list-group-item">Com o gráfico selecionado, você pode formatar o tipo, tamanho e a cor da fonte. '
            "Neste exemplo optou-se pela fonte tipo: Calibri, negrito, 10 e preta.</li>"
            + "</ul></div>"
        )
        + figure_plain("excel-passo6-fonte.png", "Formatação da fonte do gráfico")
        + row(p("O resultado será semelhante à Figura 1."))
        + figure_captioned(
            "figura1-excel.png",
            "Figura 1 – Simulação de uma análise de tendência linear no Excel",
            "Fonte: Elaborado pelo autor (2026).",
            "Gráfico de tendência linear no Excel com equação e R²",
        )
    )


def content_interpretando_excel() -> str:
    return (
        heading(4, "Interpretando os Resultados do Excel")
        + accordion(
            "m2a3-excel-resultados",
            [
                (
                    "Linha de Tendência:",
                    "<p class=\"mb-0\">A inclinação da linha tracejada indica a direção da tendência. Neste caso, a linha desce "
                    "da esquerda para a direita, indicando uma tendência de queda, significa que, ao longo "
                    "dos anos, a taxa de mortalidade vem diminuindo.</p>",
                ),
                (
                    "Equação da Reta (y = -1,188x + 2409,77):",
                    "<p><strong>Confiabilidade:</strong></p>"
                    "<p class=\"mb-0\">O coeficiente que multiplica x (neste caso, -1,188) é o mais importante. Ele diz quanto o "
                    "valor muda a cada unidade de tempo (ano). Neste exemplo como é negativo, indica queda "
                    "e mostra que, em média, a taxa de mortalidade diminuiu 1,188 pontos a cada ano.</p>",
                ),
                (
                    "Intercepto (2409,77):",
                    "<p class=\"mb-0\">É o valor de y quando x = 0. Na prática, muitas vezes não tem significado direto "
                    "(especialmente se “ano zero” não faz sentido no contexto), mas ajuda a construir a reta.</p>",
                ),
                (
                    "R-quadrado (R² = 0,9448):",
                    "<p class=\"mb-0\">Esse é um indicador de qualidade do ajuste da linha. Seu valor varia de 0 a 1. "
                    "Quanto mais perto de 1, melhor a linha explica os dados. No exemplo 0,9448 = 94,48%. "
                    "Isso significa que a linha explica quase toda a variação dos dados. Ou seja, os dados "
                    "seguem muito bem essa tendência de queda — não estão muito “espalhados”. "
                    "Dizemos que é um ajuste muito bom.</p>",
                ),
            ],
        )
    )


def content_joinpoint() -> str:
    saiba_body = (
        "<p class=\"mb-0\">Se você deseja se aprofundar no uso do Joinpoint, conhecer exemplos de análises, "
        "consultar a documentação completa ou baixar o software, o Instituto Nacional "
        "do Câncer dos Estados Unidos mantém uma página oficial dedicada ao programa. "
        "O site apresenta tudo o que você precisa: descrição detalhada do método, "
        "materiais de apoio, exemplos práticos, versões atualizadas do software e "
        "instruções de instalação. Acesse: "
        '<a href="https://surveillance.cancer.gov/joinpoint/" target="_blank" rel="noopener noreferrer">'
        "https://surveillance.cancer.gov/joinpoint/</a></p>"
    )
    return (
        heading(5, "Análise de Tendência com Joinpoint (Exemplo Teórico)")
        + row(
            p(
                "O Joinpoint é um software estatístico desenvolvido pelo National Cancer Institute (NCI), "
                "nos Estados Unidos, e amplamente utilizado para analisar tendências temporais em dados "
                "de saúde, como taxas de mortalidade e incidência. A análise de regressão joinpoint (pontos "
                "de inflexão) descreve as alterações em tendências de dados, identificando os pontos no "
                "tempo em que ocorrem mudanças significativas. O método ajusta o modelo de regressão "
                "mais simples que os dados permitem, testando se múltiplos segmentos de reta são "
                "estatisticamente melhores para descrever a série do que uma única reta (NATIONAL "
                "CANCER INSTITUTE, 2026) (BRITO et al., 2016)."
            )
        )
        + subheading("Conceitos-Chave do Joinpoint")
        + accordion(
            "m2a3-joinpoint-conceitos",
            [
                (
                    "Joinpoint (Ponto de Inflexão):",
                    "<p class=\"mb-0\">É um ponto no tempo (um ano) onde a tendência sofre uma mudança significativa, "
                    "isto é, são os pontos onde a inclinação da linha de tendência muda.</p>",
                ),
                (
                    "Annual Percent Change (APC):",
                    "<p class=\"mb-0\">É a variação percentual anual para cada segmento de reta identificado entre os joinpoints. "
                    "Mede a velocidade da tendência em cada período, ou seja, o grau de subida ou descida "
                    "em cada trecho.</p>",
                ),
                (
                    "Average Annual Percent Change (AAPC):",
                    "<p class=\"mb-0\">É uma média ponderada dos APCs, resumindo a tendência ao longo de todo o "
                    "período analisado.</p>",
                ),
            ],
        )
        + subheading("Interpretando um Resultado do Joinpoint")
        + row(
            p(
                "Imagine que aplicamos a análise de Joinpoint aos nossos dados (dados_aula2_3.xls). "
                "O software poderia identificar que a queda na mortalidade não foi constante. Ele poderia, "
                "por exemplo, encontrar um joinpoint em 2008, como na Figura 2."
            )
        )
        + figure_captioned(
            "figura2-joinpoint.png",
            "Figura 2 – Simulação de um resultado da análise de regressão Joinpoint",
            "Fonte: Elaborado pelo autor (2026).",
            "Gráfico Joinpoint com ponto de inflexão em 2008",
        )
        + row(
            p(
                "A imagem mostra uma análise de tendências temporais utilizando regressão por pontos "
                "de inflexão (Joinpoint). Observações anuais de uma taxa de mortalidade (por 100.000 "
                "habitantes) entre 2000 e 2020 (pontos azuis)."
            )
            + p("Neste exemplo, a interpretação seria:")
            + '<div class="list"><ul class="list-group">'
            + '<li class="list-group-item">Um ponto de inflexão foi identificado em 2008, dividindo a série em dois períodos com '
            "tendências distintas indicado pela linha vertical tracejada.</li>"
            + '<li class="list-group-item">De 2000 a 2008: Houve uma tendência de queda significativa, com uma Variação '
            "Percentual Anual (APC) de -5,0% ao ano (linha laranja).</li>"
            + '<li class="list-group-item">De 2008 a 2020: A tendência de queda continuou, com um APC de -5,1% ao ano, '
            "embora com uma inclinação ligeiramente diferente (linha verde).</li>"
            + "</ul></div>"
            + p("Por este método conseguimos avaliar que:")
            + '<div class="list"><ol class="list-group list-group-numbered">'
            + '<li class="list-group-item">Houve redução contínua da taxa de mortalidade entre 2000 e 2020.</li>'
            + '<li class="list-group-item">O modelo Joinpoint detectou uma mudança significativa em 2008, separando o '
            "período em duas fases de declínio.</li>"
            + '<li class="list-group-item">Apesar da mudança formal detectada, a velocidade de queda é muito similar antes '
            "e depois de 2008.</li>"
            + '<li class="list-group-item">Ambos os segmentos têm significância estatística, reforçando que a tendência '
            "de queda é robusta.</li>"
            + "</ol></div>"
            + p(
                "Esta análise, mais detalhada, permite entender nuances que a análise linear única do "
                "Excel não captura. Ela mostra não apenas se a tendência mudou, mas também quando "
                "e com que intensidade."
            )
        )
        + saiba_mais_toggle("saiba-mais-joinpoint", "SABIA MAIS!", saiba_body)
    )


def content_conclusao() -> str:
    return (
        heading(6, "Conclusão")
        + row(
            p(
                "O Excel é uma excelente porta de entrada para a análise de séries históricas, permitindo "
                "uma avaliação rápida e visual da tendência geral. Para uma análise mais aprofundada e "
                "publicável, que investiga mudanças na tendência ao longo do tempo, o Joinpoint é a "
                "ferramenta padrão-ouro, amplamente utilizada em estudos epidemiológicos no Brasil e "
                "no mundo (BRITO et al., 2016) (SOUZA et al., 2019).",
                mb0=True,
            )
        )
    )


def content_referencia() -> str:
    return (
        heading(7, "REFERÊNCIA")
        + row(
            '<div class="referencias-aula">'
            '<p class="referencias-item">BRITO, A. L.; MONTEIRO, L. D.; RAMOS JR., A. N. et al. '
            "Tendência temporal da hanseníase em uma capital do Nordeste do Brasil: epidemiologia e "
            "análise por pontos de inflexão, 2001 a 2012. "
            "<em>Revista Brasileira de Epidemiologia</em>, v. 19, n. 1, p. 194-204, 2016.</p>"
            '<p class="referencias-item">KIM, H. J.; FAY, M. P.; FEUER, E. J.; MIDTHUNE, D. N. '
            "Permutation tests for joinpoint regression with applications to cancer rates. "
            "<em>Statistics in Medicine</em>, v. 19, n. 3, p. 335-351, 2000.</p>"
            '<p class="referencias-item">NATIONAL CANCER INSTITUTE. Joinpoint Regression Program. '
            "Surveillance Research Program. Disponível em: "
            '<a href="https://surveillance.cancer.gov/joinpoint/" target="_blank" rel="noopener noreferrer">'
            "https://surveillance.cancer.gov/joinpoint/</a>. Acesso em: 19 fev. 2026.</p>"
            '<p class="referencias-item">SOUZA, C. D. F.; LUNA, C. F.; GURGEL, A. M. et al. '
            "Transmissão da hanseníase na Bahia, 2001-2015: modelagem a partir de regressão por pontos "
            "de inflexão e estatística de varredura espacial. "
            "<em>Epidemiologia e Serviços de Saúde</em>, v. 28, n. 1, e2018065, 2019.</p>"
            "</div>"
        )
    )


CONTENT_BUILDERS = [
    content_sobre,
    content_introducao,
    content_excel,
    content_interpretando_excel,
    content_joinpoint,
    content_conclusao,
    content_referencia,
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

    media = ROOT / "media" / "modulo2" / "aula3"
    for junk in media.glob("_preview-page-*.png"):
        junk.unlink()
    for junk in media.glob("embedded-p*"):
        junk.unlink()


if __name__ == "__main__":
    main()
