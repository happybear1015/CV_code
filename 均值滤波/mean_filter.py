# -*- coding: utf-8 -*-
# 使用均值滤波进行图像处理
import cv2
import matplotlib.pyplot as plt

# 读取图像
img = cv2.imread('meigui.jpg')

result=cv2.blur(img,ksize=(5,5)) # 均值滤波函数cv2.blur()
plt.subplot(1,2,1)
plt.imshow(img)
plt.subplot(1,2,2)
plt.imshow(result)
plt.savefig("result")
plt.show()




