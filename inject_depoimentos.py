with open("index.html", "r") as f:
    content = f.read()

# CSS Injection
css_code = """
  /* ---- DEPOIMENTOS ---- */
  .depoimentos-section {
    padding: 120px 0;
    background: var(--navy);
    border-top: 1px solid rgba(180,157,106,0.15);
    border-bottom: 1px solid rgba(180,157,106,0.15);
  }
  .depoimentos-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 24px;
    margin-top: 48px;
  }
  .depoimento-card {
    background: linear-gradient(145deg, rgba(255, 255, 255, 0.05), rgba(255, 255, 255, 0.01));
    border: 1px solid rgba(180,157,106, 0.2);
    border-radius: 20px;
    padding: 40px 32px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    transition: transform 0.3s ease, border-color 0.3s ease;
  }
  .depoimento-card:hover {
    transform: translateY(-4px);
    border-color: rgba(180,157,106, 0.5);
  }
  .depoimento-card .stars {
    color: var(--gold);
    font-size: 16px;
    letter-spacing: 0.1em;
    margin-bottom: 24px;
  }
  .depoimento-texto {
    color: rgba(255,255,255,0.8);
    font-size: 14.5px;
    line-height: 1.8;
    font-style: italic;
    margin-bottom: 32px;
  }
  .depoimento-autor strong {
    display: block;
    color: var(--white);
    font-size: 16px;
    font-weight: 500;
  }
  .depoimento-autor span {
    display: block;
    color: var(--gold-light);
    font-size: 12px;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    margin-top: 4px;
  }

  /* ---- RESPONSIVE ---- */
"""

content = content.replace("  /* ---- RESPONSIVE ---- */", css_code)

# Responsive CSS injection
responsive_css = """    .pilares-grid { grid-template-columns: 1fr; }
    .depoimentos-grid { grid-template-columns: 1fr; gap: 24px; }"""

content = content.replace("    .pilares-grid { grid-template-columns: 1fr; }", responsive_css)

# HTML Injection
html_code = """
<!-- DEPOIMENTOS -->
<section class="depoimentos-section">
  <div class="container">
    <div class="section-header animate-on-scroll">
      <div class="section-label" style="color: var(--gold); border-color: rgba(180,157,106,0.3); background: rgba(180,157,106,0.05);">A Voz dos Alunos</div>
      <h2 class="section-title" style="color: var(--white);">O Que Dizem os Mentorados</h2>
      <p class="section-sub" style="color: rgba(255,255,255,0.65);">Resultados reais de quem já transformou o medo da extração em previsibilidade clínica.</p>
    </div>
    
    <div class="depoimentos-grid animate-on-scroll">
      
      <!-- Card 1 -->
      <div class="depoimento-card">
        <div class="stars">★★★★★</div>
        <p class="depoimento-texto">"Eu morria de medo de pegar sisos retidos, sempre encaminhava. Depois de aplicar o método de rebatimento e osteotomia do Dr. Bruno, operei meu primeiro caso complexo na semana seguinte. Sensação de dever cumprido!"</p>
        <div class="depoimento-autor">
          <strong>Dr. Rafael Mendes</strong>
          <span>Cirurgião-Dentista</span>
        </div>
      </div>

      <!-- Card 2 -->
      <div class="depoimento-card">
        <div class="stars">★★★★★</div>
        <p class="depoimento-texto">"A mentoria me deu a confiança que faltava. A forma como a anatomia cirúrgica é destrinchada muda o jogo. Hoje o siso não é mais um problema, é uma fonte de renda previsível pro meu consultório."</p>
        <div class="depoimento-autor">
          <strong>Dra. Carolina Silva</strong>
          <span>Ortodontista</span>
        </div>
      </div>

      <!-- Card 3 -->
      <div class="depoimento-card">
        <div class="stars">★★★★★</div>
        <p class="depoimento-texto">"O suporte é impecável. As discussões de caso me ajudaram a montar planejamentos sem falhas. O investimento se pagou logo nos dois primeiros meses só com os pacientes que parei de encaminhar."</p>
        <div class="depoimento-autor">
          <strong>Dr. Felipe Castro</strong>
          <span>Clínico Geral</span>
        </div>
      </div>

    </div>
  </div>
</section>

<!-- INVESTIMENTO -->
"""

content = content.replace("<!-- INVESTIMENTO -->\n", html_code)

with open("index.html", "w") as f:
    f.write(content)

