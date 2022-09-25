# 高阶函数(函数可作为参数传入)
# abs(数字)-----取数字的绝对值
print(abs(-10))

# round(数字)----对数字四舍五入
print(round(1.2))
print(round(1.5))

# 高阶函数体验(通过改变传入的函数来提高函数的灵活性)
def sum_num(a, b, f):# 高阶函数
    return f(a) + f(b)
print(sum_num(10, -20, abs))
'''求两数的绝对值的和'''

print(sum_num(2.6, 2.3, round))
'''求两数的整数和'''

# 内置高阶函数map,reduce,filter
# map(func函数功能, lst可迭代数据)--------将传入的函数变量func作用到lst的每个元素中，返回迭代器
list1 = [1, 2, 3]
def func(x):
    return x ** 2
result = map(func, list1)
print(result)
print(list(result))

# reduce(func, lst)------func必须有两个参数， 每次func的计算结果都与列表的下一个元素做累积计算
import functools
'''导入reduce的模块'''
def func(x, y):
    return x + y
result = functools.reduce(func, list1)
print(result)

# filter(func, lst)------将可迭代对象的元素过滤，过滤不满足条件的元素，返回迭代器
list2 = [1, -2, 3, -4, 5]
func = lambda x: x >= 0
result = filter(func, list2)
print(result)
print(list(result))


