import urllib.request
import random

url = 'http://www.whatismyip.com.tw'

iplist = ['58.243.50.184:53281','122.224.227.202:3128','220.249.185.178:9999']

proxy_support = urllib.request.ProxyHandler({'http':random.choice(iplist)})
#proxy_support = urllib.request.ProxyHandler({'http':'122.224.227.202:3128'})

opener = urllib.request.build_opener(proxy_support)
opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36')]

urllib.request.install_opener(opener)

response = urllib.request.urlopen(url)
html = response.read().decode('utf-8')
print(html)

