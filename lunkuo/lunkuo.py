import cv2
import matplotlib.pyplot as plt
import numpy as np
import math


def draw(img, result):
    # 下面几个参数，可能需要根据自己的数据进行调整
    x = int(result[0][0])  # 矩形框的中心点x
    y = int(result[0][1])  # 矩形框的中心点y
    angle = result[2]  # 矩形框的倾斜角度（长边相对于水平）
    width, height = int(result[1][0]), int(result[1][1])  # 矩形框的宽和高
    if result[1][0] > result[1][1]:
        height, width = int(result[1][0]), int(result[1][1])
    else:
        height, width = int(result[1][1]), int(result[1][0])
    anglePi = angle * math.pi / 180.0  # 计算角度
    cosA = math.cos(anglePi)
    sinA = math.sin(anglePi)

    x1 = x - 0.5 * width
    y1 = y - 0.5 * height

    x0 = x + 0.5 * width
    y0 = y1

    x2 = x1
    y2 = y + 0.5 * height

    x3 = x0
    y3 = y2

    x0n = (x0 - x) * cosA - (y0 - y) * sinA + x
    y0n = (x0 - x) * sinA + (y0 - y) * cosA + y

    x1n = (x1 - x) * cosA - (y1 - y) * sinA + x
    y1n = (x1 - x) * sinA + (y1 - y) * cosA + y

    x2n = (x2 - x) * cosA - (y2 - y) * sinA + x
    y2n = (x2 - x) * sinA + (y2 - y) * cosA + y

    x3n = (x3 - x) * cosA - (y3 - y) * sinA + x
    y3n = (x3 - x) * sinA + (y3 - y) * cosA + y

    # 根据得到的点，画出矩形框
    cv2.line(img, (int(x0n), int(y0n)), (int(x1n), int(y1n)), (0, 0, 255), 1, 4)
    cv2.line(img, (int(x1n), int(y1n)), (int(x2n), int(y2n)), (0, 0, 255), 1, 4)
    cv2.line(img, (int(x2n), int(y2n)), (int(x3n), int(y3n)), (0, 0, 255), 1, 4)
    cv2.line(img, (int(x0n), int(y0n)), (int(x3n), int(y3n)), (0, 0, 255), 1, 4)


bgr_img='./yuan_.jpg'

img = cv2.imread(bgr_img)
plt.subplot(1,2,1)
# plt.imshow(img)
gray_img = cv2.imread(bgr_img,0)
plt.imshow(gray_img)
print('gray_img',gray_img)
th, binary = cv2.threshold(gray_img, 254, 255, cv2.THRESH_OTSU)
contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
print('contours',contours)
print('contours的类型为：',type(contours))
print('contours的长度为：',len(contours))
cv2.drawContours(gray_img, contours, -1, (0, 0, 255), 3)

bounding_boxes = [cv2.boundingRect(cnt) for cnt in contours]

for bbox in bounding_boxes:
    [x, y, w, h] = bbox
    cv2.rectangle(gray_img, (x, y), (x + w, y + h), color=(0, 100, 100), thickness=2)

plt.subplot(1,2,2)
plt.imshow(gray_img)
plt.show()


# # cv2.minAreaRect
# bounding_boxes = [cv2.minAreaRect(cnt) for cnt in contours]
#
# for bbox in bounding_boxes:
#     draw(gray_img, bbox)
# plt.subplot(1, 2, 2)
# plt.imshow(gray_img)
# plt.show()