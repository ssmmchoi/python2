# -*- coding: utf-8 -*-
"""
DataFrame 병합(merge)
 ex) DF1(id) + DF2(id) -> DF3
"""

import pandas as pd
from pandas import Series, DataFrame

# 1. Series merge : 1 dimension
s1 = Series([1,3], index=['a', 'b'])
s2 = Series([5,6,7], index=['a', 'b', 'c'])
s3 = Series([11,13], index=['a', 'b'])

# 행단위 결합 : R의 rbingd()
s4 = pd.concat([s1, s2, s3], axis=0)  # 결합하고자 하는 아이들을 리스트 안에 넣어줌
                                        # axis 생략하면 0 default
s4.shape  # (7,)
print(s4)
"""
a     1
b     3
a     5
b     6
c     7
a    11
b    13
dtype: int64
"""

# 열단위 결합 : R의 cbind()
s5 = pd.concat([s1,s2,s3], axis=1)
s5.shape  # (3, 3)
print(s5)
"""
     0  1     2
a  1.0  5  11.0
b  3.0  6  13.0
c  NaN  7   NaN
"""


# 2. DataFrame 병합
wdbc=pd.read_csv('wdbc_data.csv')
print(wdbc.info())

# DF1(앞16개) + DF2(뒤 16개)
cols = list(wdbc.columns)
len(cols)  # 32

DF1 = wdbc[cols[:16]]  # [['']]
DF1.shape  # (569, 16)
DF2 = wdbc[cols[16:]]
DF2.shape  # (569, 16)

# id 칼럼 추가
id = wdbc.id
DF2.shape  # (569, 17)
DF2['id'] = id
DF2.head()  # 경고메시지가 나오지만 id 칼럼이 생기긴 함. 이제 두 DF을 id를 기준으로 머지할 수 있음

DF_merge = pd.merge(DF1, DF2)
DF_merge.info()  # 처음 로드한 wdbc와 같아짐
"""
<class 'pandas.core.frame.DataFrame'>
Int64Index: 569 entries, 0 to 568
Data columns (total 32 columns):
"""

# 결합 : 카럼 단위 결합
DF1 = wdbc[cols[:16]]
DF1.shape

DF2 = wdbc[cols[16:]]
DF2.shape

DF4 = pd.concat([DF1, DF2], axis=1)  # 열 단위 결합
DF4.info()
DF4.head()















