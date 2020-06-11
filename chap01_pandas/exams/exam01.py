''' 
step02 관련문제 
문1) score.csv 파일을 읽어와서 다음과 같이 처리하시오.
   조건1> tv 칼럼이 0인 관측치 2개 삭제 (for, if문 이용)
   조건2> score, academy 칼럼만 추출하여 DataFrame 생성
   조건3> score, academy 칼럼의 평균 계산 
   - <<출력 결과 >> 참고    
   
<<출력 결과 >>
   score  academy
1     75        1
2     77        1
3     83        2
4     65        0
5     80        3
6     83        3
7     70        1
9     79        2
score      76.500
academy     1.625   
'''

import pandas as pd

score = pd.read_csv("C:\\ITWILL\\Work\\4_Python-II\\data\\score.csv")
print(score)
score.info()

# 조건1]
score2 = score[score.tv != 0]
print(score2)

# 조건2]
score_df = pd.DataFrame(score[['score', 'academy']])
print(score_df)

# 조건3]
avg_score = score.score.mean()
print(avg_score)
avg_academy = score.academy.mean()
print(avg_academy)

# or
score_df.mean(axis=0)

# 결과
print(score_df,'\n', "score = ", avg_score, '\n', "academy =", avg_academy)
"""
   score  academy
0     90        2
1     75        1
2     77        1
3     83        2
4     65        0
5     80        3
6     83        3
7     70        1
8     87        4
9     79        2 
 score =  78.9 
 academy = 1.9
 """