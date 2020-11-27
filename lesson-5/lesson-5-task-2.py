with open('task-2.txt') as f_obj:
    count_str = 0
    count_word = 0
    for line in f_obj:
        for word in line.split():
            count_word += 1
        count_str += 1
        print(f'На {count_str} строке {count_word} слов')
        count_word = 0
    print(f'В файле {count_str} строк')
