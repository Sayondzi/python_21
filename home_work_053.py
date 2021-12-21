'''
Есть два списка:
#     tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
#     klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']
Необходимо реализовать генератор, возвращающий кортежи вида (<tutor>, <klass>),
например:
#     ('Иван', '9А')
#     ('Анастасия', '7В')
#     ...
Количество генерируемых кортежей не должно быть больше длины списка tutors.
Если в списке klasses меньше элементов, чем в списке tutors, необходимо вывести
последние кортежи в виде: (<tutor>, None),
например:
#     ('Станислав', None)

### Доказать, что вы создали именно генератор.
    Проверить его работу вплоть до истощения.
    Подумать, в каких ситуациях генератор даст эффект.
'''


def tut_gen():
    variable_list = []
    el = 0
    if len(klasses) < len(tutors):
        while el < len(tutors):
            if el > len(klasses)-1:
                variable_list.append(tutors[el])
                variable_list.append(None)
                result = tuple(variable_list.copy())
                variable_list.clear()
                yield result
                el += 1
                continue
            variable_list.append(tutors[el])
            variable_list.append(klasses[el])
            result = tuple(variable_list.copy())
            variable_list.clear()
            el += 1
            yield result
    for num in range(len(tutors)):
        variable_list.append(tutors[num])
        variable_list.append(klasses[num])
        result = tuple(variable_list.copy())
        variable_list.clear()
        yield result


tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б'] #, '9В', '8Б', '10А', '10Б', '9А']


new_list = tut_gen()
for i in range(len(tutors)):
    print(next(new_list))
print(f'\n{type(new_list)}') # Проверка типа
