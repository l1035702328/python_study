# -*- coding: utf-8 -*-
# @Time    : 2022/7/6 15:31
# @Author  : LZZ
# @FileName: zhenze1.py
# @Software: PyCharm
import unittest
import re

# 正则表达式步骤
# 确定包含几个子模式
# 确定各个部分字符分类
# 各个部分如何重复
# 是否有外部位置限制
# 是否有内部制约关系
from unittest import TestLoader


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
    # 匹配任意1到多个数字\d+ 匹配0个或者多个\d* 匹配0个或者1个\d? 匹配1到5给数字\d{1,5}
    def test4(self):
        result = re.findall(r'\d+', self.text)
        print(result)

    # 匹配电话与手机号码
    def test5(self):
        text = r"djkgfjdlgjd 0746-55998844 vuevue13873301754"
        result = re.findall(r'\d{4}-\d{8}|1\d{10}', text)
        print(result)

    # 限定位置
    # 在句子开头的手机号码或座机 匹配开头^
    def test6(self):
        text = r"djkgfjdlgjd 0746-55998844 vuevue13873301754"
        result = re.findall(r'^\d{4}-\d{8}|1\d{10}', text)
        print(result)

    # 内部约束
    #()表示一组 \1要跟第一个组(括号)匹配的一样
    def test7(self):
        text = r"barbar-carcar-harhel"
        result = re.findall(r'(\w{3})(\1)', text)
        print(result)


    # 练习
    # 查找
    def test8(self):
        text = "aabb45ff3dd"
        print(re.findall(r'bb.*d', text))

    # (?<=)前面为该字符 用于匹配后面得字符  \d+(?=)后面为该字符 用于匹配前面字符
    def test9(self):
        text = "yueluowutijiannan123ruwomian"
        print(re.findall(r'(?<=nan)\d+', text))

    def test10(self):
        text = 'abc,ABC,aBC'
        print(re.findall(r'abc', text, flags=re.I))
    # match开头匹配匹配一个 search全局匹配一个
    def test11(self):
        text = 'ABC,abc,aBC,ABCfff'
        match = re.search(r'(abc).(abc)', text, flags=re.I)
        print(match.group(2))
        print('-------------------')
        print(re.match(r'(abc).(abc)', text, flags=re.I))
        print("-------------------")
        for _ in re.finditer(r'(abc).(abc)', text, flags=re.I):
            print(_)

    # 替换
    def test12(self):
        text = 'ABC,abc-aBC,ABCfff'
        subs = re.sub(r'(abc).\1', "888", text, flags=re.I)
        print(subs)
        subs = re.subn(r'(abc).\1', "888", text, flags=re.I)
        print(subs)

    # 分割
    def test13(self):
        text = r'vuevue  / dff www , fff'
        result = re.split('\s*[/,\s]\s*', text)
        print(result)

    # compile
    def test14(self):
        text = r'vuevue  / dff www , fff'
        comp = re.compile('\s*[/,\s]\s*',flags=re.I)
        print(comp.split(text))

    # 别名
    # (?P<name>...):分组,除了原有的编号外再指定一个额外的别名.
    # \<number>:引用编号为<number>的分组匹配到的字符串. (\d)abc\1
    # (?P = name):引用别名为<name>的分组匹配到的字符串
    def test15(self):
        text = '/index/111/222'
        result = re.match('/index/(?P<number1>\d+)/(?P<number2>\d+)', text)
        print(result.group('number2'))

if __name__ == '__main__':
    unittest.main()