# coding = utf-8
# 私有化 与 @property 目的是getset
# xx: 公有变量
# _x: 单前置下划线,私有化属性或方法，禁止通过from modules import *导入,但是类对象和子类可以访问
# __xx：双前置下划线,避免与子类中的属性命名冲突，无法在外部直接访问(名字重整所以访问不到)，类对象和子类不能访问
# __xx__:双前后下划线,用户名字空间的魔法对象或属性。例如:__init__ , __ 尽量不要自定义这种形式的。
# xx_:单后置下划线,用于避免与Python关键词的冲突

class Test1:
    def __init__(self):
        self.__name = "liu"
        self.old = 2


class Test11(Test1):
    def __init__(self):
        self.dd = 1
        super().__init__()


class Test2:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name


if __name__ == '__main__':
    t1 = Test11()
    print(t1.old)
    # print(t1.__name) 无法访问

    # 这样做的实际意义就是利用getset _name依然可以修改
    t2 = Test2("li")
    t2._name = 4
    print(t2._name)
    t2.name=5
    print(t2.name)
    t2.name = 6
    print(t2.name)


