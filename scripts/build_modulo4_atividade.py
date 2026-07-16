#!/usr/bin/env python3
"""Gera atividade formativa do Módulo 4."""
from __future__ import annotations

import html
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "modulo4" / "atividade.html"

MODULE_TITLE = "Interoperabilidade de Sistemas"


def esc(text: str) -> str:
    return html.escape(text, quote=True)


def exercise_block(num: int, question: str, options: list[tuple[str, str, bool]]) -> str:
    opts = []
    for text, feedback, correct in options:
        attrs = ' tabindex="0"'
        if correct:
            attrs += " correct"
        opts.append(
            f'<li class="answer__option" data-feedback="{esc(feedback)}"{attrs}><p>{text}</p></li>'
        )
    answers = "\n".join(opts)
    return (
        f'<div class="row justify-content-center mb-5"><div class="col-12 col-md-10 col-lg-8">'
        f'<div class="exercise" data-exercise="one"><div class="card">'
        f'<div class="card-header">Questão {num}</div><div class="card-body">'
        f'<div class="exercise__question"><p>{question}</p></div>'
        f'<div class="exercise__answers"><ul>{answers}</ul></div></div>'
        f'<div class="card-footer"><div class="exercise__submit">'
        f'<span class="exercise__submit--feedback d-none"></span>'
        f'<button class="fio-button fio-button-primary" type="submit" disabled>Conferir</button>'
        f"</div></div></div></div></div></div>"
    )


