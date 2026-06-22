import os

filepath = '/Users/iuryphilipylins/Documents/Antigravity/Bruno Noronha - Mentoria/index.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Fonts
content = content.replace(
    '<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;0,600;1,300;1,400&family=Montserrat:wght@300;400;500;600;700&display=swap" rel="stylesheet">',
    '<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">'
)
content = content.replace(
    "    --font-display: 'Cormorant Garamond', Georgia, serif;",
    "    --font-display: 'Inter', ui-sans-serif, system-ui, sans-serif;"
)
content = content.replace(
    "    --font-body: 'Montserrat', sans-serif;",
    "    --font-body: 'Inter', ui-sans-serif, system-ui, sans-serif;"
)

# 2. Update rounded borders & glassmorphism (Alta Office style)
content = content.replace(
    """  .dor-card {
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(180,157,106,0.2);
    border-left: 3px solid var(--gold);
    padding: 20px 24px;
    transition: background 0.3s;
  }""",
    """  .dor-card {
    background: linear-gradient(145deg, rgba(255, 255, 255, 0.05), rgba(255, 255, 255, 0.01));
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    border: 1px solid rgba(180,157,106,0.2);
    border-left: 3px solid var(--gold);
    border-radius: 20px;
    padding: 20px 24px;
    transition: all 0.3s;
    box-shadow: 0 10px 30px rgba(0,0,0,0.15);
  }"""
)

content = content.replace(
    """  .diferencial-card {
    background: var(--cream);
    border: 1px solid rgba(180,157,106,0.2);
    padding: 40px 36px;
    position: relative;
    transition: all 0.3s;
  }""",
    """  .diferencial-card {
    background: rgba(255, 255, 255, 0.6);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    border: 1px solid rgba(180,157,106,0.2);
    border-radius: 24px;
    padding: 40px 36px;
    position: relative;
    transition: all 0.3s;
    box-shadow: 0 10px 40px rgba(0,0,0,0.05);
  }"""
)

content = content.replace(
    """  .diferencial-card.destaque {
    background: #0B1038;
    border-color: var(--gold);
    grid-column: 1 / -1;
  }""",
    """  .diferencial-card.destaque {
    background: rgba(11, 16, 56, 0.95);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    border-radius: 24px;
    border-color: var(--gold);
    grid-column: 1 / -1;
  }"""
)

content = content.replace(
    """  .pilares-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 2px;
    background: var(--cream-dark);
  }""",
    """  .pilares-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 16px;
    background: transparent;
  }"""
)

content = content.replace(
    """  .pilar {
    background: var(--cream);
    padding: 48px 36px;
    position: relative;
    transition: background 0.3s;
  }""",
    """  .pilar {
    background: rgba(255, 255, 255, 0.6);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    border-radius: 24px;
    border: 1px solid rgba(180,157,106,0.1);
    padding: 48px 36px;
    position: relative;
    transition: all 0.3s;
    box-shadow: 0 10px 30px rgba(0,0,0,0.03);
  }"""
)

content = content.replace(
    """  .invest-card {
    background: #0B1038;
    border: 1px solid rgba(180,157,106,0.4);
    padding: 60px 48px;
    position: relative;
  }""",
    """  .invest-card {
    background: rgba(11, 16, 56, 0.95);
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    border: 1px solid rgba(180,157,106,0.4);
    border-radius: 28px;
    padding: 60px 48px;
    position: relative;
    box-shadow: 0 20px 60px rgba(180,157,106,0.1);
  }"""
)

# Mentor Image styling 
content = content.replace(
    """  .mentor-photo-frame {
    position: relative;
    background: #05081C;
    padding: 4px;
    border: 1px solid rgba(180,157,106,0.4);
  }""",
    """  .mentor-photo-frame {
    position: relative;
    background: #05081C;
    padding: 4px;
    border: 1px solid rgba(180,157,106,0.4);
    border-radius: 24px;
  }"""
)

content = content.replace(
    """  .mentor-photo-placeholder {
    width: 100%; aspect-ratio: 3/4;
    display: block;
    overflow: hidden;
    background: linear-gradient(135deg, #161E4D 0%, #0B1038 100%);
  }""",
    """  .mentor-photo-placeholder {
    width: 100%; aspect-ratio: 3/4;
    display: block;
    overflow: hidden;
    border-radius: 20px;
    background: linear-gradient(135deg, #161E4D 0%, #0B1038 100%);
  }"""
)

