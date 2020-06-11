# -*- coding: utf-8 -*-
'''
# 문) 2019년11월 ~ 2020년2월 까지(4개월) daum 뉴스기사를 다음과 같이 크롤링하고, 단어구름으로 시각화 하시오.
# <조건1> 날짜별 5개 페이지 크롤링
# <조건2> 불용어 전처리 
# <조건3> 단어빈도수 분석 후 top 20 단어 단어구름 시각화 
'''

import urllib.request as req # url 요청
from bs4 import BeautifulSoup # html 파싱

import konlpy
from konlpy.tag import Kkma # class

from wordcloud import WordCloud # clas
import pickle

date = pd.date_range("2019-11-01", "2020-03-01")
sdate = [re.sub('-','',str(d))[:8] for d in date]




def Crawling(date, pages = 5):
    
    one_day_data = []
    for page in range(pages + 1):
        url = f'https://news.daum.net/newsbox?regDate={date}&page={page}'
    
        src = req.urlopen(url).read().decode('utf-8')
        html = BeautifulSoup(src, 'html.parser')
        
        links =html.select('a[class="link_txt"]')
        
        one_page_data = []
        
        for link in links:
            link_str = str(link.string)
            one_page_data.append(link_str.strip())
            
        one_day_data.extend(one_page_data[:10])
    print(date) 
    return one_day_data[:5]

data = [Crawling(date)[0]  for date in sdate]   


kkma = Kkma()
nouns_word = []
for sent in data:
    for noun in kkma.nouns(sent):
        nouns_word.append(noun)

from re import match
nouns_count = {}

for noun in nouns_word:
    if len(noun) > 1 and not(match('^[0-9]', noun)):
        nouns_count[noun] = nouns_count.get(noun, 0) + 1


from collections import Counter # class

word_counter = Counter(nouns_count) # dict
top50_word = word_counter.most_common(50)
top50_word


wc = WordCloud(font_path = 'C:/Windows/Fonts/malgun.ttf',
          width = 500, height = 400, max_words = 200, max_font_size = 200,
          background_color = 'black')

wc_result = wc.generate_from_frequencies(dict(top50_word)) # dict
import matplotlib.pyplot as plt
plt.axis('off')
plt.imshow(wc_result)




