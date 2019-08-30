# /usr/bin/env python
# -*- coding:utf-8 -*-

"""
Author: DT
Blog: https://www.cnblogs.com/DT-BK/
GitHub: https://github.com/soumnsdt?tab=repositories

date: 2019/8/30 19:57
desc:
"""


####################
# 1、break语句
####################
print("被3除余2，被5除余3，被7除余2，请问这个数是多少？")
for number in range(100):
    print(number)
    if number % 3 == 2 and number % 5 == 3 and number % 7 == 2:
        print(str(number) + '是答案')
        break   # 思考不加break和加break的区别


print("分隔符".center(50, "="))
####################
# 2、continue语句
####################
# 试计算1~100（不包含100），一共有多少个尾数为7或7的倍数的数？
point = 0
for number in range(1, 100):
    if number % 7 == 0:
        point += 1
        continue
    else:
        str_number = str(number)
        if str_number.endswith('7'):
            point += 1
            continue
print("1~100（不包含100）中,一共有%d个尾数为7或7的倍数的数." % point)
