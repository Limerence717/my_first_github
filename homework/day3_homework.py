# 作者: 刘澍
# 2024 年 12 月 26 日 18 时 37 分 17 秒
# 1395698435@qq.com

import day3_homework_4_module


def homework_1():
    """
    有7个整数，其中有3个数出现了两次，1个数出现了一次， 找出出现了一次的那个数。
    :return:
    """
    my_list = [11, 11, 41, 21, 31, 31, 41]
    for i in my_list:
        if my_list.count(i) == 1:  # 找出出现了一次的那个数，找到即可退出循环
            print(i)
            break

    # 参考答案 异或：任何数和0异或得到本身，任何数和非零数异或两次得到其本身，异或满足交换律
    res = 0
    for i in my_list:
        res = res ^ i
    print(res)


def homework_2():
    """
    写一个简单的for循环，从1打印到20，横着打为1排
    :return:
    """
    for i in range(1, 21):
        print(i, end=' ')


def homework_3_say_hello(times):
    """
    写一个say_hello函数打印多次hello并给该函数加备注（具体打印几次依靠传递的参数），然后调用say_hello，
    同时学会快速查看函数备注，及如何跳转到函数实现快捷操作
    :return:
    """
    for i in range(times):
        print('hello')


def homework_5():
    """
    练习列表基本使用，排序，生成式等各种操作
    :return:
    """
    my_list1 = ['zhangsan', 'lisi', 'wangwu']
    # 1.增加
    # 在指定位置插入数据
    my_list1.insert(0, 'liushu')
    # 在末尾追加数据
    my_list1.append('刘澍')
    # 将列表my_list2的数据追加到列表my_list1
    my_list2 = ['张三', '李四', '王五']
    my_list1.extend(my_list2)

    # 2.修改
    # 修改指定索引的数据
    my_list1[0] = '张三'

    # 3.删除
    # 删除指定索引的数据
    del my_list1[0]
    # 删除第一个出现的指定数据
    my_list1.remove('张三')
    # 删除末尾数据
    my_list1.pop()
    # 删除指定索引数据
    my_list1.pop(0)
    # 清空列表
    # my_list1.clear()

    # 4.统计
    # 列表长度
    print(len(my_list1))
    # 数据在列表中出现的次数
    print(my_list1.count('lisi'))
    # 搜某个值的索引值
    print(my_list1.index('李四'))

    # 5.排序
    # 升序排序
    my_list1.sort()
    # 降序排序
    my_list1.sort(reverse=True)
    # 逆序、反转
    my_list1.reverse()

    # 6.列表生成式
    # 简单使用
    a = [x for x in range(10)]
    print(a)
    # 2个for循环
    b = [j for i in range(10) for j in range(i)]
    print(b)
    c = [[col * row for col in range(5)] for row in range(5)]
    print(c)
    d = [j for x in c for j in x]  # 2维列表转1维列表
    print(d)
    # 只有if时
    e = [x for x in range(10) if x % 2 == 1]  # if在后
    print(e)
    # if-else的三元表达式
    f = [x if x % 2 == 0 else x ** 2 for x in range(10)]  # if-else在前
    print(f)


def homework_6():
    """
    有8个整数，其中有3个数出现了两次，2个数出现了一次， 找出出现了一次的那2个数。
    :return:
    """
    my_list1 = [11, 11, 41, 21, 31, 31, 41, 51]
    for i in my_list1:
        if my_list1.count(i) == 1:  # 找出出现了一次的那个数
            print(i)

    # 参考答案
    my_list2 = [1, 1, 2, 2, 3, 6, 6, 8, 3, 9, 8, 10]
    res = 0  # 保存所有数字的异或结果
    res1 = 0  # 保存第一组数字的异或结果
    res2 = 0  # 保存第二组数字的异或结果
    # 第一步：计算所有数字的异或值
    for i in my_list2:
        res = res ^ i
    # 第二步：找到最低位的标志位
    res &= -res  # 获取res最低位为1的那个数，就是用res与-res按位与
    # 第三步：根据标志位分组并异或
    for i in my_list2:
        if res & i:
            res1 ^= i  # 标志位为1的组
        else:
            res2 ^= i  # 标志位为0的组
    # 输出两个只出现一次的数字
    print("%d %d" % (res1, res2))


if __name__ == '__main__':
    # homework_1()
    # homework_2()
    # homework_3_say_hello(7)
    # day3_homework_4_module.output()  # 调用模块对应的函数
    # homework_5()
    homework_6()
