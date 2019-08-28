# # 打印系统的默认编码
# print(-80 >> 3)
# coding=Unicode

height = float(input('请输入您的身高(m)：'))
weight = float(input('请输入您的体重(kg):'))
BMI = weight/(height*height)
print('您的BMI指数为：%s'%(BMI))
if BMI<18.5:
	print('太瘦了')
elif 18.5<= BMI <24.9:
	print('正常，保持')
elif 24.9 <= BMI < 29.9:
	print('微胖')
else:
	print('死肥猪，赶紧锻炼去！！！')


