# 作者: 刘澍
# 2024 年 12 月 27 日 18 时 57 分 36 秒
# 1395698435@qq.com


def use_tuple():
    # 创建空元组
    tuple1 = ()
    # 元组中只包含一个元素的情况，需要加逗号，不加逗号就是整形元素
    tuple2 = (17,)

    # 元组的基本使用
    my_tuple = ('zhangsan', 18, 1.75)

    # 1.取值和取索引
    print(my_tuple[0])
    # 已知内容，求索引
    print(my_tuple.index(18))
    print('-' * 50)

    # 2.统计计数
    print(my_tuple.count(1.75))
    # 统计元组中包含元素的个数
    print(len(my_tuple))
    print('-' * 50)

    # 3.使用迭代遍历元组
    for i in my_tuple:
        print(i)
    print('-' * 50)

    # 4.格式化字符串
    print('%s 年龄是 %d 身高是 %.2f' % my_tuple)
    my_str = '%s 年龄是 %d 身高是 %.2f' % my_tuple
    print(my_str)
    print('-' * 50)

    # 元组和列表之间的转换，list函数把元组转换成列表，tuple函数把列表转换成元组
    print(list(my_tuple))
    my_list = ['lisi', 19, 180]
    print(tuple(my_list))


def use_dict():
    xiaoming = {"name": "小明",
                "age": 18,
                "gender": True,
                "height": 1.75}
    print(xiaoming.keys())  # 所有key列表
    print(xiaoming.values())  # 所有value列表
    print(xiaoming.items())  # 所有(key,value)元组列表

    # 字典的基本使用
    xiaoming_dict = {"name": "小明"}

    # 1.取值
    print(xiaoming_dict["name"])
    # 在取值的时候，如果指定的key不存在，程序会报错！
    # print(xiaoming_dict["name123"])
    print('-' * 50)

    # 2. 增加/修改
    # 如果key不存在，会新增键值对
    xiaoming_dict["age"] = 18
    # 如果key存在，会修改已经存在的键值对
    xiaoming_dict["name"] = "小小明"
    print(xiaoming_dict)
    print('-' * 50)

    # 3. 删除
    xiaoming_dict.pop("name")
    # 在删除指定键值对的时候，如果指定的key不存在，程序会报错！
    # xiaoming_dict.pop("name123")
    print(xiaoming_dict)
    print('-' * 50)

    xiaoming_dict = {"name": "小明", "age": 18}
    # 4.统计键值对数量
    print(len(xiaoming_dict))
    print('-' * 50)

    # 5.合并字典
    temp_dict = {"height": 1.75, "age": 20}
    # 注意：如果被合并的字典中包含已经存在的键值对，会覆盖原有的键值对
    xiaoming_dict.update(temp_dict)
    print(xiaoming_dict)
    print('-' * 50)

    # 6. 清空字典
    xiaoming_dict.clear()
    print(xiaoming_dict)
    print('-' * 50)

    xiaoming_dict = {"name": "小明", "qq": "123456", "phone": "10086"}
    # 7.迭代遍历字典
    # 变量k是每一次循环中，获取到的键值对的key
    for k in xiaoming_dict:
        print("%s - %s" % (k, xiaoming_dict[k]))
    print('-' * 50)
    for k, v in xiaoming_dict.items():
        print("%s - %s" % (k, v))
    print('-' * 50)
    for k, v in xiaoming_dict.items():
        print(f'key - {k}, value - {v}')
    print('-' * 50)

    # 将 多个字典 放在 一个列表 中，再进行遍历
    card_list = [{"name": "张三", "qq": "12345", "phone": "110"},
                 {"name": "李四", "qq": "54321", "phone": "10086"}
                 ]
    for card_info in card_list:
        print(card_info)
    print('-' * 50)


