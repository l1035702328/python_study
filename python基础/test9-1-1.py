# coding = utf-8
# 实例方法、静态方法和类方法
class Dog1:
    def __init__(self):
        print("这是一个实例方法")

    def sit(self):
        print("dog1 is sitting,from {}".format(self))
        return self

class Dog2:
    def __init__(self):
        print("这是一个静态方法")

    @staticmethod
    def sit():
        print("dog2 is sitting,not self")

    def eat(self):
        print("dog2 is eat,from {}".format(self))


class Dog3:
    def __init__(self):
        print("这是一个类方法")

    @classmethod
    def sit(cls):
        print("dog3 is sit ,from {}".format(cls))
        return cls

    @staticmethod
    def eat():
        print("dog3 is eat")

if __name__ == '__main__':
    # 实例方法 实例方法需要实例化加载
    dog1 = Dog1()
    dog11 = dog1.sit()
    dog11.sit()
    # 静态方法
    Dog2.sit()
    # 类方法 类方法没有实例化加载过
    dog33 = Dog3.sit()
    dog33.sit()
