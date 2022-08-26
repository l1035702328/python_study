# -*- coding: utf-8 -*-
# @Time    : 2022/8/23 15:07
# @Author  : LZZ
# @FileName: test1.py
# @Software: PyCharm

class MyForm:
    def __init__(self):
        print("hello")


    def __str__(self):
        return "djsdf"
    def __repr__(self):
        return "world"



if __name__ == '__main__':
    aa = MyForm()
    print(aa)