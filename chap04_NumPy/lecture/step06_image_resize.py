# -*- coding: utf-8 -*-
"""
reshape vs resize
 - reshape : 모양 변경
 - resize : 크기 변경
   ex) images -> 120x150 픽셀로 '규격화'

image 규격화 : 실습 
"""
from glob import glob  # file 검색에서 패턴사용(문자열 경로, *.jpg)
from PIL import Image  # image file read
import numpy as np
import matplotlib.pyplot as plt  # 이미지 시각화

# 1. 1개 image file open
path = "./chap04_NumPy"
file = path + '/images/test1.jpg'


img = Image.open(file)  # image file read
type(img)  # PIL.JpegImagePlugin.JpegImageFile
# img.shape  #  'JpegImageFile' object has no attribute 'shape'
np.shape(img)  # (360, 540, 3)   : 이걸 resize를 이용해서 (120, 150, 3)로 줄여보장. (h, w, c)
plt.imshow(img)  # 함수에 픽셀정보를 넣은 형태

img_re = img.resize( (150, 120) )  # w, h 세로 픽셀과 가로 픽셀 위치를 바꿔서 넣어줘야함.
np.shape(img_re)  # (120, 150, 3)
plt.imshow(img_re)  # 해상도가 떨어졌네용. 컬러는 그대로 유지


# PIL -> numpy 변경
img_arr = np.asarray(img)
img_arr
type(img_arr)  # numpy.ndarray
img_arr.shape  # (360, 540, 3)

img_arr2 = np.array(img)
img_arr2   # 똑같눼

# 여러장의 image resize 함수
def imageResize() :
    img_h = 120  # 세로 픽셀
    img_w = 150  # 가로 픽셀
    
    image_resize = []  # 규격화된 image 저장
    
    # glob : file 패턴
    for file in glob(path + '/images/' + '*.jpg') :  # image 폴더에서 jpg형식의 파일을 모두 읽겠다.
        # test1.jpg -> test2.jpg, ...
        img = Image.open(file)  # image file read
        print(np.shape(img))  # image shape
        
        # PIL -> resize
        img = img.resize( (img_w, img_h) )  # w, h
        # PIL -> numpy
        img_data = np.asarray(img)
        
        # resized image save -> to image_resize obj.
        image_resize.append(img_data)
        print(file, ':', img_data.shape)
    
    return np.array(image_resize)  # list -> numpy


image_resize = imageResize()
"""
(360, 540, 3)
./chap04_NumPy/images\test1.jpg : (120, 150, 3)
(332, 250, 3)
./chap04_NumPy/images\test2.jpg : (120, 150, 3)
"""  # 두개의 파일, 두줄의 출력물

image_resize.shape  # (2, 120, 150, 3) (이미지 장 수, 세로 픽셀, 가로 픽셀, 컬러)

#  첫 번째 이미지만 꺼내오겠다. -> index 기본 값은 차수가 가장 높은 이미지 수
image_resize[0].shape  # (120, 150, 3)
image_resize[1].shape  # (120, 150, 3)



































