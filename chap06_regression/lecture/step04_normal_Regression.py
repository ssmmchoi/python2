# -*- coding: utf-8 -*-
"""
data scaling(정규화, 표준화)  : 이물질 제거
 - 특정 변수의 값에 따라서(그 값의 크기 등의 특성이) model에 (불필요한) 영향을 미치는 경우
     ex) 범죄율(-0.1 ~ 0.99), 주택가격(99~999) -> 회귀분석에서 비교적 값의 규모가 큰 주택 가격이 영향을 더 크게 미친다.
 - 정규화(X변수) :변수의 값을 일정한 범위로 조정(0~1, -1~1)
 - 표준화(Y변수) : 평균(0)과 표준편차(1)를 이용
     표준화 공식 z = (x-mu) / sd
"""

from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

import numpy as np

# 1. load data
X, y = load_boston(return_X_y=True)
X.shape  # (506, 13)
y.shape  # (506,)

# 2. data scaling
# X : 정규화(0~1)
# 표준화(평균0, 표준편차1)

X.max()  # 711.0
X.mean()  # 70.07396704469443
y.max()  # 50.0
y.mean()  # 22.532806324110677

# 정규화함수
def normal(x) :
    nor = (x-np.min(x)) / np.max(x) - np.min(x)
    return nor

# 표준화함수
def zscore(y) :
    mu = y.mean()
    z = (y - mu) / y.std()  # y가 np객체라서 바로 std 적용가능
    return z

# X 변수 정규화
x_nor = normal(X)
x_nor.mean()  # 0.09855691567467571

# Y 변수 표준화
y_nor = zscore(y)  # mu=0, std=1
y_nor.mean()  # -5.195668225913776e-16 : 0에 수렴
y_nor.std()  # 0.9999999999999999 : 1에 수렴


# 3. dataset split
x_train, x_test, y_train, y_test = train_test_split(x_nor, y_nor, random_state=123)

x_train.shape  # (379, 13)
x_test.shape  # (127, 13)


# 4. model 생성
lr = LinearRegression()
model = lr.fit(X=x_train, y=y_train)
model


# 5. model평가
y_pred = model.predict(x_test)
len(y_pred)  # 127


mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print('MSE = ', mse)  # MSE =  0.2933980240643525  오류율(약 30%)
print('r2 score =', r2)  # r2 score = 0.6862448857295749 정확률(약 70%)
























































