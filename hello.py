"""
Python 多线程同步问题
"""


import re

# 将他们看成列表
# 每次补充最少的 如果补充完毕不够则输出no
# 判断red三个字符谁最少 谁最多 补充最少字符至最多
#  ?是否够匹配 且后续都为3以上
#

class A:
    def aaa(self):
        return "this is aaa"

    def bbb(self):
        return "this is bbb"

class B(A):
    def aaa(self):
        self.aaa()

def hello(aa):
    print(aa)

def hello(aa,bb):
    print(aa)
    print(bb)

if __name__ == '__main__':
    bb2 = B()
    bb2.aaa()