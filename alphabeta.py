import numpy as np
import cv2
img = cv2.imread('images/6.png')
img1 = cv2.imread('images/CLAHE Image.png')
mse = np.square(np.subtract(img,img1)).mean()
print("MSE is:",mse)

imge1 = cv2.imread('images/16.jpg')
img2 = cv2.imread('images/c1.png')
mse = np.square(np.subtract(imge1,img2)).mean()
print("MSE is:",mse)

imge3 = cv2.imread('images/12.jpg')
img3 = cv2.imread('images/c44.png')
mse = np.square(np.subtract(imge3,img3)).mean()
print("MSE is:",mse)


imge4= cv2.imread('images/17.jpg')
img5 = cv2.imread('images/c8.png')
mse = np.square(np.subtract(imge4,img5)).mean()
print("MSE is:",mse)

imge5= cv2.imread('images/7.jpg')
img6 = cv2.imread('images/c5.png')
mse = np.square(np.subtract(imge5,img6)).mean()
print("MSE is:",mse)

