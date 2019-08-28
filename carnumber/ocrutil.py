# !/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:DT


from aip import AipOcr
import os

filename = 'file/key.txt'  # 记录申请的Key的文件位置
if os.path.exists(filename):
    with open(filename, 'r', encoding='UTF-8') as file:
        dictkey = eval(file.readlines()[0])   # 读取全部内容转换为字典
        APP_ID = dictkey['APP_ID']
        API_KEY = dictkey['API_KEY']
        SECRET_KEY = dictkey['SECRET_KEY']
else:
    print("key错误！！！")


# 初始化AipOcr对象
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
# 读取文件
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


# 根据图片返回车牌号,识别车牌
def getcn():
    # 读取图片
    image = get_file_content('file/test.jpg')
    # 调用车牌识别
    results = client.licensePlate(image)["words_result"]['number']
    # 输出车牌号
    print(results)
    return results

