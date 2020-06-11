# -*- coding: utf-8 -*-
"""
1. csv file read
2. csv file write
3. random sampling
"""

import pandas as pd

# 1. csv file read
iris = pd.read_csv("iris.csv")
iris.info()
"""
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 150 entries, 0 to 149
Data columns (total 5 columns):
    """

# 칼럼명 : 특수문자 or 공백 -> _로 문자 변경
iris.columns = iris.columns.str.replace('.', '_')
iris.head()  # 컬럼명의 .이 _로 바뀜
iris.Sepal_Length

# student.csv 칼럼명이 없는 파일 불러오기
st = pd.read_csv('student.csv', header=None)
st
"""
     0     1    2   3
0  101  hong  175  65
1  201   lee  185  85
2  301   kim  173  60
3  401  park  180  70
""" # 기본 칼럼명이 숫자로 들어옴. R의 경우 v1,v2 ...
col_names=['학번', '이름', '키', '몸무게']
st.columns = col_names
st.columns  # Index(['학번', '이름', '키', '몸무게']

# 행 이름 변경
#st.index = 수정값



# 비만도지수(BMI)
# BMI = 몸무게/ 키**2(단, 몸무게kg, 키m)
BMI = [round(st.loc[i,'몸무게']/(st.loc[i,'키']*0.01)**2, 3) for i in range(len(st))]
print(BMI)  # [21.224, 24.836, 20.047, 21.605]


st['bmi'] = BMI
st
"""    학번    이름    키  몸무게     bmi
     0 101    hong   175     65  21.224
    1  201     lee   185     85  24.836
    2  301     kim   173     60  20.047
    3  401    park   180     70  21.605"""
st['bmi'] = st['bmi'].round(2)
st
"""
    학번    이름    키  몸무게    bmi
0   101    hong   175     65  21.22
1   201     lee   185     85  24.84
2   301     kim   173     60  20.05
3   401    park   180     70  21.60
"""

# 2. csv file write(Save)
st.to_csv('student_df.csv', index=None, encoding='utf-8')

st_df = pd.read_csv("student_df.csv")
st_df.info()


# 3. random sampling
wdbc = pd.read_csv('wdbc_data.csv')
wdbc.info()

wdbc_train = wdbc.sample(400)
wdbc_train.shape  # (400, 32)


