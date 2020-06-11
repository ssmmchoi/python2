# -*- coding: utf-8 -*-
"""
sklearn 로지스틱 회귀모델
 - y 변수가 범주형인경우.
 
"""

from sklearn.datasets import load_breast_cancer, load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix  # model 평가 도구, 교차분할표 생성도구

#########################################
####### 1. 이항분류부터.
#########################################

# 1. dataset load & 변수 선택
breast = load_breast_cancer()

X = breast.data  # x변수
y = breast.target

X.shape  # (569, 30)
y.shape  # (569,)


# 2. model 
help(LogisticRegression)  # 이항&다항 변수에 차이가 있다.
"""
random_state=None, solver='lbfgs', max_iter=100, multi_class='auto'

random_state=None  : 난수 seed 값 지정
solver='lbfgs'  : 알고리즘
max_iter=100  : 반복학습 횟구
multi_class='auto'  : 다항분류

적용 예)
일반 데이터, 이항분류:default
일반데이터, 다항분류 : solver='lbfgs'(default), multi_class='multinomial'
빅 데이터, 이항분류 : solver='sag'or'saga'
빅 데이터, 다항분류 : solver='sag'or'saga', multi_class='multinomial'
"""

lr = LogisticRegression(random_state=123)
# multi_class='auto' --> sigmoid 활용함수 이용 -> 다항분류
model = lr.fit(X=X, y=y)
model


# 3. model 평가
acc = model.score(X, y)
acc  
# 0.9472759226713533

# or
y_pred = model.predict(X)
acc2 = accuracy_score(y, y_pred)
acc2  # 0.9472759226713533

# or  교차분할표
con_max = confusion_matrix(y, y_pred)
con_max
"""
array([[193,  19],
       [ 11, 346]], dtype=int64)
"""

acc3 = (con_max[0,0] + con_max[1,1]) / con_max.sum()
acc3  # 0.9472759226713533



import pandas as pd

tab = pd.crosstab(y, y_pred, rownames=['관측치'], colnames=['예측치'])
tab
"""
예측치    0    1
관측치          
0       193   19
1       11  346
"""

#acc4 = (tab.loc[0,0] + tab.loc[1,1]) / sum(tab)  -> sum(tab=1)
acc4 = (tab.loc[0,0] + tab.loc[1,1]) / len(y)
acc4  # 0.9472759226713533




#########################################
####### 2. 다항분류 모델
#########################################

iris = load_iris()
iris.target_names  # array(['setosa', 'versicolor', 'virginica'], dtype='<U10')

X, y = load_iris(return_X_y=True)

X.shape  # (150, 4)
y.shape  # (150,)
y  # target name을 0,1,2 로 범주화하여 나타내줌
'''
array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
       2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
       2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2])
'''


# model 생성
lr2  = LogisticRegression(random_state=123, multi_class='multinomial', solver='lbfgs')
# multi_class='multinomial' --> softmax 활용함수 이용 -> 다항분류
'''
sigmoid function : 0~1 확률값 -> cutoff=0.5 -> 이항분류
softmax function : 0~1 확률값 -> 전체합 = 1 -> 다항분류
'''
model = lr2.fit(X, y)
model


y_pred = model.predict(X)  # class
y_pred2 = model.predict_proba(X)  # 확률값

y_pred  # 0 ~ 2
"""
array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1,
       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2,
       2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
       2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2])
"""
y_pred2.shape  #  (150, 3)
y_pred2
#  array(['setosa', 'versicolor', 'virginica']  -> 합1
# array([[9.81797141e-01, 1.82028445e-02, 1.44269293e-08],

import numpy as np
arr = np.array([9.81797141e-01, 1.82028445e-02, 1.44269293e-08])
arr.max()  # 0.981797141   >> setosa라고 98%로 예측함
arr.min()  # 1.44269293e-08
arr.sum()  # 0.9999999999269293 거의 1


# model 평가
acc = accuracy_score(y, y_pred)  # 얘는 y_pred로 예측함. 비교한느 관측치와 예측치의 형식이 같아야 하므로.
acc  # 0.9733333333333334

con_max = confusion_matrix(y, y_pred)
con_max
"""
array([[50,  0,  0],
       [ 0, 47,  3],
       [ 0,  1, 49]], dtype=int64)
"""

#acc2 = (con_max[0,0] + con_max[1,1] + con_max[2,2] ) / sum(con_max)  # array([2.92      , 3.04166667, 2.80769231])
acc2 = (con_max[0,0] + con_max[1,1] + con_max[2,2] ) / con_max.sum()
acc2  # 0.9733333333333334


