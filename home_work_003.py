'''
Реализовать склонение слова «процент» во фразе «N процентов». Вывести эту фразу на экран
отдельной строкой для каждого из чисел в интервале от 1 до 100:
1 процент
2 процента
3 процента
4 процента
5 процентов
6 процентов
...
100 процентов
'''

for i in range(1,101):
    if i == 1:
        print(f'{i} процент')
    if 2 <= i < 5:
        print(f'{i} процента')
    if 5 <= i <= 100:
        print(f'{i} процентов')
