# -*- coding: utf-8 -*-
# @Time    : 2022/9/1 15:03
# @Author  : LZZ
# @FileName: demo.py
# @Software: PyCharm

# 多继承如果第一个父类没有__init__  实例化时如果有传参会交给第二个父类
class MiXin:
    # def __init__(self,mixin1,mixin2):
    #     print("mixin")
    #     print(mixin1,mixin2)
    # pass
    def __init__(self):
        print("hello")

class Father:
    def __init__(self,value1,value2):
        print("father")
        print(value1,value2)

class Son(MiXin,Father):
    pass

if __name__ == '__main__':
    bb = Son(11,22)