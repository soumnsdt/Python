# /usr/bin/env python
# -*- coding:utf-8 -*-

"""
Author: DT
Blog: https://www.cnblogs.com/DT-BK/
GitHub: https://github.com/soumnsdt?tab=repositories

date: 2019/9/1 21:10
desc: 在爬取网页的过程中，经常出现不久前可以爬取的网页现在不可以爬取了，
      原因是：您的IP被爬取网站的服务器屏蔽了。此时，代理服务可以解决。
"""

import requests

proxy = {'http': '122.114.31.177:808',
         'https': '122.114.31.177:8080'}

response = requests.get('http://www.mingrisoft.com', proxies=proxy)
print(response.content)

