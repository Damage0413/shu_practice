import cv2

img1 = cv2.imread("shu\practice/4.jpg")
img2 = cv2.imread("shu\practice/5.jpg")
img1 = cv2.resize(img1, (img2.shape[1], img2.shape[0]))  #将两幅图像的大小统一

add = cv2.add(img1, img2)  # 两个图像相加
subtract = cv2.subtract(img1, img2)  # 两个图像相减

cv2.imshow('add', add)
cv2.imshow('subtract', subtract)
cv2.waitKey(0)
cv2.destroyAllWindows()


