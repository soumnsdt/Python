import cv2 as cv
import numpy as np

src_img = cv.imread("G:/pic/yzm2.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src_img)
cv.waitKey(0)
cv.destroyAllWindows()


