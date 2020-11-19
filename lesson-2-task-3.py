def my_func(p_1, p_2, p_3):
    if p_1 < p_2:
        p_1, p_2 = p_2, p_1
    if p_2 < p_3:
        p_2, p_3 = p_3, p_2
    return p_1 + p_2


a = float(input('Введите первое число: '))
b = float(input('Введите второе число: '))
c = float(input('Введите третье число: '))

print(f'Сумма двух наибольших чисел = {my_func(a, b, c)}')
