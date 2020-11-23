from itertools import count, cycle

#первый итератор
def my_numbers():
    for el in count(3):
        if el > 10:
            break
        else:
            print(el)


my_numbers()

# пропуск строки
print()

my_list = [1, 'geekbrains', 12]

#второй итератор
def my_cycle(arg_1):
    c = 0
    for el in cycle(arg_1):
        if c > 10:
            break
        else:
            print(el)
        c += 1


my_cycle(my_list)
