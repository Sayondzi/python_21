'''
 Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом —
 данные об их хобби.
 Известно, что при хранении данных используется принцип:
 одна строка — один пользователь, разделитель между значениями — запятая.
 Написать код, загружающий данные из обоих файлов и формирующий из них словарь:
 ключи — ФИО, значения — данные о хобби.
 Сохранить словарь в файл.
 Проверить сохранённые данные. Если в файле, хранящем данные о хобби, меньше записей,
 чем в файле с ФИО, задаём в словаре значение None.
 Если наоборот — выходим из скрипта с кодом «1».
 При решении задачи считать, что объём данных в файлах во много раз меньше объема ОЗУ.

Фрагмент файла с данными о пользователях (users.csv):
     Иванов,Иван,Иванович
     Петров,Петр,Петрович
Фрагмент файла с данными о хобби (hobby.csv):
     скалолазание,охота
     горные лыжи
'''

import sys
'''
# Создание файла данных имён
with open('users.csv', 'w', encoding='utf-8') as f:
    print('Иванов,Иван,Иванович', file=f)
    print('Петров,Петр,Петрович', file=f)
    print('Васильев,Виктор,Вениаминович', file=f)
# Создание файла данных хобби
with open('hobby.csv', 'w', encoding='utf-8') as f_2:
    print('скалолазание,охота', file=f_2)
    print('горные лыжи', file=f_2)
#    print('велоспорт', file=f_2) # проверка работоспособности при равных компонентах данных
#    print('шахматы', file=f_2) # проверка работоспособности в случае, если хобби больше  участников
'''
content = []
content_1 = []
result = {}
i = 0
with open('users.csv', 'r', encoding='utf-8') as f:
    with open('hobby.csv', 'r', encoding='utf-8') as f_2:
        for el in f.read().split('\n'):
            if el == '':
                break
            a = ' '.join(el.split(','))
            content.append(a)

        for el_1 in f_2.read().split('\n'):
            if el_1 == '':
                break
            a_1 = el_1.split(',')
            content_1.append(a_1)

if len(content_1) > len(content):
    with open('users_hobby.txt', 'w', encoding='utf-8') as f_3:
        print('', file=f_3)
    sys.exit(1)
for i in range(len(content)):
    if i >= len(content_1):
        result[content[i]] = None
    else:
        result[content[i]] = content_1[i]

with open('users_hobby.txt', 'w', encoding='utf-8') as f_3:
    print(result, file=f_3)
