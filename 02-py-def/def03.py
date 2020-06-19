'''
@Author: your name
@Date: 2020-06-18 16:07:06
@LastEditTime: 2020-06-19 19:59:19
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /RiceProgram/python3/02-py-def/def03.py
'''
#def03.cy
from turtle import Turtle
# def reverse(s):
#     if s =="":
#         return s
#     else:
#         return reverse(s[1:]) + s[0]

# print(reverse("hello"))

p = Turtle()
p.speed(1)
p.pensize(5)
p.color("#675117","yellow")
p.begin_fill
for i in range(5):
    p.forward(200)
    p.right(144)
p.end_fill()


