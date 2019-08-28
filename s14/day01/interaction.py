# !/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:DT

name = (input("name:"))
age = int(input("age:"))
print(type(age))
job = (input("job:"))
salary = (input("salary:"))


info = '''
-------- info of %s --------
Name:%s
Age:%d
Job:%s
Salary:%s
''' % (name, name, age, job, salary)

print(info)

info2 = '''
-------- info of %s --------
Name:%s
Age:%d
Job:%s
Salary:%s
''' % (name, name, age, job, salary)

print(info2)

