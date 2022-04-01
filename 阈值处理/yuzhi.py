import cv2
import matplotlib.pyplot as plt

src = './apple.jpg'
src = cv2.imread(src, 0)
plt.subplot(1, 2, 1)
plt.imshow(src)
retval, dst = cv2.threshold(src, 172, 255, type=cv2.THRESH_BINARY)
plt.subplot(1, 2, 2)
plt.imshow(dst)
plt.savefig("result.jpg")
plt.show()

