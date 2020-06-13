# encoding: utf-8
'''
@Author: your name
@Date: 2020-06-10 12:34:02
@LastEditTime: 2020-06-13 16:34:38
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /RiceProgram/python3/01.py
'''

import turtle


def drawSnake(rad, angle, len, neckrad):
    for i in range(len):
        turtle.circle(rad, angle)  # rad 圆形路径左侧 -值向右运行
        turtle.circle(-rad, angle)  # angle 爬行幅度值
    turtle.circle(rad, angle/2)
    turtle.fd(rad)  # fd forward 自行爬向
    turtle.circle(neckrad+1, 180)
    turtle.fd(rad*2/3)


def main():

    turtle.setup(1300, 800, 0, 0)  # 屏幕1300px宽800px高 0 x:向左 0 Y：向下
    pythonsize = 10  # 变量 像素10px 01
    turtle.pensize(pythonsize)  # 画笔调用 01
    turtle.pencolor("#513b8d")  # 颜色 rgb #3b9909
    turtle.seth(0)  # 方向
    drawSnake(10, 150, 8, pythonsize/2)


main()

