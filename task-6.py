
my_list = []
n = int(input('Введите количество товара: '))
count = 1
my_dict = []
name = []
price = []
quantity = []
edin = []
my_analys = {'название': name, 'цена': price, 'количество': quantity, 'ед': edin}
while count <= n:
    my_dict = {'название': input('Введите название товара: '), 'цена': int(input('Введите цену: ')),
                    'количество': int(input('Введите количество: ')), 'ед': input('Введите единицы измерения: ')}
    my_list.append((count, my_dict))
    count += 1
    name.append(my_dict.get('название'))
    price.append(my_dict.get('цена'))
    quantity.append(my_dict.get("количество"))
    edin.append(my_dict.get('ед'))
edin = list(set(edin))
print(my_list)
print(my_analys)