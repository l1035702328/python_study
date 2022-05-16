"""
Python 多线程同步问题
"""

import time

import random
import threading
import time


import threading

class A(threading.Thread):
    def __init__(self, lock):
        super(A, self).__init__()
        self.lock = lock

    def run(self):
        with self.lock:
            for i in range(10000):
                print("{}\tname:{}\t{}".format(self.lock, self.getName(), i))


def test1(lock):
    with lock:
        ts1 = A(lock)
        ts1.start()
        for i in range(10000, 0, -1):
            print("{}\t {}".format(lock, i))


if __name__ == '__main__':
    lock = threading.Lock()
    t1 = threading.Thread(target=test1, args=(lock,), daemon=False)
    t1.start()
    t1.join()
    print("---------------------")
    print(t1.getName())
