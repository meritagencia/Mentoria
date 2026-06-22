import re

filepath = '/Users/iuryphilipylins/Documents/Antigravity/Bruno Noronha - Mentoria/index.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

videos = [
    'https://video.gumlet.io/69ce7db61763b418bf1cfd14/6a3979251fc7362a2ced80b2/main.m3u8',
    'https://video.gumlet.io/69ce7db61763b418bf1cfd14/6a39792563c8255987a9e1df/main.m3u8',
    'https://video.gumlet.io/69ce7db61763b418bf1cfd14/6a3979251fc7362a2ced80af/main.m3u8',
    'https://video.gumlet.io/69ce7db61763b418bf1cfd14/6a3979251fc7362a2ced80ba/main.m3u8',
    'https://video.gumlet.io/69ce7db61763b418bf1cfd14/6a3979251fc7362a2ced80b7/main.m3u8'
]

content = content.replace('src="IMG_7625.MOV"', f'data-hls-src="{videos[0]}"')
content = content.replace('src="IMG_7629.MOV"', f'data-hls-src="{videos[1]}"')
content = content.replace('src="IMG_7626.MOV"', f'data-hls-src="{videos[2]}"')
content = content.replace('src="IMG_7631.MOV"', f'data-hls-src="{videos[3]}"')
content = content.replace('src="IMG_7632.MOV"', f'data-hls-src="{videos[4]}"')

script = """
<script src="https://cdn.jsdelivr.net/npm/hls.js@latest"></script>
<script>
  document.addEventListener('DOMContentLoaded', function() {
    var videos = document.querySelectorAll('video[data-hls-src]');
    videos.forEach(function(video) {
      var src = video.getAttribute('data-hls-src');
      if (Hls.isSupported()) {
        var hls = new Hls({startLevel: -1});
        hls.loadSource(src);
        hls.attachMedia(video);
        hls.on(Hls.Events.MANIFEST_PARSED, function() {
          video.play().catch(function(e){});
        });
      } else if (video.canPlayType('application/vnd.apple.mpegurl')) {
        video.src = src;
        video.addEventListener('loadedmetadata', function() {
          video.play().catch(function(e){});
        });
      }
    });
  });
</script>
"""

# Insert script before </body>
content = content.replace('</body>', script + '\n</body>')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
