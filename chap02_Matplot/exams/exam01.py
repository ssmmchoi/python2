'''
문1) iris.csv 파일을 이용하여 다음과 같이 차트를 그리시오.
    <조건1> iris.csv 파일을 iris 변수명으로 가져온 후 파일 정보 보기
    <조건2> 1번 칼럼과 3번 칼럼을 대상으로 산점도 그래프 그리기
    <조건3> 1번 칼럼과 3번 칼럼을 대상으로 산점도 그래프 그린 후  5번 칼럼으로 색상 적용 
'''

import pandas as pd
import matplotlib.pyplot as plt


# <조건1> iris.csv 파일을 iris 변수명으로 가져온 후 파일 정보 보기
iris = pd.read_csv("iris.csv")
iris.head()
iris.info()

# <조건2> 1번 칼럼과 3번 칼럼을 대상으로 산점도 그래프 그리기
plot1 = plt.scatter(iris.iloc[:,0], iris.iloc[:,3], c='r', marker='o')
# plot1 = plt.scatter(iris.iloc[:,0], iris.iloc[:,3], c=cdata, marker='o')  왜인진 모르겠지만 아님


# <조건3> 1번 칼럼과 3번 칼럼을 대상으로 산점도 그래프 그린 후  5번 칼럼으로 색상 적용 
s1 = pd.Series(iris.Species)
s1.value_counts()
"""
setosa        50
versicolor    50
virginica     50
"""
cdata = []
for i in range(len(iris.Species)) :
    if iris.Species[i] == 'setosa' :
        cdata.append(1)
    elif iris.Species[i] == 'versicolor' :
        cdata.append(2)
    else :
        cdata.append(3)

print(cdata)
cdata_s = pd.Series(cdata)
cdata_s.head()


plot2 = plt.scatter(iris.iloc[:,0], iris.iloc[:,3], c=cdata, marker='o')
plot3 = plt.scatter(iris.iloc[:,0], iris.iloc[:,3], c=cdata_s, marker='o')





