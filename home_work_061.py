'''
Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл
логов web-сервера nginx_logs.txt
(https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs)
— получить список кортежей вида:
(<remote_addr>, <request_type>, <requested_resource>).

Например:

#     [
#     ...
#     ('141.138.90.60', 'GET', '/downloads/product_2'),
#     ('141.138.90.60', 'GET', '/downloads/product_2'),
#     ('173.255.199.22', 'GET', '/downloads/product_2'),
#     ...
#     ]

Примечание:
     код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.
'''

s = []
s1 = []
a1 = ()
s3 = []
f_name = 'nginx_logs.txt'
with open(f_name, 'r', encoding='utf-8') as f:
    content = f.read()
    row = content.splitlines()
    for i in range(len(row)):
        for el in row[i].split(' '):
            s.append(el)
        s1.append(s[0])
        s1.append(s[5][1:])
        s1.append(s[6])
        a1 = tuple(s1)
        s3.append(a1)
        s.clear()
        s1.clear()
    print(s3)



