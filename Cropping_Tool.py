import numpy as np
import cv2 as cv

img = np.zeros((256, 256, 3))

flag = False
ix = -1
iy = -1
finalx = -1
finaly = -1

def draw(event, x, y, flags, params):
    
    global flag, ix, iy, finalx, finaly
    
    if event == 1:
        flag = True
        ix = x
        iy = y
    elif event == 0:
        # Mouse hover after click
        if flag == True:
            cv.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)
    elif event == 4:
        cv.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)
        flag = False
        finalx = x
        finaly = y

cv.namedWindow(winname="window")
cv.setMouseCallback("window", draw)

while True:
    
    cv.imshow("window", img[ix:finalx, iy:finaly, :])
    
    if cv.waitKey(1) and 0xFF == ord('x'):
        break
    
cv.destroyAllWindows()
        