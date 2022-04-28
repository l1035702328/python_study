# coding = utf-8
from collections import deque
import itertools
# 一个简单的迭代器与生成器
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

def test91():
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
if __name__ == '__main__':
    # 简单迭代器
    # test1()
    # 代理迭代
    # test2()
    # 生成器
    # test3()
    # 实现迭代器协议 看不明白
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
    test9()



















# beat beat beaten
# become became become
# begin began begun
# bite bit bitten
# blow blew blown
# break broke broken
# bring brought brought
# build built built
# buy bought bought
# catch caught caught
# choose chose chosen
# come came come
# cost cost cost
# cut cut cut
# do did done
# draw drew drawn
# drink drank drunk
# drive drove driven
# eat ate eaten
# fall fell fallen
# feel felt felt
# fight fought fought
# find found found
# fly flew flown
# forget forgot forgotten
# get got got
# give gave given
# go went gone
# grow grew grown
# hang hung hung
# have had had
# hear heard heard
# hide hid hidden
# hit hit hit
# hold held held
# hurt hurt hurt
# keep kept kept
# know knew known
# leave left left
# lend lent lent

