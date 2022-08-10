# -*- coding: utf-8 -*-
# @Time    : 2022/7/6 15:31
# @Author  : LZZ
# @FileName: zhenze1.py
# @Software: PyCharm
import unittest
import re


class Test(unittest.TestCase):
    # 注解表示函数的返回类型
    def setUp(self) -> None:
        self.text = 'aabbcc123456ppss123456'

    # 查找简单文本 in 或者index
    def test1(self):
        content = 'aabbcc123456ppss'
        text = 123456
        for text in content:
            print("找到了")
        try:
            print(content.index("55"))
        except ValueError as err:
            print(err)
            print("没找到")

    # 固定字符串
    # 确定字符串是否有123456
    def test2(self):
        result = re.findall(r'123456', self.text)
        print(result)

    # 某一类字符
    # 找出所有的单个的数字\d是数字 \D不是数字 \w任何字符非标点 [1-5] []匹配里面任意一个变量
    def test3(self):
        result = re.findall(r'[1-5]', self.text)
        print(result)

    # 重复某一类数字
    # \d+匹配任意1到多个数字 \d* \d? 匹配1到5给数字\d{1,5}
    def test4(self):
        result = re.findall(r'\d+', self.text)
        print(result)
