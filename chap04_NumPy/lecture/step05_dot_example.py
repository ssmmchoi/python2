# -*- coding: utf-8 -*-
"""
신경망에서 행렬곱 적용 예

 - 은닉층(h) = [입력(X) * 가중치(w)] + 편향(b)
 
"""
import numpy as np
import matplotlib.pylab as plt
import seaborn as sns

# 1. ANN model
# input : image(28x28), hidden node : 32개 -> weight[?,?] 

# 2. input data : image data
28*28  # 784
x_img = np.random.randint(0,256,size=784)
x_img.shape  # (784,)
x_img.max()  # 255

#  이 만든 픽셀 값을 정규화(이미지 정규화)
x_img = x_img / 255
x_img
plt.plot(x_img)
sns.distplot(x_img)

x_img.max()  # 1.0
x_img_2d = x_img.reshape(28,28)
x_img_2d.shape  #  (28, 28)

# 3. weight (28,32)로 만들자. 28은 연산을 위해, 32는 h node를 위해
weight = np.random.randn(28, 32)
weight


# 4. hidden layer
hl = np.dot(x_img_2d, weight)
hl
hl.shape  # (28, 32) : 연산을 하는 횟수가(?) hidden layer 의 노드 수












