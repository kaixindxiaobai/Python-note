# 格式化输出(%s可以直接输出其他数据)
num1 = 10
num2 = 12
num3 = 100000
message=['1','2','3','4']
print('%%f=%04d,是%.02f,超出的为原始数据%04d' % (num1, num2, num3))
print(f"{num1}")
print('%s' % num2)
print('%s'%message)

#转义字符（把打印位置分成每4个空为一组，\t则是在光标处往后一组第一个书写）
print(f'000\t1\t{num3}\n\t{num3}00000\t{num1}')
print('\t%10d\t%10d\n\t%10d\t%10d\n'% (num1,num3,num3,num1))

#print结束符end,默认换行
print('好',end="...")
print('好',end="\t")
print('好',end="\n")
print('好',end="\n")
#print自带换行，如果print中加了换行符，则换两行
print()
print(10)
print('\n')
print(10)

#输出转义字符
print('\'   \\n   %%d')

#三引号
print('''hello
world''')

#引号用\连接
print('hello'\
      'world')

# 用+换行
print('hello'+
      'world')

