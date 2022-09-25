#元组是不可变量

#定义元组时用括号，定义单个元组时需要用逗号结尾，否则类型变为定义的数据的类型
tuple1=(10,20,'30','aa','bb','cc')
tuple2=(10)
tuple3=(10,)
print(type(tuple1))
print(type(tuple2))
print(type(tuple3))

#index()查找（元组只支持查找操作），成功返回对应下标，失败报错
print(tuple1.index('bb',0,-1))

#count()统计该数据出现的次数
print(tuple1.count('30'))

#len()元组长度
print(len(tuple1))

#对元组内数据的修改(不能直接修改元组第一层数据，可以修改元组里嵌套列表等可修改的数据类型，列表可修改)
tuple4=(['aa','bb'],)
tuple4[0][0]='cc'
print(tuple4)


