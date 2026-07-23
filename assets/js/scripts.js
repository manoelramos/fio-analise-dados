// Stick Header

window.addEventListener("scroll", function () {
	const header = document.querySelector(".header");
	const titleHeight = document.querySelector(".header").scrollHeight;

	if (window.scrollY > 150) {
		header.classList.add("header--sticky");
	} else {
		header.classList.remove("header--sticky");
	}
});

// Popover
var popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'));
var popoverList = popoverTriggerList.map(function (popoverTriggerEl) {
	return new bootstrap.Popover(popoverTriggerEl);
});

// Prioridades PNIIS: apenas um popover aberto por vez; fecha ao clicar fora
(function () {
	var container = document.querySelector('.pniis-prioridades');
	if (!container) return;

	var triggers = container.querySelectorAll('[data-bs-toggle="popover"]');

	function hideAllPniisPopovers() {
		triggers.forEach(function (el) {
			var instance = bootstrap.Popover.getInstance(el);
			if (instance) {
				instance.hide();
			}
		});
	}

	triggers.forEach(function (triggerEl) {
		triggerEl.addEventListener('show.bs.popover', function () {
			triggers.forEach(function (otherEl) {
				if (otherEl !== triggerEl) {
					var instance = bootstrap.Popover.getInstance(otherEl);
					if (instance) {
						instance.hide();
					}
				}
			});
		});
	});

	document.addEventListener('click', function (event) {
		if (event.target.closest('.pniis-prioridades__item') || event.target.closest('.popover')) {
			return;
		}
		hideAllPniisPopovers();
	});
})();

// //Swiper (inicialização)

// //Type 1: Swiper Navigation
// var swiper = new Swiper('.swiper--navigation', {
// 	direction: 'horizontal',
// 	loop: false,
// 	slidesPerView: 1,
// 	spaceBetween: 30,

// 	//Mousewheel control
// 	mousewheel: true,

// 	//Keyboard control
// 	keyboard: {
// 		enabled: true,
// 	},

// 	// Navigation arrows
// 	navigation: {
// 		nextEl: '.swiper-button-next',
// 		prevEl: '.swiper-button-prev',
// 	},

// 	//Pagination (if needed)
// 	pagination: {
// 		el: '.swiper-pagination',
// 		clickable: true,
// 		type: 'bullets',
// 	},

// 	// Scrollbar (if needed)
// 	scrollbar: {
// 		el: '.swiper-scrollbar',
// 	},
// });

//Type 2: Swiper Vertical
// var swiperVertical = new Swiper('.swiper--vertical', {
// 	direction: 'vertical',
// 	slidesPerView: 1,
// 	spaceBetween: 0,
// 	mousewheel: true,
// 	pagination: {
// 		el: '.swiper-pagination2',
// 		clickable: true,
// 	},
// });

// //Type 3: Effect Card
// var swiperVertical = new Swiper('.swiper--effect-card', {
// 	effect: 'cards',
// 	grabCursor: true,
// 	pagination: {
// 		el: '.swiper-pagination3',
// 		clickable: true,
// 	},
// });

// Botão de copiar podcast

const copyButton = document.querySelectorAll(".copy-to-clip");

copyButton.forEach((btn) => {
	btn.addEventListener("click", () => {
		copyToClipboard(btn);
		// tooltipShow(btn);

		tooltipFeedback(btn);
	});
});

function copyToClipboard(e) {
	const textToCopy = e.getAttribute("data-link");
	const textarea = document.createElement("textarea");
	textarea.setAttribute("readonly", "");
	textarea.style.position = "absolute";
	textarea.value = textToCopy;
	document.body.appendChild(textarea);
	textarea.select();
	document.execCommand("copy");
	document.body.removeChild(textarea);
}
function tooltipFeedback(b) {
	let feedback = $('[data-toggle="tooltip"]');

	// feedback.tooltip('show');

	b.addEventListener("mouseout", () => {
		feedback.tooltip("hide");
	});
}

// Lightbox (insert the class "lightbox" into <figure>)

const imageToLightbox = document.querySelectorAll(".lightbox");
// const lightboxImage = imageToLightbox.querySelector("img");

console.log(imageToLightbox);

imageToLightbox.forEach((image) => {
	image.addEventListener("click", () => {
		if (!image.classList.contains("lightbox--show")) {
			const getImage = image.querySelector("img");
			const getImageSrc = getImage.getAttribute("src");
			const imageLightbox = document.createElement("div");

			imageLightbox.classList.add("lightbox__image");

			document.body.appendChild(imageLightbox);
			imageLightbox.innerHTML = `<img src="${getImageSrc}"/>`;
			console.log(getImageSrc);

			image.classList.add("lightbox--show");

			document.body.style.overflow = "hidden";
			document.body.style.userSelect = "none";

			closeLightbox(imageLightbox);
		}

		function closeLightbox(e) {
			const lightboxOpen = document.querySelector(".lightbox__image");
			e.addEventListener("click", () => {
				document.body.removeChild(e);
				image.classList.remove("lightbox--show");
				document.body.style.overflow = "auto";
				document.body.style.userSelect = "auto";
			});
		}
	});
});

// Boxes - inserir o título de acordo com o atributo

const boxes = document.querySelectorAll(".box");

boxes.forEach((box) => {
	const boxAttribute = box.getAttribute("data-box");

	const boxLabel = box.querySelector(".label");

	boxLabel.innerHTML = boxAttribute;
});

// Modal - Criação dos modais principais

