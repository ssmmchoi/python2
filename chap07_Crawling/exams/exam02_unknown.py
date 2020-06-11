'''
# 문) 2019년11월 ~ 2020년2월 까지(4개월) daum 뉴스기사를 다음과 같이 크롤링하고, 단어구름으로 시각화 하시오.
# <조건1> 날짜별 5개 페이지 크롤링
# <조건2> 불용어 전처리 
# <조건3> 단어빈도수 분석 후 top 20 단어 단어구름 시각화 
'''

import urllib.request as req # url 요청
from bs4 import BeautifulSoup # html  파싱
import pandas as pd # 시계열 date
import re
from konlpy.tag import Kkma # class 
from wordcloud import WordCloud # class 
from re import match
from collections import Counter # class 
import matplotlib.pyplot as plt 
import numpy as np

# object 생성 
kkma = Kkma()


# <조건1> 날짜별 5개 페이지 크롤링
date = pd.date_range("2019-11-01", "2020-02-29") 
sdate = [re.sub('-', '', str(d))[:8]  for d in date]

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
            for link in links :
                link_str = str(link.string) # 내용 추출                
                one_page_data.append(link_str.strip()) # 1page news      
            # 1day news 
            one_day_date.extend(one_page_data[:40])
        except Exception as e :
            print('오류 발생 : ', e)
    return one_day_date # list
news_date = []
for date in sdate:
    news_date.extend(newsCrawler(date,5))
np.array(news_date).shape # (24200,)
ex_sent = [kkma.sentences(sent)[0] for sent in news_date] 


# <조건2> 불용어 전처리 
nouns_word = [] # 명사 저장 
for sent in ex_sent : 
    for noun in kkma.nouns(sent) : # 문장 -> 명사 
        nouns_word.append(noun)

nouns_count = {} # 단어 카운트 
for noun in nouns_word : 
    if len(noun) > 1 and not(match('^[0-9]', noun)) : 
        nouns_count[noun] = nouns_count.get(noun, 0) + 1  
nouns_count['확진자'] = nouns_count['진자']
del nouns_count['진자']

# <조건3> 단어빈도수 분석 후 top 20 단어 단어구름 시각화 
word_count = Counter(nouns_count) # dict 
top20_word = word_count.most_common(20)
 
wc = WordCloud(font_path='C:/Windows/Fonts/malgun.ttf',
          width=800, height=600,
          max_words=100,max_font_size=200,
          background_color='white')
wc_result = wc.generate_from_frequencies(dict(top20_word)) # dict

plt.figure(figsize=(12,8))
plt.imshow(wc_result)
plt.axis('off') # x.y축 눈금 감추기 
plt.show()







