# !/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:DT

import sqlite3

conn = sqlite3.connect('my_sql.db')

# 创建一个Cursor
Cursor = conn.cursor()
Cursor.execute('create table user(id int(10) primary key, name varchar(20))')
Cursor.execute('insert into user(id, name) values ("1", "dt")')
Cursor.execute('insert into user(id, name) values ("2", "gy")')
Cursor.execute('insert into user(id, name) values ("3", "wyx")')

Cursor.close()
conn.commit()
conn.close()

