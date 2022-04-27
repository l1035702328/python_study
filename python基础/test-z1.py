# coding = utf-8
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

    def __repr__(self):
        return "this node:({})".format(self._value)

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)

    def depth_first(self):
        yield self
        for c in self:
            yield from c.depth_first()

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

        # Reverse iterator
        def __reversed__(self):
            n = 1
            while n <= self.start:
                yield n
                n += 1

    for rr in reversed(Countdown(30)):
        print(rr)
    for rr in Countdown(30):
        print(rr)


if __name__ == '__main__':
    # 简单迭代器
    # test1()
    # 代理迭代
    # test2()
    # 生成器
    # test3()
    # 实现迭代器协议 看不明白
    # test4()
    test5()





