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

tips = pd.read_csv('C:/ITWILL/Work/4_Python-II/data/tips.csv')
print(tips)

# 조건1> 파일 정보 보기 
tips.info()
"""
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 244 entries, 0 to 243
Data columns (total 7 columns):
    """
colname = tips.columns
print(colname)  # ['total_bill', 'tip', 'sex', 'smoker', 'day', 'time', 'size']

# 조건2> header를 포함한 앞부분 5개 관측치 보기
tips.head()
"""
   total_bill   tip     sex smoker  day    time  size
0       16.99  1.01  Female     No  Sun  Dinner     2
1       10.34  1.66    Male     No  Sun  Dinner     3
2       21.01  3.50    Male     No  Sun  Dinner     3
3       23.68  3.31    Male     No  Sun  Dinner     2
4       24.59  3.61  Female     No  Sun  Dinner     4
"""

# 조건3> header를 포함한 뒷부분 5개 관측치 보기 
tips.tail()
"""
     total_bill   tip     sex smoker   day    time  size
239       29.03  5.92    Male     No   Sat  Dinner     3
240       27.18  2.00  Female    Yes   Sat  Dinner     2
241       22.67  2.00    Male    Yes   Sat  Dinner     2
242       17.82  1.75    Male     No   Sat  Dinner     2
243       18.78  3.00  Female     No  Thur  Dinner     2
"""

# 조건4> 숫자 칼럼 대상 요약통계량 보기?????????????
tips.info()  # 0,1,6이 숫자 칼럼
tips.iloc[:,[0,1,6]].describe()
# or
int_tips = tips.iloc[:, [0,1,6]]
int_tips.describe()
"""
       total_bill         tip        size
count  244.000000  244.000000  244.000000
mean    19.785943    2.998279    2.569672
std      8.902412    1.383638    0.951100
min      3.070000    1.000000    1.000000
25%     13.347500    2.000000    2.000000
50%     17.795000    2.900000    2.000000
75%     24.127500    3.562500    3.000000
max     50.810000   10.000000    6.000000
"""


# 조건5> 흡연자(smoker) 유무 빈도수 계산
smoke = tips.smoker
smoke.value_counts()
#or
tips.smoker.value_counts()
"""
No     151
Yes     93
Name: smoker, dtype: int64
"""


# 조건6> 요일(day) 칼럼의 유일한 값 출력 
dayofweek = tips.day
dayofweek.unique()
# or
tips.day.unique()
# array(['Sun', 'Sat', 'Thur', 'Fri'], dtype=object)













