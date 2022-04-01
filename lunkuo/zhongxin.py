import cv2
import matplotlib.pyplot as plt
bgr_img='./yuan_.jpg'

img = cv2.imread(bgr_img)
plt.subplot(1,2,1)
# plt.imshow(img)
gray_img = cv2.imread(bgr_img,0)
plt.imshow(gray_img)
# print('gray_img',gray_img)
th, binary = cv2.threshold(gray_img, 254, 255, cv2.THRESH_OTSU)
contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
M =cv2.moments(contours[0])
print(M)
cx=int(M['m10']/M['m00'])
cy=int(M['m01']/M['m00'])
print(cx)
print(cy)