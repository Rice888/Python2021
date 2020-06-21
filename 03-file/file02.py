#encoding:utf-8
'''
@Author: your name
@Date: 2020-06-20 17:07:51
@LastEditTime: 2020-06-21 22:59:17
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /RiceProgram/python3/03-file/file02.py
'''
import turtle

def main():
    turtle.title("数据绘制") #窗口名称
    turtle.setup(800,600,-1,500)  #平米宽800高600，开始坐标中心0左右x 500上下y
    turtle.bgcolor('#571657') #turtle 背景颜色
    pen = turtle.Turtle() #初始化turtle
    pen.color("red") #初始颜色红色
    pen.width(5)    #宽度5个像素
    pen.shape("arrow") #设置图标arrow 箭头
    pen.speed(3) #设置速度1慢10块
    result =[] #创建一个的list
    file = open("/Users/rice/Desktop/RiceProgram/python3/03-file/data.txt","r")#打开文件绝对路径 r只读
    for line in file: #循环 line 循环file文件
        result.append(list(map(float,line.split(','))))#把循环的推到result。list上 map（函数 浮点数，line，split 以逗号分割
    print(result) #打印 result
    for i in range(len(result)): #i 循环 result的长度 len(result)方法等到序列 0 -14
        pen.color((result[i][3],result[i][4],result[i][5])) # 300[i][0],0[i][1],144[i][2],1[i][3],0[i][4],0[i][5] #改变颜色
        print(result[i][0]) #查看位置
        pen.fd(result[i][0]) #前进反向
        if result[i][1]: 
            pen.rt(result[i][2])
        else:
            pen.lt(result[i][2])
    pen.goto(0,0)

main()
# def main():
#     #设置窗口信息
#     turtle.title('数据驱动的动态路径绘制')#建立的窗口标题
#     turtle.setup(800, 600, 0, 0)#建立的窗口大小及位置
#     #设置画笔
#     pen = turtle.Turtle()#创建一个画笔实例
#     pen.color("red")#初始化颜色为红色
#     pen.width(5)#线条宽度为5px
#     pen.shape("turtle")#初始化画笔形状
#     pen.speed(1)#海龟速度
#     #pen.fillcolor("blue")
#    # pen.begin_fill()
#     #读取文件
#     result=[]#创建一个列表
#     file = open("/Users/rice/Desktop/RiceProgram/python3/03-file/data.txt","r")#打开提前设置好的数据文件
#     for line in file:#遍历之
#         result.append(list(map(float,line.split(','))))#每循环一次把后面一行的数据加到result忠
#     print(result)#打印之
#     #动态绘制
#     for i in range(len(result)):#len()指的是列表数据长度
#         pen.color((result[i][3],result[i][4],result[i][5]))#随着数据的变化线条颜色变化
#         pen.forward(result[i][0])#小乌龟运动方向
#         if result[i][1]:
#             pen.rt(result[i][2])
#             #pen.fill(Ture)
#         else:
#             pen.lt(result[i][2])
#     pen.goto(0,0)
 
 
# if __name__ == '__main__':
#     main()
    