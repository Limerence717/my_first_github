# 作者: 刘澍
# 2024 年 12 月 28 日 17 时 50 分 28 秒
# 1395698435@qq.com

# homework1
# 多个缺省参数的传递练习
def hw_1(name, title="", gender=True):
    """
    在调用函数时，如果有多个缺省参数，需要指定参数名，这样解释器才能够知道参数的对应关系！
    如果都不指定是可以的，指定一个以后，后面的就必须指定
    :param title: 职位
    :param name: 班上同学的姓名
    :param gender: True 男生 False 女生
    """
    gender_text = "男生"
    if not gender:
        gender_text = "女生"
    print("%s%s 是 %s" % (title, name, gender_text))


# homework2
# 多值参数练习
def hw_2(num, *args, **kwargs):
    print(num)
    print(args)
    print(kwargs)


# 计算任意多个数字的和
def sum_numbers(*args):
    num = 0
    for n in args:
        num += n
    print(num)


# 元组和字典的拆包
def unpacking(*args, **kwargs):
    print(args)
    print(kwargs)


# homework3
# 设计类，并实例化一个对象
class Dog:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def bark(self):
        print(f'{self.name}正在汪汪叫')

    def wag_tail(self):
        print(f'{self.name}正在摇尾巴')


if __name__ == '__main__':
    # homework1
    hw_1("小明")
    hw_1("老王", title="班长")
    hw_1("小美", gender=False)
    print('-' * 50)
    # homework2
    hw_2(1, 2, 3, 4, 5, name="小明", age=18, gender=True)
    sum_numbers(1, 2, 3, 4, 5)
    # 需要将一个元组变量/字典变量传递给函数对应的参数
    gl_nums = (1, 2, 3)
    gl_xiaoming = {"name": "小明", "age": 18}
    # 不加*和**会直接把 gl_nums 和 gl_xiaoming 作为元组传递给 args
    unpacking(gl_nums, gl_xiaoming)
    # 在元组变量前，增加一个*，代表元组拆包  在字典变量前，增加两个*，代表字典拆包
    unpacking(*gl_nums, **gl_xiaoming)
    print('-' * 50)
    # homework3
    dog_1 = Dog('大黄', '黄色')
    print(dog_1.name, dog_1.color)
    dog_1.bark()
    dog_1.wag_tail()
    print('-' * 50)
