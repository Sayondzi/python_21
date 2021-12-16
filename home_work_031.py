'''
Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык.
Например:
#>>> num_translate("one")
"один"
#>>> num_translate("eight")
"восемь"
Если перевод сделать невозможно, вернуть None. Подумайте, как и где лучше хранить информацию,
необходимую для перевода: какой тип данных выбрать, в теле функции или снаружи.
'''


WORD_BOOK = {
    'zero': 'ноль',
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять'
}


def num_translate(a: str, b: dict):
    return(b.get(a))


user_word = 'twelve'
print(num_translate(user_word, WORD_BOOK))
