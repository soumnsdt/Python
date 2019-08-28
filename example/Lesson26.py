"""
    人脸识别----识别图片
"""
import cv2 as cv
import numpy as np


def face_detect_demo():
    # 我们要把src变成一张灰度图像
    gray = cv.cvtColor(src_img, cv.COLOR_BGR2GRAY)
    #  通过级联检测器 加载特征数据
    face_detector = cv.CascadeClassifier("G:/OpenCV/opencv/build/etc/haarcascades/haarcascade_frontalface_alt_tree.xml")
    # 在多个尺度空间进行人脸检测
    """
    1、输入哪一个图像
    2、尺度变化，
    3、假阳性    检测不出来就要设的低一点，一般设置2，3，4，5
    """
    faces = face_detector.detectMultiScale(gray, 1.02, 2)
    for x, y, w, h in faces:
        """
        1、
        2、
        3、
        4、颜色
        5、像素的宽度
        """
        cv.rectangle(src_img, (x, y), (x+w, y+h), (0, 0, 255), 2)
    cv.imshow("result", src_img)



src_img = cv.imread("G:/pic/myself.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.namedWindow("result", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src_img)
face_detect_demo()
cv.waitKey(0)
cv.destroyAllWindows()

