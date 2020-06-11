# -*- coding: utf-8 -*-
"""
DataFrame 모양 변경 : reshape
"""

import pandas as pd

buy = pd.read_csv("C:\\ITWILL\\Work\\4_Python-II\\data\\buy_data.csv")
buy.info()

buy.shape  # (22, 3)  # 2차원

# 1. row -> column(R wide -> long)

buy_long = buy.stack()
buy_long.shape  # (66,)  ## 22x3 1차원 벡터로
buy_long
"""
0   Date           20150101
    Customer_ID           1
    Buy                   3
1   Date           20150101
    Customer_ID           2
  
20  Customer_ID           1
    Buy                   9
21  Date           20150107
    Customer_ID           5
    Buy                   7
Length: 66, dtype: int64
"""
buy_long[0]
"""
Date           20150101
Customer_ID           1
Buy                   3
dtype: int64
"""

# 2. column -> row (R long->wide)
buy_wide = buy_long.unstack()  # 이 코드는 stack을 실행한 객체에 대해서만 실행.
buy_wide.info()


# 3. 전치행렬 : t() -> .T
wide_t = buy_wide.T
wide_t.shape  # (3, 22) 행을 열로, 열은 행으로
print(wide_t)


# 4. 중복 행 제거
buy.duplicated()
buy_df = buy.drop_duplicates()
buy_df.shape  # (20, 3)


























