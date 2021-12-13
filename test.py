

s = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

s_new = []
a_1 = '"'

for i in range(len(s)):
    while True:
        b_1 = s[i]
        try:
            c_1 = int(b_1)
            s_new.append(a_1)
            if b_1[0] == '+':
                s_new.append("{0:+03d}".format(c_1))
            else:
                s_new.append("{0:02d}".format(c_1))
            s_new.append(a_1)
        except ValueError as e:
            s_new.append(s[i])
            break
        break
print(*s_new)

