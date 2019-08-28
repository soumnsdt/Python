# !/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:DT

import pygame

# 自定义按钮
class Button():
    """初始化按钮属性"""
    def __init__(self, screen, centerxy, width, height, button_color, text_color, msg, size):
        self.screen = screen
        self.width, self.height = width, height
        self.button_color = button_color
        self.text_color = text_color
        self.font = pygame.font.SysFont('SimHei', size)   # 设置文本为默认字体，字号为20
        # 设置按钮大小
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        # 设置按钮的rect对象，并设置按钮的中心位置
        self.rect.centerx = centerxy[0] - self.width/2+2
        self.rect.centery = centerxy[1] - self.height/2+2
        # 渲染图像
        self.deal_msg(msg)

    """"将msg渲染为图像，并将其在按钮上居中"""
    def deal_msg(self, msg):
        # 应用render()方法将存储在msg的文本转换为图像
        self.msg_img = self.font.render(msg, True, self.text_color, self.button_color)
        # 根据文本图像创建一个rect
        self.msg_img_rect = self.msg_img.get_rect()
        # 将该rect的center属性设置为按钮的center属性
        self.msg_img_rect.center = self.rect.center

    def draw_button(self):
        # 填充颜色
        self.screen.fill(self.button_color, self.rect)
        # 将该图像绘制到屏幕上
        self.screen.blit(self.msg_img, self.msg_img_rect)


