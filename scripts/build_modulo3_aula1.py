#!/usr/bin/env python3
"""Gera HTML da Aula 3.1 (Abordagens teóricas da Geografia da Saúde) a partir do PDF validado."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "modulo3" / "aula1"
MEDIA = "../../media/modulo3/aula1/"
ASSETS = "../../"

COURSE_TITLE = "Análise e Interpretação de Dados em Saúde"
MODULE_NUM = 3
MODULE_TITLE = "Análise Espacial"
AULA_LABEL = "Aula 1"
AULA_TITLE = "Abordagens teóricas da Geografia da Saúde"

TOPICS = [
    "Sobre esta aula",
    "Introdução",
    "Mapeamento em estudos de saúde",
    "Geografia da Saúde",
    "Mas afinal de que saúde estamos falando?",
    "Unidade Geográfica de Análise",
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

MIASMA_POPOVER = (
    "A teoria miasmática foi uma hipótese médica, predominante até o final do século XIX, "
    "que defendia que doenças contagiosas (como cólera, peste negra e malária) eram causadas "
    'por "miasmas" — odores fétidos e vapores tóxicos exalados por matéria orgânica em '
    "decomposição, solos e águas contaminadas."
)

REFERENCES = [
    'BRADSHAW, N. A. Florence Nightingale (1820-1910): An Unexpected Master of Data. '
    '<em>Patterns (N Y)</em>, v. 1, n. 2, p. 100036, 2020. DOI: '
    '<a href="https://doi.org/10.1016/j.patter.2020.100036" target="_blank" rel="noopener noreferrer">'
    "10.1016/j.patter.2020.100036</a>.",
    "BRASIL. Conselho Nacional de Secretários de Saúde. Coleção para entender a Gestão do "
    "SUS. Brasília: CONASS, ed. 20, 2011.",
    "BRASIL. Lei nº 8.080, de 19 de setembro de 1990. Dispõe sobre as condições para a "
    "promoção, proteção e recuperação da saúde, a organização e o funcionamento dos serviços "
    "correspondentes e dá outras providências. Diário Oficial da União, Brasília, 20 set. 1990.",
    "BRASIL. Ministério da Saúde. Política Nacional de Promoção da Saúde. Brasília: "
    "Ministério da Saúde, 2014.",
    "BUSS, P. M.; PELLEGRINI FILHO, A. A saúde e seus determinantes sociais. "
    "<em>Physis: Revista de Saúde Coletiva</em>, v. 17, n. 1, p. 77‑93, 2007.",
    'COMISSÃO NACIONAL SOBRE DETERMINANTES SOCIAIS DA SAÚDE (CNDSS). As causas '
    "sociais das iniquidades em saúde no Brasil: relatório final. Rio de Janeiro: Fundação Oswaldo "
    'Cruz, 2008. Disponível em: <a href="https://bvsms.saude.gov.br/bvs/publicacoes/causas_sociais_'
    'iniquidades.pdf" target="_blank" rel="noopener noreferrer">https://bvsms.saude.gov.br/bvs/publicacoes/causas_sociais_'
    "iniquidades.pdf</a>. Acesso em: 19 fev. 2026.",
    "EYLER, J. M. William Farr on the Cholera: The Sanitarian's Disease Theory and the "
    "Statistician's Method. <em>Journal of the History of Medicine and Allied Sciences</em>, "
    "v. 28, n. 2, p. 79–100, 1973. DOI: "
    '<a href="https://doi.org/10.1093/jhmas/XXVIII.2.79" target="_blank" rel="noopener noreferrer">'
    "10.1093/jhmas/XXVIII.2.79</a>.",
    "GUIMARÃES, Raul Borges. Saúde: fundamentos de geografia humana. São Paulo: Editora "
    "Unesp Digital, 2015. E-book. Disponível em: SciELO Books. Acesso em: 23 fev. 2026.",
    "HIPÓCRATES. Ares, águas e lugares. Tradução de José Cavalcante de Souza. "
    "São Paulo: Martins Fontes, 2005.",
    "JULIA, C.; VALLERON, A. J. Louis-Rene Villerme (1782‑1863), a pioneer in social "
    "epidemiology: re‑analysis of his data on comparative mortality in Paris in the early 19th "
    "century. <em>Journal of Epidemiology and Community Health</em>, v. 65, n. 8, p. 666‑670, 2011. "
    "DOI: "
    '<a href="https://doi.org/10.1136/jech.2009.087957" target="_blank" rel="noopener noreferrer">'
    "10.1136/jech.2009.087957</a>.",
    "KALUZNY, S. P. et al. S+SpatialStats: user's manual for Windows and Unix. "
    "Seattle: Springer, 1997.",
    "MAGALHÃES, M. A. F. M. A tuberculose no espaço urbano: um estudo ecológico utilizando "
    "análise espacial no município do Rio de Janeiro nos anos 2005 a 2008. Rio de Janeiro: "
    "UFRJ/IESC, 2014.",
    "MEADE, Melinda; EMCH, Michael. Medical Geography. 3. ed. New York: Guilford Press, 2010.",
    "MENDES, Eugênio Vilaça (org.). Distrito Sanitário: o processo social de mudança das prticas "
    "sanitárias do Sistema Único de Saúde. 1993.",
    "MIRANDA, A. C.; BARCELLOS, C.; MOREIRA, J. C.; MONKEN, M. (org.). Território, Ambiente "
    "e Saúde. Rio de Janeiro: Editora Fiocruz, 2008.",
    "MONKEN, Maurício; BARCELLOS, Christovam. Vigilância em saúde e território utilizado: "
    "possibilidades teóricas e metodológicas. <em>Cadernos de Saúde Pública</em>, v. 21, n. 3, "
    "p. 898‑906, 2005.",
    "MOREIRA, Ruy. O que é geografia. 14. ed. São Paulo: Brasiliense, 2007.",
    "NAJAR, Alberto Lopes (org.). Saúde e espaço: estudos metodológicos e técnicas de análise. "
    "Rio de Janeiro: Editora Fiocruz, 1998.",
    "OPENSHAW, Stan. The Modifiable Areal Unit Problem (MAUP). In: Concepts and Techniques "
    "in Modern Geography, n. 38. Norwich: Geo Books, 1984.",
    "ORGANIZAÇÃO DAS NAÇÕES UNIDAS. Relatório sobre o Estado da Segurança Alimentar "
    "e Nutrição no Mundo. Roma: FAO/OMS, 2024. Disponível em: "
    '<a href="https://www.paho.org" target="_blank" rel="noopener noreferrer">www.paho.org</a>. '
    "Acesso em: 20 fev. 2026.",
    "Organização Mundial da Saúde (OMS). Social Determinants of Health. Genebra: OMS, 2008.",
    "ORGANIZAÇÃO MUNDIAL DA SAÚDE. Constitution of the World Health Organization. "
    "Genebra: OMS, 1946.",
    "PAINEL INTERGOVERNAMENTAL SOBRE MUDANÇAS CLIMÁTICAS. Mudanças Climáticas "
    "2023: Relatório de Síntese. Genebra: IPCC, 2023. Disponível em: "
    '<a href="https://www.ipcc.ch" target="_blank" rel="noopener noreferrer">https://www.ipcc.ch</a>. '
    "Acesso em: 20 fev. 2026.",
    "PESSOA, S. B. Ensaios Médico‑Sociais. São Paulo: CEBES; Hucitec, 1978.",
    "PINA, M. F. R. P. Potencialidades dos Sistemas de Informações Geográficas na área da saúde. "
    "In: NAJAR, A. L.; MARQUES, E. C. (org.). Saúde e espaço: estudos metodológicos e técnicas "
    "de análise. Rio de Janeiro: Fiocruz, 1998.",
    'PORTO, B.; GURGEL, H.; CATÃO, R. As dimensões do ensino de Geografia da Saúde no '
    "Brasil. <em>Estrabão</em>, v. 3, n. 1, p. 16–28, 2022. DOI: "
    '<a href="https://doi.org/10.53455/re.v3i.27" target="_blank" rel="noopener noreferrer">'
    "https://doi.org/10.53455/re.v3i.27</a>.",
    "SANTOS, Milton. A natureza do espaço: técnica e tempo, razão e emoção. 4. ed. São Paulo: "
    "EDUSP, 2006.",
    "SILVEIRA, Iara. Geografia da saúde: uma revisão integrativa da produção científica "
    "contemporânea. <em>International Seven Journal of Multidisciplinary</em>, v. 3, n. 6, "
    "p. 1649‑1664, 2024. DOI: 10.56238/isevmjv3n6‑014.",
    "SNOW, John. Sobre o modo de transmissão da cólera. 2. ed. Londres: John Churchill, 1855.",
    "TROSTLE, J. Early work in anthropology and epidemiology: from social medicine to the "
    "germ theory, 1840–1920. In: JANES, R. C.; STALL, R.; GIFFORD, S. M. D. (ed.). Anthropology "
    "and Epidemiology. Boston: Reidel Publishing Company, 1986. p. 35–57.",
    "TUAN, Yi‑Fu. Espaço e lugar: a perspectiva da experiência. São Paulo: Difel, 1983.",
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


def box(kind: str, label: str, body: str, *, raw: bool = False) -> str:
    body_html = body if raw else f'<p class="mb-0">{body}</p>'
    return row(
        f'<div class="box" data-box="{kind}"><div class="card"><div class="card-header">'
        f'<span class="icone material-symbols-rounded" aria-hidden="true"></span>'
        f'<span class="label">{label}</span></div><div class="card-body">'
        f"{body_html}</div></div></div>"
    )


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


def figure_row(figures: list[tuple[str, str, str]]) -> str:
    """Lista de (src, alt, fonte)."""
    return row(_figures_row_inner(figures))


def _figures_row_inner(figures: list[tuple[str, str, str]]) -> str:
    cols = ""
    for src, alt, fonte in figures:
        cols += (
            f'<div class="col-12 col-md-6 mb-4">'
            f'<figure class="lightbox aos-init" data-aos="fade-up" data-aos-easing="ease-out" data-aos-duration="600">'
            f'<img class="img-fluid mx-auto d-block mb-3 rounded border" src="{MEDIA}{src}" alt="{alt}" loading="lazy" />'
            f"</figure>"
            f'<p class="figure-caption fonte small mb-0">{fonte}</p></div>'
        )
    return f'<div class="row">{cols}</div>'


def accordion_text_figure(text_html: str, src: str, alt: str, fonte: str, *, row_class: str = "") -> str:
    """Texto e figura lado a lado dentro de accordion-body."""
    rc = f"row align-items-start g-4 {row_class}".strip()
    return (
        f'<div class="{rc}">'
        f'<div class="col-12 col-md-7">{text_html}</div>'
        f'<div class="col-12 col-md-5">'
        f'<figure class="mb-0"><img class="img-fluid mx-auto d-block rounded border" '
        f'src="{MEDIA}{src}" alt="{alt}" loading="lazy" /></figure>'
        f'<p class="figure-caption fonte small mb-0 mt-2">{fonte}</p>'
        "</div></div>"
    )


def accordion_figure_text(src: str, alt: str, fonte: str, text_html: str, *, row_class: str = "") -> str:
    """Figura e texto lado a lado (figura à esquerda) dentro de accordion-body."""
    rc = f"row align-items-start g-4 {row_class}".strip()
    return (
        f'<div class="{rc}">'
        f'<div class="col-12 col-md-5">'
        f'<figure class="mb-0"><img class="img-fluid mx-auto d-block rounded border" '
        f'src="{MEDIA}{src}" alt="{alt}" loading="lazy" /></figure>'
        f'<p class="figure-caption fonte small mb-0 mt-2">{fonte}</p>'
        f"</div>"
        f'<div class="col-12 col-md-7">{text_html}</div>'
        "</div>"
    )


def voce_sabia_toggle(collapse_id: str, body_html: str) -> str:
    """Você sabia? expansível: conteúdo só aparece após clicar no botão."""
    return row(
        f'<div class="saiba-mais pb-5">'
        f'<div class="row aos-init" data-aos="fade-left" data-aos-easing="ease-out" data-aos-duration="600">'
        f'<div class="col-12 d-flex justify-content-center">'
        f'<button class="saiba-mais fio-button button-md fio-button-secondary collapsed" type="button" '
        f'data-bs-toggle="collapse" data-bs-target="#{collapse_id}" aria-expanded="false" '
        f'aria-controls="{collapse_id}">'
        f'<span class="icone material-symbols-rounded" aria-hidden="true"></span> Você sabia?</button>'
        f"</div>"
        f'<div class="col-12">'
        f'<div class="mt-3 collapse" id="{collapse_id}">{body_html}</div>'
        f"</div></div></div>"
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


def accordion(accordion_id: str, items: list[tuple[str, str]], *, first_open: bool = False) -> str:
    parts = [f'<div class="accordion accordion-flush" id="{accordion_id}">']
    for i, (title, body) in enumerate(items):
        hid = f"{accordion_id}-{i}-h"
        cid = f"{accordion_id}-{i}-c"
        collapsed = "" if first_open and i == 0 else "collapsed"
        expanded = "true" if first_open and i == 0 else "false"
        show = " show" if first_open and i == 0 else ""
        parts.append(
            f'<div class="accordion-item"><h5 class="accordion-header" id="{hid}">'
            f'<button class="accordion-button {collapsed}" type="button" data-bs-toggle="collapse" '
            f'data-bs-target="#{cid}" aria-expanded="{expanded}" aria-controls="{cid}">{title}</button></h5>'
            f'<div id="{cid}" class="accordion-collapse collapse{show}" aria-labelledby="{hid}" '
            f'data-bs-parent="#{accordion_id}"><div class="accordion-body">{body}</div></div></div>'
        )
    parts.append("</div>")
    return row("".join(parts))


def popover_link(text: str, title: str, content: str, *, placement: str = "top") -> str:
    esc = content.replace('"', "&quot;")
    return (
        f'<a tabindex="0" role="button" data-bs-toggle="popover" data-bs-trigger="focus" '
        f'data-bs-placement="{placement}" data-bs-html="true" data-bs-title="{title}" '
        f'data-bs-content="<p>{esc}</p>"><strong>{text}</strong></a>'
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
                'Seja bem-vindo e bem-vinda à aula <strong>"Abordagens teóricas da Geografia da Saúde"</strong>.'
            )
            + p("A seguir, veja algumas informações importantes!")
        )
        + subheading("Objetivos de aprendizagem")
        + row(
            p("Ao final dessa aula, você será capaz de:")
            + ul(
                [
                    "Conhecer os Conceitos da Geografia da Saúde;",
                    "Compreender a importância do Território na Saúde;",
                    "Identificar diferentes unidades geográficas de análise.",
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
                "Mestre em Ciências - Métodos quantitativos em Epidemiologia &amp; Engenheira Cartógrafa."
            )
        )
    )


def content_introducao() -> str:
    return (
        heading(2, "Introdução")
        + row(
            p(
                "A ideia de que o território é um componente essencial quando observamos a saúde "
                "das populações não é nova. Hipócrates (460 a.C.- 377 a.C.), médico grego, considerado "
                "Pai da Medicina na sua obra “Sobre Ares, Águas e Lugares”, enfatizou a importância do modo "
                "de vida dos indivíduos, analisando a influência dos ventos, água, solo e localização das "
                "cidades em relação ao Sol, na ocorrência de doenças (Hipócrates, 2005). Além disso, "
                "vale enfatizar que determinadas doenças ocorrem preferencialmente em locais específicos "
                "e considerar o lugar como fator determinante na ocorrência de problemas de saúde "
                "(Pessoa, 1978; Trostle, 1986)."
            )
        )
        + figure_plain("figura-intro-cidade.jpeg", "Pessoas caminhando em via urbana")
        + row(
            p(
                "Séculos depois, entre o XVII e XVIII, o conceito de saúde pública surgiu na Europa em meio "
                "ao crescimento urbano e às epidemias. A necessidade de organizar os espaços e enfrentar "
                "altas taxas de mortalidade levou ao reconhecimento da saúde como um direito coletivo, "
                "sempre associado a ações territorializadas e ao uso do espaço como elemento essencial no "
                "planejamento sanitário (Najar &amp; Marques, 1998)."
            )
        )
        + voce_sabia_toggle(
            "m3a1-voce-sabia-hipocrates",
            "<p><strong>Hipócrates e a relação entre ambiente e saúde</strong></p>"
            "<p>Em sua obra “Sobre Ares, Águas e Lugares”, escreveu como o ambiente influencia "
            "a ocorrência das doenças. Lançou como principais ideias:</p>"
            "<ul>"
            "<li><strong>Influência do meio ambiente:</strong> defendia que o clima, os ventos, a qualidade "
            "da água, o tipo de solo e a localização das cidades em relação ao sol "
            "afetavam a saúde das populações.</li>"
            "<li><strong>Modo de vida:</strong> considerava hábitos, alimentação e condições sociais como "
            "elementos que interagiam com o espaço para determinar a saúde.</li>"
            "<li><strong>Distribuição das doenças:</strong> observou que certas doenças eram mais "
            "comuns em regiões específicas, sugerindo uma relação entre geografia "
            "e padrões epidemiológicos.</li>"
            "</ul>"
            + _figures_row_inner(
                [
                    (
                        "figura-hipocrates-busto.jpeg",
                        "Busto de Hipócrates",
                        'Fonte: Paulus Pontius / After Peter Paul Rubens - Courtesy of the National Library of Medicine [1]., '
                        'Public Domain, <a href="https://commons.wikimedia.org/w/index.php?curid=1332072" '
                        'target="_blank" rel="noopener noreferrer">Wikimedia Commons</a>',
                    ),
                    (
                        "figura-hipocrates-livro.jpeg",
                        "Página do livro de Hipócrates",
                        'Fonte: <a href="https://wellcomeimages.org/indexplus/obf_images/83/0e/bfaf5986cd33cea0f9d50ab1bddb.jpg" '
                        'target="_blank" rel="noopener noreferrer">Wellcome Images</a>, CC BY 4.0, '
                        '<a href="https://commons.wikimedia.org/w/index.php?curid=36099254" '
                        'target="_blank" rel="noopener noreferrer">Wikimedia Commons</a>',
                    ),
                ]
            ),
        )
    )


def content_mapeamento() -> str:
    farr_fonte = (
        "Fonte: Unknown author - "
        '<a href="http://johnsnow.matrix.msu.edu/book_images7.php" target="_blank" rel="noopener noreferrer">'
        "johnsnow.matrix.msu.edu</a>, Public Domain, "
        '<a href="https://commons.wikimedia.org/w/index.php?curid=20378013" target="_blank" rel="noopener noreferrer">'
        "Wikimedia Commons</a>"
    )
    miasm_link = popover_link("teorias miasmáticas", "Teoria miasmática", MIASMA_POPOVER)
    farr_text = (
        "<p>Os trabalhos de William Farr, nas décadas de 1830 a 1850, foram essenciais para consolidar "
        "essa abordagem. Ao sistematizar registros de mortalidade e analisá-los segundo local, idade "
        "e ocupação, Farr demonstrou que a ocorrência de doenças variava de forma consistente entre "
        "diferentes áreas e grupos populacionais. Embora ainda influenciado por "
        f"{miasm_link}, seu uso de dados espaciais permitiu identificar desigualdades regionais de "
        "saúde e estabelecer as bases da vigilância epidemiológica moderna. Dessa forma, o "
        "mapeamento passou a ser entendido como um instrumento estratégico para a administração "
        "sanitária e a formulação de políticas públicas (Eyler, 1973).</p>"
    )
    farr_body = accordion_text_figure(farr_text, "figura-farr.png", "Retrato de William Farr", farr_fonte)
    snow_fonte = (
        "Fonte: Originally from en.wikipedia; description page is/was here., Domínio público, "
        '<a href="https://commons.wikimedia.org/w/index.php?curid=403227" target="_blank" rel="noopener noreferrer">'
        "Wikimedia Commons</a>"
    )
    snow_mapa_fonte = (
        'Fonte: <a href="https://picryl.com/media/snow-cholera-map-5f4358" target="_blank" rel="noopener noreferrer">'
        "picryl.com</a>"
    )
    snow_text_top = (
        "<p>O marco mais emblemático da epidemiologia espacial é o estudo de John Snow sobre o surto "
        "de cólera de 1854 em Londres. Ao mapear os casos da doença e relacioná-los à localização "
        "das bombas de água, Snow demonstrou empiricamente a associação entre a contaminação "
        "hídrica e a disseminação da cólera. Esse trabalho não apenas contestou a teoria miasmática "
        "dominante, mas também evidenciou o poder do mapeamento como ferramenta analítica capaz "
        "de revelar relações causais entre ambiente e doença. O mapa de Broad Street tornou-se um "
        "símbolo da aplicação do raciocínio geográfico na investigação epidemiológica e no controle "
        "de surtos (Snow, 1855).</p>"
        "<p><strong>John Snow (1813-1858) foi um médico britânico e um dos fundadores da epidemiologia moderna</strong></p>"
    )
    snow_text_map = (
        "<p><strong>Mapa elaborado por John Snow no estudo da epidemia de cólera em Londres em 1854.</strong></p>"
        "<p><strong>Os pontos indicam a localização de pessoas afetadas pela cólera e as cruzetas indicam os poços de "
        "onde as pessoas coletavam água para consumo.</strong></p>"
    )
    snow_body = (
        accordion_text_figure(snow_text_top, "figura-snow-retrato.png", "Retrato de John Snow", snow_fonte)
        + accordion_figure_text(
            "figura-snow-mapa.png",
            "Mapa de cólera de John Snow",
            snow_mapa_fonte,
            snow_text_map,
            row_class="mt-4",
        )
    )
    nightingale_fonte = (
        "Fonte: H. Lenthall, London - Este ficheiro foi extraído de outro ficheiro, Domínio público, "
        '<a href="https://commons.wikimedia.org/w/index.php?curid=9826164" target="_blank" rel="noopener noreferrer">'
        "Wikimedia Commons</a>"
    )
    nightingale_text = (
        "<p>Florence Nightingale ampliou o uso de representações espaciais e gráficas para demonstrar a "
        "influência das condições sanitárias sobre a mortalidade. Por meio de mapas hospitalares e "
        "diagramas de áreas polares, Nightingale evidenciou que a maioria das mortes de soldados "
        "durante a Guerra da Crimeia era causada por doenças evitáveis, e não por ferimentos de guerra. "
        "(Bradshaw, 2020) Ao transformar dados complexos em imagens fáceis de entender, ela ajudou a "
        "popularizar o uso de mapas e visualizações como ferramentas importantes na saúde pública, "
        "capazes de apoiar mudanças e melhorias nas políticas e instituições.</p>"
    )
    nightingale_body = accordion_text_figure(
        nightingale_text,
        "figura-nightingale.jpeg",
        "Florence Nightingale",
        nightingale_fonte,
    )
    villerme_text = (
        "<p>No início do século XIX, os estudos de Louis-René Villermé introduziram uma dimensão social "
        "ao uso do espaço na análise da saúde. Ao correlacionar mortalidade, condições de trabalho e "
        "níveis de pobreza em diferentes áreas de Paris, Villermé demonstrou que a distribuição das "
        "doenças estava profundamente ligada às desigualdades sociais e territoriais. Embora seus "
        "trabalhos antecedam a epidemiologia espacial formal, eles antecipam princípios fundamentais "
        "da saúde coletiva contemporânea, ao integrar dados geográficos, sociais e econômicos na "
        "explicação dos padrões de adoecimento (Julia &amp; Valleron, 2011).</p>"
    )
    villerme_body = accordion_text_figure(
        villerme_text,
        "figura-villerme.png",
        "Louis-René Villermé",
        nightingale_fonte,
    )
    return (
        heading(3, "Mapeamento em estudos de saúde")
        + row(
            p(
                "Desde o início do século XIX, o uso do mapeamento e da análise espacial passou a ocupar "
                "um papel central no desenvolvimento da saúde pública, ao permitir a visualização da distri-"
                "buição geográfica das doenças e sua relação com fatores ambientais e sociais. Em um con-"
                "texto marcado por rápidas transformações urbanas, industrialização e altas taxas de mor-"
                "talidade, mapas e estatísticas tornaram-se ferramentas fundamentais para compreender "
                "padrões de adoecimento que não eram evidentes apenas por meio de observações clínicas "
                "individuais. Essa mudança representou uma transição do entendimento das doenças como "
                "eventos isolados para sua concepção como fenômenos coletivos, socialmente e territorial-"
                "mente determinados."
            )
            + p("Alguns marcos importantes do início desta história:")
        )
        + accordion(
            "m3a1-mapeamento",
            [
                ("William Farr (décadas de 1830 - 1850) Estatísticas de Mortalidade na Inglaterra:", farr_body),
                ("John Snow - mapa dos casos de cólera em Broad Street, Londres:", snow_body),
                ("Florence Nightingale (1857–1858) - Guerra da Crimeia:", nightingale_body),
                (
                    "Louis-René Villermé (início do século XIX) - estudos sobre mortalidade e condições sociais em Paris:",
                    villerme_body,
                ),
            ],
            first_open=True,
        )
        + row(
            p(
                "Essas experiências históricas demonstram que o uso de mapas se tornou fundamental para "
                "a saúde pública porque permite visualizar onde surgem doenças, identificar desigualdades e "
                "entender como fatores ambientais e sociais influenciam a saúde. Esse legado mudou a forma "
                "de estudar e enfrentar problemas de saúde coletiva e, até hoje, continuam essenciais em "
                "atividades como o uso de Sistema de Informações Geogrpaficas (SIG), a vigilância "
                "epidemiológica no território e o planejamento em saúde baseado em informações espaciais."
            )
            + p(
                "É justamente nesse ponto que a Geografia da Saúde se destaca, pois utiliza essas "
                "ferramentas e perspectivas para analisar como o espaço, o território e o lugar influenciam "
                "a distribuição das doenças, o acesso aos serviços e as condições de vida das populações."
            )
        )
    )


def content_geografia() -> str:
    return (
        heading(4, "Geografia da Saúde")
        + row(
            p(
                "A Geografia da Saúde estuda como o lugar onde as pessoas vivem influencia sua "
                "saúde, analisando fatores do território como ambiente, condições sociais, políticas e "
                "economia (Monkey &amp; Barcellos, 2006). Diferente do olhar médico tradicional, que foca no "
                "indivíduo, essa área considera que o espaço e a organização da sociedade também moldam "
                "o processo saúde–doença (Porto et al., 2022)."
            )
        )
        + figure_plain("figura-geografia-saude.jpeg", "Poluição ambiental em corpo d'água")
        + row(
            p(
                "Até meados do século XX, a área era chamada de <strong>Geografia Médica</strong>, focada principalmente nas "
                "doenças infecciosas e parasitárias. Mais tarde, entre as décadas de 1970 e 1980, influenciado "
                "por autores como Milton Santos, consolidou-se o termo <strong>Geografia da Saúde</strong>, ampliando o olhar "
                "para incluir desigualdades sociais, condições econômicas, acesso aos serviços e o papel do "
                "território na produção do bem-estar (Mendes, 1993)."
            )
            + p(
                "Nas últimas décadas, a Geografia da Saúde se fortaleceu tanto teoricamente quanto em suas "
                "aplicações práticas. Esse crescimento está ligado ao desenvolvimento do Sistema Único de "
                "Saúde (SUS), que organiza a saúde a partir de um modelo territorial descentralizado, "
                "hierarquizado e integrado por redes de atenção (Brasil, 1990)."
            )
            + p(
                "Nesta disciplina, utilizaremos os termos <strong>espaço geográfico, lugar e território</strong>. Embora não "
                "seja o objetivo fazermos uma discussão aprofundada sobre as diferenças entre eles, esses "
                "termos aparecerão com frequência, especialmente neste módulo. Por isso, serão apresentados "
                "de forma breve e didática."
            )
        )
        + accordion(
            "m3a1-conceitos-geografia",
            [
                (
                    "Espaço Geográfico",
                    "<p>O <strong>espaço geográfico</strong> é resultado da relação entre sociedade e natureza, o que significa "
                    "que a saúde das pessoas depende também das condições ambientais, sociais e econômicas do "
                    "lugar onde vivem. Segundo Milton Santos (2006), esse espaço é formado por sistemas de "
                    "objetos (como ruas, prédios e serviços) e sistemas de ações (as práticas sociais que acontecem "
                    "nele). Dessa forma, fatores como saneamento, transporte, moradia e serviços de saúde "
                    "influenciam diretamente a qualidade de vida.</p>",
                ),
                (
                    "Lugar",
                    "<p>O conceito de <strong>lugar</strong> mostra a dimensão mais humana da saúde. Lugar é o espaço onde as "
                    "pessoas vivem, criam vínculos e constroem significados, influenciando o bem-estar mental, "
                    "emocional e social. Ambientes marcados por violência e pobreza tendem a gerar medo e "
                    "sofrimento, enquanto comunidades acolhedoras, com áreas de convivência e redes de apoio, "
                    "fortalecem o sentimento de pertencimento e proteção, favorecendo a saúde coletiva (Tuan, 1983).</p>",
                ),
                (
                    "Território",
                    "<p>O <strong>território</strong> se refere às relações de poder e à forma como o espaço é organizado politicamente. "
                    "Na saúde, ele é essencial porque orienta o planejamento das ações públicas (Santos, 2006). A "
                    "Atenção Básica, por exemplo, utiliza territórios específicos para identificar necessidades da "
                    "população, distribuir recursos e garantir acesso aos serviços. Isso permite reconhecer "
                    "desigualdades e direcionar melhor ações de promoção, prevenção e cuidado.</p>",
                ),
            ],
        )
        + row(
            p(
                "Essas noções são fundamentais para compreender a saúde de maneira mais ampla, pois "
                "ajudam a analisar como as condições de vida influenciam a situação de saúde das populações. "
                "Para o SUS, pensar em território usado significa compreender:"
            )
            + ul(
                [
                    "<strong>Os fluxos e movimentos:</strong> Por onde as pessoas circulam para trabalhar, buscar "
                    "atendimento, lazer etc. A área de abrangência de uma Unidade Básica de Saúde (UBS) não pode ser "
                    "definida apenas por linhas no mapa, mas deve considerar os trajetos reais da população.",
                    "<strong>As redes sociais e de apoio:</strong> Onde as pessoas buscam ajuda e informação "
                    "(igrejas, associações de bairro, etc.).",
                    "<strong>As vulnerabilidades e potencialidades:</strong> O território contém tanto as áreas de risco "
                    "(ex: áreas de alagamento, pontos de venda de drogas) quanto os ativos de saúde "
                    "(ex: praças, academias populares, grupos comunitários).",
                ]
            )
        )
    )


def content_saude() -> str:
    return (
        heading(5, "Mas afinal de que saúde estamos falando?")
        + row(
            p(
                "Não existe um conceito único de saúde; seu significado varia conforme o contexto histórico "
                "e social. Ao longo da história, o conceito de saúde passou por diversas transformações, "
                "acompanhando as mudanças científicas, culturais e sociais da humanidade. Na Antiguidade, "
                "ela era vista como equilíbrio entre corpo e mente, influenciada pelo ambiente (Hipócrates, "
                "2005). Na Idade Moderna, prevaleceu o modelo biomédico, que entendia saúde como "
                "ausência de doença (Buss &amp; Pellegrini Filho, 2007). Após a Segunda Guerra Mundial, a OMS "
                "ampliou esse conceito ao incluir o bem-estar físico, mental e social, e não apenas a ausência "
                "de doença (OMS, 1946). Hoje, a saúde é compreendida como um processo dinâmico, "
                "determinado também pelas condições de vida, como moradia, renda, educação, trabalho e "
                "acesso a serviços públicos."
            )
        )
        + voce_sabia_toggle(
            "m3a1-voce-sabia-sus",
            "<p>Nossa Constituição Federal de 1988, artigo 196, diz que: “A saúde é direito de "
            "todos e dever do Estado, garantido mediante políticas sociais e econômicas que "
            "visem à redução do risco de doença e de outros agravos e ao acesso universal "
            "e igualitário às ações e serviços para a promoção, proteção e recuperação”. "
            "Este é o princípio que norteia o SUS, Sistema Único de Saúde (Brasil, 2014).</p>",
        )
        + box(
            "Para Refletir",
            "Para Refletir",
            "Considerando o que você leu até aqui, pense na sua cidade ou localidade. "
            "Certamente deve ter percebido que algumas doenças aparecem mais em determinados "
            "bairros, cidades ou regiões. Mas por que isso acontece? Agora você já saber responder. "
            "Basta olhar para o território, o ambiente onde as pessoas vivem, trabalham e circulam. "
            "Cada lugar reúne características físicas, como clima e relevo; sociais, como renda e "
            "condições de moradia; e estruturais, como saneamento básico e acesso aos serviços de "
            "saúde. Quando analisamos todos esses elementos juntos, entendemos melhor por que as "
            "doenças se distribuem de forma desigual e podemos planejar ações de saúde mais eficientes.",
        )
        + row(
            '<div class="row g-4">'
            + flipcard(
                "m3a1-dengue",
                "Dengue",
                "<p>Um exemplo claro é a <strong>dengue</strong>. Em áreas urbanas onde falta saneamento e há acúmulo de "
                "água parada, o mosquito Aedes aegypti se prolifera com facilidade. A análise territorial ajuda a "
                "descobrir quais bairros têm mais casos e permite direcionar ações específicas, como eliminar "
                "criadouros, reforçar campanhas educativas e intensificar a vigilância epidemiológica.</p>",
            )
            + flipcard(
                "m3a1-lepto",
                "Leptospirose",
                "<p>A <strong>leptospirose</strong> também mostra como o território influencia a saúde. Ela é mais comum em "
                "locais com enchentes, esgoto a céu aberto ou infraestrutura urbana deficiente. Assim, após "
                "períodos de chuva intensa, algumas regiões ficam mais vulneráveis a surtos. Com a análise "
                "territorial, gestores podem planejar ações preventivas, como limpeza de áreas de risco e "
                "orientação à população.</p>",
            )
            + flipcard(
                "m3a1-resp",
                "Doenças respiratórias",
                "<p>Ainda podemos pensar em outro exemplo envolvendo as doenças respiratórias. Em regiões "
                "com muita poluição do ar ou grande concentração industrial, é comum encontrar mais casos de "
                "asma e bronquite. Da mesma forma, áreas densamente povoadas, com grande circulação de "
                "pessoas, favorecem a rápida disseminação de infecções respiratórias — como vimos durante a "
                "pandemia de COVID19.</p>",
            )
            + "</div>"
        )
    )


def content_unidade() -> str:
    return (
        heading(6, "Unidade Geográfica de Análise")
        + row(
            p(
                "Até aqui, você viu que algumas doenças aparecem mais em certos lugares do que em outros. "
                "A Geografia da Saúde busca entender responder essa questão, analisando como o espaço "
                "influencia e revela desigualdades em saúde. Para isso, um passo essencial é definir qual será "
                "a unidade geográfica de análise, ou seja, o recorte territorial que será usado no estudo "
                "(Meade &amp; Emch, 2010)."
            )
            + p(
                "A unidade geográfica de análise é a entidade espacial ou recorte territorial que servirá de "
                "base para coletar, organizar e analisar os dados. Ela assume papel estratégico, pois define "
                "a escala a partir dos quais os fenômenos serão observados, comparados e interpretados."
            )
        )
        + subheading("Por que a escolha da unidade importa?")
        + row(
            p(
                "A escolha define o que você enxerga. Por exemplo, analisar o desmatamento em uma "
                "escala global revela tendências climáticas, enquanto a análise no nível local (município) "
                "revela os atores responsáveis e conflitos agrários específicos."
            )
            + p(
                "A unidade geográfica de análise é fundamental porque mostra como as doenças e os "
                "cuidados em saúde se distribuem no espaço, revelando desigualdades, vulnerabilidades e "
                "padrões que não aparecem quando olhamos apenas para indivíduos ou para escalas muito "
                "amplas (Guimarães, 2003). Ela também organiza a coleta de dados epidemiológicos, "
                "já que indicadores como incidência, prevalência, mortalidade e cobertura vacinal são "
                "calculados a partir de recortes territoriais específicos, como municípios, bairros ou setores "
                "censitários. Escolher bem a unidade torna as análises mais precisas e comparáveis entre "
                "diferentes áreas."
            )
            + p(
                "A partir da sua inserção no SUS, você deve saber que a atuação da saúde ocorre em "
                "diferentes escalas - municipal, estadual e federal - e cada uma utiliza recortes territoriais "
                "próprios para organizar serviços, ações e informações. Esses recortes podem variar entre "
                "setores administrativos usados por outras áreas, como energia, telefonia ou educação, "
                "e também pelos limites definidos pela própria saúde para atender a população. Mesmo "
                "quando não são claramente delimitados, esses territórios são essenciais para planejar "
                "os serviços e produzir diagnósticos mais precisos."
            )
            + p(
                "Nesse contexto, entender escala geográfica é fundamental: ela indica o nível de detalhe "
                "e a abrangência espacial de um fenômeno, podendo ser global, regional, nacional ou local "
                "(Moreira, 2007). Essa noção ajuda a compreender como os problemas de saúde se "
                "manifestam em cada território e orienta análises mais adequadas."
            )
        )
        + accordion(
            "m3a1-escalas",
            [
                (
                    "Escala global",
                    "<p>Na escala global, a saúde é impactada por dinâmicas que ultrapassam fronteiras "
                    "nacionais. A circulação internacional de pessoas e mercadorias, por exemplo, facilita a "
                    "disseminação de doenças infecciosas, como ocorreu durante a pandemia de COVID-19. "
                    "Além disso, questões como mudanças climáticas, insegurança alimentar e "
                    "desigualdades socioeconômicas globais afetam diretamente os indicadores de saúde em "
                    "diversos países (ONU, 2024; IPCC, 2023). Organismos internacionais, como a Organização "
                    "Mundial da Saúde (OMS), desempenham papel fundamental na coordenação de ações, na "
                    "definição de diretrizes sanitárias e no monitoramento de emergências em saúde pública.</p>",
                ),
                (
                    "Escala regional",
                    "<p>Na escala regional, observam-se padrões de saúde que variam conforme "
                    "características ambientais, econômicas e culturais específicas. Certas regiões "
                    "podem apresentar maior incidência de doenças tropicais, enquanto outras "
                    "enfrentam problemas relacionados ao envelhecimento populacional ou à poluição "
                    "industrial. A análise regional permite identificar desigualdades no acesso a "
                    "serviços de saúde e na distribuição de recursos, contribuindo para a formulação "
                    "de estratégias mais adequadas às particularidades de cada área (BRASIL, 2011).</p>",
                ),
                (
                    "Escala nacional",
                    "<p>Na escala nacional, a saúde é estruturada por políticas públicas, sistemas de "
                    "atendimento e investimentos governamentais. No caso do Brasil, por exemplo, "
                    "o Sistema Único de Saúde (SUS) organiza a oferta de serviços em todo o território, "
                    "buscando garantir acesso universal e gratuito à população. Nesse nível, são definidos "
                    "programas de vacinação, campanhas de prevenção, estratégias de combate a "
                    "epidemias e políticas de financiamento do setor. A escala nacional também evidencia "
                    "desigualdades internas, como diferenças entre áreas urbanas e rurais.</p>",
                ),
                (
                    "Escala local",
                    "<p>Na escala local, a saúde se manifesta no cotidiano das comunidades. É nesse nível "
                    "que fatores como saneamento básico, qualidade da água, coleta de lixo, condições de "
                    "moradia e acesso a unidades de saúde influenciam diretamente a qualidade de vida. "
                    "A atuação de postos de saúde, hospitais municipais e agentes comunitários torna-se "
                    "decisiva para a prevenção de doenças e para a promoção da saúde (BRASIL, 2011). "
                    "Além disso, é no espaço local que os impactos de decisões globais e nacionais se "
                    "concretizam, afetando de maneira direta a população.</p>",
                ),
            ],
            first_open=True,
        )
        + row(
            p(
                "Portanto, compreender a saúde a partir das diferentes escalas geográficas permite uma "
                "visão integrada dos problemas e das soluções. As políticas globais influenciam estratégias "
                "nacionais, que por sua vez precisam considerar as especificidades regionais e locais. "
                "Essa articulação entre escalas é fundamental para a construção de sistemas de saúde mais "
                "eficientes, equitativos e capazes de responder aos desafios contemporâneos."
            )
            + p(
                "Uma boa definição da unidade geográfica de análise permite identificar desigualdades "
                "socioespaciais em saúde de maneira mais assertiva. Problemas como surtos de doenças "
                "infecciosas, maior ocorrência de doenças crônicas ou baixa cobertura de serviços "
                "frequentemente se concentram em determinados territórios marcados por precariedade "
                "de infraestrutura, baixa renda ou dificuldades de acesso aos serviços. Ao delimitar "
                "corretamente o recorte espacial, torna-se possível evidenciar a relação entre condições "
                "ambientais, sociais e econômicas e os padrões de saúde da população."
            )
            + p(
                "Além disso, a unidade espacial é essencial para o planejamento e a gestão das políticas "
                "públicas de saúde. Na Atenção Primária, por exemplo, a organização das equipes e a "
                "definição das áreas de abrangência são feitas com base em territórios específicos (Brasil, "
                "2014). Esse recorte orienta a distribuição de recursos, a priorização de ações preventivas "
                "e o acompanhamento das famílias, tornando as intervenções mais direcionadas e eficazes."
            )
            + p(
                "Outro aspecto relevante, mas que trataremos nas últimas aulas desta disciplina - Análise "
                "Espacial, diz respeito ao rigor metodológico. Os resultados de uma pesquisa podem variar "
                "conforme o nível de agregação espacial adotado, fenômeno conhecido como Problema da "
                "Unidade Espacial Modificável (MAUP). Isso significa que a escolha da unidade de análise "
                "pode influenciar taxas, médias e interpretações, exigindo fundamentação teórica consistente "
                "e clareza nos critérios adotados (Openshaw, 1985)."
            )
            + p(
                "Portanto, a unidade geográfica de análise é importante nos estudos de saúde porque "
                "estrutura a produção do conhecimento, orienta a formulação de políticas públicas e possibilita "
                "a identificação de desigualdades territoriais, contribuindo para ações mais equitativas e "
                "eficazes no cuidado à população."
            )
            + p(
                "Ao longo desta aula, vimos que compreender a saúde exige um olhar atento para o território "
                "e para as diversas relações entre ambiente, sociedade e processos de adoecimento. "
                "A Geografia da Saúde, ao articular conceitos como espaço geográfico, lugar e território, "
                "permite reconhecer padrões, desigualdades e determinantes que moldam a vida das "
                "populações. Mais do que uma abordagem teórica, ela é uma ferramenta essencial para "
                "o planejamento em saúde, contribuindo para políticas mais justas, ações mais eficazes e uma "
                "compreensão ampliada do cuidado."
            )
            + p(
                "Ao avançarmos nos próximos conteúdos, seguiremos aprofundando essas ideias, "
                "consolidando a análise espacial e toda sua operacionalização. Nas próximas aulas, você terá a "
                "oportunidade de colocar em prática todos esses conceitos, explorando ferramentas, técnicas e "
                "exemplos reais de análise espacial em saúde. Vamos aprender como visualizar dados no "
                "território, elaborar e interpretar mapas, identificar padrões de adoecimento e compreender "
                "como essas informações apoiam o planejamento em saúde no SUS.",
                mb0=True,
            )
        )
    )


def content_referencias() -> str:
    items = "".join(f'<p class="referencias-item">{ref}</p>' for ref in REFERENCES)
    return heading(7, "Referências") + row(f'<div class="referencias-aula">{items}</div>')


CONTENT_BUILDERS = [
    content_sobre,
    content_introducao,
    content_mapeamento,
    content_geografia,
    content_saude,
    content_unidade,
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
