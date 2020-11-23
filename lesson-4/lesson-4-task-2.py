my_list = [112, 10, 6, 12, 4, 100, 65, 80, 100, 11]

new_list =[my_list[el] for el in range(1, len(my_list)) if my_list[el] > my_list[el-1]]

print(new_list)
