'''
字符串操作
'''
name = "\ttaobao"
name1 = "i am {age} years old.my name is {names}."

print(name.capitalize())   # 首字母大写


print(name.count("t"))   # 统计"t"个数

print(name.center(50, "-"))   # 首字母大写

print(name.encode())   # 转成2进制

print(name.endswith("ao"))   # 判断字符串以什么结尾

print(name.expandtabs(tabsize=30))   # 首字母大写

print(name.find("\t"))   # 首字母大写

print(name1.format(age = 23, names = "soumns"))   # 首字母大写

print(name1.format_map({'age':'23','names ':'soumns'}))   # 首字母大写