# -*- coding: utf-8 -*-
# @Time    : 2022/11/15 17:16
# @Author  : LZZ
# @FileName: demo.py
# @Software: PyCharm

# hasattr() 函数用来判断某个类实例对象是否包含指定名称的属性或方法。该函数的语法格式如下：
class CLanguage:
    def __init__ (self):
        self.name = "C语言中文网"
        self.add = "http://c.biancheng.net"
    def say(self):
        print("我正在学Python")
clangs = CLanguage()
print(hasattr(clangs,"name"))
print(hasattr(clangs,"add"))
print(hasattr(clangs,"say"))

# getattr() 函数获取某个类实例对象中指定属性的值。没错，和 hasattr() 函数不同，该函数只会从类对象包含的所有属性中进行查找。
class CLanguage:
    def __init__ (self):
        self.name = "C语言中文网"
        self.add = "http://c.biancheng.net"
    def say(self):
        print("我正在学Python")
clangs = CLanguage()
print(getattr(clangs,"name"))
print(getattr(clangs,"add"))
print(getattr(clangs,"say"))
print(getattr(clangs,"display",'nodisplay'))

# setattr() 函数的功能相对比较复杂，它最基础的功能是修改类实例对象中的属性值。其次，它还可以实现为实例对象动态添加属性或者方法。