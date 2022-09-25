#下标--用来查询字符串中一个指定位置的字符
#字符串是按顺序存储在内存中
name='012345678'
print(name[0])
print(name[2])

#切片:用来查询字符串中一段指定字符串
#序列[开始下标（闭）:结束下标（开）:步长（选取间隔，默认为1，可省略不写，也可为负数）]
print(name[0:5])
print(name[0:7:2])
print(name[:7:2])#开始不写，从头开始
print(name[0::2])#结束不写，写道末尾
print(name[:])#都不写，全部写
print(name[8:5:-1])#倒序，从右往左选取（开始位要大于结束位）
print(name[-4:-1])#从倒数第4位开始数到倒数第1位的前一位（不包含最后一位）



#序列.find(子串,开始位置,结束位置)---在字符串中查找子串,成功则返回该第一个子串第一个下标，失败则返回-1
#rfind---从右侧开始查找
str1='abcde abcde'
print(str1.find('bc',0,-1))
print(str1.find('ac',0,-1))

#index() 与find用法相同，但当查找失败时，则程序报错
#rindex---从右侧开始查找
print(str1.index('bc',0,-1))
'''
print(str1.index('ac',0,-1))--------报错
'''

#count()计算子串出现的次数，用法与find相同
print(str1.count('bc',0,-1))

#序列replace(旧子串,新子串,替换次数（可以省略或超出可替换次数，则全部修改）)  将字符串中指定子串替换成新子串
new_str1=str1.replace('e','efg',10)
print(new_str1)
new_str1=str1.replace('e','efg',1)
print(new_str1)
new_str1=str1.replace('e','efg')
print(new_str1)
print(str1)#字符串未被修改

#序列.split(分割字符,num（分割字符出现的次数）)---按照指定子串对字符串进行分割，并会丢失分割字符，将分割出的用列表装
#所以分割出来的子串与分割字符出现的次数的关系为--子串=分割字符数+1(当首字符串被去掉也不影响，会自动用空来代替)
print(str1.split('bcd'))
print(str1.split('b',1))
print(str1.split('a',1))
print(type(str1.split('bcd')))

#'连接符号'.join(需要合并的列表)---将列表合并为字符串
list1=str1.split('bcd')
'''
tuple1=[1,2,3,4]
print(''.join(tuple1))--------报错，因为只能合并字符串
'''
print('好'.join(list1))
print(''.join(list1))
print(type(''.join(list1)))

#字符串是不可变类型，不能被修改，如replace、title、strip等只能是返回值被改变，而字符串本身没有修改
str2='111'
str2=str2+'222'#这是重新给str2赋值
print(str2)

#字符在规定的字符长度内对齐-----序列.ljust(长度,填充字符)左对齐，rjust右对齐，center中心对齐
print(str2.rjust(10,'.'))
print(str2.center(11,'.'))

#判断字符串是否为指定字符开头-----序列.startswith(子串,开始位置下标，结束下标)，endswith结束
print(str2.startswith('11'))

#判断字符串是否全为字母---序列.isalpha()
#判断字符串是否全为数字---序列.isdigit()
#判断字符串是否全为字母或数字---序列.isalnum()
#判断字符串是否全为空格---序列.isspace()
print(str2.isalpha())
print(str2.isdigit())
print(str2.isalnum())
print(str2.isspace())

#title()首字母大写，upper()全大，lower()全小    (这些函数都是面向字符串，而字符串不能被修改，所以只是返回值被修改)
message1="hello world"
print(message1.title()+"\n"+message1.upper()+"\n"+message1.lower())

#capitalize()-----句首字符大写，甚至其余是大写的也全改成小写
str1='hello World'
print(f'capitalize作用下{str1.capitalize()}')

#strip()删除空白，rstrip()右空白，lstrip()左空白
message2=[' hello ',' world ','!!','!!']
print(message2[0].rstrip(),message2[1].strip())

#str()转字符型
number1=100
print(f"{message1}是{str(number1)}")






