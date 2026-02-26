import urllib.request, re, ssl
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "https://fatfa.org.ar/2026/02/25/escala-salarial-febrero-2026/"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    html = urllib.request.urlopen(req, context=ctx).read().decode('utf-8', errors='ignore')
    img = re.search(r'property="og:image" content="(.*?)"', html)
    print("IMAGE:", img.group(1) if img else "Not found")
except Exception as e:
    print("ERROR:", e)
