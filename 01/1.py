
'''
Author: your name
Date: 2021-04-23 11:05:21
LastEditTime: 2021-04-25 16:34:42
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /python2021/01/1.py
'''
#!/#usr/bin/env python3
# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
# s1 = 72
# s2 = 85
# r = (s2-s1)/s1
# print(f'{r:.2f}')

n = ['rice', 'banana', 'apple']
a = len(n)
print(a)
print(n[-1])
n.append('tomato')
n.insert(0, 'coffee')
n.pop()

# a = int(input('请输入出生年代：'))
# birth = int(a)
# if birth < 2000 :
#     print('00前')
# else:
#     print('00后')

xm = [1.75, 50.5]

BMI = xm[1]/(xm[0]*2)

if BMI < 18.8:
    print('过轻')
elif BMI <= 25:
    print('正常')
elif BMI <= 28:
    print('过重')
elif BMI <= 32:
    print('肥胖')
else :
    print('严重肥胖')

