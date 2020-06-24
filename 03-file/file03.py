# encoding:utf-8
'''
@Author: your name
@Date: 2020-06-21 23:08:16
@LastEditTime: 2020-06-24 10:58:11
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /RiceProgram/python3/03-file/file03.py
'''
# copy.py


def main():
    ftele1=open('/Users/rice/Desktop/RiceProgram/python3/03-file/ad.txt',"rb") #需要合并的文件1
    ftele2=open('/Users/rice/Desktop/RiceProgram/python3/03-file/em.txt',"rb") #需要合并的文件2
    ftele1.readline()#跳过第一行
    ftele2.readline()
    lines1=ftele1.readlines() #读取每一行
    lines2=ftele2.readlines() #读取每一行
    #建立空列表用于存储姓名电话Email
    list1_name=[]
    list1_tele=[]
    list2_name=[]
    list2_email=[]
    #获取TeleAddressBook
    for line in lines1: #循环文件1
        elements=line.split() #去掉分割
        list1_name.append(str(elements[0].decode("utf-8")))# decode 解码 推到 name1上 0以空格开始0
        list1_tele.append(str(elements[1].decode("utf-8"))) 
    #获取EmailAddressBook
    print(list1_name)
    print(list1_tele)
    for line in lines2:
        elements=line.split()
        list2_name.append(str(elements[0].decode("utf-8")))
        list2_email.append(str(elements[1].decode("utf-8")))
    print(list2_name)
    print(list2_email)
    lines=[] #新建空的行
    lines.append("姓名\t电话\t\t邮箱\n") #推入行信息
    #按索引方式遍历姓名列表
    for i in range(len(list1_name)):
        s='' #新建一个空字符串
        if list1_name[i] in list2_name: #如果l1的 名字在l2中
            j=list2_name.index(list1_name[i]) #j name2找到name1里的名字
            print(j)
            s="\t".join([list1_name[i],list1_tele[i],list2_email[j]])# s 添加 名字 电话 邮箱
            s+="\n"
        else:
            s="\t".join([list1_name[i],list1_tele[i],str("-----------")]) # s 添加 名字 电话 邮箱如果没有邮箱就空着
            s+="\n"
        lines.append(s) #推到 lines里
        print(s)
    for i in range(len(list2_name)): 
        s=''
        if list2_name[i] not in list1_name:
            s="\t".join([list2_name[i],str("-----------"),list2_email[i]])
            s+="\n"
        lines.append(s)
        print(s)   
    #将新生成的合并数据写入新的文件中
    ftele3=open('/Users/rice/Desktop/RiceProgram/python3/03-file/suPerad.txt',"w") #新建文件
    ftele3.writelines(lines)#把文件写入新文件
    #关闭文件   
    ftele3.close()
    ftele1.close()
    ftele2.close()
    print("The addressBooks are merged!")


main()