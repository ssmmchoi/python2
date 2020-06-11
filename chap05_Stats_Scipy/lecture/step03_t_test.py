# -*- coding: utf-8 -*-
"""
집단 간 평균차이 검정(t-test)
 1. 한 집단 평균차이 검정
 2. 두 집단 평균차이 검정
 3. 대응 두 집단 평균차이 검정
"""
from scipy import stats  # t 검정
import numpy as np  # 숫자 연산
import pandas as pd  # file read

# 1. 한 집단 평균차이 검정  stats.ttest_1samp()

# 대한민국 남자 평균 키(모평균) : 175.5(라고 치자)
# 모집단 -> 표본 추출(30명)
# H0 : 추출한 30명 표본의 평균은 모평균(175.5)과 차이가 없다.

sample_data = np.random.uniform(172, 180, 300)  # 균등분포 uniform
sample_data

# 기술통계
sample_data.mean()  # 175.94824207511147

one_group_test = stats.ttest_1samp(sample_data, 175.5)
one_group_test  # Ttest_1sampResult(statistic=3.2901619136217577, pvalue=0.0011210751838386566)
print('statistic = %.5f, pvalue = %.5f'%(one_group_test))
# statistic = 3.29016, pvalue = 0.00112
one_group_test['pvalue']

if one_group_test.pvalue >= 0.05 :  # 왜인지 one_group_test['pvalue']는 TypeError : tuple indices must be integers or slices, not str
    print('귀무가설 채택 : 추출한 표본(30명)의 평균 키는 모집단의 평균키와 차이가 없다.')
else :
    print('귀무가설 기각 : 추출한 표본(30명)의 평균 키는 모집단의 평균키와 차이가 있다.')
## 귀무가설 기각 : 추출한 표본(30명)의 평균 키는 모집단의 평균키와 차이가 있다.
    

# 2. 두 집단 평균차이 검정  stats.ttest_ind()
female_score = np.random.uniform(50, 100, size = 30)
male_score = np.random.uniform(45, 95, size = 30)
two_sample = stats.ttest_ind(female_score, male_score)

two_sample  # Ttest_indResult(statistic=0.28217092889941575, pvalue=0.778816906116595)

if two_sample.pvalue >= 0.05:
    print('H0채택 : 남성의 점수와 여성의 점수 평균에는 차이가 없다.')
    print('mean score of female =', female_score.mean())
    print('mean score of male =', male_score.mean())
else : 
    print('H0기각 : 남성의 점수와 여성의 점수 평균에는 차이가 있다.')
    print('mean score of female =', female_score.mean())
    print('mean score of male =', male_score.mean())

## H0채택 : 남성의 점수와 여성의 점수 평균에는 차이가 없다.
## mean score of female = 72.4342208012402
## mean score of male = 71.36267099314858


# csv file load
two_sample = pd.read_csv('C:\\ITWILL\\Work\\4_Python-II\\data\\two_sample.csv')
two_sample.info()
"""
 #   Column  Non-Null Count  Dtype  
---  ------  --------------  -----  
 0   no      240 non-null    int64  
 1   gender  240 non-null    int64  
 2   method  240 non-null    int64  
 3   score   180 non-null    float64    >>> 60개의 결측치
 4   survey  240 non-null    int64  
 """

sample_data = two_sample[['method', 'score']]
sample_data.head()
"""
   method  score  method는 집단변수
0       1    5.1
1       1    5.2
2       1    4.7
3       1    NaN
4       1    5.0   """
sample_data['method'].value_counts()
"""2    120
1    120"""

# 교육방법에 따른 subset
method1 = sample_data[sample_data.method == 1]
method2 = sample_data[sample_data.method == 2]
method1.method.value_counts()  # 1    120
method2.method.value_counts()  # 2    120

score1 = method1.score
score2 = method2.score
two_sample = stats.ttest_ind(score1, score2)
"""
C:\Users\user\anaconda3\lib\site-packages\scipy\stats\_distn_infrastructure.py:903: RuntimeWarning: invalid value encountered in greater
  return (a < x) & (x < b)
C:\Users\user\anaconda3\lib\site-packages\scipy\stats\_distn_infrastructure.py:903: RuntimeWarning: invalid value encountered in less
  return (a < x) & (x < b)
C:\Users\user\anaconda3\lib\site-packages\scipy\stats\_distn_infrastructure.py:1912: RuntimeWarning: invalid value encountered in less_equal
  cond2 = cond0 & (x <= _a)
"""
two_sample  # Ttest_indResult(statistic=nan, pvalue=nan)

# 결측치 때문에 오류가 남!! NaN을 제거하자.
# NaN 평균 대체
score1 = score1.fillna(score1.mean()) 
score2 = score2.fillna(score2.mean())
test1 = pd.isna(score1)
test1.value_counts()  # False    120
test2 = pd.isna(score2)
test2.value_counts()  # False    120


two_sample = stats.ttest_ind(score1, score2)
two_sample
print('statistic = %.5f, pvalue = %.5f' %(two_sample))
## statistic = -0.94686, pvalue = 0.34467
# H0채택역 : 두 집단의 평균에는 차이가 없다. 


# 3. 대응 두 집단 평균차이 검정  : 복용전 65 -> 복용후 : 60 변환
before = np.random.randint(65, size=30) * 0.5  # 그냥 실수로 만들기 위해 0.5 곱한것.
after = np.random.randint(60, size=30) * 0.5

before
after

paired_test = stats.ttest_rel(before, after)
paired_test  # Ttest_relResult(statistic=-0.92490930752082, pvalue=0.36264600348155207)
# [해석] pvalue >= 0.05이므로 두 집단간(복용 전, 후) 평균 차이 없다.







