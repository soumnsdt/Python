# !/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:DT

import getpass   # 密文

_username = 'dt'
_password = '123'

for i in range(3):
	username = input("username:")
	password = getpass.getpass("password:")

	if username == _username and password == _password:
	    print("Welcome user {name} login...".format(name=username))
	    break
	else:
	    print("Invalid username or password!")


