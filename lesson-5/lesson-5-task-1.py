with open("task-1.txt", 'w', encoding='UTF-8') as f_obj:
    while True:
        string = input('Введите строку, нажмите Enter, чтобы выйти: ')
        if string == '':
            break
        else:
            f_obj.writelines(string)
            print(file=f_obj)
