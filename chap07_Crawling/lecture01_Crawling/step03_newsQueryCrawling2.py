# -*- coding: utf-8 -*-
"""
 방법2) url query 이용 : 년도별 뉴스 자료 수집 
       ex) 2017.01.01 ~ 2020.01.01
           page : 1 ~ 5
"""

import urllib.request as req # url 요청
from bs4 import BeautifulSoup # html  파싱
import pandas as pd # 시계열 date

# 1. 수집 년도 생성 : 시계열 date 이용 
date = pd.date_range("2017-01-01", "2020-01-01") 
len(date) # 1827
5*365 # 1825
date[0] # '2017-01-01 00:00:00'
date[-1] # '2020-01-01 00:00:00'

import re # sub('pattern', '', string)


# '2017-01-01 00:00:00' -> 20170101
sdate = [re.sub('-', '', str(d))[:8]  for d in date]
sdate[:10]
sdate[-10:]


# 2. Crawler 함수 
def newsCrawler(date,  pages=5) : # 1 day news 
    
    one_day_date = []
    for page in range(1, pages+1) : # 1 ~ 5
        url = f"https://news.daum.net/newsbox?regDate={date}&page={page}"
        
        try : 
            # 1. url 요청
            res = req.urlopen(url)
            src = res.read() # source
               
            # 2. html 파싱
            src = src.decode('utf-8')
            html = BeautifulSoup(src, 'html.parser')
                
            # 3. tag[속성='값'] -> 'a[class="link_txt"]'
            links = html.select('a[class="link_txt"]')   
            
            one_page_data = [] # 빈 list
            
            print('date :', date)
            for link in links :
                link_str = str(link.string) # 내용 추출                
                one_page_data.append(link_str.strip()) # 1page news
            
            # 1day news 
            one_day_date.extend(one_page_data[:40])
        except Exception as e :
            print('오류 발생 : ', e)
    return one_day_date # list


# 3. Crawler 함수 호출    
year5_news_date = [ newsCrawler(date) for date in sdate]     
# [ [1day(1~5page)], [2day(1~5page)], ... , [29day(1~5page)]]   

year5_news_date
len(year5_news_date)










