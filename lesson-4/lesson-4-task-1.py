from sys import argv

def salary(arg_1, arg_2, arg_3):
    return (arg_1 * arg_2) + arg_3


_, hours, money_per_hour, prize = argv
print(salary(int(hours), int(money_per_hour), int(prize)))
