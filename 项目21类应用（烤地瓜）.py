# 创建地瓜的类
class SweetPotato(object):
    # 地瓜属性初始化
    def __init__(self):
        # 烤的总时间
        self.cook_time = 0
        # 地瓜的初状态
        self.cook_state = '生的'
        # 地瓜的配料
        self.condiments = []
    # 烤地瓜隔一段时间拿出来看烤的状态
    def make_cook_time(self, time):
        self.cook_time += time
        if self.cook_time < 3:
            pass
        elif 3 <= self.cook_time < 5:
            self.cook_state = '半生不熟'
        elif 5 <= self.cook_time < 8:
            self.cook_state = '熟了'
        else:
            self.cook_state = '烤糊了'
    def make_condiments(self, condiment):
        self.condiments.append(condiment)
    def __str__(self):
        return f'这个地瓜被烤了 {self.cook_time}分钟\n' \
               f'状态是 {self.cook_state}\n' \
               f'配料有 {self.condiments}'
# 创建地瓜对象
sp = SweetPotato()
import random
while sp.cook_time < 5:
    i = random.randint(2, 4)
    sp.make_cook_time(i)
    print(sp)
sp.make_condiments('辣椒')
sp.make_condiments('番茄酱')
print(sp)











