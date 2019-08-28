# !/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:DT

import wx
import time

class MyFrame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, title='我有很多话想对你说',
                          size=(400, 300))
        # 创建面板
        panel = wx.Panel(self)
        # 创建文本和输入框
        # 创建文本 wx.StaticText
        self.title = wx.StaticText(panel, label='请输入我的姓名和名字全拼')
        self.label_user = wx.StaticText(panel, label='我的姓名')
        # 创建输入框 wx.TextCtrl
        self.text_user = wx.TextCtrl(panel, size=(235, 25), style=wx.TE_LEFT)
        self.label_pwd = wx.StaticText(panel, label='名字全拼')
        self.text_pwd = wx.TextCtrl(panel, size=(235, 25), style=wx.TE_PASSWORD)

        # 创建按钮
        self.btn_confirm = wx.Button(panel, label='登入')
        self.btn_cancel = wx.Button(panel, label='取消')
        # 按钮绑定事件
        self.btn_confirm.Bind(wx.EVT_BUTTON, self.OnClickSubmit)
        self.btn_cancel.Bind(wx.EVT_BUTTON, self.OnClickCancel)



        # 添加容器，容器中控件横向排列
        hsizer_user = wx.BoxSizer(wx.HORIZONTAL)
        hsizer_user.Add(self.label_user, proportion=0, flag=wx.ALL, border=5)
        hsizer_user.Add(self.text_user, proportion=0, flag=wx.ALL, border=5)

        hsizer_pwd = wx.BoxSizer(wx.HORIZONTAL)
        hsizer_pwd.Add(self.label_pwd, proportion=0, flag=wx.ALL, border=5)
        hsizer_pwd.Add(self.text_pwd, proportion=1, flag=wx.ALL, border=5)

        hsizer_btn = wx.BoxSizer(wx.HORIZONTAL)
        hsizer_btn.Add(self.btn_cancel, proportion=0, flag=wx.ALL, border=5)
        hsizer_btn.Add(self.btn_confirm, proportion=1, flag=wx.ALL, border=5)



        # 添加容器，容器中控件按纵向排列
        vsizer_all = wx.BoxSizer(wx.VERTICAL)
        vsizer_all.Add(self.title, proportion=0, flag=wx.BOTTOM | wx.TOP | wx.ALIGN_CENTER,
                       border=15)
        vsizer_all.Add(hsizer_user, proportion=0, flag=wx.EXPAND | wx.LEFT | wx.RIGHT,
                       border=45)
        vsizer_all.Add(hsizer_pwd, proportion=0, flag=wx.EXPAND | wx.LEFT | wx.RIGHT,
                       border=45)
        vsizer_all.Add(hsizer_btn, proportion=0, flag=wx.ALIGN_CENTER | wx.TOP,
                       border=20)

        panel.SetSizer(vsizer_all)


    """ 单击登入按钮，执行方法"""
    def OnClickSubmit(self, event):
        message = ""
        username = self.text_user.GetValue().strip()     # 获取输入的用户名
        password = self.text_pwd.GetValue()      # 获取输入的密码
        if username == "" or password == "":     # 判断输入的密码是否为空
            message = "我的名字和全拼都不能为空哦！！！"
        elif username == "丁涛" and password == "dingtao":
            message = "其实我想对你说：我喜欢你，能做我女朋友吗？"
        else:
            message = "你不爱我了，我的名字你都能打错"
        wx.MessageBox(message)
        pass

    """单击取消按钮，执行方法"""
    def OnClickCancel(self, event):
        self.text_user.SetValue("")    # 清空输入的用户名
        self.text_pwd.SetValue("")     # 清空输入的密码
        wx.MessageBox("点击OK，3s后会退出程序。。。")
        time.sleep(3)
        wx.MessageBox("哈哈被骗到了吧！你需要手动×掉程序！")
        pass


if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame(parent=None, id=-1)
    frame.Show()
    app.MainLoop()
