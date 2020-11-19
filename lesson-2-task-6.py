def int_func(arg):
    a = arg.title()
    return a


word = input('Введите слово или предложение: ')
print(int_func(word))