# 3. Update the button styles
content = content.replace(
    """  .btn-primary {
    display: inline-block;
    font-size: 12px; font-weight: 600;
    letter-spacing: 0.15em; text-transform: uppercase;
    color: #0B1038;
    background: var(--gold);
    padding: 18px 40px;
    text-decoration: none;
    transition: all 0.3s;
    position: relative;
  }
  .btn-primary::after {
    content: '';
    position: absolute; bottom: -4px; right: -4px;
    width: 100%; height: 100%;
    border: 1px solid var(--gold);
    transition: all 0.3s;
  }
  .btn-primary:hover { background: var(--gold-light); }
  .btn-primary:hover::after { bottom: -6px; right: -6px; }""",
    """  .btn-primary {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    font-size: 14px; font-weight: 600;
    letter-spacing: 0.08em; text-transform: uppercase;
    color: #0B1038;
    background: linear-gradient(135deg, #fff3d6, #D3BE8F 44%, #B49D6A);
    padding: 18px 40px;
    border-radius: 999px;
    text-decoration: none;
    transition: all 0.3s;
    position: relative;
    box-shadow: 0 0 34px rgba(180, 157, 106, 0.28);
  }
  .btn-primary:hover {
    box-shadow: 0 0 52px rgba(180, 157, 106, 0.42);
    transform: translateY(-2px);
  }"""
)


# 4. Copy updates

content = content.replace(
    """<h1 id="hero-title">
        Toda cirurgia oral que você encaminha 
        <em>é dinheiro — e autoridade — que você entrega para outro.</em>
      </h1>
      <p class="hero-subtext">
        A insegurança nas cirurgias orais não é falta de inteligência — é falta de <strong>método, anatomia e prática supervisionada.</strong> Isso tem solução.
      </p>""",
    """<h1 id="hero-title" style="font-size: clamp(36px, 4.5vw, 56px);">
        Aprenda a realizar cirurgias orais com <br><em>segurança e previsibilidade</em>
      </h1>
      <p class="hero-subtext" style="font-size: 16px;">
        Supervisão direta em pacientes reais.
      </p>
      
      <div style="display: flex; flex-direction: column; gap: 12px; margin-bottom: 40px;">
        <div style="display: flex; align-items: center; gap: 12px; color: #1a1a1a; font-weight: 500;"><span style="color: var(--gold); font-size: 18px;">✔</span> Atendimento individual</div>
        <div style="display: flex; align-items: center; gap: 12px; color: #1a1a1a; font-weight: 500;"><span style="color: var(--gold); font-size: 18px;">✔</span> Pacientes reais</div>
        <div style="display: flex; align-items: center; gap: 12px; color: #1a1a1a; font-weight: 500;"><span style="color: var(--gold); font-size: 18px;">✔</span> 6 meses de acompanhamento</div>
        <div style="display: flex; align-items: center; gap: 12px; color: #1a1a1a; font-weight: 500;"><span style="color: var(--gold); font-size: 18px;">✔</span> Protocolo baseado em evidência científica</div>
      </div>"""
)
content = content.replace("Quero Entender Mais", "Quero minha vaga")

content = content.replace(
    """<div class="dor-label">O diagnóstico honesto</div>
        <h2 class="dor-headline">Reconhece alguma dessas situações?</h2>
        <p class="dor-body">Você é dentista. Estudou anos. Mas quando o paciente senta na cadeira com uma indicação cirúrgica mais complexa, <strong>algo muda.</strong></p>
        <p class="dor-body">Uma hesitação. Uma dúvida. Um peso que faz você pensar em encaminhar — de novo — para o especialista. E isso custa: em <strong>receita, em autoridade e em autoconfiança.</strong></p>""",
    """<div class="dor-label">Para quem é a mentoria?</div>
        <h2 class="dor-headline" style="font-size: clamp(32px, 3.5vw, 42px);">Esta mentoria é para você que:</h2>
        <ul style="list-style: none; display: flex; flex-direction: column; gap: 16px; margin-bottom: 32px;">
            <li style="display: flex; align-items: flex-start; gap: 12px; color: rgba(255,255,255,0.9); font-size: 16px;"><span style="color: var(--gold); font-size: 18px;">✔</span> É clínico geral</li>
            <li style="display: flex; align-items: flex-start; gap: 12px; color: rgba(255,255,255,0.9); font-size: 16px;"><span style="color: var(--gold); font-size: 18px;">✔</span> Faz extrações simples</li>
            <li style="display: flex; align-items: flex-start; gap: 12px; color: rgba(255,255,255,0.9); font-size: 16px;"><span style="color: var(--gold); font-size: 18px;">✔</span> Quer realizar cirurgias complexas com mais segurança</li>
            <li style="display: flex; align-items: flex-start; gap: 12px; color: rgba(255,255,255,0.9); font-size: 16px;"><span style="color: var(--gold); font-size: 18px;">✔</span> Deseja aumentar seu faturamento sem depender de encaminhamentos</li>
        </ul>
        <div style="margin-top: 32px; padding: 24px; border: 1px solid rgba(180, 157, 106, 0.20); border-left: 3px solid var(--gold); background: linear-gradient(135deg, rgba(180, 157, 106, 0.10), rgba(255, 255, 255, 0.025)); border-radius: 18px; line-height: 1.68; color: var(--white);">
            <strong>A boa notícia:</strong> isso não é falta de capacidade. É falta de método, treinamento e supervisão. Na Mentoria VIP você aprende diretamente em pacientes reais, com acompanhamento individual.
        </div>"""
)

