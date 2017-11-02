# -*- coding: utf-8 -*-

import cv2
import numpy as np
img=cv2.imread('/Users/yizeliu/Downloads/OpenCV_homework/Test_images/baboon.jpg')
cv2.namedWindow('Original image')
cv2.imshow('Original',img)
b,g,r=cv2.split(img)
cv2.imshow("Blue",b)
cv2.imshow("Green", g)
cv2.imshow("Red",r)
cv2.imwrite("Blue.jpg",b)
cv2.imwrite("Green.jpg",g)
cv2.imwrite("Red.jpg",r)

YCrCb=cv2.cvtColor(img,cv2.COLOR_BGR2YCrCb)
y,cb,cr=cv2.split(YCrCb)
cv2.imshow("Y",y)
cv2.imshow("Cb", cb)
cv2.imshow("Cr",cr)
cv2.imwrite("Y.jpg",y)
cv2.imwrite("Cb.jpg",cb)
cv2.imwrite("Cr.jpg",cr)

hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
hue,saturation,value=cv2.split(hsv)
cv2.imshow("Hue",hue)
cv2.imshow("Saturation", saturation)
cv2.imshow("Value",value)
cv2.imwrite("Hue.jpg",hue)
cv2.imwrite("Saturation.jpg",saturation)
cv2.imwrite("Value.jpg",value)
cv2.waitKey(0)
cv2.destroyAllWindows()
