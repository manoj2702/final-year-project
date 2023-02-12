import cv2
from matplotlib import pyplot as plt
image = cv2.imread('images/16.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
figure_size = 9
new_image = cv2.blur(image,(figure_size, figure_size))
plt.figure(figsize=(11,6))
plt.subplot(121), plt.imshow(cv2.cvtColor(image, cv2.COLOR_HSV2RGB)),plt.title('Original')
plt.subplot(122), plt.imshow(cv2.cvtColor(new_image, cv2.COLOR_HSV2RGB)),plt.title('Mean filter')
plt.show()