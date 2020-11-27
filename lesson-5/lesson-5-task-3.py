with open('workers.txt', 'r') as f_obj:
    count = 0
    summ_ = 0
    text = f_obj.read()
    my_list = text.split()
    print(my_list)
    for item in range(0, len(my_list)):
        if not my_list[item].isdigit():
            count += 1
        else:
            my_list[item] = int(my_list[item])
            summ_ += my_list[item]
            if my_list[item] <= 20000:
                print(f'{my_list[item - 1]} зарабатывает меньше 20 000')
    average = summ_ / count
    print(f'Средний доход сотрудников равен {average}')
    