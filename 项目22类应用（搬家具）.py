# 将小于房子的家具放入房子中
# 创建房子的类
class Home(object):
    def __init__(self, area):
        # 房子面积
        self.area = area
        # 剩余面积
        self.free_area = area
        # 家具列表
        self.furniture = []
    # 添加家具
    def add_furniture(self, furniture):
        if furniture.area <= self.free_area:
            self.free_area -= furniture.area
            self.furniture.append(furniture.name)
        else:
            print('房子空间不足')
    # 房子状况
    def __str__(self):
        return f'房子空间为{self.area}\n' \
               f'房子剩余为{self.free_area}\n' \
               f'房子中家具有{self.furniture}'
# 创建家具的类
class Furniture(object):
    def __init__(self, name, area):
        self.name = name
        self.area = area

# 创建家具
bed = Furniture('床', 300)
sofa = Furniture('沙发', 200)
football_field = Furniture('足球场', 50000)

# 创建房子
home = Home(3000)
home.add_furniture(bed)
home.add_furniture(sofa)
home.add_furniture(football_field)
print(home)





