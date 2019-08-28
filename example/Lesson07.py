"""
    高斯模糊
"""
import cv2 as cv
import numpy as np


def clamp(pv):
    if pv > 255:
        return 255
    if pv < 0:
        return 0
    else:
        return pv


# 高斯噪声
def gaussian_noise(image):
    l, w, h = image.shape
#     获取随机数
    for row in range(0, l, 1):
        for col in range(w):
            s = np.random.normal(0, 20, 3)
            b = image[row, col, 0]   # blue
            g = image[row, col, 1]   # green
            r = image[row, col, 2]   # red
            image[row, col, 0] = clamp(b + s[0])
            image[row, col, 1] = clamp(b + s[1])
            image[row, col, 2] = clamp(b + s[2])
    cv.imshow("noise image", image)






src_img = cv.imread("G:/pic/meinv.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src_img)


t1 = cv.getTickCount()
# gaussian_noise(src_img)
t2 = cv.getTickCount()
time = (t2 - t1)/cv.getTickFrequency()
print("used time is %s s" % (time))
# 高斯模糊
dst = cv.GaussianBlur(src_img, (0, 0), 200)
cv.imshow("Gaussian Blur", dst)

cv.waitKey(0)
cv.destroyAllWindows()

