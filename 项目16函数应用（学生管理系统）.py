# 整体框架
# 创建一个全局定义的列表来存储学生
info = []

# 定义功能函数
# 定义添加功能
def append_student():
    global info
    name_student = input('请输入学生姓名:')
    id_student = input('请输入学号:')
    tel_student = input('请输入手机号:')
    for info_dict in info:
        if name_student == info_dict['name']:
            print('该学生已存在')
            return
    info.append({'name': name_student, 'id': id_student, 'tel': tel_student})
# 定义删除功能
def del_student():
    global info
    name_student = input('请输入学生姓名:')
    for info_dict in info:
        if name_student == info_dict['name']:
            info.remove(info_dict)
            print(info)
            break
    else:
        print('未查找到该学生')
# 定义修改功能
def remove_student():
    global info
    name_student = input('请输入学生姓名:')
    for info_dict in info:
        if name_student == info_dict['name']:
            info_dict['id'] = input('请输入学号:')
            info_dict['tel'] = input('请输入手机号:')
            break
    else:
        print('未查找到该学生')
# 定义查找功能
def find_student():
    global info
    name_student = input('请输入学生姓名:')
    for info_dict in info:
        if name_student == info_dict['name']:
            print(info_dict['name'])
            print(info_dict['id'])
            print(info_dict['tel'])
            return
    else:
        print('未查找到该学生')
# 定义显示全部数据功能
def all_student():
    print('姓名\t学号\t手机号')
    for info_dict in info:
        print(f"{info_dict['name']}\t{info_dict['id']}\t{info_dict['tel']}")
# 建立功能界面
while True:
    print('进入学生管理系统')
    print('-'*20)
    print('1、添加学生')
    print('2、删除学生')
    print('3、修改学生')
    print('4、查找学生')
    print('5、显示全部')
    print('6、退出系统')
    print('-'*20)
    # 用户输入选择
    user_input = int(input('请输入使用的功能:'))
    # 功能选择
    # 添加学生
    if user_input == 1:
        print('添加学生')
        append_student()
    # 删除学生
    elif user_input == 2:
        print('删除学生')
        del_student()
    # 修改学生
    elif user_input == 3:
        print('修改学生')
        remove_student()
    # 查找学生
    elif user_input == 4:
        print('查找学生')
        find_student()
    # 显示全部
    elif user_input == 5:
        print('显示全部')
        all_student()
    # 退出系统
    elif user_input == 6:
        print('6、退出系统')
        break
    else:
        print('未按指定输入')










