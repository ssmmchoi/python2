# -*- coding: utf-8 -*-
"""
news crawling data -> word vector
    문장 -> 단어 벡터 -> 희소행렬(Sparse matrix)
    ex) '직업은 데이터 분석가 입니다.' -> '직업 데이터 분석가'
"""



from konlpy.tag import Kkma # class 
from wordcloud import WordCloud # class 
import pickle

# object 생성 
kkma = Kkma()

# 1. pickle file 읽기 : news_data.pck
file = open('C:\\ITWILL\\Work\\4_Python-II\\workspace\\chap07_Crawling\\data\\news_data.pck', mode='rb')
news_data = pickle.load(file)
file.close()

news_data
type(news_data) # list
len(news_data) # 11600
news_data[:5]

# docs -> sentence 
ex_sent = [kkma.sentences(sent)[0] for sent in news_data]
ex_sent
len(ex_sent) # 11600
ex_sent[:5]


# 3. 명사 추출 : Kkma 
# nouns_word = [] # 명사 저장 

# for sent in ex_sent : # '형태소 분석을 시작합니다.'
#     for noun in kkma.nouns(sent) : # 문장 -> 명사 
#         nouns_word.append(noun)
# 이렇게 하면 어디까지가 어떤문장인지 알 수 없고 그저 명사만 어펜드 됨

# 3. sentence -> word vector
from re import match    

sentence_nouns = []

for sent in ex_sent :  # 11600번
    word_vec = ""
    for noun in kkma.nouns(sent) :  # 문장에서 명사만 추출
        if len(noun) >1 and not(match('^[0-9]', noun)) :
            word_vec += noun + " "   # 문장 내에서 명사들을 띄어쓰기 단위로 append
    print(word_vec)
    sentence_nouns.append(word_vec)

len(sentence_nouns)  # 11600

ex_sent[0]  # '의협 " 감염병 위기 경보 상향 제안.. 환자 혐오 멈춰야"'  : 원본
sentence_nouns[0]  # '의협 감염병 위기 경보 상향 제안 환자 혐오 '  ->  문장번호 : 1

ex_sent[-1]  # '미, 인건비 우선 협의 제안에 " 포괄적 SMA 신속 타결 대단히 손상"'
sentence_nouns[-1]  # '인건비 우선 협의 제안 포괄적 신속 타결 손상 '  ->  문장번호 : 11600


# 4. file save
import pickle

file = open('../data/sentence_nouns.pickle', mode='wb')
pickle.dump(sentence_nouns, file)
print('file save')
file.close()


# file load
file = open('../data/sentence_nouns.pickle', mode='rb')
word_vector = pickle.load(file)
word_vector[0]  # '의협 감염병 위기 경보 상향 제안 환자 혐오 '
























