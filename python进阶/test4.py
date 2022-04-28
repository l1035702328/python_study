# coding = utf-8
from collections import deque
from collections import Iterable
import itertools
import os
import fnmatch
import gzip
import bz2
import re
# 迭代器与生成器
# isinstance('abc',Ierable) #判断是否是可迭代对象
def test1():
    lists = [1, 3, 5]
    iter_lists = iter(lists)
    print(iter_lists)
    try:
        for i in range(4):
            print(next(iter_lists))
    except StopIteration:
        print("迭代完成")
    # 你也可以手动标记结尾返回
    print(next(iter_lists, None))


# 代理迭代 使用迭代器是面向对象封装性的体现。安全，灵活。
class Node:
    def __init__(self, value):
        self._value = value
        self._children = []

# _repr_ 用于推断对象的"官方"字符串表示形式（包含有关对象的所有信息的表示, _str_ 用于推断对象的“非正式”字符串表示形式（对打印对象有用的表示形式

    def __str__(self):
        return "helloworld"

    # 重构repr 输出对象本身的内容
    def __repr__(self):
        return 'Node({!r})'.format(self._value)

    def add_child(self, node):
        self._children.append(node)

#  自定义容器对象有iter
    def __iter__(self):
        return iter(self._children)

def test2():
    a = Node([1, 3, 5])
    print(a)
    a.add_child(1)
    a.add_child(2)
    a.add_child(4)
    for i in a:
        print(i)

# 使用生成器创建新的迭代模式
# 一个生成器函数主要特征是它只会回应在迭代中使用到的 next 操作。 一旦生成器函数返回退出，迭代终止。我们在迭代中通常使用的for语句会自动处理这些细节，所以你无需担心。
def frange(start, stop, increment):
    x = start
    while x < stop:
        yield x
        x += increment
        print("hello：{}".format(x))

def test3():
    a = frange(1, 20, 4)
    print(next(a))
    print("-----")
    print(next(a))
    # for i in frange(1, 20, 4):
    #     print(i)

# 实现迭代器协议
# 你想构建一个能支持迭代操作的自定义对象，并希望找到一个能实现迭代协议的简单方法。
class Node1:
    def __init__(self, value):
        self._value = value
        self._children = []
        self.aa = []

    def __repr__(self):
        return "this node:({})".format(self._value)

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)

    def depth_first(self):
        yield self
        # 这里迭代了对象本身return了 iter(self._children) 就返回了root的迭代对象
        for c in self:
            for j in c.depth_first():
                yield j
            # yield from c.depth_first()

def test4():
    root = Node1(0)
    child1 = Node1(1)
    child2 = Node1(2)
    root.add_child(child1)
    root.add_child(child2)
    child1.add_child(Node1(3))
    child1.add_child(Node1(4))
    child2.add_child((Node1(5)))
    for ch in root.depth_first():
        print(ch)

# 反向迭代
# 问题:你想反方向迭代一个序列
# 反向迭代仅仅当对象的大小可预先确定或者对象实现了 __reversed__() 的特殊方法时才能生效。 如果两者都不符合，那你必须先将对象转换为一个列表才行
# 很多程序员并不知道可以通过在自定义类上实现 __reversed__() 方法来实现反向迭代

def test5():
    class Countdown:
        def __init__(self, start):
            self.start = start

        # Forward iterator
        def __iter__(self):
            n = self.start
            while n > 0:
                yield n
                n -= 1

        # reversed函数内置有迭代器
        def __reversed__(self):
            n = 1
            while n <= self.start:
                yield n
                n += 1
    for rr in reversed(Countdown(30)):
        print(rr)
    for rr in Countdown(30):
        print(rr)


# 带有外部状态的生成器函数
# 如果 你想让你的生成器暴露外部状态给用户，别忘了你可以简单的将它实现为一个类，然后把生成器函数放到__iter__()方法中过去。
class linehistory:
    def __init__(self, lines, histlen=3):
        self.lines = lines
        self.history = deque(maxlen=histlen)

    def __iter__(self):
        for lineno, line in enumerate(self.lines, 1):
            self.history.append((lineno, line))
            yield line

    def clear(self):
        self.history.clear()

