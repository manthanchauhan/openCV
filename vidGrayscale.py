import numpy as np
import cv2

cap = cv2.VideoCapture('input.mkv')
out = cv2.VideoWriter('output.mkv', cv2.VideoWriter_fourcc(*'DIVX'), 10, (640, 480))
while(cap.isOpened()):
	ret, frame = cap.read()
	frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	cv2.imshow('gray', frame)
	out.write(frame)
	if cv2.waitKey(1) == 97:
		break;
cap.release()
cv2.destroyAllWindows()