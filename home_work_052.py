'''
* (вместо 1) Решить задачу генерации нечётных чисел от 1 до n (включительно),
не используя ключевое слово yield.
'''

n = int(input('Введите значение "n":\n>>>'))
nums_gen = (num for num in range(1, n + 1, 2))

while True:
    try:
        print(next(nums_gen))
        continue
    except StopIteration as e:
        break
