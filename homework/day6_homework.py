# 作者: 刘澍
# 2024 年 12 月 30 日 17 时 38 分 03 秒
# 1395698435@qq.com

# homework1：练习封装
class Person:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __str__(self):
        return f'我的名字叫{self.name} 体重{self.weight}公斤'

    def run(self):
        print(f'{self.name}爱跑步，跑步锻炼身体')
        self.weight -= 0.5

    def eat(self):
        print(f'{self.name}是吃货，吃完这顿再减肥')
        self.weight += 1


class HouseItem:
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return f'[{self.name}]占地{self.area}'


class House:
    def __init__(self, house_type, area):
        self.house_type = house_type
        self.area = area
        self.free_area = area  # 剩余面积
        self.item_list = []  # 家具名称列表

    def __str__(self):
        return f'户型{self.house_type}\n总面积：{self.area}[剩余：{self.free_area}]\n家具：{self.item_list}'

    def add_item(self, item: HouseItem):
        print(f'要添加{item}')
        if item.area > self.free_area:  # 判断家具面积是否大于剩余面积
            print(f'{item.name}的面积太大，不能添加到房子中')
            return
        self.item_list.append(item.name)  # 将家具的名称追加到名称列表中
        self.free_area -= item.area  # 计算剩余面积


class Gun:
    def __init__(self, model):
        self.model = model
        self.bullet_count = 0

    def add_bullet(self, count):
        self.bullet_count += count

    def shoot(self):
        if self.bullet_count <= 0:  # 判断是否还有子弹
            print('没有子弹了')
            return
        self.bullet_count -= 1  # 发射一颗子弹
        print(f'{self.model}发射子弹[{self.bullet_count}]')


class Soldier:
    def __init__(self, name, gun: Gun = None):
        self.name = name
        self.gun = gun

    def fire(self):
        if self.gun is None:  # 判断士兵是否有枪
            print(f'[{self.name}]还没有枪')
            return
        print(f'冲啊[{self.name}]')  # 高喊口号
        self.gun.add_bullet(50)  # 让枪装填子弹
        self.gun.shoot()  # 让枪发射子弹


# homework2 私有属性和私有方法练习
class Women:
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # 私有属性

    def __secret(self):  # 私有方法
        print(f'我的年龄是{self.__age}')

    def boyfriend(self):
        self.__secret()


# homework3 单继承和多继承练习
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print('吃')

    def drink(self):
        print('喝')

    def run(self):
        print('跑')

    def sleep(self):
        print('睡')


class Dog(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def bark(self):
        print(f'{self.color}的在{self.name}汪汪叫')

    def run(self):
        super().run()
        print(f'{self.name}跑的快')


class XiaoTianQuan(Dog):
    def __init__(self, name, color, age):
        super().__init__(name, color)
        self.age = age

    def fly(self):
        print(f'{self.color}的{self.name}能飞天--{self.age}')

    def bark(self):
        print('神一样的叫唤')  # 针对子类特有的需求，编写代码
        super().bark()  # 使用 super(). 调用原本在父类中封装的方法


# 多重继承
class A:
    def test(self):
        print('A test')


class B:
    def test(self):
        print('B test')


class C(A, B):
    def test(self):
        print('C test')


# 多继承的init问题
# *args实现
# class Parent:
#     def __init__(self, height):
#         self.height = height
#
#
# class Son1(Parent):
#     def __init__(self, age, *args):
#         self.age = age
#         super().__init__(*args)
#
#
# class Son2(Parent):
#     def __init__(self, score, *args):
#         self.score = score
#         super().__init__(*args)
#
#
# class Grandson(Son1, Son2):
#     def __init__(self, name, *args):
#         self.name = name
#         super().__init__(*args)

# **kwargs实现
class Parent:
    def __init__(self, height):
        self.height = height


class Son1(Parent):
    def __init__(self, age, **kwargs):
        self.age = age
        super().__init__(**kwargs)


class Son2(Parent):
    def __init__(self, score, **kwargs):
        self.score = score
        super().__init__(**kwargs)


class Grandson(Son1, Son2):
    def __init__(self, name, **kwargs):
        self.name = name
        super().__init__(**kwargs)


# homework4 单例模式练习
class MusicPlayer(object):
    instance = None
    init_flag = False

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self, name):
        self.name = name
        if not MusicPlayer.init_flag:
            print('初始化音乐播放器')
            MusicPlayer.init_flag = True


# homework5 异常捕获练习 判断对称数
def use_exception():
    """
    通过try进行异常捕捉
    确保输入的内容一定是一个整型数
    然后判断该整型数是否是对称数
    12321就是对称数
    123321也是对称数
    :return:
    """
    # myException = Exception('不是对称数')
    try:
        num = int(input('请输入整数：'))
        print(num)
    except ValueError:
        print('请输入正确的整数')
        return
    else:
        num_str = str(num)  # 将数字转换为字符串
        if num_str == num_str[::-1]:  # 检查字符串是否与其反转形式相等
            print(f'{num}是对称数')
        else:
            raise Exception(f'{num}不是对称数')
            # raise myException
    finally:
        print('执行完成，但是不保证正确')  # 不受return影响


if __name__ == '__main__':
    # homework1
    # 大象爱跑步问题
    elephant = Person('大象', 75)
    elephant.run()
    elephant.eat()
    print(elephant)
    tiger = Person('老虎', 45)
    tiger.run()
    tiger.eat()
    print(tiger)
    print('-' * 50)
    # 摆放家具问题
    #  1.创建家具
    bed = HouseItem("席梦思", 4)
    chest = HouseItem("衣柜", 2)
    table = HouseItem("餐桌", 1.5)
    print(bed)
    print(chest)
    print(table)
    # 2.创建房子对象
    my_home = House("两室一厅", 60)
    # 3.添加家具
    my_home.add_item(bed)
    my_home.add_item(chest)
    my_home.add_item(table)
    print(my_home)
    print('-' * 50)
    # 士兵突击
    # 1.创建枪对象
    ak47 = Gun('ak47')
    # 2.创建士兵对象
    xusanduo = Soldier('许三多')
    xusanduo.fire()
    xusanduo.gun = ak47
    xusanduo.fire()
    print('-' * 50)

    # homework2
    xiaofang = Women('小芳', 18)
    # 私有属性，外部不能直接访问
    # print(xiaofang.__age)
    # 私有方法，外部不能直接调用
    # xiaofang.__secret()
    xiaofang.boyfriend()
    print('-' * 50)

    # homework3
    # 单继承
    # 创建一个对象-狗对象
    wangcai = Dog('旺财', '黄色')
    wangcai.eat()
    wangcai.drink()
    wangcai.run()
    wangcai.sleep()
    wangcai.bark()
    xtq = XiaoTianQuan('哮天犬', '黑色', 18)
    xtq.bark()
    xtq.fly()
    print('-' * 50)
    # 多重继承
    c = C()
    c.test()
    print(C.__mro__)
    print('-' * 50)
    # 多继承的init问题
    # xiaoming = Grandson('小明', 18, 98.5, 175)  # 姓名，年龄，分数,身高
    xiaoming = Grandson('小明', age=18, score=98.5, height=175)
    print(xiaoming.name)
    print(xiaoming.age)
    print(xiaoming.score)
    print(xiaoming.height)
    print(Grandson.__mro__)
    print('-' * 50)

    # homework4
    # 创建多个对象
    player1 = MusicPlayer('天外来物')
    print(id(player1))
    player2 = MusicPlayer('租购')
    print(id(player2))
    print(player1.name)
    print(player2.name)
    print('-' * 50)

    # homework5
    use_exception()
