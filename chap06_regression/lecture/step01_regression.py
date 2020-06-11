# -*- coding: utf-8 -*"-
"""
회귀방정식에서 기울기(slope)와 절편(intercept) 구하기(식)
    기울기(slope) = Cov(x, y) / Sxx(x의 편차의 제곱의 평균)
    절편(intercept) = y_mu - (slope * x_mu)
"""
from scipy import stats  # 회귀모델
import pandas as pd  # csv file read
import numpy as np

galton = pd.read_csv('C:\\ITWILL\\Work\\4_Python-II\\data\\galton.csv')
galton.info()
"""
 #   Column  Non-Null Count  Dtype  
---  ------  --------------  -----  
 0   child   928 non-null    float64
 1   parent  928 non-null    float64
"""

# x, y 변수 선택
x = galton.parent
y = galton.child


# model 생성
model = stats.linregress(x, y)
model
"""LinregressResult(slope=0.6462905819936423, 
intercept=23.941530180412748, 
rvalue=0.4587623682928238,     : 부모의 키가 자식의 키에 영향을 미치는 정도가 약 40% 밖에 되지 않는다는 뜻. 상관관계가 아주 높지는 않다.
pvalue=1.7325092920142867e-49, 
stderr=0.04113588223793335)
"""

y_pred = x*model.slope + model.intercept
y_pred

y_true = y


# 예측치 vs 관측치(정답)
y_pred.mean()  #  68.08846982758534
y_true.mean()  # 68.08846982758512


# 기울기 계산식 -> 동일하게 나오나?
#     기울기(slope) = Cov(x, y) / Sxx(x의 편차의 제곱의 평균)
xu = x.mean(); yu = y.mean(); n=len(x)  # or len(y)
Cov_xy = sum((x-xu)*(y-yu)) / n 
Cov_xy  # 2.062389686756837

Sxx = np.mean((x-xu)**2)
Sxx

slope_cal = Cov_xy / Sxx
slope_cal  # 0.6462905819936413


# 2. 절편 계산식
# 절편(intercept) = y_mu - (slope * x_mu)

intercept = yu - (slope_cal * xu)
intercept  # 23.94153018041171



# 3. 설명력(rvalue)
galton.corr()
"""
           child    parent
child   1.000000  0.458762
parent  0.458762  1.000000
"""

y_pred = x * slope_cal + intercept

y_pred.mean()  # 68.08846982758423  모델에서 생성한 예측치와 같다.!!!!















