import cv2 as cv
import numpy as np


# 均值模糊
def blur_demo(image):
    # dst = cv.blur(image, (1, 10))   # 垂直方向模糊
    dst = cv.blur(image, (10, 1))   # 水平方向模糊
    cv.imshow("blur_demo", dst)


# 中值模糊
def median_blur_demo(image):
    # dst = cv.blur(image, (1, 10))   # 垂直方向模糊
    dst = cv.blur(image, (10, 1))   # 水平方向模糊
    cv.imshow("blur_demo", dst)


src_img = cv.imread("G:/pic/meinv.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src_img)
blur_demo(src_img)
cv.waitKey(0)
cv.destroyAllWindows()

