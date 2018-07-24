# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 11:36:19 2018

@author: YGYG
"""
url='https://s.taobao.com/search?q=%E8%A3%99%E5%AD%90&type=p&tmhkh5=&spm=a21wu.241046-us.a2227oh.d100&from=sea_1_searchbutton&catId=100&ajax=true'
import urllib.request as r
data=r.urlopen(url).read().decode('utf-8','ignore')
import json
data=json.loads(data)
#练习六
#任务一、二
def sp():    
    for b in range(0,36):              
        print('***商品'+str(b+1)+'***')      
        print('名称：'+str(data['mods']['itemlist']['data']['auctions'][b]['raw_title']))
        print('价格：'+str(data['mods']['itemlist']['data']['auctions'][b]['view_price']))
        print('邮费：'+str(data['mods']['itemlist']['data']['auctions'][b]['view_fee']))
        print('地址：'+str(data['mods']['itemlist']['data']['auctions'][b]['item_loc']))
        print('已售：'+str(data['mods']['itemlist']['data']['auctions'][b]['view_sales']))
        print('店铺：'+str(data['mods']['itemlist']['data']['auctions'][b]['nick']))
        if (b+1)%4==0:
          print('-'*40)
sp()
   
#任务三
px=[]
def sp1():
    for a in range(0,36):
        p=float(data['mods']['itemlist']['data']['auctions'][a]['view_price'])
        px.append(p)
    return px
sp1()
a=sorted(px)
print('价格排序如下：')
b=list(reversed(a))
print(b)
#任务四
xlpx=[]
def sp2():
    for a in range(0,36):
        p=str((data['mods']['itemlist']['data']['auctions'][a]['view_sales']))
        b=int(p[0:-3])
        xlpx.append(b)
    return xlpx
sp2()
print('销量排序如下：')
print(sorted(xlpx))
#任务五
def by(a):    
    for a in range(36):                    
        if float(data['mods']['itemlist']['data']['auctions'][a]['view_fee'])==0.00:
            
            print('商品'+str(a+1) +'包邮')        
by(a)