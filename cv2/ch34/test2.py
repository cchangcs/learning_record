# encoding:utf-8
import cv2
import numpy as np

creteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
cap = cv2.VideoCapture(0)

# 等比缩放
frame_height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
frame_width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
frame_height = int(480 / frame_height * frame_width)
ret = cap.set(cv2.CAP_PROP_FRAME_HEIGHT, frame_height)
ret = cap.set(cv2.CAP_PROP_FRAME_WIDTH, 480)

while cap.isOpened():
    ret, img = cap.read()
    cv2.imshow('img0', img)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    '''
    第一个参数Image，传入拍摄的棋盘图Mat图像，必须是8位的灰度或者彩色图像；
    第二个参数patternSize，每个棋盘图上内角点的行列数，一般情况下，行列数不要相同，便于后续标定程序识别标定板的方向；
    第三个参数corners，用于存储检测到的内角点图像坐标位置，一般用元素是Point2f的向量来表示：vector<Point2f> image_points_buf;
    第四个参数flage：用于定义棋盘图上内角点查找的不同处理方式，有默认值。
    '''
    ret, corners = cv2.findChessboardCorners(image=gray, patternSize=(6, 4), corners=None)

    print(corners)
    print('---------')
    if ret == True:
        # objpoints.append(objp)
        corners2 = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), creteria)
        # imgpoints.append(corners)
        # Draw and display the corners
        cv2.drawChessboardCorners(img, (6, 4), corners2, ret)

    cv2.imshow('img', img)

    key = cv2.waitKey(delay=10)
    if key == ord("q"):
        break

cv2.destroyAllWindows()
