#  图像的加载和保存
import cv2 as cv
import numpy as np  # 科学技术包


def get_image_info(image):
    print(type(image))
    print(image.shape)
    print(image.size)
    print(image.dtype)
    pixel_data = np.array(image)
    print(pixel_data)


def video_demo():
    capture = cv.VideoCapture(0)
    while(True):
        ret, frame = capture.read()
        frame = cv.flip(frame, 1)  # 把视频左右翻一下
        cv.imshow("Video", frame)
        c = cv.waitKey(50)
        if c == 27:
            break


print("========Hello Python========")
src_img = cv.imread("G:/pic/meinv.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src_img)
get_image_info(src_img)
cv.imwrite("G:/pic/result.bmp", src_img)
cv.waitKey(0)
cv.destroyAllWindows()