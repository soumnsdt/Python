# /usr/bin/env python
# -*- coding:utf-8 -*-

"""
Author: DT
Blog: https://www.cnblogs.com/DT-BK/
GitHub: https://github.com/soumnsdt?tab=repositories

date: 2019/9/1 20:21
desc: 
"""

import requests


# get请求方式
response = requests.get('http://www.baidu.com/')
print(response.status_code)         # 打印状态码
print(response.url)                 # 打印请求url
print(response.headers)             # 头部信息
print(response.cookies)             # cookie信息
print(response.text)                # 以文本形式打印网页源码
print(response.content)             # 以字节流形式打印网页源码