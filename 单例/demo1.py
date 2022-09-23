# -*- coding: utf-8 -*-
# @Time    : 2022/9/9 9:34
# @Author  : LZZ
# @FileName: demo1.py
# @Software: PyCharm

# Python 的模块就是天然的单例模式，因为模块在第一次导入时，会生成 .pyc 文件，当第二次导入时，
# 就会直接加载 .pyc 文件，而不会再次执行模块代码。因此，我们只需把相关的函数和数据定义在一个模块中，就可以获得一个单例对象了。

class Single(object):
    _instance = None
    def __new__(cls, *args, **kw):
        if cls._instance is None:
            cls._instance = object.__new__(cls, *args, **kw)
        return cls._instance
    def __init__(self):
        pass

single1 = Single()
single2 = Single()
print(id(single1) == id(single2))

# 天然单例
# 作为Python模块时是天然的单例模式

#创建一个sington.py文件，内容如下：
# class Singleton(object):
#    def foo(self):
#        pass
# mysington = Singleton()
#
# # 运用
# from sington import mysington
# mysington.foo()