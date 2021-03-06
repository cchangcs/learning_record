import cv2
import numpy as np


def nothing(x):
    pass


# Create a black image, a window
img = np.zeros((300, 512, 3), np.uint8)
cv2.namedWindow('image', cv2.WINDOW_NORMAL)

# Create trackbars for color change
cv2.createTrackbar('R', 'image', 0, 255, nothing)
cv2.createTrackbar('G', 'image', 0, 255, nothing)
cv2.createTrackbar('B', 'image', 0, 255, nothing)

# create switch for ON/OFF functionality
switch = '0 : OFF \n 1 : ON'
cv2.createTrackbar(switch, 'image', 0, 1, nothing)
# 只有当 转换按钮 指向 ON 时，滑动条才有用，否则窗口都是黑的

while True:
    # get current positions of four trackbars
    r = cv2.getTrackbarPos('R', 'image')
    g = cv2.getTrackbarPos('G', 'image')
    b = cv2.getTrackbarPos('B', 'image')
    s = cv2.getTrackbarPos(switch, 'image')

    if s == 0:
        img[:] = 0
    else:
        img[:] = [b, g, r]
    cv2.imshow('image', img)
    k = cv2.waitKeyEx(1)
    if k == ord('q'):
        break

cv2.destroyAllWindows()

