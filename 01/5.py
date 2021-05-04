'''
Author: your name
Date: 2021-05-03 15:43:01
LastEditTime: 2021-05-04 18:52:58
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /python2021/01/5.py
'''
#!/usr/bin/env python3
# -*- coding:uft-8 -*-
# from turtle import *
# from turtle import *

# color('yellow','blue')
# begin_fill()
# while True:
#     forward(200)
#     left(220)
#     if abs(pos())< 1:
#         break
# end_fill()
# done()
# l = []
# n = 1
# while n <= 99:
#     l.append(n)
#     n = n + 1


L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

# r = []
# n = 2
# for i in range(n):
#     r.append(L[i])


def trim(s):
    while s[:1] == ' ':
        s = s[1:]
    while s[-1:] == ' ':
        s = s[:-1]
    return s


# print(trim('       hello         '))

d = {'a': 1, 'b': 2, 'c': 3}
for k, v in d.items():
    print(k, v)


for i in 'ABC':
    print(i)

for i, value in enumerate(['A', 'B', 'C']):
    i = i + 1
    print(i, value)

for x, y in [(1, 1), (2, 2), (3, 3)]:
    print(x, y)


def findMinAndMax(L):
        if len(L) == 0:
            return (None, None)
        else:
            max = min = L[0]
            for n in L:
                if n < min:
                    min = n
                if n > max:
                    max = n
            return (min,max)

print(findMinAndMax([7,1]))
