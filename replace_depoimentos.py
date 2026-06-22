import re

with open('index.html', 'r') as f:
    content = f.read()

# 1. Replace the Grid HTML
new_html = """    <div class="depoimentos-grid animate-on-scroll">
      <div class="depoimento-video">
        <video controls playsinline>
          <source src="https://video.gumlet.io/69ce7db61763b418bf1cfd14/6a2ee70a93651fdca9585ed8/main.m3u8" type="application/x-mpegURL">
        </video>
      </div>
      <div class="depoimento-video">
        <video controls playsinline>
          <source src="https://video.gumlet.io/69ce7db61763b418bf1cfd14/6a2ee709a0e544789ceb064a/main.m3u8" type="application/x-mpegURL">
        </video>
      </div>
      <div class="depoimento-video">
        <video controls playsinline>
          <source src="https://video.gumlet.io/69ce7db61763b418bf1cfd14/6a2ee709a0e544789ceb0647/main.m3u8" type="application/x-mpegURL">
        </video>
      </div>
      <div class="depoimento-video">
        <video controls playsinline>
          <source src="https://video.gumlet.io/69ce7db61763b418bf1cfd14/6a2ee70aa0e544789ceb0651/main.m3u8" type="application/x-mpegURL">
        </video>
      </div>
    </div>"""

start_idx = content.find('<div class="depoimentos-grid animate-on-scroll">')
end_idx = content.find('</div>\n  </div>\n</section>', start_idx)
if start_idx != -1 and end_idx != -1:
    content = content[:start_idx] + new_html + "\n" + content[end_idx:]

# 2. Update CSS for depoimentos
css_pattern = re.compile(r'\.depoimentos-grid \{.*?\n  \}', re.DOTALL)
new_grid_css = """.depoimentos-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 16px;
    margin-top: 48px;
  }
  .depoimento-video {
    width: 100%;
    border-radius: 20px;
    overflow: hidden;
    border: 1px solid rgba(180,157,106, 0.2);
    box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    background: var(--navy-mid);
    position: relative;
    aspect-ratio: 9/16;
  }
  .depoimento-video video {
    position: absolute;
    top: 0; left: 0;
    width: 100%; height: 100%;
    object-fit: cover;
    display: block;
  }"""
content = css_pattern.sub(new_grid_css, content, count=1)

# Remove old .depoimento-card css
content = re.sub(r'\.depoimento-card \{.*?\n  \}', '', content, flags=re.DOTALL)
content = re.sub(r'\.depoimento-card:hover \{.*?\n  \}', '', content, flags=re.DOTALL)
content = re.sub(r'\.depoimento-card \.stars \{.*?\n  \}', '', content, flags=re.DOTALL)
content = re.sub(r'\.depoimento-texto \{.*?\n  \}', '', content, flags=re.DOTALL)
content = re.sub(r'\.depoimento-autor strong \{.*?\n  \}', '', content, flags=re.DOTALL)
content = re.sub(r'\.depoimento-autor span \{.*?\n  \}', '', content, flags=re.DOTALL)

# 3. Update Responsive CSS
resp_css_pattern = r'    \.depoimentos-grid \{ grid-template-columns: 1fr; gap: 24px; \}'
resp_new = """    .depoimentos-grid {
      display: flex;
      overflow-x: auto;
      scroll-snap-type: x mandatory;
      gap: 16px;
      padding-bottom: 20px;
      -webkit-overflow-scrolling: touch;
      grid-template-columns: none;
    }
    .depoimento-video {
      flex: 0 0 85%;
      scroll-snap-align: center;
    }
    /* Hide scrollbar for a cleaner look */
    .depoimentos-grid::-webkit-scrollbar { display: none; }
    .depoimentos-grid { -ms-overflow-style: none; scrollbar-width: none; }"""
content = content.replace(resp_css_pattern, resp_new)

# 4. Inject hls.js at the end before </body>
hls_script = """<script src="https://cdn.jsdelivr.net/npm/hls.js@latest"></script>
<script>
  document.addEventListener('DOMContentLoaded', function() {
    var videos = document.querySelectorAll('.depoimento-video video');
    videos.forEach(function(video) {
      var source = video.querySelector('source').src;
      if (Hls.isSupported()) {
        var hls = new Hls();
        hls.loadSource(source);
        hls.attachMedia(video);
      } else if (video.canPlayType('application/vnd.apple.mpegurl')) {
        video.src = source;
      }
    });
  });
</script>
</body>"""

if "hls.js" not in content:
    content = content.replace("</body>", hls_script)

with open('index.html', 'w') as f:
    f.write(content)

