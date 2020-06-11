# -*- coding: utf-8 -*-
"""
시계열 분석(time series analysis) : x축 = 시간 축, y축 = 시간에 따른 변화 (ex :주식)
 1. 시계열 자료 생성
 2. 날짜 형식을 국내 형태로 수정(다국어)
 3. 시계열 시각화
 4. 이동평균 기능 : 5일, 10일, 20일 단위 평균 -> 추세선 평활(smoothing)
"""
from datetime import datetime  # 날짜형식 수정
import pandas as pd  # csv file read
import matplotlib.pyplot as plt  # 시계열 시각화
import numpy as np  # 수치 자료 생성


# 1. 시계열 자료 생성
time_data = pd.date_range("2017-03-01", "2020-03-30")
time_data = pd.date_range("2017-03-01", "2020-03-30")
time_data
"""
DatetimeIndex(['2017-03-01', '2017-03-02', '2017-03-03', '2017-03-04',
               '2017-03-05', '2017-03-06', '2017-03-07', '2017-03-08',
               '2017-03-09', '2017-03-10',
               ...
               '2020-03-21', '2020-03-22', '2020-03-23', '2020-03-24',
               '2020-03-25', '2020-03-26', '2020-03-27', '2020-03-28',
               '2020-03-29', '2020-03-30'],
              dtype='datetime64[ns]', length=1126, freq='D')

>> length=1126, freq='D' 일 단위로 생성됨
"""

time_data2 = pd.date_range("2017-03-01", "2020-03-30", freq='M')
time_data3 = pd.date_range("2017-03-01", "2020-03-30", freq='Y')
time_data2  # 월 단위
"""
DatetimeIndex(['2017-03-31', '2017-04-30', '2017-05-31', '2017-06-30',
               '2017-07-31', '2017-08-31', '2017-09-30', '2017-10-31',
               '2017-11-30', '2017-12-31', '2018-01-31', '2018-02-28',
               '2018-03-31', '2018-04-30', '2018-05-31', '2018-06-30',
               '2018-07-31', '2018-08-31', '2018-09-30', '2018-10-31',
               '2018-11-30', '2018-12-31', '2019-01-31', '2019-02-28',
               '2019-03-31', '2019-04-30', '2019-05-31', '2019-06-30',
               '2019-07-31', '2019-08-31', '2019-09-30', '2019-10-31',
               '2019-11-30', '2019-12-31', '2020-01-31', '2020-02-29'],
              dtype='datetime64[ns]', freq='M')
"""
len(time_data2)  # 36


# 월 단위 매출현황 : x
x = pd.Series(np.random.uniform(10, 100,36))
 
df = pd.DataFrame({'date' : time_data2, 'price' : x})
df

plt.plot(df.date, df.price, 'g--')  # (x, y)
plt.show()


# 2. 날짜형식 수정(다국어)

cospi = pd.read_csv('C:\\ITWILL\\Work\\4_Python-II\\data\\cospi.csv')
cospi.info()

cospi.head()
"""
        Date     Open     High      Low    Close  Volume
0  26-Feb-16  1180000  1187000  1172000  1172000  176906
1  25-Feb-16  1172000  1187000  1172000  1179000  128321
2  24-Feb-16  1178000  1179000  1161000  1172000  140407
3  23-Feb-16  1179000  1189000  1173000  1181000  147578
4  22-Feb-16  1190000  1192000  1166000  1175000  174075
"""

date = cospi.Date
len(date)  # 247


# list + for  : 26-Feb-16 -> 2016-02-16
kdate = [datetime.strptime(d, '%d-%b-%y') for d in date]
kdate = [datetime.strptime(d, '%d-%b-%y') for d in date]
kdate
"""
[datetime.datetime(2016, 2, 26, 0, 0),
 datetime.datetime(2016, 2, 25, 0, 0),
 datetime.datetime(2016, 2, 24, 0, 0),
 ...
"""

cospi.Date = kdate
cospi.info()  # Date column이 object -> datetime64[ns]으로 변경됨
cospi.head()
"""
        Date     Open     High      Low    Close  Volume
0 2016-02-26  1180000  1187000  1172000  1172000  176906
1 2016-02-25  1172000  1187000  1172000  1179000  128321
2 2016-02-24  1178000  1179000  1161000  1172000  140407
"""
cospi.tail()  # 2015-03-02 ~ 2016-02-26 까지의 데이터가 존재함
"""
          Date     Open     High      Low    Close  Volume
242 2015-03-06  1414000  1449000  1406000  1442000  234312
243 2015-03-05  1439000  1443000  1417000  1422000  191913
244 2015-03-04  1411000  1440000  1410000  1437000  231146
245 2015-03-03  1435000  1437000  1406000  1418000  251018
246 2015-03-02  1375000  1423000  1367000  1423000  425208
"""



