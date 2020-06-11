# -*- coding: utf-8 -*-
"""
공분산 vs 상관계수(correlation)  : 나중에 회귀모형에서 자주 볼 수 있는 용어
 - 공통점 :변수 간의 상관성 분석, 부호가 같다.

1. 공분산 : 두 확률변수 간의 분산(평균에서 퍼짐 정도)을 나타내는 통계
  - 두 확률변수 : x, y -> x 표본평균(ux), y 표본평균(uy)
    공분산 Cov(x, y) = sum((x-ux)*(y-uy)) / n
    
    Cov(x, y) > 0 : x 증가 -> y 증가(비례 관계)
    Cov(x, y) < 0 : x 증가 -> y 감소(반비례 관계)
    Cov(x, y) = 0 : 두 변수는 선형관계가 아님
    문제점 : 값 자체가 큰 변수의 영향을 받게 됨.

2. 상관계수 : 공분산을 각각의 표준편차로 나누어서 정규화한 통계
  - 부호는 공분산과 동일, -1 ~ +1(절댓값 1을 넘지 않음)
  - Cor(x, y) = Cov(x, y) / std(x)*std(y)
"""

import numpy as np
import pandas as pd


score_iq = pd.read_csv('C:\\ITWILL\\Work\\4_Python-II\\data\\score_iq.csv')
score_iq.info()
"""
 #   Column   Non-Null Count  Dtype
---  ------   --------------  -----
 0   sid      150 non-null    int64
 1   score    150 non-null    int64
 2   iq       150 non-null    int64
 3   academy  150 non-null    int64
 4   game     150 non-null    int64
 5   tv       150 non-null    int64
"""

cor = score_iq.corr()
cor
"""
              sid     score        iq   academy      game        tv
sid      1.000000 -0.014399 -0.007048 -0.004398  0.018806  0.024565
score   -0.014399  1.000000  0.882220  0.896265 -0.298193 -0.819752  > 실제 score와 iq, academy와의 상관성은 비슷함.
iq      -0.007048  0.882220  1.000000  0.671783 -0.031516 -0.585033
academy -0.004398  0.896265  0.671783  1.000000 -0.351315 -0.948551
game     0.018806 -0.298193 -0.031516 -0.351315  1.000000  0.239217
tv       0.024565 -0.819752 -0.585033 -0.948551  0.239217  1.000000
"""

score_iq['score'].corr(score_iq['iq'])  #  0.88222034461347
score_iq['score'].corr(score_iq['academy'])  # 0.8962646792534938





# 1. 공분산
#  - score vs iq
#  - score vs academy

# 공분산 Cov(x, y) = sum((x-ux)*(y-uy)) / n

X = score_iq['score']
Y1 = score_iq['iq']
Y2 = score_iq['academy']

def Cov(X, Y) :
    ux = X.mean()
    uy = Y.mean()
    n = len(X)
    
    covxy = sum((X-ux)*(Y-uy)) / n
    
    return covxy

cov_x_y1 = Cov(X, Y1)  # score vs iq
cov_x_y1  # 50.99528888888886

cov_x_y2 = Cov(X, Y2)  # score vs academy
cov_x_y2  # 7.072444444444438

print('score vs iq cov : %.3f \nscore vs academy : %.3f' %(cov_x_y1, cov_x_y2))
# score vs iq cov : 50.995 
# score vs academy : 7.072

# 하지만!
# score_iq.csv 파일을 보면 iq는 비교적 높은 값(약 100), academy는 비교적 낮은 값(0,1,2)을 가지므로 iq와의 공분산이 더 크게 나타남.

score_iq.cov()
'''
                 sid      score         iq   academy      game        tv
sid      1887.500000  -4.100671  -2.718121 -0.231544  1.208054  1.432886
score      -4.100671  42.968412  51.337539  7.119911 -2.890201 -7.214586
iq         -2.718121  51.337539  78.807338  7.227293 -0.413691 -6.972975
academy    -0.231544   7.119911   7.227293  1.468680 -0.629530 -1.543400
game        1.208054  -2.890201  -0.413691 -0.629530  2.186309  0.474899
tv          1.432886  -7.214586  -6.972975 -1.543400  0.474899  1.802640
'''

# 따로 확인 가능.
score_iq['score'].cov(score_iq['iq'])  # 51.33753914988811
score_iq['score'].cov(score_iq['academy'])  # 7.11991051454138


'''
2. 상관계수

Cor(x, y) = Cov(x, y) / std(x)*std(y)
'''

def Cor(X, Y) :
    cov = Cov(X, Y)
    std_x = X.std()
    std_y = Y.std()
    
    corxy = cov / (std_x * std_y)
    
    return corxy

cor_x_y1 = Cor(X, Y1)
cor_x_y1  # 0.8763388756493802

cor_x_y2 = Cor(X, Y2)
cor_x_y2  # 0.8902895813918037

print('score vs iq cor : %.3f \nscore vs academy cor : %.3f' %(cor_x_y1, cor_x_y2))
'''
score vs iq cor : 0.876 
score vs academy cor : 0.890    값에 대한 크게에 상관없이 변수간의 어떤 영향을 받는지 보여줌.
'''














