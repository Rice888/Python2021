# encoding: utf-8
'''
@Author: your name
@Date: 2020-06-16 11:30:13
@LastEditTime: 2020-06-17 11:12:59
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /RiceProgram/python3/01-python/moredata.py
'''
# moreData.py


def average2():
    sum = 0.0
    count = 0
    moredata = "yes"
    while moredata[0] == "y":  # 索引

        print(moredata[0])
        x = eval(input("Enter a number >>"))
        sum += x
        count += 1
        moredata = input("Do you have more number (yes ore no)? ")
    print("\nThe average of the numbers is", sum/count)
    print(moredata[0])

# average2()


def average3():
    sum = 0.0
    count = 0
    x = eval(input("Enter a number (negative to quit) >>"))
    while x >= 0:
        sum += x
        count += 1
        x = eval(input("Enter a number (negative to quit)>>"))
    print("\nThe average of the number is ", sum/count)
    print(x)

# average3()


def average4():
    sum = 0.0
    count = 0
    xStr = input("Enter a number (negative to quit) >>")
    while xStr != "":
        x = eval(xStr)
        print(type(x))
        sum += x
        count += 1
        xStr = input("Enter a number (negative to quit) >>")
    print("\nThe average of the number is ", sum/count)

# average4()


def average5():
    fileName = input("What file are the number in?")
    infile = open(fileName, 'r')
    sum = 0
    count = 0
    for line in infile:
        sum += eval(line)
        count += 1
    print("\nThe average of the number is", sum/count)

# average5()


def average6():
    fileName = input("What file are the number in?")
    infile = open(fileName, 'r')
    sum = 0
    count = 0
    line = infile.readline()
    while line != "":
        sum += eval(line)
        count += 1
        line = infile.readline()
    print("\nThe average of the number is", sum/count)

# average6()


def average7():
    fileName = input("What file are the number in?")
    infile = open(fileName, 'r')
    sum = 0
    count = 0
    line = infile.readline()
    while line != "":
        for xStr in line.split(","):
            sum += eval(xStr)
            count += 1
        line = infile.readline()
    print("\nThe average of the number is", sum/count)


# average7()

def xun():
    while True:
        try:
            x = int(input("Please enter a number:"))
            break
        except ValueError:
            print("Oops that was no valid number. Try again...")


def getN():
    x = int(input("Please enter a number:"))
    if x < 0:
        x = int(input("Please enter a number:"))
    else:
        print("Result", x)

# getN()

#后测循环
def getN2(): 
    number = -1
    while number < 0 :
        number = eval(input("Enter a positive number:"))
    print(number)

getN2()

#后侧循环3

def getN3():
    while True:
        number = eval(input("Enter a positive number: "))
        # if x >= 0 : break

getN3()
