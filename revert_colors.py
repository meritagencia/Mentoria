import re

with open("index.html", "r") as f:
    content = f.read()

# 1. Restore root
old_root = """  :root {
    --navy: #e4e0dd;
    --navy-mid: #d5d0cd;
    --gold: #ac9c6d;
    --gold-light: #C0B187;
    --gold-pale: #E6E0D2;
    --cream: #f4f0ed;
    --cream-dark: #eae6e3;
    --white: #1a1a1a;
    --text-dark: #1a1a1a;
    --text-mid: #4a4a4a;
    --text-muted: #6a6a6a;
    --font-display: 'Cormorant Garamond', Georgia, serif;
    --font-body: 'Montserrat', sans-serif;
  }"""

new_root = """  :root {
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
  }"""
content = content.replace(old_root, new_root)

# 2. Restore 255,255,255
content = content.replace("0,0,0", "255,255,255")

# 3. Restore footer
content = content.replace("background: var(--navy-mid);", "background: #05081C;")

# 4. Restore mentor placeholder
content = content.replace("var(--navy-mid)", "#161E4D").replace("var(--navy)", "#0B1038")

# 5. The hero overlay stays light because it's hardcoded to rgba(228,224,221,...)
# But we need to make sure the hero text is dark, because --white is now #FFFFFF again.
# We will inject some CSS right after .hero-trust
hero_css_add = """
  .hero h1 { color: #1a1a1a; }
  .hero h1 em { color: #ac9c6d; }
  .hero-subtext { color: #4a4a4a; }
  .hero-subtext strong { color: #1a1a1a; }
  .hero-eyebrow { color: #ac9c6d; }
  .hero-eyebrow::after { background: #ac9c6d; }
  .hero-trust { color: #6a6a6a; }
"""
content = content.replace(".hero-trust {", hero_css_add + "\n  .hero-trust {")

with open("index.html", "w") as f:
    f.write(content)
