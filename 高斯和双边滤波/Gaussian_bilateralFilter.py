import cv2
import matplotlib.pyplot as plt
import numpy as np

img=cv2.imread('R-C.jpg')
img_1=cv2.resize(img,(480,300))
img_2=cv2.GaussianBlur(img_1,(5,5),.8,.8)
img_3=cv2.bilateralFilter(img_1,9,75,75)
# cv2.imshow('GaussianBlur',img_2)
# cv2.imshow('bilateralFilter',img_3)
imgs = np.hstack([img_1,img_2,img_3])
cv2.imshow('result',imgs)
cv2.imwrite('result.jpg',imgs)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.KeyPoint()
cv2.SIFT_create()