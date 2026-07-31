#!/usr/bin/env python3
"""Gera HTML da Aula 4.2 (Módulo 4) e atualiza index/sidebars da aula 1."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "modulo4" / "aula2"
ASSETS = "../../"

MODULE_NUM = 4
MODULE_TITLE = "Interoperabilidade de Sistemas"
AULA_LABEL = "Aula 2"
AULA_TITLE = "Integração de Dados em Saúde"
AULA1_TITLE = "Interoperabilidade na Saúde"
AUTHOR = "José Nildo de Barros Silva Júnior"
AUTHOR_BIO = (
    "Pesquisador em Saúde Pública no Instituto de Comunicação e Informação "
    "Científica e Tecnológica em Saúde (ICICT), Fundação Oswaldo Cruz (Fiocruz) "
    "– Rio de Janeiro (RJ)."
)

TOPICS = [
    ("Sobre esta aula", "Sobre esta aula"),
    ("Rede Nacional de Dados em Saúde (RNDS)", "Rede Nacional de Dados em Saúde (RNDS)"),
    ("Histórico da RNDS e sua criação como parte da transformação digital do SUS", "Histórico da RNDS e sua criação como parte da transformação digital do SUS"),
    ("Interoperabilidade e sua importância na saúde", "Interoperabilidade e sua importância na saúde"),
    ("Funcionamento da RNDS: como os dados são coletados, integrados e acessados", "Funcionamento da RNDS: como os dados são coletados, integrados e acessados"),
    ("Aplicações práticas para profissionais, gestores e cidadãos", "Aplicações práticas para profissionais, gestores e cidadãos"),
    (
        "Federalização da RNDS: descentralização e governança compartilhada",
        "Federalização da RNDS: descentralização e governança compartilhada",
    ),
    ("Qualidade dos dados", "Qualidade dos dados"),
    ("Referências", "Referências"),
]

OBJECTIVES = [
    "Compreender o conceito, o histórico e a importância estratégica da Rede Nacional de Dados em Saúde (RNDS) para a transformação digital do SUS.",
    "Analisar o funcionamento técnico da RNDS, descrevendo como os dados são coletados, integrados e acessados por diferentes atores.",
    "Identificar as aplicações práticas da RNDS para cidadãos, profissionais de saúde e gestores públicos, reconhecendo seus impactos concretos.",
    "Explicar o processo de federalização da RNDS, seus objetivos e o modelo de governança compartilhada que a sustenta.",
    "Reconhecer os principais desafios (infraestrutura, capacitação, segurança) e as perspectivas futuras para a consolidação da RNDS.",
    "Discutir a importância da qualidade dos dados e o papel central dos integradores e conectores nesse processo.",
]

REFERENCES = [
    'BRASIL. Presidência da República. Casa Civil. Secretaria Especial para Assuntos Jurídicos. <strong>Decreto nº 12.560, de 23 de julho de 2025</strong>. Institui disposições relativas à Rede Nacional de Dados em Saúde. Diário Oficial da União, Brasília, DF, 2025a. Disponível em: <a href="https://www.in.gov.br/en/web/dou/-/decreto-n-12.560-de-23-de-julho-de-2025-643871577" target="_blank" rel="noopener noreferrer">https://www.in.gov.br/en/web/dou/-/decreto-n-12.560-de-23-de-julho-de-2025-643871577</a>. Acesso em: 12 dez. 2025.',
    'BRASIL. Presidência da República. Secretaria-Geral. Subchefia para Assuntos Jurídicos. <strong>Lei nº 13.709, de 14 de agosto de 2018</strong>. Dispõe sobre a Lei Geral de Proteção de Dados Pessoais (LGPD). Brasília, DF: Pres. da Rep., 14 ago. 2018. Disponível em: <a href="https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm" target="_blank" rel="noopener noreferrer">https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm</a>. Acesso em: 12 dez. 2025.',
    'BRASIL. Ministério da Saúde. <strong>Guia: Rede Nacional de Dados em Saúde (RNDS)</strong>. Brasília, DF, [s. d.]b. Disponível em: <a href="https://rnds-guia.saude.gov.br/" target="_blank" rel="noopener noreferrer">https://rnds-guia.saude.gov.br/</a>. Acesso em: 12 dez. 2025.',
    'BRASIL. Ministério da Saúde. Ministério da Saúde institui Rede Nacional de Dados em Saúde como plataforma oficial de integração de dados do SUS. Brasília, DF, [s. d.]a. Disponível em: <a href="https://www.gov.br/saude/pt-br/assuntos/noticias/2025/julho/ministerio-da-saude-institui-rede-nacional-de-dados-em-saude-como-plataforma-oficial-de-integracao-de-dados-do-sus" target="_blank" rel="noopener noreferrer">https://www.gov.br/saude/pt-br/assuntos/noticias/2025/julho/ministerio-da-saude-institui-rede-nacional-de-dados-em-saude-como-plataforma-oficial-de-integracao-de-dados-do-sus</a>. Acesso em: 12 dez. 2025.',
    'BRASIL. Ministério da Saúde. <strong>Portaria GM/MS nº 6.656, de 7 de março de 2025</strong>. Dispõe sobre diretrizes relacionadas à Rede Nacional de Dados em Saúde. Diário Oficial da União, Brasília, DF, 2025b. Disponível em: <a href="https://www.in.gov.br/en/web/dou/-/portaria-gm/ms-n-6.656-de-7-de-marco-de-2025-616482574" target="_blank" rel="noopener noreferrer">https://www.in.gov.br/en/web/dou/-/portaria-gm/ms-n-6.656-de-7-de-marco-de-2025-616482574</a>. Acesso em: 12 dez. 2025.',
    'BRASIL. Ministério da Saúde. <strong>Portaria nº 1.434, de 28 de maio de 2020</strong>. Institui o Programa Conecte SUS e dispõe sobre a Rede Nacional de Dados em Saúde. Diário Oficial da União, Brasília, DF, 2020. Disponível em: <a href="https://bvsms.saude.gov.br/bvs/saudelegis/gm/2020/prt1434_01_06_2020_rep.html" target="_blank" rel="noopener noreferrer">https://bvsms.saude.gov.br/bvs/saudelegis/gm/2020/prt1434_01_06_2020_rep.html</a>. Acesso em: 12 dez. 2025.',
]

PRINCIPLES_MATCHING = [
    ("Interoperabilidade", "Um médico na Paraíba acessa exames feitos no Rio de Janeiro."),
    ("Eficiência na Gestão", "Gestores identificam regiões que precisam de mais USF."),
    ("Centralidade no Cidadão", "Você baixa suas informações de saúde pelo Meu SUS Digital."),
    ("Transparência", "Relatórios públicos mostram como os dados são utilizados."),
    ("Segurança da Informação", "Alertas automáticos detectam tentativas de acesso não autorizado."),
]


def row(inner: str, mb: str = "mb-5") -> str:
    return (
        f'<div class="row justify-content-center"><div class="col-12 col-md-10 col-lg-8 {mb}">'
        f"{inner}</div></div>\n"
    )


def p(text: str) -> str:
    return f"<p>{text}</p>"


def heading(topic_num: int, title: str) -> str:
    return row(
        f'<div class="heading__block"><span class="small">Tópico {topic_num}</span>'
        f'<h3 class="heading__title">{title}</h3></div>',
        "mb-5",
    )


def subheading(title: str, tag: str = "h4") -> str:
    return row(f'<div class="heading__block"><{tag} class="heading__title">{title}</{tag}></div>', "mb-4")


def box(kind: str, label: str, body: str) -> str:
    return row(
        f'<div class="box" data-box="{kind}"><div class="card"><div class="card-header">'
        f'<span class="icone material-symbols-rounded" aria-hidden="true"></span>'
        f'<span class="label">{label}</span></div><div class="card-body">'
        f'<p class="mb-0">{body}</p></div></div></div>'
    )


def box_html(kind: str, label: str, body_html: str) -> str:
    return row(
        f'<div class="box" data-box="{kind}"><div class="card"><div class="card-header">'
        f'<span class="icone material-symbols-rounded" aria-hidden="true"></span>'
        f'<span class="label">{label}</span></div><div class="card-body">'
        f"{body_html}</div></div></div>"
    )


def figure_block(caption: str, src: str, alt: str, fonte: str = "") -> str:
    fonte_html = f'<p class="figure-caption fonte small mb-0">{fonte}</p>' if fonte else ""
    return row(
        f'<p class="mb-2"><strong>{caption}</strong></p>'
        f'<figure class="lightbox aos-init aos-animate" data-aos="fade-up" data-aos-easing="ease-out" data-aos-duration="600">'
        f'<img class="img-fluid mx-auto d-block mb-3 rounded border" src="{src}" alt="{alt}" loading="lazy" />'
        f"</figure>{fonte_html}"
    )


def quotation_block(quote: str, author: str = "", intro: str = "") -> str:
    intro_html = f"{intro} " if intro else ""
    author_html = f'<span class="quotation-autor">{author}</span>' if author else ""
    return row(
        '<div class="quotation"><blockquote>'
        '<div class="quotation-body"><span class="quotation-mark fa1"></span>'
        f"<p>{intro_html}<em>{quote}</em></p>"
        f"{author_html}"
        '</div><span class="quotation-mark fa2"></span>'
        "</blockquote></div>"
    )


def flipcard(card_id: str, title: str, back_html: str, *, col: str = "col-12 col-md-6") -> str:
    return (
        f'<div class="{col}"><div class="flipcard"><div class="flip-card">'
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


def flip_row(*cards: str) -> str:
    return (
        '<div class="row justify-content-center"><div class="col-12 col-md-10 col-lg-8">'
        '<div class="row g-4 mb-5">'
        + "".join(cards)
        + "</div></div></div>"
    )


def exercise_block(num: int, question: str, options: list[tuple[str, str, bool]]) -> str:
    opts = []
    for text, feedback, correct in options:
        attrs = ' tabindex="0"'
        if correct:
            attrs += " correct"
        opts.append(
            f'<li class="answer__option" data-feedback="{feedback}"{attrs}><p>{text}</p></li>'
        )
    answers = "\n".join(opts)
    return row(
        f'<div class="exercise" data-exercise="one"><div class="card">'
        f'<div class="card-header">Questão {num}</div><div class="card-body">'
        f'<div class="exercise__question"><p>{question}</p></div>'
        f'<div class="exercise__answers"><ul>{answers}</ul></div></div>'
        f'<div class="card-footer"><div class="exercise__submit">'
        f'<span class="exercise__submit--feedback d-none"></span>'
        f'<button class="fio-button fio-button-primary" type="submit" disabled>Conferir</button>'
        f"</div></div></div></div>",
        "mb-5",
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


def video_embed(youtube_url: str, title: str = "Vídeo") -> str:
    vid = youtube_url.split("v=")[-1].split("&")[0]
    return (
        f'<div class="ratio ratio-16x9"><iframe src="https://www.youtube.com/embed/{vid}" '
        f'title="{title}" allow="accelerometer; autoplay; clipboard-write; encrypted-media; '
        f'gyroscope; picture-in-picture; web-share" allowfullscreen loading="lazy"></iframe></div>'
    )


def video_box(youtube_url: str, intro: str, title: str = "Vídeo") -> str:
    body = f'<p class="mb-3">{intro}</p>{video_embed(youtube_url, title)}'
    return box_html("Para Assistir", "Para Assistir!", body)


def topic_list_html(current: int) -> str:
    items = []
    for i, (label, _) in enumerate(TOPICS, 1):
        status = ' status="visited"' if i < current else ""
        aria = 'aria-label="Tópico concluído"' if i < current else 'aria-label="Tópico não concluído"'
        items.append(
            f'\t\t\t\t\t\t\t<a href="topico{i}.html" tabindex="0" role="link" class="topic-list__item" {aria}{status}>'
            f'<span class="material-symbols-rounded"></span>{label}</a>'
        )
    return "\n".join(items)


def page_nav(num: int) -> str:
    parts = []
    if num == 1:
        parts.append(
            '<a class="fio-button fio-button-primary" href="../aula1/topico9.html" rel="prev">'
            '<span class="material-symbols-rounded" aria-hidden="true">west</span> Aula anterior</a>'
        )
    elif num > 1:
        parts.append(
            f'<a class="fio-button fio-button-primary" href="topico{num - 1}.html" rel="prev">'
            f'<span class="material-symbols-rounded" aria-hidden="true">west</span> Tópico anterior</a>'
        )
    if num < len(TOPICS):
        parts.append(
            f'<a class="fio-button fio-button-primary" href="topico{num + 1}.html" rel="next">Próximo tópico '
            f'<span class="material-symbols-rounded" aria-hidden="true">east</span></a>'
        )
    else:
        parts.append(
            '<a class="fio-button fio-button-primary" href="../atividade.html" rel="next">'
            'Atividade formativa <span class="material-symbols-rounded" aria-hidden="true">east</span></a>'
        )
    inner = "".join(parts)
    return (
        f'\t\t\t<section><div class="container"><div class="row justify-content-center">'
        f'<div class="col-12 col-md-10 col-lg-8"><div class="page-nav d-flex justify-content-evenly flex-wrap gap-3">'
        f"{inner}</div></div></div></div></section>\n"
    )


def extra_scripts(num: int) -> str:
    if num == 2:
        return '\t<script type="text/javascript" src="../../assets/js/exercise.js"></script>\n'
    return ""


def build_sidebar(current: int) -> str:
    topics = topic_list_html(current)
    return f"""				<div class="sidebar__group d-lg-none">
					<div class="sidebar__group-item">
						<div class="sidebar__header">
							<span>Curso</span>
							<a class="mobile-toggle-close" tabindex="0" role="button"><span class="icon material-symbols-rounded">read_more</span></a>
						</div>
					</div>
					<div class="sidebar__group-item"><div class="sidebar__title"><h1>Fontes de Dados e Sistemas de Informação para o SUS</h1></div></div>
					<div class="sidebar__group-item">
						<ul class="nav">
							<li class="nav-item"><a href="../../index.html" class="nav-link" tabindex="0"><span class="icon material-symbols-rounded" aria-hidden="true">home</span>Início</a></li>
							<li class="nav-item"><a href="#" class="nav-link" tabindex="0" data-bs-toggle="modal" data-bs-target="#modal-creditos"><span class="icon material-symbols-rounded" aria-hidden="true">format_list_bulleted</span>Créditos</a></li>
						</ul>
					</div>
				</div>
				<div class="sidebar__group">
					<div class="sidebar__group-item">
						<div class="dropend">
							<button id="dropdown-modulos" type="button" class="dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false" data-bs-auto-close="outside" data-bs-offset="0,30">
								<span class="icon material-symbols-rounded" aria-hidden="true">grid_view</span><span class="label">Módulos</span>
							</button>
							<ul class="dropdown-menu" aria-labelledby="dropdown-modulos">
								<li class="d-lg-none dropdown-menu__header">
									<a class="dropdown-menu__back-button" tabindex="0" role="button"><span class="icon material-symbols-rounded">chevron_left</span> Voltar</a>
									<a class="mobile-toggle-close" tabindex="0" role="button"><span class="icon material-symbols-rounded">read_more</span></a>
								</li>
								<li class="dropdown-menu__item"><a class="dropdown-menu__item-link" tabindex="0" role="link" href="../../modulo1/aula1/topico1.html"><strong>Módulo 1</strong><br />Introdução à Informação em Saúde no SUS</a></li>
								<li class="dropdown-menu__item"><a class="dropdown-menu__item-link" tabindex="0" role="link" href="../../modulo2/aula1/topico1.html"><strong>Módulo 2</strong><br />Fontes de Dados Socioeconômicos e Demográficos: subsídios para a Saúde</a></li>
								<li class="dropdown-menu__item"><a class="dropdown-menu__item-link" tabindex="0" role="link" href="../../modulo3/aula1/topico1.html"><strong>Módulo 3</strong><br />Sistemas de Informação em Saúde</a></li>
								<li class="dropdown-menu__item"><a class="dropdown-menu__item-link" tabindex="0" role="link" href="../../modulo4/aula1/topico1.html"><strong>Módulo 4</strong><br />{MODULE_TITLE}</a></li>
							</ul>
						</div>
					</div>
				</div>
				<div class="divider"><hr /></div>
				<div class="sidebar__group">
					<div class="sidebar__group-item"><span class="text module">Módulo <br class="d-none d-lg-block" /><span>{MODULE_NUM}</span></span></div>
					<div class="sidebar__group-item">
						<div class="dropend">
							<button type="button" class="dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false" data-bs-auto-close="outside" data-bs-offset="0,30">
								<span class="icon material-symbols-rounded" aria-hidden="true">apps</span><span class="label">Conteúdo</span>
							</button>
							<ul class="dropdown-menu">
								<li class="d-lg-none dropdown-menu__header">
									<a class="dropdown-menu__back-button" tabindex="0" role="button"><span class="icon material-symbols-rounded">chevron_left</span> Voltar</a>
									<a class="mobile-toggle-close" tabindex="0" role="button"><span class="icon material-symbols-rounded">read_more</span></a>
								</li>
								<li class="dropdown-menu__title"><span class="label">Módulo {MODULE_NUM}</span><span class="title">{MODULE_TITLE}</span></li>
								<li class="dropdown-menu__item"><a class="dropdown-menu__item-link" tabindex="0" role="link" href="../aula1/topico1.html"><strong>Aula 1: </strong>{AULA1_TITLE}</a></li>
								<li class="dropdown-menu__item"><a class="dropdown-menu__item-link" tabindex="0" role="link" href="topico1.html"><strong>Aula 2: </strong>{AULA_TITLE}</a></li>
								<li class="dropdown-menu__item"><a class="dropdown-menu__item-link" tabindex="0" role="link" href="../atividade.html"><strong>Atividade</strong></a></li>
							</ul>
						</div>
					</div>
				</div>
				<div class="divider"><hr /></div>
				<div class="sidebar__group">
					<div class="sidebar__group-item"><span class="text class">{AULA_LABEL}</span></div>
					<div class="sidebar__group-item">
						<div class="dropend">
							<button type="button" class="dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false" data-bs-auto-close="outside" data-bs-offset="0,30">
								<span class="icon material-symbols-rounded" aria-hidden="true">format_list_bulleted</span><span class="label">Tópicos</span>
							</button>
							<ul class="dropdown-menu">
								<li class="d-lg-none dropdown-menu__header">
									<a class="dropdown-menu__back-button" tabindex="0" role="button"><span class="icon material-symbols-rounded">chevron_left</span> Voltar</a>
									<a class="mobile-toggle-close" tabindex="0" role="button"><span class="icon material-symbols-rounded">read_more</span></a>
								</li>
								<li class="dropdown-menu__title"><span class="label">{AULA_LABEL}</span><span class="title">{AULA_TITLE}</span></li>
								<li class="dropdown-menu__item"><nav class="topic-list">
{topics}
							</nav></li>
							</ul>
						</div>
					</div>
				</div>"""


def build_page(num: int, content: str) -> str:
    ex_scripts = extra_scripts(num)
    return f"""<!DOCTYPE html>
