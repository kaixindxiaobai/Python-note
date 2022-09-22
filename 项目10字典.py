#字典是可变类型
#字典分为key键值对:

# 创建新字典，2、3创建空字典
dict1={'name':'Tom','class':3,'gender':'男'}
dict2={}
dict3=dict()
print(type(dict1))

# 字典序列[key]=数据，如果没有该键值对，则增加键值对；如果有该键值对，则修改该键值对的数据
dict2['name']='Join'
dict1['name']='TOM'
print(f'{dict2}\n{dict1}')

# del 字典删除数键值对或数据(删除的目标需要存在)

del dict3        # 删除字典
# print(dict3)--------报错，不存在该字典
# del dict2['Name']#---报错，不存在该键值对

del dict2['name']   # 删除键值对
print(dict2)

#clear()清空
dict1.clear()
print(dict1)

# 查找-------------------------------------------
# key查找，成功返回对应数据，失败报错
dict1={'name':'Tom','class':3,'gender':'男'}
print(dict1['name'])
# print(dict1['names'])------报错，没有names查找失败

# 字典序列.get(key,默认值)查找成功返回对应数据，失败返回默认值（没有默认值则返回None）
print(dict1.get('name'))
print(dict1.get('names'))
print(dict1.get('names','未查找到'))

# 字典序列.keys()返回全部键值对，返回可迭代的对象（可用for进行遍历,列表形式）
print(dict1.keys())

# 字典序列.values()返回全部数据，返回可迭代对象（可用for遍历，列表形式）
print(dict1.values())

# 字典序列.items()返回由(1:key,2:values)组成的元组，可迭代（用列表嵌套元组）
print(dict1.items())


# 字典的遍历
# key的遍历
for key in dict1.keys():
    print(key)

# value的遍历
for value in dict1.values():
    print(value)

# itme的遍历
for item in dict1.items():
    print(item)

# 遍历key拆包(将元组数据1、2在遍历是分给两个临时变量)
for key,value in dict1.items():
    print(f'{key}-->{value}')




