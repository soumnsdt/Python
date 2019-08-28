# numpy数组操作
import cv2 as cv
import numpy as np


def access_pixels(image):
    print(image.shape)
    height = image.shape[0]
    width = image.shape[1]
    channels = image.shape[2]
    print("width : %s, height = %s, channels = %s" % (width, height, channels))
    for row in range(height):
        for col in range(width):
            for c in range(channels):
                pv = image[row, col, c]
                image[row, col, c] = 255 - pv
    cv.imshow("pixels_demo", image)


def inverse(image):
    dit = cv.bitwise_not(image)  # 像素取反
    cv.imshow("inverse image", dit)


def create_image():
    """
    img = np.zeros([400, 400, 3], np.uint8)
    img[:, :, 0] = np.ones([400, 400])*255
    cv.imshow("create_image", img)
    """
    """
    单通道图像
    """
    """
    img = np.zeros([400, 400, 1], np.uint8)
    img[:, :, 0] = np.ones([400, 400])*127
    cv.imshow("create_image", img)
    """

    m1 = np.ones([3, 4], np.uint8)
    m1.fill(122.388)
    print(m1)

    m2 = m1.reshape([4, 3])
    print(m2)


src_img = cv.imread("G:/pic/meinv.jpg")  # blue   green   red
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src_img)
start_time = cv.getTickCount()
inverse(src_img)
end_time = cv.getTickCount()
times = (end_time - start_time) / cv.getTickFrequency()
print("time : %s ms" % (times*1000))
cv.waitKey(0)
cv.destroyAllWindows()
