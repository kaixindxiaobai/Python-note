'''
for 临时变量 in 序列:
    重复执行语句
    ......
'''
list=[1,2,3,4,5,6]
j=0
for i in list:
    print(i)

#while: else:正常执行循环退出（不正常如:break）
i=0
while i<5:
    i+=1
    if i==3:
        #break
        continue
    print(i)
else:
    print('正常退出')

list1=[]
for i in range(0,11):
    list1.append(i)
print(list1)

# for else-----当循环正常运行结束时执行else中的代码，若有break终止时，不执行else的代码
# 当break使循环异常结束时，同时退出了for和else
j=int(input('请输入'))
for i in range(0,11):
    if j==0:
        break
    print(i)
else:
    print('执行了else')
print('完成')




