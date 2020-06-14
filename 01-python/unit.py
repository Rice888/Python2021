# encoding: utf-8
'''
@Author: your name
@Date: 2020-06-14 11:53:40
@LastEditTime: 2020-06-14 13:54:29
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /RiceProgram/python3/01-python/unit.py
'''
#pi.py
#元祖类型类似数组 用,号分隔 不能修改
from random import random
from math import sqrt
from time import perf_counter
t3 = 123,456,"你号",("hello","666")
t3[0]

a = [1,2,3,4,"hello"]
a[4]

DARTS = 1200
hits = 0 
perf_counter()
for i in range(1,DARTS):
    x,y =random(),random()
    dist =sqrt(x**2+y**2)
    if dist <= 1.0:
        hits = hits + 1
pi =4* (hits/DARTS)
print("pi的值是 %s" % pi)

print("程序运行时间是 %-5.5ss" % perf_counter())