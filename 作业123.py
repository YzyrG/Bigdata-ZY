# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#作业1
a=[21,32,43,32,30,32,32]
print(a[0])
print(a[1])
print('周三'+str(a[2]))
print(a[3])
print(a[4])
#作业2
b={'周一':['20','晴'],
   '周二':['23','阴'],
   '周三':['20','晴'],
   '周四':['32','阴'],
   '周五':['24','晴'],
   }
print(b['周三'])
c={'weather':['晴','阴','晴','阴','晴'], 'wendu':['21','22','32','32','32']}

#作业3
a=b'1'
print(a)
import urllib.request as r
data=r.urlopen('http://api.openweathermap.org/data/2.5/weather?q=lanzhou&mode=json&units=metric&lang=zh_cn&APPID=6a67ed641c0fda8b69715c43518b6996').read().decode('utf-8','ignore')
import json
data=json.loads(data)
data['main']['temp']
data['description']
data['pressure']