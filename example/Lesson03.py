#  色彩空间（Color Space）
#  RGB   HSV   HLS  YCrCb   YUV
#  色彩空间转换API   H:0~100    S:0~255   V:0~255
#  学会用inRange
#  通道分离与合并
#  黑色  lower_hsv = np.array([0, 0, 0])      upper_hsv = np.array([180, 255, 46])
#  灰色  lower_hsv = np.array([0, 0, 46])     upper_hsv = np.array([180, 43, 220])
#  白色  lower_hsv = np.array([0, 0, 221])    upper_hsv = np.array([180, 30, 255])
#  红色   lower_hsv = np.array([0/156, 43, 46])     upper_hsv = np.array([10/180, 255, 255])
#  橙色   lower_hsv = np.array([0, 0, 0])
# #        upper_hsv = np.array([180, 255, 46])
#  黄色   lower_hsv = np.array([0, 0, 0])
# #        upper_hsv = np.array([180, 255, 46])
#  绿色  lower_hsv = np.array([37, 43, 46])
#        upper_hsv = np.array([77, 255, 255])
#  青色  lower_hsv = np.array([0, 0, 0])
# #        upper_hsv = np.array([180, 255, 46])
#  蓝色   lower_hsv = np.array([0, 0, 0])
# #        upper_hsv = np.array([180, 255, 46])
#  紫色  lower_hsv = np.array([0, 0, 0])
# #        upper_hsv = np.array([180, 255, 46])
import cv2 as cv
import numpy as np


def extrace_object_demo():
    capture = cv.VideoCapture("G:/video/1.mp4")
    while(True):
        ret, frame = capture.read()
        if ret == False:
            break
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        lower_hsv = np.array([37, 43, 46])
        upper_hsv = np.array([77, 255, 255])
        mask = cv.inRange(hsv, lowerb=lower_hsv, upperb=upper_hsv)
        dit = cv.bitwise_and(frame, frame, mask=mask)
        cv.imshow("video", frame)
        cv.imshow("mask", dit)
        c = cv.waitKey(40)
        if c == 27:
            break


def color_space_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    cv.imshow("gray", gray)
    hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    cv.imshow("HSV", hsv)
    yuv = cv.cvtColor(image, cv.COLOR_BGR2YUV)
    cv.imshow("YUV", yuv)
    hls = cv.cvtColor(image, cv.COLOR_BGR2HLS)
    cv.imshow("HLS", hls)



print("========Hello Python========")
# src_img = cv.imread("G:/pic/meinv.jpg")
# cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
# cv.imshow("input image", src_img)
# 分离
# b, g, r = cv.split(src_img)
# cv.imshow("b", b)
# cv.imshow("g", g)
# cv.imshow("r", r)
# 合并
# change_img = cv.merge([b, g, r])
# cv.imshow("change_img", change_img)
extrace_object_demo()

# cv.imwrite("G:/pic/result.bmp", src_img)
cv.waitKey(0)
cv.destroyAllWindows()
