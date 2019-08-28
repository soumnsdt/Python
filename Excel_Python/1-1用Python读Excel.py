# !/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:DT

import xlrd

xlsx = xlrd.open_workbook('G:/test02.xls')  # 打开我们的工作簿

table = xlsx.sheet_by_index(0)
# table = xlsx.sheet_by_name('sheet1')

print(table.cell_value(0, 0))






# print(table.cell(1, 1).value)

# print(table.row(1)[1].value)