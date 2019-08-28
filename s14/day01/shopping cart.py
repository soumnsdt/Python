import time

goods_list = [("iphone", 5800), ("coffee", 38), ("car", 50000), ("bag", 200)]
shopping_cart_list = []

salary = input("Please input your salary:")
if salary.isdigit():  # 判断salary是数字
	salary = int(salary)

	while True:
		print("All goods below:")
		# for items in goods_list:
		# 	print(goods_list.index(items), items)
		for index, items in enumerate(goods_list):
			print(index + 1, items)
		user_choice = input("What do you want yo buy? >>>:")
		if user_choice.isdigit():
			user_choice = int(user_choice)
			if user_choice <= len(goods_list) and user_choice > 0:
				# p_item 选择商品的下标 ("iphone",5800)
				p_item = goods_list[user_choice-1]
				if p_item[1] <= salary:  # 买的起
					shopping_cart_list.append(p_item)
					salary -= p_item[1]
					print("Added %s into shopping cart,your current balance is $%s" % (p_item, salary))
				else:
					print("your current balance is $%s only.Cannot afford it!" %(salary) )
			else:
				print("you input goods code %d is not exist!\n" % (user_choice))
		elif user_choice == 'q':
			print("========== shopping list ==========")
			for p in shopping_cart_list:
				print(p)
			print("Your current balance: $%s" %(salary))
			print("5s later exit...")
			time.sleep(5)
			exit()
		else:
			print("Invalid option.")
else:
	print("your input salary error!!! 5s later exit...")
	time.sleep(5)
			
		