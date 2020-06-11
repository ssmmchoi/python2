# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 15:22:36 2020

@author: user
"""
"""
DataFrame 자료구조 특징
 - 2차원 행렬구조(table 유사함)
 - 열(칼럼) 단위 데이터 처리가 용이함
 - Series(1차원)의 모음 <-> DataFrame(2차원)
"""

import pandas as pd
from pandas import Series, DataFrame


# 1. DataFrame 생성

# 1) 기본 자료 구조(list, dict) 이용
name = ['hong', 'lee', 'kang', 'yoo']  # list(1 dim)
age = [35,45,55,25]
pay= [250,350,450,200]
addr = ['서울시', '부산시', '대전시', '인천시']
data = {'name' : name, 'age' : age, 'pay' : pay, 'addr' : addr}

frame = pd.DataFrame(data = data, columns=['name', 'age', 'addr', 'pay'], index=[0,1,2,3])
print(frame)
"""
   name  age addr  pay
0  hong   35  서울시  250
1   lee   45  부산시  350
2  kang   55  대전시  450
3   yoo   25  인천시  200 """
print(frame['name'])
"""
0    hong
1     lee
2    kang
3     yoo
Name: name, dtype: object  """
print(frame['name'][0])  # hong
#print(frame.ix[0])  # SyntaxError

age = frame['age']  # frame.age
print(age,'\n', age.mean())
"""0    35
1    45
2    55
3    25
Name: age, dtype: int64
 40.0"""
print(type(age))  # <class 'pandas.core.series.Series'> 시리즈!

# 새 컬럼 추가
gender = Series(['남','남','남','여'])  # 1차원
frame['gender'] = gender
print(frame)
"""
   name  age addr  pay gender
0  hong   35  서울시  250      남
1   lee   45  부산시  350      남
2  kang   55  대전시  450      남
3   yoo   25  인천시  200      여 """


# 2) numpy 이용 : 선형대수 관련 함수
import numpy as np

frame2 = DataFrame(np.arange(12).reshape(3,4), columns=['a','b','c','d'])   # .reshape(행, 열)
print(frame2)
"""
   a  b   c   d
0  0  1   2   3
1  4  5   6   7
2  8  9  10  11"""

# 행/열 통계 구하기
frame2.mean(axis = 0)  # 행축 : 열단위
"""a    4.0
b    5.0
c    6.0
d    7.0
dtype: float64"""

frame2.mean(axis = 1)  # 열축 : 행단위
"""0    1.5
1    5.5
2    9.5
dtype: float64"""


# 2. DataFrame 칼럼 참조
frame2.index  # RangeIndex(start=0, stop=3, step=1)  : 행이름
frame2.values
"""
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11]])""" # : 값 : array라는 함수 형태로 나온당.
                            # 중첩 리스트임. 각 내부 리스트는 각 행을 의미함. ]]2개. 2차원

# emp.csv 호출
import os
os.getcwd()  # 'C:\\ITWILL\\Work\\4_Python-II\\data'
emp = pd.read_csv("C:\\ITWILL\\Work\\4_Python-II\\data/emp.csv", encoding='utf-8')
print(emp)
print(emp.info())  # str(emp)
"""
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 5 entries, 0 to 4
Data columns (total 3 columns):
 #   Column  Non-Null Count  Dtype 
---  ------  --------------  ----- 
 0   No      5 non-null      int64 
 1   Name    5 non-null      object
 2   Pay     5 non-null      int64 
dtypes: int64(2), object(1)
memory usage: 248.0+ bytes
None
"""
emp.head(3)


# 1) 단일 카럼 선택
print(emp["No"])
print(emp.No)  # 칼럼명에 점 포함 X
print(emp.No[1:])  # No의 1~5번째 행 추출(특정 원소 선택)

no = emp.No
no.plot()
pay = emp['Pay']
pay.plot()

# 2) 복수 칼럼 선택 : 중첩 list
print(emp[["No", "Pay"]])
#print(emp[["No" : "Name"]])  # SyntaxError 연속되어도 콜론으로 표시 불가능 : 행렬로 인식
print(emp[["No", "Name"]])

emp[['No', 'Pay']].plot()


# 3. subset 만들기 : old DF -> new DF

# 1) 특정 컬럼 제외 : 칼럼이 적은 경우
emp.info()
subset1 = emp[['Name', 'Pay']]
print(subset1)

# 2) 특정 행 제외 
subset2 = emp.drop(0)
print(subset2)
"""
    No Name  Pay
