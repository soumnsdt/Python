def list_of_groups(init_list, children_list_len):
    list_of_groups = zip(*(iter(init_list),) *children_list_len)
    end_list = [list(i) for i in list_of_groups]
    count = len(init_list) % children_list_len
    end_list.append(init_list[-count:]) if count !=0 else end_list
    return end_list


f = open("abc.txt",encoding = "utf-8")
firstling_data = f.readlines()
print("firstling_data:",firstling_data)
# print("==========================================")
# data = f.read()
# print(data)
split_data = firstling_data.split("\n")
print(split_data)