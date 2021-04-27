'''
Author: your name
Date: 2021-04-25 16:46:23
LastEditTime: 2021-04-25 17:48:29
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /python2021/01/2.py
'''
#!/usr/bin/env python3
# -*- coding:utf-8 -*-

names = ['rice', 'apple', 'pear']
for a in names:
    print(a)

sum = 0
l = list(range(10))
for x in l:
    sum = sum + (x+1)
print(x)
print(l)
print(sum)

sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(n)
print(sum)

n = 1
while n <= 100:
    print(n)
    n = n + 1
print('End')

n = 1
while n <= 100:
    if n > 10:
        break
    print(n)
    n = n+1
print('End')

n = 0
while n < 10:
    n = n + 1
    if n % 2 != 0:
        continue
    print(n)

L = ['Bart', 'Lisa', 'Adam']
for x in L:
    print('hello', x)

J = {'A': 75, 'b': 55, 'c': 66}
print(J['A'])
J['d']= 88
a = 'd' in J
print(J['d'])
b = J.get('A')
print(b)
