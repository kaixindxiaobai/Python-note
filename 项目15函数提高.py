# 局部变量和全局变量
a=10     # 全局变量
def text1():
    a=100     # 局部变量
text1()
print(a)

# global 变量——————在函数内修改全局变量
def text2():
    global a   # 声明a为全局变量（直接赋值时的a不是修改了a的值，而是相当于在函数体内重新定义了一个新的全局变量a）
    a=100
text2()
print(a)

# 返回值做参数传递
def text3(a):
    a=a*2
    return a
double1=text3(3)
print(double1)

# 一个函数多个返回值 (列表后可直接接元组、列表、字典来返回多个值,默认返回的是元组）
def text4():
    return 1,2
result1=text4()
print(result1)

def text5():
#    return [1,2,3]
#    return {'text_1':1,'text_2':2}
    return (1,2,3)
result2=text5()
print(result2)

# 函数参数的位置
# 1、位置参数（传递和定义参数的顺序和参数必须一致）
def text6(name,age,gender):
    print(f'您的名字是{name}，年龄是{age}，性别是{gender}')
text6('李华','18','男')#--与函数的形参对应，否则报错

# 2、关键字参数（通过键=值的形式指定）（使函数更加明确，没有顺序的限制）
def text7(name,age,gender):
    print(f'您的名字是{name}，年龄是{age}，性别是{gender}')
text6('张三',age=20,gender='男')  # (位置参数只能在关键字参数之前)
text6('张三',gender='男',age=20)  # (位置参数顺序不影响)

# 3、缺省参数，也叫默认参数，用于定义函数，为参数设置默认值，调用函数时可不传默认参数的值（所有位置参数都必须在缺省参数前）
def text8(name,age,gender='男'):
    print(f'您的名字是{name}，年龄是{age}，性别是{gender}')
text8('Tom',22)
text8('Jone',23,'女')
text8('李四',24,gender='男')

# 4、不定长参数之位置参数，也叫可变参数，用于不确定参数个数（不传参数也可）参数被args收集为元组
def text9(*args):
    print(args)
    for i in args:
        print(i)
text9('hello','world')
text9('hello','world','!')
text9()

# 5、不定长参数之关键字参数，收集所有参数，返回一个字典
def text10(**kwagrs):
    print(kwagrs)
text10(name='你',age='好')
'''name不能加引号，因为name直接作为函数的形参'''

# 拆包:元组
def return1():
    return 1,2
result=return1()
print(result1)
result1,result2=return1()
print(result1)
print(result2)

# 拆包:字典(直接取出键，值需要用键在原字典中提取)
def text11(**kwagrs):
    return kwagrs
result5=text11(name='王五',age='11')
result3,result4=result5
print(result5)
print(result3)
print(result4)
print(result5[result3])
print(result5[result4])

# 交换变量1:定义一个中间变量
a=10
b=20
c=a
a=b
b=c
print(a)
print(b)

# 交换变量2
a,b=1,2
a,b=b,a
print(a,b)

# id()用来查找变量的地址
a=1
b=a
print(id(a),id(b))

# 引用----给调用的地址一个名字来引用（数据都是通过引用进行传递的，也可作实参传入函数）
a = 1
b = a
print(id(a), id(b), a, b)
a = 2
print(id(a), id(b), a, b)# 地址不同，内存需要重新创建了一个新地址来存储新数据，说明int是不可变类型

a = [11]
b = a
print(id(a), id(b), a, b)
b[0] = 22
print(id(a), id(b), a, b)# 地址相同，内存中的列表没变，只是列表发生了改变，说明list是可变类型
b = [33]
print(id(a), id(b), a, b)# 直接改变了列表，相当于重新定义，内存重新开辟空间存储数据

# 数据可直接修改的就是可变类型
# 可变类型：
# 列表，字典，集合
# 不可变类型：
# 整型，浮点型，字符，元组










