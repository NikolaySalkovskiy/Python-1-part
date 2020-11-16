
my_list = [8, 5, 4, 4, 3, 2]
print(my_list)
number = int(input('Введите ваш рейтинг: '))
count = 0
for i in my_list:
    if number > i:
        list.insert(count, number)
        break
    count += 1
if number not in my_list:
    my_list.append(number)

print('Ваш новый рейтинг:')
print(my_list)