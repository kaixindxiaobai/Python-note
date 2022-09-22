# 集合是可变类型，并且有去除同一数据，且顺序不同

# 集合的创建{}，或set()，空集合只能用set()来创建(否则是字典)
set1={10,20,30,40,50,20,20,20,20}
set2={}
set3=set()
print(f'{type(set1)},{type(set2)},{type(set3)}')

# 无序
set2=set('set')
print(set2)

# 去重复
print(set1)

# 集合的增加数据
# add()增加单一数据，若增加数据序列则报错(若增加已有数据，则没变化)
set1.add(60)
print(set1)
# set1.add([0,1,2])-----报错

# update()增加序列，若增加单一数据则报错
set1.update([10,20,70,80])
print(set1)
# set1.update(100)-----报错

# 删除数据
# 集合序列.remove()删除指定数据，没有该指定数据报错
set1.remove(80)
print(set1)
# set1.remove(80)------报错

# discard()同remove，失败不报错,返回None
set1.discard(70)
print(set1)
print(set1.discard(70))
set1.discard(70)
print(set1)

# pop()随机删除数据，并返回这个值
print(set1.pop())
print(set1)

# 集合的查找(in/ not in)判断数据在不在集合里
print(10 in set1)
print(10 not in set1)