content = content.replace(
    """<div class="dor-cards">
        <div class="dor-card animate-on-scroll">
          <div class="dor-card-title">O encaminhamento que drena receita</div>
          <div class="dor-card-text">Cada procedimento cirúrgico que você encaminha é uma consulta, um procedimento e um paciente fidelizado que você entrega para outro profissional.</div>
        </div>
        <div class="dor-card animate-on-scroll">
          <div class="dor-card-title">O medo de complicação</div>
          <div class="dor-card-text">Parestesia, hemorragia, fratura óssea. Esses riscos existem — mas são gerenciáveis com protocolo correto e anatomia dominada.</div>
        </div>
        <div class="dor-card animate-on-scroll">
          <div class="dor-card-title">A técnica vista no papel, nunca na prática</div>
          <div class="dor-card-text">A faculdade ensinou a teoria. Mas nenhum professor colocou o afastador na sua mão e disse: "agora você faz."</div>
        </div>
        <div class="dor-card animate-on-scroll">
          <div class="dor-card-title">A sensação de estar ficando para trás</div>
          <div class="dor-card-text">Colegas ampliando o escopo clínico enquanto você ainda hesita nas cirurgias que deveriam ser rotina.</div>
        </div>
      </div>""",
    """<div class="dor-cards">
        <div style="margin-bottom: 8px; color: rgba(255,255,255,0.5); font-size: 12px; font-weight: 600; text-transform: uppercase; letter-spacing: 2px;">Você se identifica?</div>
        
        <div class="dor-card animate-on-scroll" style="display: flex; gap: 16px; align-items: center;">
          <div style="width: 40px; height: 40px; border-radius: 12px; border: 1px solid rgba(180,157,106,0.3); background: rgba(180,157,106,0.1); color: var(--gold); display: flex; align-items: center; justify-content: center; font-size: 20px; font-weight: 500;">?</div>
          <div class="dor-card-text" style="font-size: 16px; color: var(--white); font-weight: 500; margin: 0;">Encaminha casos por insegurança?</div>
        </div>
        
        <div class="dor-card animate-on-scroll" style="display: flex; gap: 16px; align-items: center;">
          <div style="width: 40px; height: 40px; border-radius: 12px; border: 1px solid rgba(180,157,106,0.3); background: rgba(180,157,106,0.1); color: var(--gold); display: flex; align-items: center; justify-content: center; font-size: 20px; font-weight: 500;">!</div>
          <div class="dor-card-text" style="font-size: 16px; color: var(--white); font-weight: 500; margin: 0;">Tem receio de complicações?</div>
        </div>
        
        <div class="dor-card animate-on-scroll" style="display: flex; gap: 16px; align-items: center;">
          <div style="width: 40px; height: 40px; border-radius: 12px; border: 1px solid rgba(180,157,106,0.3); background: rgba(180,157,106,0.1); color: var(--gold); display: flex; align-items: center; justify-content: center; font-size: 20px; font-weight: 500;">...</div>
          <div class="dor-card-text" style="font-size: 16px; color: var(--white); font-weight: 500; margin: 0;">Aprendeu a teoria, mas falta prática?</div>
        </div>
      </div>"""
)

