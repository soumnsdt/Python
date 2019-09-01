# /usr/bin/env python
# -*- coding:utf-8 -*-

"""
Author: DT
Blog: https://www.cnblogs.com/DT-BK/
GitHub: https://github.com/soumnsdt?tab=repositories

date: 2019/9/1 20:45
desc: 
"""

import requests

for i in range(50):
    try:
        # 设置超时0.5s
        response = requests.get('http://www.baidu.com/', timeout=0.02)
        print(response.status_code)
    except Exception as e:
        print('异常'+str(e))

