# task_3.py
# Zoom/Сергей; github.com/Sergey-Chardin; Telegram/Nygell Hardbard
# 4.1 This task broke my brain :) I couldn't fulfill it.
# Maybe it is necessary to convert the dictionary to a string, and
# then convert it into separate dictionaries, then dictionaries into a list :0
a = list(range(0, 11))
b = [i**2 for i in a]
dict_a = dict(zip(a, b))
print(dict_a)
# 4.2
d1 = {'a': 1}
d2 = {'b': 2}
d2['b'] = 5
d1.update(d2)
print(d1)
# 4.3
d1 = {'key1': 1, 'key2': 2}
d2 = {}
for key, value in d1.items():
    d2[value] = key
d1 = d2
print(d1)
# 4.4
import os


for root, dirs, files in os.walk("."):  
    for filename in files:
        print(filename)
# 4.5
import time


print(time.strftime('%H-%M %m-%d-%Y'))
# 4.6
# The user can type almost anything – Python reacts to input only after pressing the Enter key
numbers = list(range(1, 11))
action = 1
while action == 1:
    print('Press «Enter»')
    for i in numbers:
        list_action = input()
        print(i)
        action = 0
# 4.7
# Is this a task "with a star"? :)
string = 'LthHJKiHs GisH nKSiDJceFJ KASsolDIUKuJHtDHiSSonAK'
s = []
for i in string:
    if not i.isupper(): s.append(i)
    string = ''.join(s)
print(string)
# 4.8
colors = ['красный', 'оранжевый', 'желтый', 'зеленый', 'голубой', 'синий', 'фиолетовый']
n = 0
c = -1
for i in colors:
    n += 1
    c += 1
    if n > 6: 
        break
    else:
        st = str(colors[c])
        st1 = st.capitalize()
        print(st1, '–', n, 'цвет радуги')
# 4.9
import time


t = time.monotonic()
n= -1
action = 1
while action == 1:
    while time.monotonic() - t < 10:
        n += 1
        print(n)
# 4.10
a = list(range(1, 10))
times = 0
for i in a:
    times += 1
    print(times*str(i))
