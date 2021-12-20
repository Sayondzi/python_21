'''
Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов,
взятых из трёх списков (по одному из каждого):
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
       Например:
#>>> get_jokes(2)
["лес завтра зеленый", "город вчера веселый"]
Документировать код функции.
Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в
шутках (когда каждое слово можно использовать только в одной шутке)?
Сможете ли вы сделать аргументы именованными?
'''


import random


def get_jokes(n: int, m: str):
    joke = []
    joke_ = []
    jokes = []
    base = []
    i = 1

    base.append(nouns)
    base.append(adverbs)
    base.append(adjectives)
    if m == answer[0]:
        while i <= n:
            for k in range(len(base)):
                joke.append(random.sample(base[k], 1))
            for l in range(len(base)):
                joke_.append(' '.join(joke[l]))
            jokes.append(' '.join(joke_))
            joke.clear()
            joke_.clear()
            i += 1
    else:
        while i <= user_number:

            k = random.randrange(len(nouns_copy))
            joke = [f'{nouns_copy.pop(k)} {adverbs_copy.pop(k)} {adjectives_copy.pop(k)}']
            for l in range(len(joke)):
                joke_.append(joke[l])
            jokes.append(' '.join(joke_))
            joke_.clear()
            i += 1
    return(jokes)


nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
answer = ['ДА', 'НЕТ']
et = 10
et_1 = len(nouns)
nouns_copy = nouns.copy()
adverbs_copy = adverbs.copy()
adjectives_copy = adjectives.copy()

while True:
    user_number = input(f'Введите целое число (от 1 до {et}):\n>>>')
    try:
        user_number = int(user_number)
        if user_number < 1 or user_number > et:
            print(f'Значение должно находиться в диапазоне от 1 до {et}.')
            continue
    except ValueError as e:
        print('Необходимо ввести число. Попробуйте ещё раз.')
        continue
    break

while True:
    user_answer = input('Повторы разрешены? (варианты ответа да/нет)\n>>>').upper()
    if user_answer == answer[0]:
        print('Вы выбрали вариант, где разрешены повторы.')
        break
    elif user_answer == answer[1]:
        print('Вы выбрали вариант, где неразрешены повторы.')
        if user_number > et_1:
            while True:
                user_number = input(f'Введите целое число (от 1 до {et_1}):\n>>>')
                try:
                    user_number = int(user_number)
                    if user_number < 1 or user_number > et_1:
                        print(f'Значение должно находиться в диапазоне от 1 до {et_1}.')
                        continue
                except ValueError as e:
                    print('Необходимо ввести число. Попробуйте ещё раз.')
                    continue
                break
        break
    else:
        print('Некорректный ввод. Следуйте чётко инструкции.')
        continue

print(get_jokes(user_number, user_answer))
