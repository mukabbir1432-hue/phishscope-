import os
import re
from urllib.parse import urlparse, parse_qs
from flask import Flask, request, render_template_string
from datetime import datetime

app = Flask(__name__)

HTML = """
<!doctype html>
<html>
<head>
<title>PhishScope</title>
<style>
body{font-family:system-ui;background:#0f172a;color:#e2e8f0;padding:40px}
.card{background:#1e293b;padding:24px;border-radius:12px;max-width:800px;margin:auto}
input{width:70%;padding:12px;border-radius:8px;border:1px solid #334155;background:#0f172a;color:white}
button{padding:12px 20px;border-radius:8px;background:#3b82f6;color:white;border:0;cursor:pointer}
.tag{display:inline-block;padding:4px 10px;border-radius:20px;font-size:12px;margin:4px}
.safe{background:#065f46} .warn{background:#92400e} .danger{background:#991b1b}
</style>
</head>
<body>
<div class="card">
<h1>🛡️ PhishScope</h1>
<p>Advanced Phishing Link Analyzer - 8 Indicators</p>
<form method="post" action="/scan">
<input name="url" placeholder="https:// suspicious-link.com/login" required>
<button>Analyze</button>
</form>
{% if result %}
<hr>
<h3>Result for: {{ result.url }}</h3>
<h2>Risk Score: {{ result.score }}/100 - {{ result.verdict }}</h2>
{% for k,v in result.indicators.items() %}
<div><b>{{ k }}:</b> <span class="tag {{ v.level }}">{{ v.text }}</span> - {{ v.detail }}</div>
{% endfor %}
{% endif %}
</div>
</body>
</html>
"""

def analyze_url(url):
    parsed = urlparse(url)
    indicators = {}
    score = 0
    
    # 1 Domain age (simulated)
    domain = parsed.netloc
    if len(domain) < 5:
        indicators['Domain'] = {'level':'danger','text':'Invalid','detail':'Domain too short'}
        score+=25
    else:
        indicators['Domain'] = {'level':'safe','text':'Valid','detail':f'{domain} - structure ok'}

    # 2 Subdomain nesting
    dots = domain.count('.')
    if dots > 3:
        indicators['Subdomain'] = {'level':'danger','text':'Brand impersonation','detail':f'{dots} dots - possible nesting'}
        score+=20
    else:
        indicators['Subdomain'] = {'level':'safe','text':'Clean','detail':'No nesting'}

    # 3 Redirect ( @ symbol )
    if '@' in url:
        indicators['Redirect'] = {'level':'danger','text':'@ detected','detail':'@ can hide real destination'}
        score+=20
    else:
        indicators['Redirect'] = {'level':'safe','text':'Direct','detail':'No @'}

    # 4 HTTPS
    if parsed.scheme != 'https':
        indicators['HTTPS'] = {'level':'warn','text':'No HTTPS','detail':'Insecure scheme'}
        score+=10
    else:
        indicators['HTTPS'] = {'level':'safe','text':'HTTPS','detail':'Secure'}

    # 5 Length
    if len(url) > 75:
        indicators['Length'] = {'level':'warn','text':'Too long','detail':f'{len(url)} chars'}
        score+=10
    else:
        indicators['Length'] = {'level':'safe','text':'Normal','detail':f'{len(url)} chars'}

    # 6 Params
    qs = parse_qs(parsed.query)
    if any(re.search(r'base64|%[0-9a-f]{2}', k+str(v), re.I) for k,v in qs.items()):
        indicators['Parameters'] = {'level':'danger','text':'Encoded payload','detail':'Suspicious encoding in params'}
        score+=25
    else:
        indicators['Parameters'] = {'level':'safe','text':'Clean','detail':'No suspicious params'}

    # 7 Keywords
    sus = ['login','verify','secure','account','update','banking']
    found = [w for w in sus if w in url.lower()]
    if found:
        indicators['Keywords'] = {'level':'warn','text':','.join(found),'detail':'Phishing keywords found'}
        score+=15
    else:
        indicators['Keywords'] = {'level':'safe','text':'None','detail':'No phishing keywords'}

    # 8 IP instead of domain
    if re.match(r'^\d+\.\d+\.\d+\.\d+', domain):
        indicators['IP Host'] = {'level':'danger','text':'IP used','detail':'Direct IP hosting'}
        score+=25
    else:
        indicators['IP Host'] = {'level':'safe','text':'Domain','detail':'Not IP'}

    verdict = "Safe" if score < 30 else "Suspicious" if score < 60 else "High Risk - Phishing"
    return {'url':url,'score':score,'verdict':verdict,'indicators':indicators}

@app.route('/', methods=['GET'])
def home():
    return render_template_string(HTML, result=None)

@app.route('/scan', methods=['POST'])
def scan():
    url = request.form.get('url','')
    result = analyze_url(url)
    return render_template_string(HTML, result=result)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
