import numpy as np
import cv2
from math import log10, sqrt
img = cv2.imread('images/6.png')
img1 = cv2.imread('images/CLAHE Image.png')
imge1 = cv2.imread('images/16.jpg')
img2 = cv2.imread('images/c1.png')
imge3 = cv2.imread('images/12.jpg')
img3 = cv2.imread('images/c44.png')
imge4= cv2.imread('images/17.jpg')
img5 = cv2.imread('images/c8.png')
imge5= cv2.imread('images/7.jpg')
img6 = cv2.imread('images/c5.png')


def PSNR(img, img1):
    mse = np.mean((img - img1) ** 2)
    if (mse == 0):
        return 100
    max_pixel = 255.0
    psnr = 20 * log10(max_pixel / sqrt(mse))
    return psnr
def main():
    value = PSNR(img, img1)
    print(f"PSNR value of image  {value} dB")
if __name__ == "__main__":
    main()


def PSNR(imge1, img2):
    mse = np.mean((imge1 - img2) ** 2)
    if (mse == 0):
        return 100
    max_pixel = 255.0
    psnr = 20 * log10(max_pixel / sqrt(mse))
    return psnr
def main():
    value = PSNR(imge1, img2)
    print(f"PSNR value of image  {value} dB")
if __name__ == "__main__":
    main()

def PSNR(imge3, img3):
    mse = np.mean((imge3 - img3) ** 2)
    if (mse == 0):
        return 100
    max_pixel = 255.0
    psnr = 20 * log10(max_pixel / sqrt(mse))
    return psnr
def main():
    value = PSNR(imge3, img3)
    print(f"PSNR value of image  {value} dB")
if __name__ == "__main__":
    main()

def PSNR(imge4, img5):
    mse = np.mean((imge4 - img5) ** 2)
    if (mse == 0):
        return 100
    max_pixel = 255.0
    psnr = 20 * log10(max_pixel / sqrt(mse))
    return psnr
def main():
    value = PSNR(imge4, img5)
    print(f"PSNR value of image  {value} dB")
if __name__ == "__main__":
    main()

def PSNR(imge5, img6):
    mse = np.mean((imge5 - img6) ** 2)
    if (mse == 0):
        return 100
    max_pixel = 255.0
    psnr = 20 * log10(max_pixel / sqrt(mse))
    return psnr
def main():
    value = PSNR(imge5, img6)
    print(f"PSNR value of image  {value} dB")
if __name__ == "__main__":
    main()


