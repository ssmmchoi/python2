# -*- coding: utf-8 -*-
"""
Numpy 패키지 특징kernel76d9d12735
 - 선형대수(벡터, 행렬) 연산 관련 함수 제공
 - list보다 이점 : n차원 배열 생성, 선형대수연산, 고속처리
 - Series 공통점
  -> 수학/통계 함수 지원
      ex) obj.수학/통계()
  -> 범위 수정, 블럭연산
  -> indexing, slicing
 - 주요 모듈과 함수
    1. random : 난수 생성 함수
    2. array 함수 : n차원 배열 생성(array([[list]])) : 대괄호 수 = n
    3. sampling 함수 
    4. arange : 기본함수 range()와 유사함
    
그외 판타스와 넘파이에 관한 모든 내용은 https://www.scipy.org 참조
"""

import numpy as np

# list 자료구조 - 선형대수가 불가능한 자료구조
lst = [1,2,3]
#lst**2  # TypeError: unsupported operand type(s) for ** or pow(): 'list' and 'int'

lst2 = []
for i in lst :
    lst2.append(i**2)
print(lst2)

# list -> numpy  모양은 같아보여도 연산과정이 간편해진다.
arr = np.array(lst)
arr  # array([1, 2, 3])
arr**2  # array([1, 4, 9], dtype=int32)

# 동일 type
arr = np.array([1,'two',3])
arr  # array(['1', 'two', '3'], dtype='<U11') : 1,3이 동일하게 문자열 타입으로 바뀌었음

arr2 = np.array([[1,'two', 3]])
arr2.shape  # (1, 3) 2차원. 대괄호의 수


# 1. 모듈 random : 난수 생성 함수
data = np.random.randn(3,4)  # 모듈.모듈.함수() randomnormal 표준정규분포를 따르는 난수, 3행 4열의 12개 난수를 생성한다.
data
"""array([[-0.94432324, -0.5987548 , -0.59014313, -0.32074148],
       [ 0.09261328,  0.60832648, -1.23740264, -0.22847465],
       [ 1.15640141, -1.67136838, -0.48281411,  0.36456969]])"""  # 대괄호 2개가 중첩되어있음. 2차원

cnt = 0
for row in data :
    cnt += 1
    print(cnt, '째 행 행단위 합계 : ', row.sum(), sep='')
    print(cnt, '째 행 행단위 평균 : ', row.mean(),'\n', sep='')
"""
1째 행 행단위 합계 : -2.4539626519241002
1째 행 행단위 평균 : -0.6134906629810251

2째 행 행단위 합계 : -0.7649375375524636
2째 행 행단위 평균 : -0.1912343843881159

3째 행 행단위 합계 : -0.6332114001216296
3째 행 행단위 평균 : -0.1583028500304074"""

# 1) 수학/통계 함수 지원
type(data)  # numpy.ndarray  : 데이터의 소속(출처) 확인 가능
print(data.sum())  # -3.8521115895981937 : 난수 12개 전체의 합계
print(data.mean())  # -0.3210092991331828
print(data.var(), data.std())  # 0.5769662798941809 0.7595829644575903

dir(data)  # data객체에서 어떤 모듈은 호출할수있는지
data.shape  # (3, 4)
data.size  # 12  : 전체 원소의 개수
# 뒤에 괄호가 있는것은 메소드, 괄호가 없는 것은 멤버

# 2) 범위수정, 블럭연산
data + data
data - data

# 3) indexing : R과 유사하나 0부터 시작
data[0]  # array([-0.94432324, -0.5987548 , -0.59014313, -0.32074148])\data
data[:,0]  # array([-0.94432324, -0.5987548 , -0.59014313, -0.32074148])
data[0,1]  # -0.598754801598203
data[1,0:2]  # array([0.09261328, 0.60832648])


# 2. array 함수 : n차원 배열 생성

# 1) 단일 list
lst1 = [3,5.6,4,7,8]
lst1

# list -> array(numpy 객체)
arr1 = np.array(lst1)
arr1  # array([3. , 5.6, 4. , 7. , 8. ])

arr1.var()  # 3.4016000000000006
arr1.std()  # 1.8443427013437608

# 2) 중첩 list
lst2 = [[1,2,3,4,5], [2,3,4,5,6]]
lst2
lst2[0]  # [1, 2, 3, 4, 5]
lst2[0][2]  # 3

arr2 = np.array(lst2)
arr2
"""array([[1, 2, 3, 4, 5],
       [2, 3, 4, 5, 6]])"""
