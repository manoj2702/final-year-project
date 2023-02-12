import numpy as np
import cv2
img = cv2.imread('images/6.png')
img1 = cv2.imread('images/CLAHE Image.png')
mse = np.square(np.subtract(img,img1)).mean()
print("MSE is:",mse)


