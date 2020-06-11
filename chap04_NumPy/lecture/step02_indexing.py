# -*- coding: utf-8 -*-
"""
indexing/slicing 
 - 1차원 indexing : list 동일함
 - 2, 3차 indexing
 - boolean indexing
"""

import numpy as np

# 1. indexing
'''
1차원 : obj[index]
2차원 : obj[행index, 열index]
3차원 : obj[면index, 행index, 열index]
'''

# 1) list 객체
ldata = [0,1,2,3,4,5]
ldata
#ldata[:] = 10  # TypeError: can only assign an iterable
ldata[:]  # 전체 원소
ldata[2:] # [n:~]
ldata[:3] # [~:n-1]
ldata[-1] # 5

# 2) numpy 객체
arr1d = np.array(ldata)
arr1d.shape  # (6,)
arr1d[2:]
arr1d[:3]
arr1d[-1]


# 2. sclicing
arr = np.array(range(1,11))
arr  # array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10])  : 원본

arr_sl = arr[4:8]
arr_sl  # array([5, 6, 7, 8])  : 사본
# 블럭 수정
arr_sl[:] = 50
arr_sl  # array([50, 50, 50, 50])

arr  # array([ 1,  2,  3,  4, 50, 50, 50, 50,  9, 10]) 원본에서도 수정됨.
# 1차원 array의 slicing은 slicing한 객체를 수정하면 원본도 수정된다.******************************

# 2, 3차 indexing
arr2d = np.array([[1,2,3], [2,3,4], [3,4,5]])
arr2d
arr2d.shape  # (3,3)

 # 행 index : default
arr2d[1]  # array([2, 3, 4])  = arr2d[1, :]
arr2d[1:]  # 2~3 행
arr2d[:, 1:]  # 2~3 열,  행 자리는 생략할 수 없다.
arr2d[2,1]  # 3행 2열
arr2d[1:, 1:]
arr2d[:2, 1:]

# [면, 행, 열] : 면 index : default
arr3d = np.array( [ [[1,2,3], [2,3,4], [3,4,5]],
                   [[2,3,4], [3,4,5], [6,7,8]] ] )  # 2, 3, 3
arr3d.shape  # (2, 3, 3)
arr3d
"""
array([[[1, 2, 3],
        [2, 3, 4],        1면 덩어리
        [3, 4, 5]],                      \
                                           둘다 3행 3열
       [[2, 3, 4],                       /
        [3, 4, 5],        2면 덩어리       
        [6, 7, 8]]])
"""

arr3d[0]  # 면 index = 1면

# 면 -> 행 index
arr3d[0,2]  # array([3, 4, 5])

# 면 -> 행 -> 열 index
arr3d[1,2,2]  # 8

arr3d[1, 1: ,1:]
"""
array([[4, 5],
       [7, 8]])
"""

# 4. boolean indexing
dataset = np.random.randint(1, 10, size=100)
len(dataset)  # 100

dataset

# 5 이상
dataset2 = dataset[dataset >= 5]
len(dataset2)  # 60
dataset2

# 5~8 자료 선택
#dataset3 = dataset[dataset >= 5 and dataset <= 8]
# ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()
# indexing시 관계식과 논리식을 한꺼번에 쓸 수 없다. >= / and
# np에서는 논리식을 사용할 수 있는 함수를 제공한다.
np.logical_and()
np.logical_or()
np.logical_not()

dataset3 = dataset[np.logical_and(dataset >=5, dataset <= 8)]
dataset3
len(dataset3)  # 52



































