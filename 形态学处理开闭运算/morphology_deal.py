#coding=utf-8
import cv2
import numpy as np
img=cv2.imread('biyunsuan.png',0)
#创建矩形结构单元
g=cv2.getStructuringElement(cv2.MORPH_RECT,(15,15))

#形态学处理,开运算
# img_open=cv2.morphologyEx(img,cv2.MORPH_OPEN,g)
#形态学处理,闭运算
img_open=cv2.morphologyEx(img,cv2.MORPH_CLOSE,g)
print(img.shape)

# img_hat=img-img_open
# cv2.imshow('img',img)
#cv2.imshow('erode',edge_dilate)
# img_none=np.ndarray([397, 395])

img_result=np.hstack([img,img_open])
cv2.imshow('img_open',img_result)
# cv2.imshow('img_open_',img_hat)
cv2.imwrite("result.jpg",img_result)
cv2.waitKey(0)
cv2.destroyAllWindows()