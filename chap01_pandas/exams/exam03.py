'''  
step02 관련문제
문3) 다음 df를 대상으로 iloc 속성을 이용하여 단계별로 행과 열을 선택하시오.
   단계1 : 1,3행 전체 선택    
   단계2 : 1~4열 전체 선택 
   단계3 : 1,3행 1,3,5열 선택
'''
import pandas as pd
import numpy as np

data = np.arange(1, 16).reshape(3,5) # 3x5
print(data)

df = pd.DataFrame(data, index = ['one', 'two', 'three'],
                  columns = [1,2,3,4,5])
print(df)
"""
        1   2   3   4   5
one     1   2   3   4   5
two     6   7   8   9  10
three  11  12  13  14  15
"""

#단계1 : 1,3행 전체 선택 
step01 = df.loc[['one', 'three'], :]
print(step01)

step01_2 = df.iloc[[0,2], :]
print(step01_2)



#단계2 : 1~4열 전체 선택
step02 = df.loc[:, 1:4]
print(step02)
"""
        1   2   3   4
one     1   2   3   4
two     6   7   8   9
three  11  12  13  14
"""
step02_2 = df.iloc[:, :4]
print(step02_2)
"""
        1   2   3   4
one     1   2   3   4
two     6   7   8   9
three  11  12  13  14
"""


#단계3 : 1,3행 1,3,5열 선택
step03 = df.loc[['one', 'three'], [1,3,5]]
print(step03)
"""
        1   3   5
one     1   3   5
three  11  13  15
"""

step03_2 = df.iloc[[0, 2],[0,2,4]]
print(step03_2)
"""
        1   3   5
one     1   3   5
three  11  13  15
"""









