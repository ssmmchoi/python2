# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""
1. csv file read -> 파일명 temp_spam_data2.csv
2. text, target -> 전처리
3. max features
4. Sparse matrix
5. train / test split
6. binary file save
"""


from sklearn.feature_extraction.text import TfidfVectorizer  # 공백을 기준으로 strip 및 전처리 기능이 내장되어 있음.
import pandas as pd

# 1. csv file read
spam_data = pd.read_csv("./data/temp_spam_data2.csv", encoding='utf-8', header=None)
spam_data
"""
         0                                                  1
0      ham  Go until jurong point, crazy.. Available only ...
1      ham                      Ok lar... Joking wif u oni...
2     spam  Free entry in 2 a wkly comp to win FA Cup fina...
3      ham  U dun say so early hor... U c already then say...
4      ham  Nah I don't think he goes to usf, he lives aro...
   ...                                                ...
5569  spam  This is the 2nd time we have tried 2 contact u...
5570   ham                Will  b going to esplanade fr home?
5571   ham  Pity, * was in mood for that. So...any other s...
5572   ham  The guy did some bitching but I acted like i'd...
5573   ham                         Rofl. Its true to its name

[5574 rows x 2 columns]
"""
spam_data.info()
'''
 #   Column  Non-Null Count  Dtype 
---  ------  --------------  ----- 
 0   0       5574 non-null   object
 1   1       5574 non-null   object
'''


target = spam_data[0]
target  # y변수
texts = spam_data[1]
texts  # -> sparse matrix -> x 변수

# 2. texts, target -> 전처리
# 1) target 전처리 -> dummy 변수
target = [1 if t=='spam' else 0 for t in target]
target 
type(target)  # list

# 2) texts 전처리  -> TfidVectorizer()에 내장
# import string # text 전처리 

# def text_prepro(texts):
#     # Lower case
#     texts = [x.lower() for x in texts]
#     # Remove punctuation
#     texts = [''.join(c for c in x if c not in string.punctuation) for x in texts]
#     # Remove numbers
#     texts = [''.join(c for c in x if c not in string.digits) for x in texts]
#     # Trim extra whitespace
#     texts = [' '.join(x.split()) for x in texts]
#     return texts


# texts_re = text_prepro(texts)
# texts_re


# 3. matrix features
"""
사용할 x 변수의 개수(열의 차수)
"""
tfidf_fit = TfidfVectorizer().fit(texts)  # 문장->단어 생성
vocs = tfidf_fit.vocabulary_
vocs  # 16개의 단어와 그에 해당하는 고유숫자  --> 피쳐 최댓값 16까지 사용가능
len(vocs)  # 8722

#max_features = len(vocs)
max_features = 4000  # 전체 8722개 단어 중 가중치가 높은 4000개 단어를 이용하겠다
max_features  #  4000  -> Sparse matrix = [5574 x 4000]



# 4. Sparse matrix
sparse_mat = TfidfVectorizer(max_features=max_features, stop_words='english').fit_transform(texts)
sparse_mat
"""
<5574x4000!!!!!! sparse matrix of type '<class 'numpy.float64'>'
	with 39080 stored elements in Compressed Sparse Row format>
"""
print(sparse_mat)
"""
  (0, 3827)     0.22589839945445928
  (0, 1640)     0.18954016110208324
  (0, 919)      0.3415462652078248
"""  # ㄴ> 이런 자료가 39080개 등장!


# spicy -> numpy
sparse_mat_arr = sparse_mat.toarray()
sparse_mat_arr.shape  # (5574, 4000)
sparse_mat_arr
"""
array([[0., 0., 0., ..., 0., 0., 0.],
       [0., 0., 0., ..., 0., 0., 0.],
       [0., 0., 0., ..., 0., 0., 0.],
       ...,
       [0., 0., 0., ..., 0., 0., 0.],
       [0., 0., 0., ..., 0., 0., 0.],
       [0., 0., 0., ..., 0., 0., 0.]])
"""



# 5. train / test split
from sklearn.model_selection import train_test_split

# 70% : 30%
x_train, x_test, y_train, y_test = train_test_split(sparse_mat_arr, target, test_size=0.3, random_state=123)

x_train.shape  # (3901, 4000)
type(x_train)  #  numpy.ndarray
x_test.shape  #  (1673, 4000)


# 6. numpy binary file save
import numpy as np

spam_data_split = (x_train, x_test, y_train, y_test)  # 튜플 형태로 묶었음. 4개의 객체를 하나의 파일로 저장하기 위해
np.save('./data/spam_data', spam_data_split)  # np형식으로 저장했으므로 확장자 '.npy'가 자동으로 들어감



# file load
x_train, x_test, y_train, y_test = np.load('./data/spam_data.npy', allow_pickle=True)  # 저장할 때 묶어서 저장한 것들을 읽을 때 쪼개서 불러올 수 있음
x_train.shape  # (3901, 4000)
x_test.shape  # (1673, 4000)









































