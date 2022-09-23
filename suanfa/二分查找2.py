# -*- coding: utf-8 -*-
# @Time    : 2022/9/22 11:54
# @Author  : LZZ
# @FileName: 二分查找2.py
# @Software: PyCharm

import re





def binary_search_recursive(elements, value):
    global num
    global index
    num = num + 1
    if len(elements) == 0:
        return False

    left, right = 0, len(elements) - 1

    if left <= right:
        # 向下取整
        middle = (left + right) // 2

        if elements[middle] == value:
            # 返回下标以及查找次数
            # 查找次数
            index = index + middle
            return "'{},{}'".format(index, num)
        # 中间数是否小于value
        elif elements[middle] < value:
            index = index + middle
            return binary_search_recursive(elements[middle + 1:], value)
        # 中间数>value
        else:
            return binary_search_recursive(elements[:middle], value)

    return False


if __name__ == '__main__':
    index= 0
    num = 0
    get_str = input()
    my_group = re.search(r"\[(.*)],(\d+)", get_str)
    nums = list(map(int, my_group.group(1).split(',')))
    value = int(my_group.group(2))
    print(nums)
    result = binary_search_recursive(nums, value)
    print(result)

