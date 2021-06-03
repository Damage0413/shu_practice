import cv2

img = cv2.imread("shu/practice/3.jpg",0)
retval, dst = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY)

cv2.imshow('original',img)
cv2.imshow('result',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()