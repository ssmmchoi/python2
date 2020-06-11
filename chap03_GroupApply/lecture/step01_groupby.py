# -*- coding: utf-8 -*-
"""
DataFrame 객체 대상 그룹화
 - 형식) DF.groupby('집단변수').수학/통계함수()
"""

import pandas as pd
tips = pd.read_csv("C:/ITWILL/Work/4_Python-II/data/tips.csv")
tips.info()
tips.head()
"""                  object object object object
   total_bill   tip     sex smoker  day    time  size
0       16.99  1.01  Female     No  Sun  Dinner     2
1       10.34  1.66    Male     No  Sun  Dinner     3
2       21.01  3.50    Male     No  Sun  Dinner     3
3       23.68  3.31    Male     No  Sun  Dinner     2
4       24.59  3.61  Female     No  Sun  Dinner     4
"""

# 팁 비율 : 파생변수
tips['tip_per'] = tips['tip'] / tips['total_bill']
tips.info()
tips.head()
tips.tail()

# 변수 복제
tips['gender'] = tips['sex']

# 변수 제거
del tips['sex']
tips.info()

tips.groupby(['size']).sum()

# 1. 집단변수 1개 -> 전체 칼럼 그룹화
gender_grp = tips.groupby('gender')
gender_grp  # object info : <pandas.core.groupby.generic.DataFrameGroupBy object at 0x000001D5B6022948>

# 그룹객체.함수()
gender_grp.size()
"""  각 그룹의 빈도수
gender
Female     87
Male      157
dtype: int64
"""

# 그룹 통계량
gender_grp.sum()  # 대상은 모두 숫자변수 칼럼만.
"""
        total_bill     tip  size    tip_per
gender                                     
Female     1570.95  246.51   214  14.484694
Male       3256.82  485.07   413  24.751136
"""
gender_grp.mean()
"""
        total_bill       tip      size   tip_per
gender                                          
Female   18.056897  2.833448  2.459770  0.166491
Male     20.744076  3.089618  2.630573  0.157651
"""

# 해당 객체에서 호출 가능한 멤버 리스트 확인
dir(gender_grp)  

# 그룹별 요약통계량
gender_grp.describe()  # 수치 제공
"""
       total_bill                       ...   tip_per                    
            count       mean       std  ...       50%       75%       max
gender                                  ...                              
Female       87.0  18.056897  8.009209  ...  0.155581  0.194266  0.416667
Male        157.0  20.744076  9.246469  ...  0.153492  0.186240  0.710345
"""
gender_grp.boxplot()  # 그래프제공


# 2. 집단변수 1개 -> 특정 칼럼 그룹화
smoker_grp = tips['tip'].groupby(tips['smoker'])
smoker_grp  # <pandas.core.groupby.generic.SeriesGroupBy object at 0x000001D5B93C5C88>
smoker_grp.head()
smoker_grp.tail()
smoker_grp.size()
"""No     151
Yes     93"""

smoker_grp.mean()
"""No     2.991854
Yes    3.008710"""


# 3. 집단변수 2개 -> 전체 칼럼 그룹화
# 형식) DF.groupby(['칼럼1', '칼럼2'])  # 1차:칼럼1, 2차:칼럼2
gender_smoker_grp = tips.groupby(['gender', 'smoker'])
gender_smoker_grp.size()
"""
        gender  smoker
Female  No        54
        Yes       33
Male    No        97
        Yes       60
"""

# 특정 변수 통계량
gender_smoker_grp.describe()
gender_smoker_grp['tip'].describe()
"""
               count      mean       std   min  25%   50%     75%   max
gender smoker                                                          
Female No       54.0  2.773519  1.128425  1.00  2.0  2.68  3.4375   5.2
       Yes      33.0  2.931515  1.219916  1.00  2.0  2.88  3.5000   6.5
Male   No       97.0  3.113402  1.489559  1.25  2.0  2.74  3.7100   9.0
       Yes      60.0  3.051167  1.500120  1.00  2.0  3.00  3.8200  10.0
[해설] 여성은 흡연자, 남성은 비흡연자가 팀 지불에 후하다
"""


# 4. 집단변수 2개 -> 특정 칼럼 그룹화
gender_smoker_tip_grp = tips['tip'].groupby([tips['gender'], tips['smoker']])
gender_smoker_tip_grp.size()
"""     gender  smoker
Female  No        54
        Yes       33
Male    No        97
        Yes       60"""
gender_smoker_tip_grp.size().shape  # (4,)  : 1차원 vector
gender_smoker_tip_grp.sum()  # 각 집단별 tip 합계
"""     gender  smoker
Female  No        149.77
        Yes        96.74
Male    No        302.00
        Yes       183.07"""
# 1d -> 2d
grp_2d = gender_smoker_tip_grp.sum().unstack()
grp_2d  # 성별 vs 흡열유무 교차분할표(합계)
"""
smoker      No     Yes
gender                
Female  149.77   96.74
Male    302.00  183.07 """
grp_2d.shape  # (2, 2)

# 2d -> 1d
grp_1d = grp_2d.stack()
grp_1d  # 
"""
gender  smoker
Female  No        149.77
        Yes        96.74
Male    No        302.00
        Yes       183.07 """

# 성별 vs 흡연유무 -> 교차분할표(빈도수)
grp_2d_size = gender_smoker_tip_grp.size().unstack()
grp_2d_size
"""
smoker  No  Yes
gender         
Female  54   33
Male    97   60
"""





# iris dataset 그룹화
# 1) dataset load
iris = pd.read_csv("iris.csv")
iris.info()

# 2) group : group -> apply(sum)
iris_grp = iris.groupby(['Species'])
iris_grp.size()
"""
setosa        50
versicolor    50
virginica     50"""

iris_grp.sum()
"""
            Sepal.Length  Sepal.Width  Petal.Length  Petal.Width
Species                                                         
setosa             250.3        171.4          73.1         12.3
versicolor         296.8        138.5         213.0         66.3
virginica          329.4        148.7         277.6        101.3
"""

# 3) 집단변수 1개 이용하여 Sepal.Width만 그룹화
iris['Sepal.Width'].groupby(iris['Species']).sum()
"""
setosa        171.4
versicolor    138.5
virginica     148.7"""  # or,
iris_grp['Sepal.Width'].sum()
"""
setosa        171.4
versicolor    138.5
virginica     148.7
"""























