import cv2
import numpy as np
import math

# read image
img = cv2.imread('images/image4.png')

# convert img to HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
hue, sat, val = cv2.split(hsv)

# compute gamma = log(mid*255)/log(mean)
mid = 0.5
mean = np.mean(val)
gamma = math.log(mid*255)/math.log(mean)
print(gamma)

# do gamma correction on value channel
val_gamma = np.power(val, gamma).clip(0,255).astype(np.uint8)


# combine new value channel with original hue and sat channels
hsv_gamma = cv2.merge([hue, sat, val_gamma])
img_gamma2 = cv2.cvtColor(hsv_gamma, cv2.COLOR_HSV2BGR)

# show results
cv2.imshow('input', img)
cv2.imshow('result2', img_gamma2)
cv2.waitKey(0)
cv2.destroyAllWindows()

# save results
cv2.imwrite('images/im3.jpg', img_gamma2)


