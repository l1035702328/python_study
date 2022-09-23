# -*- coding: utf-8 -*-
# @Time    : 2022/9/6 9:18
# @Author  : LZZ
# @FileName: demo.py
# @Software: PyCharm

import re


with open('1.text','r',encoding='utf-8') as f:
    mylist = re.findall(r'(?<=183px;"><span>)\d+',f.read())

my_set = set(mylist)
print(my_set)
print(len(my_set))


# values = ';'.join(my_set)
# print(values)
# print(len(values.split(';')))
