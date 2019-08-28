# !/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:DT

import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, title="创建StaticTest类",
                          pos=(100, 100), size=(600, 400))

        panel = wx.Panel(self)   # 创建画板
        # 创建标题，设置字体
        title = wx.StaticText(panel, label='Python之禅', pos=(250, 15))
        font = wx.Font(18, wx.DEFAULT, wx.FONTSTYLE_NORMAL, wx.NORMAL)
        title.SetFont(font)
        # 创建文本
        wx.StaticText(panel, label='Beautiful is better than ugly.', pos=(50, 50))
        wx.StaticText(panel, label='Explicit is better than implicit.', pos=(50, 70))
        wx.StaticText(panel, label='Simple is better than complex.', pos=(50, 90))
        wx.StaticText(panel, label='Flat is better than nested.', pos=(50, 110))


if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame(parent=None, id=-1)
    frame.Show()
    app.MainLoop()

