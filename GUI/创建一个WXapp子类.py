# !/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:DT

import wx

class App(wx.App):
    # 初始化方法
    def OnInit(self):
        frame = wx.Frame(parent=None, title='Hello wxPython')    # 创建窗口
        frame.Show()  # 显示窗口
        return True

if __name__ == '__main__':
    app = App()
    app.MainLoop()

