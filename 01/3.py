'''
Author: your name
Date: 2021-04-26 11:24:48
LastEditTime: 2021-04-27 12:03:23
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /python2021/01/3.py
'''
#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import math
a = ['whh','lsd','hxm']
a.append('mzd')
a.insert(0,'ff')
a.pop(1)
for x in a:
    b = 'hellow, %s ' %(x)
    
    print(b)
b = abs(-100)
print(b)
print(max(1,4))
print(bool(1+1))

def my_abs(x):
    if x >= 0:
        return x
    else:
        print(x)
        return -x

print(my_abs(-1))

a = int(input())
b = math.sqrt(a)
print(b)