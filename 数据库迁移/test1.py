# -*- coding: utf-8 -*-
# @Time    : 2022/8/22 9:45
# @Author  : LZZ
# @FileName: test1.py
# @Software: PyCharm
import logging
from functools import wraps


def test(func):
    def decorator():
        func()
        print(f'这是一个装饰器')
    return decorator

@test
def target():
    print(f'这是被装饰函数')

target() # 这是一个装饰器