def use_str():
    str1 = "Hello Python"
    for c in str1:
        print(c)
    print('-' * 50)
    print(len(str1))  # 获取字符串的长度
    print('-' * 50)
    print(str1.count('llo'))  # 小字符串在大字符串中出现的次数
    print('-' * 50)
    print(str1[0])  # 从字符串中取出单个字符
    print('-' * 50)
    print(str1.index('thon'))  # 获得小字符串第一次出现的索引
    print('-' * 50)

    # 1.判断类型
    print(str1.isalnum())  # 如果string至少有一个字符并且所有字符都是字母或数字则返回True
    print(str1.isalpha())  # 如果string至少有一个字符并且所有字符都是字母则返回True
    print(str1.isdecimal())  # 如果string只包含数字则返回True
    print('-' * 50)

    # 2.查找和替换
    # 检测str是否包含在string中，如果start和end指定范围，则检查是否包含在指定范围内，如果是返回开始的索引值，否则返回-1(与index区别）,只能用位置参数，不能用keyword
    print(str1.find('llo', 0, len(str1)))
    # 把string中的old_str替换成new_str，如果num指定，则替换不超过num次
    print(str1.replace('Python', 'PyCharm', 2))
    print('-' * 50)

    # 3.大小写转换
    print(str1.lower())  # 转换string中所有大写字符为小写
    print(str1.upper())  # 转换string中的小写字母为大写
    print(str1.swapcase())  # 翻转string中的大小写
    print('-' * 50)

    # 4.拆分和连接
    # 以str为分隔符拆分string，如果num有指定值，则仅分隔num+1个子字符串，str默认包含空格
    print(str1.split())  # string.split(str="", num)
    # splitlines 只是换行，每行字符串的内容不做修改
    str2 = 'hello\nworld\nhello\npython'
    # print(str2)
    print(str2.splitlines())
    # 以string 作为分隔符，将seq中所有的字符以string分割开 print(c.join(list1))列表变为字符串
    list_1 = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    str3 = ''
    print(str3.join(list_1))
    print('-' * 50)

    # 5.字符串的切片
    str4 = 'python'
    print(str4[2:6])  # 截取从2~5位置的字符串
    print(str4[2:])  # 截取从2~末尾的字符串
    print(str4[:6])  # 截取从开始~5位置的字符串
    print(str4[:])  # 截取完整的字符串
    print(str4[::2])  # 从开始位置，每隔一个字符截取字符串
    print(str4[1::2])  # 从索引1开始，每隔一个取一个
    print(str4[2:-1])  # 截取从2~末尾- 1的字符串
    print(str4[-2:])  # 截取字符串末尾两个字符
    print(str4[::-1])  # 字符串的逆序（面试题）