# O que você vai aprender
content = content.replace(
    """<div class="pilares-grid">
      <div class="pilar animate-on-scroll">
        <div class="pilar-number">01</div>
        <div class="pilar-icon">
          <svg viewBox="0 0 24 24"><path d="M9 12h6M9 16h6M9 8h3M5 21h14a2 2 0 002-2V7l-5-5H5a2 2 0 00-2 2v15a2 2 0 002 2z"/></svg>
        </div>
        <div class="pilar-title">Protocolo Seguro</div>
        <div class="pilar-text">Cada etapa da cirurgia seguindo um protocolo construído com anos de experiência clínica e embasamento científico rigoroso. Sem modismos, sem achismo.</div>
      </div>
      <div class="pilar animate-on-scroll">
        <div class="pilar-number">02</div>
        <div class="pilar-icon">
          <svg viewBox="0 0 24 24"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
        </div>
        <div class="pilar-title">Anatomia como Fundação</div>
        <div class="pilar-text">Você vai entender o nervo alveolar inferior como nunca entendeu. Porque quem domina a anatomia, domina a cirurgia — e opera sem medo.</div>
      </div>
      <div class="pilar animate-on-scroll">
        <div class="pilar-number">03</div>
        <div class="pilar-icon">
          <svg viewBox="0 0 24 24"><path d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0"/></svg>
        </div>
        <div class="pilar-title">Prática com Paciente Real</div>
        <div class="pilar-text">Nada de manequim. Você opera em paciente real com o Dr. Bruno ao seu lado — corrigindo, orientando e transferindo segurança a cada gesto.</div>
      </div>
    </div>""",
    """<div class="pilares-grid" style="grid-template-columns: repeat(4, 1fr);">
      <div class="pilar animate-on-scroll" style="padding: 32px 24px; text-align: center; display: flex; flex-direction: column; align-items: center; justify-content: center;">
        <span style="color: var(--gold); font-size: 24px; margin-bottom: 12px;">✔</span>
        <div class="pilar-title" style="font-size: 16px;">Exodontias simples e complexas</div>
      </div>
      <div class="pilar animate-on-scroll" style="padding: 32px 24px; text-align: center; display: flex; flex-direction: column; align-items: center; justify-content: center;">
        <span style="color: var(--gold); font-size: 24px; margin-bottom: 12px;">✔</span>
        <div class="pilar-title" style="font-size: 16px;">Terceiros molares</div>
      </div>
      <div class="pilar animate-on-scroll" style="padding: 32px 24px; text-align: center; display: flex; flex-direction: column; align-items: center; justify-content: center;">
        <span style="color: var(--gold); font-size: 24px; margin-bottom: 12px;">✔</span>
        <div class="pilar-title" style="font-size: 16px;">Manejo de complicações</div>
      </div>
      <div class="pilar animate-on-scroll" style="padding: 32px 24px; text-align: center; display: flex; flex-direction: column; align-items: center; justify-content: center;">
        <span style="color: var(--gold); font-size: 24px; margin-bottom: 12px;">✔</span>
        <div class="pilar-title" style="font-size: 16px;">Planejamento cirúrgico</div>
      </div>
      <div class="pilar animate-on-scroll" style="padding: 32px 24px; text-align: center; display: flex; flex-direction: column; align-items: center; justify-content: center;">
        <span style="color: var(--gold); font-size: 24px; margin-bottom: 12px;">✔</span>
        <div class="pilar-title" style="font-size: 16px;">Anatomia aplicada</div>
      </div>
      <div class="pilar animate-on-scroll" style="padding: 32px 24px; text-align: center; display: flex; flex-direction: column; align-items: center; justify-content: center;">
        <span style="color: var(--gold); font-size: 24px; margin-bottom: 12px;">✔</span>
        <div class="pilar-title" style="font-size: 16px;">Prescrição medicamentosa</div>
      </div>
      <div class="pilar animate-on-scroll" style="padding: 32px 24px; text-align: center; display: flex; flex-direction: column; align-items: center; justify-content: center;">
        <span style="color: var(--gold); font-size: 24px; margin-bottom: 12px;">✔</span>
        <div class="pilar-title" style="font-size: 16px;">Suturas e fechamento</div>
      </div>
      <div class="pilar animate-on-scroll" style="padding: 32px 24px; text-align: center; display: flex; flex-direction: column; align-items: center; justify-content: center;">
        <span style="color: var(--gold); font-size: 24px; margin-bottom: 12px;">✔</span>
        <div class="pilar-title" style="font-size: 16px;">Protocolos clínicos</div>
      </div>
    </div>
    
    <style>
      @media(max-width: 768px) {
          .pilares-grid { grid-template-columns: repeat(2, 1fr) !important; }
      }
    </style>"""
)
content = content.replace(
    """<div class="section-label">A solução</div>
      <h2 class="section-title">Um método que transforma hesitação em maestria</h2>
      <p class="section-sub">Técnicas baseadas em anatomia, simplificadas com evidência científica — e praticadas em paciente real, ao seu lado.</p>""",
    """<div class="section-label">O que você vai aprender</div>
      <h2 class="section-title">Conteúdo Prático</h2>"""
)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