<html lang="pt-br">
<head>
	<meta charset="utf-8" />
	<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no, user-scalable=yes" />
	<meta http-equiv="content-type" content="text/html; charset=utf-8" />
	<meta name="robots" content="noindex" />
	<meta name="author" content="Fiocruz, Campus Virtual" />
	<meta name="description" content="Curso Fontes de Dados e Sistemas de Informação para o SUS" />
	<link rel="apple-touch-icon" sizes="180x180" href="{ASSETS}media/icons/apple-icon-180x180.png" />
	<link rel="icon" type="image/png" sizes="32x32" href="{ASSETS}media/icons/favicon-32x32.png" />
	<link rel="manifest" href="../media/icons/manifest.json" />
	<meta name="theme-color" content="#001833" />
	<title>Curso Fontes de Dados e Sistemas de Informação para o SUS | Mod {MODULE_NUM} | {AULA_LABEL}</title>
	<link rel="stylesheet" href="{ASSETS}source/bootstrap-5.1.3/css/bootstrap.min.css" />
	<link rel="stylesheet" href="{ASSETS}assets/css/style.css" />
</head>
<body>
	<header class="header">
		<div class="mobile-toggle-open"><a class="mobile-toggle__button" tabindex="0" role="button"><span class="icon material-symbols-rounded">read_more</span></a></div>
		<div class="brand"><img class="img-fluid logo-black" src="{ASSETS}media/logos/header-fiocruz-campus-virtual.png" alt="Campus Virtual Fiocruz" /></div>
		<div class="title"><h1>Fontes de Dados e Sistemas de Informação para o SUS</h1></div>
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
			<div id="page-title"><div class="container"><div class="row align-items-center hstify-content-center justify-content-xxl-start ms-lg-5"><div class="col-12 col-md-10 col-lg-11"><h2 class="title"><span class="label">Módulo {MODULE_NUM} | {AULA_LABEL}</span><br />{AULA_TITLE}</h2></div></div></div></div>
			<div id="page-content" class="">
				<section><div class="container">
{content}				</div></section>
			</div>
{page_nav(num)}			<footer>
				<div class="container-fluid">
					<div class="row justify-content-center align-items-center linha-de-marcas">
						<div class="col-12 text-center py-3">
							<img class="img-fluid regua-logos" src="{ASSETS}media/logos/regua-de-logos.png" alt="Régua de logos: ICICT, Campus Virtual Fiocruz e Fiocruz" />
						</div>
					</div>
				</div>
			</footer>
	</div>
	<script src="{ASSETS}source/bootstrap-5.1.3/js/bootstrap.bundle.min.js"></script>
	<script type="text/javascript" src="{ASSETS}assets/js/ResizeSensor.js"></script>
	<script type="text/javascript" src="{ASSETS}assets/js/sticky-sidebar.js"></script>
	<script type="text/javascript" src="{ASSETS}assets/js/sidebar.js"></script>
{ex_scripts}	<script type="text/javascript">var sidebar = new StickySidebar(".sidebar", {{ topSpacing: 0, bottomSpacing: 0, containerSelector: ".main", innerWrapperSelector: ".sidebar__inner", minWidth: 991 }});</script>
	<script type="text/javascript" src="{ASSETS}assets/js/scripts.js"></script>
	<script type="text/javascript" src="{ASSETS}assets/js/custom-anime.js"></script>
	<script type="text/javascript" src="{ASSETS}source/animate/aos/dist/aos.js"></script>
	<script>AOS.init();</script>
