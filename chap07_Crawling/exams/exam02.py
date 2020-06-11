# -*- coding: utf-8 -*-
'''
# 문) 2019년11월 ~ 2020년2월 까지(4개월) daum 뉴스기사를 다음과 같이 크롤링하고, 단어구름으로 시각화 하시오.
# <조건1> 날짜별 5개 페이지 크롤링
# <조건2> 불용어 전처리 
# <조건3> 단어빈도수 분석 후 top 20 단어 단어구름 시각화 
'''
import urllib.request as req # url 요청
from bs4 import BeautifulSoup # html  파싱
import pandas as pd # 시계열 date
from konlpy.tag import Kkma # class 



# <조건1> 날짜별 5개 페이지 크롤링

date = pd.date_range("2019-11", "2020-02-28") 
len(date)
date


import re
sdate = [re.sub('-', '', str(d))[:8] for d in date]
sdate[:10]
sdate[-10:]



def newsCrawler(date, pages=5) :
    
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

month4_news_date = [ newsCrawler(date) for date in sdate]     

month4_news_date
len(month4_news_date)
type(month4_news_date)

month4_news = [news[0] for news in month4_news_date]
month4_news
len(month4_news)


kkma = Kkma()
ex_sent = [kkma.sentences(row)[0] for row in month4_news]



# <조건2> 불용어 전처리 

# nouns_word = [] # 명사 저장 

# for sent in ex_sent : # '형태소 분석을 시작합니다.'
#     for noun in kkma.nouns(sent) : # 문장 -> 명사 
#         nouns_word.append(noun)
        
# nouns_word
# len(nouns_word)


from re import match    

nouns_word = []

for sent in ex_sent :  # 11600번
    word_vec = ""
    for noun in kkma.nouns(sent) :  # 문장에서 명사만 추출
        if len(noun) >1 and not(match('^[0-9]', noun)) :
            word_vec += noun + " "   # 문장 내에서 명사들을 띄어쓰기 단위로 append
    print(word_vec)
    nouns_word.append(word_vec)



# 전처리 + 단어 카운트 : 단어 길이 제한(1음절), 숫자 제외
from re import match
 
nouns_count = {} # 단어 카운트 

for noun in nouns_word : 
    if len(noun) > 1 and not(match('^[0-9]', noun)) : 
        # key[noun] = value[출현빈수]
        nouns_count[noun] = nouns_count.get(noun, 0) + 1
        
nouns_count
len(nouns_count) # 12,194


# word cloud -> 수작업 
# nouns_count['확진자'] = nouns_count['진자']
# del nouns_count['진자']



















