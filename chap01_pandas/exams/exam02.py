'''
step02 관련문제
문2) wdbc_data.csv 파일을 읽어와서 단계별로 x, y 변수를 생성하시오.
     단계 1 : 파일 가져오기, 정보 확인 
     단계 2 : y변수 : diagnosis 
         x변수 : id 칼럼 제외  나머지 30개 칼럼
'''
import pandas as pd
# 단계 1 : 파일 가져오기, 정보 확인 
wdbc_data = pd.read_csv("C:\\ITWILL\\Work\\4_Python-II\\data\\wdbc_data.csv")
wdbc_data.info()
""" 암 진단 결과
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 569 entries, 0 to 568
Data columns (total 32 columns):  """


# 단계 2 : y변수, x변수 선택
y_wdbc = wdbc_data['diagnosis']
print(y_wdbc)

cols = list(wdbc_data.columns)
print(cols)
x_cols = cols[2:]
print(x_cols)

x_wdbc = wdbc_data[x_cols]
print(x_wdbc)
x_wdbc.info()  # 아니 왜 29개냐고..
