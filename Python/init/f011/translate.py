import urllib.request
import urllib.parse
import uuid
import time
import json

while True:
    content = input('please input the words you want translate(press q! to exit) : ')
    if content == 'q!':
        break

    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc'

    uu = uuid.uuid1()
    sign = str(uu).replace('-','')

    salt = int(time.time()*1000)
    head = {
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36'
    }
    data = {
        'i':content,
        'from':'AUTO',
        'to':'AUTO',
        'smartresult':'dict',
        'client':'fanyideskweb',
        'salt':salt,
        'sign':sign,
        'doctype':'json',
        'version':'2.1',
        'keyfrom':'fanyi.web',
        'action':'FY_BY_CLICKBUTTION',
        'typoResult':True
        }
    data = urllib.parse.urlencode(data).encode('utf-8')


    req = urllib.request.Request(url, data, head)
    #req.add_header('User-Agent', '')
    #print(req.headers)
    res = urllib.request.urlopen(req)

    html = res.read().decode('utf-8')

    target = json.loads(html)

    print(target['translateResult'][0][0]['tgt'])
    time.sleep(5)
