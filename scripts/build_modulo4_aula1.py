#!/usr/bin/env python3
"""Gera HTML da Aula 4.1 (Módulo 4) e atualiza index/sidebars."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "modulo4" / "aula1"
ASSETS = "../../"

MODULE_NUM = 4
MODULE_TITLE = "Interoperabilidade de Sistemas"
AULA_LABEL = "Aula 1"
AULA_TITLE = "Interoperabilidade na Saúde"
AUTHOR = "José Nildo de Barros Silva Júnior"
AUTHOR_BIO = (
    "Pesquisador em Saúde Pública no Instituto de Comunicação e Informação "
    "Científica e Tecnológica em Saúde (ICICT), Fundação Oswaldo Cruz (Fiocruz) "
    "– Rio de Janeiro (RJ)."
)

TOPICS = [
    ("Sobre esta aula", "Sobre esta aula"),
    ("O que é interoperabilidade?", "O que é interoperabilidade?"),
    ("Importância e vantagens", "Importância e vantagens"),
    ("Dimensões da interoperabilidade", "Dimensões da interoperabilidade"),
    ("Importância na Saúde Pública", "Importância na Saúde Pública"),
    ("Pareamento de dados", "Pareamento de dados"),
    ("Tipos de pareamento e métodos", "Tipos de pareamento e métodos"),
    ("Aplicações e importância na saúde pública", "Aplicações e importância na saúde pública"),
    ("Referências", "Referências"),
]

def mod4_dropdown_item(prefix: str = "../../") -> str:
    return (
        '\t\t\t\t\t\t\t\t<li class="dropdown-menu__item">\n'
        '\t\t\t\t\t\t\t\t\t<a class="dropdown-menu__item-link" tabindex="0" role="link" '
        f'href="{prefix}modulo4/aula1/topico1.html"><strong>Módulo 4</strong><br />'
        f"{MODULE_TITLE}</a>\n"
        "\t\t\t\t\t\t\t\t</li>\n"
    )

REFERENCES = [
    'BALIAN, D. M. C.; SUPPI, G. D.; CRUZ, J. V. S.; BERNARDES, M. V. A interoperabilidade de dados na saúde e os desafios da privacidade: uma análise sob a perspectiva da LGPD. <strong>Revista Foco</strong> (Interdisciplinary Studies Journal), v. 18, n. 5, 2025. Disponível em: <a href="https://ojs.focopublicacoes.com.br/foco/article/download/8733/6172/21508" target="_blank" rel="noopener noreferrer">https://ojs.focopublicacoes.com.br/foco/article/download/8733/6172/21508</a>. Acesso em: 12 dez. 2025.',
    'BRASIL. Câmara dos Deputados. Centro de Documentação e Informação. <strong>Lei nº 14.129, de 29 de março de 2021</strong>. Dispõe sobre princípios, regras e instrumentos para o Governo Digital. Brasília, DF: CD, 2021. Disponível em: <a href="https://www2.camara.leg.br/legin/fed/lei/2021/lei-14129-29-marco-2021-791203-normaatualizada-pl.pdf" target="_blank" rel="noopener noreferrer">https://www2.camara.leg.br/legin/fed/lei/2021/lei-14129-29-marco-2021-791203-normaatualizada-pl.pdf</a>. Acesso em: 12 dez. 2025.',
    'BRASIL. Governo Digital. <strong>Conecta gov.br</strong>. Brasília, DF, [s. d.]. Disponível em: <a href="https://www.gov.br/governodigital/pt-br/infraestrutura-nacional-de-dados/interoperabilidade/conecta-gov.br" target="_blank" rel="noopener noreferrer">https://www.gov.br/governodigital/pt-br/infraestrutura-nacional-de-dados/interoperabilidade/conecta-gov.br</a>. Acesso em: 12 dez. 2025.',
    'BRASIL. Governo Digital. <strong>Interoperabilidade</strong>. Brasília, DF, [s. d.]. Disponível em: <a href="https://www.gov.br/governodigital/pt-br/infraestrutura-nacional-de-dados/interoperabilidade" target="_blank" rel="noopener noreferrer">https://www.gov.br/governodigital/pt-br/infraestrutura-nacional-de-dados/interoperabilidade</a>. Acesso em: 12 dez. 2025.',
    'BRASIL. Ministério da Saúde. Secretaria de Vigilância em Saúde. <strong>Boletim Epidemiológico de Coinfecção TB-HIV</strong>. Brasília, DF: MS, 2022. Disponível em: <a href="https://www.gov.br/aids/pt-br/central-de-conteudo/boletins-epidemiologicos/2022/coinfeccao-tb-hiv/boletim_coinfeccao_tb_hiv_2022.pdf" target="_blank" rel="noopener noreferrer">https://www.gov.br/aids/pt-br/central-de-conteudo/boletins-epidemiologicos/2022/coinfeccao-tb-hiv/boletim_coinfeccao_tb_hiv_2022.pdf</a>. Acesso em: 12 dez. 2025.',
    'BRASIL. Ministério da Saúde. Gabinete do Ministro. <strong>Portaria nº 1.434, de 28 de maio de 2020</strong>. Institui o Programa Conecte SUS e altera a Portaria de Consolidação nº 1/GM/MS, de 28 de setembro de 2017, para instituir a Rede Nacional de Dados em Saúde e dispor sobre a adoção de padrões de interoperabilidade em saúde. Brasília, DF: MS, 28 maio 2020. Disponível em: <a href="https://bvsms.saude.gov.br/bvs/saudelegis/gm/2020/prt1434_29_05_2020.html" target="_blank" rel="noopener noreferrer">https://bvsms.saude.gov.br/bvs/saudelegis/gm/2020/prt1434_29_05_2020.html</a>. Acesso em: 12 dez. 2025.',
    'BRASIL. Ministério do Planejamento, Orçamento e Gestão. Secretaria de Logística e Tecnologia da Informação. <strong>Guia de interoperabilidade:</strong> manual do gestor. Brasília, DF: MP, 2012. Disponível em: <a href="https://www.gov.br/governodigital/pt-br/governanca-de-dados/Guia_de_Interoperabilidade_Manual_do_Gestor_2012.pdf" target="_blank" rel="noopener noreferrer">https://www.gov.br/governodigital/pt-br/governanca-de-dados/Guia_de_Interoperabilidade_Manual_do_Gestor_2012.pdf</a>. Acesso em: 12 dez. 2025.',
    'BRASIL. Presidência da República. Secretaria-Geral. Subchefia para Assuntos Jurídicos. <strong>Decreto nº 10.046, de 9 de outubro de 2019</strong>. Institui a governança de compartilhamento de dados no âmbito da administração pública federal. Brasília, DF: 9 out. 2019. Disponível em: <a href="https://www.planalto.gov.br/ccivil_03/_Ato2019-2022/2019/Decreto/D10046.htm" target="_blank" rel="noopener noreferrer">https://www.planalto.gov.br/ccivil_03/_Ato2019-2022/2019/Decreto/D10046.htm</a>. Acesso em: 12 dez. 2025.',
    'BRASIL. Presidência da República. Secretaria-Geral. Subchefia para Assuntos Jurídicos. <strong>Lei nº 13.709, de 14 de agosto de 2018</strong>. Dispõe sobre a Lei Geral de Proteção de Dados Pessoais (LGPD). Brasília, DF: Pres. da Rep., 14 ago. 2018. Disponível em: <a href="https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm" target="_blank" rel="noopener noreferrer">https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm</a>. Acesso em: 12 dez. 2025.',
    'BRASIL. Presidência da República. Secretaria-Geral. Subchefia para Assuntos Jurídicos. <strong>Lei nº 14.534, de 10 de janeiro de 2023</strong>. Altera as Leis nºs 7.116/1983, 9.454/1997, 13.444/2017 e 13.460/2017 para adotar número único para os documentos que especifica e estabelecer o Cadastro de Pessoas Físicas (CPF) como número suficiente para identificação do cidadão nos bancos de dados de serviços públicos. Brasília, DF: Pres. da Rep., 11 jan. 2023. Disponível em: <a href="https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2023/lei/l14534.htm" target="_blank" rel="noopener noreferrer">https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2023/lei/l14534.htm</a>. Acesso em: 12 dez. 2025.',
    'COELI, C. M.; PINHEIRO, R. S.; CAMARGO JR., K. R. Conquistas e desafios para o emprego das técnicas de record linkage na pesquisa e avaliação em saúde no Brasil. <strong>Epidemiologia e Serviços de Saúde</strong>, Brasília, DF, v. 24, n. 4, p. 637-646, 2015. Disponível em: <a href="https://www.scielo.br/j/ress/a/zH4GSZzP9DNZRxwGz3wpMTL/" target="_blank" rel="noopener noreferrer">https://www.scielo.br/j/ress/a/zH4GSZzP9DNZRxwGz3wpMTL/</a>. Acesso em: 12 dez. 2025.',
    'GODOY, A.; LOPES, Â. M. M. A importância da interoperabilidade nos níveis de complexidade do SUS: gestão, segurança e qualidade da saúde. <strong>Revista FT – Ciências da Saúde</strong>, v. 29, ed. 145, abr. 2025. Disponível em: <a href="https://revistaft.com.br/a-importancia-da-interoperabilidade-nos-niveis-de-complexidade-do-sus-gestao-seguranca-e-qualidade-de-saude/" target="_blank" rel="noopener noreferrer">https://revistaft.com.br/a-importancia-da-interoperabilidade-nos-niveis-de-complexidade-do-sus-gestao-seguranca-e-qualidade-de-saude/</a>. Acesso em: 12 dez. 2025.',
]

OBJECTIVES = [
    "Definir o conceito de interoperabilidade no contexto da saúde.",
    "Identificar os principais benefícios e vantagens da interoperabilidade para a Administração Pública e o cidadão.",
    "Diferenciar as dimensões ou níveis da interoperabilidade.",
    "Relacionar a importância da interoperabilidade para a Saúde Pública.",
    "Explicar o conceito e o objetivo do pareamento de dados em Saúde Pública.",
    "Comparar os métodos de pareamento determinístico e probabilístico.",
    "Exemplificar as aplicações do linkage na produção de indicadores e na qualificação da informação em saúde.",
]

LINKAGE_QUESTIONS = [
    "uma pessoa com tuberculose também vive com HIV, e se está em uso de TARV regularmente?",
    "as condições climáticas (chuvas, temperatura) influenciam o aumento de casos de leptospirose ou dengue?",
    "um caso de covid-19 grave ocorreu em uma pessoa com doença crônica preexistente registrada no SIA/SIH?",
    "os casos de sífilis congênita estão concentrados em áreas com baixa cobertura pré-natal?",
    "as áreas com maior vulnerabilidade social (CadÚnico) também concentram maior carga de doenças infecciosas?",
    "há relação entre desmatamento, clima e surtos de doenças respiratórias na Amazônia?",
]

PAR_EXERCISES = [
    ("Kamylla Carvalho", "20050825", "Kamyla Carvalho", "20050825", "não par", "par"),
    ("Marizete Zanini", "19820406", "Marizete Zanini", "19820406", "par", "par"),
    ("João Victor", "19990309", "Joao Vitor", "19990309", "não par", "par"),
    ("Yury Bitencourt", "19960915", "Yuri Santos", "19990615", "não par", "não par"),
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


def box(kind: str, label: str, body: str, *, raw: bool = False) -> str:
    body_html = body if raw else f'<p class="mb-0">{body}</p>'
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


def flipcard(card_id: str, title: str, back_html: str) -> str:
    return (
        f'<div class="col-12 col-md-6"><div class="flipcard"><div class="flip-card">'
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
        f'<div class="card-header">Exemplo {num}</div><div class="card-body">'
        f'<div class="exercise__question"><p>{question}</p></div>'
        f'<div class="exercise__answers"><ul>{answers}</ul></div></div>'
        f'<div class="card-footer"><div class="exercise__submit">'
        f'<span class="exercise__submit--feedback d-none"></span>'
        f'<button class="fio-button fio-button-primary" type="submit" disabled>Conferir</button>'
        f"</div></div></div></div>",
        "mb-5",
    )


def par_exercise(num: int, method: str, n1: str, d1: str, n2: str, d2: str, correct: str) -> str:
    correct_par = correct == "par"
    fb_par = (
        "Correta. Os registros correspondem ao mesmo indivíduo para este método de pareamento."
        if correct_par
        else "Incorreta. Para este método, os registros não devem ser considerados o mesmo indivíduo."
    )
    fb_nao = (
        "Incorreta. Para este método, os registros devem ser considerados o mesmo indivíduo."
        if correct_par
        else "Correta. Os registros não correspondem ao mesmo indivíduo para este método de pareamento."
    )
    return exercise_block(
        num,
        f"Considerando um resultado do pareamento <strong>{method}</strong>, os registros abaixo são par ou não par?<br />"
        f"<strong>Base 1:</strong> {n1} — {d1}<br /><strong>Base 2:</strong> {n2} — {d2}",
        [("Par", fb_par, correct_par), ("Não par", fb_nao, not correct_par)],
    )


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
    if num > 1:
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
            '<a class="fio-button fio-button-primary" href="../aula2/topico1.html" rel="next">Próxima aula '
            '<span class="material-symbols-rounded" aria-hidden="true">east</span></a>'
        )
    inner = "".join(parts)
    return (
        f"\t\t\t<section><div class=\"container\"><div class=\"row justify-content-center\">"
        f"<div class=\"col-12 col-md-10 col-lg-8\"><div class=\"page-nav d-flex justify-content-evenly flex-wrap gap-3\">"
        f"{inner}</div></div></div></div></section>\n"
    )


def extra_scripts(num: int) -> str:
    if num in (6, 7):
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
								<li class="dropdown-menu__item"><a class="dropdown-menu__item-link" tabindex="0" role="link" href="../aula1/topico1.html"><strong>Aula 1: </strong>{AULA_TITLE}</a></li>
								<li class="dropdown-menu__item"><a class="dropdown-menu__item-link" tabindex="0" role="link" href="../aula2/topico1.html"><strong>Aula 2: </strong>Integração de Dados em Saúde</a></li>
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
							<img class="img-fluid regua-logos" src="{ASSETS}media/logos/regua-de-logos.png" alt="Régua de logos: Campus Virtual Fiocruz, Fiocruz, SUS Digital, SUS 35 Anos, Ministério da Saúde e Governo do Brasil" />
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
        + row(p("Seja bem-vindo e bem-vinda à aula <strong>“Interoperabilidade na Saúde”</strong>."))
        + row(p("A seguir veja algumas informações importantes!"))
        + row(
            p(
                "Suponha tentar conectar um carregador de um modelo antigo de celular em um smartphone novo. "
                "Eles simplesmente não se conectam, certo? Em informática e em gestão da informação, problemas de "
                '"conexão" e "comunicação" entre sistemas são muito comuns. A interoperabilidade é a solução para '
                "esse desafio. Ela vai além da simples troca de dados; é sobre fazer com que sistemas diferentes, "
                "desenvolvidos por times diferentes e em momentos diferentes, possam trabalhar juntos de forma "
                "eficiente e sem perder o significado das informações."
            )
        )
        + subheading("Objetivos de aprendizagem")
        + row("<p>Ao final desta aula você será capaz de:</p><div class=\"list\"><ul class=\"list-group\">" + objs + "</ul></div>")
        + subheading("Autoria")
        + row(f"<p><strong>{AUTHOR}</strong></p><p>{AUTHOR_BIO}</p>")
    )


def content_topico2() -> str:
    return (
        heading(2, TOPICS[1][1])
        + row(
            p(
                "A interoperabilidade refere-se à capacidade que diferentes sistemas de informação, plataformas, "
                "dispositivos ou organizações, sejam eles informatizados ou não, possuem de estabelecer comunicação "
                "entre si para compartilhar dados de maneira estruturada, segura e eficiente. Esse processo ocorre de "
                "forma automática, sem exigir reentrada manual da mesma informação pelo usuário, assegurando qualidade "
                "e agilidade à prestação de serviços. Na esfera pública, essa capacidade é fundamental para que o "
                "cidadão não precise reapresentar repetidamente suas informações a diferentes órgãos, permitindo uma "
                "experiência integrada e menos burocrática (Brasil, [s. d.]a)."
            )
        )
        + figure_block(
            "Figura 1 – Interoperabilidade na saúde.",
            f"{ASSETS}media/modulo4/aula1-fig1.jpeg",
            "Ilustração sobre interoperabilidade na saúde.",
            "Fonte: Freepik",
        )
    )


def content_topico3() -> str:
    return (
        heading(3, TOPICS[2][1])
        + row(
            p(
                "Compreender a importância da interoperabilidade é essencial para perceber como ela transforma a relação "
                "entre governo e cidadão. Quando diferentes sistemas conseguem se comunicar e compartilhar dados de "
                "forma estruturada e segura, os serviços públicos tornam-se mais ágeis, menos burocráticos e muito mais "
                "eficientes. Isso significa que você, como cidadão, não precisa fornecer repetidamente as mesmas "
                "informações a diferentes órgãos, um ganho que parece simples, mas que representa economia de tempo, "
                "redução de custos e maior confiabilidade nos processos (Brasil, [s. d.]a)."
            )
        )
        + row(
            p(
                "A interoperabilidade é um dos pilares do governo digital brasileiro. Ela permite que órgãos públicos "
                "integrem suas bases de dados e utilizem padrões comuns para troca de informações, seja em nível "
                "institucional, regional, nacional ou até transnacional. Essa integração não apenas facilita a "
                "prestação de serviços, mas também fortalece a tomada de decisão dos gestores, que passam a contar com "
                "dados mais completos e consistentes para planejar políticas públicas (Balian et al., 2025)."
            )
        )
        + row(
            p(
                "Além disso, é possível observar os benefícios de forma concreta a partir dos dados do programa Conecta "
                "gov.br. A interoperabilidade já gerou economia superior a R$ 12 bilhões e viabilizou bilhões de "
                "transações automáticas entre órgãos federais, eliminando redundâncias e acelerando processos "
                "(Brasil, [s. d.]b). Essa prática também contribui para a confiabilidade dos cadastros, pois permite "
                "cruzamento de informações com base no Comprovante de Situação Cadastral (CPF), conforme previsto no "
                "Art. 39 da Lei nº 14.129/2021. Essa lei estabelece objetivos claros para a interoperabilidade, como "
                "aprimorar a gestão de políticas públicas, aumentar a segurança das informações e viabilizar meios "
                "unificados de identificação do cidadão (Brasil, 2021)."
            )
        )
        + row(
            p(
                "Outro ponto relevante é a governança de dados, regulamentada pelo Decreto nº 10.046/2019, que "
                "instituiu o Cadastro Base do Cidadão e o Comitê Central de Governança de Dados. Essa estrutura garante "
                "que a interoperabilidade ocorra com qualidade, respeitando a Lei Geral de Proteção de Dados (LGPD) e "
                "assegurando a privacidade dos cidadãos (Brasil, 2019)."
            )
        )
        + box(
            "Importante",
            "Importante!",
            "A interoperabilidade não é um fim em si mesma. É um meio para se alcançar objetivos maiores, como "
            "continuidade do cuidado, vigilância em saúde eficaz, redução de custos e melhoria dos resultados para "
            "os pacientes e para a população.",
        )
    )


def content_topico4() -> str:
    return (
        heading(4, TOPICS[3][1])
        + row(
            p(
                "A interoperabilidade pode ser compreendida em diferentes dimensões que se comunicam e se complementam "
                "(Brasil, 2012):"
            )
        )
        + figure_block(
            "Dimensões da interoperabilidade.",
            f"{ASSETS}media/modulo4/aula1-dimensoes-interoperabilidade.png",
            "Diagrama das dimensões da interoperabilidade: organizacional, semântica e técnica.",
        )
        + box(
            "Saiba Mais",
            "Saiba Mais!",
            'O portal Governo Digital disponibiliza uma série de documentos (leis, decretos e portarias) relacionados a '
            "legislação, governança de dados e interoperabilidade. "
            '<a href="https://www.gov.br/governodigital/pt-br/infraestrutura-nacional-de-dados/interoperabilidade" '
            'target="_blank" rel="noopener noreferrer">Governança de Dados e Interoperabilidade — Governo Digital</a>. '
            "A Lei nº 14.129/2021 (Lei do Governo Digital) estabelece a interoperabilidade como princípio do Estado. "
            "Em seu Art. 39, ela define finalidades específicas para o mecanismo de interoperabilidade. Leia na íntegra: "
            '<a href="https://www2.camara.leg.br/legin/fed/lei/2021/lei-14129-29-marco-2021-791203-normaatualizada-pl.pdf" '
            'target="_blank" rel="noopener noreferrer">Lei nº 14.129/2021</a>.',
        )
        + row(
            p(
                "A <strong>interoperabilidade organizacional</strong> envolve cooperação entre instituições que precisam "
                "compartilhar informações, mesmo possuindo estruturas internas e processos de negócio distintos. Cada "
                "organização tem seus próprios fluxos e tempos de execução, o que torna necessário harmonizar essas "
                "diferenças. Um dos grandes desafios é identificar quando e como essa integração deve ocorrer. Para "
                "isso, é fundamental que as instituições conheçam os processos umas das outras, o que só é possível se "
                "esses processos estiverem modelados e padronizados (Brasil, 2012)."
            )
        )
        + box(
            "Exemplo",
            "Exemplo!",
            "A Lei Geral de Proteção de Dados (LGPD - Lei nº 13.709/2018) é elemento central da interoperabilidade "
            "organizacional no Brasil, ao estabelecer regras para o compartilhamento de dados pessoais.",
        )
        + row(
            p(
                "A <strong>interoperabilidade semântica</strong> refere-se à capacidade de dois ou mais sistemas "
                "heterogêneos trabalharem juntos, garantindo que os dados trocados sejam interpretados corretamente. "
                "Isso significa que, além de transmitir informações, é preciso assegurar que o significado seja "
                "preservado dentro do contexto da transação, respeitando terminologias, convenções e cultura de cada "
                "setor. Essa dimensão é essencial para evitar ambiguidades e garantir que todos os envolvidos "
                "compreendam os dados da mesma forma (Brasil, 2012)."
            )
        )
        + box(
            "Exemplo",
            "Exemplo!",
            'Quando um sistema envia o código A15 para outro, ambos devem interpretar, sem ambiguidade ou margem para '
            "erro, que esse código corresponde a “Tuberculose respiratória, com confirmação bacteriológica e histológica”, "
            "conforme a CID-10. Esse entendimento comum evita interpretações equivocadas e garante que os dados sejam "
            "usados corretamente em prescrições, relatórios ou análises epidemiológicas. Para isso, padrões como CID-10, "
            "SNOMED CT (para termos clínicos) e LOINC (para exames laboratoriais) são fundamentais.",
        )
        + row(
            p(
                "Já a <strong>interoperabilidade técnica</strong> trata do “como fazer” essa integração. Ela envolve "
                "padrões tecnológicos para apresentação, coleta, troca, processamento e transporte de dados, abrangendo "
                "hardware, software e protocolos. Após definir os momentos e motivos para interoperar e estabelecer "
                "vocabulários comuns, é necessário adotar padrões técnicos que permitam a comunicação entre sistemas. No "
                "Brasil, esses padrões estão descritos na Arquitetura e-PING, que orienta a interoperabilidade no "
                "governo eletrônico (Brasil, 2012)."
            )
        )
        + box(
            "Exemplo",
            "Exemplo!",
            "Dois postos de saúde conseguem trocar informações de pacientes porque seus sistemas utilizam padrões "
            "compatíveis definidos pela e-PING, como protocolos seguros e formatos padronizados. Na área da saúde, um "
            "exemplo comum é o uso do padrão HL7 FHIR (Fast Healthcare Interoperability Resources), que permite que "
            "sistemas diferentes compartilhem dados clínicos de forma estruturada e segura.",
        )
        + row(
            p(
                "Embora essas três dimensões sejam amplamente reconhecidas, a Portaria nº 1.434, de 28 de maio de 2020, "
                "também estabelece o conceito de interoperabilidade sintática. Essa abordagem garante que diferentes "
                "sistemas possam trocar informações padronizadas de forma que sejam compreendidas tanto por máquinas "
                "quanto por pessoas, sem perda de significado ou contexto. Em outras palavras, ela assegura que a "
                "conversão entre linguagens computacionais e humanas ocorra de maneira precisa (Brasil, 2020)."
            )
        )
        + box(
            "Exemplo",
            "Exemplo!",
            'Dois sistemas concordam em usar formatos padronizados para troca de dados, como XML ou JSON, seguindo uma '
            "estrutura definida. Por exemplo, se um sistema espera &lt;nome&gt;João&lt;/nome&gt; (XML) e o outro envia "
            '{ "nome": "João" } (JSON), ocorre uma falha sintática porque a estrutura não corresponde ao padrão '
            "acordado. A interoperabilidade sintática garante que ambos utilizem o mesmo formato e estrutura, evitando "
            "erros na interpretação.",
        )
    )


def content_topico5() -> str:
    return (
        heading(5, TOPICS[4][1])
        + row(
            p(
                "A interoperabilidade é uma ferramenta estratégica para garantir gestão eficiente, segurança do paciente "
                "e qualidade assistencial no SUS. Em um sistema que opera em diferentes níveis de complexidade (Atenção "
                "Primária, especializada e hospitalar), a integração de dados é essencial para evitar fragmentação das "
                "informações e assegurar a continuidade do cuidado (Godoy; Lopes, 2025)."
            )
        )
        + row(
            p(
                "Quando sistemas interoperam, os profissionais têm acesso a um histórico clínico completo, o que reduz "
                "duplicidade de exames, agiliza diagnósticos e melhora a tomada de decisão. Essa integração também "
                "fortalece a gestão pública, permitindo monitoramento de indicadores, planejamento de recursos e respostas "
                "mais rápidas a crises sanitárias. Além disso, a interoperabilidade contribui para a segurança da "
                "informação, garantindo que dados sejam compartilhados com integridade e em conformidade com a LGPD "
                "(Godoy; Lopes, 2025)."
            )
        )
        + figure_block(
            "Figura 2 – Importância da interoperabilidade na Saúde Pública.",
            f"{ASSETS}media/modulo4/aula1-fig2.jpeg",
            "Ilustração sobre importância da interoperabilidade na Saúde Pública.",
            "Fonte: Freepik",
        )
        + box(
            "Para Refletir",
            "Para Refletir!",
            "Como a falta de integração entre uma Unidade de Saúde da Família e um hospital de referência pode impactar "
            "o cuidado de um paciente crônico? E como a interoperabilidade pode transformar essa jornada?",
        )
        + row(
            p(
                "Além disso, a interoperabilidade é um alicerce para a Vigilância em Saúde, pois permite notificação e "
                "rastreamento mais ágil de agravos, surtos e eventos de interesse público, fortalecendo a capacidade de "
                "resposta do SUS. Também viabiliza a pesquisa e a produção de conhecimento a partir de dados reais e "
                "populacionais, fundamentais para avaliação de políticas e avanços científicos."
            )
        )
        + box(
            "Exemplo",
            "Exemplo!",
            "Na prática, a interoperabilidade permite que o profissional da saúde da Estratégia Saúde da Família veja, "
            "em tempo real, a alta hospitalar de um paciente hipertenso, junto com o novo esquema medicamentoso prescrito. "
            "Isso permite que a equipe da Atenção Primária agende uma visita domiciliar proativa, evitando uma possível "
            "reinternação. Essa é a integralidade do cuidado materializada pela tecnologia.",
        )
        + row(
            p(
                "Além disso, vale mencionar a Rede Nacional de Dados em Saúde (RNDS), iniciativa do Ministério da Saúde "
                "que conecta sistemas e serviços para integrar informações em todo o país. Entretanto, esse tema será "
                "aprofundado na próxima aula."
            )
        )
        + row(
            p(
                "Por fim, é importante compreender que, embora a interoperabilidade seja o caminho ideal, nem sempre ela "
                "está plenamente implementada em todos os contextos. Nesses casos, para garantir análises consistentes "
                "e apoiar decisões, pode ser necessário recorrer a técnicas como o linkage probabilístico de dados, "
                "assunto que será explorado no próximo tópico."
            )
        )
    )


def content_topico6() -> str:
    qs = "".join(f'<p class="mb-2">...{q}</p>' for q in LINKAGE_QUESTIONS)
    fc1 = "<p><strong>Permissivo:</strong> Aceita combinações com <strong>menor grau de semelhança</strong> entre os registros.</p><p><strong>Vantagem:</strong> encontra mais pares verdadeiros.</p><p class=\"mb-0\"><strong>Desvantagem:</strong> inclui também mais falsos-positivos (liga registros que não pertencem à mesma pessoa).</p>"
    fc2 = "<p><strong>Restritivo:</strong> Exige <strong>alta semelhança</strong> entre os registros para considerar um par verdadeiro.</p><p><strong>Vantagem:</strong> reduz falsos-positivos.</p><p class=\"mb-0\"><strong>Desvantagem:</strong> pode perder pares verdadeiros (falsos-negativos).</p>"
    flip_row = (
        '<div class="row justify-content-center"><div class="col-12 col-md-10 col-lg-8">'
        '<div class="row g-4 mb-5">'
        + flipcard("m4a1fc1", "Permissivo", fc1)
        + flipcard("m4a1fc2", "Restritivo", fc2)
        + "</div></div></div>"
    )
    return (
        heading(6, TOPICS[5][1])
        + row(p("No Brasil nós temos diversos sistemas que tratam de assuntos isolados,"))
        + subheading("mas imagina se fosse possível saber se...", "h4")
        + row(qs)
        + row(
            '<p class="h5 fw-bold mb-0">Pois é, com o relacionamento de dados é possível vincular informações de sistemas diferentes!</p>'
        )
        + row(
            p(
                "Pareamento de dados (também conhecido como linkage, “vinculação” ou “relacionamento de dados”) é um "
                "processo técnico e metodológico que visa identificar e conectar registros que se referem à mesma "
                "entidade (como uma pessoa, um evento ou um estabelecimento) em diferentes fontes de dados."
            )
        )
        + row(
            p(
                "O objetivo é transformar bases de dados isoladas e desconexas em uma visão integrada e mais rica da "
                "realidade. Na Saúde Pública, isso permite construir trajetórias de cuidado, monitorar desfechos, "
                "avaliar políticas e fortalecer a Vigilância Epidemiológica, criando informações que não estavam "
                "visíveis quando os sistemas eram analisados separadamente. O método utilizado deve levar em conta "
                "trazer o máximo de pares reais e minimizar ou até mesmo zerar os falsos-positivos*."
            )
        )
        + box(
            "Importante",
            "Importante!",
            "<strong>*Falsos-positivos:</strong> pares encontrados, mas cuja informação entre ambos é divergente.",
        )
        + row(
            '<p class="h5 fw-bold mb-0">O técnico deve sempre levar em consideração os objetivos do '
            "pareamento para identificar se falsos-positivos poderão ser aceitos e até que ponto serão tolerados.</p>"
        )
        + box(
            "Importante",
            "Importante!",
            'O linkage pode ser mais "permissivo" ou mais "restritivo".',
        )
        + flip_row
        + subheading("Exemplos práticos")
        + exercise_block(
            1,
            "Objetivo: retirar da fila pacientes que já faleceram. Fila de Espera de Cirurgia × Sistema de Mortalidade. "
            "Devemos ser mais restritivos ou permissivos nessa situação?",
            [
                (
                    "Permissivo",
                    "Incorreta. Nesse caso, um erro é grave (não podemos excluir alguém vivo), então o linkage precisa ser bem rigoroso.",
                    False,
                ),
                (
                    "Restritivo",
                    "Correta. Nesse caso, um erro é grave (não podemos excluir alguém vivo), então o linkage precisa ser bem rigoroso.",
                    True,
                ),
            ],
        )
        + exercise_block(
            2,
            "Objetivo: identificar possíveis mães e recém-nascidos. AIH (Internações Hospitalares) × SINASC (Nascidos Vivos). "
            "Devemos ser mais restritivos ou permissivos nessa situação?",
            [
                (
                    "Restritivo",
                    "Incorreta. Aqui, errar não é tão crítico, e o foco é ampliar a busca ativa, então o linkage pode ser mais flexível.",
                    False,
                ),
                (
                    "Permissivo",
                    "Correta. Aqui, errar não é tão crítico, e o foco é ampliar a busca ativa, então o linkage pode ser mais flexível.",
                    True,
                ),
            ],
        )
    )


def content_topico7() -> str:
    det_ex = "".join(
        par_exercise(i + 1, "determinístico", *row_data[:4], row_data[4])
        for i, row_data in enumerate(PAR_EXERCISES)
    )
    prob_ex = "".join(
        par_exercise(i + 1, "probabilístico", *row_data[:4], row_data[5])
        for i, row_data in enumerate(PAR_EXERCISES)
    )
    table = (
        '<div class="row justify-content-center"><div class="col-12 col-md-10 col-lg-8 mb-5">'
        '<p class="mb-2"><strong>Quadro 1 – Relação entre o pareamento determinístico e probabilístico.</strong></p>'
        '<div class="table-responsive"><table class="table table-sm table-bordered align-middle mb-0">'
        "<thead><tr class=\"bg-primary text-white\">"
        "<th scope=\"col\">Característica</th>"
        "<th scope=\"col\">Pareamento determinístico</th>"
        "<th scope=\"col\">Pareamento probabilístico</th></tr></thead><tbody>"
        "<tr><td>Lógica</td><td>Conexão exata e rígida entre identificadores únicos.</td>"
        "<td>Cálculo da <strong>probabilidade</strong> de dois registros serem o mesmo.</td></tr>"
        "<tr><td>Chaves</td><td>Utiliza identificadores únicos e perfeitos (ex.: CPF, CNS, CNES).</td>"
        "<td>Utiliza um conjunto de <strong>variáveis comuns parcialmente concordantes</strong> "
        "(nome, data de nascimento, nome da mãe, endereço).</td></tr>"
        "<tr><td>Resultado</td><td>Binário: os registros <strong>são</strong> ou <strong>não são</strong> o mesmo.</td>"
        "<td>Probabilístico: os registros têm uma <strong>pontuação</strong> que indica a chance de serem o mesmo.</td></tr>"
        "<tr><td>Melhor aplicação</td><td>Quando há identificadores únicos de alta qualidade e cobertura.</td>"
        "<td><strong>Contexto real do SUS:</strong> para integrar bases históricas, de vigilância ou onde "
        "identificadores únicos são ausentes ou falhos.</td></tr>"
        "<tr><td>Falsos positivos</td><td>Praticamente zero, se o identificador for confiável.</td>"
        "<td>Controlados por meio do <strong>estabelecimento de um limiar (cut-off)</strong> estatístico.</td></tr>"
        "</tbody></table></div>"
        '<p class="figure-caption fonte small mt-2 mb-0">Fonte: Coeli; Pinheiro; Camargo (2015).</p></div></div>'
    )
    return (
        heading(7, TOPICS[6][1])
        + row(
            p(
                "A escolha do método depende da qualidade dos dados e do contexto. A tabela a seguir compara as duas "
                "abordagens principais."
            )
        )
        + subheading("Determinístico", "h5")
        + row(
            p(
                "O linkage determinístico utiliza regras rígidas para identificar registros iguais em diferentes bases. "
                "Esse método baseia-se em comparações exatas de valores, como nome completo, data de nascimento ou CPF. "
                "Por exemplo, dois registros são considerados pertencentes à mesma pessoa apenas se todos os campos "
                "correspondentes coincidirem perfeitamente. É simples e rápido, oferecendo alta precisão, mas pode falhar "
                "quando há variações de escrita, erros de digitação ou dados faltantes (Coeli; Pinheiro; Camargo, 2015)."
            )
        )
        + subheading("Atividade prática", "p")
        + det_ex
        + subheading("Probabilístico", "h5")
        + row(
            p(
                "O linkage probabilístico utiliza modelos estatísticos para avaliar a probabilidade de que dois registros "
                "correspondam à mesma entidade. Cada campo de comparação (por exemplo, nome, nome da mãe, data de "
                "nascimento, sexo) recebe um peso com base em sua capacidade de identificar corretamente uma pessoa. A "
                "combinação desses pesos gera uma pontuação de probabilidade; se acima de um limiar, os registros são "
                "vinculados; se abaixo, são separados; se intermediária, são analisados manualmente (Coeli; Pinheiro; "
                "Camargo, 2015)."
            )
        )
        + subheading("Atividade prática", "p")
        + prob_ex
        + table
        + box(
            "Importante",
            "Importante!",
            "No cenário do SUS, o pareamento probabilístico é frequentemente indispensável. Muitos sistemas de "
            "informação foram implementados em diferentes épocas, com padrões variados de coleta, o que dificulta a "
            "padronização de um identificador único, válido e consistente em todas as bases. Contudo, visando superar "
            "essa fragmentação, o Governo Federal estabeleceu uma diretriz importante para o futuro. A Lei nº 14.534, "
            "de 10 de janeiro de 2023, determina em seu Art. 1º a utilização do Cadastro de Pessoas Físicas (CPF) como "
            "identificador único do cidadão em todos os sistemas e cadastros do SUS, com o objetivo de substituir "
            "cadastros paralelos e viabilizar uma integração mais ágil e segura (Brasil, 2023).",
        )
    )


def content_topico8() -> str:
    cards = [
        ("m4a1app1", "Continuidade do cuidado", "A integração de prontuários permite que qualquer profissional autorizado visualize o histórico completo, reduzindo erros, evitando repetição de exames e garantindo cuidado seguro."),
        ("m4a1app2", "Vigilância em saúde oportuna", "A correlação automatizada de dados de sintomas, diagnósticos e laboratórios em tempo real permite identificar rapidamente anomalias e tendências, viabilizando respostas mais rápidas a emergências."),
        ("m4a1app3", "Gestão eficiente e planejamento", "A análise integrada de dados de mortalidade, morbidade e custos gera indicadores precisos para a distribuição equitativa de recursos, avaliação de programas e formulação de políticas baseadas em evidências."),
        ("m4a1app4", "Pesquisa e inovação", "Bases de dados nacionais integradas fornecem um campo rico para pesquisas epidemiológicas, avaliação de tratamentos e estudos sobre os determinantes sociais da saúde."),
        ("m4a1app5", "Transparência e controle social", "Plataformas como o Conecte SUS e painéis de dados abertos permitem que a sociedade monitore indicadores e resultados de políticas, fortalecendo a prestação de contas."),
    ]
    flip_html = (
        '<div class="row justify-content-center"><div class="col-12 col-md-10 col-lg-8">'
        '<div class="row g-4 mb-5">'
        + "".join(flipcard(cid, title, f"<p class=\"mb-0\">{body}</p>") for cid, title, body in cards)
        + "</div></div></div>"
    )
    return (
        heading(8, TOPICS[7][1])
        + row(
            p(
                "A interoperabilidade e o linkage de dados são pilares indispensáveis para uma gestão em saúde moderna. "
                "Eles transformam informações fragmentadas em conhecimento estratégico, impactando desde o cuidado "
                "individual até políticas públicas."
            )
        )
        + flip_html
        + row(
            p(
                "Vale ressaltar que o tratamento de dados pessoais sensíveis da saúde deve obedecer estritamente à Lei "
                "Geral de Proteção de Dados (LGPD - Lei nº 13.709/2018). Práticas como minimização de dados (coletar "
                "apenas o necessário), anonimização, segurança robusta dos ambientes de análise e transparência sobre as "
                "finalidades do uso são mandatórias. O cidadão mantém seus direitos sobre seus dados, e a interoperabilidade "
                "deve ser um instrumento para o bem público, jamais uma brecha para violação de privacidade (Brasil, 2018)."
            )
        )
        + box(
            "Exemplo",
            "Exemplo!",
            "Um exemplo real da aplicação do linkage probabilístico na Saúde Pública brasileira é a produção do "
            "Boletim Epidemiológico de Coinfecção Tuberculose-HIV (Brasil, 2022). Esse documento estratégico para os "
            "programas nacionais de controle da tuberculose e da Aids só é viável a partir da integração de múltiplas "
            "bases de dados, como o Sinan (casos de tuberculose e HIV/aids), o SIM (óbitos) e os sistemas Siscel/Siclom "
            "(acompanhamento de HIV). O linkage probabilístico identifica quais registros se referem à mesma pessoa nessas "
            "bases distintas. Dessa forma, é possível qualificar as informações como proporção de pessoas com tuberculose "
            "que vivem com HIV, uso da terapia antirretroviral (Tarv), realização de exame de CD4 e desfechos, como o óbito. "
            'Link: <a href="https://www.gov.br/aids/pt-br/central-de-conteudo/boletins-epidemiologicos/2022/coinfeccao-tb-hiv/boletim_coinfeccao_tb_hiv_2022.pdf" '
            'target="_blank" rel="noopener noreferrer">Boletim de Coinfecção TB-HIV 2022</a>.',
        )
        + box(
            "Saiba Mais",
            "Saiba Mais!",
            (
                "<p>Outras referências interessantes para aprofundar o conhecimento sobre relacionamento de dados:</p>"
                '<p class="mb-3">GARCIA, K. K. S.; MIRANDA, C. B.; SOUSA, F. N. F. Procedimentos para vinculação de dados da saúde. '
                '<a href="http://scielo.iec.gov.br/pdf/ess/v31n3/2237-9622-ess-31-03-e20211272.pdf" target="_blank" rel="noopener noreferrer">Epidemiologia e Serviços de Saúde</a>, 2022.</p>'
                '<p class="mb-3">COELI, C. M.; PINHEIRO, R. S.; CAMARGO JR., K. R. '
                '<a href="https://www.scielo.br/j/ress/a/zH4GSZzP9DNZRxwGz3wpMTL/?format=pdf&lang=pt" target="_blank" rel="noopener noreferrer">Epidemiologia e Serviços de Saúde</a>, 2015.</p>'
                '<p class="mb-0">ROCHA, M. S. et al. '
                '<a href="https://www.scielo.br/j/csp/a/9phcLypWdsdk9WqPj7w4n8P/" target="_blank" rel="noopener noreferrer">Cadernos de Saúde Pública</a>, 2019.</p>'
            ),
            raw=True,
        )
        + box(
            "Saiba Mais",
            "Saiba Mais!",
            (
                "<p>Para solicitar ou executar o relacionamento de dados dos sistemas de informação sob gestão do "
                "Departamento de Análise Epidemiológica e Vigilância de Doenças não Transmissíveis (DAENT), seja para fins "
                "de pesquisa científica ou para uso em vigilância em saúde nos serviços, é necessário seguir um procedimento "
                "oficial específico.</p>"
                f'<p class="mb-0">Download: <a class="no-after" href="{ASSETS}media/modulo4/documents/nota-informativa-5-2025-daent-svsa-ms.pdf" '
                'target="_blank" rel="noopener noreferrer">Nota Informativa nº 5/2025 – Procedimento para solicitação de dados (DAENT)</a>.</p>'
            ),
            raw=True,
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
    return created


def update_index() -> None:
    index_path = ROOT / "index.html"
    text = index_path.read_text(encoding="utf-8")
    old_footer = (
        '<span class="fio-button fio-button-primary disabled w-100 d-block text-center" '
        'aria-disabled="true">Em breve</span>'
    )
    new_footer = (
        '<a href="modulo4/aula1/topico1.html" class="fio-button fio-button-primary">Iniciar Módulo 4</a>'
    )
    if old_footer in text:
        text = text.replace(old_footer, new_footer, 1)
    text = text.replace(
        "<li class=\"list-group-item\">Aula 4.1: Interoperabilidade na Saúde</li>",
        '<li class="list-group-item"><a href="modulo4/aula1/topico1.html">Aula 4.1: Interoperabilidade na Saúde</a></li>',
        1,
    )
    text = text.replace(
        "<li class=\"list-group-item\">Aula 4.2: Integração de Dados em Saúde</li>",
        '<li class="list-group-item">Aula 4.2: Integração de Dados em Saúde</li>',
        1,
    )
    index_path.write_text(text, encoding="utf-8")
    print(f"Atualizado: {index_path.relative_to(ROOT)}")


MOD3_ITEM_RE = re.compile(
    r'(<li class="dropdown-menu__item">\s*'
    r'(?:<!--[\s\S]*?-->\s*)?'
    r'<a class="dropdown-menu__item-link"[^>]*href="((?:\.\./)+)modulo3/aula1/topico1\.html"[^>]*>'
    r"<strong>Módulo 3</strong><br\s*/>\s*[^<]+</a>\s*"
    r"</li>\s*)",
    re.IGNORECASE,
)


def update_sidebars() -> int:
    count = 0
    for mod in ("modulo1", "modulo2", "modulo3"):
        for html in (ROOT / mod).rglob("*.html"):
            text = html.read_text(encoding="utf-8")
            if "modulo4/aula1/topico1.html" in text:
                continue
            m = MOD3_ITEM_RE.search(text)
            if not m:
                continue
            prefix_match = re.search(
                r'href="((?:\.\./)+)modulo3/aula1/topico1\.html"', m.group(0)
            )
            prefix = prefix_match.group(1) if prefix_match else "../../"
            text = MOD3_ITEM_RE.sub(r"\1" + mod4_dropdown_item(prefix), text, count=1)
            html.write_text(text, encoding="utf-8")
            count += 1
    print(f"Sidebars atualizados: {count} arquivos")
    return count


def main() -> None:
    print("=== Gerando modulo4/aula1 ===")
    files = generate_all()
    print("\n=== Atualizando index.html ===")
    update_index()
    print("\n=== Atualizando sidebars (mod1–3) ===")
    update_sidebars()
    print(f"\nTotal: {len(files)} arquivos HTML gerados.")


if __name__ == "__main__":
    main()