# 3. 시계열 시각화 (Date : x축, 나버지 : y축)
cospi.index  # RangeIndex(start=0, stop=247, step=1)

# 칼럼 -> index 적용
new_cospi = cospi.set_index('Date')
new_cospi=cospi.set_index('Date')
new_cospi.info()
"""
 #   Column  Non-Null Count  Dtype
---  ------  --------------  -----
 0   Open    247 non-null    int64
 1   High    247 non-null    int64
 2   Low     247 non-null    int64
 3   Close   247 non-null    int64
 4   Volume  247 non-null    int64
"""
new_cospi.index
"""
DatetimeIndex(['2016-02-26', '2016-02-25', '2016-02-24', '2016-02-23',
               '2016-02-22', '2016-02-19', '2016-02-18', '2016-02-17',
               '2016-02-16', '2016-02-15',
               ...
               '2015-03-13', '2015-03-12', '2015-03-11', '2015-03-10',
               '2015-03-09', '2015-03-06', '2015-03-05', '2015-03-04',
               '2015-03-03', '2015-03-02'],
"""

# subset
new_cospi['2016']  # 2016년도 1년치 정보
new_cospi['2015']  # 2015년도 1년치 정보 = 210개
new_cospi['2015-05':'2015-03']  # 2015년도의 3,4,5 월 정보 = 62개

new_cospi_hl = new_cospi[['High', 'Low']]
new_cospi_hl.index
"""DatetimeIndex(['2016-02-26', '2016-02-25', '2016-02-24', '2016-02-23',
               '2016-02-22', '2016-02-19', '2016-02-18', '2016-02-17',
               '2016-02-16', '2016-02-15',
               ...
               '2015-03-13', '2015-03-12', '2015-03-11', '2015-03-10',
               '2015-03-09', '2015-03-06', '2015-03-05', '2015-03-04',
               '2015-03-03', '2015-03-02'],    :::::::::::::Date
"""
new_cospi_hl.columns  # Index(['High', 'Low'], dtype='object')

# 2015기준
new_cospi_hl['2015'].plot(title='2015 tear : High vs Low')
plt.show()


# 2016년 2월 기준
new_cospi_hl['2016-02'].plot(title='Feb 2016: High vs Low')
plt.show()



#  4. 이동평균 기능 : 5일, 10일, 20일 단위 평균 -> 추세선 평활(smoothing)

# 1) 5일 단위 이동평균 : 5일 단위 평균 -> 마지막 5일째 날에 평균을 이동
roll_mean5 = pd.Series.rolling(new_cospi_hl, window=5, center=False).mean()
help(pd.Series.rolling)
roll_mean5
"""
                 High        Low
Date                            
2016-02-26        NaN        NaN
2016-02-25        NaN        NaN
2016-02-24        NaN        NaN
2016-02-23        NaN        NaN
2016-02-22  1186800.0  1168800.0
              ...        ...
2015-03-06  1456800.0  1422200.0
2015-03-05  1450800.0  1416200.0
2015-03-04  1443000.0  1414600.0
2015-03-03  1441800.0  1411800.0
2015-03-02  1438400.0  1401200.0
"""
roll_mean5.head()
roll_mean5.tail()

# 2) 10일 단위 이동평균 : 10일 단위 평균 -> 마지막 10일째 날에 평균을 이동
roll_mean10 = pd.Series.rolling(new_cospi_hl, window=10, center=False).mean()
roll_mean10
roll_mean10.head(20)
roll_mean10.tail(20)


# 3) 20일 단위 이동평균 : 20일 단위 평균 -> 마지막 20일째 날에 평균을 이동
roll_mean20 = pd.Series.rolling(new_cospi_hl, window=20, center=False).mean()
roll_mean20
roll_mean20.head(20)


# 4) rolling mean 시각화
roll_mean5 = pd.Series.rolling(new_cospi_hl.High, window=5, center=False).mean()
roll_mean10 = pd.Series.rolling(new_cospi_hl.High, window=10, center=False).mean()
roll_mean20 = pd.Series.rolling(new_cospi_hl.High, window=20, center=False).mean()

new_cospi_hl.High.plot(color = 'b', label = 'High column')  # 원본
roll_mean5.plot(color='red', label='rolling mean 5 days')  # Pandas 멤버는 원래 객체 뒤에 plot 호출 가능
roll_mean10.plot(color='g', label='rolling mean 10 days')
roll_mean20.plot(color='orange', label='rolling mean 20 days')
plt.legend(loc='best')
plt.show()

























