# -*- coding: utf-8 -*-
# @Time    : 2022/9/20 11:12
# @Author  : LZZ
# @FileName: shiti.py
# @Software: PyCharm
import re

# nums = input("nums=")
nums = "3,9,5,6,4,7,  55"
numre = re.search(r".*\s", nums)
print(numre.group())