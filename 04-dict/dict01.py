#encoding:utf-8
'''
@Author: your name
@Date: 2020-06-24 12:09:30
@LastEditTime: 2020-06-26 12:54:23
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /python3/04-dict/dict01.py
'''
#dictionary.py
a = 72
b = 85
r = (b-a)/a*100
print("%s的进步是%.1f%%" % ("小明", r))

d = ["Adam","Michael","track","Bob"]
d.append('Rice')
d.insert(0,'Su')
d.pop() #默认删除末尾 （0）删除第一项
d[2]='d' #替换文件内容直接用索引
d[2] = ['apple',123,True]
e = [1,2,'df',d,'ee']
print(d)
print(e)
print(e[3][4])
l = []
print(len(l))

g = (1,2) #tuple 为了消除歧义1,必须加点
print(g)

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
print(L[0][0])
print(L[1][1])
print(L[2][2])

