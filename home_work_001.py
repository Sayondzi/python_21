'''
1. Реализовать вывод информации о промежутке времени в зависимости от его продолжительности
duration в секундах:
до минуты: <s> сек;
до часа: <m> мин <s> сек;
до суток: <h> час <m> мин <s> сек;
* в остальных случаях: <d> дн <h> час <m> мин <s> сек.
'''

while True:
    duration = input("Укажите число секунд: \n>>> ")
    try:
        duration = int(duration)
    except ValueError as e:
        print(f'{e}\n\nУказаны некорректные данные. Пожалуйста, попробуйте ещё.\n')
        continue
    break

s = 60
h = 3600
d = 86400
if duration < s:
    print(duration % s, 'сек')
elif s <= duration < h:
    print(duration // s, 'мин', duration % s, 'сек')
elif h <= duration < d:
    print(duration // h, 'час', duration % h // s, 'мин', duration % s, 'сек')
else:
    print(duration // d, 'дн', duration % d // h, 'час', duration % h // s, 'мин', duration % s, 'сек')
