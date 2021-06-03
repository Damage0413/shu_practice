import cv2
import numpy as np
from sympy import im
img = cv2.imread("shu/practice/2.jpg")
height = img.shape[0]
width = img.shape[1]
center=cv2.imread("shu/practice/center_2.jpg")
means, stdevs = [], []
for i in range(3):
    pixels = center[:, :, i]  # 拉成一行
    means.append(np.mean(pixels))
    stdevs.append(np.std(pixels))
stdevs=np.power(stdevs,2)
img_1 = np.zeros(img.shape, np.uint8)
for i in range(height):
        for j in range(width):
            (b,g,r) =  img[i,j]
            img_1[i][j]=[0,0,0]
            if((np.square(b-means[0])+ np.square(g-means[1])+ np.square(r-means[2]))<max(stdevs)):
                img_1[i][j]=(b,g,r)
img_2=np.zeros(img.shape, np.uint8)
for i in range(height):
        for j in range(width):
            (b,g,r) =  img[i,j]
            img_2[i][j]=[0,0,0]
            if(abs(b-means[0])<np.power(stdevs[0],0.5) and abs(g-means[1])<np.power(stdevs[1],0.5) and abs(r-means[2])<np.power(stdevs[2],0.5)):
                img_2[i][j]=(b,g,r)
cv2.imshow('image',img)
cv2.imshow('image1',img_1)
cv2.imshow('image2',img_2)
cv2.waitKey(0)
