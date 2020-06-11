# -*- coding: utf-8 -*-
"""
문) california 주택가격을 대상으로 다음과 같은 단계별로 선형회귀분석을 수행하시오.
"""

# california 주택가격 데이터셋 
'''
캘리포니아 주택 가격 데이터(회귀 분석용 예제 데이터)

•타겟 변수
1990년 캘리포니아의 각 행정 구역 내 주택 가격의 중앙값

•특징 변수(8) 
MedInc : 행정 구역 내 소득의 중앙값
HouseAge : 행정 구역 내 주택 연식의 중앙값
AveRooms : 평균 방 갯수
AveBedrms : 평균 침실 갯수
Population : 행정 구역 내 인구 수
AveOccup : 평균 자가 비율
Latitude : 해당 행정 구역의 위도
Longitude : 해당 행정 구역의 경도
'''

from sklearn.datasets import fetch_california_housing # dataset load
import pandas as pd # DataFrame 생성 
from sklearn.linear_model import LinearRegression  # model
from sklearn.model_selection import train_test_split # dataset split
from sklearn.metrics import mean_squared_error, r2_score # model 평가 
import matplotlib.pyplot as plt 

# 캘리포니아 주택 가격 dataset load 
california = fetch_california_housing()
print(california.DESCR)
california.data
colnames = california.feature_names

df = pd.DataFrame(california.data, columns = colnames)
df



# 단계1 : 특징변수와 타켓변수(MEDV)를 이용하여 DataFrame 생성하기     ::: target?
california.target
df['MEDV'] = california.target
df.info()
len(california.target)  # 20640



# 단계2 : 타켓변수와 가장 상관관계가 높은 특징변수 확인하기  
cor = df.corr()
cor.MEDV
"""
MedInc        0.688075  >> 가장 높은 변수. x
HouseAge      0.105623  > x2
AveRooms      0.151948  > x3
AveBedrms    -0.046701
Population   -0.024650
AveOccup     -0.023737
Latitude     -0.144160  > x4
Longitude    -0.045967
MEDV          1.000000
"""


# 단계3 : california 데이터셋(=df)을 대상으로 1만개 샘플링하여 서브셋 생성하기  
import numpy as np
idx = np.random.choice(20640, 10000, replace=False)
idx

cal_sam = df.loc[idx, :]
cal_sam
len(cal_sam.MEDV)  # Out[380]: 10000




# 단계4 : 단계3의 데이터를 75%(train) vs 25(test) 비율 데이터셋 split 
train, test = train_test_split(cal_sam, random_state=123)
train.shape  # (7500, 9)
test.shape  # (2500, 9)

type(train)  # pandas.core.frame.DataFrame
x_train = train.loc[:, ['MedInc', 'HouseAge', 'HouseAge', 'AveBedrms', 'Population', 'Population', 'Latitude', 'Longitude']]
x_train.shape  # (7500, 8)
x_train.info()
y_train = train.loc[:, ['MEDV']]
y_train.shape  # (7500, 1)

x_test = test.loc[:, ['MedInc', 'HouseAge', 'HouseAge', 'AveBedrms', 'Population', 'Population', 'Latitude', 'Longitude']]
x_test.shape  # (2500, 8)
y_test = test.loc[:, ['MEDV']]
y_test.shape  # (2500, 1)



# 단계5 : 선형회귀모델 생성
lr = LinearRegression()
model = lr.fit(X=x_train, y=y_train)
model

y_pred = model.predict(x_test)
y_pred[:5]  # np.array
y_test[:5]  # pd.dataframe
type(y_test)



# 단계6 : 모델 검정(evaluation)  : 예측력 검정, 과적합(overfitting) 확인  
mse = mean_squared_error(y_test, y_pred)
mse  # 0.5274189872712136

r2 = r2_score(y_test, y_pred)
r2  # 0.606146996673435 정확률이 약 60%

# 원본데이터에 넣어볼깡
y_pred_or = model.predict(california.data)
y_pred_or.shape  # (20640, 1), array

y_true_or = california.target
y_true_or.shape  # (20640,)
y_true_or = y_true_or.reshape(20640,1)
y_true_or.shape

mse_or = mean_squared_error(y_true_or, y_pred_or)
mse_or  # 0.5515218603026506

r2_or = r2 = r2_score(y_true_or, y_pred_or)
r2_or  #  0.5858047117943901 : 원본에 넣으니 정확률이 아주조금 더 떨어짐. 과적합 이 아주조금 있다는 뜻인 것 같음.



## [정답]   ************************** 정확한 이름은 test data가 아니라 evaluation용 데이타
train_acc = model.score(x_train, y_train)
train_acc  # 0.5895442139986966
test_acc = model.score(x_test, y_test)
test_acc  # 0.606146996673435  >> 훈련셋과 검정셋 모두 비슷한 분류정확도 >> 과적합 X#











# 단계7 : 모델 평가(test) 
# 조건1) 단계3의 서브셋 대상으로 30% 샘플링 자료 이용
# 조건2) 평가방법 : MSE, r2_score
test_idx = np.random.choice(a=len(cal_sam), size = int(len(cal_sam)*0.3), replace=False)

modeltest = df.loc[test_idx, :]
modeltest.shape  # (3000, 9)

predtest = model.predict(modeltest.iloc[:,:8])  # 예측치
type(predtest)
truetest = modeltest.iloc[:,8]
type(truetest)  # pandas.core.series.Series

mse_test = mean_squared_error(truetest, predtest)
mse_test   # 0.5935521055307215

r2_test = r2_score(truetest, predtest)
r2_test  # 0.5620018169006155 정확률 not good


# 단계8 : 예측치 100개 vs 정답 100개 비교 시각화 
truetest = np.array(truetest)


plt.plot(truetest[:100], color='b', label='real values')
plt.plot(predtest[:100], color='r', label = 'fitted values')
plt.xlabel('index')
plt.ylabel('fitted values')
plt.legend(loc='best')
plt.show()