const modalInfos = {
	creditos: {
		ariaLabel: "creditos",
		modalSize: "modal-xl",
		modalTitle: "Créditos",
		modalBody: `
			<div class="row justify-content-center pt-4">
				<div class="col-12 col-md-11 col-lg-10 creditos-curso">
					<span class="h5 mb-3 d-block">Curso</span>
					<p class="mb-5">Análise e Interpretação de Dados em Saúde</p>
					<span class="h5 mb-3 d-block">Ministério da Saúde</span>
					<div class="mb-5">
						<p class="mb-1">Alexandre Padilha</p>
						<p class="small text-muted"><em>Ministro</em></p>
					</div>
					<span class="h5 mb-3 d-block">Fundação Oswaldo Cruz – Fiocruz</span>
					<div class="mb-5">
						<p class="mb-1">Mario Moreira</p>
						<p class="small text-muted"><em>Presidente</em></p>
						<p class="mb-1">Marly Cruz</p>
						<p class="small text-muted"><em>Vice-Presidência de Educação, Informação e Comunicação (VPEIC)</em></p>
					</div>
					<span class="h5 mb-3 d-block">Campus Virtual Fiocruz</span>
					<div class="mb-5">
						<p class="mb-1">Ana Cristina da Matta Furniel</p>
						<p class="small text-muted"><em>Coordenadora geral</em></p>
						<p class="mb-1">Rosane Mendes</p>
						<p class="small text-muted"><em>Coordenadora Adjunta</em></p>
						<p class="mb-1">Renata Bernardes David</p>
						<p class="small text-muted"><em>Coordenação de produção</em></p>
						<p class="mb-1">Juliana Dutra</p>
						<p class="small text-muted"><em>Gerente de produção</em></p>
						<p class="mb-1">Claúdia Reis</p>
						<p class="small text-muted"><em>Assessora pedagógica</em></p>
						<p class="mb-1">Isabela Schincariol</p>
						<p class="small text-muted"><em>Assessora de comunicação</em></p>
						<p class="mb-1">Igor Cruz</p>
						<p class="small text-muted"><em>Designer Educacional</em></p>
						<p class="mb-1">Marco Macedo</p>
						<p class="small text-muted"><em>Designer Gráfico</em></p>
						<p class="mb-1">Manoel Ramos</p>
						<p class="small text-muted"><em>Desenvolvedor</em></p>
						<span class="h6 mb-3 d-block">Suporte Técnico de Tecnologia da Informação</span>
						<p class="mb-1">Bruno Alexandre de Oliveira</p>
						<p class="small text-muted"><em>Desenvolvedor</em></p>
						<p class="mb-1">Eduardo Xavier da Silva</p>
						<p class="small text-muted"><em>Desenvolvedor</em></p>
						<p class="mb-1">Adriano Lourenço</p>
						<p class="small text-muted"><em>Analista de suporte</em></p>
						<p class="mb-1">Orlando Terra</p>
						<p class="small text-muted"><em>Analista de suporte</em></p>
						<p class="mb-1">Fábio Carneiro</p>
						<p class="small text-muted"><em>Designer gráfico e web designer</em></p>
						<p class="mb-1">Catarina Santiago</p>
						<p class="small text-muted"><em>Designer gráfico</em></p>
					</div>
					<span class="h5 mb-3 d-block">Coordenação Acadêmica</span>
					<div class="mb-5">
						<p class="mb-1">Carolina de Campos Carvalho</p>
						<p class="small text-muted mb-0"><em>Instituto de Comunicação e Informação Científica e Tecnológica em Saúde - Icict/Fiocruz</em></p>
						<p class="small text-muted mb-3"><em>Coordenadora</em></p>
						<p class="mb-1">Mônica de Avelar Figueiredo Mafra Magalhães</p>
						<p class="small text-muted mb-0"><em>Instituto de Comunicação e Informação Científica e Tecnológica em Saúde - Icict/Fiocruz</em></p>
						<p class="small text-muted mb-3"><em>Coordenadora</em></p>
						<p class="mb-1">Mel Bonfim</p>
						<p class="small text-muted mb-0"><em>Relações Institucionais/PR/Fiocruz</em></p>
						<p class="small text-muted mb-3"><em>Coordenadora</em></p>
					</div>
					<span class="h5 mb-3 d-block">Conteudistas</span>
					<div class="mb-5">
						<p class="creditos-modulo mb-2 mt-4">Módulo 1: Estatística</p>
						<p class="mb-1">Carla Lourenço Tavares de Andrade</p>
						<p class="small text-muted mb-0"><em>Escola Nacional de Saúde Pública Sergio Arouca – ENSP/Fiocruz</em></p>
						<p class="small text-muted mb-3"><em>[Aulas 1, 2 e 3]</em></p>
						<p class="creditos-modulo mb-2 mt-4">Módulo 2: Análise Temporal</p>
						<p class="mb-1">Diego Ricardo Xavier</p>
						<p class="small text-muted mb-0"><em>Instituto de Comunicação e Informação Científica e Tecnológica em Saúde - Icict/Fiocruz</em></p>
						<p class="small text-muted mb-3"><em>[Aulas 1, 2 e 3]</em></p>
						<p class="mb-1">Julia Novaes de Barros Peixoto</p>
						<p class="small text-muted mb-0"><em>Instituto de Comunicação e Informação Científica e Tecnológica em Saúde - Icict/Fiocruz</em></p>
						<p class="small text-muted mb-3"><em>[Aulas 1, 2 e 3]</em></p>
						<p class="creditos-modulo mb-2 mt-4">Módulo 3: Análise Espacial</p>
						<p class="mb-1">Mônica de Avelar Figueiredo Mafra Magalhães</p>
						<p class="small text-muted mb-0"><em>Instituto de Comunicação e Informação Científica e Tecnológica em Saúde - Icict/Fiocruz</em></p>
						<p class="small text-muted mb-3"><em>[Aulas 1, 2, 3, 4, 5, 6 e 7]</em></p>
						<p class="mb-1">Julia Novaes de Barros Peixoto</p>
						<p class="small text-muted mb-0"><em>Instituto de Comunicação e Informação Científica e Tecnológica em Saúde - Icict/Fiocruz</em></p>
						<p class="small text-muted mb-3"><em>[Aulas 1, 2, 3, 4, 5, 6 e 7]</em></p>
						<p class="mb-1">Diego Ricardo Xavier</p>
						<p class="small text-muted mb-0"><em>Instituto de Comunicação e Informação Científica e Tecnológica em Saúde - Icict/Fiocruz</em></p>
						<p class="small text-muted mb-3"><em>[Aulas 6 e 7]</em></p>
					</div>
				</div>
			</div>
		`,
	},
	bibliografiaMod1: {
		ariaLabel: "bibliografiaMod1",
		modalSize: "modal-xl",
		modalTitle: "Bibliografia Módulo 1",
		modalBody: `
			<div class="row justify-content-center pt-5">
				<div class="col-12 col-md-11">
					<div class="mb-5">
						<!-- Accordion -->
						<div class="accordion accordion-flush" id="accordionExample2">
							<div class="accordion-item">
								<h5 class="accordion-header" id="heading1-item1">
									<button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapse1-item1" aria-expanded="true" aria-controls="collapse1-item1">Aula 1</button>
								</h5>
								<div id="collapse1-item1" class="accordion-collapse collapse" aria-labelledby="heading1-item1" data-bs-parent="">
									<div class="accordion-body">
										<div class="list">
											<ul class="list-group">
												<li class="list-group-item aos-init aos-animate" list-style="default" data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="1200">FIGUEIREDO, José Augusto N. G.; FIGUEIREDO, Jacyra N. G. <strong>Algoritmos</strong>: Lógica para Desenvolvimento de Programação de Computadores. 28. ed. Rio de Janeiro: Érica, 2016.</li>

												<li class="list-group-item aos-init aos-animate" list-style="default" data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="1200">MENEZES, Nilo Ney Coutinho. <strong>Introdução à Programação com Python</strong>: Algoritmos e Lógica de Programação para Iniciantes. 2. ed. São Paulo: Novatec Editora, 2018. Disponível em: <a href='' target='_blank' rel="noopener noreferrer">https://www.kufunda.net/publicdocs/Introdu%C3%A7%C3%A3o%20%C3%A0%20programa%C3%A7%C3%A3o%20com%20Python%20algoritmos%20e%20l%C3%B3gica%20de%20programa%C3%A7%C3%A3o%20para%20iniciantes%20(Nilo%20Ney%20Coutinho%20Menezes).pdf</a>. Acesso em: 8 jun. 2025.</li>

												<li class="list-group-item aos-init aos-animate" list-style="default" data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="1200">MENEZES, Nilo Ney Coutinho.<strong> Introdução à programação com Python:</strong> algoritmos e lógica de programação. 2. ed. São Paulo: Novatec Editora, 2014. p. 53.</li>
											</ul>
										</div>
									</div>
								</div>
							</div>

							<div class="accordion-item">
								<h5 class="accordion-header" id="heading1-item2">
									<button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapse1-item2" aria-expanded="false" aria-controls="collapse1-item2">Aula 2</button>
								</h5>
								<div id="collapse1-item2" class="accordion-collapse collapse" aria-labelledby="heading1-item2" data-bs-parent="">
									<div class="accordion-body">
										<div class="list">
											<ul class="list-group">
												<li class="list-group-item aos-init aos-animate" list-style="default" data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="1200">GROLEMUND, Garrett; WICKHAM, Hadley. <strong>R for Data Science</strong>: import, tidy, transform, visualize, and model data. Disponível em: <a href='https://r4ds.had.co.nz' target='_blank' rel="noopener noreferrer">https://r4ds.had.co.nz</a>. Acesso em: 8 jun. 2025. Versão em português em tradução: Disponível em: <a href='https://r4ds-translation.netlify.app' target='_blank' rel="noopener noreferrer">https://r4ds-translation.netlify.app</a>. Acesso em: 8 jun. 2025.</li>

												<li class="list-group-item aos-init aos-animate" list-style="default" data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="1200">MATLOFF, Norman. <strong>The Art of R Programming</strong>: a tour of statistical software design. San Francisco: No Starch Press, 2011.</li>

												<li class="list-group-item aos-init aos-animate" list-style="default" data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="1200">THEUS, Garrett. <strong>Hands-On Programming with R</strong>: write your own functions and simulations. [S.l.]: Shroff Publishers & Distributors Pvt Ltd, 1 jul. 2014.</li>
											</ul>
										</div>
									</div>
								</div>
							</div>
						</div>
						<!-- Fim do Accordion -->
					</div>

				</div>
			</div>
		`,
	},
	bibliografiaMod2: {
		ariaLabel: "bibliografiaMod2",
		modalSize: "modal-xl",
		modalTitle: "Bibliografia Módulo 2",
		modalBody: `
			<div class="row justify-content-center pt-5">
				<div class="col-12 col-md-11">
					<div class="mb-5">
						<!-- Accordion -->
						<div class="accordion accordion-flush" id="accordionExample2">
							<div class="accordion-item">
								<h5 class="accordion-header" id="heading1-item1">
									<button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapse1-item1" aria-expanded="true" aria-controls="collapse1-item1">Aula 1</button>
								</h5>
								<div id="collapse1-item1" class="accordion-collapse collapse" aria-labelledby="heading1-item1" data-bs-parent="">
									<div class="accordion-body">
										<div class="list">
											<ul class="list-group mb-5">
												<li class="list-group-item aos-init aos-animate" list-style="default" data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="1200">GROLEMUND, Garrett; WICKHAM, Hadley. <strong>R for Data Science</strong>: import, tidy, transform, visualize, and model data. Disponível em: <a href='https://r4ds.had.co.nz' target='_blank' rel="noopener noreferrer">https://r4ds.had.co.nz</a>. Acesso em: 8 jun. 2025. Versão em português em tradução: Disponível em: <a href='https://r4ds-translation.netlify.app' target='_blank' rel="noopener noreferrer">https://r4ds-translation.netlify.app</a>. Acesso em: 8 jun. 2025.</li>

												<li class="list-group-item aos-init aos-animate" list-style="default" data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="1200">GIOVANIS, E.; OZDAMAR, O.; SAMUK, S. Health status and willingness-to-pay estimates for the benefits of improved recycling rates: evidence from Great Britain. <strong>SN Business & Economics</strong>, v. 1, n. 1, 2021. Dispoível em: <a href='https://doi.org/10.1007/s43546-020-00006-9' target='_blank' rel="noopener noreferrer">https://doi.org/10.1007/s43546-020-00006-9</a></li>

												<li class="list-group-item aos-init aos-animate" list-style="default" data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="1200">IMAI, C. <em>et al</em>. Tropical influenza and weather variability among children in an urban low-income population in Bangladesh. <strong>Global Health Action</strong>, v. 7, n. 1, 2014. Disponível em: <a href='https://doi.org/10.3402/gha.v7.24413' target='_blank' rel="noopener noreferrer">https://doi.org/10.3402/gha.v7.24413</a></li>

												<li class="list-group-item aos-init aos-animate" list-style="default" data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="1200">Kostaki, E. G. l. <em>et al</em>. Estimation of the determinants for HIV late presentation using the traditional definition and molecular clock‐inferred dates: Evidence that older age, heterosexual risk group and more recent diagnosis are prognostic factors. <strong>HIV Medicine</strong>, v. 23, n. 11, p. 1143-1152, 2022. Disponível em: <a href='https://doi.org/10.1111/hiv.13415' target='_blank' rel="noopener noreferrer">https://doi.org/10.1111/hiv.13415</a></li>

												<li class="list-group-item aos-init aos-animate" list-style="default" data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="1200">Morettin, P. A. <strong>Estatística Básica</strong>. 10. ed. Campinas, SP: Saraiva Uni, 2024</li>

												<li class="list-group-item aos-init aos-animate" list-style="default" data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="1200">Rosner, B. <strong>Fundamentals of biostatistics</strong>. 6th ed. Belmont, CA: Thomson-Brooks/Cole, 2006</li>
											</ul>

											<p><strong>Websites</strong></p>

											<ul class="list-group">
												<li class="list-group-item aos-init aos-animate" list-style="default" data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="1200">GDESCRIPTIVE Statistics. Disponível em: <a href='https://aprendeconalf.es/en/teaching/statistics/manual/descriptive-statistics/' target='_blank' rel="noopener noreferrer">https://aprendeconalf.es/en/teaching/statistics/manual/descriptive-statistics/</a></li>

												<li class="list-group-item aos-init aos-animate" list-style="default" data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="1200">HISTOGRAMA. 2022. 1 vídeo (8 min.). Disponível em: <a href='https://www.youtube.com/watch?v=cTFUfb0QL7o' target='_blank' rel="noopener noreferrer">https://www.youtube.com/watch?v=cTFUfb0QL7o</a></li>

												<li class="list-group-item aos-init aos-animate" list-style="default" data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="1200">MEDIUM . Boxplot: Como interpretar e plotar em Python? Disponível em: </li>

												<li class="list-group-item aos-init aos-animate" list-style="default" data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="1200">INSTITUTO BRASILEIRO DE GEOGRAFIA E ESTATÍSTICA. PNAD – Pesquisa Nacional por Amostra de Domicílios. Disponível em: <a href='https://www.ibge.gov.br/estatisticas/sociais/populacao/9127-pesquisa-nacional-por-amostra-de-domicilios.html?=&t=o-que-e' target='_blank' rel="noopener noreferrer">https://www.ibge.gov.br/estatisticas/sociais/populacao/9127-pesquisa-nacional-por-amostra-de-domicilios.html?=&t=o-que-e</a></li>
											</ul>
										</div>
									</div>
								</div>
							</div>

							<div class="accordion-item">
								<h5 class="accordion-header" id="heading1-item2">
									<button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapse1-item2" aria-expanded="false" aria-controls="collapse1-item2">Aula 2</button>
								</h5>
								<div id="collapse1-item2" class="accordion-collapse collapse" aria-labelledby="heading1-item2" data-bs-parent="">
									<div class="accordion-body">
										<div class="list">
											<ul class="list-group mb-5">
												<li class="list-group-item aos-init aos-animate" list-style="default" data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="1200">EME, P. E. <em>et al</em>. Obesity measures in the Kiribati population: a need to reclassify body mass index cut-points. <strong>BMC Public Health</strong>, v. 20, n. 1, 2020. <a href='https://doi.org/10.1186/s12889-020-09217-z' target='_blank' rel="noopener noreferrer">https://doi.org/10.1186/s12889-020-09217-z</a></li>

												<li class="list-group-item aos-init aos-animate" list-style="default" data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="1200">IMAI, C. <em>et al</em>. Tropical influenza and weather variability among children in an urban low-income population in Bangladesh. <strong>Global Health Action</strong>, v. 7, n. 1, 2014. <a href='https://doi.org/10.3402/gha.v7.24413' target='_blank' rel="noopener noreferrer">https://doi.org/10.3402/gha.v7.24413</a></li>

												<li class="list-group-item aos-init aos-animate" list-style="default" data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="1200">CERQUEIRA-SILVA, Thiago; CARDIM, Luciana L.; PAIXÃO, Enny; ROSSI, Marta; SANTOS, Andreia Costa;<em>et al</em>. Hospitalisation, mortality and years of life lost among chikungunya and dengue cases in Brazil: a nationwide cohort study, 2015–2024. <strong>The Lancet Regional Health – Americas</strong>, [S. l.], v. 49, p. 101177, set. 2025.  <a href='https://www.sciencedirect.com/science/article/pii/S2667193X25001875' target='_blank' rel="noopener noreferrer">https://www.sciencedirect.com/science/article/pii/S2667193X25001875</a> </li>


											</ul>

											<p><strong>Websites</strong></p>

											<ul class="list-group">
												<li class="list-group-item aos-init aos-animate" list-style="default" data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="1200">DATA VIZ PROJECT. Disponível em: <a href='https://datavizproject.com/' target='_blank' rel="noopener noreferrer">https://datavizproject.com/</a></li>

												<li class="list-group-item aos-init aos-animate" list-style="default" data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="1200">THE DATA visualisation catalogue. <strong>Data Viz Project</strong>. Disponível em: <a href='https://datavizcatalogue.com/' target='_blank' rel="noopener noreferrer">https://datavizcatalogue.com/</a>.</li>

												<li class="list-group-item aos-init aos-animate" list-style="default" data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="1200">FLOURISH. How to choose the right chart type for your data. Disponível em: <a href='https://flourish.studio/blog/choosing-the-right-visualisation/' target='_blank' rel="noopener noreferrer">https://flourish.studio/blog/choosing-the-right-visualisation/</a></li>
											</ul>
										</div>
									</div>
								</div>
							</div>
						</div>
						<!-- Fim do Accordion -->
					</div>
				</div>
			</div>
		`,
	},
	bibliografiaMod3: {
		ariaLabel: "bibliografiaMod3",
		modalSize: "modal-xl",
		modalTitle: "Bibliografia Módulo 3",
		modalBody: `
			<div class="row justify-content-center pt-5">
				<div class="col-12 col-md-11">
					<div class="mb-5">
						<!-- Accordion -->
						<div class="accordion accordion-flush" id="accordionExample2">
							<div class="accordion-item">
								<h5 class="accordion-header" id="heading1-item1">
									<button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapse1-item1" aria-expanded="true" aria-controls="collapse1-item1">Aula 1</button>
								</h5>
								<div id="collapse1-item1" class="accordion-collapse collapse" aria-labelledby="heading1-item1" data-bs-parent="">
									<div class="accordion-body">
										<div class="list">
											<ul class="list-group">
												<li class="list-group-item aos-init aos-animate" list-style='default' data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="1200">BRASIL. Ministério da Saúde. <strong>A experiência brasileira em sistemas de informação em saúde</strong>. Brasília, DF: Editora do MS, 2009. v. 2. (Série B. Textos Básicos de Saúde).</li>

												<li class="list-group-item aos-init aos-animate" list-style='default' data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="1200">BRASIL. Ministério da Saúde. <strong>Dados para vigilância: perfis das bases de dados produzidas pela Vigilância em Saúde no Brasil</strong>. Brasília, DF: MS, 2023.</li>

												<li class="list-group-item aos-init aos-animate" list-style='default' data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="1200">BRASIL. Ministério da Saúde. <strong>Estatísticas de mortalidade: Brasil 1980</strong>. Brasília, DF: Centro de Documentação do MS, 1983.</li>

												<li class="list-group-item aos-init aos-animate" list-style='default' data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="1200">BRASIL. Ministério da Saúde. Secretaria de Vigilância em Saúde. Departamento de Análise de Saúde e Vigilância de Doenças Não Transmissíveis. <strong>Declaração de óbito: manual de instruções para preenchimento</strong>. Brasília, DF: MS, 2022a. 67 p. il.</li>

												<li class="list-group-item aos-init aos-animate" list-style='default' data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="1200">BRASIL. Ministério da Saúde. Secretaria de Vigilância em Saúde. Departamento de Análise Epidemiológica e Vigilância de Doenças Não Transmissíveis. <strong>Declaração de nascido vivo: manual de instruções para preenchimento</strong>. 4. ed. Brasília, DF: MS, 2022b.</li>

												<li class="list-group-item aos-init aos-animate" list-style='default' data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="1200">JORGE, M. H. P. de M.; LAURENTI, R.; GOTLIEB, S. L. D. Análise da qualidade das estatísticas vitais brasileiras: a experiência de implantação do SIM e do SINASC. <strong>Ciência &amp; Saúde Coletiva</strong>, v. 12, n. 3, p. 643-654, 2007. Disponível em: <a href='https://doi.org/10.1590/S1413-81232007000300014' target='_blank' rel="noopener noreferrer">https://doi.org/10.1590/S1413-81232007000300014</a>. Acesso em: 6 dez. 2025.</li>

												<li class="list-group-item aos-init aos-animate" list-style='default' data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="1200">MORAIS, R. M. de; COSTA, A. L. Uma avaliação do Sistema de Informação sobre Mortalidade. <strong>Saúde em Debate</strong>, Rio de Janeiro, v. 41, n. esp., p. 101-117, 2017. Disponível em: <a href='https://doi.org/10.1590/0103-11042017S09' target='_blank' rel="noopener noreferrer">https://doi.org/10.1590/0103-11042017S09</a>. Acesso em: 6 dez. 2025.</li>

												<li class="list-group-item aos-init aos-animate" list-style='default' data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="1200">PEDRAZA, D. F. Sistema de informações sobre nascidos vivos: uma análise da qualidade com base na literatura. <strong>Cadernos de Saúde Coletiva</strong>, v. 29, n. 1, p. 143-152, jan. 2021. Disponível em: <a href='https://doi.org/10.1590/1414-462X202129010106' target='_blank' rel="noopener noreferrer">https://doi.org/10.1590/1414-462X202129010106</a>. Acesso em: 6 dez. 2025.</li>

												<li class="list-group-item aos-init aos-animate" list-style='default' data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="1200">PELISSARI, M. CNES como instrumento de gestão e sua importância no planejamento das ações em saúde. <strong>Revista de Saúde Pública do Paraná</strong>, v. 2, n. 1, p. 159-165, 2019. Disponível em: <a href='http://revista.escoladesaude.pr.gov.br/index.php/rspp/article/view/210' target='_blank' rel="noopener noreferrer">http://revista.escoladesaude.pr.gov.br/index.php/rspp/article/view/210</a>. Acesso em: 9 jul. 2024.</li>

												<li class="list-group-item aos-init aos-animate" list-style='default' data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="1200">ROCHA, T. A. H. <em>et al</em>. Cadastro Nacional de Estabelecimentos de Saúde: evidências sobre a confiabilidade de dados. <strong>Ciência &amp; Saúde Coletiva</strong>, v. 23, n. 1, p. 229-240, 2018.</li>

												<li class="list-group-item aos-init aos-animate" list-style='default' data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="1200">SZWARCWALD, C. L. <em>et al</em>. Busca ativa de óbitos e nascimentos no Nordeste e na Amazônia Legal: estimação das coberturas do SIM e do SINASC nos municípios brasileiros. <em>In:</em> BRASIL. Ministério da Saúde. Secretaria de Vigilância em Saúde. Departamento de Análise de Situação em Saúde. <strong>Saúde Brasil 2010: uma análise da situação de saúde e de evidências selecionadas de impacto de ações de vigilância em saúde</strong>. Brasília, DF: MS, 2011. p. 79-98.</li>

											</ul>
										</div>
									</div>
								</div>
							</div>

							<div class="accordion-item">
								<h5 class="accordion-header" id="heading1-item2">
									<button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapse1-item2" aria-expanded="false" aria-controls="collapse1-item2">Aula 2</button>
								</h5>
								<div id="collapse1-item2" class="accordion-collapse collapse" aria-labelledby="heading1-item2" data-bs-parent="">
									<div class="accordion-body">
										<div class="list">
											<ul class="list-group">
												<li class="list-group-item aos-init aos-animate" list-style='default' data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="1200">BITTENCOURT, S. A.; CAMACHO, L. A. B.; LEAL, M. do C. O Sistema de Informação Hospitalar e sua aplicação na saúde coletiva. <strong>Cadernos de Saúde Pública</strong>, Rio de Janeiro, v. 22, p. 19-30, jan. 2006.</li>

												<li class="list-group-item aos-init aos-animate" list-style='default' data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="1200">BRASIL. Ministério da Saúde. <strong>Manual técnico do Sistema de Informação Hospitalar</strong>. Brasília, DF: MS, 2007.</li>

												<li class="list-group-item aos-init aos-animate" list-style='default' data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="1200">BRASIL. Ministério da Saúde. <strong>Manual técnico operacional SIA/SUS: sistema de informações ambulatoriais</strong>. Aplicativos auxiliares e de captação da produção ambulatorial: APAC Magnético, BPA Magnético, Versia, De-Para, FPO Magnético. Brasília, DF: MS, [s. d.].</li>

												<li class="list-group-item aos-init aos-animate" list-style='default' data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="1200">BRASIL. Ministério da Saúde. <strong>O que é o e-SUS APS?</strong> Brasília, DF: MS, [s. d.]. Disponível em: <a href='https://sisaps.saude.gov.br/sistemas/esusaps/' target='_blank' rel='noopener noreferrer'>https://sisaps.saude.gov.br/sistemas/esusaps/</a>. Acesso em: 12 dez. 2025.</li>

												<li class="list-group-item aos-init aos-animate" list-style='default' data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="1200">COELHO, G. C.; ANDREAZZA, R.; CHIORO, A. Integração entre os sistemas nacionais de informação em saúde: o caso do e-SUS Atenção Básica. <strong>Revista de Saúde Pública</strong>, São Paulo, v. 55, e000000, 2021. Disponível em: <a href='https://doi.org/' target='_blank' rel='noopener noreferrer'>https://doi.org/</a>. Acesso em: 12 dez. 2025.</li>

												<li class="list-group-item aos-init aos-animate" list-style='default' data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="1200">LEVCOVITZ, E.; PEREIRA, T. R. C. SIH/SUS (Sistema AIH): uma análise do sistema público de remuneração de internações hospitalares no Brasil – 1983–1991. <em>In:</em> LEVCOVITZ, E.; PEREIRA, T. R. C. SIH/SUS (Sistema AIH): uma análise do sistema público de remuneração de internações hospitalares no Brasil – 1983-1991. [S. l.: s. n.], [1991]. p. 83.</li>

												<li class="list-group-item aos-init aos-animate" list-style='default' data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="1200">LOPES, S. P. A. <em>et al</em>. Evolução dos cadastros individuais no SISAB a partir do novo financiamento da Atenção Básica: um estudo descritivo. SciELO Preprints, 2021. Disponível em: <a href='https://preprints.scielo.org/index.php/scielo/preprint/view/2135' target='_blank' rel='noopener noreferrer'>https://preprints.scielo.org/index.php/scielo/preprint/view/2135</a>. Acesso em: 12 dez. 2025.</li>

												<li class="list-group-item aos-init aos-animate" list-style='default' data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="1200">MARQUES, J. A. <em>et al</em>. Avaliação da cobertura de registro de partos no Sistema de Informação Hospitalar do Sistema Único de Saúde, segundo hospital de internação, Brasil, 2012-2020. <strong>Cadernos de Saúde Pública</strong>, Rio de Janeiro, v. 40, e00225623, 2025. Disponível em: <a href='https://doi.org/' target='_blank' rel='noopener noreferrer'>https://doi.org/</a>. Acesso em: 12 dez. 2025.</li>

												<li class="list-group-item aos-init aos-animate" list-style='default' data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="1200">MUZY, J. (org.). Fontes de informações para indicadores em saúde. <em>In:</em> MUZY, J. <strong>Informação e indicadores: conceitos, fontes e aplicações para a saúde do idoso e envelhecimento</strong>. Rio de Janeiro: Edições Livres, 2021. p. 23-41.</li>

												<li class="list-group-item aos-init aos-animate" list-style='default' data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="1200">MUZY, J. <em>et al</em>. Oferta e demanda de procedimentos atribuíveis ao diabetes mellitus e suas complicações no Brasil. <strong>Ciência &amp; Saúde Coletiva</strong>, v. 27, p. 1653-1667, 2022. Disponível em: <a href='https://doi.org/' target='_blank' rel='noopener noreferrer'>https://doi.org/</a>. Acesso em: 12 dez. 2025.</li>

												<li class="list-group-item aos-init aos-animate" list-style='default' data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="1200">OLIVEIRA JUNIOR, J. G. de. Subutilização, limites e potencialidades do Sistema de Informação em Saúde para a Atenção Básica (SISAB). <strong>Asklepion – Informação em Saúde</strong>, v. 2, n. 2, p. 52-70, 2023.</li>

												<li class="list-group-item aos-init aos-animate" list-style='default' data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="1200">OLIVEIRA, M. R. de <em>et al</em>. Avaliação da completude do quesito raça/cor nos Sistemas Nacionais de Informação em Saúde no município do Recife. <strong>Brazilian Journal of Health Review</strong>, v. 8, n. 1, e76791, 2025. Disponível em: <a href='https://doi.org/' target='_blank' rel='noopener noreferrer'>https://doi.org/</a>. Acesso em: 12 dez. 2025.</li>

												<li class="list-group-item aos-init aos-animate" list-style='default' data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="1200">ORGANIZAÇÃO MUNDIAL DA SAÚDE. <strong>CID-10: classificação estatística internacional de doenças e problemas relacionados à saúde</strong>. São Paulo: Edusp, 1999.</li>

											</ul>
										</div>
									</div>
								</div>
							</div>

							<div class="accordion-item">
								<h5 class="accordion-header" id="heading1-item3">
									<button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapse1-item3" aria-expanded="false" aria-controls="collapse1-item3">Aula 3</button>
								</h5>
								<div id="collapse1-item3" class="accordion-collapse collapse" aria-labelledby="heading1-item3" data-bs-parent="">
									<div class="accordion-body">
										<div class="list">
											<ul class="list-group">
												<li class="list-group-item aos-init aos-animate" list-style='default' data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="1200">BRASIL. Ministério da Saúde. <strong>Guia de Vigilância em Saúde</strong>. 6. ed. Brasília, DF: MS, 2024. v. 3.</li>

												<li class="list-group-item aos-init aos-animate" list-style='default' data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="1200">BRASIL. Ministério da Saúde. <strong>Sistema de Informação de Agravos de Notificação (SINAN): normas e rotinas</strong>. 2. ed. Brasília, DF: Editora do Ministério da Saúde, 2007.</li>

												<li class="list-group-item aos-init aos-animate" list-style='default' data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="1200">FERRAZ, V. C. de A. B. <em>et al</em>. Painéis de monitoramento de dados epidemiológicos como estratégia de gestão da vigilância e da atenção à saúde. <strong>Ciência &amp; Saúde Coletiva</strong>, v. 29, e04142024, 2024. Disponível em: <a href='https://doi.org/' target='_blank' rel='noopener noreferrer'>https://doi.org/</a>. Acesso em: 12 dez. 2025.</li>

												<li class="list-group-item aos-init aos-animate" list-style='default' data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="1200">GERALDO, E. C. <em>et al</em>. Análise comparativa da evolução da completude dos dados de coqueluche nas cinco regiões brasileiras: período 2007-2020. <strong>Revista Interdisciplinar de Saúde e Educação</strong>, v. 5, n. 1, p. 125-146, 2024.</li>

												<li class="list-group-item aos-init aos-animate" list-style='default' data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="1200">LIMA, A. M. de; CORRÊA, A. P. de V.; UEHARA, S. C. da S. A. Influência dos indicadores socioeconômicos na distribuição dos casos suspeitos de dengue no município de São Carlos-SP. <strong>Physis – Revista de Saúde Coletiva</strong>, v. 34, e34009, 2024. Acesso em: 12 dez. 2025.</li>

												<li class="list-group-item aos-init aos-animate" list-style='default' data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="1200">MELO, M. A. de S. <em>et al</em>. Subnotificação no SINAN e fatores gerenciais e operacionais associados: revisão sistemática da literatura. <strong>Revista de Administração da UEG</strong>, v. 9, n. 1, p. 26, 2018.</li>

												<li class="list-group-item aos-init aos-animate" list-style='default' data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="1200">MIRANDA, C. B. D.; GARCIA, K. K. S. Perspectivas da Vigilância em Saúde do Trabalhador diante do Programa e-SUS Linha da Vida. <strong>Epidemiologia e Serviços de Saúde</strong>, Brasília, DF, v. 32, n. 4, e20231171, 2023. Disponível em: <a href='https://doi.org/' target='_blank' rel='noopener noreferrer'>https://doi.org/</a>. Acesso em: 12 dez. 2025.</li>

												<li class="list-group-item aos-init aos-animate" list-style='default' data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="1200">PAIVA, M. F. da C. M. de; FONSECA, S. C. Sífilis congênita no município do Rio de Janeiro, 2016-2020: perfil epidemiológico e completude dos registros. <strong>Medicina</strong>. Ribeirão Preto, v. 56, n. 1, e198451, 2023.</li>

												<li class="list-group-item aos-init aos-animate" list-style='default' data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="1200">SILVA, M. T.; GALVÃO, T. F. Incidência de tuberculose no Brasil: análise de série temporal entre 2001 e 2021 e projeção até 2030. <strong>Revista Brasileira de Epidemiologia</strong>, v. 27, e240027, 2024. Disponível em: <a href='https://doi.org/' target='_blank' rel='noopener noreferrer'>https://doi.org/</a>. Acesso em: 12 dez. 2025.</li>

												<li class="list-group-item aos-init aos-animate" list-style='default' data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="1200">SILVA, T. F. P. de L. A. da <em>et al</em>. Tendências na incidência e letalidade da dengue: análise de séries temporais interrompida, Brasil, 2001-2022. <strong>Epidemiologia e Serviços de Saúde</strong>, v. 34, e20240424, 2025.</li>

												<li class="list-group-item aos-init aos-animate" list-style='default' data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="1200">VÉRAS, G. C. B. <em>et al</em>. Perfil epidemiológico e distribuição espacial dos casos de hanseníase na Paraíba. <strong>Cadernos de Saúde Coletiva</strong>, v. 31, e31020488, 2023. Acesso em: 12 dez. 2025.</li>

												<li class="list-group-item aos-init aos-animate" list-style='default' data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="1200">VILLELA, D. A. M.; GOMES, M. F. da C. O impacto da disponibilidade de dados e informação oportuna para a vigilância epidemiológica. <strong>Cadernos de Saúde Pública</strong>, v. 38, e00115122, 2022. Disponível em: <a href='https://doi.org/' target='_blank' rel='noopener noreferrer'>https://doi.org/</a>. Acesso em: 12 dez. 2025.</li>

												<li class="list-group-item aos-init aos-animate" list-style='default' data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="1200">XAVIER, D. R. <em>et al</em>. Avaliação da completude e oportunidade dos dados no Sistema de Informação de Agravos de Notificação (SINAN) para febre maculosa no estado de São Paulo, 2007–2017. <strong>Epidemiologia e Serviços de Saúde</strong>, v. 32, e2022416, 2023.</li>
											</ul>
										</div>
									</div>
								</div>
							</div>

							<div class="accordion-item">
								<h5 class="accordion-header" id="heading1-item4">
									<button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapse1-item4" aria-expanded="false" aria-controls="collapse1-item4">Aula 4</button>
								</h5>
								<div id="collapse1-item4" class="accordion-collapse collapse" aria-labelledby="heading1-item4" data-bs-parent="">
									<div class="accordion-body">
										<div class="list">
											<ul class="list-group">
												<li class="list-group-item aos-init aos-animate" list-style='default' data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="1200">BRASIL. Lei Complementar nº 141, de 13 de janeiro de 2012. Regulamenta os valores mínimos a serem aplicados anualmente em ações e serviços públicos de saúde. Brasília, DF: Pres. da Rep., 2012.</li>

												<li class="list-group-item aos-init aos-animate" list-style='default' data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="1200">BRASIL. Ministério da Saúde. CNES – Arquivos de microdados. Brasília, DF: DATASUS. Disponível em: <a href='https://cnes.datasus.gov.br/pages/downloads/arquivosBaseDados.jsp' target='_blank' rel='noopener noreferrer'>https://cnes.datasus.gov.br/pages/downloads/arquivosBaseDados.jsp</a>. Acesso em: 7 dez. 2025.</li>

												<li class="list-group-item aos-init aos-animate" list-style='default' data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="1200">BRASIL. Ministério da Saúde. ElastiCNES: plataforma de estatísticas do CNES. Disponível em: <a href='https://elasticnes.saude.gov.br' target='_blank' rel='noopener noreferrer'>https://elasticnes.saude.gov.br</a>. Acesso em: 11 dez. 2025.</li>

												<li class="list-group-item aos-init aos-animate" list-style='default' data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="1200">BRASIL. Ministério da Saúde. DATASUS. Informações de saúde (TABNET). Disponível em: <a href='https://datasus.saude.gov.br/informacoes-de-saude-tabnet/' target='_blank' rel='noopener noreferrer'>https://datasus.saude.gov.br/informacoes-de-saude-tabnet/</a>. Acesso em: 10 dez. 2025.</li>

												<li class="list-group-item aos-init aos-animate" list-style='default' data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="1200">BRASIL. Ministério da Saúde. Manual de preenchimento do Cadastro Nacional de Estabelecimentos de Saúde (CNES). Brasília, DF: Ministério da Saúde, 2006. Disponível em: <a href='https://cnes.saude.gov.br' target='_blank' rel='noopener noreferrer'>https://cnes.saude.gov.br</a>. Acesso em: 10 dez. 2025.</li>

												<li class="list-group-item aos-init aos-animate" list-style='default' data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="1200">BRASIL. Ministério da Saúde. Módulo de indicadores – SIOPS. Brasília, DF. Disponível em: <a href='https://www.gov.br/saude/pt-br/acesso-a-informacao/siops' target='_blank' rel='noopener noreferrer'>https://www.gov.br/saude/pt-br/acesso-a-informacao/siops</a>. Acesso em: 9 dez. 2025.</li>

												<li class="list-group-item aos-init aos-animate" list-style='default' data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="1200">BRASIL. Ministério da Saúde. Painéis estatísticos do CNES. Brasília, DF. Disponível em: <a href='https://datasus.saude.gov.br' target='_blank' rel='noopener noreferrer'>https://datasus.saude.gov.br</a>. Acesso em: 8 dez. 2025.</li>

												<li class="list-group-item aos-init aos-animate" list-style='default' data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="1200">BRASIL. Ministério da Saúde. Portaria de Consolidação nº 1, de 28 de setembro de 2017. Consolida as normas sobre direitos e deveres, organização e funcionamento do Sistema Único de Saúde (SUS). Brasília, DF: MS, 2017.</li>

												<li class="list-group-item aos-init aos-animate" list-style='default' data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="1200">BRASIL. Ministério da Saúde. Portaria nº 1.646, de 2 de outubro de 2015. Institui o Cadastro Nacional de Estabelecimentos de Saúde (CNES) como sistema oficial de cadastramento de estabelecimentos de saúde no país. Brasília, DF: MS, 2015.</li>

												<li class="list-group-item aos-init aos-animate" list-style='default' data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="1200">BRASIL. Ministério da Saúde. DATASUS. Sistema de Cadastro Nacional de Estabelecimentos de Saúde (SCNES). Brasília, DF. Disponível em: <a href='https://datasus.saude.gov.br' target='_blank' rel='noopener noreferrer'>https://datasus.saude.gov.br</a>. Acesso em: 12 dez. 2025.</li>

												<li class="list-group-item aos-init aos-animate" list-style='default' data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="1200">BRASIL. Ministério da Saúde. Sistema de Informações sobre Orçamentos Públicos em Saúde (SIOPS). Brasília, DF. Disponível em: <a href='https://www.gov.br/saude/pt-br/acesso-a-informacao/siops' target='_blank' rel='noopener noreferrer'>https://www.gov.br/saude/pt-br/acesso-a-informacao/siops</a>. Acesso em: 12 dez. 2025.</li>

												<li class="list-group-item aos-init aos-animate" list-style='default' data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="1200">BRASIL. Ministério da Saúde. Tabelas de domínio do Cadastro Nacional de Estabelecimentos de Saúde (CNES). Brasília, DF: DATASUS, 2019. Disponível em: <a href='https://cnes.datasus.gov.br' target='_blank' rel='noopener noreferrer'>https://cnes.datasus.gov.br</a>. Acesso em: 9 dez. 2025.</li>

												<li class="list-group-item aos-init aos-animate" list-style='default' data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="1200">BRASIL. Ministério da Saúde. Wiki do Cadastro Nacional de Estabelecimentos de Saúde (CNES). Disponível em: <a href='https://wiki.saude.gov.br/cnes/' target='_blank' rel='noopener noreferrer'>https://wiki.saude.gov.br/cnes/</a>. Acesso em: 8 dez. 2025.</li>

												<li class="list-group-item aos-init aos-animate" list-style='default' data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="1200">COELHO, V. S. P. <em>et al</em>. Transparência e qualidade da informação no CNES: uma análise da documentação e do processo de coleta de dados. Interface – Comunicação, Saúde, Educação, v. 28, p. 1-20, 2024. Disponível em: <a href='https://doi.org/10.1590/2358-289820241408383P' target='_blank' rel='noopener noreferrer'>https://doi.org/10.1590/2358-289820241408383P</a>. Acesso em: 10 dez. 2025.</li>

												<li class="list-group-item aos-init aos-animate" list-style='default' data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="1200">FELICIANO, M. <em>et al</em>. Avaliação da cobertura e completude de variáveis de Sistemas de Informação sobre orçamentos públicos em saúde. Saúde em Debate, Rio de Janeiro, v. 43, n. 121, 2019. Disponível em: <a href='https://doi.org/10.1590/0103-1104201912104' target='_blank' rel='noopener noreferrer'>https://doi.org/10.1590/0103-1104201912104</a>. Acesso em: 9 dez. 2025.</li>

												<li class="list-group-item aos-init aos-animate" list-style='default' data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="1200">HARTZ, Z. M. de A. (org.). <strong>Avaliação em saúde: dos modelos conceituais à prática na análise da implantação de programas</strong>. Rio de Janeiro: Editora Fiocruz, 1997. Disponível em: <a href='https://books.scielo.org/id/3zcft' target='_blank' rel='noopener noreferrer'>https://books.scielo.org/id/3zcft</a>. Acesso em: 9 dez. 2025.</li>

												<li class="list-group-item aos-init aos-animate" list-style='default' data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="1200">MEDEIROS, K. R. de <em>et al</em>. Bases de dados orçamentários e qualidade da informação: uma avaliação do Finanças do Brasil (FINBRA) e do Sistema de Informações sobre Orçamentos Públicos em Saúde (SIOPS). Revista de Administração Pública, Rio de Janeiro, v. 48, n. 5, p. 1113-1133, set./out. 2014. Disponível em: <a href='https://www.scielo.br/j/rap/a/J8PM8PNN5nXyvGKCHkw7sXF/' target='_blank' rel='noopener noreferrer'>https://www.scielo.br/j/rap/a/J8PM8PNN5nXyvGKCHkw7sXF/</a>. Acesso em: 12 dez. 2025.</li>

												<li class="list-group-item aos-init aos-animate" list-style='default' data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="1200">ROCHA, T. A. <em>et al</em>. Cadastro Nacional de Estabelecimentos de Saúde: evidências sobre a confiabilidade dos dados. Ciência &amp; Saúde Coletiva, Rio de Janeiro, v. 23, n. 1, p. 229-240, 2018. Disponível em: <a href='https://doi.org/10.1590/1413-81232018231.16672015' target='_blank' rel='noopener noreferrer'>https://doi.org/10.1590/1413-81232018231.16672015</a>. Acesso em: 11 dez. 2025.</li>

												<li class="list-group-item aos-init aos-animate" list-style='default' data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="1200">SILVA, M. Análise das deficiências do Cadastro Nacional de Estabelecimentos de Saúde (CNES) e proposta de soluções em sistemas de informação. 2021. Dissertação (Mestrado Profissional em Informática em Saúde) – Centro de Ciências da Saúde, Universidade Federal de Santa Catarina, Florianópolis, 2021. Disponível em: <a href='https://repositorio.ufsc.br/handle/123456789/229890' target='_blank' rel='noopener noreferrer'>https://repositorio.ufsc.br/handle/123456789/229890</a>. Acesso em: 12 dez. 2025.</li>
											</ul>
										</div>
									</div>
								</div>
							</div>

							<div class="accordion-item">
								<h5 class="accordion-header" id="heading1-item5">
									<button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapse1-item5" aria-expanded="false" aria-controls="collapse1-item5">Aula 5</button>
								</h5>
								<div id="collapse1-item5" class="accordion-collapse collapse" aria-labelledby="heading1-item5" data-bs-parent="">
									<div class="accordion-body">
										<div class="list">
											<ul class="list-group">
												<li class="list-group-item aos-init aos-animate" list-style='default' data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="1200">BRASIL. Ministério da Saúde. DATASUS. Informações de saúde (TABNET). Disponível em: <a href='https://datasus.saude.gov.br/informacoes-de-saude-tabnet/' target='_blank' rel='noopener noreferrer'>https://datasus.saude.gov.br/informacoes-de-saude-tabnet/</a>. Brasília, DF: MS, 2025. Acesso em: 10 nov. 2025.</li>

												<li class="list-group-item aos-init aos-animate" list-style='default' data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="1200">BRASIL. Ministério da Saúde. DATASUS. Transferência de arquivos. Disponível em: <a href='https://datasus.saude.gov.br/transferencia-de-arquivos/' target='_blank' rel='noopener noreferrer'>https://datasus.saude.gov.br/transferencia-de-arquivos/</a>. Brasília, DF: MS, 2025. Acesso em: 10 nov. 2025.</li>

												<li class="list-group-item aos-init aos-animate" list-style='default' data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="1200">BRASIL. Ministério da Saúde. DATASUS. TabWin: programa para Windows. Versão 4.1.5. Brasília, DF: MS, 2025. Disponível em: <a href='http://www2.datasus.gov.br/DATASUS/index.php?area=060805' target='_blank' rel='noopener noreferrer'>http://www2.datasus.gov.br/DATASUS/index.php?area=060805</a>. Acesso em: 10 nov. 2025.</li>

												<li class="list-group-item aos-init aos-animate" list-style='default' data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="1200">BRASIL. Ministério da Saúde. DATASUS. Tutorial TABNET. Brasília, DF: MS, 2020. Disponível em: <a href='https://datasus.saude.gov.br/wp-content/uploads/2020/02/Tutorial-TABNET-2020.pdf' target='_blank' rel='noopener noreferrer'>https://datasus.saude.gov.br/wp-content/uploads/2020/02/Tutorial-TABNET-2020.pdf</a>. Acesso em: 30 jan. 2026.</li>

												<li class="list-group-item aos-init aos-animate" list-style='default' data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="1200">DUARTE, E.; EBLE, L. J.; GARCIA, L. P. 30 anos do Sistema Único de Saúde. <em>Epidemiologia e Serviços de Saúde</em>, Brasília, DF, v. 27, n. 1, e00100018, 2018. Disponível em: <a href='https://www.scielo.br/j/ress/a/chVKtyVFqkm9PJyqNMsf5zx/' target='_blank' rel='noopener noreferrer'>https://www.scielo.br/j/ress/a/chVKtyVFqkm9PJyqNMsf5zx/</a>. Acesso em: 10 nov. 2025.</li>

												<li class="list-group-item aos-init aos-animate" list-style='default' data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="1200">FRANCO, J. L. F. Sistemas de informação: indicadores de saúde. São Paulo: UNA-SUS/UNIFESP, 2012. Disponível em: <a href='http://ares.unasus.gov.br/acervo/handle/ARES/177' target='_blank' rel='noopener noreferrer'>http://ares.unasus.gov.br/acervo/handle/ARES/177</a>. Acesso em: 10 nov. 2025.</li>

												<li class="list-group-item aos-init aos-animate" list-style='default' data-aos="fade-right" data-aos-easing="ease-out" data-aos-duration="1200">ORGANIZAÇÃO PAN-AMERICANA DA SAÚDE. Indicadores de saúde: elementos conceituais e práticos. Washington, DC: OPAS, 2018. Disponível em: <a href='https://iris.paho.org/handle/10665.2/49057' target='_blank' rel='noopener noreferrer'>https://iris.paho.org/handle/10665.2/49057</a>. Acesso em: 10 nov. 2025.</li>
											</ul>
										</div>
									</div>
								</div>
							</div>
						</div>
						<!-- Fim do Accordion -->
					</div>
				</div>
			</div>
		`,
	},
	autorMod1Aula1: {
		ariaLabel: "autorMod1Aula1",
		modalSize: "modal-xl",
		modalTitle: "Sobre os autores",
		modalBody: `
			<div class="row justify-content-center pt-5">
				<div class="col-12 col-md-10 col-lg-10">
					<div class="mb-5">
						<h5 class="mb-3">Uende Aparecida Figueiredo Gomes</h5>
						<p class="mb-0">Professora-pesquisadora do Departamento de Engenharia Sanitária e Ambiental da Escola de Engenharia da Universidade Federal de Minas Gerais (DESA/UFMG).</p>
					</div>

					<div class="mb-5">
						<h5 class="mb-3">Alexandre Pessoa Dias </h5>
						<p class="mb-0">Coordenador acadêmico do curso, professor-pesquisador da Escola Politécnica de Saúde Joaquim Venâncio da Fiocruz (ESPJV/Fiocruz).</p>
					</div>

				</div>
			</div>
		`,
	},
	glossario: {
		ariaLabel: "glossario",
		modalSize: "modal-lg",
		modalTitle: "Glossário",
		modalBody: `
			<div class="accordion accordion-flush" id="accordionExample2">
	<div class="accordion-item">
		<h2 class="accordion-header" id="heading1-c">
			<button class="accordion-button collapsed" type="button" data-bs-toggle="collapse"
				data-bs-target="#collapse1-c" aria-expanded="false" aria-controls="collapse1-c">C</button>
		</h2>
		<div id="collapse1-c" class="accordion-collapse collapse" aria-labelledby="heading1-c" data-bs-parent="">
			<div class="accordion-body">
				<div class="mb-5">
					<p class="mb-3"><strong>CIT</strong></p>
					<p><strong>Comissão Intergestores Tripartite:</strong> Um fórum de discussão e deliberação que reúne
						representantes do Ministério da Saúde, dos estados e dos municípios para tratar de temas
						relacionados ao SUS.</p>
				</div>
			</div>
		</div>
	</div>

	<div class="accordion-item">
		<h2 class="accordion-header" id="heading1-e">
			<button class="accordion-button collapsed" type="button" data-bs-toggle="collapse"
				data-bs-target="#collapse1-e" aria-expanded="false" aria-controls="collapse1-e">E</button>
		</h2>
		<div id="collapse1-e" class="accordion-collapse collapse" aria-labelledby="heading1-e" data-bs-parent="">
			<div class="accordion-body">
				<div class="mb-5">
					<p class="mb-3"><strong>ESD</strong></p>
					<p><strong>Estratégia de Saúde Digital:</strong> Iniciativa do Ministério da Saúde para promover a
						digitalização dos serviços de saúde no Brasil, com foco na integração de dados e no uso de
						tecnologias emergentes.</p>
				</div>
			</div>
		</div>
	</div>

	<div class="accordion-item">
		<h2 class="accordion-header" id="heading1-i">
			<button class="accordion-button collapsed" type="button" data-bs-toggle="collapse"
				data-bs-target="#collapse1-i" aria-expanded="false" aria-controls="collapse1-i">I</button>
		</h2>
		<div id="collapse1-i" class="accordion-collapse collapse" aria-labelledby="heading1-i" data-bs-parent="">
			<div class="accordion-body">
				<div class="mb-5">
					<p class="mb-3"><strong>IA</strong></p>
					<p>Inteligência Artificial: Tecnologia que simula processos de inteligência humana, utilizada na
						saúde para diagnósticos, previsão de surtos e personalização de tratamentos.</p>
				</div>

				<div class="mb-5">
					<p class="mb-3"><strong>IoT</strong></p>
					<p><strong>Internet das Coisas:</strong> Tecnologia que conecta objetos do dia a dia à internet,
						permitindo que eles coletem e compartilhem dados, sendo aplicada na saúde para monitoramento e
						gestão de dados clínicos.</p>
				</div>
			</div>
		</div>
	</div>

	<div class="accordion-item">
		<h2 class="accordion-header" id="heading1-o">
			<button class="accordion-button collapsed" type="button" data-bs-toggle="collapse"
				data-bs-target="#collapse1-o" aria-expanded="false" aria-controls="collapse1-o">O</button>
		</h2>
		<div id="collapse1-o" class="accordion-collapse collapse" aria-labelledby="heading1-o" data-bs-parent="">
			<div class="accordion-body">
				<div class="mb-5">
					<p class="mb-3"><strong>OMS</strong></p>
					<p><strong>Organização Mundial da Saúde:</strong> Agência especializada das Nações Unidas que
						coordena a saúde pública internacional e define normas e diretrizes globais para a saúde.</p>
				</div>
			</div>
		</div>
	</div>

	<div class="accordion-item">
		<h2 class="accordion-header" id="heading1-p">
			<button class="accordion-button collapsed" type="button" data-bs-toggle="collapse"
				data-bs-target="#collapse1-p" aria-expanded="false" aria-controls="collapse1-p">P</button>
		</h2>
		<div id="collapse1-p" class="accordion-collapse collapse" aria-labelledby="heading1-p" data-bs-parent="">
			<div class="accordion-body">
				<div class="mb-5">
					<p class="mb-3"><strong>PNIIS</strong></p>
					<p><strong>Política Nacional de Informação e Informática em Saúde:</strong> Política elaborada para
						consolidar as ações do SUS relacionadas à informação e tecnologia da informação em saúde, com
						diretrizes para os três níveis da federação.</p>
				</div>
			</div>
		</div>
	</div>

	<div class="accordion-item">
		<h2 class="accordion-header" id="heading1-r">
			<button class="accordion-button collapsed" type="button" data-bs-toggle="collapse"
				data-bs-target="#collapse1-r" aria-expanded="false" aria-controls="collapse1-r">R</button>
		</h2>
		<div id="collapse1-r" class="accordion-collapse collapse" aria-labelledby="heading1-r" data-bs-parent="">
			<div class="accordion-body">
				<div class="mb-5">
					<p class="mb-3"><strong>RNDS</strong></p>
					<p><strong>Rede Nacional de Dados e Saúde:</strong> Plataforma de interoperabilidade do SUS que
						integra dados de saúde em todo o país, promovendo a conectividade entre as diferentes regiões.
					</p>
				</div>
			</div>
		</div>
	</div>

	<div class="accordion-item">
		<h2 class="accordion-header" id="heading1-s">
			<button class="accordion-button collapsed" type="button" data-bs-toggle="collapse"
				data-bs-target="#collapse1-s" aria-expanded="false" aria-controls="collapse1-s">S</button>
		</h2>
		<div id="collapse1-s" class="accordion-collapse collapse" aria-labelledby="heading1-s" data-bs-parent="">
			<div class="accordion-body">
				<div class="mb-5">
					<p class="mb-3"><strong>SNIS</strong></p>
					<p><strong>Sistema Nacional de Informações em Saúde:</strong> Um sistema proposto para organizar as
						informações em saúde no Brasil, gerido pelo Ministério da Saúde em parceria com estados e
						municípios.</p>
				</div>

				<div class="mb-5">
					<p class="mb-3"><strong>SUS</strong></p>
					<p><strong>Sistema Único de Saúde:</strong> O sistema de saúde pública do Brasil que visa garantir
						acesso universal, integral e gratuito aos serviços de saúde para toda a população.</p>
				</div>
			</div>
		</div>
	</div>

	<div class="accordion-item">
		<h2 class="accordion-header" id="heading1-t">
			<button class="accordion-button collapsed" type="button" data-bs-toggle="collapse"
				data-bs-target="#collapse1-t" aria-expanded="false" aria-controls="collapse1-t">T</button>
		</h2>
		<div id="collapse1-t" class="accordion-collapse collapse" aria-labelledby="heading1-t" data-bs-parent="">
			<div class="accordion-body">
				<p class="mb-3"><strong>TIC</strong></p>
				<p><strong>Tecnologias de Informação e Comunicação:</strong> Conjunto de tecnologias usadas para o
					processamento e comunicação de dados, fundamentais para a organização e gestão da informação em
					saúde.</p>
			</div>
		</div>
	</div>
</div>
		`,
	},
};

