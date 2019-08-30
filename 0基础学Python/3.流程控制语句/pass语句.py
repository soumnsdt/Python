# /usr/bin/env python
# -*- coding:utf-8 -*-

"""
Author: DT
Blog: https://www.cnblogs.com/DT-BK/
GitHub: https://github.com/soumnsdt?tab=repositories

date: 2019/8/30 21:20
desc: pass语句，表示空语句，一般起到占位的作用
"""

# 例子：用for循环输出1~10（不包括10）之间的偶数，不是偶数时，应用pass语句占位，
# 方便以后对不是偶数的数进行处理

for number in range(1, 10):
    if number % 2 == 0:
        print(number)
    else:
        pass
