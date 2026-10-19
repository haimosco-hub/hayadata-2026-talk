import re, base64, json, os, sys, mimetypes, urllib.request
ROOT = os.getcwd()
V = os.path.join(ROOT, 'build')
def rd(p, mode='r'):
    with open(p, mode, encoding=None if 'b' in mode else 'utf-8') as f: return f.read()
def b64file(p):
    mt = mimetypes.guess_type(p)[0] or 'application/octet-stream'
    if p.endswith('.svg'): mt = 'image/svg+xml'
    return 'data:%s;base64,%s' % (mt, base64.b64encode(rd(p,'rb')).decode())

# ---- fonts: keep latin + latin-ext blocks, embed woff2 as base64
css = rd(os.path.join(V, 'fonts.css'))
blocks = re.findall(r'/\* ([\w-]+) \*/\s*(@font-face \{.*?\})', css, re.S)
font_css = []
cache = {}
for subset, block in blocks:
    if subset not in ('latin', 'latin-ext'): continue
    url = re.search(r'url\((https://[^)]+)\)', block).group(1)
    if url not in cache:
        cache[url] = base64.b64encode(urllib.request.urlopen(url).read()).decode()
    block = block.replace(url, 'data:font/woff2;base64,' + cache[url])
    font_css.append('/* %s */\n%s' % (subset, block))
FONT_CSS = '\n'.join(font_css)
print('fonts embedded:', len(cache), 'files')

GF_LINK = re.compile(r'<link[^>]+fonts\.googleapis\.com[^>]*>\s*')

# ---- demos -> templates with {{PART}} tokens
PARTS = {
    'chartjs': rd(os.path.join(V, 'chart.umd.min.js')),
    'datalabels': rd(os.path.join(V, 'datalabels.min.js')),
    'geo': rd(os.path.join(V, 'geo.umd.min.js')),
    'data': rd('demo/dashboard_data.js'),
    'topo': rd('demo/us-states-topojson-data.js'),
    'theme': rd('demo/dashboard-theme.css'),
    'fonts': FONT_CSS,
}
def demo_template(path):
    h = rd(path)
    n0 = len(GF_LINK.findall(h)); h = GF_LINK.sub('', h)
    subs = [
        (r'<script src="https://cdn\.jsdelivr\.net/npm/chart\.js@[^"]+"></script>', '<script>{{chartjs}}</script>'),
        (r'<script src="https://cdn\.jsdelivr\.net/npm/chartjs-plugin-datalabels@[^"]+"></script>', '<script>{{datalabels}}</script>'),
        (r'<script src="https://cdn\.jsdelivr\.net/npm/chartjs-chart-geo@[^"]+"></script>', '<script>{{geo}}</script>'),
        (r'<link[^>]+href="dashboard-theme\.css"[^>]*>', '<style>{{fonts}}</style>\n<style>{{theme}}</style>'),
        (r'<script src="dashboard_data\.js"></script>', '<script>{{data}}</script>'),
        (r'<script src="us-states-topojson-data\.js"></script>', '<script>{{topo}}</script>'),
    ]
    for pat, rep in subs:
        h, n = re.subn(pat, rep, h)
        assert n == 1, (path, pat, n)
    assert n0 == 2, (path, 'google font links', n0)
    left = re.findall(r'(?:src|href)="(https?://[^"]+)"', h)
    assert not left, (path, left)
    return h
TEMPLATES = {'dashboard': demo_template('demo/dashboard.html'), 'agent': demo_template('demo/dashboard-agent.html')}

def js_json(obj):
    return json.dumps(obj, ensure_ascii=False).replace('</', '<'+chr(92)+'/').replace('<!--', '<'+chr(92)+'!--')
PAYLOAD = ('<script id="demo-payload">\n'
           '/* Embedded dashboard demos (demo/dashboard.html, demo/dashboard-agent.html) and their\n'
           '   shared parts (Chart.js + plugins, dashboard data, US topojson, theme, fonts), stored\n'
           '   once; reloadDashboard() assembles them and loads the result through iframe.srcdoc. */\n'
           'window.DEMO_PARTS = %s;\nwindow.DEMO_TEMPLATES = %s;\n</script>\n') % (js_json(PARTS), js_json(TEMPLATES))

# ---- deck
d = rd('presentation.src.html')
n = len(GF_LINK.findall(d)); assert n == 2, n
d = GF_LINK.sub('', d, count=1)  # drop preconnect
d = GF_LINK.sub(lambda m: '<style>' + chr(10) + FONT_CSS + chr(10) + '</style>' + chr(10), d, count=1)

# images
def img_sub(m):
    p = m.group(1)
    assert os.path.exists(p), p
    return 'src="%s"' % b64file(p)
d, ni = re.subn(r'src="([^"]+\.(?:png|jpe?g|svg|gif|webp))"', img_sub, d)
print('images embedded:', ni)

# iframes -> data-demo
d, a = re.subn(r'<iframe class="dash-iframe" src="demo/dashboard\.html"', '<iframe class="dash-iframe" data-demo="dashboard"', d); assert a == 1
d, b = re.subn(r'<iframe class="dash-iframe" src="demo/dashboard-agent\.html"', '<iframe class="dash-iframe" data-demo="agent"', d); assert b == 1

old_reload = """  function loadDashboardInto(iframe) {
    iframe.src = iframe.getAttribute('src').split('?')[0] + '?t=' + Date.now();
  }
  function reloadDashboard(slide) {
    const iframe = slide.querySelector('.dash-iframe');
    if (iframe) loadDashboardInto(iframe);
  }"""
new_reload = """  function buildDemo(name) {
    return window.DEMO_TEMPLATES[name].replace(/\{\{(\w+)\}\}/g, (m, k) => window.DEMO_PARTS[k]);
  }
  function reloadDashboard(slide) {
    const iframe = slide.querySelector('.dash-iframe');
    if (iframe) loadDashboardInto(iframe);
  }
  function loadDashboardInto(iframe) {
    // srcdoc instead of src: the demo pages are embedded in this file (#demo-payload),
    // so the deck has no file or network dependency. A fresh timestamp comment makes
    // every assignment a real navigation, i.e. a replay from the default state.
    iframe.srcdoc = buildDemo(iframe.dataset.demo) + '<!-- ' + Date.now() + ' -->';
  }
  document.querySelectorAll('.dash-iframe[data-demo]').forEach(f => reloadDashboard(f.closest('.dashboard-slide')));"""
assert old_reload in d
d = d.replace(old_reload, new_reload)

# payload script goes right before the deck's main <script>
idx = d.rfind('<script>')
assert idx > 0
d = d[:idx] + PAYLOAD + d[idx:]

left = re.findall(r'(?:src|href)="(https?://[^"]+)"', d) + re.findall(r'url\((?!["\']?data:)[^)]*\)', d)
print('remaining external refs:', left)
with open('presentation.html', 'w', encoding='utf-8') as f: f.write(d)
print('written', len(d.encode('utf-8')), 'bytes')
