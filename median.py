import cv2
img = cv2.imread('images/6.png')
Img = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
filteredImg = cv2.medianBlur(Img, ksize=3)
cv2.imshow('Original image', Img)
cv2.imshow('Median Filter image', filteredImg)
cv2.waitKey(0)
cv2.destroyAllWindows()