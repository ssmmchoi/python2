'''
step01_array 관련 문제 
 문제) 정규분포를 따르는 난수를 이용하여 5행 4열 구조의 다차원 배열 객체를 생성하고,
       각 행 단위로 합계, 최댓값, 최솟값을 구하시오.

  << 출력 결과 예시>>
1 행 합계 :  -1.2126122901
1 행 최댓값 :  1.13798453455
1 행 최솟값 :  -1.5068942376
2 행 합계 :  1.54051825695
2 행 최댓값 :  2.29973856355
2 행 최솟값 :  -1.29798198518
3 행 합계 :  -2.7021834762
3 행 최댓값 :  0.914392834242
3 행 최솟값 :  -2.1954633708
4 행 합계 :  2.35515059667
4 행 최댓값 :  3.01882725644
4 행 최솟값 :  -0.420709089935
5 행 합계 :  1.14825745061
5 행 최댓값 :  1.81204331436
5 행 최솟값 :  -1.5605324754
'''    

import numpy as np
num = np.random.rand(5,4)
num

cnt = 0
for row in num :
    cnt += 1
    rsum = row.sum()
    rmax = row.max()
    rmin = row.min()
    print(cnt, ' 행 합계 : ', rsum, '\n', cnt, ' 행 최댓값 : ', rmax, '\n', cnt, ' 행 최솟값 : ', rmin, sep='')


cnt = 0
for row in num :
    cnt += 1
    rsum = row.sum()
    rmax = row.max()
    rmin = row.min()
    print(f"{cnt}행 합계 : {rsum}")
    print(f"{cnt}행 최댓값 : {rmax}")
    print(f"{cnt}행 최솟값 : {rmin}")


cnt = 0
for row in num :
    cnt += 1
    rsum = row.sum()
    rmax = row.max()
    rmin = row.min()
    print("{}행 합계 : {}".format(cnt, rsum))
    print("{}행 최댓값 : {}".format(cnt, rmax))
    print("{}행 최솟값 : {}".format(cnt, rmin))

    
"""
1 행 합계 : 2.052772790928463
1 행 최댓값 : 0.7782114032916481
1 행 최솟값 : 0.2942274893694511
2 행 합계 : 2.45315957489965
2 행 최댓값 : 0.8120130863736899
2 행 최솟값 : 0.4133496964484399
3 행 합계 : 1.617188428966351
3 행 최댓값 : 0.6553858765177978
3 행 최솟값 : 0.14953273440220516
4 행 합계 : 2.252166972967724
4 행 최댓값 : 0.7672673922196287
4 행 최솟값 : 0.1894620229225107
5 행 합계 : 0.7693919138322477
5 행 최댓값 : 0.4025914470766837
5 행 최솟값 : 0.00030220681953285755
"""

num.mean()
num.std()
