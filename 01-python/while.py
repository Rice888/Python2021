# encoding: utf-8
'''
@Author: your name
@Date: 2020-06-15 15:00:52
@LastEditTime: 2020-06-15 17:25:02
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /RiceProgram/python3/01-python/while.py
'''
# while.py
def sumMachine():
    sum = 0
    number =0
    while number <20:
        number += 1
        print("数字:",number)
        sum += number
        print("总数是:",sum)
        if sum > 100:
            break
    print("This is number:", number)
    print("This is number:", sum)
        


def numMachine():
    for num in range(1,11):
        print(num)
        if num % 2 != 0:
            continue
        print("Found a odd number:",num)

def numSuper():
    for n in range(1,11):
        # print("This is n", n)
        for x in range(2,n):
            print('this is x', x)
            if n % x == 0:
                print(n,'equals',x ,'*', n // x)
                print(n)
                break
    else:
        #loop fell through without finding a factor
        print(n,'is a prime number')

numSuper()
