'''
Написать функцию currency_rates(), принимающую в качестве аргумента код
валюты (например, USD, EUR, GBP, ...) и возвращающую курс этой валюты по отношению к рублю.
Использовать библиотеку requests.
В качестве API можно использовать http://www.cbr.ru/scripts/XML_daily.asp.
Рекомендация: выполнить предварительно запрос к API в обычном браузере, посмотреть содержимое ответа.
Можно ли, используя только методы класса str, решить поставленную задачу?
Функция должна возвращать результат числового типа, например float.
Подумайте: есть ли смысл для работы с денежными величинами использовать вместо float тип Decimal?
Сильно ли усложняется код функции при этом?
Если в качестве аргумента передали код валюты, которого нет в ответе, вернуть None.
Можно ли сделать работу функции не зависящей от того, в каком регистре был передан аргумент?
В качестве примера выведите курсы доллара и евро.
'''

import requests


def currency_rates(user_valute):
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    # print(response.status_code)
    content = response.content.decode(encoding=response.encoding)
    # print(content)
    s = []
    for el in content.split('<CharCode>'):
        s.append(el.split('</Value>')[0])
    s.pop(0)
    s1 = []
    s2 = []
    s3 = []
    s_ = []
    d_ = {}
    for i in range(len(s)):
        for el in s[i].split('</CharCode><Nominal>'):
            s1.append(el)
        for el1 in s1[1].split('</Nominal><Name>'):
            s2.append(el1)
        for el2 in s2[1].split('</Name><Value>'):
            s3.append(el2)
        nominal = int(s2[0])
        currency = float(s3[1].replace(',', '.'))
        s_.append(nominal)
        s_.append(s3[0])
        s_.append(currency)
        d_[s1[0]] = s_.copy()
        s1.clear()
        s2.clear()
        s3.clear()
        s_.clear()
    currencies = d_.get(user_valute)
    if d_.get(user_valute) is not None:
        currencies = d_[user_valute][2] / d_[user_valute][0]
        return f'Курс 1 {d_[user_valute][1]} составляет {currencies} руб.'
    return currencies


user_valute = str(input('Введите код валюты (например USD)\n>>>').upper())
print(currency_rates(user_valute))

