# encoding: utf-8
'''
@Author: your name
@Date: 2020-06-14 14:07:49
@LastEditTime: 2020-06-14 14:17:56
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /RiceProgram/python3/01-python/if-pm.py
'''

#pm2.5.py

def main():
    PM = eval(input("what is today's PM2.5? "))
    if PM >= 75:
        print("unhealthy. Be careful!")
    if PM <= 35:
        print("Good. Go running!")

main()  