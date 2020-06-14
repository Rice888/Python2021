'''
@Author: your name
@Date: 2020-06-13 18:37:03
@LastEditTime: 2020-06-14 10:41:50
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /RiceProgram/python3/01-python/type.py
'''
# encoding: utf-8
'''
@Author: your name
@Date: 2020-06-13 18:37:03
@LastEditTime: 2020-06-13 23:13:52
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /RiceProgram/python3/type.py
'''
# monthy.py
months = "JanFebMarAprMayJunJulAugSepOctNovDec"
n = input("请输入月份")
pos = (int(n)-1) * 3
monthAbbrev = months[pos:pos+3]
print("月份缩写是" + monthAbbrev + ".")
