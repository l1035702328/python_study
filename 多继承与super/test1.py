# -*- coding: utf-8 -*-
# @Time    : 2022/8/24 17:12
# @Author  : LZZ
# @FileName: test1.py
# @Software: PyCharm
class Father1:
    @classmethod
    def sys(cls):
        super(Father1, cls).sys()


class Father2:
    @classmethod
    def sys(cls):
        print("father2 sys")


class Father3:
    @classmethod
    def sys(cls):
        print('father3 sys')


class Father3_1(Father3):
    @classmethod
    def sys(cls):
        super(Father3_1, cls).sys()


class Son(Father1, Father3_1, Father2):
    def son(self):
        print("i im a son")


if __name__ == '__main__':
    print(Son.mro())
    Son.sys()
