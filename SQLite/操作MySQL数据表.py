# !/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:DT

import pymysql

db = pymysql.connect("localhost", "root", "19950716dt", "mrsoft")

cursor = db.cursor()
data = [("0基础学Python", 'Python', '79.8', '2018-5-20'),
        ("Python从入门到精通", 'Python', '69.8', '2018-6-18'),
        ("0基础学PHP", 'PHP', '79.8', '2017-5-21'),
        ("0基础学JAVA", 'JAVA', '69.8', '2017-5-21'),
        ("Python项目开发集锦", 'Python', '128', '2019-3-20'),
        ]
try:
    cursor.executemany("insert into books(name, category, price, publish_time) values (%s,%s,%s,%s)", data)
    # 提交数据
    db.commit()
except:
    # 发生错误时回滚
    db.rollback()

# 关闭数据库
db.close()

