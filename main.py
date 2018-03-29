import numpy as np
import cv2

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    img = cv2.inRange(frame, np.array([33, 116, 137]), np.array([92, 191, 216]))
    img = cv2.erode(img, np.ones((5, 5), np.uint8), iterations=1)
    img = cv2.dilate(img, np.ones((5, 5), np.uint8), iterations=1)
    ret, img = cv2.threshold(img, 250, 255, cv2.THRESH_BINARY)
    one, two, three = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(frame, two, -1, [0, 0, 255], 3)
    cv2.imshow('video', frame)
    if cv2.waitKey(1) == 97:
        break
cap.release()
cv2.destroyAllWindows()

