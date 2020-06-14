#encoding: utf-8
'''
@Author: your name
@Date: 2020-06-13 23:18:04
@LastEditTime: 2020-06-14 10:49:29
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /RiceProgram/python3/01-python/findWeek.py
'''

# week.py

week = "MondayTuedayWedndyThudayFirdaySatdaySunday" #保证同样的长度
n = input("请输入") #输入数字1-7
pos = (int(n)-1) * 6 #转换成整数数字-1等于索引 *长度6
weekDate = week[pos:pos+6] #选择范围 6 + 6的位置
print(weekDate) #输出
