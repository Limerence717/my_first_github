# 作者: 刘澍
# 2025 年 01 月 02 日 17 时 27 分 50 秒
# 1395698435@qq.com
from operator import itemgetter, attrgetter
import random
import time
import sys

sys.setrecursionlimit(100000)  # 增加递归深度


# Homework1：二叉树的建树，前序、中序、后序、层序遍历练习
class Node:
    def __init__(self, data=1, lchild=None, rchild=None):
        self.data = data
        self.lchild = lchild
        self.rchild = rchild


class BiTree:
    def __init__(self):
        self.root = None
        self.q = []

    # 建树
    def level_build_tree(self, node: Node):
        self.q.append(node)
        if self.root is None:
            self.root = node
        else:
            if self.q[0].lchild is None:
                self.q[0].lchild = node
            else:
                self.q[0].rchild = node
                self.q.pop(0)

    # 先序遍历
    def pre_order(self, node: Node):
        if node:
            print(node.data, end=' ')
            self.pre_order(node.lchild)
            self.pre_order(node.rchild)

    # 中序遍历
    def in_order(self, node: Node):
        if node:
            self.in_order(node.lchild)
            print(node.data, end=' ')
            self.in_order(node.rchild)

    # 后序遍历
    def post_order(self, node: Node):
        if node:
            self.post_order(node.lchild)
            self.post_order(node.rchild)
            print(node.data, end=' ')

    # 层序遍历
    def level_order(self):
        help_q = []
        help_q.append(self.root)
        while help_q:
            node = help_q.pop(0)
            print(node.data, end=' ')
            if node.lchild:
                help_q.append(node.lchild)
            if node.rchild:
                help_q.append(node.rchild)


# homework2
class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age

    def __repr__(self):
        """
        相对于__str__来说，更方便，可以返回非字符串类型
        :return:
        """
        return repr((self.name, self.grade, self.age))


