# 作者: 刘澍
# 2025 年 01 月 03 日 18 时 20 分 06 秒
# 1395698435@qq.com
import copy
import re


# homework1：练习深copy与浅copy
def shallow_copy():
    """
    浅copy，只是copy第一层
    :return:
    """
    a = [1, 2]
    b = [3, 4]
    c = [a, b]
    d = copy.copy(c)
    a[0] = 10
    print(c)
    print(d)


def deep_copy():
    """
    深copy，递归copy所有，形成一个完全独立的
    :return:
    """
    a = [1, 2]
    b = [3, 4]
    c = [a, b]
    d = copy.deepcopy(c)
    a[0] = 10
    print(c)
    print(d)


# homework2：练习正则表达式
def single_match():
    """
    匹配单个字符
    :return:
    """
    # . 匹配任意1个字符（除了\n）
    ret = re.match("t.o", "two")
    print(ret.group())
    # [] 匹配[]中列举的字符
    ret = re.match("[hH]", "hello Python")
    print(ret.group())
    ret = re.match("[hH]", "Hello Python")
    print(ret.group())
    ret = re.match("[0-35-9]Hello Python", "7Hello Python")
    print(ret.group())
    # \d 匹配数字，即0-9 decimal \D 匹配非数字，即不是数字
    ret = re.match(r"嫦娥\d号", "嫦娥1号发射成功")
    print(ret.group())
    ret = re.match(r"嫦娥\d号", "嫦娥2号发射成功")
    print(ret.group())
    ret = re.match(r"嫦娥\d号", "嫦娥3号发射成功")
    print(ret.group())
    # \s 匹配空白，即空格，tab键space \S 匹配非空白
    # \w 匹配单词字符，即a-z、A-Z、0-9、_(汉字)word \W 匹配非单词字符


def multiple_matches():
    """
    匹配多个字符
    :return:
    """
    # * 匹配前一个字符出现0次或者无限次，即可有可无
    ret = re.match("[A-Z][a-z]*", "M")
    print(ret.group())
    ret = re.match("[A-Z][a-z]*", "MnnM")
    print(ret.group())
    ret = re.match("[A-Z][a-z]*", "Aabcdef")
    print(ret.group())
    # + 匹配前一个字符出现1次或者无限次，即至少有1次
    ret = re.match(r'\d+', '123, 4567, and 89.')
    print(ret.group())
    # ? 匹配前一个字符出现1次或者0次，即要么有1次，要么没有
    ret = re.match("[1-9]?[0-9]", "7")
    print(ret.group())
    ret = re.match(r"[1-9]?\d", "33")
    print(ret.group())
    ret = re.match(r"[1-9]?\d", "09")
    if ret:
        print(ret.group())
    # {m} 匹配前一个字符出现m次 {m,n} 匹配前一个字符出现从m到n次
    ret = re.match("[a-zA-Z0-9_]{6}", "12a3g45678")
    print(ret.group())
    ret = re.match("[a-zA-Z0-9_]{8,20}", "1ad12f23s34455ff66")  # 默认贪婪
    print(ret.group())


def group_matching():
    """
    分组匹配
    :return:
    """
    # | 匹配左右任意一个表达式
    ret = re.match(r"[1-9]?\d$|100$", "100")
    print(ret.group())
    # （ab） 将括号中字符作为一个分组
    ret = re.match(r"\w{4,20}@163\.com", "test@163.com")
    print(ret.group())  # test@163.com
    ret = re.match(r"\w{4,20}@(163|126|qq)\.com", "test@126.com")
    print(ret.group())  # test@126.com
    ret = re.match(r"\w{4,20}@(163|126|qq)\.com", "test@qq.com")
    print(ret.group())  # test@qq.com
    ret = re.match(r"\w{4,20}@(163|126|qq)\.com", "test@gmail.com")
    if ret:
        print(ret.group())
    else:
        print("不是163、126、qq 邮箱")
    tels = ["13100001234", "18912344321", "10086", "18800007777"]
    for tel in tels:
        ret = re.match(r"1\d{9}[0-35-68-9]$", tel)
        if ret:
            print(ret.group())
        else:
            print(f"{tel}不是想要的手机号")
    ret = re.match(r"([^-]+)-(\d+)", "010-12345678")  # ([^-]*) 代表没有遇到小横杠-就一直进行匹配，一直匹配下去
    print(ret.group())
    # \num 引用分组num匹配到的字符串
    # 通过引用分组中匹配到的数据即可，但是要注意是元字符串，即类似 r""这种格式
    ret = re.match(r"<([a-zA-Z]*)>\w*</\1>", "<html>hh</html>")
    print(ret.group())
    labels = ["<html><h1>www.cskaoyan.com</h1></html>", "<html><h1>www.cskaoyan.com</h2></html>"]
    for label in labels:
        ret = re.match(r"<(\w*)><(\w*)>.*</\2></\1>", label)
        if ret:
            print("%s 是符合要求的标签" % ret.group())
        else:
            print("%s 不符合要求" % label)
    # (?P<name>) 分组起别名 (?P=name) 引用别名为name 分组匹配到的字符串
    labels1 = ["<html><h1>www.cskaoyan.com</h1></html>", "<html><h1>www.cskaoyan.com</h2></html>"]
    for label in labels1:
        ret = re.match(r"<(?P<name1>\w*)><(?P<name2>\w*)>.*</(?P=name2)></(?P=name1)>", label)
        if ret:
            print("%s 是符合要求的标签" % ret.group())
        else:
            print("%s 不符合要求" % label)


# homework3：search，findall,sub练习
def advanced_use_re():
    """
    re模块的高级用法
    :return:
    """
    # search 只能搜第一个
    ret = re.search(r"\d+", "阅读次数为 9999")
    print(ret.group())
    # findall 返回所有匹配的
    ret = re.findall(r"\d+", "python = 9999, c = 7890, c++ = 12345")
    print(ret)
    #  sub 将匹配到的数据进行替换
    ret = re.sub(r"\d+", '998', "python = 997")
    print(ret)
    ret = re.sub(r"\d+", add, "python = 997")
    print(ret)
    text = "apple apple apple apple"  # 原始文本
    pattern = r"apple"  # 正则表达式模式，用于匹配要替换的内容
    replacement = "orange"  # 替换的内容
    new_text = re.sub(pattern, replacement, text, count=2)  # 指定最多替换的次数。默认值为 0，表示替换所有匹配项。
    print(new_text)


def add(temp):
    strNum = temp.group()
    num = int(strNum) + 100
    return str(num)


def find_second_match(pattern, text):
    matches = re.finditer(pattern, text)
    try:
        next(matches)  # 跳过第一个匹配项
        second_match = next(matches)  # 获取第二个匹配项
        return second_match.group()
    except StopIteration:
        return None


if __name__ == '__main__':
    # homework1
    # shallow_copy()
    # deep_copy()
    # homework2
    # single_match()
    # multiple_matches()
    # group_matching()
    # homework3
    advanced_use_re()
    text = "abc123def456ghi789"
    pattern = r"\d+"
    second_match = find_second_match(pattern, text)
    print(second_match)
