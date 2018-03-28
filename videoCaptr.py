import numpy as np
import cv2

camera = cv2.VideoCapture(0)
out = cv2.VideoWriter('capturdVid.mkv', cv2.VideoWriter_fourcc(*'DIVX'), 50, (640, 480))
while True:
	ret, frame = camera.read()
	cv2.imshow('video', frame)
	out.write(frame)
	if cv2.waitKey(1) == 'a':
		break
camera.release()
out.release()
cv2.destroyAllWindows()