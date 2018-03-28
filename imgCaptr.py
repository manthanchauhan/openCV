import numpy
import cv2

camera = cv2.VideoCapture(0)
ret, frame = camera.read()
cv2.imshow("capturedImage", frame)
camera.release()
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('capturedImage.png', frame)
