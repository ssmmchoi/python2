# -*- coding: utf-8 -*-
"""
scipy 패키지의 stats 모듈의 함수
 - 통계적인 방식의 회귀분석
 1. 단순선형회귀모델
 2.다중선형회귀모델
"""

from scipy import stats  # 회귀모델 생성
import pandas as pd  # csv file read

# 1. 단순선형회귀모델
'''
x -> y
'''

score_iq = pd.read_csv("C:/ITWILL/Work/4_Python-II/data/score_iq.csv")
score_iq.info()

# 변수 선택
x = score_iq.iq
y = score_iq['score']

# 회귀모델 생성
model = stats.linregress(x, y)
model
'''
LinregressResult(slope=0.6514309527270075,   : 기울기
intercept=-2.8564471221974657,               : 절편
rvalue=0.8822203446134699,                   : r-squared : 설명력(상당히 높은 편)
pvalue=2.8476895206683644e-50,               : p-value : x의 유의성 검정을 할 수 있는 데이터
stderr=0.028577934409305443)                 : 표본에 대한 오차

: 5개의 값이 튜플 형태로 묶여서 나옴.
'''
# 따로 꺼낼 수도 있음.
print('x변수의 기울기 =', model.slope)  # x변수의 기울기 = 0.6514309527270075
print('y절편 =', model.intercept)  # y절편 = -2.8564471221974657


score_iq.head(1)  
'''
     sid  score   iq  academy  game  tv
0  10001     90  140        2     1   0   >> 해당 iq를 넣고 score를 예측해보자.
'''
# y = X*a + b
X = 140
y_pred = X*model.slope + model.intercept
print('iq=140일 때의 score 예측치 :', y_pred)  # iq=140일 때의 score 예측치 : 88.34388625958358

Y = 90
err = Y-y_pred
print('err of this model for iq=140 :', err)  # err of this model for iq=140 : 1.6561137404164157



########################
###product.csv
########################

product = pd.read_csv("C:/ITWILL/Work/4_Python-II/data/product.csv")
product.info()
product.head()

product.corr()
"""
          a         b         c
a  1.000000  0.499209  0.467145
b  0.499209  1.000000  0.766853  >> b vs c correlation이 가장 높다.
c  0.467145  0.766853  1.000000
b = 제품적절성, c = 제품만족도
"""

# x : 제품적절성(b) vs y : 제품만족도(c)
model2 = stats.linregress(product.b, product.c)
model2
'''
LinregressResult(slope=0.7392761785971821, 
intercept=0.7788583344701907,
 rvalue=0.766852699640837,
 pvalue=2.235344857549548e-52, 
 stderr=0.03822605528717565)
'''

product.head(1)
"""
   a  b(x)  c(y)
0  3  4     3
"""
X = 4
y_pred = X*model2.slope + model2.intercept
y_pred  # 3.735963048858919

Y = 3  # 이므로
err = Y - y_pred
print('error of this model(model2) for x=4 is :', err)  # error of this model(model2) for x=4 is : -0.7359630488589191

err2 = (Y-y_pred)**2
err2  #  평균제곱오차 : 0.5416416092857157


X = product.b  # x 변수
y_pred = X*model2.slope + model2.intercept  # 예측치
Y = product.c  # 관측치(실제값)

len(y_pred)  # 264
y_pred[1:10]
Y[1:10]

tab = pd.crosstab(y_pred, Y)
tab
"""c         1   2   3   4  5
b                         
1.518135  7   1   0   0  0
2.257411  1  30  17   0  0
2.996687  1  12  91  15  0
3.735963  0   2  21  53  3
4.475239  0   0   0   6  4
"""



# 2. 회귀모델 시각화
from pylab import plot, legend, show

plot(product.b, product['c'], 'b.')  # (x,y)-산점도
plot(product.b, y_pred, 'r.-')  # 회귀선
legend(['x,y scatter', 'regress model line'])
show()



# 3. 다중선형회귀모델 : y ~ x1 + x2, ...
from statsmodels.formula.api import ols  # function

wine = pd.read_csv('C:\\ITWILL\\Work\\4_Python-II\\data\\winequality-both.csv')
wine.info()

wine.columns = wine.columns.str.replace(' ', '_')
wine.info()

# quality vs others

cor = wine.corr()
cor.quality
"""
fixed_acidity          -0.076743
volatile_acidity       -0.265699   >> x3
citric_acid             0.085532
residual_sugar         -0.036980
chlorides              -0.200666   >> x2
free_sulfur_dioxide     0.055463
total_sulfur_dioxide   -0.041385
density                -0.305858   >> x4
pH                      0.019506
sulphates               0.038485
alcohol                 0.444319   >> x1
quality                 1.000000
"""

formula = "quality ~ alcohol + chlorides + volatile_acidity"
formula_sm = "quality ~ alcohol + chlorides + volatile_acidity + density"

model = ols(formula, data=wine).fit()  # 모델의 모형부분.모델생성부분
model_sm = ols(formula_sm, data=wine).fit()

