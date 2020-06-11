# -*- coding: utf-8 -*-
"""
피벗테이벌(pivot table)
 - 사용자가 행, 열 그리고 교차셀에 변수를 지정하여 테이블 생성
"""

import pandas as pd

pivot_data = pd.read_csv("C:\\ITWILL\\Work\\4_Python-II\\data\\pivot_data.csv")
pivot_data
pivot_data.info()
"""
교차셀 : 매출액(price)
행 : 년도(year), 분기(quarter)
열 : 매출규모(size)
셀에 적용할 통계 : sum
"""

ptable = pd.pivot_table(pivot_data, values = 'price', index = ['year', 'quarter'],
               columns = 'size', aggfunc = 'sum')
ptable
"""
size          LARGE  SMALL
year quarter              
2016 1Q        2000   1000
     2Q        2500   1200
2017 3Q        2200   1300
     4Q        2800   2300
"""
ptable.shape  # (4, 2)

ptable.plot(kind='barh', title='2016 vs 2017')
ptable.plot(kind='barh', title='2016 vs 2017', stacked = True)



# movie_rating.csv
# 행 : critic
# 열 : title
# 셀 : rating
# 적용할 함수 : mean

rating = pd.read_csv("C:\\ITWILL\\Work\\4_Python-II\\data\\movie_rating.csv")
r_table = pd.pivot_table(rating, values='rating', index='critic', columns='title', aggfunc='mean')
r_table

r_table.plot(kind = 'bar', title = 'movie ratings : critic x title')
r_table.plot(kind = 'barh', title = 'movie ratings : critic x title')


r_table2 = pd.pivot_table(rating, values='rating', index='title', columns='critic', aggfunc='mean')
r_table2
r_table2.plot(kind = 'barh', title = 'movie ratings : title x critic')

r_table.mean()  # 영화별 평균평점. superman이 가장 좋다.
# or!
r_table.mean(axis=0)

# 평가자 별 평균을 확인하려면
r_table.mean(axis=1)
























