# /usr/bin/env python
# -*- coding:utf-8 -*-

"""
Author: DT
Blog: https://www.cnblogs.com/DT-BK/
GitHub: https://github.com/soumnsdt?tab=repositories

date: 2019/9/3 19:39
desc: 通过Beautiful Soup库进行HTML的解析
"""
from bs4 import BeautifulSoup       # 导入Beautiful Soup库

# 创建模拟HTML代码的字符串
html_doc = """
<html>
<head>
    <meta http-equiv="content-type" content="text/html;charset=utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=Edge">
	<meta content="always" name="referrer">
    <meta name="theme-color" content="#2932e1">
    <link rel="shortcut icon" href="/favicon.ico" type="image/x-icon" />
    <link rel="search" type="application/opensearchdescription+xml" href="/content-search.xml" title="百度搜索" />
    <link rel="icon" sizes="any" mask href="//www.baidu.com/img/baidu_85beaf5496f291521eb75ba38eacbd87.svg">
	
	
	<link rel="dns-prefetch" href="//s1.bdstatic.com"/>
	<link rel="dns-prefetch" href="//t1.baidu.com"/>
	<link rel="dns-prefetch" href="//t2.baidu.com"/>
	<link rel="dns-prefetch" href="//t3.baidu.com"/>
	<link rel="dns-prefetch" href="//t10.baidu.com"/>
	<link rel="dns-prefetch" href="//t11.baidu.com"/>
	<link rel="dns-prefetch" href="//t12.baidu.com"/>
	<link rel="dns-prefetch" href="//b1.bdstatic.com"/>
    
    <title>百度一下，你就知道</title>
</head>
</html>
"""

# # 创建一个Beautiful Soup对象，获取页面正文
# soup = BeautifulSoup(html_doc, features="lxml")
# # 打印解析的HTML代码
# print(soup.prettify())


# 创建Beautiful Soup对象打开需要解析的html文件
soup = BeautifulSoup(open('index.html', encoding='utf-8'), 'lxml')
# 打印格式化后的代码
print(soup.prettify())