// Get all buttons and links that have "modal" in the data-bs-toggle
const modalButtons = document.querySelectorAll('[data-bs-toggle="modal"]');

document.addEventListener("DOMContentLoaded", function (event) {
	//do work

	modalButtons.forEach((btn) => {
		// Check if the modal exist
		const modalId = btn.getAttribute("data-bs-target").slice(1);
		const createdModalId = document.getElementById(modalId);
		const modalOrigin = btn.getAttribute("data-bs-target").slice(7);
		const hasPropriety = Object.hasOwn(modalInfos, modalOrigin);

		if (!createdModalId && hasPropriety) {
			// console.log('modalOrigin: ' + modalOrigin + ' hasPropriety: ' + hasPropriety);

			// If don't exist create one
			createModal(modalId);
		}
	});
});

function createModal(id) {
	const newModal = document.createElement("div");
	const modalLabel = id.slice(6);

	newModal.classList.add("modal", "fade");
	newModal.setAttribute("id", id);
	newModal.setAttribute("tabindex", "-1");
	newModal.setAttribute("aria-labelledby", modalLabel);
	newModal.setAttribute("aria-hidden", "true");

	newModal.innerHTML = `
		<div class="modal-dialog ${modalInfos[modalLabel].modalSize}">
			<div class="modal-content">
				<div class="modal-header">
					<h5 class="modal-title" id="${modalInfos[modalLabel].ariaLabel}">${modalInfos[modalLabel].modalTitle}</h5>
					<button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
				</div>
				<div class="modal-body">
					${modalInfos[modalLabel].modalBody}
				</div>
				<div class="modal-footer">
					<button type="button" class="fio-button fio-button-primary" data-bs-dismiss="modal">Fechar</button>
				</div>
			</div>
		</div>
	`;

	document.body.appendChild(newModal);
}

//Before and after
const container = document.querySelector(".antes-e-depois--container");
document.querySelector(".antes-e-depois--slider").addEventListener("input", (e) => {
	container.style.setProperty("--position", `${e.target.value}%`);
});
