import cv2
import numpy as np
import math
img = cv2.imread('images/g2.png')
IMG1 = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
mid = 0.6
mean = np.mean(IMG1)
gamma = math.log(mid*255)/math.log(mean)
print(gamma)
img_gamma1 = np.power(img, gamma).clip(0,255).astype(np.uint8)
cv2.imshow('input', img)
cv2.imshow('Gamma', img_gamma1)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('images/gammacorred6.jpg', img_gamma1)



