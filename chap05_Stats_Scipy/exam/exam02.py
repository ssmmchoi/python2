'''
문02) winequality-both.csv 데이터셋을 이용하여 다음과 같이 처리하시오.
   <조건1> quality, type 칼럼으로 교차분할표 작성 
   <조건2> 교차분할표를 대상으로 white 와인 내림차순 정렬       
   <조건3> red 와인과 white 와인의 quality에 대한 두 집단 평균 검정
           -> 각 집단 평균 통계량 출력
   <조건4> alcohol 칼럼과 다른 칼럼 간의 상관계수 출력  
'''

import pandas as pd
from scipy import stats

wine = pd.read_csv('C:\\ITWILL\\Work\\4_Python-II\\data\\winequality-both.csv')
wine.info()


# <조건1> quality, type 칼럼으로 교차분할표 작성 
wine_grp = wine.groupby(['quality', 'type'])
wine_grp.size()
'''
quality  type 
3        red        10
         white      20
4        red        53
         white     163
5        red       681
         white    1457
6        red       638
         white    2198
7        red       199
         white     880
8        red        18
         white     175
9        white       5
'''

wine_cross = wine_grp.size().unstack()
wine_cross
"""
type       red   white
quality               
3         10.0    20.0
4         53.0   163.0
5        681.0  1457.0
6        638.0  2198.0
7        199.0   880.0
8         18.0   175.0
9          NaN     5.0
"""

# or
wine_cross_other = pd.crosstab(wine.type, wine.quality)
wine_cross_other



# <조건2> 교차분할표를 대상으로 white 와인 내림차순 정렬 
wine_cross2 = wine_cross.sort_values(by = 'white', ascending=False)  # pandas
wine_cross2
'''
type       red   white
quality               
6        638.0  2198.0
5        681.0  1457.0
7        199.0   880.0
8         18.0   175.0
4         53.0   163.0
3         10.0    20.0
9          NaN     5.0
'''



# <조건3> red 와인과 white 와인의 quality에 대한 두 집단 평균 검정
#           -> 각 집단 평균 통계량 출력

# 1) ttest_ind()로
red = wine[wine['type']=='red'].quality
white = wine[wine['type']=='white'].quality
# or 
red_wine = wine.loc[wine['type']=='red', 'quality']
white_wine = wine.loc[wine['type']=='white', 'quality']
red_wine


test_t = stats.ttest_ind(red, white)
test_t  # Ttest_indResult(statistic=-9.685649554187696, pvalue=4.888069044201508e-22)

# [해설] 양측검정 -> 귀무가설 기각. 두 집단의 평균에는 차이가 있다.

# 단측검정을 수행하면 다음과 같은 결과를 알 수 있다(나중에배움) :
red.mean()  # 5.6360225140712945
white.mean()  # 5.87790935075541
# [해설] 레드와인 보다는 화이트 와인의 평균적인 품질이 더 좋네용.


# 2) ttest_rel()도 해보자
#test_t2 = stats.ttest_rel(red, white)  # ValueError: unequal length arrays
# 이건 안되는거임. 상관성.


# <조건4> alcohol 칼럼과 다른 칼럼 간의 상관계수 출력
wine_cor = wine.corr()
wine_cor
wine_cor_al = wine_cor['alcohol']
wine_cor_al
"""
fixed acidity          -0.095452
volatile acidity       -0.037640
citric acid            -0.010493
residual sugar         -0.359415
chlorides              -0.256916
free sulfur dioxide    -0.179838
total sulfur dioxide   -0.265740
density                -0.686745
pH                      0.121248
sulphates              -0.003029
alcohol                 1.000000
quality                 0.444319
"""



















