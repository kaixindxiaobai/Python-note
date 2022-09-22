# 推导式作用：化简代码

# 列表推导式：创建一个有规律的列表或控制一个有规律的列表
list1=[i for i in range(10)]
print(list1)

# 带条件判断的推导式
list2=[i for i in range(10) if i%2==0]
print(list2)

# 双循环推导式
list3=[(i,j) for i in range(5) for j in range(2,4)]
print(list3)

# 创建字典推导式
dict1={i:i**2 for i in range(4)}
print(dict1)

# 用字典连接两个列表的推导式
list4=['name','year','class']
list5=['Tom',12,2]
dict2={list4[i]:list5[i] for i in range(len(list4))}
print(dict2)

# 提取字典中的数据
dict3={'1':90,'2':80,'3':75}
count1={key:value for key,value in dict3.items() if value>=80}
print(count1)

# 集合推导式
list6=[1,2,1]
set1={i**2 for i in list6}
print(set1)# ------集合自动去重




