import re

with open("index.html", "r") as f:
    content = f.read()

# We will write a new CSS section and inject it.
new_css = """
  /* --- BASE AND VARS --- */
  *, *::before, *::after { margin: 0; padding: 0; box-sizing: border-box; }

  :root {
    --navy: #0B1038;
    --navy-mid: #161E4D;
    --gold: #B49D6A;
    --gold-light: #CABA94;
    --gold-pale: #E6E0D2;
    --cream: #E7E3DA;
    --cream-dark: #D9D4CB;
    --white: #FFFFFF;
    --text-dark: #0B1038;
    --text-mid: #2C3258;
    --text-muted: #6C739A;
    --font-display: 'Cormorant Garamond', Georgia, serif;
    --font-body: 'Montserrat', sans-serif;
  }

  html { scroll-behavior: smooth; }

  body {
    font-family: var(--font-body);
    background: var(--cream);
    color: var(--text-dark);
    overflow-x: hidden;
    font-size: 16px;
    line-height: 1.7;
  }

  /* --- ANIMATIONS --- */
  .char {
    display: inline-block;
    opacity: 0;
    transform: translateY(100%);
    clip-path: polygon(0 0, 100% 0, 100% 0, 0 0);
    transition: opacity 800ms cubic-bezier(0.16, 1, 0.3, 1), transform 800ms cubic-bezier(0.16, 1, 0.3, 1), clip-path 800ms cubic-bezier(0.16, 1, 0.3, 1);
  }
  .word { display: inline-block; white-space: nowrap; }
  .char.revealed {
    opacity: 1;
    transform: translateY(0);
    clip-path: polygon(0 0, 100% 0, 100% 100%, 0 100%);
  }
  .animate-on-scroll {
    opacity: 0.01;
    filter: blur(10px);
    transform: translateY(24px);
    transition: opacity 900ms cubic-bezier(0.25, 0.46, 0.45, 0.94), filter 900ms cubic-bezier(0.25, 0.46, 0.45, 0.94), transform 900ms cubic-bezier(0.25, 0.46, 0.45, 0.94);
  }
  .animate-on-scroll.in-view {
    opacity: 1;
    filter: blur(0);
    transform: translateY(0);
  }

  /* --- UTILITIES --- */
  .gold { color: var(--gold); }
  .serif { font-family: var(--font-display); }
  .container { max-width: 1180px; margin: 0 auto; padding: 0 32px; }

  /* --- NAV --- */
  nav {
    position: fixed; top: 0; left: 0; right: 0; z-index: 100;
    background: rgba(11,16,56,0.96);
    backdrop-filter: blur(12px);
    padding: 18px 32px;
    display: flex; justify-content: space-between; align-items: center;
    border-bottom: 1px solid rgba(180,157,106,0.3);
  }
  nav .brand {
    font-family: var(--font-display);
    font-size: 20px; font-weight: 500;
    color: var(--gold-light);
    letter-spacing: 0.04em;
  }
  nav .brand span { color: rgba(255,255,255,0.5); font-weight: 300; }
  .nav-cta {
    font-family: var(--font-body);
    font-size: 12px; font-weight: 600;
    letter-spacing: 0.12em; text-transform: uppercase;
    color: var(--navy);
    background: var(--gold);
    padding: 10px 24px;
    text-decoration: none;
    border-radius: 999px;
    transition: background 0.3s;
  }
  .nav-cta:hover { background: var(--gold-light); }

  /* --- HERO --- */
  .hero {
    min-height: 100vh;
    background: var(--navy);
    display: flex; align-items: center;
    position: relative;
    overflow: hidden;
    padding-top: 80px;
  }
  .hero-animation-grid {
    position: absolute; inset: 0; z-index: 0;
    display: grid; grid-template-columns: repeat(12, minmax(0, 1fr));
    pointer-events: none; opacity: 0.22;
  }
  .bg-column {
    min-height: 100%;
    border-right: 1px solid rgba(255, 255, 255, 0.08);
    background: linear-gradient(180deg, rgba(180,157,106, 0), rgba(180,157,106, 0.18), rgba(180,157,106, 0.10));
    clip-path: inset(100% 0 0 0);
    transition: clip-path 1500ms cubic-bezier(0.65, 0, 0.35, 1);
  }
  .bg-column.active { clip-path: inset(0 0 0 0); }
  .hero-content {
    position: relative; z-index: 2;
    max-width: 800px;
    padding: 80px 32px 80px 64px;
  }
  .hero-eyebrow {
    display: inline-flex; align-items: center; gap: 10px;
    color: var(--gold);
    border: 1px solid rgba(180,157,106, 0.22);
    background: rgba(180,157,106, 0.08);
    border-radius: 999px;
    padding: 8px 14px;
    font-size: 11px; font-weight: 700;
    letter-spacing: 0.25em; text-transform: uppercase;
    margin-bottom: 28px;
  }
  .hero h1 {
    font-family: var(--font-display);
    font-size: clamp(42px, 6vw, 78px);
    font-weight: 300; line-height: 1.1;
    color: var(--white);
    margin-bottom: 32px;
    letter-spacing: -0.01em;
  }
  .hero h1 em { font-style: italic; color: var(--gold-light); display: block; }
  .hero-subtext {
    font-size: 15px; font-weight: 300;
    color: rgba(255,255,255,0.65);
    max-width: 520px; margin-bottom: 48px; line-height: 1.8;
  }
  .hero-subtext strong { color: rgba(255,255,255,0.9); font-weight: 500; }
  .hero-actions { display: flex; align-items: center; gap: 32px; flex-wrap: wrap; }
  
  .btn-primary {
    position: relative; overflow: hidden; isolation: isolate;
    display: inline-flex; align-items: center; justify-content: center;
    border-radius: 999px; border: 1px solid rgba(180,157,106, 0.72);
    color: var(--navy); background: linear-gradient(135deg, var(--gold-light), var(--gold) 44%, #8A6E3B);
    padding: 16px 36px; font-size: 13px; font-weight: 650;
    letter-spacing: 0.15em; text-transform: uppercase;
    box-shadow: 0 0 34px rgba(180,157,106, 0.28);
    text-decoration: none; transition: transform 180ms ease, border-color 180ms ease, box-shadow 180ms ease;
  }
  .btn-primary:hover {
    transform: translateY(-2px); box-shadow: 0 0 52px rgba(180,157,106, 0.42);
  }
  .hero-trust { font-size: 12px; color: rgba(255,255,255,0.4); letter-spacing: 0.08em; }

  /* --- DOR --- */
  .dor-section {
    background: var(--navy-mid); padding: 100px 0; position: relative;
    border-bottom: 1px solid rgba(180,157,106,0.2);
  }
  .dor-inner { display: grid; grid-template-columns: minmax(0, 0.92fr) minmax(420px, 1.08fr); gap: 64px; align-items: center; }
  .dor-label {
    display: inline-flex; align-items: center; gap: 10px;
    color: var(--gold); border: 1px solid rgba(180,157,106, 0.22);
    background: rgba(180,157,106, 0.08); border-radius: 999px;
    padding: 8px 14px; font-size: 10px; font-weight: 700;
    letter-spacing: 0.3em; text-transform: uppercase; margin-bottom: 24px;
  }
  .dor-headline {
    font-family: var(--font-display); font-size: clamp(32px, 4vw, 52px);
    font-weight: 400; line-height: 1.2; color: var(--white); margin-bottom: 32px;
  }
  .dor-body { font-size: 15px; font-weight: 300; color: rgba(255,255,255,0.65); line-height: 1.9; margin-bottom: 20px; }
  .dor-body strong { color: rgba(255,255,255,0.9); font-weight: 500; }
  
  .pain-list { display: grid; gap: 16px; position: relative; }
  .pain-list::before {
    content: ""; position: absolute; left: 27px; top: 40px; bottom: 40px; width: 1px;
    background: linear-gradient(180deg, rgba(180,157,106, 0), rgba(180,157,106, 0.42), rgba(180,157,106, 0));
  }
  .pain {
    position: relative; display: grid; grid-template-columns: 54px 1fr; gap: 18px;
    min-height: 142px; padding: 24px; border: 1px solid rgba(255, 255, 255, 0.09);
    border-radius: 22px;
    background: linear-gradient(145deg, rgba(255, 255, 255, 0.075), rgba(255, 255, 255, 0.025)), var(--navy);
    box-shadow: 0 18px 80px rgba(0, 0, 0, 0.28);
    transition: transform 180ms ease, border-color 180ms ease, background 180ms ease;
  }
  .pain:hover {
    transform: translateX(6px); border-color: rgba(180,157,106, 0.28);
    background: linear-gradient(145deg, rgba(180,157,106, 0.10), rgba(255, 255, 255, 0.025)), var(--navy);
  }
  .pain-mark {
    width: 54px; height: 54px; display: grid; place-items: center; border-radius: 16px;
    border: 1px solid rgba(180,157,106, 0.24); background: rgba(180,157,106, 0.08);
    color: var(--gold-light); font-weight: 800; font-size: 13px; letter-spacing: 0.08em;
  }
  .pain p { color: rgba(255,255,255,0.6); font-size: 14px; line-height: 1.65; }
  .pain strong { display: block; margin-bottom: 5px; color: #fff; font-size: 1.08rem; line-height: 1.2; font-weight: 650; }

  /* --- SOLUCAO (PILLARS) --- */
  .solucao-section { padding: 120px 0; background: var(--cream); }
  .section-header { text-align: center; margin-bottom: 72px; }
  .section-label {
    display: inline-flex; align-items: center; gap: 10px;
    color: var(--navy); border: 1px solid rgba(11,16,56, 0.22);
    background: rgba(11,16,56, 0.08); border-radius: 999px;
    padding: 8px 14px; font-size: 10px; font-weight: 700;
    letter-spacing: 0.3em; text-transform: uppercase; margin-bottom: 20px;
  }
  .section-title {
    font-family: var(--font-display); font-size: clamp(36px, 4vw, 58px);
    font-weight: 300; line-height: 1.2; color: var(--navy); margin-bottom: 20px;
  }
  .section-sub { font-size: 15px; font-weight: 300; color: var(--text-mid); max-width: 540px; margin: 0 auto; line-height: 1.8; }
  
  .pillar-grid {
    display: grid; grid-template-columns: repeat(3, 1fr); gap: 1px;
    margin-top: 48px; overflow: hidden; border: 1px solid rgba(11,16,56, 0.1);
    border-radius: 24px; background: rgba(11,16,56, 0.1);
  }
  .pillar {
    position: relative; overflow: hidden; min-height: 310px;
    background: var(--cream); padding: 36px;
  }
  .pillar::before {
    content: ""; position: absolute; inset: 0; z-index: 2; pointer-events: none;
    border-radius: inherit; opacity: 0;
    background: radial-gradient(600px circle at var(--mouse-x, 50%) var(--mouse-y, 50%), rgba(180,157,106, 0.15), transparent 40%);
    transition: opacity 400ms ease;
  }
  .pillar:hover::before { opacity: 1; }
  .pillar-num { color: var(--gold); font-size: 12px; font-weight: 800; letter-spacing: 0.12em; text-transform: uppercase; }
  .pillar h3 { margin-top: 50px; font-family: var(--font-display); font-size: 1.8rem; line-height: 1; color: var(--navy); font-weight: 500; }
  .pillar p { margin-top: 14px; color: var(--text-mid); font-size: 14px; line-height: 1.7; }
  .pilar-icon {
    width: 48px; height: 48px; border: 1px solid var(--gold); display: flex; align-items: center; justify-content: center;
    border-radius: 12px; margin-top: 24px; background: rgba(180,157,106,0.05);
  }
  .pilar-icon svg { width: 22px; height: 22px; stroke: var(--gold); fill: none; stroke-width: 1.5; }

  /* --- MENTOR --- */
  .mentor-section {
    padding: 120px 0; background: var(--navy); position: relative; overflow: hidden;
    border-top: 1px solid rgba(180,157,106,0.2);
  }
  .mentor-section::after {
    content: 'BRUNO NORONHA'; position: absolute; bottom: -20px; right: -10px;
    font-family: var(--font-display); font-size: 120px; font-weight: 300;
    color: rgba(255,255,255,0.02); white-space: nowrap; line-height: 1; pointer-events: none;
  }
  .instructor-grid { display: grid; grid-template-columns: minmax(280px, 0.82fr) minmax(0, 1.18fr); gap: 64px; align-items: center; }
  .instructor-photo {
    position: relative; border: 1px solid rgba(180,157,106, 0.2); border-radius: 28px;
    overflow: hidden; background: var(--navy-mid); box-shadow: 0 30px 120px rgba(0, 0, 0, 0.44);
    aspect-ratio: 4/5; display: flex; align-items: center; justify-content: center;
  }
  .mentor-initials { font-family: var(--font-display); font-size: 80px; color: rgba(180,157,106,0.6); }
  .mentor-headline { font-family: var(--font-display); font-size: clamp(32px, 4vw, 50px); font-weight: 300; line-height: 1.2; color: var(--white); margin-top: 20px; }
  .mentor-headline em { font-style: italic; color: var(--gold-light); }
  .mentor-bio { display: grid; gap: 16px; margin-top: 28px; color: rgba(255,255,255,0.6); font-size: 15px; line-height: 1.8; }
  .mentor-bio strong { color: rgba(255,255,255,0.9); font-weight: 500; }
  .instructor-proof { display: grid; grid-template-columns: repeat(3, 1fr); gap: 12px; margin-top: 30px; }
  .instructor-proof div {
    min-height: 96px; padding: 16px; border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 18px; background: rgba(255, 255, 255, 0.035);
  }
  .instructor-proof strong { display: block; color: var(--gold); font-size: 1.45rem; font-family: var(--font-display); line-height: 1; font-weight: 600; }
  .instructor-proof span { display: block; margin-top: 9px; color: rgba(255,255,255,0.4); font-size: 12px; line-height: 1.35; text-transform: uppercase; letter-spacing: 0.05em; }

  /* --- DIFERENCIAIS (BENTO) --- */
  .diferenciais-section { padding: 120px 0; background: var(--cream-dark); }
  .bento { display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px; margin-top: 48px; }
  .card {
    position: relative; overflow: hidden; min-height: 260px;
    border: 1px solid rgba(11,16,56, 0.08); border-radius: 22px; padding: 28px;
    background: linear-gradient(145deg, rgba(255, 255, 255, 0.6), rgba(255, 255, 255, 0.1));
    transition: transform 180ms ease, border-color 180ms ease, background 180ms ease;
  }
  .card::before {
    content: ""; position: absolute; inset: 0; z-index: 2; pointer-events: none; border-radius: inherit; opacity: 0;
    background: radial-gradient(720px circle at var(--mouse-x, 50%) var(--mouse-y, 50%), rgba(180,157,106, 0.2), transparent 42%);
    transition: opacity 400ms ease;
  }
  .card:hover::before { opacity: 1; }
  .card:hover {
    transform: translateY(-5px); border-color: rgba(180,157,106, 0.4);
    background: linear-gradient(145deg, rgba(255,255,255,0.8), rgba(255,255,255,0.2));
  }
  .card.wide { grid-column: span 2; }
  .card.tall { min-height: 350px; }
  .card.destaque { background: var(--navy); border-color: var(--gold); grid-column: 1 / -1; }
  .card.destaque h3 { color: var(--white); }
  .card.destaque p { color: rgba(255,255,255,0.6); }
  .tag {
    display: inline-flex; align-items: center; border: 1px solid rgba(180,157,106, 0.3);
    color: var(--navy); background: rgba(180,157,106, 0.15); border-radius: 999px;
    padding: 5px 10px; font-size: 10px; font-weight: 800; letter-spacing: 0.1em; text-transform: uppercase;
  }
  .card.destaque .tag { color: var(--gold); border-color: rgba(180,157,106, 0.3); background: rgba(180,157,106, 0.1); }
  .card h3 { margin-top: 18px; max-width: 420px; font-family: var(--font-display); font-size: clamp(1.35rem, 2vw, 2rem); line-height: 1.08; color: var(--navy); }
  .card p { margin-top: 14px; color: var(--text-mid); font-size: 14px; line-height: 1.6; max-width: 520px; }

  /* --- INVESTIMENTO E PASSOS --- */
  .invest-section { padding: 120px 0; background: var(--cream); }
  .split { display: grid; grid-template-columns: 1.2fr 1fr; gap: 80px; align-items: start; }
  .invest-card {
    background: var(--navy); border: 1px solid rgba(180,157,106,0.4); padding: 60px 48px; border-radius: 22px; position: relative;
    box-shadow: 0 20px 60px rgba(11,16,56,0.2);
  }
  .invest-card::before { content: ''; position: absolute; top: 0; left: 0; right: 0; height: 3px; background: linear-gradient(90deg, var(--gold), var(--gold-light)); border-top-left-radius: 22px; border-top-right-radius: 22px; }
  .invest-tag { font-size: 10px; font-weight: 700; letter-spacing: 0.3em; text-transform: uppercase; color: var(--gold); margin-bottom: 32px; }
  .invest-price-main { font-family: var(--font-display); font-size: 72px; font-weight: 300; color: var(--white); line-height: 1; margin-bottom: 8px; }
  .invest-price-main span { font-size: 32px; color: var(--gold-light); }
  .invest-price-label { font-size: 12px; font-weight: 400; letter-spacing: 0.1em; color: rgba(255,255,255,0.4); text-transform: uppercase; margin-bottom: 32px; }
  .invest-divider { width: 100%; height: 1px; background: rgba(180,157,106,0.2); margin: 32px 0; }
  .invest-parcel { font-size: 15px; font-weight: 300; color: rgba(255,255,255,0.6); margin-bottom: 8px; }
  .invest-parcel strong { color: var(--gold-light); font-weight: 500; font-family: var(--font-display); font-size: 24px; }
  .invest-obs { font-size: 12px; font-weight: 300; color: rgba(255,255,255,0.3); line-height: 1.7; margin-top: 24px; }
  .invest-cta { display: block; text-align: center; margin-top: 40px; font-size: 12px; font-weight: 700; letter-spacing: 0.2em; text-transform: uppercase; text-decoration: none; color: var(--navy); background: var(--gold); padding: 20px; border-radius: 999px; transition: all 0.3s; }
  .invest-cta:hover { background: var(--gold-light); }

  .steps { display: grid; grid-template-columns: repeat(1, 1fr); gap: 18px; margin-top: 46px; }
  .step {
    position: relative; overflow: hidden; border: 1px solid rgba(11,16,56, 0.1); border-radius: 22px;
    background: linear-gradient(180deg, rgba(255,255,255,0.6), rgba(255,255,255,0.2)); padding: 26px;
  }
  .step::before {
    content: ""; position: absolute; inset: 0; z-index: 2; pointer-events: none; border-radius: inherit; opacity: 0;
    background: radial-gradient(720px circle at var(--mouse-x, 50%) var(--mouse-y, 50%), rgba(180,157,106, 0.15), transparent 42%); transition: opacity 400ms ease;
  }
  .step:hover::before { opacity: 1; }
  .step-num {
    width: 54px; height: 54px; display: grid; place-items: center; border: 1px solid rgba(180,157,106, 0.38);
    border-radius: 50%; color: var(--navy); background: rgba(180,157,106, 0.1); font-size: 20px; font-weight: 800; font-family: var(--font-display);
  }
  .step h3 { margin-top: 34px; font-size: 1.25rem; color: var(--navy); font-family: var(--font-display); }
  .step p { margin-top: 10px; color: var(--text-mid); font-size: 14px; }

  /* --- CTA FINAL --- */
  .cta-final { background: var(--navy); padding: 120px 0; text-align: center; position: relative; overflow: hidden; }
  .cta-final::before { content: ''; position: absolute; top: 0; left: 0; right: 0; height: 1px; background: linear-gradient(90deg, transparent, var(--gold), transparent); }
  .cta-final-headline { font-family: var(--font-display); font-size: clamp(36px, 5vw, 64px); font-weight: 300; line-height: 1.2; color: var(--white); margin-bottom: 20px; }
  .cta-final-headline em { font-style: italic; color: var(--gold-light); }
  .cta-final-sub { font-size: 15px; font-weight: 300; color: rgba(255,255,255,0.5); margin-bottom: 48px; max-width: 480px; margin-left: auto; margin-right: auto; }
  .btn-wpp {
    display: inline-flex; align-items: center; gap: 12px; font-size: 13px; font-weight: 600; letter-spacing: 0.1em;
    text-transform: uppercase; text-decoration: none; color: var(--navy); background: var(--gold);
    padding: 18px 36px; border-radius: 999px; transition: all 0.3s;
  }
  .btn-wpp:hover { background: var(--gold-light); }
  .btn-wpp svg { width: 20px; height: 20px; fill: var(--navy); }

  /* --- FOOTER --- */
  footer { background: #05081C; padding: 56px 32px; text-align: center; border-top: 1px solid rgba(180,157,106,0.15); }
  .footer-brand { font-family: var(--font-display); font-size: 22px; font-weight: 300; color: var(--gold-light); margin-bottom: 8px; }
  .footer-sub { font-size: 11px; letter-spacing: 0.15em; text-transform: uppercase; color: rgba(255,255,255,0.25); margin-bottom: 20px; }
  .footer-insta { font-size: 12px; font-weight: 400; color: rgba(255,255,255,0.35); text-decoration: none; letter-spacing: 0.05em; transition: color 0.3s; }
  .footer-insta:hover { color: var(--gold-light); }

  @media (max-width: 768px) {
    .container { padding: 0 20px; }
    .hero-content { padding: 60px 20px 60px 32px; }
    .dor-inner, .instructor-grid, .split { grid-template-columns: 1fr; gap: 48px; }
    .pillar-grid { grid-template-columns: 1fr; }
    .bento { grid-template-columns: 1fr; }
    .card.wide { grid-column: span 1; }
    .card.destaque { grid-column: 1 / -1; }
    .steps { grid-template-columns: 1fr; }
  }
"""

