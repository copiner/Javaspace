import urllib.request
import json
import pickle
import easygui as g
import sys

pickle_file = open('city_date.pkl','rb')
city = pickle.load(pickle_file)
g.msgbox('由于中国天气网接口原因，只能查询到3月4号的天气，请大家谅解~','温馨提示')

while 1:
    password=g.enterbox(msg='请输入城市:', title=' ', default='', strip=True, image=None, root=None)
    name1=city[password]
    File1 =urllib.request.urlopen('http://m.weather.com.cn/data/'+name1+'.html')#打开url
    weatherHTML= File1.read().decode('utf-8')#读入打开的url
    weatherJSON = json.JSONDecoder().decode(weatherHTML)#创建json
    weatherInfo = weatherJSON['weatherinfo']
    #打印信息
    information = ''
    information =  ('城市' + weatherInfo['city'] + '\n' +
                '时间：' + weatherInfo['date_y'] + '\n' +
                '24小时天气：' + '\n' +
                '温度：' + weatherInfo['temp1'] + '\n' +
                '天气：'+weatherInfo['weather1'] + '\n' +
                '风速：'+ weatherInfo['wind1'] + '\n' +
                '紫外线：'+ weatherInfo['index_uv'] + '\n' +
                '穿衣指数：', weatherInfo['index_d'])
    g.msgbox(information)
    i = g.ccbox('还要查询其它城市吗？',choices=('必须的！','不玩了！'))
    if i:
        pass
    else:
        sys.exit(0)
