import numpy as np
import cv2

testImg_ = cv2.imread('test.jpg')
testImg = cv2.cvtColor(testImg_, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(testImg, 250, 255, cv2.THRESH_BINARY_INV)
thresh = cv2.erode(thresh, np.ones((0, 0), np.uint8), iterations = 1)
thresh = cv2.dilate(thresh, np.ones((0, 0), np.uint8), iterations = 1)
ret, contours, trash = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(testImg_, contours, -1, [0, 0, 0], 2)
cv2.imshow('contours', testImg_)
cv2.waitKey(0)
for i in contours:
	apprxEdgs = cv2.approxPolyDP(i,0.025 * cv2.arcLength(i, True), True)
	if(len(apprxEdgs) == 3):
		print('triangle')
	elif(len(apprxEdgs) == 4):
		print('square')
	elif(len(apprxEdgs) == 5):
		print('pentagon')
	elif(len(apprxEdgs) == 7):
		print('arrow')
	else:
		print('circle')
cv2.waitKey(0)
cv2.destroyAllWindows()


