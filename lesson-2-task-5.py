summ = 0
stop_while = False
while not stop_while:
    my_list = input('Введите числа, разделенные пробелами: ').split()
    for i in range(len(my_list)):
        try:
            my_list[i] = float(my_list[i])
            summ += my_list[i]
        except BaseException:
            print('Вы ввели не число')
            stop_while = True
            break
    print(f'Сумма: {summ}')

