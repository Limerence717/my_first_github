# 作者: 刘澍
# 2024 年 12 月 25 日 17 时 57 分 35 秒
# 1395698435@qq.com
def func1():
    """
    练习1：
    定义变量赋值不同的数据类型并打印，并使用type
    :return:
    """
    # 数字型
    a = 717
    print(type(a))
    print(a)

    # 浮点型
    b = 7.17
    print(type(b))
    print(b)

    # 布尔型
    print(type(True))
    print(True + 1)
    print(type(False))
    print(False + 1)

    # 复数型
    c = complex(3, 4)
    print(type(c))
    print("c is %d+%dj" % (c.real, c.imag))


def func2():
    """
    练习2：
    将整型转为不同进制，进行输出
    :return:
    """
    a = 717
    print(bin(a))  # 实现整形转换为二进制
    print(hex(a))  # 实现整形转换为十六进制
    print(oct(a))  # 实现整形转换为八进制


def func3():
    """
    练习3：
    实现从1到100之间的奇数求和
    :return:
    """
    result = 0
    i = 1
    while i <= 100:
        if i % 2 == 1:
            result += i
        i += 1

    # for i in range(1, 101):
    #     if i % 2 == 1:
    #         result += i

    print("1到100之间的奇数求和的结果 = %d" % result)

    # 参考答案
    print(sum([x for x in range(1, 101) if x % 2]))


def func4():
    """
    练习4：
    打印九九乘法表
    :return:
    """
    for i in range(1, 10):
        for j in range(1, i + 1):
            if j != i:
                print("%d * %d = %-2d" % (j, i, i * j), end='  ')
            else:
                print("%d * %d = %-2d" % (j, i, i * j))

    # 参考答案
    for i in range(1, 10):
        for j in range(1, i + 1):
            print("%d * %d = %-2d" % (j, i, i * j), end='  ')
            # print(f'{j}*{i}={i * j:<2}', end=' ')  # 左对齐是<2
        print()


def func5():
    """
    练习5：
    统计一个整数对应的二进制数的1的个数。
    输入一个整数（可正可负，负数就按64位去遍历即可），
    输出该整数的二进制包含1的个数（使用位运算）
    :return:
    """
    x = int(input("请输入一个整数："))
    a = x
    count = 0  # 记录整数对应二进制数的1的个数
    index = 64
    if a >= 0:  # 非负整数
        while a > 0:
            temp = a & 1  # 取其二进制最低位
            if temp == 1:
                count += 1
            a = a >> 1
    else:  # 负整数
        while a <= -1 and index > 0:
            temp = a & 1
            if temp == 1:
                count += 1
            a = a >> 1
            index -= 1
    print("%d的2进制中1的个数为%d" % (x, count))

    # 参考答案1
    s = int(input("输入整数"))
    bin_s = bin(s)

    if s >= 0:
        # 正数补码=正数原码
        num = bin_s.count('1')
    else:
        # 对于负数
        num = 64 - bin(-s - 1).count('1')  # 64位，-s-1为原负数补码取反

    print("%d 的2进制中1的个数为%d" % (s, num))

    #  参考答案2
    s = int(input('请输入一个整数'))
    check_bit_flag = 1
    count = 0  # 统计数目
    while check_bit_flag < 2 ** 64:
        if check_bit_flag & s:
            count += 1
        check_bit_flag <<= 1
    print(count)


if __name__ == '__main__':
    # func1()
    # func2()
    # func3()
    # func4()
    func5()
