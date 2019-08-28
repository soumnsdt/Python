import cv2 as cv
import numpy as np

src_img = cv.imread("G:/pic/meinv.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src_img)

face = src_img[50:500, 100:480]
gray = cv.cvtColor(face, cv.COLOR_BGR2GRAY)
change_face = cv.cvtColor(gray, cv.COLOR_GRAY2BGR)
src_img[50:500, 100:480] = change_face
cv.imshow("face", src_img)
cv.waitKey(0)
cv.destroyAllWindows()



