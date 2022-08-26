# -*- coding: utf-8 -*-
# @Time    : 2022/8/16 16:23
# @Author  : LZZ
# @FileName: my_redis.py
# @Software: PyCharm

import time
import re
import redis
from django.core.cache import cache

def test1():
    for i in range(10):
        soc = '7'+i.__str__()
        soh = '66%'
        localtime = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
        name = 'HXYA2530'
        data = 'name:{};soc:{};soh:{};local_time:{};'.format(name, soc, soh, localtime)
        result = re.search('(?<=name:)\w+', data)
        print(result.group())
        # redis_pool = redis.ConnectionPool(host='119.91.55.183', port=6379, password='', db=1)
        # redis_conn = redis.Redis(connection_pool=redis_pool)
        # result = redis_conn.rpush(name, data)
        # print(result)
        # time.sleep(5)

def test2():
    redis_pool = redis.ConnectionPool(host='119.91.55.183', port=6379, password='', db=1)
    redis_conn = redis.Redis(connection_pool=redis_pool)
    flag = {'power_flag': '0', 'upgrade_flag': '0', 'filename': '0'}
    s = redis_conn.hset("lzz", mapping=flag)
    print(s)

if __name__ == '__main__':
    test2()
