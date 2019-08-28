# !/usr/bin/python
# -*- coding:UTF-8 -*-
# Author:DT

import pygame
import cv2
from pandas import DataFrame
import os
import btn
import ocrutil

'''显示摄像头画面'''
def device():
    try:
        cam = cv2.VideoCapture(0)   # 创建摄像头实例
    except:
        print('请链接摄像头')
    # 从摄像头读取图片
    sucess, img = cam.read()
    # 保存图片并退出
    cv2.imwrite('file/test.jpg', img)
    # 加载图像
    image = pygame.image.load('file/test.jpg')
    # 设置图片大小
    image = pygame.transform.scale(image, (640, 480))
    # 绘制视频画面
    screen.blit(image, (2, 2))


'''创建保存数据文件'''
def create_save_file():
    # 获取文件的路径
    cdir = os.getcwd()
    # 文件路径
    path = cdir+'/datafile/'
    # 读取路径
    if not os.path.exists(path+'停车场车辆表.xlsx'):
        # 根据路径建立文件夹
        os.makedirs(path)
        # 车牌号、日期、时间、价格、状态
        carnfile = DataFrame(columns=['carnumber', 'data', 'price', 'state'])
        # 生成.xlsx文件
        carnfile.to_excel(path+'停车场车辆表.xlsx', sheet_name='data')
        carnfile.to_excel(path + '停车场信息表.xlsx', sheet_name='data')

# 窗体大小
size = 1000, 484
# 设置帧率（帧率就是每秒显示的帧数）
FPS = 60
# 定义背景颜色
DARKBLUE = (73, 119, 142)
BG = DARKBLUE   # 指定背景颜色
# 初始化pygame
pygame.init()
# 设置窗体名称
pygame.display.set_caption('智能停车场车牌识别计费系统'.encode(encoding="gbk").decode(encoding="gbk"))
# 图标
ic_launcher = pygame.image.load('file/ic_launcher.png')
# 设置图标
pygame.display.set_icon(ic_launcher)
# 设置窗体大小
screen = pygame.display.set_mode(size)
# 设置背景颜色
screen.fill(BG)
# 游戏循环帧率设置
clock = pygame.time.Clock()


"""button"""
# 定义颜色
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (72, 61, 139)
GRAY = (96, 96, 96)
RED = (220, 20, 60)
YELLOW = (255, 255, 0)


# 主线程
Running = True
while Running:
    # 创建识别按钮
    button_go = btn.Button(screen, (640, 480), 150, 60, BLUE, WHITE, "识别", 25)
    # 绘制创建的按钮
    button_go.draw_button()

    device()
    create_save_file()
    # print(os.getcwd()+'/datafile/')

    for event in pygame.event.get():
        # 关闭页面游戏退出
        if event.type == pygame.QUIT:
            # 退出
            pygame.quit()
            exit()
            # 识别按钮
            if 492 <= event.pos[0] and event.pos[0] <= 642 and 422 <= event.pos[1] and event.pos[1] <= 482:
                print('点击识别')
                try:
                    # 获取车牌
                    carnumber = ocrutil.getcn()
                except:
                    print('识别错误')
                    continue
                pass

    # 更新界面
    pygame.display.flip()
    # 控制游戏最大帧率为60
    clock.tick(FPS)
