# 히트맵 : 시각화
import seaborn as sn
import matplotlib.pyplot as plt

# confusion matrix heatmap
plt.figure(figsize=(6,6))  # chart size
sn.heatmap(con_max, annot=True, fmt='.3f', linewidths=.5, square=True)
plt.ylabel('Actual label')
plt.xlabel('Predicted label')
all_sample_title = 'Accuracy Score : {0}'.fromat(acc)
plt.title(all_sample_title, size=18)
plt.show()




#########################################
####### 3. 다항분류 : digits : multiclass
####### y변수의 범주가 매우 많은 것(0~9)
#########################################

from sklearn.datasets import load_digits

# 1. dataset load
digits = load_digits()
digits.target_names  # array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) 10개의 범주 : 정답

X = digits.data  # 이미지 픽셀 정보
y = digits.target
X.shape  #  (1797, 64)  : 1797장의 이미지 데이터가 각각 64(8x8)픽셀
y.shape  # (1797,) 이미지의 10진수 정답


# 2. datasplit
img_train, img_test, label_train, label_test = train_test_split(X, y, random_state=123)

import matplotlib.pyplot as plt
img2d = img_train.reshape(-1,8,8)  # -1 : 전체 이미지 대상
img2d.shape # (1347, 8, 8)

plt.imshow(img2d[0])
label_train[0]  # 7 : 정답
img2d[0]
"""array([[ 0.,  0., 10., 16.,  5.,  0.,  0.,  0.],
       [ 0.,  1., 10., 14., 12.,  0.,  0.,  0.],
       [ 0.,  0.,  0.,  9., 11.,  0.,  0.,  0.],
       [ 0.,  0.,  2., 11., 13.,  3.,  0.,  0.],
       [ 0.,  0., 11., 16., 16., 16.,  7.,  0.],
       [ 0.,  0.,  3., 16.,  4.,  5.,  1.,  0.],
       [ 0.,  0.,  7., 13.,  0.,  0.,  0.,  0.],
       [ 0.,  0., 13.,  6.,  0.,  0.,  0.,  0.]])
"""  ## 0~16에서 16으로 갈수록 선명한?진한?색



# 2. model 생성
lr  = LogisticRegression(random_state=123, multi_class='multinomial', solver='lbfgs')
model = lr2.fit(img_train, label_train)
model

y_pred = model.predict(img_test)
len(y_pred)


# 4. evaluating model
acc = accuracy_score(label_test, y_pred)
acc  # 0.9644444444444444

conmat = confusion_matrix(label_test, y_pred)
conmat
"""
array([[51,  0,  0,  0,  0,  0,  0,  0,  0,  0],
       [ 0, 42,  0,  0,  0,  0,  0,  0,  0,  0],
       [ 0,  0, 41,  0,  0,  0,  0,  0,  0,  0],
       [ 0,  0,  0, 39,  0,  0,  0,  0,  0,  1],
       [ 0,  0,  0,  0, 51,  0,  0,  1,  0,  0],
       [ 0,  1,  0,  0,  0, 42,  0,  2,  0,  3],
       [ 0,  1,  0,  0,  0,  1, 46,  0,  0,  0],
       [ 0,  0,  0,  0,  0,  0,  0, 41,  0,  0],
       [ 0,  4,  0,  0,  0,  0,  0,  0, 41,  0],
       [ 0,  1,  0,  0,  0,  0,  0,  0,  1, 40]], dtype=int64)
"""

def accuracy() :
    temp=0
    for i in range(10) :
        temp += np.sum(conmat[i,i])
    acc = temp / len(y_pred)
    
    return acc

acc = accuracy()
acc  # 0.9644444444444444

result = label_test == y_pred
result  # True or False로 나타나므로 
result.mean()  # 0.9644444444444444 -> result에서 나타난 True(1)와 False(0) 의 평균 : accuracy


# 틀린 image
false_img = img_test[result==False]
false_img.shape  #  (16, 64)
y_pred[result==False]  #  array([7, 7, 1, 1, 1, 1, 1, 9, 1, 7, 9, 5, 1, 8, 9, 9])
#plt.imshow(false_img)
label_test[result==False]  #  array([5, 5, 8, 8, 8, 6, 5, 5, 8, 4, 5, 6, 9, 9, 5, 3]) 원래 답




# for img in range(false_img.shape[0]) :  # row
#     print(idx)
#     plt.imshow(false_img3d[idx])