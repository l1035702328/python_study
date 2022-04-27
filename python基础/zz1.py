class Node:
    def __init__(self, value):
        self._children = []
        # value用来标识实例化对象体现重构repr的价值
        self._value = value

    def __iter__(self):
        return iter(self._children)

    def __repr__(self):
        return "number is {}".format(self._value)

    def children(self):
        return self._children

    def add_children(self, value):
        self._children.append(value)




if __name__ == '__main__':
    node = Node(1)
    print(node)
    node.add_children(3)
    node.add_children(4)
    for i in node:
        print(i)
