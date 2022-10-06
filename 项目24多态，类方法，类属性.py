# 面向对象三大特性：封装，继承，多态
# 封装：将属性和方法封装到类里，封装私有方法和属性
# 继承：子类默认继承父类的所有方法和属性，可重写父类方法和属性
# 多态：传入不同对象，产生不同结果
# 多态：子类重写父类，调用不同的子类产生不同的结果
'''
定义父类
定义子类，重写父类
创建对象，调用不同功能
'''
class Dog(object):
    def work(self):
        print('接收指令')
class Army(Dog):
    def work(self):
        print('追击敌人')
class Drug(Dog):
    def work(self):
        print('追查毒品')
class Person(object):
    def work_dog(self, dog):
        dog.work()
ad = Army()
dd = Drug()
person = Person()
person.work_dog(ad)
person.work_dog(dd)

# 类属性：类对象所拥有的属性，该类的实例对象共有，只有一份空间，节省空间
# 可通过对象访问，也可用类进行访问
class A(object):
    num = 1
a = A()
print(A.num)
print(a.num)

# 修改类属性只能通过类修改,如果通过对象修改，则为创建了一个和类属性同名的实例属性
A.num = 10
print(A.num)
print(a.num)

# 类方法:需要使用类对象时（如需要访问私有类属性或类属性时）
# 需要用装饰器@classmethod标识类方法，参数为cls
class B():
    __num = 2
    @classmethod
    def get_num(cls):
        return cls.__num
b = B()
result = b.get_num()
print(result)

# 静态方法：既不需要类对象（如类属性，类方法，创建实例等）也不需要使用实例对象（如实例对象，实例属性）时，定义静态方法
# 不需要参数的传递，减少不必要的内存
# 既能用对象访问，也能用类访问
# 需要用@staticmethod修饰
class C(object):
    @staticmethod
    # 括号不传参
    def print_():
        print('这是静态方法')
        num = 10
        return num
cc = C()
cc.print_()
C.print_()
print(C.print_())

class D():
    num = 10
    def n(cls):
        cls.num += 1
d = D()
d.num
print(d.num)





