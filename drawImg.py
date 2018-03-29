import cv2
import numpy as np
image = cv2.imread("grayNat.jpg")
cv2.line(image, (0, 0), (150, 150), (255, 0, 0), 10)
cv2.rectangle(image, (0, 0), (150, 150), (255, 0, 0), 10)
cv2.circle(image, (150, 150), 50, (0, 255, 0), -1)
pts = np.array([[125, 125], [160, 100], [170, 130], [90, 175], [145, 200]])
cv2.polylines(image, [pts], True, (0, 0, 255), 5)
cv2.imshow("image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()