# encoding: utf-8
'''
@Author: your name
@Date: 2020-06-17 11:16:28
@LastEditTime: 2020-06-17 16:55:37
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /RiceProgram/python3/def01.py
'''
# def01.py


def new(x):
    x = str(x)
    print(x)

# new(input("侵入书"))


def demo1(x):
    x += 1
    return x

# demo1(int(input("请输入：")))

def sing():
    h = "Happy Birthday to you!"
    print(h)


def birthday(x):
    sing()
    sing()
    name = "Happy Birthday" +str(x)
    print(name)
    sing()


# birthday(input("输入名字"))

def sumDiff(x,y):  
    sum = x + y
    diff = x - y
    return sum,diff
    print(sum,diff)

num1 = eval(input("please enter two numbers (num1)"))
num2 = eval(input("please enter two numbers (num1)"))
s,d= sumDiff(num1,num2)
print("This sum is:",s ,"This diff is:", d)