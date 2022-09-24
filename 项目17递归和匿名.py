# 递归函数，函数内部自己调用自己（必须有出口）
# 用递归进行累加
def return_num(a):
    '''
    累加函数
    6的累加和=3+2的累加和（调用函数）
    2的累加和=2+1的累加和（调用函数）
    1的累加和=1（返回）
    '''
    if a <= 1:
        # 出口
        return 1
    return a + return_num(a-1)
print(return_num(3))

# lambda表达式(匿名函数):可简化函数（当函数有一个返回值（只能返回一个值），且只有一个表达式的时候）
# lambda 参数列表（可省略）: 表达式（不可省略，结果直接返回）
def fn1():
    return 10
print(fn1)
print(fn1())

fn2 = lambda: 10
print(fn2)
print(fn2())

# 计算a+b
def fn_1(a, b):
    return a + b
print(fn_1(10,20))

fn_2 = lambda a, b: a + b
print(fn_2(10, 20))

# lambda的参数形式(与函数参数运用方式一致)
# 1、无参数
fn1 = lambda: 1
print(fn1())

# 2、位置参数
fn2 = lambda a, b: a + b
print(fn2(10 ,30))

# 3、关键字参数
fn3 = lambda a, b: a + b
print(fn3(100, b = 200))

# 4、默认参数
fn4 = lambda a, b, c = 100: a + b + c
print(fn4(10, 20))
print(fn4(10, 20, 30))

# 5、可变位置参数
fn5 = lambda *args: args
print(fn5(10, 50, 100))

# 6、可变关键字参数
fn6 = lambda **kwargs: kwargs
print(fn6(name='Tom', age=10))

# 带判断的lambda表达式
def fn1(a, b):
    return a if a > b else b
print(fn1(20, 10))

fn1 = lambda a, b: a if a > b else b
print(fn1(10, 30))

# 列表内字典key的排序
student = [
    {'name': 'Tom', 'age': 10},
    {'name': 'Ant', 'age': 20},
    {'name': 'Bone', 'age': 13},
    {'name': 'Cat', 'age': 14},
]
def sort_1(x):
    return x['name']
student.sort(key=sort_1)
print(student)
# [{'name': 'Ant', 'age': 20}, {'name': 'Bone', 'age': 13}, {'name': 'Cat', 'age': 13}, {'name': 'Tom', 'age': 10}]

student.sort(key=lambda x: x['name'], reverse=True)
print(student)



