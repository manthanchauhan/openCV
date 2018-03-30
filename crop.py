import cv2
import numpy as np

input = cv2.imread('sample_image.jpg', cv2.IMREAD_GRAYSCALE)
input = cv2.resize(input, (640, 480))
aftrCnny = cv2.Canny(input, 100, 200)
cv2.imshow('canny', aftrCnny)
cv2.waitKey(0)
cv2.destroyAllWindows()

