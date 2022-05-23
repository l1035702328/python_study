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

