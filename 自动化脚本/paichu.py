# -*- coding: utf-8 -*-
# @Time    : 2022/9/6 16:41
# @Author  : LZZ
# @FileName: paichu.py
# @Software: PyCharm

def remove_data():
    add_list = []
    with open("1.text",'r',encoding='utf-8') as f1:
        total_list = f1.read().split(';')
    with open('身份只有一位数的uin.txt','r',encoding='utf-8') as f2:
        some_list = f2.read().split(',')

    for _ in total_list:
        if _ in some_list:
            print("已充值")
        else:
            add_list.append(_)

    print(len(add_list))
    print(','.join(add_list))

if __name__ == '__main__':
    remove_data()