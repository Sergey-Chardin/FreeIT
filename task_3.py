# task_3.py
# Zoom/Сергей; github.com/Sergey-Chardin; Telegram/Nygell Hardbard
# 3.1
print('Hello world!')
print()
# 3.2
user = input()
print('Hello, {}!'.format(user))
print()
# 3.3
str1 = 'Hi, I am a string variable'
n = 100
print(str1 + str(n))
print()
# 3.4
import math
n = 100
print(math.factorial(n))
print()
# 3.5
tup = tuple(range(0, 101))
print(tup[::2])
print()
# 3.6
tup = tuple(range(0, 101))
list1 = list(tup)
list2 = [i ** 2 for i in list1]
print(list2)
print()
# 3.7
# Attention! In the task, 'sounds' is changed to 'midi', but output only '.wav'!
str2 = 'sounds/lofi/chillstep.wav'
str2 = str2.replace('sounds', 'midi')
print(str2[-4:])
print()
# 3.8
a = [1, 1, 2, 3, 5, 8, 10, 10]
print([i for i in a if a.count(i) == 1])
print()
# 3.9
a = [1, 1, 2, 3, 5, 8, 10, 10]
print( [i + 1 for i in a])
print()
# 3.10
str4 = 'Python is the most popular programming language'
print(str2.count('p'))
print()
# 3.11
a = [0, 2, 3, 4]
b = [2, 2, 5]
print(set(a).difference(set(b)))
