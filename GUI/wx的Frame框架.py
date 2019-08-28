# !/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:DT

import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, title="创建Frame", pos=(100, 100),
                          size=(600, 400))

if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame(parent=None, id=-1)
    frame.Show()
    app.MainLoop()

