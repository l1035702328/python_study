# coding = utf-8
# 导入特定的函数
from pizza import pt1

# 使用as 给函数指定别名
from pizza import pt1 as pt1_a
# 导入模块中的所有函数
from pizza import *

# Python读取这个文件时，代码行import pizza 让Python打开文件
# pizza.py，并将其中的所有函数都复制到这个程序中。你看不到复
# 制的代码，因为在这个程序即将运行时，Python在幕后复制了这些
# 代码。你只需知道，在making_pizzas.py中，可使用pizza.py中定义
# 的所有函数。
if __name__ == '__main__':
    print("hello")
    pt1()
    pt1_a()

