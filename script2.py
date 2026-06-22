import re

filepath = '/Users/iuryphilipylins/Documents/Antigravity/Bruno Noronha - Mentoria/index.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Mentor Credentials
old_credentials = """        <div class="mentor-credentials">
          <div class="credential-item">
            <div class="credential-dot"></div>
            <div class="credential-text">Graduação em Odontologia</div>
          </div>
          <div class="credential-item">
            <div class="credential-dot"></div>
            <div class="credential-text">Residência em Cirurgia Bucomaxilofacial</div>
          </div>
          <div class="credential-item">
            <div class="credential-dot"></div>
            <div class="credential-text">Especialização em Implantes Dentários</div>
          </div>
          <div class="credential-item">
            <div class="credential-dot"></div>
            <div class="credential-text">Mestrado em Ciências Odontológicas</div>
          </div>
          <div class="credential-item">
            <div class="credential-dot"></div>
            <div class="credential-text">Pós-Graduação em Harmonização Orofacial</div>
          </div>
          <div class="credential-item">
            <div class="credential-dot"></div>
            <div class="credential-text">+7 anos de prática em cirurgia oral</div>
          </div>
        </div>"""

new_credentials = """        <div class="mentor-credentials">
          <div class="credential-item">
            <div class="credential-dot"></div>
            <div class="credential-text">Cirurgião Oral desde 2017</div>
          </div>
          <div class="credential-item">
            <div class="credential-dot"></div>
            <div class="credential-text">Residência em Cirurgia Bucomaxilofacial</div>
          </div>
          <div class="credential-item">
            <div class="credential-dot"></div>
            <div class="credential-text">Mestre em Ciências Odontológicas</div>
          </div>
          <div class="credential-item">
            <div class="credential-dot"></div>
            <div class="credential-text">Especialista em Implantes</div>
          </div>
          <div class="credential-item">
            <div class="credential-dot"></div>
            <div class="credential-text">Mais de 10 anos de experiência clínica</div>
          </div>
        </div>"""

content = content.replace(old_credentials, new_credentials)

# 2. Update Diferenciais Section
old_diferenciais = re.search(r'<!-- DIFERENCIAIS -->(.*?)<!-- DEPOIMENTOS -->', content, re.DOTALL)
if old_diferenciais:
    new_diferenciais = """<!-- DIFERENCIAIS -->
<section class="diferenciais-section" style="padding: 120px 0; background: var(--cream-dark);">
  <div class="container">
    <div class="section-header animate-on-scroll">
      <div class="section-label">O que torna essa mentoria diferente?</div>
      <h2 class="section-title">Acompanhamento e Prática Real</h2>
    </div>

    <div class="pilares-grid" style="grid-template-columns: repeat(3, 1fr);">
      <div class="pilar animate-on-scroll" style="padding: 32px 24px; text-align: center; display: flex; flex-direction: column; align-items: center; justify-content: center;">
        <span style="color: var(--gold); font-size: 24px; margin-bottom: 12px;">✔</span>
        <div class="pilar-title" style="font-size: 16px;">100% individual</div>
      </div>
      <div class="pilar animate-on-scroll" style="padding: 32px 24px; text-align: center; display: flex; flex-direction: column; align-items: center; justify-content: center;">
        <span style="color: var(--gold); font-size: 24px; margin-bottom: 12px;">✔</span>
        <div class="pilar-title" style="font-size: 16px;">Paciente real</div>
      </div>
      <div class="pilar animate-on-scroll" style="padding: 32px 24px; text-align: center; display: flex; flex-direction: column; align-items: center; justify-content: center;">
        <span style="color: var(--gold); font-size: 24px; margin-bottom: 12px;">✔</span>
        <div class="pilar-title" style="font-size: 16px;">Instrumental disponível</div>
      </div>
      <div class="pilar animate-on-scroll" style="padding: 32px 24px; text-align: center; display: flex; flex-direction: column; align-items: center; justify-content: center;">
        <span style="color: var(--gold); font-size: 24px; margin-bottom: 12px;">✔</span>
        <div class="pilar-title" style="font-size: 16px;">Discussão de casos</div>
      </div>
      <div class="pilar animate-on-scroll" style="padding: 32px 24px; text-align: center; display: flex; flex-direction: column; align-items: center; justify-content: center;">
        <span style="color: var(--gold); font-size: 24px; margin-bottom: 12px;">✔</span>
        <div class="pilar-title" style="font-size: 16px;">Suporte por 6 meses</div>
      </div>
      <div class="pilar animate-on-scroll" style="padding: 32px 24px; text-align: center; display: flex; flex-direction: column; align-items: center; justify-content: center;">
        <span style="color: var(--gold); font-size: 24px; margin-bottom: 12px;">✔</span>
        <div class="pilar-title" style="font-size: 16px;">Acompanhamento em cirurgias hospitalares</div>
      </div>
    </div>
  </div>
</section>

<!-- DEPOIMENTOS -->"""
    content = content.replace(old_diferenciais.group(0), new_diferenciais)

