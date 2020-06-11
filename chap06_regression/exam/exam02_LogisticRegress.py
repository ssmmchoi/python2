'''
문) load_wine() 함수를 이용하여 와인 데이터를 다항분류하는 로지스틱 회귀모델을 생성하시오. 
  조건1> train/test - 7:3비울
  조건2> y 변수 : wine.target
  조건3> x 변수 : wine.data
  조건4> 모델 평가 : confusion_matrix, 분류정확도[accuracy]
'''

from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from sklearn.metrics import accuracy_score

# 1. wine 데이터셋 
wine = load_wine()


# 2. 변수 선택 
wine_x = wine.data # x변수 
wine_y = wine.target # y변수

# 3. train/test split(7:3)
x_train, x_test, y_train, y_test = train_test_split(wine_x, wine_y, test_size=0.3, random_state=123)
x_train.shape  # (124, 13)
x_test.shape  # (54, 13)
y_train.shape  # (124,)
y_test.shape  #  (54,)


# 4. model 생성  : solver='lbfgs', multi_class='multinomial'
lr = LogisticRegression(solver='lbfgs', multi_class='multinomial', random_state=123)
lr2 = LogisticRegression(solver='lbfgs', multi_class='multinomial', random_state=123,
                         max_iter=200, n_jobs=1, verbose=1)
'''
max_iter=200 반복횟수
n_jobs=1 병렬처리 cpu수
verbose=1 학습과정 출력여부
'''
model=lr.fit(x_train, y_train)
model
model2 = lr2.fit(x_train, y_train)

y_pred = model.predict_proba(x_test)
y_pred
type(y_pred)
y_pred2 = model.predict(x_test)
y_pred2
"""
array([2, 1, 2, 1, 1, 2, 0, 2, 2, 1, 2, 2, 2, 0, 0, 2, 1, 1, 0, 1, 2, 2,
       2, 2, 1, 2, 2, 1, 0, 0, 0, 0, 2, 1, 2, 1, 1, 0, 1, 1, 2, 2, 0, 0,
       1, 0, 0, 1, 1, 1, 1, 2, 2, 1])
"""

# y_pred를 if문으로 y_pred의 형태로.
y_pred3 = []
for row in y_pred :
    if row[0] > 0.5 :
        y_pred3.append(0)
    else :  # row[1] or row[2]가 > 0.5
        if row[1] > 0.5 :
            y_pred3.append(1)
        else : 
            y_pred3.append(2)

y_pred3
import numpy as np
y_pred3 = np.array(y_pred3)a
y_pred3.shape  # (54,)


# [model2] 예측치는 yp라고 하쟈.
yp = model2.predict_proba(x_test)
yp
yp2 = model2.predict(x_test)
yp2

yp3 = []
for row in yp :
    if row[0] > 0.5 :
        yp3.append(0)
    else :  # row[1] or row[2]가 > 0.5
        if row[1] > 0.5 :
            yp3.append(1)
        else : 
            yp3.append(2)

yp3
import numpy as np
yp3 = np.array(yp3)
yp3.shape 



# 5. 모델 평가 : accuracy, confusion matrix

# 1) confusion matrix
conmat = confusion_matrix(y_test, y_pred2)
conmat
"""
array([[13,  1,  0],
       [ 0, 18,  0],
       [ 0,  1, 21]], dtype=int64)
"""
acc = (conmat[0,0] + conmat[1,1] + conmat[2,2]) / conmat.sum()
acc  # 0.9629629629629629
#or
conmat2 = confusion_matrix(y_test, y_pred3)
conmat2  # conmat과 똑같이 나옴. acc도 동일


# 2) model.score(x_test, y_pred)
acc2 = model.score(x_test, y_test)
acc2  # 0.9629629629629629


# 3) accuacy_score
acc3 = accuracy_score(y_test, y_pred2)
acc3  # 0.9629629629629629

acc3_2 = accuracy_score(y_test, y_pred3)
acc3_2  #  0.9629629629629629



# [model 2] 평가   :::::::  이 모델이 정확도가 더 낮음.
conmat = confusion_matrix(y_test, yp3)
conmat
"""
array([[13,  1,  0],  wine의 클래스가 0번인 경우
       [ 1, 17,  0],   1번인 경우
       [ 0,  1, 21]],   2번인경우
"""
acc = (conmat[0,0] + conmat[1,1] + conmat[2,2]) / conmat.sum()
acc  # 0.9444444444444444




# (+) 시각화
import matplotlib.pyplot as plt
import seaborn as sn

plt.figure(figsize=(10,10))
sn.heatmap(conmat2, annot=True, fmt='.3f', linewidths=.5, square=True)
plt.ylabel('Acual value')
plt.xlabel('Predicted value')
title_all = "Accuracy Score = {0}".format(acc)
plt.title(title_all, size=18)
plt.show()