# homework3：实现快速排序、堆排序
class Sort:
    def __init__(self, n):
        self.len = n
        self.arr = [0] * n
        self.random_data()

    def random_data(self):
        for i in range(self.len):
            self.arr[i] = random.randint(0, 99)

    def partition(self, left, right):
        # 挖坑法
        arr = self.arr
        pivot = arr[left]
        while left < right:
            while left < right and arr[right] >= pivot:
                right -= 1
            arr[left] = arr[right]
            while left < right and arr[left] <= pivot:
                left += 1
            arr[right] = arr[left]
        arr[left] = pivot
        return left

        # 交换法
        # arr = self.arr
        # k = left
        # random_pos = random.randint(left, right)  # 如何避免陷入最坏时间复杂度
        # arr[random_pos], arr[right] = arr[right], arr[random_pos]
        # for i in range(left, right):
        #     if arr[i] < arr[right]:
        #         arr[i], arr[k] = arr[k], arr[i]
        #         k += 1
        # arr[k], arr[right] = arr[right], arr[k]
        # return k

    def quick_sort(self, left, right):
        if left < right:
            pivot = self.partition(left, right)
            self.quick_sort(left, pivot - 1)
            self.quick_sort(pivot + 1, right)

    def adjust_max_heap(self, pos, arr_len):
        arr = self.arr  # 获取堆数组
        parent = pos  # 当前需要调整的父节点位置
        child = parent * 2 + 1  # 左子节点的位置
        while child < arr_len:  # 当子节点在数组范围内时循环
            # 如果右子节点存在且右子节点的值大于左子节点，则选择右子节点
            if child + 1 < arr_len and arr[child] < arr[child + 1]:
                child += 1
            # 如果子节点的值大于父节点的值，则交换父子节点
            if arr[child] > arr[parent]:
                arr[child], arr[parent] = arr[parent], arr[child]
                parent = child  # 将父节点移动到子节点的位置
                child = parent * 2 + 1  # 更新子节点的位置
            else:
                break  # 如果父节点已经大于子节点，则调整完成，退出循环

    def heap_sort(self):
        # 第一步：构建大顶堆
        for parent in range(self.len // 2 - 1, -1, -1):
            self.adjust_max_heap(parent, self.len)
        # 第二步：逐步将堆顶元素（最大值）交换到数组末尾，并调整堆
        arr = self.arr
        arr[0], arr[self.len - 1] = arr[self.len - 1], arr[0]
        for arr_len in range(self.len - 1, 1, -1):
            self.adjust_max_heap(0, arr_len)
            arr[0], arr[arr_len - 1] = arr[arr_len - 1], arr[0]

    def text_time_use(self, sort_func, *args, **kwargs):
        start = time.time()
        sort_func(*args, **kwargs)
        end = time.time()
        print(end - start)


if __name__ == '__main__':
    # homework1
    # bt = BiTree()
    # for i in range(1, 11):
    #     new_node = Node(i)
    #     bt.level_build_tree(new_node)
    # bt.pre_order(bt.root)
    # print()
    # bt.in_order(bt.root)
    # print()
    # bt.post_order(bt.root)
    # print()
    # bt.level_order()
    # print()

    # homework2：sorted的练习
    # 列表
    # my_list = "This is a test string from Andrew".split()
    # print(my_list)
    # # key可以传递一个比较规则的函数,比较规则发生了改变,key就是给它传递一个函数
    # print(sorted(my_list, key=str.lower))
    # print('-' * 50)
    # # 列表嵌套元组
    # student_tuples = [
    #     ('jane', 'B', 12),
    #     ('john', 'A', 15),
    #     ('dave', 'B', 10),
    # ]
    # # lambda表达式，就是匿名函数，匿名函数好处，提高编写效率，提高阅读速度
    # print(sorted(student_tuples, key=lambda x: x[1]))
    # student = Student('john', 'A', 15)
    # student_objects = [
    #     Student('john', 'A', 15),
    #     Student('jane', 'B', 12),
    #     Student('dave', 'B', 10),
    # ]
    # print('-' * 50)
    # print(sorted(student_objects, key=lambda student: student.age))
    # print('使用operator系列')
    # print(sorted(student_tuples, key=itemgetter(0)))
    # print(sorted(student_objects, key=attrgetter('age')))
    # print('使用operator系列,多列排序')
    # print(sorted(student_tuples, key=itemgetter(1, 2)))
    # print(sorted(student_tuples, key=lambda x: (x[1], -x[2])))  # 第一列升序，第二列降序
    # print(sorted(student_objects, key=attrgetter('grade', 'age'), reverse=True))
    # # 字典嵌套列表
    # mydict = {'Li': ['M', 7],
    #           'Zhang': ['E', 2],
    #           'Wang': ['P', 3],
    #           'Du': ['C', 2],
    #           'Ma': ['C', 9],
    #           'Zhe': ['H', 7]}
    # print(sorted(mydict.items(), key=lambda x: x[1][1]))
    # # 列表嵌套字典
    # gameresult = [
    #     {"name": "Bob", "wins": 10, "losses": 3, "rating": 75.00},
    #     {"name": "David", "wins": 3, "losses": 5, "rating": 57.00},
    #     {"name": "Carol", "wins": 4, "losses": 5, "rating": 57.00},
    #     {"name": "Patty", "wins": 9, "losses": 3, "rating": 71.48}]
    # print('-' * 50)
    # print(sorted(gameresult, key=lambda x: x['rating']))
    # # 先按rating，再按name
    # print(sorted(gameresult, key=itemgetter("rating", "name")))

    # homework3
    count = 100000
    my_sort = Sort(count)
    # print(my_sort.arr)
    # my_sort.quick_sort(0, count - 1)
    # my_sort.heap_sort()
    my_sort.text_time_use(my_sort.quick_sort, 0, count - 1)
    my_sort.text_time_use(my_sort.heap_sort)
    # print(my_sort.arr)
