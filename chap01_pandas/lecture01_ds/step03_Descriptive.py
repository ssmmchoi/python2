# -*- coding: utf-8 -*-
"""
- DataFrame의 요약통계량
- 상관계수
"""

import pandas as pd
product = pd.read_csv("C:\\ITWILL\\Work\\4_Python-II\\data\\product.csv")
product.info()
"""
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 264 entries, 0 to 263
Data columns (total 3 columns):
"""
product.head()
"""
   a  b  c
0  3  4  3
1  3  3  2
2  4  4  4
3  2  2  2
4  2  2  2
"""
product.shape  # (264, 3)


# 요약통계량
summ = product.describe()
print(summ)
"""
                a           b           c
count  264.000000  264.000000  264.000000
mean     2.928030    3.132576    3.094697
std      0.970345    0.859657    0.828744
min      1.000000    1.000000    1.000000
25%      2.000000    3.000000    3.000000
50%      3.000000    3.000000    3.000000
75%      4.000000    4.000000    4.000000
max      5.000000    5.000000    5.000000
"""

# 행/열 통계
product.sum(axis=0)  # 행축 열단위 합계
"""
a    773
b    827
c    817
dtype: int64
"""
product.sum(axis=1)  # 열축 행단위 합계
"""
0      10
1       8
2      12
3       6
4       6
       ..
259    11
260    10
261    12
262    12
263     8
Length: 264, dtype: int64
"""

# 산포도 : 분산, 표준편차
product.var()  # axis=0이 기본
"""
a    0.941569
b    0.739011
c    0.686816
dtype: float64
"""
product.std()  # axis=0이 기본
"""
a    0.970345
b    0.859657
c    0.828744
dtype: float64
"""

# 빈도수 : 집단변수
product['a']
product.a.head()
a_cnt = product['a'].value_counts()
print(a_cnt)
"""
3    126
4     64
2     37
1     30
5      7
Name: a, dtype: int64
"""
a_cnt.sum()  # 264

b_cnt = product['b'].value_counts()
print(b_cnt)
b_cnt.sum()

# 유일값 보기
product.c.unique()  #  array([3, 2, 4, 5, 1], dtype=int64)

# 상관관계
product.corr()  # 상관계수 행렬
"""
          a         b         c
a  1.000000  0.499209  0.467145
b  0.499209  1.000000  0.766853
c  0.467145  0.766853  1.000000
>> b,c 높은 상관관계, a,b/a,c 다소 높은 상관관계, 모두 양의 상관성을 가짐
"""

# iris dataset 적용
iris = pd.read_csv("iris.csv")  # 현재 경로(우측 상단)이 일치한다면 절대경로 꼭 쓸 필요 X
iris.info()
"""
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 150 entries, 0 to 149
Data columns (total 5 columns)
"""

iris_df = iris.iloc[:, 0:4]
print(iris_df.head())
iris_df.shape  # (150, 4)

iris_df.describe()
"""
       Sepal.Length  Sepal.Width  Petal.Length  Petal.Width
count    150.000000   150.000000    150.000000   150.000000
mean       5.843333     3.057333      3.758000     1.199333
std        0.828066     0.435866      1.765298     0.762238
min        4.300000     2.000000      1.000000     0.100000
25%        5.100000     2.800000      1.600000     0.300000
50%        5.800000     3.000000      4.350000     1.300000
75%        6.400000     3.300000      5.100000     1.800000
max        7.900000     4.400000      6.900000     2.500000
"""

# 상관계수 행렬
iris_df.corr()
"""
              Sepal.Length  Sepal.Width  Petal.Length  Petal.Width
Sepal.Length      1.000000    -0.117570      0.871754     0.817941
Sepal.Width      -0.117570     1.000000     -0.428440    -0.366126
Petal.Length      0.871754    -0.428440      1.000000     0.962865
Petal.Width       0.817941    -0.366126      0.962865     1.000000
"""

species = iris.Species
species.value_counts()
species.unique()

list(species.unique())


# exam04















