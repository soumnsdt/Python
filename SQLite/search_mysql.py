# !/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:DT

import sqlite3

conn = sqlite3.connect('my_sql.db')


# 创建cursor
cursor = conn.cursor()
# 执行查询语句
# cursor.execute('select * from user')
# cursor.execute('insert into user(id, name) values ("4", "my_love" )')  # 增
# cursor.execute('update user set name = ? where id = ?', ('dt_gy', 4))  # 改
cursor.execute('delete from user where id > ?', (2,))  # 删
cursor.execute('select * from user where id > ?', (0,))    # 查
# 获取查询结果
result1 = cursor.fetchall()
print(result1)

# 关闭游标
cursor.close()
# 提交事务
conn.commit()
# 关闭连接
conn.close()

