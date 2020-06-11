'''  
문4) tips.csv 파일을 읽어와서 다음과 같이 처리하시오.
   조건1> 파일 정보 보기 
   조건2> header를 포함한 앞부분 5개 관측치 보기 
   조건3> header를 포함한 뒷부분 5개 관측치 보기 
   조건4> 숫자 칼럼 대상 요약통계량 보기 
   조건5> 흡연자(smoker) 유무 빈도수 계산  
   조건6> 요일(day) 칼럼의 유일한 값 출력 
'''

import pandas as pd

tips = pd.read_csv('D:/ITWILL/4_Python_ML/data/tips.csv')

# 조건1> 파일 정보 보기
tips.info()
'''
RangeIndex: 244 entries, 0 to 243
Data columns (total 7 columns):
 0   total_bill  244 non-null    float64
 1   tip         244 non-null    float64
 2   sex         244 non-null    object 
 3   smoker      244 non-null    object 
 4   day         244 non-null    object 
 5   time        244 non-null    object 
 6   size        244 non-null    int64  
'''

# 조건2> header를 포함한 앞부분 5개 관측치 보기 
tips.head()

# 조건3> header를 포함한 뒷부분 5개 관측치 보기 
tips.tail()

# 조건4> 숫자 칼럼 대상 요약통계량 보기
tips[['total_bill','tip','size']].describe()

# 조건5> 흡연자(smoker) 유무 빈도수 계산
tips.smoker.value_counts()
'''
No     151
Yes     93
'''

# 조건6> 요일(day) 칼럼의 유일한 값 출력
tips['day'].unique()
# ['Sun', 'Sat', 'Thur', 'Fri']