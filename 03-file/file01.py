#encoding
'''
@Author: your name
@Date: 2020-06-19 22:13:59
@LastEditTime: 2020-06-20 17:07:36
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /RiceProgram/python3/03-file/file01.py
'''
#ASCII码 7个二进制 表示128个字符
print(ord('A'))

print(chr(65))

'''
Unicode
跨语言 跨平台
统一且唯一的二进制编码
每个字符两只字节长
65366个字符集空间
‘严’ ：4E25
'''

'''
UTF-8编码
可变长度的unicode
‘严’ ：E4B8A5
encode:编码
decode:解码

GBK编码

print(s.decode("GBK"))

s = "中文字符串"
bs = s.encode("utf-8")
print(bs)
print(bs.decode("utf-8"))

rr = open('/Users/rice/Downloads/stock-photo-77010759-1.jpg','rb')#图片为rb

# print(rr.read()) #加括号

def main1():
    fname = input("Enter filename")
    infile = open(fname,'rb')
    data = infile.read()
    print(data)

# main()

def main2():
    fname = input("Enter fname")
    infil = open(fname,'r')
    for i in range(3):
        line = infil.readline()
        print(line[:-1])  #readline 末尾是空格 ：-1 表示删掉最后的空格
 
# main2()

def main3():
    w = input("Enter any thing")
    infile = open("/Users/rice/Desktop/RiceProgram/python3/03-file/a.txt","w")
    infile.writelines(w)
    infile.close()
    ofile = open("/Users/rice/Desktop/RiceProgram/python3/03-file/a.txt","r")
    data=ofile.read()
    print(data)

# main3()

#通用文件遍历框架

def main66():
    file = open("someFile","r")
    for line in file.readlines():
        #文件出来    
    file.close() 


def main666():
    file = open("someFile","r")
    for line in file:
        #文件出来    
    file.close() 
'''
def main6():
    #输入原地址
    f1 = input("Enter a source file:").strip() 
    #输入新地址
    f2 = input("Enter a source file:").strip()

    #读取原文件
    infile = open(f1,"r") 
    #写入新文件
    outfile = open(f2,"w")

    #行数很 字符都等于0
    countLines = countChars = 0
    #循环原文件
    for line in infile:
        #每行加1
        countLines += 1
        print("this is countLines:",countLines)
        #计算line都字符+chars
        countChars += len(line)
        print("This is countChars",countChars)
        #写入新文件
        outfile.write(line)
    #打印行数和字符
    print(countLines, "lines and", countChars,"chars copied")

    #关闭文件
    infile.close()
    outfile.close()

main6()


    
