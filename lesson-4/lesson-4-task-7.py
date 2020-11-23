
# factorial

def factorial(arg_1):
    fact = 1
    for i in range(1, arg_1 + 1):
        fact *= i
        yield fact


number = int(input('Введите целое число: '))
for el in factorial(number):
    print(el)