QUESTIONS = [
    (
        "A Lei nº 14.129/2021 estabelece a interoperabilidade como princípio do Estado. Em seu Art. 39, ela define "
        "finalidades específicas para o mecanismo de interoperabilidade. Uma dessas finalidades é:",
        [
            (
                "a) Concentrar a gestão de todos os dados de saúde em um banco federal único para maior segurança.",
                "Incorreta. A lei não prega a centralização, mas sim a interoperabilidade entre sistemas distribuídos, "
                "respeitando a gestão descentralizada do SUS.",
                False,
            ),
            (
                "b) Aprimorar a gestão de políticas públicas por meio da integração qualificada de dados entre órgãos.",
                "Correta. O Art. 39, inciso I, da Lei nº 14.129/2021, tem como uma de suas finalidades expressas "
                '"aprimorar a gestão de políticas públicas".',
                True,
            ),
            (
                "c) Permitir o acesso irrestrito de pesquisadores internacionais às bases de dados nacionais para fins de estudo.",
                "Incorreta. O acesso é regulado por leis nacionais (como a LGPD) e acordos de governança, não sendo irrestrito.",
                False,
            ),
            (
                "d) Substituir o CPF por um novo identificador biométrico único para todos os serviços públicos.",
                "Incorreta. A lei, em seu Art. 39, V, reforça o uso do CPF como base para o tratamento de informações, "
                "não prevendo sua substituição.",
                False,
            ),
            (
                "e) Obrigar os entes federados a utilizarem exclusivamente softwares proprietários fornecidos pela União.",
                "Incorreta. A lei incentiva padrões abertos e a interoperabilidade entre sistemas heterogêneos, "
                "não a adoção de um software único.",
                False,
            ),
        ],
    ),
    (
        "O decreto de 2025, que oficializa a RNDS como plataforma de interoperabilidade do SUS, estabelece diretrizes "
        "para sua governança e uso. De acordo com esse marco legal, um dos objetivos centrais da rede é:",
        [
            (
                "a) Transferir a responsabilidade pela coleta e gestão de todos os dados de saúde dos municípios para o governo federal.",
                "Incorreta. O decreto não centraliza a gestão, mas organiza o compartilhamento. A responsabilidade primária "
                "pelos dados permanece com o ente federativo que os gerou.",
                False,
            ),
            (
                "b) Criar um banco de dados centralizado no Ministério da Saúde para análise exclusiva por pesquisadores do governo.",
                "Incorreta. O acesso é descentralizado e serve a múltiplos fins (assistência, gestão, vigilância), "
                "não sendo restrito a um único grupo ou finalidade.",
                False,
            ),
            (
                "c) Substituir os sistemas de informação estaduais e municipais por uma única plataforma nacional obrigatória para todos os entes.",
                "Incorreta. A RNDS opera em modelo de interoperabilidade, conectando-se aos sistemas locais existentes, não os substituindo.",
                False,
            ),
            (
                "d) Garantir acesso integral, ágil e descentralizado aos dados pelos estados, Distrito Federal e municípios, "
                "promovendo a continuidade do cuidado.",
                "Correta. O decreto define como objetivo garantir o acesso integral, ágil e descentralizado a seus dados pelos "
                "estados, pelo Distrito Federal e pelos municípios, de forma a promover a transição e a continuidade do cuidado ao cidadão.",
                True,
            ),
            (
                "e) Permitir que empresas privadas de tecnologia acessem dados anonimizados para desenvolver novos produtos comerciais.",
                "Incorreta. O compartilhamento é estritamente regulado para fins de Saúde Pública, assistência e pesquisa autorizada, "
                "observando a LGPD, e não para desenvolvimento comercial.",
                False,
            ),
        ],
    ),
    (
        "A interoperabilidade da RNDS cria um ecossistema por meio do qual dados de saúde são compartilhados de forma segura. "
        "Um exemplo concreto de seu impacto direto na assistência à população, é:",
        [
            (
                "a) A identificação de pacientes que interromperam a retirada de medicamentos e seu reengajamento de modo facilitado.",
                "Correta. Conforme divulgado pelo Ministério da Saúde, a RNDS e o Meu SUS Digital permitiram identificar e notificar "
                "mais de 150 mil usuários que haviam deixado de retirar medicamentos no Farmácia Popular, resultando no retorno ao tratamento.",
                True,
            ),
            (
                "b) A substituição automática de consultas presenciais por telemedicina em todas as especialidades.",
                "Incorreta. Embora a RNDS possa dar suporte à telemedicina ao compartilhar dados, ela não determina ou substitui "
                "modalidades de atendimento, que são decisões clínicas e organizacionais.",
                False,
            ),
            (
                "c) A redução imediata do preço dos medicamentos dispensados pelo Farmácia Popular em todo o país.",
                "Incorreta. A RNDS atua na integração de dados e gestão da informação, não na definição de políticas de preços de medicamentos.",
                False,
            ),
            (
                "d) A criação de um novo sistema de agendamento único nacional que unificou todas as filas do SUS.",
                "Incorreta. A RNDS não é um sistema de agendamento. Ela pode fornecer dados sobre filas, mas não é, em si, a plataforma de agendamento.",
                False,
            ),
            (
                "e) A permissão para que hospitais privados acessem dados clínicos completos de qualquer cidadão para otimizar internações.",
                "Incorreta. O acesso aos dados na RNDS é extremamente seguro e segmentado. Hospitais privados participantes do SUS só podem "
                "acessar dados relevantes ao cuidado do paciente sob sua responsabilidade no contexto do atendimento e dentro das regras "
                "estritas da LGPD.",
                False,
            ),
        ],
    ),
]


def build_exercises() -> str:
    return "\n".join(exercise_block(i, q, opts) for i, (q, opts) in enumerate(QUESTIONS, 1))


