# !/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:DT


import pymysql

# 1、打开数据库连接，
'''
    参数1：主机名或IP
    参数2：用户名
    参数3：密码
    参数4：数据库名称
'''
db = pymysql.connect("localhost", "root", "19950716dt", "mrsoft")
# 2、使用cursor()创建一个游标对象cursor
cursor = db.cursor()
# 3、使用execute()执行SQL语句
cursor.execute("SELECT VERSION()")
# 4、使用fetchone()获取单条数据
data = cursor.fetchone()

print("Database version is: %s" % data)

# 5、关闭数据库
db.close()
