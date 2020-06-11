# -*- coding: utf-8 -*-
"""
step01_Series.py

Series 객체 특징
 - 1차원의 배열구조(R의 vector)
 - 수학/통계 함수 제공
 - 범위 수정, 블럭 연산
 - indexing/slicing 기능
 - 시계열 데이터 생성
"""

import pandas as pd  # 별칭
from pandas import Series  # 패키지 import class

# 1. Series 객체 생성

# 1) list 이용
lst = [4000, 3000, 3500, 2000]
ser = pd.Series(lst)  # lst -> Series

print('list =', lst)  # list = [4000, 3000, 3500, 2000]
print('ser =\n', ser)
"""
ser =
 0    4000   : index   value
1    3000
2    3500
3    2000
dtype: int64
"""

# object.member
print(ser.index)  # RangeIndex(start=0, stop=4, step=1)  : 색인
print(ser.values)  # [4000 3000 3500 2000]  : 값
print(ser[0])  # 4000


ser1_2 = Series([4000,3000,3500,2000], index=['a','b','c','d'])
print(ser1_2)
"""
a    4000
b    3000
c    3500
d    2000
dtype: int64"""
print(ser1_2.index)  # Index(['a', 'b', 'c', 'd'], dtype='object')
print(ser1_2.values)  # [4000 3000 3500 2000]
print(pd.isnull(ser1_2))  # a    False b    False c    False d    False  dtype: bool
print(ser+ser1_2)  # 0   NaN  1   NaN  2   NaN  3   NaN  a   NaN  b   NaN  c   NaN  d   NaN  
ser1_3 = Series([4000,3000,3500,2000], index=['a',None, 'c','d'])
print(ser1_2 + ser1_3)
"""NaN       NaN
a      8000.0
b         NaN
c      7000.0
d      4000.0
dtype: float64"""


# 2) dict 이용
person = {'name':'홍길동', 'age':35, 'addr':'서울시'}
ser2 = Series(person)
print(ser2)
'''
name    홍길동     : 이때 key는 나중에 index의 역할을 수행.
age      35
addr    서울시
dtype: object
'''
print(ser2.index)  # Index(['name', 'age', 'addr'], dtype='object')  : 들어간 순서대로
print(ser2.values)  # ['홍길동' 35 '서울시']

# index 사용 : object[n or 조건식]
print(ser2['age'])  # 35

# boolean 조건식
print(ser[ser >= 3000])
"""0    4000
1    3000
2    3500
dtype: int64"""


# 2. indexing : list 동일
ser3 = Series([4,4.5,6,8,10.5])  # 클래스() : 생성자
print(ser3[0])  # 4.0
print(ser3[:3])  # 2번 인덱스까지.   0    4.0     1    4.5   2    6.0   dtype: float64
print(ser3[3:])  # 3~n.  3     8.0    4    10.5   dtype: float64
print(ser3[-1])  # KerError. 이게 list와 series 객체의 차이점. (-) 속성 사용 불가능


# 3. Series 결합과 NA 처리
p1 = Series([400, None, 350, 200], index=['a','b','c','d'])
p2 = Series([400, 150, 350, 200], index=['a','c','d', 'e'])

# Series 결합(연산)
p3 = p1+p2
print(p3)
"""
a    800.0
b      NaN  -> 결측치
c    500.0
d    500.0
e      NaN
dtype: float64"""  # 같은 인덱스 원소끼리는 사칙연산 가능


# 4. 결측치 처리 방법(평균, 0, 제거)
print(type(p3))  # <class 'pandas.core.series.Series'>

# 1) 평균 대체
p4 = p3.fillna(p3.mean())
print(p4)
"""a    800.0
b    600.0
c    500.0
d    500.0
e    600.0
dtype: float64""" # b와 e의 NaN 부분이 a, c, d의 평균으로 대체됨

# 2) 0 대체
p5 = p3.fillna(0)
print(p5)
"""a    800.0
b      0.0
c    500.0
d    550.0
e      0.0
dtype: float64"""

# 3) 결측치 제거
p6 = p3[pd.notnull(p3)]  # Subset 만들어주기
print(p6)
"""a    800.0
c    500.0
d    550.0
dtype: float64"""


# 5. 범위 수정, 블럭 연산
print(p2)
"""a    400
c    150
d    350
e    200
dtype: int64"""


# 1) 범위 수정
p2[1:3] = 300  # 범위 수정
print(p2)
"""a    400
c    300  -> 수정됨
d    300  -> 수정됨
e    200
dtype: int64"""

# 리스트에서는 범위 수정 사용 불가
lst = [1,2,3,4]
lst[1:3] = 3  # TypeError: can only assign an iterable


# 2) 블럭 연산
print(p2+p2)
"""a    800
c    600
d    600
e    400
dtype: int64"""
print(p2-p2)
"""a    0
c    0
d    0
e    0
dtype: int64"""

# 3) broadcast 연산(1차 vs 0차)
v1 = Series([1,2,3,4])
scala = 0.5


b = v1 * scala
print(b)
"""0    0.5
1    1.0
2    1.5
3    2.0
dtype: float64""" # 이것도 리스트는 불가능해서 for 문을 사용했음.

# 4) 수학/통계 함수를 제공함(Series)
print('sum =', v1.sum())  # sum = 10
print('mean =', v1.mean())  # mean = 2.5
print('var =', round(v1.var(),2)) # var = 1.67
print('std =', round(v1.std(),2)) # std = 1.29
print('max', v1.max())  # max 4


# 호출 가능한 멤버 확인
print(dir(v1))

print(v1.shape)  # (4,)  : 일차원의 자료구조이며 4개 원소
print(v1.size)  #  4































