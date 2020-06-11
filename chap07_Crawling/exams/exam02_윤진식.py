# -*- coding: utf-8 -*-
'''
# 문) 2019년11월 ~ 2020년2월 까지(4개월) daum 뉴스기사를 다음과 같이 크롤링하고, 단어구름으로 시각화 하시오.
# <조건1> 날짜별 5개 페이지 크롤링
# <조건2> 불용어 전처리 
# <조건3> 단어빈도수 분석 후 top 20 단어 단어구름 시각화 
'''
import urllib.request as req # url 요청
from bs4 import BeautifulSoup # html  파싱
import pandas as pd
import urllib.request as req
from konlpy.tag import Kkma
from wordcloud import WordCloud # class
from re import match, sub
from collections import Counter
import matplotlib.pyplot as plt
import pickle

#%% url query 생성
date = pd.date_range("2019-11-01", "2020-02-29")
mdate = [ sub('-','',str(d))[:8] for d in date]
mdate

#%% crawler 함수 정의

def crawler (date, pages = 5):
    one_day=[]
    for page in range(1,pages+1):
        try:
            # 1, url 요청
            url = f'https://news.daum.net/newsbox?regDate={date}&page={page}'
            src = req.urlopen(url).read()
            
            # 2, html 파싱
            src = src.decode('utf-8')
            html = BeautifulSoup(src, 'html.parser')
            
            # 3, tag[속성='값'] -> 'a[class="link_txt"]'
            links = html.select('a[class="link_txt"]')   
        
            one_page = [] # 빈 list

            print(date, page)
            for link in links :
                link_str = str(link.string) # 내용 추출
                one_page.append(link_str.strip()) # 문장 끝 불용어 처리(\n, 공백)
            one_day.extend(one_page[:40])
        except Exception as error:
            print(error)
    return one_day # list

#%% crawler 함수 호출
news_data = [ crawler(date) for date in mdate ]

#%% 문장 -> 단어
kkma = Kkma()
kkma.sentences(news_data)

dummy = []
for par in news_data:
    if len(par) > 1:
        for sent in par:
            dummy.append(sent)
    else:
        dummy.append(par)
news_data = dummy

nouns = []
for cnt1, sentence in enumerate(news_data):
    for cnt2, noun in enumerate(kkma.nouns(sentence)):
        nouns.append(noun)
        print(cnt1,cnt2)
        
len(nouns)

#%% 전처리 + 단어 카운트 : 음절이 한개, 서수로 시작하는 단어 제거
nouns_cnt = {}
for noun in nouns:
    if len(noun) > 1 and not match('^[0-9]',noun):
        nouns_cnt[noun] = nouns_cnt.get(noun,0) + 1
print(nouns_cnt)
len(nouns_cnt)
nouns_cnt['확진자'] = nouns_cnt['진자']

#%% 상위 20개 단어
top20 = Counter(nouns_cnt).most_common(20)

#%% wordcloud
wc = WordCloud(font_path='C:\Windows\Fonts\malgun.ttf',
               width = 1920, height = 1080,
               max_words = 100, max_font_size = 300,
               background_color = 'white')
# font : C:\Windows\Fonts\*.ttf
wc_res = wc.generate_from_frequencies(dict(top20)) # dict 형으로 인자 전달해야함
plt.axis('off')
plt.imshow(wc_res)