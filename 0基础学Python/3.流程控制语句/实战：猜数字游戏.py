# /usr/bin/env python
# -*- coding:utf-8 -*-

"""
Author: DT
Blog: https://www.cnblogs.com/DT-BK/
GitHub: https://github.com/soumnsdt?tab=repositories

date: 2019/8/30 21:39
desc: 编写一个猜数字的小游戏，随机生成一个1~10之间的数（包括1和10）作为基准数，
      玩家每次通过键盘输入一个数，如果输入的数和基准数相同，则通关成功，
      并打印猜了几次，否则重新输入。如果玩家输入-1，则表示退出游戏。
"""

import random    # 用于生成随机数的库


start_str = "猜数字游戏"
end_str = "游戏结束"
guess_times = 0    # 猜测的次数
start_num = 1      # 随机数最小值
end_num = 100      # 随机数最大值

print(start_str.center(50, "-"))
random_number = random.randint(start_num, end_num)  # 随机生成一个1~100（包括1和100）的整数
# print(random_number)
number = int(input("请输入1~100之间的任意一个整数："))
while True:
    if number == random_number:
        guess_times += 1
        print("恭喜你，你赢了，总共猜测了%d次，猜中的数字是%d" % (guess_times, number))
        break
    elif 0 < number < random_number:
        guess_times += 1
        number = int(input("太小，请重新输入："))
        continue
    elif random_number < number < 101:
        guess_times += 1
        number = int(input("太大，请重新输入："))
        continue
    elif number == -1:
        break
    else:
        number = int(input("输入错误，请输入1~100之间的任意一个整数："))
        continue

print(end_str.center(50, '-'))
