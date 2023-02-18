import cv2 

image1 = cv2.imread('sample.png')

cv2.imshow('original', image1)

gray_img = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
invert = cv2.bitwise_not(gray_img)

blur = cv2.GaussianBlur(invert, (21,21), 0)
invertblur = cv2.bitwise_not(blur)
sketch = cv2.divide(gray_img, invertblur, scale=256.0)

cv2.imwrite('sketch.png', sketch)
cv2.imread('sketch.png')
cv2.imshow('window', sketch)

cv2.waitKey(0)
cv2.destroyAllWindows()
