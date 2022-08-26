# -*- coding: utf-8 -*-
# @Time    : 2022/8/15 9:51
# @Author  : LZZ
# @FileName: pro.py
# @Software: PyCharm

class Project:
    def __init__(self):
        self.__aa = 1
        self.__bb = 2
        self.__cc = 3

    def aa(self):
        return self.__aa

    @property
    def bb(self):
        return self.__bb

    @property
    def cc(self):
        return self.__cc

    @cc.setter
    def cc(self, cc):
        self.__cc = cc


if __name__ == '__main__':
    pro = Project()
    print(pro.aa())
    print(pro.bb)
    pro.cc = 500
    print(pro.cc)
