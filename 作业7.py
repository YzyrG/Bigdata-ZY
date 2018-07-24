# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 17:59:54 2018

@author: YGYG
"""
#练习七
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
    a=str(data['list'][b]['weather'][0]['main'])        
    if a=='Clear':                                          
        print('今天天气不错，可以出去散散步！')
    elif a=='Clouds':
        print('今天多云，气温较低，注意保暖！')
    elif a=='Rain':
        print('今天有雨，出门记得带伞！')
day(1,2)
day(2,10)
day(3,18)
day(4,26)
day(5,34)

                  
            

      
    