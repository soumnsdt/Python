# !/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:DT

import getpass   # 密文

_username = 'dt'
_password = '123'

username = input("username:")
# password = getpass.getpass("password:")
password = input("password:")

if username == _username and password == _password:
    print("Welcome user {name} login...".format(name=username))
else:
    print("Invalid username or password!")


