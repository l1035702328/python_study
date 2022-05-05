"""
Python 多线程同步问题
"""
import time
from threading import *

class Node:
    def __init__(self, flag):
        self.condition = flag

    def run(self):
        print("loading thread")
        self.condition.wait()
        for i in range(50):
            print(i)



def test1():
    condition = Condition()
    a = Node(condition)
    t1 = Thread(target=a.run, args=()).start()





if __name__ == '__main__':
    test1()