# -*- coding: utf-8 -*-
# @Time    : 2022/9/6 16:24
# @Author  : LZZ
# @FileName: check.py
# @Software: PyCharm

def check_data():
    datalist = []
    with open('批量查询/一位数与存在零钱uin.txt','r',encoding='utf-8') as f1:
        file1 = f1.read().split(',')

    with open('身份只有一位数的uin.txt','r',encoding='utf-8') as f2:
        file2 = f2.read().split(',')

    print(file2)
    print(file1)
    for j in file2:
        if j in file1:
            print("已被修正")

        else:
            datalist.append(j)
    print(datalist)

if __name__ == '__main__':
    check_data()