def use_set():
    # 初始化一个空集合
    my_set = set()
    print(my_set)
    print('-' * 50)
    # 为集合添加元素
    # add() 只能添加一个元素，并且如果该元素已存在于集合中，集合不会发生变化（集合不允许重复元素）
    my_set.add('apple')
    my_set.add('banana')
    my_set.add('cherry')
    my_set.add('orange')
    # update() 允许一次性添加多个元素，甚至可以添加多个可迭代对象的元素。如果已经存在的元素在集合中，它们不会被重复添加
    my_set.update(('apple1', 'banana1', 'cherry1', 'orange1'))
    my_set.update(['apple2', 'banana2'])
    my_set.update({'cherry2', 'orange2'})
    print(my_set)
    print('-' * 50)
    # 删除集合中的元素
    my_set.remove('cherry')  # 如果指定的元素不存在于集合中，remove() 会引发 KeyError 异常
    my_set.discard('banana')  # 如果指定的元素不存在于集合中，discard() 不会引发异常，而是直接忽略
    print(my_set)
    print('-' * 50)
    # 移除集合中的所有元素
    # my_set.clear()
    # print(my_set)
    # 拷贝一个集合
    x = my_set.copy()
    print(x)
    print('-' * 50)
    # print(id(my_set))
    # print(id(x))
    # 返回多个集合的差集 difference()方法返回一个移除相同元素的新集合
    x = {"apple", "banana", "cherry"}
    y = {"google", "microsoft", "apple"}
    z = x.difference(y)
    print(z)
    print('-' * 50)
    # 移除集合中的元素，该元素在指定的集合也存在。 difference_update()方法是直接在原来的集合中移除元素，没有返回值
    x = {"apple", "banana", "cherry"}
    y = {"google", "microsoft", "apple"}
    x.difference_update(y)
    print(x)
    print('-' * 50)
    # 返回集合的交集 intersection()方法是返回一个新的集合
    x = {"a", "b", "c"}
    y = {"c", "d", "e"}
    z = {"f", "g", "c"}
    result = x.intersection(y, z)
    print(result)
    print('-' * 50)
    # 返回集合的交集 intersection_update()方法是在原始的集合上移除不重叠的元素
    x = {"a", "b", "c"}
    y = {"c", "d", "e"}
    z = {"f", "g", "c"}
    x.intersection_update(y, z)
    print(x)
    print('-' * 50)
    # 判断两个集合是否包含相同的元素，如果没有返回True，否则返回False
    x = {"apple", "banana", "cherry"}
    y = {"google", "runoob", "facebook"}
    z = x.isdisjoint(y)
    print(z)
    print('-' * 50)
    # 判断指定集合是否为该方法参数集合的子集
    x = {"a", "b", "c"}
    y = {"f", "e", "d", "c", "b", "a"}
    z = x.issubset(y)
    print(z)
    print('-' * 50)
    # 判断该方法的参数集合是否为指定集合的子集
    x = {"f", "e", "d", "c", "b", "a"}
    y = {"a", "b", "c"}
    z = x.issuperset(y)
    print(z)
    print('-' * 50)
    # 返回两个集合中不重复的元素集合
    x = {"apple", "banana", "cherry"}
    y = {"google", "runoob", "apple"}
    z = x.symmetric_difference(y)
    print(z)
    print('-' * 50)
    # 移除当前集合中在另外一个指定集合相同的元素，并将另外一个指定集合中不同的元素插入到当前集合中
    # A+B-AB
    x = {"apple", "banana", "cherry"}
    y = {"google", "runoob", "apple"}
    x.symmetric_difference_update(y)
    print(x)
    print('-' * 50)
    # 返回两个集合的并集
    x = {"apple", "banana", "cherry"}
    y = {"google", "runoob", "apple"}
    z = x.union(y)
    print(z)
    print('-' * 50)
    # 查询
    basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
    print(basket)
    print('orange' in basket)
    print('crabgrass' in basket)
    print('-' * 50)
    # 使用运算符对集合进行操作
    a = set('abracadabra')
    b = set('alacazam')
    print(a)
    print(b)
    print(a - b)  # 在a中不在b中
    print(a | b)  # 在a中或在b中
    print(a & b)  # 在a中且在b中
    print(a ^ b)  # 在a中不在b中或不在a中在b中
    print('-' * 50)
    # 集合也支持推导式形式（语法格式与列表，元组类似）
    a = {x for x in 'abracadabra' if x not in 'abc'}
    print(a)
    print('-' * 50)


def exchange():
    # 交换两个数字
    a = 6
    b = 100
    a, b = b, a  # Python专有，利用元组
    print(a)
    print(b)


def print_info_1(name, gender=True):
    """
    指定函数的缺省参数
    缺省参数，需要使用最常见的值作为默认值！
    如果一个参数的值不能确定，则不应该设置默认值，具体的数值在调用函数时，由外界传递！
    必须保证带有默认值的缺省参数在参数列表末尾
    :param name: 姓名
    :param gender: 性别
    :return:
    """
    gender_text = "男生"
    if not gender:
        gender_text = "女生"
    print("%s 是 %s" % (name, gender_text))


def print_info_2(name, title="", gender=True):
    """
    在调用函数时，如果有多个缺省参数，需要指定参数名，这样解释器才能够知道参数的对应关系！，如果都不指定是可以的，指定一个以后，后面的就必须指定
    :param title: 职位
    :param name: 班上同学的姓名
    :param gender: True 男生 False 女生
    """
    gender_text = "男生"
    if not gender:
        gender_text = "女生"
    print("%s%s 是 %s" % (title, name, gender_text))


if __name__ == '__main__':
    # use_tuple()
    # use_dict()
    # use_str()
    # use_set()
    # exchange()
    print_info_1('小明')
    print_info_1('小明', False)
    print_info_2("小明")
    print_info_2("老王", title="班长")
    print_info_2("小美", gender=False)
