import numpy as np
import cv2

frame = cv2.imread("shield.png")
cv2.imshow("imageRead", frame)
cv2.waitKey(0)
cv2.destroyAllWindows()