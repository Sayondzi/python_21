'''
Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield,
например:
#   >>> odd_to_15 = odd_nums(15)
#   >>> next(odd_to_15)
#   1
#   >>> next(odd_to_15)
#   3
#   ...
#   >>> next(odd_to_15)
#   15
#   >>> next(odd_to_15)
#   ...StopIteration...
'''

MAX_NUM = 15


def nums_generator():
    for num in range(1, MAX_NUM + 1, 2):
        yield num


nums = nums_generator()

while True:
    try:
        print(next(nums))
        continue
    except StopIteration as e:
        break
