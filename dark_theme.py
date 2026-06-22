import re

filepath = '/Users/iuryphilipylins/Documents/Antigravity/Bruno Noronha - Mentoria/index.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Body background
content = content.replace('background: var(--cream);', 'background: #0B1038;')
content = content.replace('color: var(--text-dark);', 'color: var(--white);')

# Nav background
content = content.replace('background: rgba(228,224,221,0.96);', 'background: rgba(11, 16, 56, 0.96);')

# Hero section background and text
content = content.replace('background: linear-gradient(135deg, rgba(228,224,221,0.92) 0%, rgba(228,224,221,0.3) 100%)', 'background: linear-gradient(135deg, rgba(11, 16, 56, 0.92) 0%, rgba(11, 16, 56, 0.3) 100%)')
content = content.replace('color: #1a1a1a;', 'color: var(--white);')
content = content.replace('color: #4a4a4a;', 'color: rgba(255, 255, 255, 0.65);')
content = content.replace('color: #1a1a1a; font-weight: 500;"', 'color: var(--white); font-weight: 500;"')

# Solucao section (O que voce vai aprender)
content = content.replace('.solucao-section { padding: 120px 0; background: var(--cream); }', '.solucao-section { padding: 120px 0; background: #05081C; }')
content = content.replace('.section-title {\n    font-family: var(--font-display);\n    font-size: clamp(36px, 4vw, 58px);\n    font-weight: 300; line-height: 1.2;\n    color: #0B1038;', '.section-title {\n    font-family: var(--font-display);\n    font-size: clamp(36px, 4vw, 58px);\n    font-weight: 300; line-height: 1.2;\n    color: var(--white);')
content = content.replace('.section-sub {\n    font-size: 15px; font-weight: 300;\n    color: var(--text-mid);', '.section-sub {\n    font-size: 15px; font-weight: 300;\n    color: rgba(255,255,255,0.65);')

# Pilares cards (inside Solucao/Diferenciais)
content = content.replace('background: rgba(255, 255, 255, 0.6);', 'background: linear-gradient(145deg, rgba(255, 255, 255, 0.05), rgba(255, 255, 255, 0.01));')
content = content.replace('color: #0B1038;\n    margin-bottom: 14px;', 'color: var(--white);\n    margin-bottom: 14px;')
content = content.replace('.pilar-title" style="font-size: 16px;">', '.pilar-title" style="font-size: 16px; color: var(--white);">')

# Diferenciais section
content = content.replace('class="diferenciais-section" style="padding: 120px 0; background: var(--cream-dark);"', 'class="diferenciais-section" style="padding: 120px 0; background: #0B1038;"')

# Invest section
content = content.replace('.invest-section {\n    padding: 120px 0;\n    background: var(--cream);\n  }', '.invest-section {\n    padding: 120px 0;\n    background: #05081C;\n  }')
content = content.replace('.invest-side-title {\n    font-family: var(--font-display);\n    font-size: 36px; font-weight: 300;\n    color: #0B1038;', '.invest-side-title {\n    font-family: var(--font-display);\n    font-size: 36px; font-weight: 300;\n    color: var(--white);')
content = content.replace('color: var(--text-mid); line-height: 1.6;', 'color: rgba(255,255,255,0.65); line-height: 1.6;')
content = content.replace('color: #0B1038; margin-bottom: 4px;', 'color: var(--white); margin-bottom: 4px;')
content = content.replace('color: var(--text-muted); line-height: 1.6;', 'color: rgba(255,255,255,0.65); line-height: 1.6;')
content = content.replace('color: var(--cream-dark); flex-shrink: 0;', 'color: rgba(180,157,106,0.2); flex-shrink: 0;')

# FAQ section
content = content.replace('class="faq-section" style="padding: 120px 0; background: var(--cream);"', 'class="faq-section" style="padding: 120px 0; background: #0B1038;"')
content = content.replace('color: #0B1038; list-style: none;', 'color: var(--white); list-style: none;')
content = content.replace('color: var(--text-mid); line-height: 1.8;', 'color: rgba(255,255,255,0.65); line-height: 1.8;')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
