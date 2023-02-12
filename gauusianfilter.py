import cv2
image = cv2.imread('images/17.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2BGRA)
figure_size = 9
new_image = cv2.GaussianBlur(image, (figure_size, figure_size),0)
cv2.imshow('Original image', image)
cv2.imshow('Filtered image', new_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
