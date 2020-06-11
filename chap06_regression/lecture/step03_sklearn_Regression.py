# -*- coding: utf-8 -*-
"""
sklearn 관련 Linear Regression
"""

from sklearn.linear_model import LinearRegression  # model object
from sklearn.model_selection import train_test_split  # train/test split
from sklearn.metrics import mean_squared_error, r2_score  # model 평가
from sklearn.datasets import load_diabetes  # dataset
import numpy as np


###########################
#### diabetes
###########################

# 단순선형회귀 : x(1) -> y

# 1. dataset load
X, y = load_diabetes(return_X_y = True)
X.shape  # (442, 10)
y.shape  # (442,)
y.mean()  # 152.13348416289594
X

# 2. x, y 변수
# x(bmi : 비만도지수) -> y
x_bmi = X[:, 2]
x_bmi.shape  # (442,)

# 3. model 생성 : object -> training -> model
obj = LinearRegression()  # 생성자() -> object
obj.fit()  # x, y 변수로 모델을 학습시켜주는 역할.
#model = obj.fit(x_bmi, y)  # (X,y) -> model  # ValueError: Expected 2D array, got 1D array instead:

x_bmi = x_bmi.reshape(442,1)  # 1d -> 2d : 함수가 이와 같은 형식의 변수를 요구하기 때문
model = obj.fit(x_bmi, y)
model


# model의 예측치
y_pred = model.predict(x_bmi)  # predict(X)
y_pred.shape  # (442,)


# model 평가  : MSE(정규화0), !!r2_Score(정규화X)!!
mse = mean_squared_error(y, y_pred)
mse  # 3890.4565854612724

r2 = r2_score(y, y_pred)
r2  # 0.3439237602253803


# 4. dataset split(70:30)
x_train, x_test, y_train, y_test = train_test_split(x_bmi, y, test_size=0.3, random_state=123)
x_train.shape  #  (309, 1)
x_test.shape   # (133, 1)
y_train.shape  # (309,)
y_test.shape  #  (133,)
y_test.mean()

model_train = obj.fit(x_train, y_train)
model_train

y_pred2 = model_train.predict(x_test)
y_pred2
y_pred2.shape  # (133,)

# 다시 평가
r2 = r2_score(y_test, y_pred2)
r2  # 0.3082201463223284  위 모델 평가와 거의 유사함

MSE = mean_squared_error(y_test, y_pred2)
MSE  # 4113.813814261836 ???????????????????????????????????


y_test[:10]
y_pred[:10]


import pandas as pd
df = pd.DataFrame({'y_true' : y_test, 'y_pred' : y_pred})
cor = df['y_true'].corr(df['y_pred'])
cor  # 0.5580208836956722  :1 에 가까울수록 예측력 good


import matplotlib.pyplot as plt
plt.plot(x_test, y_test, 'bo', label='x vs y true')
plt.plot(x_test, y_pred, 'r.-', label = 'x vs y predicted')
plt.legend(loc='best')
plt.show()



################################
##### iris.csv
################################
# 다중회귀모델 생성. y(1st) <- x(3 rest), 5th remove

iris = pd.read_csv('C:\\ITWILL\\Work\\4_Python-II\\data\\iris.csv')
cols = list(iris.columns)
cols  # ['Sepal.Length', 'Sepal.Width', 'Petal.Length', 'Petal.Width', 'Species']

y_col = cols[0]
x_col = cols[1:4]
# or
x_col = cols[1:-1]
y_col  # 'Sepal.Length'
x_col  # ['Sepal.Width', 'Petal.Length', 'Petal.Width']

# x = iris[x_col]
# x.info()
# y = iris[y_col]
# y.shape

# dataset split(default test_size=0.25)
# x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=123)
iris_train, iris_test = train_test_split(iris, test_size=0.3, random_state=123)
iris_train.shape  # (105, 5)
iris_test.shape  # (45, 5)

# x_train = iris_train[x_col]
# x_test = iris_test[x_col]
# y_train = iris_train[y_col]
# y_test = iris_test[y_col]
# x_train.shape
# y_test.shape


# model  생성

# from statsmodels.formula.api import ols
# # formula = "y_train ~ x_train"
# model = ols(X=iris_train[x_col], y=iris_train[y_col], data = iris_train).fit()

lr = LinearRegression()
model = lr.fit(X=iris_train[x_col], y=iris_train[y_col])
model


# 5. model 평가 : test data
y_pred = model.predict(X=iris_test[x_col])
y_true = iris_test[y_col]


y_true.min()  # 4.3
y_true.max()  # 7.9  >> both 어느 정도 정규화가 되어 있는 작은 값

mse = mean_squared_error(y_true, y_pred)
mse  # 0.11633863200224723

r2 = r2_score(y_true, y_pred)
r2      # 0.8546807657451759   : 1이 100% 예측
    

# y_true vs y_pred 시각화
import matplotlib.pyplot as plt
# plt.plot(x_test, y_test, 'bo', label = 'x vs y true value')
# plt.plot(x_test, y_pred, 'r.-', label = 'x vs y predicted')
# plt.legend(loc='best')
# plt.show()

type(y_true)  # pandas.core.series.Series
type(y_pred)  # numpy.ndarray : 자료형이 서로 다르다.
y_true = np.array(y_true)

fig = plt.figure(figsize=(10,5))   
chart = fig.subplots()
chart.plot(y_true, color = 'b', label='real values')
chart.plot(y_pred, color='r', label='fitted values')
plt.legend(loc='best')
plt.show()



plt.plot(y_true, color = 'b', label='real values')
plt.plot(y_pred, color='r', label='fitted values')
plt.legend(loc='best')
plt.show()
