import re

with open("index.html", "r") as f:
    content = f.read()

# Replace variables block
old_root = """  :root {
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

new_root = """  :root {
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

content = content.replace(old_root, new_root)

# Replace 255,255,255 with 0,0,0 for opacities
# E.g. rgba(255,255,255,0.65) -> rgba(0,0,0,0.65)
content = content.replace("255,255,255", "0,0,0")

# Update hero background gradient to light overlay
# We had: background: linear-gradient(135deg, rgba(11,16,56,0.92) 0%, rgba(11,16,56,0.3) 100%), url('Topo.png') center/cover no-repeat;
# Change to light overlay
content = re.sub(
    r"rgba\(11,16,56,[0-9\.]+\)",
    lambda m: "rgba(228,224,221," + m.group(0).split(",")[-1],
    content
)

# Wait, the footer was hardcoded background: #05081C;
content = content.replace("background: #05081C;", "background: var(--navy-mid);")

# Also the mentor placeholder had hardcoded linear-gradient(135deg, #161E4D 0%, #0B1038 100%)
content = content.replace("#161E4D", "var(--navy-mid)").replace("#0B1038", "var(--navy)")

with open("index.html", "w") as f:
    f.write(content)
