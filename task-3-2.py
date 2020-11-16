# решение через список

my_list = ['зима', 'зима', 'весна', 'весна', 'весна', 'лето', 'лето', 'лето', 'осень', 'осень', 'осень', 'зима']
a = int(input('Введите номер месяца: '))
print(my_list[a-1])

# можно по-другому

new_list = ['зима', 'весна', 'лето', 'осень']
month = int(input('Введите номер месяца: '))
if month == 0 or month == 1 or month == 2:
    print(new_list[0])
elif month == 3 or month == 4 or month == 5:
    print(new_list[1])
elif month == 6 or month == 7 or month == 8:
    print(new_list[2])
else:
    print(new_list[3])
    