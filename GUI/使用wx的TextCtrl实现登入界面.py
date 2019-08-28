# !/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:DT

import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, title='创建TextCtrl类',
                          size=(400, 300))
        # 创建面板
        panel = wx.Panel(self)
        # 创建文本和输入框
        # 创建文本 wx.StaticText
        self.title = wx.StaticText(panel, label='请输入用户名和密码', pos=(140, 20))
        self.label_user = wx.StaticText(panel, label='用户名', pos=(50, 53))
        # 创建输入框 wx.TextCtrl
        self.text_user = wx.TextCtrl(panel, pos=(100, 50), size=(235, 25),
                                     style=wx.TE_LEFT)
        self.label_pwd = wx.StaticText(panel, label='密   码', pos=(50, 93))
        self.text_pwd = wx.TextCtrl(panel, pos=(100, 90), size=(235, 25),
                                    style=wx.TE_PASSWORD)

        # 创建按钮
        self.btn_confirm = wx.Button(panel, label='登入', pos=(235, 130))
        self.btn_cancel = wx.Button(panel, label='取消', pos=(105, 130))


if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame(parent=None, id=-1)
    frame.Show()
    app.MainLoop()
