'''
1. news Crawling 
  - 3_Python-I -> chap08_Crawling -> step05_newsCrawling
  url : http://media.daum.net
2. pickle save
  binary file save
'''

import urllib.request as req # url 요청
import urllib.request as req
from bs4 import BeautifulSoup # html  파싱
from bs4 import BeautifulSoup

url = 'http://media.daum.net'
url = 'http://media.daun.net'

# 1. url 요청
res = req.urlopen(url)
res = req.urlopen(url)
res
src = res.read() # source
src = res.read()
print(src)

# 2. html 파싱
src = src.decode('utf-8')
src = src.decode('utf-8')
html = BeautifulSoup(src, 'html.parser')
html = BeautifulSoup(src, 'html.parser')
print(html)

# 3. tag[속성='값'] -> 'a[class="link_txt"]'
links = html.select('a[class="link_txt"]')
links = html.select('a[class="link_txt"]')
print(len(links)) # 62
print(links)

crawling_data = [] # 빈 list

for link in links :
    link_str = str(link.string) # 내용 추출
    print(link_str)
    crawling_data.append(link_str.strip()) # 문장 끝 불용어 처리(\n, 공백)

print(crawling_data) # list
print(len(crawling_data)) # 62

# 4. pickle file save
import pickle

# save
file = open("../data/new_crawling.pickle", mode='wb')
pickle.dump(crawling_data, file)
print('pickle file saved')



