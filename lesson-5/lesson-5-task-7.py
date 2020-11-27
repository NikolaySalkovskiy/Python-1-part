import json

with open('task-7.txt', 'r') as f_obj:
    income_dict = {}
    itog_list = []
    average_dict = {}
    total = 0
    count = 0
    for item in f_obj.readlines():
        new_list = item.split()
        profit = int(new_list[2]) - int(new_list[3])
        income_dict[new_list[0]] = profit

        #Считаем только положительную прибыль в среднем значении

        if profit >= 0:
            total += profit
            count += 1
    itog_list.append(income_dict)
    average_dict['average profit'] = round((total / count), 2)
    itog_list.append(average_dict)

with open('task-7.json', 'w') as json_file:
    json.dump(itog_list, json_file)