</body>
</html>
"""


def content_topico1() -> str:
    objs = "".join(
        f'<li class="list-group-item aos-init aos-animate" list-style="default" data-aos="fade-right" '
        f'data-aos-easing="ease-out" data-aos-duration="1200">{o}</li>'
        for o in OBJECTIVES
    )
    return (
        heading(1, TOPICS[0][1])
        + row(p('Seja bem-vindo e bem-vinda à aula <strong>“Integração de Dados em Saúde”</strong>.'))
        + row(p("A seguir veja algumas informações importantes!"))
        + row(
            p(
                "Suponha que você está atendendo um paciente que acabou de se mudar de outro estado. Ele não traz "
                "exames nem relatórios, mas precisa de acompanhamento contínuo. Como acessar seu histórico de forma "
                "rápida e segura? É aí que a <strong>Rede Nacional de Dados em Saúde (RNDS)</strong> entra em cena! "
                "Vamos explorar juntos o que é, como funciona e por que essa plataforma é um dos pilares da "
                "transformação digital do SUS."
            )
        )
        + subheading("Objetivos de aprendizagem")
        + row('<p>Ao final desta aula você será capaz de:</p><div class="list"><ul class="list-group">' + objs + "</ul></div>")
        + subheading("Autoria")
        + row(f"<p><strong>{AUTHOR}</strong></p><p>{AUTHOR_BIO}</p>")
    )


def content_topico2() -> str:
    principles_fc = flip_row(
        flipcard("m4a2p1", "Interoperabilidade e padronização", "<p class=\"mb-0\">Padrões técnicos comuns permitem que diferentes sistemas \"conversem\" entre si de forma estruturada e segura.</p>"),
        flipcard("m4a2p2", "Segurança, privacidade e confidencialidade", "<p class=\"mb-0\">Proteção robusta contra acessos não autorizados, vazamentos ou alterações indevidas de dados, em estrito cumprimento da Lei Geral de Proteção de Dados Pessoais (LGPD).</p>"),
        flipcard("m4a2p3", "Centralidade no cidadão", "<p class=\"mb-0\">O titular dos dados tem acesso e controle sobre suas informações de saúde, garantindo transparência e autonomia.</p>"),
        flipcard("m4a2p4", "Transparência, ética e responsabilidade", "<p class=\"mb-0\">Clareza sobre como os dados são tratados, com uso ético, legal e responsável, sempre com propósito definido e sem discriminação.</p>"),
        flipcard("m4a2p5", "Eficiência e melhoria contínua", "<p class=\"mb-0\">Uso estratégico das informações para qualificar a assistência, apoiar a pesquisa e orientar políticas públicas de saúde mais eficazes.</p>"),
    )
    interactive_activity = (
        subheading("Atividade interativa", "h5")
        + row("<p><strong>Instrução:</strong> selecione a opção correta para cada princípio da RNDS.</p>")
        + exercise_block(
            1,
            "Interoperabilidade corresponde a qual exemplo de aplicação?",
            [
                (
                    "Um médico na Paraíba acessa exames feitos no Rio de Janeiro.",
                    "Correta. Esse cenário representa interoperabilidade entre serviços e sistemas.",
                    True,
                ),
                (
                    "Relatórios públicos mostram como os dados são utilizados.",
                    "Incorreta. Esse exemplo está relacionado à transparência.",
                    False,
                ),
                (
                    "Alertas automáticos detectam tentativas de acesso não autorizado.",
                    "Incorreta. Esse exemplo está ligado à segurança da informação.",
                    False,
                ),
            ],
        )
        + exercise_block(
            2,
            "Eficiência na Gestão corresponde a qual exemplo de aplicação?",
            [
                (
                    "Gestores identificam regiões que precisam de mais USF.",
                    "Correta. Esse uso orienta gestão e alocação eficiente de recursos.",
                    True,
                ),
                (
                    "Você baixa suas informações de saúde pelo Meu SUS Digital.",
                    "Incorreta. Esse exemplo representa centralidade no cidadão.",
                    False,
                ),
                (
                    "Relatórios públicos mostram como os dados são utilizados.",
                    "Incorreta. Esse exemplo está relacionado à transparência.",
                    False,
                ),
            ],
        )
        + exercise_block(
            3,
            "Centralidade no Cidadão corresponde a qual exemplo de aplicação?",
            [
                (
                    "Você baixa suas informações de saúde pelo Meu SUS Digital.",
                    "Correta. Esse é um caso direto de protagonismo do cidadão.",
                    True,
                ),
                (
                    "Gestores identificam regiões que precisam de mais USF.",
                    "Incorreta. Esse exemplo está relacionado à eficiência na gestão.",
                    False,
                ),
                (
                    "Um médico na Paraíba acessa exames feitos no Rio de Janeiro.",
                    "Incorreta. Esse exemplo está relacionado à interoperabilidade.",
                    False,
                ),
            ],
        )
        + exercise_block(
            4,
            "Transparência corresponde a qual exemplo de aplicação?",
            [
                (
                    "Relatórios públicos mostram como os dados são utilizados.",
                    "Correta. Transparência envolve clareza sobre uso e finalidade dos dados.",
                    True,
                ),
                (
                    "Você baixa suas informações de saúde pelo Meu SUS Digital.",
                    "Incorreta. Esse exemplo está relacionado à centralidade no cidadão.",
                    False,
                ),
                (
                    "Alertas automáticos detectam tentativas de acesso não autorizado.",
                    "Incorreta. Esse exemplo está ligado à segurança da informação.",
                    False,
                ),
            ],
        )
        + exercise_block(
            5,
            "Segurança da Informação corresponde a qual exemplo de aplicação?",
            [
                (
                    "Alertas automáticos detectam tentativas de acesso não autorizado.",
                    "Correta. Esse é um mecanismo típico de proteção e monitoramento de segurança.",
                    True,
                ),
                (
                    "Relatórios públicos mostram como os dados são utilizados.",
                    "Incorreta. Esse exemplo está relacionado à transparência.",
                    False,
                ),
                (
                    "Gestores identificam regiões que precisam de mais USF.",
                    "Incorreta. Esse exemplo está relacionado à eficiência na gestão.",
                    False,
                ),
            ],
        )
    )
    legis_body = (
        "<p class=\"mb-0\">O <strong>Decreto nº 12.560/2025</strong> transformou a RNDS em uma política de Estado, "
        "consolidando seu papel como infraestrutura estratégica para a saúde digital brasileira. Isso significa que "
        "a RNDS deixou de ser um projeto temporário para se tornar uma plataforma permanente e essencial para o SUS.</p>"
    )
    return (
        heading(2, TOPICS[1][1])
        + row(
            p(
                "A RNDS é muito mais do que um sistema de informática, é a <strong>plataforma oficial de "
                "interoperabilidade do Ministério da Saúde</strong>, criada para conectar diferentes sistemas de "
                "saúde em todo o Brasil. Simplificando, pense nela como uma <strong>\"ponte digital segura\"</strong> "
                "que permite a hospitais, Unidades de Saúde da Família, laboratórios e outros serviços trocarem "
                "informações de saúde de forma padronizada, ágil e protegida."
            )
        )
        + row(
            p(
                "Antes cada serviço de saúde operava como uma \"ilha\" de informações. Com a implementação da RNDS, "
                "é possível criar um \"arquipélago conectado\", por meio do qual os dados podem fluir de maneira "
                "organizada e segura. Isso significa que um exame realizado em um laboratório de Manaus pode ser "
                "acessado por um médico em Porto Alegre durante uma consulta, desde que o paciente autorize e todos "
                "os protocolos de segurança sejam seguidos."
            )
        )
        + box_html("Legislação", "Legislação!", legis_body)
        + row(
            p(
                "A RNDS opera sob princípios descritos no Decreto nº 12.560/2025, que garantem sua funcionalidade, "
                "segurança e respeito ao cidadão."
            )
        )
        + row(p("Assim, esses princípios incluem:"))
        + principles_fc
        + interactive_activity
    )


def content_topico3() -> str:
    stats_figure = (
        '<figure class="lightbox aos-init aos-animate" data-aos="fade-up" data-aos-easing="ease-out" '
        f'data-aos-duration="600"><img class="img-fluid mx-auto d-block mb-3 rounded border" '
        f'src="{ASSETS}media/modulo4/aula2-cobertura-volume-dados.png" '
        'alt="Infográfico sobre cobertura nacional e volume de dados da RNDS." loading="lazy" /></figure>'
    )
    return (
        heading(3, TOPICS[2][1])
        + row(
            p(
                "A RNDS foi formalmente instituída pela <strong>Portaria GM/MS nº 1.434, de 28 de maio de 2020</strong>, "
                "como parte essencial do antigo Programa Conecte SUS, hoje chamado Programa SUS Digital. Embora sua "
                "criação tenha ocorrido em um contexto de crise, durante a pandemia de covid-19, a RNDS representa o "
                "marco central para a transformação digital do Sistema Único de Saúde (SUS) e a continuidade do cuidado "
                "(Brasil, 2020)."
            )
        )
        + row(
            p(
                "A partir dessa base operacional bem-sucedida, a RNDS expandiu seu escopo. Deixou de ser uma solução "
                "emergencial para a covid-19 e se tornou a <strong>plataforma oficial de interoperabilidade do SUS</strong>, "
                "integrando progressivamente diversos tipos de dados e sistemas de saúde estaduais e municipais. Vale "
                "ressaltar que o contexto da covid-19 acelerou a criação e a implementação da RNDS, mas ela não foi "
                "criada exclusivamente por causa da pandemia."
            )
        )
        + row(
            p(
                "O grande marco de consolidação ocorreu em <strong>julho de 2025</strong>, com a assinatura de um "
                "<strong>Decreto Presidencial</strong> nº 12.560, que oficializou a RNDS como a plataforma nacional "
                "definitiva. Esse ato legal reafirmou o papel central da RNDS na integração de dados do SUS e "
                "fortaleceu sua governança, que passou a ser coordenada por instâncias formalmente instituídas e "
                "coordenadas pela área gestora do Ministério da Saúde com competência em informação e saúde digital "
                "(Brasil, 2025a)."
            )
        )
        + row(p("Conforme dados oficiais de julho de 2025 (Brasil, [s. d.]a), a RNDS é uma realidade consolidada e em plena operação:"))
        + row(stats_figure)
    )


def content_topico4() -> str:
    importante_body = (
        "<p class=\"mb-0\">Se a interoperabilidade é a capacidade de conversar, precisamos de um idioma comum que todos os "
        "sistemas entendam. É aí que entra o <strong>HL7 FHIR</strong> (Fast Healthcare Interoperability Resources).</p>"
    )
    return (
        heading(4, TOPICS[3][1])
        + row(
            p(
                "Como vimos anteriormente, a interoperabilidade funciona como uma <strong>conversa eficiente entre "
                "sistemas diferentes</strong>, permitindo que eles troquem dados e utilizem informações de forma "
                "segura e integrada. No setor Saúde, isso se traduz na possibilidade de hospitais, Unidades de Saúde "
                "da Família, laboratórios e outros serviços compartilharem prontuários, exames, prescrições e registros "
                "clínicos <strong>sem barreiras tecnológicas</strong>."
            )
        )
        + row(
            p(
                "A RNDS foi desenvolvida com foco em <strong>interoperabilidade, segurança e escalabilidade</strong>, "
                "utilizando tecnologias que garantem um repositório acessível e confiável. Tudo isso preservando a "
                "privacidade, a integridade e a rastreabilidade dos dados. A informação de saúde precisa ser tanto "
                "útil quanto protegida."
            )
        )
        + box_html("Importante", "Importante!", importante_body)
        + row(
            "<p><strong>Como o FHIR funciona na prática?</strong></p>"
            "<p class=\"mb-0\">Pense em um formulário padronizado que todo serviço de saúde usa para registrar uma consulta. "
            "Independentemente do sistema específico que cada serviço utiliza internamente, quando precisam compartilhar "
            "essa informação, todos \"traduzem\" para o <strong>formato FHIR</strong>. Essa padronização permite que "
            "sistemas distintos \"conversem\" entre si de forma ágil e segura.</p>"
        )
        + figure_block(
            "Figura 1 – Interoperabilidade via formato FHIR.",
            f"{ASSETS}media/modulo4/aula2-formato-fhir.png",
            "Diagrama de interoperabilidade via formato FHIR entre serviços de saúde.",
        )
    )


def content_topico5() -> str:
    purposes_figure = (
        '<figure class="lightbox aos-init aos-animate" data-aos="fade-up" data-aos-easing="ease-out" '
        f'data-aos-duration="600"><img class="img-fluid mx-auto d-block mb-3 rounded border" '
        f'src="{ASSETS}media/modulo4/aula2-funcionamento-rnds.png" '
        'alt="Diagrama das finalidades do funcionamento da RNDS no SUS." loading="lazy" /></figure>'
    )
    legis_art12 = (
        "<p><strong>Decreto nº 12.560, de 23 de julho de 2025:</strong></p>"
        "<p class=\"mb-0\">Art. 12. [...] os dados coletados conforme os modelos serão enviados pelos estados, pelo "
        "Distrito Federal e pelos municípios, de forma a permitir a gestão compartilhada pela União e pelos demais "
        "entes federativos das informações [...].</p>"
    )
    sharing_list = (
        "<ul class=\"mb-0 list-unstyled\">"
        "<li class=\"mb-2\">I - Órgãos e entidades da administração pública direta, autárquica e fundacional.</li>"
        "<li class=\"mb-2\">II - Órgãos e entidades da Administração Pública direta e indireta de gestão em saúde, por meio da federalização da RNDS.</li>"
        "<li>III - Órgãos de pesquisa.</li>"
        "</ul>"
    )
    return (
        heading(5, TOPICS[4][1])
        + row(
            p(
                "A RNDS é fundamental para garantir a soberania dos dados do SUS. Sua estrutura foi planejada para "
                "assegurar a autonomia tecnológica nacional, bem como a disponibilidade, integridade, confidencialidade, "
                "autenticidade e segurança das informações. Desse modo, a RNDS garante a devida proteção dos dados e a "
                "privacidade de seus titulares."
            )
        )
        + row(
            p(
                "O tratamento dos dados na RNDS é orientado por finalidades específicas que convergem para o objetivo "
                "maior de cuidado ao cidadão. Essas finalidades funcionam como pilares que sustentam a operação da Rede:"
            )
        )
        + row(purposes_figure, "mb-5")
        + row(
            p(
                "Para atender a essas múltiplas finalidades, a RNDS opera a partir de um ciclo contínuo de dados. Esse "
                "ciclo começa com a <strong>Coleta</strong> dos dados nas unidades de saúde (laboratórios, hospitais etc.), "
                "passa pela <strong>Integração</strong> na plataforma da RNDS (sendo padronizados e armazenados de forma "
                "segura) e termina com o <strong>Acesso</strong> qualificado por parte dos profissionais e gestores. A "
                "qualidade e o sucesso desse ciclo são o que permite que a RNDS apoie a assistência, monitore a vigilância "
                "e fundamente a gestão e as políticas públicas já mencionadas, transformando dados brutos em decisões "
                "que impactam a vida do usuário."
            )
        )
        + subheading("Ciclo do dado na RNDS", "h6")
        + row(
            "<ol class=\"mb-0\">"
            "<li class=\"mb-3\"><strong>Coleta descentralizada:</strong> Os dados são gerados e coletados na ponta, pelos "
            "<strong>estados, municípios e prestadores de serviço</strong> (hospitais, Unidades de Saúde da Família, "
            "laboratórios etc.), em seus próprios sistemas de informação. Conforme estabelecido, o envio de dados para a "
            "RNDS será feito por <strong>estabelecimentos públicos e privados</strong>, seguindo modelos informacionais e "
            "computacionais padronizados. A RNDS não substitui esses sistemas locais, mas estabelece um canal padronizado "
            "para o envio de conjuntos de dados específicos, garantindo integração, consistência e reutilização segura das "
            "informações. Em outras palavras, a integração ocorre pelo envio regular e padronizado de dados dos sistemas "
            "locais para a plataforma nacional.</li>"
            "</ol>"
        )
        + box_html("Legislação", "Legislação!", legis_art12)
        + row(
            "<ol class=\"mb-0\" start=\"2\">"
            "<li class=\"mb-3\"><strong>Integração e interoperabilidade:</strong> Para que os dados de milhares de fontes "
            "diferentes possam se comunicar, a RNDS define <strong>padrões técnicos e semânticos obrigatórios (HL7 FHIR)</strong>. "
            "Isso significa que, independentemente do software usado no município, as informações (como um diagnóstico, um "
            "resultado de exame ou uma dose de vacina) devem ser codificadas e transmitidas em um formato comum que a rede "
            "consegue interpretar.</li>"
            "<li class=\"mb-0\"><strong>Acesso segmentado:</strong> Uma vez integrados e disponibilizados na RNDS, os dados "
            "não são abertos indiscriminadamente. O acesso é regulado por <strong>papel, necessidade e finalidade legal</strong>, "
            "ocorrendo por meio de portais específicos, como poderemos observar no tópico seguinte “Aplicações práticas para "
            "profissionais, gestores e cidadãos”.</li>"
            "</ol>"
        )
        + subheading("O compartilhamento dos dados da RNDS poderá ser feito para (Brasil, 2025a):", "h6")
        + row(sharing_list)
        + box(
            "Importante",
            "Importante!",
            "É vedado o tratamento de dados da RNDS para quaisquer outros fins que não os previstos.",
        )
    )


def content_topico6() -> str:
    platforms = flip_row(
        flipcard(
            "m4a2plat1",
            "SUS Digital Profissional",
            '<p class="mb-0">Para profissionais de saúde acessarem dados clínicos no contexto do atendimento. '
            '<a href="https://susdigital-profissional.saude.gov.br/login" target="_blank" rel="noopener noreferrer">Acessar plataforma</a></p>',
        ),
        flipcard(
            "m4a2plat2",
            "SUS Digital Gestor",
            '<p class="mb-0">Para gestores públicos acessarem dados agregados e anonimizados para análise. '
            '<a href="https://susdigitalgestor.saude.gov.br/login" target="_blank" rel="noopener noreferrer">Acessar plataforma</a></p>',
        ),
        flipcard(
            "m4a2plat3",
            "Meu SUS Digital",
            '<p class="mb-0">Para cidadãos acessarem e gerenciarem seus próprios dados de saúde. '
            '<a href="https://meususdigital.saude.gov.br/login" target="_blank" rel="noopener noreferrer">Acessar plataforma</a></p>',
        ),
    )
    prof_acc = accordion(
        "m4a2-prof",
        [
            ("Suporte à decisão clínica com base em dados integrados", "<p class=\"mb-0\">Permite diagnósticos mais precisos e tratamentos mais informados.</p>"),
            ("Evita a repetição desnecessária de exames e procedimentos", "<p class=\"mb-0\">Otimiza recursos e reduz a exposição do paciente.</p>"),
            ("Identifica padrões importantes na saúde do paciente", "<p class=\"mb-0\">Permite acompanhar a saúde do paciente ao longo do tempo e em diferentes serviços.</p>"),
            ("Fortalecimento da Atenção Primária", "<p class=\"mb-0\">O profissional da Unidade de Saúde da Família tem visão do paciente/usuário em níveis de saúde diferentes, coordenando o cuidado de forma mais eficaz.</p>"),
        ],
    )
    gest_acc = accordion(
        "m4a2-gest",
        [
            ("Monitoramento de filas de espera, demanda e oferta de serviços", "<p class=\"mb-0\">Permite identificar gargalos e redistribuir demandas de forma ágil (conforme regulação da Portaria GM/MS nº 6.656/2025 sobre dados de regulação) (Brasil, 2025b).</p>"),
            ("Análise de indicadores de saúde em tempo real", "<p class=\"mb-0\">Para vigilância de surtos, monitoramento de campanhas de vacinação e acompanhamento de doenças crônicas.</p>"),
            ("Planejamento de políticas públicas e alocação de recursos", "<p class=\"mb-0\">Direciona investimentos e programas para onde são mais necessários, com base em dados concretos sobre morbidade, mortalidade e utilização de serviços.</p>"),
            ("Avaliação de desempenho e eficiência", "<p class=\"mb-0\">Permite medir o impacto de programas de saúde e a performance de diferentes redes e serviços.</p>"),
        ],
    )
    cid_acc = accordion(
        "m4a2-cid",
        [
            ("Acesso ao próprio histórico unificado", "<p class=\"mb-0\">Consulta a resultados de exames, carteira de vacinação digital completa, histórico de medicações, relatórios de atendimento e agendamentos.</p>"),
            ("Maior transparência e autonomia", "<p class=\"mb-0\">Permite que o cidadão acompanhe seu percurso de saúde, facilitando a comunicação com profissionais e a adesão a tratamentos.</p>"),
            ("Gestão do cuidado pessoal", "<p class=\"mb-0\">Recebe lembretes e informações relevantes, como a necessidade de retirar medicamentos na farmácia popular ou de seguir com um tratamento.</p>"),
            ("Facilidade e acesso", "<p class=\"mb-0\">Todo esse conjunto de informações está disponível na palma da mão, de forma digital e integrada.</p>"),
        ],
    )
    saiba_guia = (
        "<p class=\"mb-0\">Você sabia que a RNDS disponibiliza um guia voltado para orientar gestores de serviços de "
        "saúde e profissionais de tecnologia da informação sobre como realizar a integração com a rede? Além disso, "
        "o guia oferece contextos explicativos para facilitar a compreensão e disponibiliza um portal com serviços "
        'integrados. Acesse o guia pelo link: <a href="https://rnds-guia.saude.gov.br/" target="_blank" '
        'rel="noopener noreferrer">https://rnds-guia.saude.gov.br/</a></p>'
    )
    saiba_app = (
        "<ul class=\"mb-0\">"
        '<li><a href="https://meususdigital.saude.gov.br/" target="_blank" rel="noopener noreferrer">Conheça o aplicativo Meu SUS Digital</a></li>'
        '<li><a href="https://meususdigital.saude.gov.br/" target="_blank" rel="noopener noreferrer">Como se cadastrar no aplicativo?</a></li>'
        '<li><a href="https://meususdigital.saude.gov.br/login" target="_blank" rel="noopener noreferrer">Página de login do Meu SUS Digital</a></li>'
        '<li><a href="https://play.google.com/store/apps/details?id=br.gov.datasus.meususdigital" target="_blank" rel="noopener noreferrer">Aplicativo Meu SUS Digital no Google Play</a></li>'
        '<li><a href="https://apps.apple.com/br/app/meu-sus-digital/id6444023235" target="_blank" rel="noopener noreferrer">Aplicativo Meu SUS Digital na App Store</a></li>'
        "</ul>"
    )
    return (
        heading(6, TOPICS[5][1])
        + row(
            p(
                "A verdadeira força da RNDS está em sua capacidade de conectar diferentes atores do sistema de saúde em "
                "um ecossistema integrado, transformando dados em ações concretas que beneficiam cada elo da cadeia de "
                "cuidado. Antes de explorarmos exemplos específicos, é fundamental compreender as "
                "<strong>Plataformas SUS Digital</strong>, que são os canais práticos de acesso e disseminação das "
                "informações consolidadas pela RNDS (Brasil, 2025a)."
            )
        )
        + row(
            p(
                "As <strong>Plataformas SUS Digital</strong> são os portais oficiais que simplificam e democratizam o "
                "acesso a informações e serviços de saúde para pessoas usuárias, profissionais e gestores públicos. "
                "Elas são instrumentos centrais para a transformação digital do SUS, visando continuidade do cuidado, "
                "execução de políticas públicas e transparência (Brasil, 2025a). Seus objetivos, conforme estabelecido "
                "legalmente no Art. 16, incluem:"
            )
        )
        + row(
            "<ul>"
            "<li>Ampliar o acesso a dados de forma simplificada e integrada.</li>"
            "<li>Fortalecer a continuidade do cuidado, fornecendo aos profissionais informações essenciais.</li>"
            "<li>Fortalecer a atuação dos gestores, fornecendo informações estratégicas para a tomada de decisão.</li>"
            "<li>Fomentar a cultura de proteção de dados e reduzir desigualdades no acesso à saúde digital.</li>"
            "</ul>"
        )
        + row(
            p(
                "O acesso a essas plataformas é rigorosamente regulado pela Lei de Acesso à Informação (Lei nº 12.527/2011) "
                "e pela Lei Geral de Proteção de Dados (LGPD - Lei nº 13.709/2018), garantindo que as informações sejam "
                "acessadas apenas por quem tem direito e para fins legítimos (Art. 17). Especificamente, o acesso de "
                "profissionais e estabelecimentos de saúde será <strong>restrito e relacionado estritamente ao contexto "
                "de atendimento</strong> (Art. 17, parágrafo único) (Brasil, 2025a)."
            )
        )
        + subheading("Conheça as portas de entrada para a RNDS", "h5")
        + platforms
        + row(p("A partir dessas plataformas, as aplicações práticas se desdobram de maneira distinta para cada grupo:"))
        + subheading("Para profissionais de saúde", "h5")
        + row(
            p(
                "A principal aplicação é a <strong>continuidade do cuidado na prática</strong>. Por meio do "
                "<strong>SUS Digital Profissional</strong>, o profissional pode acessar o histórico clínico completo de "
                "um paciente durante uma consulta, incluindo consultas anteriores, exames realizados, prescrições, "
                "alergias registradas e carteira vacinal, mesmo que esses registros tenham sido gerados em outro município "
                "ou estado (Brasil, 2025a)."
            )
        )
        + row("<p><strong>Algumas possibilidades de aplicações práticas da plataforma:</strong></p>")
        + prof_acc
        + subheading("Para gestores", "h5")
        + row(
            p(
                "A RNDS se converte em uma <strong>ferramenta estratégica de gestão baseada em evidências</strong>. "
                "Por meio do <strong>SUS Digital Gestor</strong>, gestores municipais, estaduais e federais acessam "
                "dados agregados e anonimizados para uma visão unificada e em tempo real da saúde da população."
            )
        )
        + row("<p><strong>Algumas possibilidades de aplicações práticas da plataforma:</strong></p>")
        + gest_acc
        + box_html("Saiba Mais", "Saiba Mais!", saiba_guia)
        + subheading("Para cidadãos", "h5")
        + row(
            p(
                "A aplicação mais tangível é o <strong>protagonismo e a transparência</strong>, quando o paciente/usuário "
                "se torna um agente ativo no cuidado de sua própria saúde. Por meio do aplicativo "
                "<strong>Meu SUS Digital</strong>, o cidadão tem acesso seguro e centralizado às suas informações de "
                "saúde de forma rápida e segura. Nele, é possível ter acesso a histórico clínico, dados de vacinação, "
                "resultados de exames, medicações, posição em fila de transplante, à Caderneta Digital da Criança e a "
                "outros serviços."
            )
        )
        + quotation_block(
            "“O Meu SUS Digital empodera o cidadão, permitindo que ele acesse seu histórico de saúde, "
            "acompanhe seus atendimentos e tome decisões mais conscientes sobre seu próprio cuidado.”",
            "Ana Estela Haddad, Secretária de Informação e Saúde Digital (Brasil, [s. d.])",
        )
        + row("<p><strong>Algumas possibilidades de aplicações práticas da plataforma:</strong></p>")
        + cid_acc
        + box_html("Saiba Mais", "Saiba Mais!", saiba_app)
    )


def art14_table() -> str:
    rows = [
        ("I", "Requisitos técnicos e institucionais para adesão", "Define as especificações que os sistemas locais devem atender para se conectar à RNDS, e as condições de governança que os entes precisam estabelecer."),
        ("II", "Etapas e processos para adesão e efetivação", "Estabelece um cronograma e um fluxo passo a passo para integração, a exemplo da fase piloto da federalização, incorporação progressiva de conjuntos de dados e metas graduais para estados e municípios."),
        ("III", "Forma de suporte técnico contínuo", "Cria canais de assistência (manuais, qualificações etc.) para favorecer a sustentabilidade da rede."),
        ("IV", "Gerenciamento automatizado e seguro de credenciamento e acesso", "Implementa um sistema centralizado de controle de identidade e acesso, garantindo que apenas usuários autorizados acessem dados específicos."),
        ("V", "Forma de autenticação e verificação para proteção dos dados", "Adota mecanismos robustos como certificação digital, token ou biometria para validar a identidade de quem acessa e rastrear todas as consultas aos dados, assegurando não-violabilidade."),
    ]
    tbody = "".join(
        f"<tr><td>{inc}</td><td>{significado}</td><td>{pratica}</td></tr>"
        for inc, significado, pratica in rows
    )
    return (
        '<div class="row justify-content-center"><div class="col-12 col-md-10 col-lg-8 mb-5">'
        '<p class="mb-2"><strong>Tabela 1 – Detalhamento dos Incisos do Art. 14 e sua Aplicação Prática.</strong></p>'
        '<div class="table-responsive"><table class="table table-sm table-bordered align-middle mb-0">'
        '<thead><tr class="bg-primary text-white">'
        "<th scope=\"col\">Inciso</th>"
        "<th scope=\"col\">O que significa</th>"
        "<th scope=\"col\">Como se materializa na prática</th>"
        "</tr></thead><tbody>"
        f"{tbody}"
        "</tbody></table></div>"
        '<p class="figure-caption fonte small mt-2 mb-0">Fonte: Brasil (2025a).</p></div></div>'
    )


def desafios_perspectivas_section() -> str:
    infra_back = (
        "<p><strong>Desafios:</strong></p><ul>"
        "<li><strong>Integração completa:</strong> apesar de mais de 80% dos estados e 68,3% dos municípios estarem integrados, persiste o desafio de incluir os demais entes, especialmente em regiões com menor infraestrutura digital (Brasil, [s. d.]a);</li>"
        "<li><strong>Diversidade de sistemas locais:</strong> conectar milhares de estabelecimentos que utilizam diferentes softwares exige padronização técnica complexa e contínua;</li>"
        "<li><strong>Conectividade e infraestrutura de rede:</strong> garantir acesso à internet de qualidade em todos os pontos de atendimento, especialmente em áreas remotas.</li>"
        "</ul><p><strong>Perspectivas e ações em curso:</strong></p><ul class=\"mb-0\">"
        "<li><strong>Padronização:</strong> uso obrigatório de modelos como o MIRA para uniformizar os dados (Brasil, 2025b);</li>"
        "<li><strong>Retroalimentação:</strong> compromisso do Ministério da Saúde em devolver dados processados aos entes locais, incentivando a adesão (Brasil, 2025b).</li>"
        "</ul>"
    )
    cap_back = (
        "<p><strong>Desafios:</strong></p><ul>"
        "<li><strong>Apropriação tecnológica:</strong> garantir que profissionais, gestores e cidadãos compreendam e saibam utilizar as novas plataformas de forma eficaz;</li>"
        "<li><strong>Cultura baseada em dados:</strong> transformar a rotina de trabalho para incorporar a consulta e a interpretação de dados integrados na tomada de decisão clínica e gerencial;</li>"
        "<li><strong>Capacitação em escala:</strong> implementar programas de treinamento massivos e contínuos para atingir milhares de profissionais em todo o território nacional.</li>"
        "</ul><p><strong>Perspectivas e ações em curso:</strong></p><ul class=\"mb-0\">"
        "<li><strong>Plataformas intuitivas:</strong> as plataformas SUS Digital foram desenhadas para simplificar o acesso;</li>"
        "<li><strong>Empoderamento do cidadão:</strong> com mais de 59 milhões de downloads, o Meu SUS Digital já é uma realidade para milhões de pessoas/usuários (Brasil, [s. d.]a);</li>"
        "<li><strong>Guias e suporte:</strong> a disponibilização de guias técnicos, como o Guia da RNDS, e a previsão de suporte contínuo pelos entes federativos (Brasil, 2025a).</li>"
        "</ul>"
    )
    seg_back = (
        "<p><strong>Desafios:</strong></p><ul>"
        "<li><strong>Proteção de dados sensíveis:</strong> a RNDS lida com bilhões de registros de saúde, informações sensíveis por excelência, que são alvo permanente de ameaças cibernéticas (Brasil, [s. d.]a);</li>"
        "<li><strong>Conformidade regulatória:</strong> garantir a adesão integral à LGPD (Lei nº 13.709/2018) e a outras normativas de segurança em todos os níveis da federação (Brasil, 2018; Brasil, 2025a).</li>"
        "</ul><p><strong>Perspectivas e ações em curso:</strong></p><ul class=\"mb-0\">"
        "<li><strong>Previsão legal:</strong> o decreto da RNDS e suas portarias regulamentadoras reiteram o compromisso com a LGPD, a privacidade e a segurança da informação (Brasil, 2018; Brasil, 2025b; Brasil, 2025a);</li>"
        "<li><strong>Mecanismos técnicos de segurança:</strong> a federalização prevê a definição de formas robustas de autenticação, verificação e gerenciamento automatizado de credenciamento (Brasil, 2025a);</li>"
        "<li><strong>Governança com participação federativa:</strong> coordenação nacional com participação dos estados e municípios na proteção dos dados.</li>"
        "</ul>"
    )
    return (
        subheading(
            "Desafios e perspectivas: infraestrutura, capacitação, segurança da informação",
            "h6",
        )
        + flip_row(
            flipcard("m4a2d1", "Infraestrutura tecnológica", infra_back),
            flipcard("m4a2d2", "Capacitação de profissionais e gestores", cap_back),
            flipcard(
                "m4a2d3",
                "Segurança da informação e proteção de dados",
                seg_back,
            ),
        )
    )


def content_topico7() -> str:
    video_section = video_box(
        "https://www.youtube.com/watch?v=t3q8X2RNarU",
        "Assista ao vídeo e acompanhe o andamento da fase piloto da federalização da RNDS:",
        "Federalização da RNDS",
    )
    return (
        heading(7, TOPICS[6][1])
        + row(
            p(
                "A <strong>federalização da RNDS</strong> representa um marco na consolidação do SUS como uma rede "
                "verdadeiramente integrada e cooperativa. Mais do que uma simples centralização de informações, a "
                "federalização é um modelo de gestão que equilibra a <strong>coordenação nacional</strong> com a "
                "<strong>autonomia local</strong>, garantindo que dados de saúde sejam acessíveis de forma ágil e "
                "segura por todos os entes federativos, em benefício do cidadão."
            )
        )
        + quotation_block(
            "“Garantir o acesso integral, ágil e descentralizado a seus dados pelos Estados, pelo Distrito Federal "
            "e pelos Municípios, de forma a promover a transição e continuidade do cuidado ao cidadão.”",
            intro="Conforme estabelece o Art. 13 do Decreto nº 12.560, a federalização tem por objetivo:",
        )
        + row(
            p(
                "Isso significa que a RNDS não é controlada exclusivamente pela União. Em vez disso, é uma "
                "plataforma federada na qual os dados permanecem sob a responsabilidade primária de "
                "quem os gerou (estados e municípios), mas são compartilhados de forma padronizada e segura para "
                "permitir a continuidade do cuidado, gestão descentralizada, transparência e controle social."
            )
        )
        + row(
            p(
                "Além disso, tem-se o Art. 14 do Decreto nº 12.560, que estabelece com clareza as "
                "responsabilidades do Ministério da Saúde na condução do processo de federalização. Este artigo não "
                "apenas atribui competências, mas desenha um modelo estruturado e seguro para garantir "
                "que a descentralização do acesso aos dados ocorra com padrão técnico, segurança jurídica e suporte "
                "adequado. Esta se dá por meio de ato normativo próprio, conforme a tabela abaixo:"
            )
        )
        + art14_table()
        + row(
            p(
                "Embora o Art. 14 atribua ao Ministério da Saúde a competência para editar a norma de implementação, "
                "esse processo não é unilateral. A construção desse ato normativo ocorre no âmbito das "
                "<strong>instâncias de governança compartilhada da RNDS</strong>, como comitês técnicos com participação "
                "de Estados e Municípios. Essa construção coletiva assegura que os requisitos e etapas sejam factíveis "
                "e atendam às realidades locais, verdadeiro cerne do federalismo cooperativo na saúde digital "
                "(Brasil, 2025a; Brasil, 2020)."
            )
        )
        + video_section
        + desafios_perspectivas_section()
    )


def content_topico8() -> str:
    return (
        heading(8, TOPICS[7][1])
        + row(
            p(
                "Antes de tratarmos sobre qualidade de dados é importante destacar dois elementos técnicos essenciais "
                "para que os dados do serviço de qualquer local do Brasil possam fluir para a RNDS: o "
                "<strong>integrador</strong> e o <strong>conector</strong> (Brasil, [s. d.]b)."
            )
        )
        + row(
            "<ul class=\"mb-0\">"
            "<li class=\"mb-3\"><strong>Integrador:</strong> é o <strong>profissional ou equipe de TI</strong> responsável por "
            "desenvolver e implementar a solução que permitirá a um Sistema de Informação em Saúde se comunicar com a RNDS.</li>"
            "<li><strong>Conector:</strong> é o <strong>software propriamente dito</strong> desenvolvido pelo integrador. "
            "É este programa que, instalado no estabelecimento de saúde, realiza a troca segura e padronizada de "
            "informações com os servidores da RNDS.</li>"
            "</ul>"
        )
        + row(
            p(
                "O trabalho do integrador, materializado no conector, é a <strong>primeira e mais crucial camada de "
                "garantia da qualidade</strong>. É no momento da integração local que os dados brutos são filtrados, "
                "validados e traduzidos para um padrão nacional. Um Conector bem desenvolvido, seguindo as especificações "
                "do Guia, é a base para que informações confiáveis entrem na RNDS."
            )
        )
        + row(
            p(
                "A qualidade dos dados na RNDS é, portanto, um resultado direto da <strong>arquitetura técnica robusta</strong> "
                "(que impõe padrões como FHIR) combinada com uma <strong>estratégia ativa de governança e capacitação</strong>. "
                "O trabalho dos integradores, guiado pelos padrões e ferramentas fornecidos pelo Ministério da Saúde, é o "
                "elo crítico que transforma dados locais em informações nacionais confiáveis, seguras e prontas para salvar vidas."
            )
        )
        + row(
            p(
                "O Guia da RNDS detalha que o conector é responsável por executar uma sequência de processos que, em si, "
                "são etapas de qualificação dos dados antes do envio como: filtragem e coleta; mapeamento e conversão; "
                "criação do recurso FHIR; validação do “Bundle” e autenticação segura."
            )
        )
        + row(
            p(
                'Para se aprofundar no papel do integrador e nos requisitos técnicos, você pode acessar diretamente: '
                '<a href="https://rnds-guia.saude.gov.br/" target="_blank" rel="noopener noreferrer">'
                "https://rnds-guia.saude.gov.br/</a>"
            )
        )
    )


def content_topico9() -> str:
    refs = "".join(f'<p class="referencias-item mb-3">{r}</p>\n' for r in REFERENCES)
    return (
        f'<div class="row justify-content-center"><div class="col-12 col-md-10 col-lg-8 mb-5 referencias-aula">'
        f'<div class="heading__block"><span class="small">Tópico 9</span>'
        f'<h3 class="heading__title">Referências</h3></div>\n{refs}</div></div>'
    )


CONTENT_BUILDERS = [
    content_topico1,
    content_topico2,
    content_topico3,
    content_topico4,
    content_topico5,
    content_topico6,
    content_topico7,
    content_topico8,
    content_topico9,
]


def generate_all() -> list[Path]:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    created = []
    for i, builder in enumerate(CONTENT_BUILDERS, 1):
        path = OUT_DIR / f"topico{i}.html"
        path.write_text(build_page(i, builder()), encoding="utf-8")
        created.append(path)
        print(f"Criado: {path.relative_to(ROOT)}")
    orphan = OUT_DIR / "topico10.html"
    if orphan.exists():
        orphan.unlink()
        print(f"Removido: {orphan.relative_to(ROOT)}")
    return created


AULA2_ITEM = (
    '\t\t\t\t\t\t\t\t<li class="dropdown-menu__item">\n'
    '\t\t\t\t\t\t\t\t\t<a class="dropdown-menu__item-link" tabindex="0" role="link" '
    'href="../aula2/topico1.html"><strong>Aula 2: </strong>Integração de Dados em Saúde</a>\n'
    "\t\t\t\t\t\t\t\t</li>\n"
)


def update_index() -> None:
    index_path = ROOT / "index.html"
    text = index_path.read_text(encoding="utf-8")
    old_li = '<li class="list-group-item">Aula 4.2: Integração de Dados em Saúde</li>'
    new_li = (
        '<li class="list-group-item"><a href="modulo4/aula2/topico1.html">'
        "Aula 4.2: Integração de Dados em Saúde</a></li>"
    )
    if old_li in text:
        text = text.replace(old_li, new_li)
    index_path.write_text(text, encoding="utf-8")
    print(f"Atualizado: {index_path.relative_to(ROOT)}")


def update_aula1_sidebars() -> int:
    count = 0
    aula1_dir = ROOT / "modulo4" / "aula1"
    sidebar_marker = "<strong>Aula 2: </strong>Integração de Dados em Saúde</a>"
    for html in aula1_dir.glob("*.html"):
        text = html.read_text(encoding="utf-8")
        if sidebar_marker in text:
            continue
        needle = (
            '<li class="dropdown-menu__item"><a class="dropdown-menu__item-link" tabindex="0" role="link" '
            'href="../aula1/topico1.html"><strong>Aula 1: </strong>Interoperabilidade na Saúde</a></li>'
        )
        if needle not in text:
            continue
        text = text.replace(needle, needle + "\n" + AULA2_ITEM.strip())
        html.write_text(text, encoding="utf-8")
        count += 1
    print(f"Sidebars aula1 atualizados: {count} arquivos")
    return count


def main() -> None:
    print("=== Gerando modulo4/aula2 ===")
    files = generate_all()
    print("\n=== Atualizando index.html ===")
    update_index()
    print("\n=== Atualizando sidebars modulo4/aula1 ===")
    update_aula1_sidebars()
    print(f"\nTotal: {len(files)} arquivos HTML gerados.")


if __name__ == "__main__":
    main()
