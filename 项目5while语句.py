a=0
while a<5:
    print(10)
    a+=1

#偶数相加1（限制条件）
i=0
a=0
while i<100:
    i+=1
    if i%2==0:
        a=a+i
print(a)

#偶数相加2（控制计数）
i=0
a=0
while i<100:
    i+=2
    a=a+i
print(a)

#有坏苹果和吃饱数量
import random
time=0
apple=0
nothungry = random.randint(3, 5)
print('我想吃%d个苹果'% nothungry)
while time<10:
    bad = random.randint(1, 3)
    time+=1
    if bad==3:
        print('第%d苹果坏了'% time)
        continue
    apple+=1
    if nothungry==apple:
        print('吃了%d第个苹果，吃饱了'% time)
        break
    print('吃了%d第个苹果'% time)
if nothungry!=apple:
    print('没有吃饱')
print('共吃了%d个苹果'% apple)

#打印九九乘法表
j=0
while j<9:
    j+=1
    i=0
    while i<j:
        i+=1
        num=i*j
        print(f'{i}*{j}={num}',end='\t')
    print()#自带换行符







