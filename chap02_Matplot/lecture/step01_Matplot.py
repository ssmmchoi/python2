# -*- coding: utf-8 -*-
"""
matplotlib API 사용 차트 그리기
 형식) plt.plot(data); plt.show()
@author : user

1. 기본차트 그리기
2. 산점도 그리기
3. subplot 
"""
import matplotlib.pyplot as plt

# 차트에서 한글 지원 
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)
# 음수 부호 지원 
import matplotlib
matplotlib.rcParams['axes.unicode_minus'] = False
import pandas as pd  # file read

import numpy as np  # 숫자 데이터 생성

# 1. 기본차트 그리기
help(plt.plot)
#plot(x, y)        # plot x and y using default line style and color
#plot(x, y, 'bo')  # plot x and y using blue circle markers
#plot(y)           # plot y using x as index array 0..N-1
#plot(y, 'r+')     # ditto, but with red plusses

data1 = np.arange(10)  # 0 ~ 9
data1
plt.plot(data1, 'r+')
plt.show()


# 평균0, 표준편차1 표준정규분포
data2 = np.random.randn(10)  
plt.plot(data1, data2)  # x, y
plt.show()

plt.plot(data1, data2, 'ro')
plt.show()


# 2. 산점도 그리기
# 단색 산점도
plt.scatter(data1, data2, c='r', marker='o')
plt.show()

# 여러가지 색상 산점도
cdata = np.random.randint(1, 4, 10)
cdata  # array([2, 1, 2, 2, 1, 2, 3, 1, 1, 3])

plt.scatter(data1, data2, c=cdata, marker='o')
plt.show()


# 3. subplot 이용 차트 그리기
fig = plt.figure(figsize=(5,3))
x1 = fig.add_subplot(2,2,1)
x2 = fig.add_subplot(2,2,2)
x3 = fig.add_subplot(2,2,3)
x4 = fig.add_subplot(2,2,4)

# data 생성
data3 = np.random.randint(1,100,100)
data4 = np.random.randint(10,110,100)
cdata = np.random.randint(1,4,100)

# 첫번째 격자 : 히스토그램
x1.hist(data3)
plt.show()

# 두번째 격자 : 산점도
x2.scatter(data3, data4, c=cdata)
plt.show()

# 세번째 격자 : 선 그래프
x3.plot(data3)
plt.show()

# 네번째 격자 : 점선 그래프
x4.plot(data4, 'g--')


# 4. 차트 크기 지정, 2개 이상의 차트 그리기
fig = plt.figure(figsize=(12,5))

chart = fig.add_subplot()  # (1,1,1) default

#계단스타일 차트
chart.plot(data1, color='r', label='step', drawstyle='steps-post')

# 선스타일 차트
chart.plot(data2, color='b', label='line')

# 차트 제목
plt.title('계단형 vs 선 스타일')
plt.xlabel('데이터')
plt.ylabel('난수 정수')
plt.legend(loc='best')  # 범례
plt.show()





































