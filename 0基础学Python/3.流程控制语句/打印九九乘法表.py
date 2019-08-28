# !/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:DT

for i in range(1, 10):     # 行
    for j in range(1, i + 1):     # 列
        print(str(i) + "*" + str(j) + "=" + str(i*j) + "\t", end="")
    print("")

