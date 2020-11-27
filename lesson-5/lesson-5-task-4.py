with open('task-4.txt', 'r', encoding="UTF-8") as f_obj:
    new_obj = open('task-4-2.txt', 'w', encoding='UTF-8')
    for i in range(1, 5):
        new_string = f_obj.readline()
        new_string = new_string.replace('One', 'Один')
        new_string = new_string.replace('Two', 'Два')
        new_string = new_string.replace('Three', 'Три')
        new_string = new_string.replace('Four', 'Четыре')
        new_obj.write(new_string)
    new_obj.close()
