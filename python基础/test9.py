# coding = utf-8
# 面向对象 类
class Dog:
    def __init__(self, name, age):
        print("dog name is {}, it is {} old".format(name, age))
        self.name = name
        self.age = age
        # 属性指定默认值
        self.active = 0

    def sit(self):
        print("{} is sitting".format(self.name))

    def roll_over(self):
        print("{} is roll_over".format(self.name))


if __name__ == '__main__':
    dog = Dog("xiaoguai", "13")
    dog.sit()
    dog.roll_over()
    # 多个实例
    mydog = Dog("wodegou", "15")
    youdog = Dog("nidegou","66")
    mydog.sit()
    youdog.sit()