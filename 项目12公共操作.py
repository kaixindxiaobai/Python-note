str1='aa'
str2='bb'

list1=['11',22]
list2=[33,'44']

tuple1=(11,'22')
tuple2=('33',44)

dict1={1:11,2:22}
dict2={3:33,4:44}

set1={10,20,'30'}
set2={40,}

# +运算符---合并（字符串，列表，元组）
print(str1+str2)
print(list1+list2)
print(tuple1+tuple2)

# *运算符---复制（字符串，列表，元组）
print(str1*2)
print(list1*2)
print(tuple1*2)

# in运算符---判断元素存在（字符串，列表，元组，字典）
# not in---不存在
print('a' in str1)
print(22 in list1)
print('22' in tuple1)
print(1 in dict1)
print(11 in dict1)
print(11 in dict1.values())
print((1, 11) in dict1.items())

# len()元素长度
print(len(str1))
print(len(list1))
print(len(dict1))
print(len(set1))

# del 目标 或者 del(目标)------删除
del str2
del list2
del(tuple2)
del(dict2)
del(set2)
''' print(f'{str2}{list2}{tuple2}{dict2}{set2}')----报错'''

# max返回序列中最大值
# min返回序列中最小值
str2='acde'
print(max(str2))
'''print(max(list1))----元素中类型不同'''
list2=[11,22]
print(max(list2))
print(max(dict1))
set2={40,30}
print(max(set2))

# range(start,end,step)生成一系列可迭代对象   (不包含end位  ，step可不写，默认为1   ，可不写start,若不写则为1)
for i in range(1,10):
    print(i)

for i in range(1,10,3):
    print(i)

# enumerate(可遍历对象，start=0)   返回值为元组（对应元素位置，对应元素）     （start用来修改对应元素位置的起始值，可不写，默认值为0）
for i in enumerate(list1):
    print(i)
for i in enumerate(list2,start=1):
    print(i)

# 容器类型的转换:tuple转换为元组，list转换为列表，set转换为集合
print(tuple(str1))
print(list(list1))
print(set(tuple1))


