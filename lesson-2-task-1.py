a = float(input('Введите делимое: '))
b = float(input('Введите делитель: '))

def my_func(p_1, p_2):
    return p_1 / p_2

try:
    print(my_func(a, b))
except ZeroDivisionError:
    print('На ноль делить нельзя')
