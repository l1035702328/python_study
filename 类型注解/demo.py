# -*- coding: utf-8 -*-
# @Time    : 2022/9/1 15:32
# @Author  : LZZ
# @FileName: demo.py
# @Software: PyCharm

# 列表、字典、元组等包含元素的复合类型，用简单的 list，dict，tuple 不能够明确说明内部元素的具体类型。因此要用到 typing 模块提供的复合注解功能：
# 如果你用的是 Python 3.9+ 版本，甚至连 typing 模块都不需要了，内置的容器类型就支持了复合注解：

from typing import List, Dict, Tuple

def aa(name:str, num=0):
    print(name)
    print(type(name))
    print(num)

def bb(name:Tuple[int,str]):
    print(type(name))
    print(name)

def cc(flag=True):
    print(flag)

class Test:
    def __init__(self):
        self.r = None
        self.r.hello = "hello"

    def __repr__(self):
        return "{}".format(self.r.hello)
if __name__ == '__main__':
    s = Test()