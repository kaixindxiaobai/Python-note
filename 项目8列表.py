#列表是可变类型------------------


#直接赋值=修改
message2=[' hello ',' world ','!!','!!']
message2[-1]="?"
print(message2)

#append()结尾追加，追加的如果是列表，则直接将列表加入原列表
message2.append("A")
print(message2)
message3=['1','2','3','4','5']
message3.append(['6','7'])
print(message3)

#extend()结尾追加，追加的如果是列表，则将列表元素依次添加至原列表
message3=['1','2','3','4','5']
message3.extend(['6','7'])
print(message3)

#insert(位数,字符)插入
message2.insert(-2,"!!")
print(message2)

#del删除,可以删除列表或数据
del message2[-1]
print(message2)
'''
del(message3)
del message3
print(message3)----报错，不存在message#
'''

#remove()按内容删除第一个相等的
message2.remove("!!")
print(message2)
message2.remove("!!")
print(message2)

#pop()弹出
print(message2.pop(-1))
print(message2)

#clear()清空列表，返回空列表
message3.clear()
print(message3)

#sort()排序顺序,reverse=True加入括号表示逆排序，reverse=False表示顺序(一般不用)
message3=["bbcd","abcd","dbcd","cbcd"]
message3.sort()
print(message3)
message3.sort(reverse=True)
print(message3)

#sorted()临时排序,reverse=True加入括号表示逆排序
print(sorted(message3))
print(message3)

#reverse逆序（没有排序功能）
message2.reverse()
print(message2)
message2.reverse()
print(message2)

#copy()复制列表
print(f'{message3}\n{message2}')
message2=message3.copy()
print(message2)

# 用切片来复制列表（直接用赋值并没有新建一个列表，只是多了一个访问的方式，列表还是原来的列表）
message4=message3[:]
message4[0]='修改'
print(message4+message3)

message5=message3
message5[0]='修改'
print(message5+message3)
message3[0]='dbcd'

#遍历列表
i=0
while i<len(message3):
    print(message3[i])
    i+=1

print('for------')
for j in message3:
    print(j)

#创建办公室随机分配（列表嵌套）
teachers=['伯一','仲二','张三','李四','王五','小六']
offices=[[],[],[]]
import random
for name in teachers:
    j=random.randint(0,2)
    offices[j].append(name)
print(offices)


