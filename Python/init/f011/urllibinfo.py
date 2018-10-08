import io
import sys
import urllib.request
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

res = urllib.request.urlopen("http://www.baidu.com")
html = res.read()
html = html.decode("utf-8")
f = open('read.txt', 'w')
#f.write(html)
print(html, file = f)
f.close()
