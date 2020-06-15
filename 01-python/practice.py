# encoding: utf-8
'''
@Author: your name
@Date: 2020-06-15 10:56:36
@LastEditTime: 2020-06-15 13:58:17
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /RiceProgram/python3/01-python/practice.py
'''

def month():
    months = "JanFebMarAprMayJunJulAugSepOctNovDec"
    n = input("请输入1-12月份查询英文缩写")
    type(n)
    print(n)
    pos = (int(n)-1)*3
    if pos < 1 or pos >12:
        print("请输入1-12月份查询英文缩写")
    else:
        monthAbbr = months[pos:pos+3]
        print("月份的缩写是" + monthAbbr)

month()
    