# -*- coding: utf-8 -*-
"""
scipy 패키지의 확률분포 검정
 1. 정규분포 검정 : 연속변수의 확률분포
   - 연속확률분포 : 정규분포, 균등분포, 카이제곱, T/Z/F 분포
 2. 이항분포 검정 : 2가지 범주의 확률분포
   - 이산확률분포 : 베르누이분포, 이항분포, 포아송분포
"""

from scipy import stats  # 확률분포 검정
import numpy as np
import matplotlib.pyplot as plt  # 히스토그램


# 1. 정규분포 검정 : 평균을 중심으로 좌우대칭인가?

# 1) 정규분포객체 생성
mu = 0; std = 1  # 표준정규분포
std_norm = stats.norm(mu, std)  # 정규분포객체 생성
std_norm  # object info :  <scipy.stats._distn_infrastructure.rv_frozen at 0x1b09e1d24c8>

# 2) 정규분포확률변수
N = 1000  # 시행 횟수
norm_data = std_norm.rvs(N)  # 시뮬레이션 : 모집단으로부터 1000개의 난수가 생성됨.
norm_data
len(norm_data)  # 1000
norm_data.mean()  # -0.0192807358149145
norm_data.std()  # 0.9880265968215409
type(norm_data)  # numpy.ndarray

# 3) 히스토그램
plt.hist(norm_data)
plt.show()

import seaborn as sns
sns.distplot(norm_data)
import pandas as pd
import numpy as np

# 4) 정규성 검정
# 귀무가설(H0) : 정규분포와 차이가 없다.
# 대립 가설 : 정규분포와 차이가 있다. 정규분포가 아니다.
stats.shapiro(norm_data)  
# (0.9989621043205261, 0.8529985547065735)
#      검정통계량            p-value
test_stats, pvalue = stats.shapiro(norm_data)
print('검정통계량 : %.5f'%(test_stats), '유의확률 p-value : %.5f'%(pvalue), sep='\n')
"""
검정통계량 : 0.99896  -> -1.96 ~ +1.96이면 채택역
유의확률 p-value : 0.85300  -> >=0.05이면 채택역.

[결론] : 해당 데이터는 정규분포와 차이가 없다. 정규분포이다.
"""


#  2. 이항분포 검정 : 2가지(성공/실패) 범주의 확률분포 + 가설검정
'''
- 베르누이 분포 : 이항변수(성공 or 실패)에서 성공(1)이 나올 확률분포(모수:성공확률)
- 이항분포 : 베르누이 분포에 시행횟수(N)을 적용한 확률분포(모수 : P(성공확률), N)

ex) P = 게임에 이길 확률(40%), N = 시행횟수(100번) -> 성공횟수(?)  
'''
N = 100  # 시행횟수
P = 0.4  # 성공확률

# 1) 베르누이 확률분포
x = stats.bernoulli(P).rvs(N)
x  # 0(실패), 1(성공)
"""
array([0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0,
       1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1,
       0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1,
       1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0,
       0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1])
"""
x.size()

pd.value_counts(x)
'''0    62
1    38'''
np.count_nonzero(x)  # 38
x.isna()












































