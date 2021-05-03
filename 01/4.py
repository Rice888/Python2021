'''
Author: your name
Date: 2021-04-27 12:07:55
LastEditTime: 2021-05-03 15:42:09
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /python2021/01/4.py
'''
#!/usr/bin/env python3
# -*- coding:utf-8 -*-


# def power(x, n=2):
#     s = 1
#     while n > 0:
#         n = n - 1
#         print('n:', n)
#         s = s * x
#         print('s:', s)
#     return s


# def enroll(name, gender, age=6, city='Beijing'):
#     print('name', name)
#     print('gender', gender)
#     print('age', age)
#     print('city', city)


# enroll('mac', 'F', 7, 'fuzhou')


# def add_end(l=None):
#     if l is None:
#         l = []
#     l.append('END')
#     return l


# a = add_end()

# # print(a)

# def calc(*numbers):
#     sum = 0
#     for n in numbers:
#         sum = sum + n * n
#         print(sum)
#     return sum
# x = [1,2,3,5]
# b = calc(*x)
# print(b)

def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


extra = {'city:': 'Bj', 'gender:': 'male'}

print(person('Rice,', 35, **extra))


# def mul(*args):
#     s = 1
#     if len(args) > 0:
#         for i in args:
#             s = s * i
#         return s
#     else:
#         raise TypeError


# print(mul(23, 2))


# def students(name, age, *args, city, job):
#     print(name, age, 'args:', args, city, job)


# d = students('mac', 18, 1, 2, 3, city='bj', job='teather')
# args = (5,6,7,)
# o = students(*args)
# print(d,o)

def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)


def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)


args = (5, 6, 7, 4, 6)
kw = {'hah:': 'hah'}

print(f1(1, 2, 3, *args, **kw))


def mul(*args):
    s = 1
    if len(args) > 0:
        for i in args:
            s = s * i
        return s
    else:
        raise TypeError


print(mul(5))


# def fact(n):
#     # print('我是N：',n)
#     return fact(n, 1)


# def fact_iter(num, product):
#     print('我是num', num)
#     if num == 1:
#         return product
#     print('我是p', product)
#     return fact_iter(num - 1, num * product)


# print(fact(3))


# def hanoi(n):
#     return hanoi_iter(n, a, b, c)


def hanoi(n, a, b, c): #1 A B C  #3 #10
    if n == 1:
        print(a, '--1>', c) #5  #8 C - B
    else:
        hanoi(n-1, a, c, b)#2 a= A c= b  b =c  #4
        print('我是：',c )  
        print(a, '--2>', c) #6 #9
        hanoi(n-1, b, a, c) #7  C A B  # 11  a= B b = A c= C  
        print('我是n2：',n)


# n = int(input('请输入层数：'))

print(hanoi(3,'A','B','C'))


def test(x):
    if x == 1:
        print(x)
    else:
        print(2)

print(test(2))

