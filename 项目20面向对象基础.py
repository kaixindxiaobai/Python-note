# 类和对象（现有类再有对象）
# 定义类（类名用大驼峰）
class Washer():
    def wash(self):
        print('wash clothes')
        # 打印self等于打印调用这个函数的对象地址，如haier
        print(self)
# 创建对象
# 对象名 = 类名()
haier = Washer()

# 调试
# 打印haier对象
print(haier)
# 调用wash功能----对象名.wash()
haier.wash()

print('_'*50)

# 一个类创建多个对象
class Washer2():
    def wash2(self):
        print('洗衣服')
        print(self)
haier2 = Washer2()
haier2.wash2()

haier3 = Washer2()
haier3.wash2()

# 类外添加对象属性——————对象名.属性名 = 值
haier2.width = 400
haier2.height = 500

# 类外获取属性 对象名.属性名
print('洗衣机的宽度是%d' % haier2.width)
print('洗衣机的高度是%d' % haier2.height)

# 类里获取属性 self.属性
class Washer3():
    def wash3(self):
        print('洗衣服')
    def print_info(self):
        print(self.width)
        print(self.height)

haier3 = Washer3()
# haier3.print_info()在没有获取属性前调用含属性的函数，报错
haier3.width = 400
haier3.height = 500
haier3.print_info()

# 魔法方法，添加类自带属性（初始化对象）-----会将值定为相同
# __init__(self)默认调用
class Washer4():
    def __init__(self):
        self.width = 400
        self.height = 500
    def wash4(self):
        print('洗衣服')
    def print_info4(self):
        print(self.width)
        print(self.height)

haier4 = Washer4()
haier4.print_info4()

# 定义带参数的init,对多个对象定义时设置不同的参数
class Washer5():
    def __init__(self, width, height):
        # 因为在创建对象时默认调用，所以在创建对象时可直接传参定义实例参数传入
        self.width = width
        self.height = height
    def wash5(self):
        print('洗衣服')
    def print_info5(self):
        print(self.width)
        print(self.height)

haier5 = Washer5(300, 400)# 必须调用参数，否则报错
haier5.print_info5()

# __str__将打印对象时打印对象地址改为返回值
class Washer6():
    def __init__(self, width, height):
        # 因为在创建对象时默认调用，所以在创建对象时可直接传参定义实例参数传入
        self.width = width
        self.height = height
    def __str__(self):
        return '洗衣机说明书'
    def wash6(self):
        print('洗衣服')
    def print_info6(self):
        print(self.width)
        print(self.height)

haier6 = Washer6(500, 600)
print(haier6)

# __del__删除对象时自动调用
class Washer7():
    def __init__(self, width, height):
        # 因为在创建对象时默认调用，所以在创建对象时可直接传参定义实例参数传入
        self.width = width
        self.height = height
    def __str__(self):
        return '洗衣机说明书'
    def __del__(self):
        print('对象已被删除')
    def wash7(self):
        print('洗衣服')
    def print_info7(self):
        print(self.width)
        print(self.height)

haier7 = Washer7(500, 600)
del haier7# 可写也可不写，因代码自动执行完毕后会自动关闭对象

