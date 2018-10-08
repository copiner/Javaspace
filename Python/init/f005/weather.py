import urllib.request
import json
import pickle

pickle_file = open('city_data.pkl','rb')
city = pickle.load(pickle_file)
pickle_file.close()
password = input('input a city name : ')
name=city[password]
File =urllib.request.urlopen('http://m.weather.com.cn/mweather/'+name+'.shtml')#open the url
weatherHTML= File.read().decode('utf-8')#read the url
weatherJSON = json.JSONDecoder().decode(weatherHTML)#create json
weatherInfo = weatherJSON['weatherinfo']
#paint info
print('city : ', weatherInfo['city'])
print('time : ', weatherInfo['date_y'])
print('24 hours weather : ')
print('tempture : ', weatherInfo['temp1'])
print('weather : ', weatherInfo['weather1'])
print('wind : ', weatherInfo['wind1'])
print('sun : ', weatherInfo['index_uv'])
print('dress : ', weatherInfo['index_d'])
print('48 hours weather : ')
print('tempture : ', weatherInfo['temp2'])
print('weather : ', weatherInfo['weather2'])
print('wind : ', weatherInfo['wind2'])
print('sun : ', weatherInfo['index48_uv'])
print('dress : ', weatherInfo['index48_d'])
print('72 hours weather : ')
print('tempture : ', weatherInfo['temp3'])
print('weather : ', weatherInfo['weather3'])
print('wind : ', weatherInfo['wind3'])
input('press any key to exit')