1  102  이순신  450
2  103  강감찬  500
3  104  유관순  350
4  105  김유신  400"""

#3) 조건식으로 행 선택
subset3 = emp[emp.Pay > 350]
print(subset3)

# 4) columns 이용 : 칼럼이 많은 경우
iris = pd.read_csv('C:/ITWILL/Work/4_Python-II/data/iris.csv')
print(iris.info())
print(iris.head())


iris['Sepal.Width']
#iris.Sepal.Width  # AttributeError. 칼럼명에 점이 있어서 이런식으로 호출 안됨

cols = list(iris.columns)  # 칼럼명 추출
print(cols)
"""
Index(['Sepal.Length', 'Sepal.Width', 'Petal.Length', 'Petal.Width',
       'Species'],
      dtype='object') """
type(cols)  # list

iris_x = cols[:4]
iris_y = cols[4]
print(iris_x, iris_y)
iris_y = cols[-1]
print(iris_y)  # Species

# x, y변수 선택
x = iris[iris_x]
y = iris[iris_y]
x.shape  # (150, 4)  : 2차원
y.shape  # (150,)  : 1차원

x.head()
y.head(); y.tail()

# exam01~ exam02


# 4. DataFrame 행렬 참조 : DF[row, col]
# 1) DF.loc[row, col]  : label index(칼럼과 행 이름)
# 2) DF.iloc[row, col]  : integer index

emp
"""
    No Name  Pay
0  101  홍길동  150
1  102  이순신  450
2  103  강감찬  500
3  104  유관순  350
4  105  김유신  400
>> 열 이름 : No Name  Pay
   행 이름 : 0 ~ 4
"""

# loc[행labelindex, 열labelindex]
emp.loc[1:3,]  # loc 방식에서는 1:3 인덱스를 부여하면 결과도 1:3까지 모두 출력됨. 행이름을 입력해준 것이나 마찬가지.
emp.loc[1:3, :]  # 위와 같다.
emp.loc[1:3]  # 역시 위와 같다.
emp.loc[1:3, 'No':'Name']
#emp.loc[1:3, 'No', 'Pay']  # IndexingError. 3차원으로 인식함
emp.loc[1:3, ['No', "Pay"]]
"""
    No  Pay
1  102  450
2  103  500
3  104  350
"""

# iloc[행숫자index, 열숫자index]
emp.iloc[1:3]  # 숫자 index 1~2째 행
"""
    No Name  Pay
1  102  이순신  450
2  103  강감찬  500
"""
emp.iloc[1:3, 0:2]
"""
    No Name
1  102  이순신
2  103  강감찬
"""
emp.iloc[1:3, :2]
"""
    No Name
1  102  이순신
2  103  강감찬
"""
emp.iloc[:, [0,2]]
"""
    No  Pay
0  101  150
1  102  450
2  103  500
3  104  350
4  105  400
"""
#emp.iloc[1:3, ['No', "Pay"]]  # IndexError: .iloc requires numeric indexers, got ['No' 'Pay']

##################################
## DF 행렬참조 example
##################################
iris.shape  #  (150, 5)

from numpy.random import choice

help(choice)  # choice(a, size=None, replace=True, p=None)

row_idx = choice(a=len(iris), size=int(len(iris)*0.7), replace=False)  # 비복원추출
print(row_idx)
"""
[ 96 128 106  72 149  62   4  88 130 143 104 112 142  70  66   3  93 127
 111 109 113  43  32 119  30   2  44  16 138  23  86  89   6  80  65 124
  85 123  47 126  83  15 125  75 105  13  35  53  18  63  81   1  71 108
  97  61  82  46  42   9  19  28  39 117 114   8  74  95 102 140  64  92
  27  11  10 146  22 134  87  94  41  12 115  91 129  54  79 139  40 110
  99  25  21 148  50  45 136  68  24  31 116  29   0 144  33]
"""
len(row_idx)  # 105개

# train dataset
train_set = iris.iloc[row_idx]  # 고른 인덱스 그 이름 그대로
train_set.head()
"""
     Sepal.Length  Sepal.Width  Petal.Length  Petal.Width     Species
96            5.7          2.9           4.2          1.3  versicolor
128           6.4          2.8           5.6          2.1   virginica
106           4.9          2.5           4.5          1.7   virginica
72            6.3          2.5           4.9          1.5  versicolor
149           5.9          3.0           5.1          1.8   virginica
"""

train_set2 = iris.loc[row_idx]  # 숫자 인덱스로. 결과는 그대로임
print(train_set2)
train_set2.head()
"""
     Sepal.Length  Sepal.Width  Petal.Length  Petal.Width     Species
96            5.7          2.9           4.2          1.3  versicolor
128           6.4          2.8           5.6          2.1   virginica
106           4.9          2.5           4.5          1.7   virginica
72            6.3          2.5           4.9          1.5  versicolor
149           5.9          3.0           5.1          1.8   virginica
"""
train_set2.shape  # (105, 5)

# test dataset :  list + for
test_idx = [i for i in range(len(iris)) if not i in row_idx]
len(test_idx)  # 45

test_set = iris.iloc[test_idx]
test_set.shape  # (45, 5)


# x, y 변수 분리
cols=list(iris.columns)
x_cols = cols[:4]
y_col = cols[-1]
print(y_col)

iris_x = iris.loc[test_idx, x_cols]  # loc만 사용 가능. index의 구조 때문
iris_y = iris.loc[test_idx, y_col]
iris_x.shape  # (45, 4)
iris_y.shape  # (45,)






















