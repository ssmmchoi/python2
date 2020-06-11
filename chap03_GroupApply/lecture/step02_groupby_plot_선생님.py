# -*- coding: utf-8 -*-
"""
집단변수 기준 자료 분석 
 - subset 생성 
 - group 객체 생성 
 - 시각화 
"""

import pandas as pd

# 1. dataset load 
wine = pd.read_csv('C:\\ITWILL\\Work\\4_Python-II\\data\\winequality-both.csv')
wine.info() # type, quality 

# 칼럼명 변경 : 공백 -> '_' 교체 
wine.columns = wine.columns.str.replace(' ', '_')
wine.info()
# RangeIndex: 6497 entries, 0 to 6496
# Data columns (total 13 columns)

# 집단변수 확인 
wine['type'].unique() # ['red', 'white']
wine.quality.unique() # [5, 6, 7, 4, 8, 3, 9]

# 2. subset 생성

# 1) type 칼럼 : DataFrame(2차원) 
red_wine = wine.loc[wine['type']=='red'] #[row, col]
red_wine.info()
# Int64Index: 1599 entries, 0 to 1598
# Data columns (total 13 columns):
red_wine.shape # (1599, 13)

# 2) type(행) vs quality(열) : Series(1차원) 
red_quality = wine.loc[wine['type']=='red', 'quality']#[행, 열]
type(red_quality) # pandas.core.series.Series
red_quality.shape # (1599,)
red_quality.head(20)

white_quality = wine.loc[wine['type']=='white', 'quality']#[행, 열]
type(white_quality) # pandas.core.series.Series
white_quality.shape # (4898,)


# 3. group 객체 생성 : 집단변수 2개 -> 11변수 그룹화 
# 형식) DF.groupby(['칼럼1', '칼럼2']) 
wine_grp = wine.groupby(['type', 'quality'])
# 각 그룹의 빈도수 
wine_grp.size()
'''
type   quality
red    3            10
       4            53
       5           681
       6           638
       7           199
       8            18
white  3            20
       4           163
'''  

# 1d -> 2d : 교차분할표 
grp_2d = wine_grp.size().unstack()
grp_2d
'''
quality     3      4       5       6      7      8    9
type                                                   
red      10.0   53.0   681.0   638.0  199.0   18.0  NaN
white    20.0  163.0  1457.0  2198.0  880.0  175.0  5.0
'''

# 교차분할표
tab = pd.crosstab(wine['type'], wine['quality']) # (index=행, columns=열)
tab
'''
quality   3    4     5     6    7    8  9
type                                     
red      10   53   681   638  199   18  0
white    20  163  1457  2198  880  175  5
'''

# 4. group 객체 시각화
import matplotlib.pyplot as plt

type(grp_2d) # pandas.core.frame.DataFrame

# 누적형 가로막대 
grp_2d.plot(kind='barh',
            title='type vs quality',
            stacked=True)
plt.show()


# 5. wine 종류(집단변수) vs 알콜(연속형) 통계량 
wine_grp = wine.groupby('type') # 집단변수 1개 -> 12개 변수 그룹화 

# 각 집단별 알콜 요약통계량 
wine_grp['alcohol'].describe()
'''
        count       mean       std  min  25%   50%   75%   max
type                                                          
red    1599.0  10.422983  1.065668  8.4  9.5  10.2  11.1  14.9
white  4898.0  10.514267  1.230621  8.0  9.5  10.4  11.4  14.2
'''      





     







