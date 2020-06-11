'''
문1) score_iq.csv 데이터셋을 이용하여 단순선형회귀모델을 생성하시오.
   <조건1> y변수 : score, x변수 : academy      
   <조건2> 회귀모델 생성과 결과확인(회귀계수, 설명력, pvalue, 표준오차) 
   <조건3> 회귀선 적용 시각화 
   
문2) irsi.csv 데이터셋을 이용하여 다중선형회귀모델을 생성하시오.
   <조건1> 칼럼명에 포함된 '.' 을 '_'로 수정
   iris = pd.read_csv('../data/iris.csv')
   iris.columns = iris.columns.str.replace('.', '_')
   <조건2> y변수 : 1번째 칼럼, x변수 : 2~4번째 칼럼    
   <조건3> 회귀계수 확인 
   <조건4> 회귀모델 세부 결과 확인  : summary()함수 이용 
'''

from scipy import stats
import pandas as pd
import statsmodels.formula.api as sm
import matplotlib.pyplot as plt

# 문1) score_iq.csv 데이터셋을 이용하여 단순선형회귀모델을 생성하시오.

# <조건1> y변수 : score, x변수 : academy
score_iq = pd.read_csv('C:\\ITWILL\\Work\\4_Python-II\\data\\score_iq.csv')

y=score_iq.score
x=score_iq.academy


# <조건2> 회귀모델 생성과 결과확인(회귀계수, 설명력, pvalue, 표준오차) 
model_lin = stats.linregress(x, y)
model_lin

print('회귀계수 : 기울기 = %.3f, 절편 = %.3f \n설명력 =%.3f \npvalue = %.3f \n표준오차 = %.3f' %(model_lin))
"""
회귀계수 : 기울기 = 4.848, 절편 = 68.239 
설명력 =0.896   : 설명력 good
pvalue = 0.000   : 통계적으로 유의함
표준오차 = 0.197  : 오차 비교적 낮은 편
"""


# <조건3> 회귀선 적용 시각화 
y_pred = x*model_lin.slope + model_lin.intercept
y_pred

from pylab import plot, legend, show
plot(x, y, 'b.')
plot(x, y_pred, 'r.-')
legend(['x, y scatter', 'linear y predictions'])
show()

"""
plot(x, y, 'b.', label = 'x, y scatter')
plot(x, y_pred, 'r.-', label = 'linear y predictions')
legend(loc = 'best')   ## >> 이렇게 하면 최적의 위치에 범례 추가
show()
"""













# 문2) irsi.csv 데이터셋을 이용하여 다중선형회귀모델을 생성하시오.
iris = pd.read_csv('C:\\ITWILL\\Work\\4_Python-II\\data\\iris.csv')
iris.info()

# <조건1> 칼럼명에 포함된 '.' 을 '_'로 수정  >> 그래야 formula 만들 수 있음
iris.columns = iris.columns.str.replace('.', '_')
iris.info()


# <조건2> y변수 : 1번째 칼럼, x변수 : 2~4번째 칼럼    
y = iris['Sepal_Length']
y
x = iris[['Sepal_Width', 'Petal_Length', 'Petal_Width']]
x



# <조건3> 회귀계수 확인 
formula = 'Sepal_Length ~ Sepal_Width + Petal_Length + Petal_Width'
model_reg = sm.ols(formula, data=iris).fit()

model_reg.params
"""
Intercept       1.855997  : 절편
Sepal_Width     0.650837  : ㄱ 세 x 변수의 기울기
Petal_Length    0.709132
Petal_Width    -0.556483
dtype: float64
"""





# <조건4> 회귀모델 세부 결과 확인  : summary()함수 이용 
model_reg.summary()
"""
                            OLS Regression Results                            
==============================================================================
Dep. Variable:           Sepal_Length   R-squared:                       0.859
Model:                            OLS   Adj. R-squared:                  0.856
Method:                 Least Squares   F-statistic:                     295.5
Date:                Mon, 11 May 2020   Prob (F-statistic):           8.59e-62
Time:                        16:23:04   Log-Likelihood:                -37.321
No. Observations:                 150   AIC:                             82.64
Df Residuals:                     146   BIC:                             94.69
Df Model:                           3                                         
Covariance Type:            nonrobust                                         
================================================================================
                   coef    std err          t      P>|t|      [0.025      0.975]
--------------------------------------------------------------------------------
Intercept        1.8560      0.251      7.401      0.000       1.360       2.352
Sepal_Width      0.6508      0.067      9.765      0.000       0.519       0.783
Petal_Length     0.7091      0.057     12.502      0.000       0.597       0.821
Petal_Width     -0.5565      0.128     -4.363      0.000      -0.809      -0.304
==============================================================================
Omnibus:                        0.345   Durbin-Watson:                   2.060
Prob(Omnibus):                  0.842   Jarque-Bera (JB):                0.504
Skew:                           0.007   Prob(JB):                        0.777
Kurtosis:                       2.716   Cond. No.                         54.7
==============================================================================

Warnings:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
"""

# Adj. R-squared:                  0.856  : 설명력 good
# F-statistic:                     295.5  : 채택역은 -1.96 ~ +1.96  : 이를 벗어나면 통계적으로 유의하다
# Prob (F-statistic):           8.59e-62  : p-value에 해당. < 0.05이면 회귀적으로 유의한 통계라는 뜻


# [조건 최수미 ㅎ] 시각화
y_reg_pred = model_reg.fittedvalues
y_reg_pred

y_reg_true = iris.Sepal_Length

plt.plot(y_reg_true, 'b', label='real values')
plt.plot(y_reg_pred, 'r.-', label = 'predicted sepal length')
plt.legend(loc='best')
plt.show()

# or

plot(x, y, 'b.')
plot(x, y_reg_pred, 'r.-')
legend(['scatter x, y', 'predicted sepal length'])
show()