# 3. Add FAQ Section right before CTA FINAL
faq_section = """<!-- FAQ -->
<section class="faq-section" style="padding: 120px 0; background: var(--cream);">
  <div class="container">
    <div class="section-header animate-on-scroll" style="margin-bottom: 50px;">
      <div class="section-label">Dúvidas?</div>
      <h2 class="section-title">Perguntas Frequentes</h2>
    </div>
    <div class="faq-list animate-on-scroll" style="max-width: 800px; margin: 0 auto; display: flex; flex-direction: column; gap: 16px;">
      
      <details style="background: rgba(255, 255, 255, 0.6); backdrop-filter: blur(12px); border-radius: 20px; border: 1px solid rgba(180,157,106,0.2); padding: 24px 32px; cursor: pointer; transition: all 0.3s; box-shadow: 0 10px 30px rgba(0,0,0,0.03);">
        <summary style="font-weight: 600; font-size: 18px; color: #0B1038; list-style: none; display: flex; justify-content: space-between; align-items: center;">
          Isso é para mim? <span style="color: var(--gold);">+</span>
        </summary>
        <div style="margin-top: 16px; font-size: 15px; color: var(--text-mid); line-height: 1.8;">
          A mentoria é ideal para clínicos gerais que já realizam extrações simples e desejam dar o próximo passo para cirurgias complexas (como terceiros molares) com total segurança, parando de encaminhar pacientes por insegurança.
        </div>
      </details>
      
      <details style="background: rgba(255, 255, 255, 0.6); backdrop-filter: blur(12px); border-radius: 20px; border: 1px solid rgba(180,157,106,0.2); padding: 24px 32px; cursor: pointer; transition: all 0.3s; box-shadow: 0 10px 30px rgba(0,0,0,0.03);">
        <summary style="font-weight: 600; font-size: 18px; color: #0B1038; list-style: none; display: flex; justify-content: space-between; align-items: center;">
          O que vou aprender? <span style="color: var(--gold);">+</span>
        </summary>
        <div style="margin-top: 16px; font-size: 15px; color: var(--text-mid); line-height: 1.8;">
          Você dominará exodontias simples e complexas, extração de terceiros molares, manejo de complicações, planejamento cirúrgico minucioso, anatomia aplicada, prescrição medicamentosa, suturas e protocolos clínicos baseados em evidência.
        </div>
      </details>
      
      <details style="background: rgba(255, 255, 255, 0.6); backdrop-filter: blur(12px); border-radius: 20px; border: 1px solid rgba(180,157,106,0.2); padding: 24px 32px; cursor: pointer; transition: all 0.3s; box-shadow: 0 10px 30px rgba(0,0,0,0.03);">
        <summary style="font-weight: 600; font-size: 18px; color: #0B1038; list-style: none; display: flex; justify-content: space-between; align-items: center;">
          Quem vai me ensinar? <span style="color: var(--gold);">+</span>
        </summary>
        <div style="margin-top: 16px; font-size: 15px; color: var(--text-mid); line-height: 1.8;">
          O Dr. Bruno Noronha. Cirurgião Oral desde 2017, com Residência em Cirurgia Bucomaxilofacial, Mestrado em Ciências Odontológicas e mais de 10 anos de experiência clínica que será repassada diretamente para você, na prática.
        </div>
      </details>
      
      <details style="background: rgba(255, 255, 255, 0.6); backdrop-filter: blur(12px); border-radius: 20px; border: 1px solid rgba(180,157,106,0.2); padding: 24px 32px; cursor: pointer; transition: all 0.3s; box-shadow: 0 10px 30px rgba(0,0,0,0.03);">
        <summary style="font-weight: 600; font-size: 18px; color: #0B1038; list-style: none; display: flex; justify-content: space-between; align-items: center;">
          Quanto custa e como me inscrevo? <span style="color: var(--gold);">+</span>
        </summary>
        <div style="margin-top: 16px; font-size: 15px; color: var(--text-mid); line-height: 1.8;">
          O investimento é de R$ 4.500 à vista ou em até 12x de R$ 397,16. Para se inscrever, basta clicar em qualquer botão de "Garantir Minha Vaga" na página, falar diretamente com a equipe pelo WhatsApp e realizar o pagamento de reserva (R$ 250,00).
        </div>
      </details>
      
    </div>
  </div>
</section>

<!-- CTA FINAL -->"""

content = content.replace("<!-- CTA FINAL -->", faq_section)

# 4. Remove any existing default <details> styles to ensure it uses the inline styles smoothly
details_css = """
  details[open] summary ~ * {
    animation: sweep .5s ease-in-out;
  }
  @keyframes sweep {
    0%    {opacity: 0; margin-top: -10px}
    100%  {opacity: 1; margin-top: 16px}
  }
  summary::-webkit-details-marker {
    display: none;
  }
"""
content = content.replace("</style>", details_css + "\n</style>")


with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
