file = input('Введите названия файла (.txt): ')
flag = False
# string = 'SU003420'
string = 'SU001921'
# string = 'SU001430'


with open(file, 'r') as f:
    for i in f:
        if string in i:
            print('####\nНашел\n####')
            flag = True
            break

if not flag:
    print('Не найдено')
input('ENTER')
