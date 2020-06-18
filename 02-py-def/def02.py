# encoding:utf-8
'''
@Author: your name
@Date: 2020-06-17 17:04:31
@LastEditTime: 2020-06-18 15:34:19
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /RiceProgram/python3/02-py-def/def02.py
'''
# def02.py
'''
def addInterest1(balance,rate):
    newBalance = balance * (1+rate) #金额加上 1的比例
    balance = newBalance
    return newBalance
def main():
    amount = int(input("请输入存款金额:"))
    rate = 0.05
    amount = addInterest1(amount,rate) #传参 parament
    print(amount)

# main()
'''


def addInterest1(balance, rate):
    for i in range(len(balance)):
        balance[i] *= (1+rate)  # 循环每一条


def main():
    amount = [1000, 500, 105, 3500]
    rate = 0.05
    addInterest1(amount, rate)  # 传参 parament
    print(amount)

# main()





def createTable(principal, apr):
    for year in range(1, 11):
        principal = principal * (1 + apr)
        print("%2d" % year, end='')
        total = caculateNum(principal)
        print("*" * total)
    print("0.0k 2.5k 5.0k 7.5k 10.0k")

def caculateNum(principal):
    total = int(principal*4/1000.0)
    return total


def newMain():
    principal = eval(input("输入本金"))
    apr = eval(input("请速速利率"))
    createTable(principal,apr)

newMain()
