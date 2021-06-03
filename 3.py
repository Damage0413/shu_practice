import cv2
import numpy as np

img = cv2.imread('E:\VS-Code-Python\shu\practice/lena.jpg')
img_b = cv2.bilateralFilter(img, 9, 75, 75)
kernel1 = np.array([[0, -1, 0], [-1, 4, -1], [0, -1, 0]])  #四方向模板
kernel2 = np.array([[1, 1, 1], [1, -8, 1], [1, 1, 1]])  #八方向模板
img1 = cv2.filter2D(img_b, cv2.CV_8UC3, kernel1)
img2 = cv2.filter2D(img_b, cv2.CV_8UC3, kernel2)
img1 = cv2.add(img, img1)
img2 = cv2.add(img, img2)
cv2.imshow('original', img)
cv2.imshow('result1', img1)
cv2.imshow('result2', img2)
cv2.waitKey()
cv2.destroyAllWindows()
