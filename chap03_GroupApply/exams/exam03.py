import pandas as pd

election = pd.read_csv('C:\\ITWILL\\Work\\4_Python-II\\data\\election_2012.csv', encoding='ms949')
print(election.info())
'''
cand_id : 대선 후보자 id
cand_nm : 대선 후보자 이름
contbr_nm : 후원자 이름 
contbr_occupation : 후원자 직업군 
contb_receipt_amt : 후원금 
'''

# DF 객체 생성 
name = ['cand_nm', 'contbr_occupation', 'contb_receipt_amt'] 
# subset 생성 
election_df = pd.DataFrame(election, columns= name)
print(election_df.info())
print(election_df.head())
print(election_df.tail())


# 중복되지 않은 대선 후보자 추출 
unique_name = election_df['cand_nm'].unique()
unique_name2 = election['cand_nm'].unique()  # 둘이 같다.
print(len(unique_name))  # 13
print(unique_name) 

# 중복되지 않은 후원자 직업군 추출 
unique_occ = election_df['contbr_occupation'].unique()
print(len(unique_occ))  # 45074
print(unique_occ)

#############################################
#  Obama, Barack vs Romney, Mitt 후보자 분석 
#############################################

# 1. 두 후보자 관측치만 추출 : isin()
two_cand_nm = election_df[election_df.cand_nm.isin(['Obama, Barack', 'Romney, Mitt'])]
two_cand_nm = election_df[election_df.cand_nm.isin(['Obama, Barack', 'Romney, Mitt'])]
print(two_cand_nm.head())  # Romey's
print(two_cand_nm.tail())  # Obama's
print(len(two_cand_nm)) # 700975/1001731
'''
문1) two_cand_nm 변수를 대상으로 피벗테이블 생성하기 
    <조건1> 교차셀 칼럼 : 후원금, 열 칼럼 : 대선 후보자,
             행 칼럼 : 후원자 직업군, 적용함수 : sum
    <조건2> 피벗테이블 앞부분 5줄 확인   
문2) 피벗테이블 대상 필터링 : 2백만달러 이상 후원금 대상     
'''

#  문1) <조건1> 교차셀 칼럼 : 후원금, 열 칼럼 : 대선 후보자,
#            행 칼럼 : 후원자 직업군, 적용함수 : sum
ptable = pd.pivot_table(two_cand_nm, values='contb_receipt_amt', index='contbr_occupation',
                        columns='cand_nm', aggfunc='sum', fill_value=0)
ptable = pd.pivot_table(two_cand_nm, values='contb_receipt_amt', index='contbr_occupation',
                        columns='cand_nm', aggfunc='sum', fill_value=0)

# 문2) <조건2> 피벗테이블 앞부분 5줄 확인 
ptable.head()
"""
cand_nm                              Obama, Barack  Romney, Mitt
contbr_occupation                                               
   MIXED-MEDIA ARTIST / STORYTELLER          100.0           0.0
 AREA VICE PRESIDENT                         250.0           0.0
 RESEARCH ASSOCIATE                          100.0           0.0
 TEACHER                                     500.0           0.0
 THERAPIST                                  3900.0           0.0
"""
ptable.shape  # (33605, 2)



# 문2) 피벗테이블 대상 필터링 : 2백만달러 이상 후원금 대상  
ptable_200 = ptable[ptable.sum(axis=1) >= 2000000]
ptable_200 = ptable[ptable.sum(axis=1) >= 2000000]
ptable_200
"""
cand_nm                                 Obama, Barack  Romney, Mitt
contbr_occupation                                                  
ATTORNEY                                  11126932.97    5302578.82
CEO                                        2069784.79     353310.92
CONSULTANT                                 2459812.71    1404576.94
EXECUTIVE                                  1355161.05    2230653.79
HOMEMAKER                                  4243394.30    8037250.86
INFORMATION REQUESTED                      4849801.96          0.00
INFORMATION REQUESTED PER BEST EFFORTS           0.00   11173374.84
INVESTOR                                    884133.00    1494725.12
LAWYER                                     3159391.87       7705.20
PHYSICIAN                                  3732387.44    1332996.34
PRESIDENT                                  1878009.95    2403439.77
PROFESSOR                                  2163571.08     160362.12
RETIRED                                   25270507.23   11266949.23
"""

## 추가 문) 두 후보자에게 모두 200만달러 이상의 후원금을 지불한 직업군 필터링
import numpy as np
ptable_200_each = ptable[np.logical_and(ptable['Obama, Barack']>=2000000, ptable['Romney, Mitt']>=2000000)]
ptable_200_each.shape  # (3, 2)
ptable_200_each
"""
cand_nm            Obama, Barack  Romney, Mitt
contbr_occupation                             
ATTORNEY             11126932.97    5302578.82
HOMEMAKER             4243394.30    8037250.86
RETIRED              25270507.23   11266949.23
"""

## 추가 문2) 두 후보자 중 한 명에게 200만 달러 달러 이상의 후원금을 지불한 직업군 필터링
ptable_200_or = ptable[np.logical_or(ptable['Obama, Barack']>=2000000, ptable['Romney, Mitt']>=2000000)]
ptable_200_or
ptable_200_or.shape  # (12, 2)
