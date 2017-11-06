import cv2

src=cv2.imread('/Users/yizeliu/Downloads/OpenCV_homework/Test_images/Lenna.png')
cv2.imwrite('Original.jpg',src)
grays = cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)

[temp,threshold]=cv2.threshold(grays,128,255,2)
cv2.imwrite('Threshold.jpg',threshold)

[temp,threshold1]=cv2.threshold(grays,128,255,cv2.THRESH_BINARY)
cv2.imwrite('Binarythreshold.jpg',threshold1)

[temp,threshold2]=cv2.threshold(grays,125,255,cv2.THRESH_BINARY_INV)
[temp,threshold3]=cv2.threshold(grays,27,255,cv2.THRESH_BINARY)
bandthreshold=cv2.bitwise_and(threshold2,threshold3)
cv2.imwrite('BandThreshold.jpg',bandthreshold)

[temp,threshold4]=cv2.threshold(grays,128,255,cv2.THRESH_BINARY_INV|cv2.THRESH_OTSU)
semithreshold=cv2.bitwise_and(grays,threshold4)
cv2.imwrite('SemiThreshold.jpg',semithreshold)

threshshold5 = cv2.adaptiveThreshold(grays,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,101,10)
cv2.imwrite('AdaptiveThreshold.jpg',threshshold5)