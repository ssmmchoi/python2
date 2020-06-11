# -*- coding: utf-8 -*-
"""
1. image shape : 3차원(세로 픽셀, 가로 픽셀, 컬러)
2. reshape : size는 변경하면 안됨
    ex) [2, 5] -> [5, 2] ok.
        [3, 4] -> [4, 2] X
"""
import numpy as np
from matplotlib.image import imread  # image 읽어오는 함수
import matplotlib.pylab as plt


# 1. image shape
file_path = 'C:\\ITWILL\\Work\\4_Python-II\\workspace\\chap04_NumPy\\images\\test1.jpg'
image = imread(file_path)
"""
array([[[ 93,  93,  85],
        [ 93,  93,  85],
        [ 94,  94,  86],
        ...,
        [112, 114, 101],
        [112, 114, 101],
        [112, 114, 101]],

       [[ 91,  91,  83],
        [ 92,  92,  84],
        [ 93,  93,  85],
        ...,
        [112, 114, 101],
        [112, 114, 101],
        [112, 114, 101]],

       [[ 90,  90,  82],
        [ 90,  90,  82],
        [ 91,  91,  83],
        ...,
        [112, 114, 101],
        [112, 114, 101],
        [112, 114, 101]],

       ...,

       [[ 30,  28,  33],
        [ 30,  28,  33],
        [ 30,  28,  33],
        ...,
        [137, 126, 106],
        [136, 125, 105],
        [135, 124, 104]],

       [[ 32,  30,  35],
        [ 32,  30,  35],
        [ 32,  30,  35],
        ...,
        [131, 118,  99],
        [130, 117,  98],
        [129, 116,  97]],

       [[ 34,  32,  37],
        [ 34,  32,  37],
        [ 34,  32,  37],
        ...,
        [128, 113,  94],
        [127, 112,  93],
        [126, 111,  92]]], dtype=uint8)
"""
type(image)  # numpy.ndarray
image.shape  # (360, 540, 3)  : (세로, 가로, 컬러)
print(image)  # 0~ 255의 농도(컬러)

plt.imshow(image)

# RGB 색상 분류
r = image[:, :, 0]
g = image[:, :, 1]
b = image[:, :, 2]
r.shape  # (360, 540)
g.shape  # (360, 540)
b.shape  # (360, 540)


# 2. image data reshape
from sklearn.datasets import load_digits  # 아나콘다에서 데이터셋을 제공하는 모듈 : numpy

digit = load_digits()  # dataset loading
digit.DESCR  # 디스크라이브 멤버 : 해당 데이터에 대한 정보를 설명문으로.

X = digit.data  # x 변수(입력변수)  : image
Y = digit.target  # y 변수(정답=정수)  : 

X.shape  # (1797, 64)  64 = 8X8로 reshape할 수 있음.
Y.shape  # (1797,)

X[0]  # 행 index
img0 = X[0].reshape(8,8)
img0
"""
array([[ 0.,  0.,  5., 13.,  9.,  1.,  0.,  0.],
       [ 0.,  0., 13., 15., 10., 15.,  5.,  0.],
       [ 0.,  3., 15.,  2.,  0., 11.,  8.,  0.],
       [ 0.,  4., 12.,  0.,  0.,  8.,  8.,  0.],
       [ 0.,  5.,  8.,  0.,  0.,  9.,  8.,  0.],
       [ 0.,  4., 11.,  0.,  1., 12.,  7.,  0.],
       [ 0.,  2., 14.,  5., 10., 12.,  0.,  0.],    0 흰색 <- -> 숫자 커질수록 검정색에 가까워짐
       [ 0.,  0.,  6., 13., 10.,  0.,  0.,  0.]])
"""
plt.imshow(img0)
Y[0]  # 0


X3d = img0 = X.reshape(-1, 8,8)  # -1 : 1797 전체
X3d.shape  # (1797, 8, 8) 흑백. >> 만약 컬러 이미지라면 (1797, 8, 8, 3)
           # (전체이미지수, 세로, 가로, (컬러))

# (1797, 8, 8, 1)
X4d = X3d[:, :, :, np.newaxis]  # 4번축 추가
X4d.shape  # (1797, 8, 8, 1)


# 3. reshape
"""
전치행렬 : T
swapaxis = 전치행렬과 비슷
transpose() : 3차원 이상 모양 변경
"""

# 1) 전치행렬
data = np.arange(10).reshape(2,5)
data
"""
array([[0, 1, 2, 3, 4],
       [5, 6, 7, 8, 9]])
"""

print(data.T)
"""
[[0 5]
 [1 6]
 [2 7]
 [3 8]
 [4 9]]
"""

# 3) transpose()
'''
1차원 : 효과 없음
2차원 : 전치행렬 동일함
3차원 : (0,1,2) -> (2,1,0) 지정하여 축이 바뀜
'''

arr3d = np.arange(1, 25).reshape(4,2,3)
arr3d
"""
array([[[ 1,  2,  3],
        [ 4,  5,  6]],

       [[ 7,  8,  9],
        [10, 11, 12]],

       [[13, 14, 15],
        [16, 17, 18]],

       [[19, 20, 21],
        [22, 23, 24]]])
"""
arr3d.shape  # (4, 2, 3)

#  (0,1,2) -> (2,1,0)  : 축의 넘버를 가지고 위치를 변경할 때
arr3d_tran = arr3d.transpose(2,1,0)
arr3d_tran.shape  # (3,2,4)
arr3d_tran

#  (0,1,2) -> (1,2,0)
arr3d_tran = arr3d.transpose(1,2,0)
arr3d_tran.shape  # (2, 3, 4)
arr3d_tran






























