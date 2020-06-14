'''
@Author: your name
@Date: 2020-06-14 10:51:05
@LastEditTime: 2020-06-14 11:51:53
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /RiceProgram/python3/01-python/string.py
'''
n = input('输入')
print(n.capitalize())
print(n.upper())
print(n.lower())
print(n.strip())
print(n.split( )) #空格变成分割 ，
print(n.split('d'))  #d变成分割
print(n.split('d',2)) #都变成分割 2次
print(n.isdigit()) #是否是数字
print(n.find('day')) #查找在第几个

h = "hello \nworld"
print(h)