'''
* (вместо 2) Доработать функцию currency_rates(): теперь она должна возвращать кроме курса дату,
которая передаётся в ответе сервера. Дата должна быть в виде объекта date. Подумайте,
как извлечь дату из ответа, какой тип данных лучше использовать в ответе функции?
'''

import requests
import datetime


def currency_rates(user_valute):
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    # print(response.status_code)
    content = response.content.decode(encoding=response.encoding)
    # print(content)
    s = []
    date_ = []
    for el in content.split('<CharCode>'):
        s.append(el.split('</Value>')[0])
    for s_date in s.pop(0).split('<ValCurs Date="'):
        date_ = s_date.split('"')[0].split('.')
    a = datetime.datetime(int(date_[2]), int(date_[1]), int(date_[0]))
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
        return f'На {a.strftime("%d/%m/%Y")} курс 1 {d_[user_valute][1]} составляет {currencies} руб.'
    return currencies


user_valute = str(input('Введите код валюты (например USD)\n>>>').upper())
print(currency_rates(user_valute))


