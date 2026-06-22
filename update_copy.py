import re

with open('index.html', 'r') as f:
    content = f.read()

# 1. Tagline do Topo (Eyebrow)
content = content.replace("Mentoria VIP Individual — Cirurgia de Siso", "Mentoria VIP Individual — Cirurgia Oral Menor")

# 2. Título Principal (Hero)
content = content.replace("Todo siso que você encaminha", "Toda cirurgia oral que você encaminha")

# 3. Subtítulo Principal
content = content.replace("A insegurança na extração de terceiros molares não é falta de inteligência", "A insegurança nas cirurgias orais menores não é falta de inteligência")

# 4. Seção de Dor (Texto Introdutório)
content = content.replace("indicação de siso incluso", "indicação cirúrgica mais complexa")

# 5. Seção de Dor (Card 1)
content = content.replace("Cada siso que você encaminha é uma consulta", "Cada procedimento cirúrgico que você encaminha é uma consulta")

# 6. Subtítulo dos Depoimentos
content = content.replace("transformou o medo da extração em previsibilidade clínica.", "transformou o medo da cirurgia em previsibilidade clínica.")

# 7. Links do WhatsApp (URL encoded text)
content = content.replace("Mentoria%20VIP%20de%20Cirurgia%20de%20Siso", "Mentoria%20VIP%20de%20Cirurgia%20Oral%20Menor")

# 8. Chamada Final (Fundo da Página)
content = content.replace("A próxima extração de siso pode ser sua.", "A próxima cirurgia oral pode ser sua.")

# 9. Rodapé e Titulo
content = content.replace("Mentoria VIP em Cirurgia de Siso", "Mentoria VIP em Cirurgia Oral Menor")

with open('index.html', 'w') as f:
    f.write(content)

