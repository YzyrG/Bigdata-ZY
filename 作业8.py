# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 20:08:38 2018

@author: YGYG
"""
#练习八
#淘宝数据 
   
def main():
    try:
        f=open('裙子金华.txt','w',encoding='utf-8')
        for i in range (1,101):
            url='https://s.taobao.com/search?q=%E8%A3%99%E5%AD%90&type=p&tmhkh5=&spm=a21wu.241046-us.a2227oh.d100&from=sea_1_searchbutton&catId=100&fs=1&sort=default&bcoffset=0&p4ppushleft=%2C44&a=&loc=%E9%87%91%E5%8D%8E'+'&s=((2i-2)*22)'+'&ajax=true'
            import urllib.request as r
            data=r.urlopen(url).read().decode('utf-8','ignore')
            f.write(data+'\n')
            print('第'+str(i)+'页数据爬取成功！')
        f.close()
        print('100条数据爬取完毕！')           
    except Exception:
        print('出现错误！')
main()