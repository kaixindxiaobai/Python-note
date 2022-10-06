# 父类
# 子类(父类)----继承父类属性和方法
# 单继承----一个父类继承给一个子类
class A(object):
    def __init__(self):
        self.num = 1
    def print(self):
        print('父类A')
class B(A):
    pass
b = B()
b.print()
print(b.num)

# 多继承-----多个父类继承给一个子类
# 当遇到同名属性或方法时，第一个父类优先
class C(object):
    def __init__(self):
        self.num = 2
    def print(self):
        print('父类C')
class D(A, C):
    pass
d = D()
d.print()
print(d.num)

# 子类重写父类同名方法和属性
class E(A, C):
    def __init__(self):
        self.num = 3
    def print(self):
        print('子类E')
e = E()
e.print()
print(e.num)

# __mro__ 查看类的继承关系
print(E.__mro__)

# 子类中调用父类----需要对父类的方法或属性进行封装
class F(A, C):
    def __init__(self):
        self.num = 3
    def print(self):
        self.__init__()# 因为如果调用过父类后，如果不再次调用子类的初始化，则调用子类方法时，不使用子类的初始属性
        print('子类F')
        print(self.num)
    def a(self):
        A.__init__(self)# 同子类方法中类似
        A.print(self)
    def c(self):
        C.__init__(self)
        C.print(self)
f = F()
f.print()
print(f.num)
f.a()
print(f.num)
f.c()
print(f.num)
f.print()

# 多层继承
class G(F):
    pass
print(G.__mro__)
g = G()
g.print()
# 调用父类C
g.c()

# super()调用父类方法
class H(A):
    def __init__(self):
        self.num = 3
    def print(self):
        self.__init__()
        print('子类H')
        super().__init__()
        super().print()
class I(H):
    def __init__(self):
        self.num = 4
    def print(self):
        self.__init__()
        print('孙类I')
        print(self.num)
    def ha(self):
        '''
        方法一：重新封装同时调用两个父类的属性和方法
        A.__init__(self)
        A.print(self)
        C.__init__(self)
        C.print(self)
        方法二：super()----便于修改，可指定调用父类
        super(当前类名, self).函数()
        方法三：super()无参数----常用，更简洁
        super().函数()
        '''
        super(I, self).__init__()
        super(I, self).print()
print(I.__mro__)
i = I()
i.ha()

# 私有权限----使子类在继承父类时不会默认继承私有属性和方法
# __方法或属性----定义私有属性和方法
# 获取和修改私有属性----私有属性只能在类里修改
class J(A, C):
    def __init__(self):
        self.num = 3
        # 定义私有属性
        self.__money = 1000
    def print(self):
        self.__init__()
        print('子类J')
        print(self.num)
    # 定义私有方法
    def __print1(self):
        print('子类J')
        print(self.num)
    # 获取私有属性
    def get_money(self):
        return self.__money
    # 调用私有方法
    def get_print1(self):
        self.__print1()
    # 修改私有属性
    def set_money(self, num):
        self.__money = num
    def a(self):
        A.__init__(self)
        A.print(self)
    def c(self):
        C.__init__(self)
        C.print(self)
class K(J):
    pass
k = K()
# print(k.money)报错，没有传递给k
# k.print1()报错，没有传递给k
print(k.get_money())
k.set_money(200)
print(k.get_money())

# 调用私有属性和私有方法
# 方法一：对象名._类名__方法或属性名
j = J()
j._J__print1()
print(j._J__money)
# 方法二：在类中调用（类里封装函数对私有属性进行调用）
j.get_print1()
result = j.get_money()
print(result)
