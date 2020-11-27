with open('task-5.txt', 'w') as f_obj:
    number = input('Введите строку чисел: ')
    f_obj.write(number)

with open('task-5.txt', 'r') as file_summ:
    itog = 0
    string = file_summ.readline()
    my_list = string.split()
    for item in my_list:
        if item.isdigit():
            item = int(item)
            itog += item
        else:
            continue
    print(itog)