def test6():
    with open('text1.txt') as f:
        lines = linehistory(f)
        for line in lines:      # 返回的是枚举的值 放入队列的是元组
            if 'python进阶' in line:
                for lineno, hline in lines.history:
                    print('{}:{}'.format(lineno, hline), end='')

# 迭代器切片
# 问题:它通过遍历并丢弃直到切片开始索引位置的所有元素。 然后才开始一个个的返回元素，并直到切片结束索引位置
def test7():
    def count(n):
        while True:
            yield n
            n += 1

    c = count(0)
    for x in itertools.islice(c, 10, 20):
        print(x)


# 跳过迭代器的开始部分
# 问题:你想遍历一个可迭代对象，但是它开始的某些元素你并不感兴趣，想跳过它们。
def test8():
    a = ["he", 'mf', 'wee', 3, 6, 2]
    for x in itertools.islice(a, 3, None):
        print(x)

# 排列组合的迭代
# 问题:你想迭代遍历一个集合中元素的所有可能的排列或组合
def test9():
    items = ["a", "a", "b", "c", "d"]
    lists1 = []
    # 排列
    for p in itertools.permutations(items, 3):
        print(p)
        lists1.append(p)
    print(len(lists1))
    lists1.clear()
    # 组合
    # 对于 combinations() 来讲，元素的顺序已经不重要了。 也就是说，组合 ('a', 'b') 跟 ('b', 'a') 其实是一样的(最终只会输出其中一个)。
    for k in itertools.combinations(items, 3):
        print(k)
        lists1.append(k)
    print(len(lists1))

def test9_1():
    items = ["a", "b", "c", "d"]
    lists2 = []
    for i in items:
        for j in items:
            for k in items:
                for s in items:
                    if i != j and i != k and i != s and j != k and j != s and k != s:
                        print("{}{}{}{}".format(i, j, k, s))
                        lists2.append("{}{}{}{}".format(i, j, k, s))
    print(len(lists2))


# 序列上索引值迭代
def test10():
    items = ["a", "b", "c", "d"]
    for index, i in enumerate(items, 1):
        print(index)


# 同时迭代多个序列
def test11():
    xds = ["a", "b", "c"]
    yds = [1, 2, 3]
    for i, j in zip(xds, yds):
        print(i, j)

    for i in zip(xds, yds):
        print(type(i))
        print(i)


# 创建数据处理管道
def gen_find(filepat, top):
    '''
    Find all filenames in a directory tree that match a shell wildcard pattern
    '''
    for path, dirlist, filelist in os.walk(top):
        for name in fnmatch.filter(filelist, filepat):
            yield os.path.join(path, name)

def gen_opener(filenames):
    '''
    Open a sequence of filenames one at a time producing a file object.
    The file is closed immediately when proceeding to the next iteration.
    '''
    for filename in filenames:
        if filename.endswith('.gz'):
            f = gzip.open(filename, 'rt')
        elif filename.endswith('.bz2'):
            f = bz2.open(filename, 'rt')
        else:
            f = open(filename, 'rt')
        yield f
        f.close()

def gen_concatenate(iterators):
    '''
    Chain a sequence of iterators together into a single sequence.
    '''
    for it in iterators:
        yield from it

def gen_grep(pattern, lines):
    '''
    Look for a regex pattern in a sequence of lines
    '''
    pat = re.compile(pattern)
    for line in lines:
        if pat.search(line):
            yield line

def test12():
    print("略")


# 展开嵌套的序列
# 问题:你想将一个多层嵌套的序列展开成一个单层列表
def flatten(items, ignore_types=(str, bytes)):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            for i in flatten(x):
                yield i
            # yield from flatten(x)
        else:
            yield x
def test13():
    items = [1, 2, [3, 4, [5, 6], 7], 8]
    for x in flatten(items):
        print(x)



if __name__ == '__main__':
    # 简单迭代器
    # test1()
    # 代理迭代
    # test2()
    # 生成器
    # test3()
    # 实现迭代器协议 多看
    # test4()
    # 反向迭代
    # test5()
    # 带有外部状态的生成器函数
    # test6()
    # 迭代器切片
    # test7()
    # 跳过迭代器的开始部分
    # test8()
    # 排列与组合迭代
    # test9()
    # 序列上索引值迭代
    # test10()
    # 同时迭代多个序列
    # test11()
    test13()