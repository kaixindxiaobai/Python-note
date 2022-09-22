# 定义函数(先定义再调用)
'''
def  函数名（参数）
    代码1
    代码2
    ......
'''

# 创建一个登录界面
def sel_func():
    print('选择1')
    print('选择2')
    print('选择3')
print('选项界面')
sel_func()
print('支付成功')
sel_func()
print('插卡成功')
sel_func()

# 定义使用参数的函数, return 数据----返回函数调用的地方
def add_num1(a,b):
    result=a+b
    return result
result=add_num1(10,20)
print(result)

# help（）函数，用来查看说明文档
print(help(len))

# 注释函数
def sum_numl2(a,b,c):
    '''

    :param a:
    :param b:
    :param c:
    :return:
    '''
    return a+b+c

help(sum_numl2)

# 函数的嵌套调用(嵌套时嵌套函数的定义不必要在外函数前先定义)
def first1():
    print('text1 开始')
    print('text1 执行第一段代码')
    second2()
    print('text1 第二段代码')
    print('text1 结束')

def second2():
    print('text2 开始')
    print('text2 执行代码')
    print('text2 结束')
first1()

# 函数嵌套的运用
def lines():
    print('-',end='')

def rows():
    i=0
    while i<15:
        lines()
        i+=1

j=0
while j<5:
    rows()
    print('')
    j+=1