# Extract the HTML body parts and wrap them with the new classes
# We will use regex to replace the old CSS with the new CSS.
new_html = re.sub(r'<style>.*?</style>', f'<style>\n{new_css}\n</style>', content, flags=re.DOTALL)

# Refactor Hero
new_html = new_html.replace('<div class="hero-line"></div>', '<div class="hero-animation-grid" id="bg-grid" aria-hidden="true"></div>')
new_html = new_html.replace('<div class="hero-content">', '<div class="container hero-content">')
new_html = new_html.replace('<div class="hero-eyebrow">Mentoria VIP — Cirurgia de Siso</div>', '<span class="eyebrow animate-on-scroll">Mentoria VIP — Cirurgia de Siso</span>')
new_html = new_html.replace('<h1>', '<h1 id="hero-title" class="animate-on-scroll">')
new_html = new_html.replace('<p class="hero-subtext">', '<p class="hero-subtext animate-on-scroll">')
new_html = new_html.replace('<div class="hero-actions">', '<div class="hero-actions animate-on-scroll">')

# Refactor Dor -> Problem
new_html = new_html.replace('<div class="dor-label">O diagnóstico honesto</div>', '<span class="section-label animate-on-scroll">O diagnóstico honesto</span>')
new_html = new_html.replace('<h2 class="dor-headline">Reconhece alguma dessas situações?</h2>', '<h2 class="dor-headline animate-on-scroll">Reconhece alguma dessas situações?</h2>')
new_html = new_html.replace('<p class="dor-body">', '<p class="dor-body animate-on-scroll">')
# Cards to Pain List
new_html = new_html.replace('<div class="dor-cards">', '<div class="pain-list">')
new_html = new_html.replace('<div class="dor-card">', '<article class="pain animate-on-scroll">')
new_html = new_html.replace('<div class="dor-card-title">', '<p><strong>')
new_html = new_html.replace('</div>\n          <div class="dor-card-text">', '</strong><br>')
new_html = new_html.replace('</div>\n        </article>', '</p>\n        </article>')
# Inject numbers into pain
count = 1
while '<article class="pain animate-on-scroll">' in new_html:
    new_html = new_html.replace('<article class="pain animate-on-scroll">', f'<article class="pain animate-on-scroll">\n          <span class="pain-mark">0{count}</span>', 1)
    count += 1

