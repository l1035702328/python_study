"""
Python 多线程同步问题
"""

import time

import random
import threading
import time

# 创建车票总量
from functools import wraps
# 加锁

ticket = 100000
num = 0


class Station(threading.Thread):
    def __init__(self, value):
        super(Station, self).__init__()
        self.value = value
        self._lock = threading.Lock()

    def run(self):
        global ticket, num
        while 1:
            with self._lock:
                if ticket <= 0:
                    break
                ticket = ticket-1
                print("线程:{}: 拿{}票,锁对象:{}".format(self.getName(), ticket,self._lock))
                num = num + 1

        print(num)


if __name__ == '__main__':
    for i in range(7):
        Station(i).start()


    print(num)




