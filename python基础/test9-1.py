# coding = utf-8
# 继承
# classMethod 工厂方法：它用于创建类的实例，例如一些预处理。如果使用@staticmethod代替，那我们不得不硬编码Pizza类名在函数中，这使得任何继承Pizza的类都不能使用我们这个工厂方法给它自己用。

class Animal:
    def __init__(self, name, old):
        print("loading Animal")
        self.name = name
        self.old = old

    def eye(self):
        print("Animal have eye")

    def nose(self):
        print("Animal have nose")

    def mouth(self):
        print("Animal have mouth")


class Dog(Animal):
    def __init__(self, name="xiaoguai", old=1):
        print("loading Dog")
        # 初始化父类属性这里实例化了父类 或重写父类方法
        super().__init__(name, old)
        # 将实例用作属性
        self.state = State()

    def sit(self):
        print("dog is sitting")

    # 重写父类方法
    def nose(self):
        print("Dog have nose")


class State:
    def state_msg(self):
        print("描述一条动物状态的信息")

if __name__ == '__main__':
    dog = Dog()
    # 仅有实例化时才加载init
    dog.eye()
    print(dog.old)
    print(dog.name)
    # 重写父类方法
    dog.nose()
    # 将实例用作属性
    dog.state.state_msg()