# Refactor Solução -> Pillars
new_html = new_html.replace('<div class="section-label">A solução</div>', '<span class="section-label animate-on-scroll">A solução</span>')
new_html = new_html.replace('<h2 class="section-title">', '<h2 class="section-title animate-on-scroll">')
new_html = new_html.replace('<p class="section-sub">', '<p class="section-sub animate-on-scroll">')
new_html = new_html.replace('<div class="pilares-grid">', '<div class="pillar-grid">')
new_html = new_html.replace('<div class="pilar">', '<article class="pillar animate-on-scroll">')
new_html = new_html.replace('<div class="pilar-number">', '<p class="pillar-num">Pilar ')
new_html = new_html.replace('</div>\n        <div class="pilar-icon">', '</p>\n        <div class="pilar-icon">')
new_html = new_html.replace('<div class="pilar-title">', '<h3>')
new_html = new_html.replace('</div>\n        <div class="pilar-text">', '</h3>\n        <p>')
new_html = new_html.replace('</div>\n      </article>', '</p>\n      </article>')

# Refactor Mentor -> Instructor
new_html = new_html.replace('<div class="mentor-inner">', '<div class="instructor-grid">')
new_html = new_html.replace('<div class="mentor-photo-wrap">', '<div class="instructor-photo animate-on-scroll">')
# Actually keep mentor photo inside since we styled it.
new_html = new_html.replace('<div class="section-label">Quem vai te guiar</div>', '<span class="section-label animate-on-scroll">Quem vai te guiar</span>')
new_html = new_html.replace('<h2 class="mentor-headline">', '<h2 class="mentor-headline animate-on-scroll">')
new_html = new_html.replace('<p class="mentor-bio">', '<p class="mentor-bio animate-on-scroll">')
new_html = new_html.replace('<div class="stats-row">', '<div class="instructor-proof animate-on-scroll">')
new_html = new_html.replace('<div class="stat-item">', '<div>')
new_html = new_html.replace('<div class="stat-number">', '<strong>')
new_html = new_html.replace('</div>\n            <div class="stat-label">', '</strong>\n            <span>')
new_html = new_html.replace('</div>\n          </div>', '</span>\n          </div>')

