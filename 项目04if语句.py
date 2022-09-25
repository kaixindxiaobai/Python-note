# 列表为空时，布朗值为False
list1=[]
if list1:
    print('好')
else:
    print('列表为空')

# 判断运用
c=int(input('请输入'))
if c < 0 or c > 0:
    print('c不等于0')
else:
    print('c=0')

#判断输入与零的关系（将输入转换为整型比较） 多个elif执行时，只要成功执行一个，则中断if
b=None
a=input(b)
if int(a)<0:
    print('a小于0')
elif int(a)>0:
    print('a大于0')
else:
    print('a等于0')
#（将输入直接与字符型比较）
if a>'0':
    print('a大于0')
else :
    print('a小于等于0')

#三目运算符（三元运算符、三元表达式）
#条件成立执行 if 条件 else 条件不成立执行
c = 1 if int(a)>0 else 0
print('a>0成立----%d' % c)

#猜拳游戏
#导入模块import+模块，random随机数
import random
player=int(input('请出拳（0--石头，1--剪刀，2--布）'))
#使用random.randint(开始数字，结束数字)包含开始和结束
computer=random.randint(0,2)
print(computer)
if player==computer:
    print('平局')
elif (player+1)%3==computer:
    print('玩家获胜')
else :
    print('电脑获胜')




