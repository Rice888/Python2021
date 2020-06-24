#encoding:utf-8
'''
@Author: your name
@Date: 2020-06-24 10:59:51
@LastEditTime: 2020-06-24 12:05:23
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /RiceProgram/python3/04-dict/dict.py
'''
#dict.py
#像js打对象 无序 数字 字符串 元祖 
password ={"xm":"xm1987","zs":"19870q","df":"18,823q"}
password['su'] = "19870" #添加一条
print(password)
print(password["xm"]) #查询代码
del password["xm"]
for i in password:
    print(i +':' + str(password[i]))

for key in password.keys():
    print(key)
for value in password.values():
    print(value)
for item in password.items():
    print(item)
for item ,value in password.items():
    print(item,value)

print("zs" in password)
print('zs' not in password)

d1 = {'red':41,'blue':31}
d2 = {'blue':31,'red':41}

print(d1 != d2)
print(d1 == d2)

print(tuple(password.keys()))
print(tuple(password.values()))
print(tuple(password.items()))
