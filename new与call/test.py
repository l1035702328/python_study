# -*- coding: utf-8 -*-
# @Time    : 2022/9/5 14:58
# @Author  : LZZ
# @FileName: test.py
# @Software: PyCharm

class Test:
    def __new__(cls, *args, **kwargs):
        inst = object.__new__(cls, *args, **kwargs)
        print(inst)
        return inst

    def __init__(self):
        print("实例化后初始化的方法")

    def hello(self):
        print("hello")

if __name__ == '__main__':
    t1 = Test()
