# -*- coding: utf-8 -*-
# @Time    : 2022/8/22 11:40
# @Author  : LZZ
# @FileName: 装饰器.py
# @Software: PyCharm
import time


def timer(rule: str, **options):
    def decorator(func):
        start_time = time.time()
        func()
        end_time = time.time()
        print("总耗时{}".format(end_time-start_time))
        print('rule={}'.format(rule))
        print("options={}".format(options))
        return func
    return decorator

@timer(rule='hello',b='hi',c='ok')
def h_test1():
    a=3
    b=4
    time.sleep(0.5)
    print("hello")
    return a+b

if __name__ == '__main__':
     h_test1()


# 装饰器工厂
