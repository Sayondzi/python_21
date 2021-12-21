'''
Подумайте, как можно сделать оптимизацию кода по памяти, по скорости.
Представлен список чисел.
Определить элементы списка, не имеющие повторений.
Сформировать из этих элементов список с сохранением порядка их следования в
исходном списке, например:
#     src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
#     result = [23, 1, 3, 10, 4, 11]
Подсказка: напишите сначала решение «в лоб». Потом подумайте об оптимизации.
'''

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

result = set()
repeated_numbers = set()
for number in src:
    if number in repeated_numbers:
        continue
    if number in result:
        repeated_numbers.add(number)
        result.discard(number)
        continue
    result.add(number)
print([number for number in src if number in result])
