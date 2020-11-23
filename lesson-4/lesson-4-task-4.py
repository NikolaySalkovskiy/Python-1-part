my_list = [2, 2, 2, 11, 23, 23, 42, 50, 11, 12, 1]
new_list = [el for el in my_list if my_list.count(el) == 1]
print(new_list)