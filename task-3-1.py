# решение через dict

my_dict = {'Зима': (1, 2, 12),
           'Весна': (3, 4, 5),
           'Лето': (6, 7, 8),
           'Осень': (9, 10, 11)}
a = int(input('Введите номер месяца: '))
for i in my_dict.keys():
    if a in my_dict[i]:
        print(i)
