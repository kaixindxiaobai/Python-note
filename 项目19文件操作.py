# 打开文件----open(name文件名或路径, mode访问模式（读'w'写'r'追加'a'）)
# 关闭文件----文件对象.close()   打开文件后需关闭

# 体验文件操作
import os

f = open('text1.txt', 'w')

f.write('aaa')

f.close()

# 主访问模式（访问模式可省略，默认'r'只读）

# 'r'只读,(1)当文件未查询到的时候，会报错 (2)只能进行读的操作 (3)光标在开头
# f = open('text2.txt', 'r')报错
f = open('text1.txt', 'r')
# f.write('aaa')报错
f.read()
f.close()

# 'w'只写，(1)当文件未查询到的时候，自动创建新文件 (2)只能进行写的操作 (3)光标在开头 (4)写入时将原有的数据覆盖
f = open('text2.txt', 'w')
f.write('aaa')
# f.read()报错
f.close()

# 'a'追加，(1)当文件未查询到时，自动创建新文件 (2)只能进行追加 (3)光标在结尾 (4)在文件后写入追加，每次运行都会加新数据
f = open('text3.txt', 'a')
f.write('abc\n')
# f.read()报错
f.close()

# read(num可省略则为全部)操作，num则表示读取文件的长度(字节)
f = open('text3.txt', 'r')
# print(f.read())
# print(f.read(6))
'''
aaa
aa
换行符占一个字节，所以表面上只有5个
'''
# readlines()将文件全部读取，并返回一个列表，每一行为一个元素
# content = f.readlines()
# print(content)

# readline()将文件读取一行，并将光标移到下一行开头
content1 = f.readline()
content2 = f.readline()
print(content1, content2, sep='')
f.close()

'''
都遵循主访问模式
'r+'文件不存在报错，文件指针开头
'w+'文件不存在创建，文件指针开头，文件存在覆盖
'a+'文件不存在创建，文件指针结尾，文件存在追加
都可读可写
'''

# 文件对象.seek(偏移量, 起始位置)    起始位置（0:文件开头[默认]，1:当前位置，2:文件收尾）
f = open('text4.txt', 'w+')
f.write('aaaaa\n')
f.write('ccccc')
f.seek(2, 0)
print(f.read())
f.close()
'''
若要将seek的偏移量为负数，则Python3需要rb访问模式
f = open('text4.txt', 'rb')
f.seek(-5, 2)
print('-'*20)
print(f.read())
f.close()
'''

# 文件备份
# 用户输入
user = 'text5.txt'
# user = input('请输入想要备份的文件名:')
# 获取'.'的位置

# 若输入文件名不符合规范，则不会执行复制操作
if dict != 0:
    dict = user.rfind('.')
# 组成新名字
new_name = user[:dict] + '[备份]' + user[dict:]
f = open(user, 'rb')
f1 = open(new_name, 'wb')
# 复制
while True:
    file_content = f.read(1024)
    if len(file_content) == 0:
        break
    f1.write(file_content)
f.close()
f1.close()

# 文件和文件夹操作
'''
导入os模块
使用模块功能
'''
import os
# rename():重命名文件或文件夹----当第一次运行修改成功后，再次运行因文件被修改找不到目标修改而报错
# os.rename('text6.txt', 'text5.txt')

# remove():删除文件
f = open('text6.txt', 'w')
f.close()
os.remove('text6.txt')

# 文件夹操作
# mkdir(文件夹名):创建文件夹,当文件运行成功创建文件夹后，再次运行会重复创建，报错
# os.mkdir('aa')

# rmdir(文件夹名):删除文件夹
# os.rmdir('aa')

# getcwd()获取当前目录路径
print(os.getcwd())

# chdir(文件夹名)改变目录路径
# 在aa文件目录里创建bb文件
# os.mkdir('cc')
# 将默认路径改成aa文件夹
# os.chdir('aa')
# os.mkdir('bb')

# listdir()获取当前目录返回列表
print(os.listdir())

# 修改所有文件名(将文件名为Python的文件名删除Python)
for name in os.listdir():
    if name[:6] == 'Python':
        new_name = name[6:]
        os.rename(name, new_name)


