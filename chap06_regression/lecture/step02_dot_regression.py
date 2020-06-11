# -*- coding: utf-8 -*-
"""
행렬곱 함수(np.dot)  : 4장 step05 참조
   y_pred = np.dot(X,a)  + b
"""

from scipy import stats  # 단순회귀모델(기울기, 절편)
from statsmodels.formula.api import ols  # 다중회귀모델
import pandas as pd
import numpy as np

# 1. data load
score = pd.read_csv('C:\\ITWILL\\Work\\4_Python-II\\data\\score_iq.csv')
score.info()
"""
 0   sid      150 non-null    int64
 1   score    150 non-null    int64   >> y
 2   iq       150 non-null    int64   >> x1
 3   academy  150 non-null    int64   >> x2
 4   game     150 non-null    int64
 5   tv       150 non-null    int64
 """
 
formula = "score ~ iq + academy"
model = ols(formula, data=score).fit() 
model.params
"""
Intercept    25.229141
iq            0.376966
academy       2.992800
"""


# model 결과 확인
model.summary() 
"""
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                  score   R-squared:                       0.946
Model:                            OLS   Adj. R-squared:                  0.946   설명력 good 꽤 영향을 미친다.
Method:                 Least Squares   F-statistic:                     1295.
Date:                Tue, 12 May 2020   Prob (F-statistic):           4.50e-94   귀무가설 기각역. 관련성 있다. 
Time:                        11:43:16   Log-Likelihood:                -275.05
No. Observations:                 150   AIC:                             556.1
Df Residuals:                     147   BIC:                             565.1
Df Model:                           2                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
Intercept     25.2291      2.187     11.537      0.000      20.907      29.551
iq             0.3770      0.019     19.786      0.000       0.339       0.415
academy        2.9928      0.140     21.444      0.000       2.717       3.269  영향을 미치는 강도는 t검정 통계량이 높은 것이 높다.
==============================================================================
Omnibus:                       36.342   Durbin-Watson:                   1.913
Prob(Omnibus):                  0.000   Jarque-Bera (JB):               54.697
Skew:                           1.286   Prob(JB):                     1.33e-12
Kurtosis:                       4.461   Cond. No.                     2.18e+03
==============================================================================

Warnings:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 2.18e+03. This might indicate that there are
strong multicollinearity or other numerical problems.
"""
 
 
# model 예측치
y_pred = model.fittedvalues
y_true = score.score 
print(len(y_pred), len(y_true)) 


#   y_pred = np.dot(X,a)  + b
X = score[['iq', 'academy']]
X.shape  # (150, 2)  # x1, x2

'''
np.dot(X,a) 전제조건
1. X,a : 행렬구조
2. 수일치 : X열차수 = a행차수
a는 (2,1)
'''

a = [[model.params.iq],[model.params.academy]]  # (2,1)
b = model.params.Intercept 

matmul = np.dot(X,a)
matmul.shape  # (150,1)
X.shape  # (150, 2)
y_pred_matmul = matmul + b  # broadcast(2차원 + 0차원)
y_pred_matmul.mean()


y_pred_dot = np.dot(X, a) + b
y_pred_dot 
y_pred_dot.shape  # (150, 1)
len(y_pred_dot)  # 150
y_pred_dot.mean()  # 77.77333333333335
y_pred.mean()  # 77.77333333333341
y_true.mean()  # 77.77333333333333

 
 # 2차원 -> 1차원
y_pred1d = y_pred_dot.reshape(150)
y_pred1d 
y_pred1d.shape  # (150,)

y_true.shape  # (150,)
# 예측치와 관측치 쉐잎 같다. df 만들자

df = pd.DataFrame({'y_true' : y_true, 'y_pred' : y_pred1d})
df.head()
"""
   y_true     y_pred
0      90  83.989997
1      75  75.342705
2      77  73.457874
3      83  82.105166
4      65  64.810583
"""
df.tail()
"""
     y_true     y_pred
145      83  82.105166
146      65  64.810583
147      80  80.574373
148      65  64.810583
149      83  82.105166
"""

cor = df['y_true'].corr(df.y_pred)
cor   # 0.9727792069594764  : 97퍼센트 정도 예측치와 관측치가 비슷하다
 
 
 
 
 
 
 
 