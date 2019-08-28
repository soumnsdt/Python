list_1 = [1,4,5,7,3,6,7,9]
list_1 = set(list_1)   # 去重

list_2 = set([2,6,0,66,22,8,4])
list_3 = set([1,3,7])
list_4 = set([5,6,8])

# 集合也是无序的
print(list_1,type(list_1))
print(list_1,list_2)


# 交集
print(list_1.intersection(list_2))

# 并集
print(list_1.union(list_2))

# 差集  in list_1 but not in list_2
print(list_1.difference(list_2))


# 子集
print(list_1.issubset(list_2))

# 父集
print(list_1.issuperset(list_2))


# 对称差集    并集-差集
print(list_1.symmetric_difference(list_2))



print("=============================")
print(list_3.isdisjoint(list_4))   # 没有交集就返回Ture，否则就返回False















