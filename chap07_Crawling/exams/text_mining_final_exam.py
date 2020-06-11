'''
TextMining 최종문제  

문) movies.dat 파일의 자료를 이용하여 다음과 같이 단계별로 단어의 빈도수를 구하고,
    단어 구름으로 시각화하시오.
'''

import pandas as pd
import numpy as np

# [단계1] 영화 dataset 가져오기  
name = ['movie_id', 'title', 'genres']
movies = pd.read_csv('C:\\ITWILL\\Work\\4_Python-II\\workspace\\chap07_Crawling\\data/movies.dat', sep='::', header=None, names=name )
print(movies.info())
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 3883 entries, 0 to 3882
Data columns (total 3 columns):
movie_id    3883 non-null int64 -> 각 영화 구분자 
title       3883 non-null object -> 영화 제목 
genres      3883 non-null object -> 영화 장르 : 한 개 이상의 장르(genres) 구성됨  
'''
print(movies.head())
'''
   movie_id                               title                        genres
0         1                    Toy Story (1995)   Animation|Children's|Comedy
1         2                      Jumanji (1995)  Adventure|Children's|Fantasy
2         3             Grumpier Old Men (1995)                Comedy|Romance
3         4            Waiting to Exhale (1995)                  Comedy|Drama
4         5  Father of the Bride Part II (1995)                        Comedy
'''
print('전체 영화수 : ', len(movies)) # 전체 영화수 :  3883


# [단계2] zero 행렬 만들기[행수 : 전체 영화수, 열수 : 중복되지 않은 장르 수]  
# 힌트 : 중복되지 않은 장르 수 구하기
# 각 영화의 장르는 구분자(|)에 의해서 1개 이상의 장르로 구성된 문자열이다.
# 따라서 중복되지 않은 장르 수를 구하기 위해서 구분자(|)를 기준으로 split하여 
# 토큰을 생성한 후 중복을 제거한다.

# 1) unique genres 구하기
temp_gen = []
def UniqueGenres(genres) :
    for g in genres :
        eda = g.split('|')
        
        for words in eda :
            temp_gen.append(words)
            
    return temp_gen

genre_un = set(UniqueGenres(movies.genres))
genre_un
"""
{'Action',
 'Adventure',
 'Animation',
 "Children's",
 'Comedy',
 'Crime',
 'Documentary',
 'Drama',
 'Fantasy',
 'Film-Noir',
 'Horror',
 'Musical',
 'Mystery',
 'Romance',
 'Sci-Fi',
 'Thriller',
 'War',
 'Western'}
"""
len(genre_un)  # 18
genre_name = list(genre_un)


# 2) zero 행렬
import numpy as np

zarr = np.zeros( (len(movies.movie_id), len(genre_name)))
zarr.shape  # (3883, 18)
zarr
"""
array([[0., 0., 0., ..., 0., 0., 0.],
       [0., 0., 0., ..., 0., 0., 0.],
       [0., 0., 0., ..., 0., 0., 0.],
       ...,
       [0., 0., 0., ..., 0., 0., 0.],
       [0., 0., 0., ..., 0., 0., 0.],
       [0., 0., 0., ..., 0., 0., 0.]])
"""




# [단계3] zero 행렬 -> DataFrame 변환(열 제목 = 장르명) 
# 설명 : zero 행렬을 대상으로 열 이름에 장르명을 지정하여 DataFrame을 생성한다.
import pandas as pd

z_df = pd.DataFrame(zarr, columns=genre_name)
z_df.shape  # (3883, 18)
z_df.info()
"""
 #   Column       Non-Null Count  Dtype  
---  ------       --------------  -----  
 0   Drama        3883 non-null   float64
 1   Mystery      3883 non-null   float64
 2   Film-Noir    3883 non-null   float64
 3   War          3883 non-null   float64
 4   Comedy       3883 non-null   float64
 5   Romance      3883 non-null   float64
 6   Thriller     3883 non-null   float64
 7   Children's   3883 non-null   float64
 8   Animation    3883 non-null   float64
 9   Action       3883 non-null   float64
 10  Crime        3883 non-null   float64
 11  Documentary  3883 non-null   float64
 12  Musical      3883 non-null   float64
 13  Sci-Fi       3883 non-null   float64
 14  Fantasy      3883 non-null   float64
 15  Western      3883 non-null   float64
 16  Horror       3883 non-null   float64
 17  Adventure    3883 non-null   float64
"""





# [단계4] 희소행렬(Sparse matrix) 생성 
# 설명 : 각 영화별로 해당 장르에 해당하는 교차 셀에 0 -> 1 교체하여 희소행렬을 만든다.
# 힌트 : index와 내용을 반환하는 enumerate() 함수 이용 
sparse_mat = z_df.copy()
id(z_df)  # 1543080539848
id(sparse_mat)  # 1543082223752


for m, gs in enumerate(movies.genres) :  # 문장 위치와 문장  -> m은 영화 각 하나, g는 장르를 모아놓은 것
    for g in gs.split('|') :  # 문장 -> 단어 분리
        sparse_mat.loc[m, g]  += 1

sparse_mat
"""
      Drama  Mystery  Film-Noir  War  ...  Fantasy  Western  Horror  Adventure
0       0.0      0.0        0.0  0.0  ...      0.0      0.0     0.0        0.0
1       0.0      0.0        0.0  0.0  ...      1.0      0.0     0.0        1.0
2       0.0      0.0        0.0  0.0  ...      0.0      0.0     0.0        0.0
3       1.0      0.0        0.0  0.0  ...      0.0      0.0     0.0        0.0
4       0.0      0.0        0.0  0.0  ...      0.0      0.0     0.0        0.0
    ...      ...        ...  ...  ...      ...      ...     ...        ...
3878    0.0      0.0        0.0  0.0  ...      0.0      0.0     0.0        0.0
3879    1.0      0.0        0.0  0.0  ...      0.0      0.0     0.0        0.0
3880    1.0      0.0        0.0  0.0  ...      0.0      0.0     0.0        0.0
3881    1.0      0.0        0.0  0.0  ...      0.0      0.0     0.0        0.0
3882    1.0      0.0        0.0  0.0  ...      0.0      0.0     0.0        0.0

[3883 rows x 18 columns]
"""




# [단계5] 단어문서 행렬(TDM) 만들기 
# 설명 : 희소행렬(Sparse matrix)에 전치행렬을 적용하여 장르명과 영화 축을 교체한다. 
# 힌트 : 전치행렬 -> 형식) 데이터프레임객체.T 
sparse_tdm = sparse_mat.T
sparse_tdm
"""
             0     1     2     3     4     ...  3878  3879  3880  3881  3882
Drama         0.0   0.0   0.0   1.0   0.0  ...   0.0   1.0   1.0   1.0   1.0
Mystery       0.0   0.0   0.0   0.0   0.0  ...   0.0   0.0   0.0   0.0   0.0
Film-Noir     0.0   0.0   0.0   0.0   0.0  ...   0.0   0.0   0.0   0.0   0.0
War           0.0   0.0   0.0   0.0   0.0  ...   0.0   0.0   0.0   0.0   0.0
Comedy        1.0   0.0   1.0   1.0   1.0  ...   1.0   0.0   0.0   0.0   0.0
Romance       0.0   0.0   1.0   0.0   0.0  ...   0.0   0.0   0.0   0.0   0.0
Thriller      0.0   0.0   0.0   0.0   0.0  ...   0.0   0.0   0.0   0.0   1.0
Children's    1.0   1.0   0.0   0.0   0.0  ...   0.0   0.0   0.0   0.0   0.0
Animation     1.0   0.0   0.0   0.0   0.0  ...   0.0   0.0   0.0   0.0   0.0
Action        0.0   0.0   0.0   0.0   0.0  ...   0.0   0.0   0.0   0.0   0.0
Crime         0.0   0.0   0.0   0.0   0.0  ...   0.0   0.0   0.0   0.0   0.0
Documentary   0.0   0.0   0.0   0.0   0.0  ...   0.0   0.0   0.0   0.0   0.0
Musical       0.0   0.0   0.0   0.0   0.0  ...   0.0   0.0   0.0   0.0   0.0
Sci-Fi        0.0   0.0   0.0   0.0   0.0  ...   0.0   0.0   0.0   0.0   0.0
Fantasy       0.0   1.0   0.0   0.0   0.0  ...   0.0   0.0   0.0   0.0   0.0
Western       0.0   0.0   0.0   0.0   0.0  ...   0.0   0.0   0.0   0.0   0.0
Horror        0.0   0.0   0.0   0.0   0.0  ...   0.0   0.0   0.0   0.0   0.0
Adventure     0.0   1.0   0.0   0.0   0.0  ...   0.0   0.0   0.0   0.0   0.0

[18 rows x 3883 columns]
"""





# [단계6] 장르 빈도수(word count)
# 설명 : 단어문서 행렬(TDM)를 대상으로 행 단위 합계를 계산하여 장르별 출현빈도수를 계산한다. 
# 힌트 : dict() 이용하여 장르명과 빈도수를 key : value 형식으로 만든다.
movie_count = sparse_tdm.sum(axis=1)
movie_count

count_dict = dict(movie_count)
count_dict
"""
{'Drama': 1603.0,
 'Mystery': 106.0,
 'Film-Noir': 44.0,
 'War': 143.0,
 'Comedy': 1200.0,
 'Romance': 471.0,
 'Thriller': 492.0,
 "Children's": 251.0,
 'Animation': 105.0,
 'Action': 503.0,
 'Crime': 211.0,
 'Documentary': 127.0,
 'Musical': 114.0,
 'Sci-Fi': 276.0,
 'Fantasy': 68.0,
 'Western': 68.0,
 'Horror': 343.0,
 'Adventure': 283.0}
"""





# [단계7] 단어 구름 시각화
# 설명 : 장르 빈도수를 Counter 객체를 생성하고, WordCloud 클래스를 이용하여 단어 구름으로 시각화한다.
from wordcloud import WordCloud
help(WordCloud)

wc = WordCloud(font_path='C:/Windows/Fonts/malgun.ttf', width=800, height=600, max_words=100,
               max_font_size=200, background_color='white')

wc_result = wc.generate_from_frequencies(count_dict)

import matplotlib.pyplot as plt
plt.figure(figsize=(12,8))
plt.imshow(wc_result)
plt.axis('off')
plt.show()





















