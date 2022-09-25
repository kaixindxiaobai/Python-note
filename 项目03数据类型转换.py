a='1'
b=10
c=['1','2','3']
#int()转为整型
a=int(a)
print(type(a))

#str()转为字符串
print(type(str(b)))

#float()转为浮点型
print(type(float(b)))

#tuple()转为元组
c=tuple(c)
print(type(c))

#list()转为列表
c=list(c)
print(type(c))

#eval()转为对应的类型
str1='1'
str2='1.2'
str3='[1,2,3]'
str4='(1,2,3)'
print(type(eval(str1)))
print(type(eval(str2)))
print(type(eval(str3)))
print(type(eval(str4)))






