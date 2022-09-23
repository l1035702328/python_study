# -*- coding: utf-8 -*-
# @Time    : 2022/9/22 11:30
# @Author  : LZZ
# @FileName: 二分查找.py
# @Software: PyCharm

import re

# 递归实现二分查找
class Solution:
    def __init__(self, elements, value):
        self.elements = elements
        self.value = value

    def binary_search_recursive(self, elements, value):
        global num
        num = num+1
        index = 0
        if len(elements) == 0:
            return False

        left, right = 0, len(elements) - 1

        if left <= right:
            middle = (left + right) // 2

            if elements[middle] == value:
                # 返回下标以及查找次数
                # 查找次数
                for _ in self.elements:
                    index += 1
                    if _ == self.value:
                        break
                return "'{},{}'".format(index-1, num)

            elif elements[middle] < value:
                return self.binary_search_recursive(elements[middle+1:], value)
            else:
                return self.binary_search_recursive(elements[:middle], value)

        return False

if __name__ == '__main__':
    num = 0
    get_str = input()
    my_group = re.search(r"\[(.*)],(\d+)", get_str)
    nums = list(map(int,my_group.group(1).split(',')))
    value = int(my_group.group(2))
    print(nums)
    solution = Solution(nums, value)
    result = solution.binary_search_recursive(nums,value)
    print(result)


