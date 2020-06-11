# -*- coding: utf-8 -*-
"""
1. group 객체에 외부 함수 적용
  - obj.apply()
  - obj.agg([func1, func2, func3, ...]) : 여러개의 외부함수를 하나의 객체에 동시 적용.

2. data 정규화
"""
import pandas as pd

# 1. group 객체에 외부 함수 적용
"""
apply vs agg
 - 공통점 : 그룹 obj(또는 일반 DF obj)에 외부 함수를 적용한다.
 - 차이점 : 적용할 함수의 개수
"""

# apply()
test = pd.read_csv("C:\\ITWILL\\Work\\4_Python-II\\data\\test.csv")
test.info()
"""
 #   Column  Non-Null Count  Dtype 
---  ------  --------------  ----- 
 0   key     6 non-null      object
 1   data1   6 non-null      int64 
 2   data2   6 non-null      int64 
 """
 
grp = test['data2'].groupby(test['key'])
grp.size()
"""
a    3
b    3
"""
grp.head(6)
grp.sum()
grp.max()  # a    100,  b    200
grp.min()  # a    100,  b    100

# 사용자 정의함수
def diff(grp) :
    result = grp.max() - grp.min()
    return result

# 그룹객체 내장함수 먼저 적용해보자. mean의 경우는 통계관련 패키지를 따로 임포트해줘야함
grp.apply(sum)
grp.apply(max)
grp.apply(min)

# 사용자함수 적용
grp.apply(diff)    
"""
a      0
b    100 """

# obj.agg([func1, func2, func3, ...]) 
agg_func = grp.agg([max, min, diff])
agg_func
"""
     max  min  diff
key                
a    100  100     0
b    200  100   100
"""

# 2. data 정규화
#  - 다양한 특징을 갖는 변수(x변수/독립변수)를 대상으로 일정한 범위(주로 0~1)로 조정
#  - x(30개) -> y

import numpy as np  # max, min, log  : np것은 indexing 가능, 기본 빌트인의 함수는 포문으로 작성해야함.

# 1) 사용자 정의 함수 : 0~1
def normal(x) :
    n = (x-np.min(x)) / (np.max(x) - np.min(x))
    return n

x = [10,20000,-100,0]

normal(x)  # array([0.00547264, 1.        , 0.        , 0.00497512])

# 2) 자연 log  : 밑수 e : 음수, 영 -> 결측치, -무한대
e = np.exp(1)
e  # 2.718281828459045

# 로그 -> 지수값 (8=2^3)
np.log(10)  # 밑수 e : 2.302585092994046 -> e^2.3025 = 10이여야.
e**2.3025  # 9.999149106262605

# 지수 -> 로그값
np.exp(2.302585092994046)  # 10.000000000000002

"""
로그 vs 지수 : 역함수 관계
  - 로그 : 지수값 반환
  - 지수 : 로그값 반환
"""


np.log(x)  # array([2.30258509, 9.90348755,        nan,       -inf])

import seaborn as sns
sol = np.log1p(x)
print(sol)
seedist = sns.distplot(sol)



iris = pd.read_csv("C:\\ITWILL\\Work\\4_Python-II\\data\\iris.csv")

# 전체 칼럼명 가져오기
cols = list(iris.columns)
cols  # ['Sepal.Length', 'Sepal.Width', 'Petal.Length', 'Petal.Width', 'Species']
cols[0]
cols[4]

iris_x = iris[cols[:4]]
iris_x.shape   # (150, 4)
iris_x.head()

# x변수 정규화
iris_x_nor = iris_x.apply(normal)
iris_x_nor

iris_x.agg(['var', 'mean', 'max', 'min'])
