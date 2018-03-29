import numpy as np
import cv2

file = cv2.imread('input.jpg')
img = cv2.inRange(file, np.array([0, 0, 0]), np.array([20, 20, 20]));
ret, thr = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY)
c1, c2, c3 = cv2.findContours(thr, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE);
cv2.drawContours(file, c2, -1, [0, 255, 0], 5);
cv2.imshow('file', file);
cv2.imwrite('output.jpg', file)
cv2.waitKey(0)
cv2.destroyAllWindows()