arr2[0]  # array([1, 2, 3, 4, 5])
arr2[0,2]  # 3
arr2.shape  # (2, 5)

# index : obj[행index, 열index]
arr2[1, :]  # array([2, 3, 4, 5, 6])
arr2[:, 1]  # array([2, 3])
arr2[0:2, 2:4]
"""
array([[3, 4],
       [4, 5]])"""


# broadcast 연산
# - 작은 차원이 큰 차원으로 늘어난 후 연산

# 1 scala(0) vs vector(1)
arr1  # array([3. , 5.6, 4. , 7. , 8. ])
0.5 * arr1  # array([1.5, 2.8, 2. , 3.5, 4. ])  : 0.5가 array의 길이만큼 스트레칭되어 연산되는것

# 2) scala(0) vs matrix(2)
0.5 * arr2
"""
array([[0.5, 1. , 1.5, 2. , 2.5],
       [1. , 1.5, 2. , 2.5, 3. ]])
"""


# 3) vector(1) vs matrix(2)
print(arr1.shape, arr2.shape)  # (5,) (2, 5)
arr3 = arr1 + arr2
print(arr3)
"""
[[ 4.   7.6  7.  11.  13. ]
 [ 5.   8.6  8.  12.  14. ]]
"""


# 3. sampling(random) 함수
num = list(range(1,11))
num  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

help(np.random.choice)
"""
a : 관측치 길이
size : 임의 추출 크기
replace : 복원 or 비복원
p: 확률 
"""
  # 모듈.모듈.함수
print(idx)  # [6 9 0 5 4]

import pandas as pd
score = pd.read_csv("C:\\ITWILL\\Work\\4_Python-II\\data\\score_iq.csv")
score.info()
len(score)  # 150

idx = np.random.choice(a=len(score), size=int(len(score)*0.3), replace = False)
idx
len(idx)  # 45

# DataFrame index
score_train = score.iloc[idx, :]
score_train.shape  # (45, 6)

# pandas(DF) -> numpy(array)
score_arr = np.array(score)
score_arr
score_arr.shape  # (150, 6)

#score_train2 = score_arr.iloc[idx, :]  # AttributeError: 'numpy.ndarray' object has no attribute 'iloc'
score_train2 = score_arr[idx, :]
score_train2.shape  #  (45, 6)


# test set
test_idx = [i for i in range(len(score)) if i not in idx]
len(test_idx)  # 105
score_test = score.iloc[test_idx, :]
score_test.shape  # (105, 6)


# 4. arange : 기본함수 range()와 유사함

# 제로행렬 만들기 : 모든 원소가 0로 이루어진 행렬
zero_arr = np.zeros((3,5))
zero_arr
"""
array([[0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0.]])
"""

cnt = 1
for i in range(3) :  # 행 index 0~2
    for j in range(5) :  # 열 index 0~4
       zero_arr[i,j] = cnt
       cnt += 1
zero_arr
"""
array([[ 1.,  2.,  3.,  4.,  5.],
       [ 6.,  7.,  8.,  9., 10.],
       [11., 12., 13., 14., 15.]])
"""

cnt = 1
for i in np.arange(3):
    for j in np.arange(5) :
        zero_arr[i,j] = cnt
        cnt += 1
zero_arr
"""
array([[ 1.,  2.,  3.,  4.,  5.],
       [ 6.,  7.,  8.,  9., 10.],
       [11., 12., 13., 14., 15.]])
"""

# range의 경우 
#range(-1.0, 2, 0.1)  # (start, stop, step)
# 는 안됨. 음수 불가능, TypeError: 'float' object cannot be interpreted as an integer
np.arange(-1.0, 2, 0.1)
"""
array([-1.00000000e+00, -9.00000000e-01, -8.00000000e-01, -7.00000000e-01,
       -6.00000000e-01, -5.00000000e-01, -4.00000000e-01, -3.00000000e-01,
       -2.00000000e-01, -1.00000000e-01, -2.22044605e-16,  1.00000000e-01,
        2.00000000e-01,  3.00000000e-01,  4.00000000e-01,  5.00000000e-01,
        6.00000000e-01,  7.00000000e-01,  8.00000000e-01,  9.00000000e-01,
        1.00000000e+00,  1.10000000e+00,  1.20000000e+00,  1.30000000e+00,
        1.40000000e+00,  1.50000000e+00,  1.60000000e+00,  1.70000000e+00,
        1.80000000e+00,  1.90000000e+00])
"""





























