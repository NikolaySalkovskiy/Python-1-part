
phrase = input('Введите предложение: ').split()
count = 1
for i in phrase:
    if len(i) <= 10:
        print(f'{count}) {i}')
    else:
        print(f'{count}) {i[:10]}')
    count += 1