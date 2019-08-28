# 算数运算
import cv2 as cv
import numpy as np


def subtract_demo(m1, m2):
    dst = cv.subtract(m1, m2)
    cv.imshow("subtract demo", dst)


def add_demo(m1, m2):
    dst = cv.add(m1, m2)
    cv.imshow("add demo", dst)


def multiply_demo(m1, m2):
    dst = cv.multiply(m1, m2)
    cv.imshow("multiply demo", dst)


def divide_demo(m1, m2):
    dst = cv.divide(m1, m2)
    cv.imshow("divide demo", dst)


# 均值
def mean_demo(m1, m2):
    M1 = cv.mean(m1)
    M2 = cv.mean(m2)
    print(M1)
    print(M2)


# 逻辑运算
def logic_and_demo(m1, m2):
    A1 = cv.bitwise_and(m1, m2)
    cv.imshow("and image", A1)



# 方差
def meanStdDev_demo(m1, m2):
    M1, dev1 = cv.meanStdDev(m1)
    M2, dev2 = cv.meanStdDev(m2)
    print(M1)
    print(M2)
    print(dev1)
    print(dev2)


# 提升图像的亮度和对比度
def contract_brightness_demo(image, c, b):
    h, w, ch = image.shape
    blank = np.zeros([h, w, ch], image.dtype)
    dst = cv.addWeighted(image, c, blank, 1-c, b)
    cv.imshow("contract_brightness_demo", dst)


print("========Hello Python========")
src_img1 = cv.imread("G:/pic/LinuxLogo.jpg")
cv.namedWindow("input image1", cv.WINDOW_AUTOSIZE)
cv.imshow("input image1", src_img1)
print(src_img1.shape)
src_img2 = cv.imread("G:/pic/WindowsLogo.jpg")
cv.namedWindow("input image2", cv.WINDOW_AUTOSIZE)
cv.imshow("input image2", src_img2)
print(src_img2.shape)
# subtract_demo(src_img1, src_img2)
# add_demo(src_img1, src_img2)
# multiply_demo(src_img1, src_img2)
# divide_demo(src_img1, src_img2)
# mean_demo(src_img1, src_img2)
# meanStdDev_demo(src_img1, src_img2)
# logic_and_demo(src_img1, src_img2)
contract_brightness_demo(src_img2, 1.5, 1)

# cv.imwrite("G:/pic/result.bmp", src_img)
cv.waitKey(0)
cv.destroyAllWindows()


