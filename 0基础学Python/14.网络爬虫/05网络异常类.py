# /usr/bin/env python
# -*- coding:utf-8 -*-

"""
Author: DT
Blog: https://www.cnblogs.com/DT-BK/
GitHub: https://github.com/soumnsdt?tab=repositories

date: 2019/9/1 20:53
desc: requests模块提供了3种常见的网络异常类
"""
import requests
# 导入requests.exceptions模块中的3中异常类
from requests.exceptions import ReadTimeout,HTTPError,RequestException


for i in range(50):
    try:
        response = requests.get('https://github.com/soumnsdt?tab=repositories', timeout=3)
        print(response.status_code)
    except ReadTimeout:         # 超时异常
        print('timeout')
    except HTTPError:           # HTTP异常
        print('http_error')
    except RequestException:    # 请求异常
        print('req_error')

