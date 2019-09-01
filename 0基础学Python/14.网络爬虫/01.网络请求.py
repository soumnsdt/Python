# /usr/bin/env python
# -*- coding:utf-8 -*-

"""
Author: DT
Blog: https://www.cnblogs.com/DT-BK/
GitHub: https://github.com/soumnsdt?tab=repositories

date: 2019/9/1 19:50
desc:
"""
####################
# 1、urllib模块
####################

import urllib.request             # 导入模块
import urllib3            # 导入模块


# # 打开指定需要爬取的页面
# response = urllib.request.urlopen('http://www.baidu.com')

# 将数据使用urlencode编码处理后，在使用encoding设置为utf-8编码
data = bytes(urllib.parse.urlencode({'word': 'hello'}), encoding='utf-8')
# 打开指定需要爬取的页面
response = urllib.request.urlopen('http://httpbin.org/post', data=data)

# 读取页面代码
html = response.read()
# 打印读取内容
print(html)


####################
# 2、urllib3模块
####################



http = urllib3.PoolManager()
# response = http.request('GET', 'http://www.baidu.com/')
response = http.request('POST', 'http://www.baidu.com/', fields={'word': 'hello'})
print(response.data)
