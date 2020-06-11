'''
문) load_boston() 함수를 이용하여 보스턴 시 주택 가격 예측 회귀모델 생성 
  조건1> train/test - 7:3비울
  조건2> y 변수 : boston.target
  조건3> x 변수 : boston.data
  조건4> 모델 평가 : MSE, r2_score
'''

from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

import numpy as np
import pandas as pd

# 1. data load
boston = load_boston()
print(boston)
x_cols = boston.feature_names

# 2. 변수 선택  
X, y = load_boston(return_X_y = True)
X.shape  # (506, 13)
y.shape  # (506,)

# 3. train/test split
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=123)
x_train.shape  # (354, 13)
x_test.shape  # (152, 13)
y_train.shape  # (354,)
y_test.shape  # (152,)

# 4. 회귀모델 생성 : train set
obj = LinearRegression()
model = obj.fit(X=x_train, y=y_train)
model



# 5. 모델 평가 : test set
y_pred = model.predict(x_test)
y_true = y_test

from sklearn.metrics import mean_squared_error, r2_score
# mse
mse = mean_squared_error(y_true, y_pred)
mse  # 28.40585481050824

# r2_score
r2 = r2_score(y_true, y_pred)
r2  # 0.6485645742370703


# or!!  직접 계산 하면:

mse = sum((y_true - y_pred)**2) / len(y_true)
mse  # 28.405854810508238


## 보너스 : 시각화
import matplotlib.pyplot as plt

# plt.plot(x_test, y_test, 'bo', label='real values')
# plt.plot(x_test, y_pred, 'r.-', label='predicted values')
# plt.legend(loc='best')
# plt.show()


fig = plt.figure(figsize=(10,4))
chart=fig.add_subplot()
chart.plot(y_true, color='b', label='real values')
chart.plot(y_pred, color='r', label='fitted values')
plt.title('real values(blue) vs fitted values(red)')
plt.xlabel('index')
plt.ylabel('prediction')
plt.legend(loc='best')
plt.show()











