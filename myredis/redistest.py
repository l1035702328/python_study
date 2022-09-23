# -*- coding: utf-8 -*-
# @Time    : 2022/9/5 9:20
# @Author  : LZZ
# @FileName: redistest.py
# @Software: PyCharm

import threading
import time

import redis
pool = redis.ConnectionPool(host='119.91.55.183', db=1, port=6379, password='1156989490',decode_responses=True)
r = redis.Redis(connection_pool=pool)

def test1():

    r.set('name', 'runoob')  # 设置 name 对应的值
    print(r.connection_pool._created_connections)
    print(r.connection_pool._available_connections)

def test2():
    r.set('name', 'runoob')  # 设置 name 对应的值
    print(r.connection_pool._created_connections)
    print(r.connection_pool._available_connections)

# 采集
def test3():
    value = r.lrange("HXYA3958", 0,-1)
    for i in value:
        print(i)
test3()