# Refactor Diferenciais -> Bento
new_html = new_html.replace('<div class="section-label">Por que esta mentoria é diferente</div>', '<span class="section-label animate-on-scroll">Por que esta mentoria é diferente</span>')
new_html = new_html.replace('<div class="diferenciais-grid">', '<div class="bento">')
new_html = new_html.replace('<div class="diferencial-card">', '<article class="card wide animate-on-scroll">')
new_html = new_html.replace('<div class="diferencial-card destaque">', '<article class="card destaque animate-on-scroll">')
new_html = new_html.replace('<div class="dc-tag">', '<span class="tag">')
new_html = new_html.replace('</div>\n        <div class="dc-title">', '</span>\n        <h3>')
new_html = new_html.replace('</div>\n        <div class="dc-text">', '</h3>\n        <p>')
new_html = new_html.replace('</div>\n      </article>', '</p>\n      </article>')
new_html = new_html.replace('</div>\n        <div class="bonus-items">', '</p>\n        <div class="bonus-items">')

# Refactor Investimento -> Steps
new_html = new_html.replace('<div class="invest-inner">', '<div class="split">')
new_html = new_html.replace('<div class="invest-card">', '<div class="invest-card animate-on-scroll">')
new_html = new_html.replace('<div class="invest-side">', '<div class="invest-side animate-on-scroll">')
new_html = new_html.replace('<div class="inscricao-steps">', '<div class="steps">')
new_html = new_html.replace('<div class="step-item">', '<article class="step animate-on-scroll">')
new_html = new_html.replace('<div class="step-n">', '<div class="step-num">')
new_html = new_html.replace('</div>\n            <div class="step-info">\n              <div class="step-name">', '</div>\n            <h3>')
new_html = new_html.replace('</div>\n              <div class="step-desc">', '</h3>\n            <p>')
new_html = new_html.replace('</div>\n            </div>\n          </article>', '</p>\n          </article>')