model  # obj info  : <statsmodels.regression.linear_model.RegressionResultsWrapper at 0x1cb92101dc8>
model_sm   # <statsmodels.regression.linear_model.RegressionResultsWrapper at 0x1cb91af8f48>

model.summary()  # R에서 summary(model)
# <class 'statsmodels.iolib.summary.Summary'>
"""
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                quality   R-squared:                       0.260   >> 설명력!
Model:                            OLS   Adj. R-squared:                  0.259   >> 조정된 설명력! 이걸 채택(낮은편)
Method:                 Least Squares   F-statistic:                     758.6   >> F 검정 통계량!
Date:                Mon, 11 May 2020   Prob (F-statistic):               0.00   >> 모델 유의성 검정 : F 검정 통계량으로 만들어진 확률값! 0.05와 비교하여 0.05보다 작은 값이면 이 모델은 유의하다고 할 수 있음
Time:                        14:57:12   Log-Likelihood:                -7361.8
No. Observations:                6497   AIC:                         1.473e+04
Df Residuals:                    6493   BIC:                         1.476e+04
Df Model:                           3                                         
Covariance Type:            nonrobust                                         
====================================================================================
                       coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------------
Intercept            2.9099      0.091     31.977      0.000       2.732       3.088  >> y절편
alcohol              0.3196      0.008     39.415      0.000       0.304       0.335  >> x1  P>|t|를 보면 0.05보다 작으므로 영향을 미친다.(양의 상관성)
chlorides            0.1593      0.298      0.535      0.593      -0.425       0.743  >> x2  
volatile_acidity    -1.3349      0.061    -21.780      0.000      -1.455      -1.215  >> x3  P>|t|를 보면 0.05보다 작으므로 영향을 미친다.(음의 상관성)
==============================================================================
Omnibus:                      113.350   Durbin-Watson:                   1.645   >> 잔차에 대한 통계값
Prob(Omnibus):                  0.000   Jarque-Bera (JB):              229.732
Skew:                           0.007   Prob(JB):                     1.30e-50
Kurtosis:                       3.921   Cond. No.                         342.
==============================================================================

Warnings:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
"""

"""
Adf. R-squared : 유의성검정
F-statistic : 
Prob(F-statistic) : 
x의 유의성 검정
"""


model_sm.summary()
# <class 'statsmodels.iolib.summary.Summary'>
"""
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                quality   R-squared:                       0.267
Model:                            OLS   Adj. R-squared:                  0.267
Method:                 Least Squares   F-statistic:                     592.3
Date:                Mon, 11 May 2020   Prob (F-statistic):               0.00
Time:                        14:57:46   Log-Likelihood:                -7327.1
No. Observations:                6497   AIC:                         1.466e+04
Df Residuals:                    6492   BIC:                         1.470e+04
Df Model:                           4                                         
Covariance Type:            nonrobust                                         
====================================================================================
                       coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------------
Intercept          -35.6534      4.625     -7.709      0.000     -44.720     -26.587
alcohol              0.3818      0.011     34.747      0.000       0.360       0.403
chlorides           -0.2330      0.300     -0.777      0.437      -0.821       0.355
volatile_acidity    -1.4752      0.063    -23.323      0.000      -1.599      -1.351
density             38.1824      4.578      8.340      0.000      29.207      47.158
==============================================================================
Omnibus:                      115.280   Durbin-Watson:                   1.653  
Prob(Omnibus):                  0.000   Jarque-Bera (JB):              235.361
Skew:                          -0.003   Prob(JB):                     7.80e-52
Kurtosis:                       3.932   Cond. No.                     7.48e+03
==============================================================================

Warnings:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 7.48e+03. This might indicate that there are
strong multicollinearity or other numerical problems.
"""

# 기울기, 절편
model.params
"""
Intercept           2.909941  절편
alcohol             0.319578  여기서부터는 x변수에 대한 각각의 기울기
chlorides           0.159258
volatile_acidity   -1.334944
dtype: float64
"""
model_sm.params
"""
Intercept          -35.653368
alcohol              0.381815
chlorides           -0.232955
volatile_acidity    -1.475170
density             38.182433
"""

model.fittedvalues
"""
0       4.991616
1       4.882661
2       5.041899
3       5.679965
4       4.991616
  
6492    6.215087
6493    5.558192
6494    5.600117
6495    6.616908
6496    6.403807
Length: 6497, dtype: float64   >> 모델에 대한 y 변수의 예측치
"""  
y_pred = model.fittedvalues
y_true = wine.quality

err = (y_true - y_pred)**2
err.mean()  # 0.5645782511233358

y_true.mean()  # 5.818377712790519
y_pred.mean()  # 5.81837771279059

# 차트
import matplotlib.pyplot as plt

plt.plot(y_true[:50], 'b', label='real values')
plt.plot(y_pred[:50], 'r', label='y prediction')
plt.yticks(range(0,10))  # y축눈금
plt.legend(loc = 'best')
plt.show()









