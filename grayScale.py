import cv2
import numpy as np
image = cv2.imread("image.jpg",cv2.IMREAD_GRAYSCALE)
cv2.imshow("image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('graythanos2.jpg', image)