def build_page() -> str:
    exercises = build_exercises()
    return f"""<!DOCTYPE html>
<html lang="pt-br">
<head>
	<meta charset="utf-8" />
	<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no, user-scalable=yes" />
	<meta http-equiv="content-type" content="text/html; charset=utf-8" />
	<meta name="robots" content="noindex" />
	<meta name="author" content="Fiocruz, Campus Virtual" />
	<meta name="description" content="Curso Fontes de Dados e Sistemas de Informação para o SUS" />
	<link rel="apple-touch-icon" sizes="180x180" href="../media/icons/apple-icon-180x180.png" />
	<link rel="icon" type="image/png" sizes="32x32" href="../media/icons/favicon-32x32.png" />
	<meta name="theme-color" content="#001833" />
	<title>Curso Fontes de Dados e Sistemas de Informação para o SUS | Mod 4 | Atividade</title>
	<link rel="stylesheet" href="../source/bootstrap-5.1.3/css/bootstrap.min.css" />
	<link rel="stylesheet" href="../assets/css/style.css" />
</head>
<body>
	<header class="header">
		<div class="mobile-toggle-open"><a class="mobile-toggle__button" tabindex="0" role="button"><span class="icon material-symbols-rounded">read_more</span></a></div>
		<div class="brand"><img class="img-fluid logo-black" src="../media/logos/header-fiocruz-campus-virtual.png" alt="Campus Virtual Fiocruz" /></div>
		<div class="title"><h1>Fontes de Dados e Sistemas de Informação para o SUS</h1></div>
		<ul class="nav nav-pills">
			<li class="nav-item"><a href="../index.html" class="nav-link">Início</a></li>
			<li class="nav-item"><a href="#" class="nav-link" data-bs-toggle="modal" data-bs-target="#modal-creditos">Créditos</a></li>
		</ul>
	</header>
	<div class="main">
		<div class="sidebar" role="navigation">
			<div class="sidebar__inner" style="position: relative">
				<div class="sidebar__group d-lg-none">
					<div class="sidebar__group-item"><div class="sidebar__header"><span>Curso</span><a class="mobile-toggle-close" tabindex="0" role="button"><span class="icon material-symbols-rounded">read_more</span></a></div></div>
					<div class="sidebar__group-item"><div class="sidebar__title"><h1>Fontes de Dados e Sistemas de Informação para o SUS</h1></div></div>
					<div class="sidebar__group-item"><ul class="nav">
						<li class="nav-item"><a href="../index.html" class="nav-link" tabindex="0"><span class="icon material-symbols-rounded" aria-hidden="true">home</span>Início</a></li>
						<li class="nav-item"><a href="#" class="nav-link" tabindex="0" data-bs-toggle="modal" data-bs-target="#modal-creditos"><span class="icon material-symbols-rounded" aria-hidden="true">format_list_bulleted</span>Créditos</a></li>
					</ul></div>
				</div>
				<div class="sidebar__group">
					<div class="sidebar__group-item">
						<div class="dropend">
							<button id="dropdown-modulos" type="button" class="dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false" data-bs-auto-close="outside" data-bs-offset="0,30">
								<span class="icon material-symbols-rounded" aria-hidden="true">grid_view</span><span class="label">Módulos</span>
							</button>
							<ul class="dropdown-menu" aria-labelledby="dropdown-modulos">
								<li class="d-lg-none dropdown-menu__header"><a class="dropdown-menu__back-button" tabindex="0" role="button"><span class="icon material-symbols-rounded">chevron_left</span> Voltar</a><a class="mobile-toggle-close" tabindex="0" role="button"><span class="icon material-symbols-rounded">read_more</span></a></li>
								<li class="dropdown-menu__item"><a class="dropdown-menu__item-link" tabindex="0" role="link" href="../modulo1/aula1/topico1.html"><strong>Módulo 1</strong><br />Introdução à Informação em Saúde no SUS</a></li>
								<li class="dropdown-menu__item"><a class="dropdown-menu__item-link" tabindex="0" role="link" href="../modulo2/aula1/topico1.html"><strong>Módulo 2</strong><br />Fontes de Dados Socioeconômicos e Demográficos: subsídios para a Saúde</a></li>
								<li class="dropdown-menu__item"><a class="dropdown-menu__item-link" tabindex="0" role="link" href="../modulo3/aula1/topico1.html"><strong>Módulo 3</strong><br />Sistemas de Informação em Saúde</a></li>
								<li class="dropdown-menu__item"><a class="dropdown-menu__item-link" tabindex="0" role="link" href="aula1/topico1.html"><strong>Módulo 4</strong><br />{MODULE_TITLE}</a></li>
							</ul>
						</div>
					</div>
				</div>
				<div class="divider"><hr /></div>
				<div class="sidebar__group">
					<div class="sidebar__group-item"><span class="text module">Módulo <br class="d-none d-lg-block" /><span>4</span></span></div>
					<div class="sidebar__group-item">
						<div class="dropend">
							<button type="button" class="dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false" data-bs-auto-close="outside" data-bs-offset="0,30">
								<span class="icon material-symbols-rounded" aria-hidden="true">apps</span><span class="label">Conteúdo</span>
							</button>
							<ul class="dropdown-menu">
								<li class="d-lg-none dropdown-menu__header"><a class="dropdown-menu__back-button" tabindex="0" role="button"><span class="icon material-symbols-rounded">chevron_left</span> Voltar</a><a class="mobile-toggle-close" tabindex="0" role="button"><span class="icon material-symbols-rounded">read_more</span></a></li>
								<li class="dropdown-menu__title"><span class="label">Módulo 4</span><span class="title">{MODULE_TITLE}</span></li>
								<li class="dropdown-menu__item"><a class="dropdown-menu__item-link" tabindex="0" role="link" href="aula1/topico1.html"><strong>Aula 1: </strong>Interoperabilidade na Saúde</a></li>
								<li class="dropdown-menu__item"><a class="dropdown-menu__item-link" tabindex="0" role="link" href="aula2/topico1.html"><strong>Aula 2: </strong>Integração de Dados em Saúde</a></li>
								<li class="dropdown-menu__item"><a class="dropdown-menu__item-link" tabindex="0" role="link" href="atividade.html"><strong>Atividade</strong></a></li>
							</ul>
						</div>
					</div>
				</div>
			</div>
		</div>
		<div class="content">
			<div id="page-title"><div class="container"><div class="row align-items-center hstify-content-center justify-content-xxl-start ms-lg-5"><div class="col-12 col-md-10 col-lg-11"><h2 class="title"><span class="label">Módulo 4</span><br />{MODULE_TITLE}</h2></div></div></div></div>
			<div id="page-content" class="">
				<section><div class="container">
					<div class="row justify-content-center"><div class="col-12 col-md-10 col-lg-8 mb-4">
						<div class="heading__block"><h3 class="heading__title">Atividade formativa</h3></div>
						<p>Responda às três questões a seguir para revisar os principais conceitos do módulo <strong>{MODULE_TITLE}</strong>. Selecione uma alternativa e clique em <strong>Conferir</strong> para ver se acertou e ler o feedback.</p>
					</div></div>
{exercises}
				</div></section>
			</div>
			<section><div class="container"><div class="row justify-content-center"><div class="col-12 col-md-10 col-lg-8"><div class="page-nav d-flex justify-content-evenly flex-wrap gap-3"><a class="fio-button fio-button-primary" href="aula2/topico9.html" rel="prev"><span class="material-symbols-rounded" aria-hidden="true">west</span> Referências (Aula 4.2)</a></div></div></div></div></section>
			<footer><div class="container-fluid"><div class="row justify-content-center align-items-center linha-de-marcas"><div class="col-12 text-center py-3"><img class="img-fluid regua-logos" src="../media/logos/regua-de-logos.png" alt="Régua de logos: Campus Virtual Fiocruz, Fiocruz, SUS Digital, SUS 35 Anos, Ministério da Saúde e Governo do Brasil" /></div></div></div></footer>
		</div>
	</div>
	<script src="../source/bootstrap-5.1.3/js/bootstrap.bundle.min.js"></script>
	<script type="text/javascript" src="../assets/js/ResizeSensor.js"></script>
	<script type="text/javascript" src="../assets/js/sticky-sidebar.js"></script>
	<script type="text/javascript" src="../assets/js/sidebar.js"></script>
	<script type="text/javascript">var sidebar = new StickySidebar('.sidebar', {{ topSpacing: 0, bottomSpacing: 0, containerSelector: '.main', innerWrapperSelector: '.sidebar__inner', minWidth: 991 }});</script>
	<script type="text/javascript" src="../assets/js/scripts.js"></script>
	<script type="text/javascript" src="../assets/js/exercise.js"></script>
	<script type="text/javascript" src="../assets/js/custom-anime.js"></script>
	<script type="text/javascript" src="../source/animate/aos/dist/aos.js"></script>
	<script>AOS.init();</script>
</body>
</html>
"""


def main() -> None:
    OUT.write_text(build_page(), encoding="utf-8")
    print(f"Criado: {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
