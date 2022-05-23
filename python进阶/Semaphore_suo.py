# -*- coding: utf-8 -*-

import threading
import time
# 本质上说，信号量是一个内部数据，用于标明当前的共享资源可以有多少并发读取。
maxSubThreadNumber = 6


def task():
    thName = threading.currentThread().name
    print(thName)
    with semaLock:
        print("run sub thread %s" % thName)
        time.sleep(3)


if __name__ == "__main__":

    semaLock = threading.Semaphore(2)

    for i in range(maxSubThreadNumber):
        subThreadIns = threading.Thread(target=task)
        subThreadIns.start()
