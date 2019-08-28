# !/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:DT

import xlwt

# 新建一个工作簿
new_workbook = xlwt.Workbook()

# 新建一个工作表
worksheet = new_workbook.add_sheet('new_test')   # 表名不写的话，默认是“sheet1”

# 在工作表的单元格中写入数据
worksheet.write(0, 0, '你好')

# 保存工作簿
new_workbook.save('G:/test02.xls')


