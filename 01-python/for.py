#encoding:utf-8
#for.py
'''
@Author: your name
@Date: 2020-06-15 14:12:54
@LastEditTime: 2020-06-15 14:55:48
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /RiceProgram/python3/01-python/for.py
'''

def words():
    words = ['cat','window','difficulty']
    for i in  words:
        print(i+":",len(i))

def Findaverage():
    n = eval(input("how many numbers? "))
    s = eval(input("Much sale? "))
    sale = (float(s)) /10
    sum = 0.0
    for i in range(n):
        x = eval(input("Enter a number >> "))
        sum = sum + x
        print(sum)
    print("\nThe average is", sum * sale)# /斜杠除以
Findaverage()   
