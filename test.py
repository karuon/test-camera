import cv2
import sys

delay = 1
window_name = 'frame'
camera = cv2.VideoCaputure(0)
if not camera.isOpened():
    sys.exit()

while True:
    ret,frame = camera.read()
    cv2.imshow(window_name,frame)
    if cv2.waitKey(delay) & 0xFF == ord('q'):
        break
cv2.destroyWindow(winodw_name)

