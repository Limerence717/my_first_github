# 作者:刘澍
# 2024年12月31日17时27分30秒
# 1395698435@qq.com
import os
import sys
# homework1：包的使用
import hw_7


# homework2:文件的文本模式的读写
def open_r():
    """
    练习读取文件，r模式
    :return:
    """
    file = open('file1.txt', mode='r', encoding='utf-8')
    text = file.read()
    print(text)
    file.close()


def open_rw():
    """
    练习r+模式
    :return:
    """
    file = open('file1.txt', mode='r+', encoding='utf-8')
    text = file.read()
    print(text)
    file.write('liushu')  # 写到文件末尾
    file.close()


def open_w():
    """
    练习w模式
    :return:
    """
    file = open('file1.txt', mode='w', encoding='utf-8')
    file.write('liushu')  # 文件不存在就会创建，存在就会清空
    file.close()


def open_a():
    """
    练习a模式，每次写的时候写到文件末尾
    :return:
    """
    file = open('file1.txt', mode='a', encoding='utf-8')
    file.write('how')  # 使用r+模式，打开后在开头，内容直接覆盖
    file.close()


def use_readline():
    # 打开文件
    file = open("file1.txt", encoding='utf8')

    while True:
        # 读取一行内容
        text = file.readline()

        # 判断是否读到内容,读取到文件末尾拿到的是一个空字符串
        if not text:
            break

        # 每读取一行的末尾已经有了一个 `\n`
        print(text, end="")

    # 关闭文件
    file.close()


# homework3:目录的listdir，getcwd,chdir的使用
def use_dir_func():
    file_list = os.listdir('.')
    print(file_list)
    # os.mkdir('dir1')
    # os.mkdir('dir2')
    print(os.getcwd())
    os.chdir('dir2')
    file = open('file1.txt', mode='w', encoding='utf-8')
    print(os.getcwd())
    file.close()


# homework4:python的传参练习
def write_hello(file_path):
    file = open(file_path, 'w+', encoding='utf-8')
    file.write('hello')
    file.close()


if __name__ == '__main__':
    # homework1
    # hw_7.send_message.send()
    # txt = hw_7.receive_message.receive()
    # print(txt)

    # homework2
    # open_r()
    # open_rw()
    # open_w()
    # open_a()
    # use_readline()

    # homework3
    # use_dir_func()

    # homework4
    write_hello(sys.argv[1])
