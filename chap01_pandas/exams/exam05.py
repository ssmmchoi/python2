'''   
문5) iris.csv 파일을 읽어와서 다음과 같이 처리하시오.
   조건1> 1~4 칼럼 대상 vector 생성(col1, col2, col3, col4)    
   조건2> 1,4 칼럼 대상 합계, 평균, 표준편차 구하기 
   cc
   조건4> df1과 df2 칼럼 단위 결합 iris_df 데이터프레임 생성      
'''

import pandas as pd

iris = pd.read_csv('C:/ITWILL/Work/4_Python-II/data/iris.csv')
print(iris.info())

# 조건1> 1~4 칼럼 대상 vector 생성(col1, col2, col3, col4)    
col1 = iris.iloc[:,0]
col2 = iris.iloc[:,1]
col3 = iris.iloc[:,2]
col4 = iris.iloc[:,3]

print(col1)
print(col4)
colnames = list(iris.columns)
print(colnames)

# 조건2> 1,4 칼럼 대상 합계, 평균, 표준편차 구하기 
# col1
col1.sum()  # 876.5
round(col1.mean(),2)  #  5.84
round(col1.std(), 2)  # 0.83
# or
col1.describe()
"""
count    150.000000
mean       5.843333  !
std        0.828066  !
min        4.300000
25%        5.100000
50%        5.800000
75%        6.400000
max        7.900000
Name: Sepal.Length, dtype: float64
"""

# col2
col2.sum()  #  458.6
round(col2.mean(),2)  # 3.06
round(col2.std(), 2)  # 0.44


# col3
col3.sum()  # 563.7
round(col3.mean(),2)  #  3.76
round(col3.std(), 2)  # 1.77


# col4
col4.sum()  # 179.90000000000003
round(col4.mean(),2)  #  1.2
round(col4.std(), 2)  # 0.76


# 조건3> 1,2 칼럼과 3,4 칼럼을 대상으로 각 df1, df2 데이터프레임 생성
df1 = pd.concat([col1, col2], axis=1)
df1.info()
df2 = pd.concat([col3, col4], axis=1)
df2.info()
