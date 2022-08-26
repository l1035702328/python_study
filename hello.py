"""
Python 多线程同步问题
"""

import time

import random
import threading
import time

# Lock锁 会发生死锁
# 加锁
# Condition提供了一种多线程通信机制，假如线程1需要数据，那么线程1就阻塞等待，这时线程2就去制造数据，线程2制造好数据后，通知线程1可以去取数据了，然后线程1去获取数据。
import threading

class AA:
    def __init__(self,db=1,name='',**connect_args):
        print(db)
        print(connect_args)
        print("hello")

def test1(a,b,**kwargs):
    print(kwargs)
if __name__ == '__main__':
    ss = AA(db=3, url='www.baidu.conm')
    print(ss)
    test1()