# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 10:25:29 2018

@author: YGYG
"""

#全球五天天气
url='http://api.openweathermap.org/data/2.5/forecast?q=huining,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
import urllib.request as r
data=r.urlopen(url).read().decode('utf-8','ignore')
import json
data=json.loads(data)
def day(a,b):
    print('day'+str(a))
    print('temperature：'+str(data['list'][b]['main']['temp']))
    print('weather：'+str(data['list'][b]['weather'][0]['description']))
    print('pressure：'+str(data['list'][b]['main']['pressure']))
    print('Maximum temperature：'+str(data['list'][b]['main']['temp_max']))
    print('Minimum temperature：'+str(data['list'][b]['main']['temp_min']))
day(1,2)
day(2,10)
day(3,18)
day(4,26)
day(5,34)

def zxt(c,d):
    return('day'+str(c)+'-'*int(data['list'][d]['main']['temp']))
print('温度折线图如下：')
print(zxt(1,2))
print(zxt(2,10))
print(zxt(3,18))
print(zxt(4,26))
print(zxt(5,34))

print('排序如下：')
def px(s):
    return(int(data['list'][s]['main']['temp']))
print(sorted([px(2),px(10),px(18),px(26),px(34)]))
