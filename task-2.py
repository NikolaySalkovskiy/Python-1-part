
my_list = []
n = int(input('Введите количество элементов списка: '))
for i in range(n):
    new_element = input('Введите элемент списка: ')
    my_list.append(new_element)

for item in range(1, n, 2):
    my_list[item], my_list[item - 1] = my_list[item - 1], my_list[item]
print(my_list)