# Final CTA
new_html = new_html.replace('<h2 class="cta-final-headline">', '<h2 class="cta-final-headline animate-on-scroll">')
new_html = new_html.replace('<p class="cta-final-sub">', '<p class="cta-final-sub animate-on-scroll">')
new_html = new_html.replace('<div class="cta-final-actions">', '<div class="cta-final-actions animate-on-scroll">')

# Inject JS
js = """
<script>
  (function initCleanAnimations() {
    const prefersReducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

    const bgGrid = document.getElementById("bg-grid");
    if (bgGrid) {
      const columnCount = window.innerWidth < 640 ? 6 : 12;
      for (let index = 0; index < columnCount; index += 1) {
        const column = document.createElement("div");
        column.className = "bg-column";
        bgGrid.appendChild(column);
        window.setTimeout(() => column.classList.add("active"), 120 + index * 90);
      }
    }

    const title = document.getElementById("hero-title");
    if (title) {
      let charIndex = 0;
      const splitTextNode = node => {
        const fragment = document.createDocumentFragment();
        node.textContent.split(/(\\s+)/).forEach(token => {
          if (!token) return;
          if (/^\\s+$/.test(token)) {
            fragment.appendChild(document.createTextNode(token));
            return;
          }
          const word = document.createElement("span");
          word.className = "word";
          token.split("").forEach(char => {
            const span = document.createElement("span");
            span.className = "char";
            span.textContent = char;
            span.style.transitionDelay = `${Math.min(charIndex * 24, 1200)}ms`;
            charIndex += 1;
            word.appendChild(span);
          });
          fragment.appendChild(word);
        });
        node.replaceWith(fragment);
      };

      const walker = document.createTreeWalker(title, NodeFilter.SHOW_TEXT);
      const textNodes = [];
      while (walker.nextNode()) textNodes.push(walker.currentNode);
      textNodes.forEach(splitTextNode);

      window.setTimeout(() => {
        title.querySelectorAll(".char").forEach(char => char.classList.add("revealed"));
      }, prefersReducedMotion ? 0 : 120);
    }

    const animatedElements = document.querySelectorAll(".animate-on-scroll");
    animatedElements.forEach((element, index) => {
      element.style.transitionDelay = `${Math.min((index % 6) * 70, 350)}ms`;
      if (element.closest(".hero")) element.classList.add("in-view");
    });

    if (prefersReducedMotion || !("IntersectionObserver" in window)) {
      animatedElements.forEach(element => element.classList.add("in-view"));
    } else {
      const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
          if (!entry.isIntersecting) return;
          entry.target.classList.add("in-view");
          observer.unobserve(entry.target);
        });
      }, { threshold: 0.12, rootMargin: "0px 0px -8% 0px" });

      animatedElements.forEach(element => observer.observe(element));
    }

    const flashlightElements = document.querySelectorAll(".card, .pillar, .step, .pain");
    window.addEventListener("pointermove", event => {
      flashlightElements.forEach(element => {
        const rect = element.getBoundingClientRect();
        element.style.setProperty("--mouse-x", `${event.clientX - rect.left}px`);
        element.style.setProperty("--mouse-y", `${event.clientY - rect.top}px`);
      });
    }, { passive: true });
  })();
</script>
</body>
"""

new_html = new_html.replace('</body>', js)

with open("index.html", "w") as f:
    f.write(new_html)
