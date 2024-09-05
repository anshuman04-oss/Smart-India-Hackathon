import numpy as np
import cv2 as cv

img = np.zeros((256, 256, 3))

def draw(event, x, y, flags, params):
    if event == 1:
        cv.circle(img, center=(x, y), radius=10, color=(0, 0, 255), thickness=-1)

cv.namedWindow(winname="window")
cv.setMouseCallback("window", draw)

while True:
    cv.imshow("window", img)
    
    if cv.waitKey(1) and 0xFF == ord('x'):
        break
    
cv.destroyAllWindows()
        