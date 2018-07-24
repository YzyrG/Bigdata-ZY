# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 17:11:05 2018

@author: YGYG
"""
#吉林全部获取#
ls=open('all_school.txt',encoding='utf_8').readlines()
schoolls=[]
for line in ls:            
    schoolls.append(line.split('-jianjie-')[1].split('.')[0])
import urllib.request as r
url='http://www.gaokaopai.com/university-ajaxGetMajor.html'
headers={'User-Agent':' Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
         'X-Requested-With': 'XMLHttpRequest'}
f=open('全国招生人数吉林.txt','a',encoding='utf_8')
i=0
for schoolid in schoolls:                
    for kmlx in [1,2]:
        req=r.Request(url,data='id={}&type={}&city=22&state=1'.format(schoolid,kmlx).encode(),headers=headers)
        f.write(r.urlopen(req).read().decode('utf-8','ignore')+'\n')
        i=i+1
        print('第'+str(i)+'条数据爬取成功！')
f.close()
print('数据爬取完毕！')
#吉林错误补充#
import urllib.request as r
url='http://www.gaokaopai.com/university-ajaxGetMajor.html'
headers={'User-Agent':' Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
         'X-Requested-With': 'XMLHttpRequest'}
f=open('全国招生人数吉林2.txt','a',encoding='utf_8')
req=r.Request(url,data='id=2731&type=1&city=22&state=1'.encode(),headers=headers)
f.write(r.urlopen(req).read().decode('utf-8','ignore')+'\n')                
print('本条数据爬取成功！')
f.close()
print('数据爬取完毕！')
#获取大学编号
ls=open('all_school.txt',encoding='utf_8').readlines()
schoolls=[]
for line in ls:            
    schoolls.append(line.split('-jianjie-')[1].split('.')[0])
print(schoolls)
#获取省份编号
ct=open('高考派城市.txt',encoding='gbk').readlines()
for line in ct[0:31]:            
    a = line.split(',')[1].split(')')[0]
    b = line.split(')">')[1].split('<')[0]
    print(str(a)+':'+str(b))





                    





