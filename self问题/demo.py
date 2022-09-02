# -*- coding: utf-8 -*-
# @Time    : 2022/9/1 18:39
# @Author  : LZZ
# @FileName: demo.py
# @Software: PyCharm

class AA:
    def __init__(self, aa1, aa2):
        self.aa1 = aa1
        self.aa2 = aa2


class BB:
    cc1 = 7
    def __init__(self, bb1, bb2):
        self.bb1 = bb1
        self.bb2 = bb2


class CC:
    cc1 = 6
    bb = BB

    def __init__(self, cc1=4, cc2=5):
        self.cc1 = cc1
        self.cc2 = cc2

    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("退出")

class Test(object):
    def __init__(self, test1, test2,server):
        self.test1 = test1
        self.test2 = test2
        self.server = server

    def get_value(self):
        print(self.cc_test)

    def get_with(self):
        print(self.server.cc1)

class DD:
    hello = 1
if __name__ == '__main__':
    tt = Test(1,2,CC)
    tt.get_with()


