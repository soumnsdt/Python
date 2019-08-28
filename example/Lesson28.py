"""
    数字验证码的识别
    OpenCV + Tesserct-OCR
    OpenCV预处理
    Tesserct-OCR验证码识别
"""
import cv2 as cv
import numpy as np
from PIL import Image
import pytesseract as tess


def recognize_text():
    gray = cv.cvtColor(src_img, cv.COLOR_BGR2GRAY)
    # 二值化图片
    ret, binary = cv.threshold(gray, 255, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (1, 3))
    bin1 = cv.morphologyEx(binary, cv.MORPH_OPEN, kernel)
    # kernel = cv.getStructuringElement(cv.MORPH_CROSS, (2, 1))
    # open_out = cv.morphologyEx(bin1, cv.MORPH_OPEN, kernel)
    cv.imshow("binary-image", bin1)

    # cv.bitwise_not(open_out, open_out)
    # text_Image = Image.fromarray(open_out)
    # text = tess.image_to_string(text_Image)
    # print("识别结果：%s" %(text))


src_img = cv.imread("G:/pic/yzm.png")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src_img)
recognize_text()
cv.waitKey(0)
cv.destroyAllWindows()




