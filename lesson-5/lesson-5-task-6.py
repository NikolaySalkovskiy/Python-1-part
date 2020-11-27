with open('task-6.txt', 'r', encoding='UTF-8') as f_obj:
    my_dict = {}
    content = f_obj.readlines()
    for i in range(len(content)):
        s = content[i].split()
        subject = s[0].rstrip(':')
        lectures = s[1].rstrip('—(л)')
        practices = s[2].rstrip('—(пр)')
        lab = s[3].rstrip('—()лаб.')
        if lectures == '': lectures = '0'
        if practices == '': practices = '0'
        if lab == '': lab = '0'
        summ = int(lectures) + int(practices) + int(lab)
        my_dict[subject] = summ

    print(my_dict)
