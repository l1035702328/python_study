# coding = utf-8
# 并发编程
import threading
import time
from threading import Thread, current_thread,Event
import multiprocessing
from queue import Queue


def countdown(n):
    while n > 0:
        print('T-minus', n)
        n -= 1
        time.sleep(2)

def test1():
    print("这是主线程:{}".format(current_thread().name))
    t1 = Thread(target=countdown, args=(10,), daemon=True)  # 如果没有开启守护线程(后台线程)主线程会等待所有子线程运行完毕才退出
    t2 = Thread(target=countdown, args=(5,))

    t1.start()
    t2.start()
    # t2.join()  # 等待t2运行完毕才结束
    print("主线程结束了")


# 后台线程无法等待，不过，这些线程会在主线程终止时自动销毁。
# 除了如上所示的两个操作，并没有太多可以对线程做的事情。
# 你无法结束一个线程，无法给它发送信号，无法调整它的调度，也无法执行其他高级操作。
# 如果需要这些特性，你需要自己添加。
# 比如说，如果你需要终止线程，那么这个线程必须通过编程在某个特定点轮询来退出。你可以像下边这样把线程放入一个类中：
def test1_1():
    class CountDownTask:
        def __init__(self):
            self._running = True

        def terminate(self):
            self._running = False

        def run(self, n):
            while self._running and n > 0:
                print('T-minus', n)
                n -= 1
                time.sleep(5)

    c = CountDownTask()
    t1 = Thread(target=c.run, args=(5,))
    t1.start()
    c.terminate()
    t1.join()

# 如果线程执行一些像I/O这样的阻塞操作，那么通过轮询来终止线程将使得线程之间的协调变得非常棘手。
# 比如，如果一个线程一直阻塞在一个I/O操作上，它就永远无法返回，也就无法检查自己是否已经被结束了。
# 要正确处理这些问题，你需要利用超时循环来小心操作线程。
def test1_2():
    class IOTask:
        def terminate(self):
            self._running = False

        def run(self, sock):
            # sock is a socket
            sock.settimeout(5)  # Set timeout period
            while self._running:
                # Perform a blocking I/O operation w/ timeout
                try:
                    data = sock.recv(8192)
                    break
                except socket.timeout:
                    continue
                # Continued processing
                ...
            # Terminated
            return

# 通过初始化父类直接创建线程
def test1_3():
    class CountdownThread(Thread):
        def __init__(self, n):
            super().__init__()
            self.n = n

        def run(self):
            while self.n > 0:
                print('T-minus', self.n)
                self.n -= 1
                time.sleep(5)

    c = CountdownThread(5)
    c.start()
    # 可以单独创建一个进程执行代码
    # c = CountdownTask(5)
    # p = multiprocessing.Process(target=c.run)
    # p.start()


# 判断线程是否已启动 利用Event
def test2():
    # Code to execute in an independent thread
    def countdown(n, started_evt):
        print('countdown starting')
        time.sleep(20)
        started_evt.set()
        while n > 0:
            print('T-minus', n)
            n -= 1
            time.sleep(5)

    # Create the event object that will be used to signal startup
    started_evt = Event()
    # Launch the thread and pass the startup event
    print('Launching countdown')
    t1 = Thread(target=countdown, args=(10, started_evt))
    t1.start()
    # Wait for the thread to start
    started_evt.wait()
    print('countdown is running')

# event 对象最好单次使用，就是说，你创建一个 event 对象，让某个线程等待这个对象，一旦这个对象被设置为真，你就应该丢弃它。
# 尽管可以通过 clear() 方法来重置 event 对象，但是很难确保安全地清理 event 对象并对它重新赋值。
# 很可能会发生错过事件、死锁或者其他问题（特别是，你无法保证重置 event 对象的代码会在线程再次等待这个 event 对象之前执行）。
# 如果一个线程需要不停地重复使用 event 对象，你最好使用 Condition 对象来代替。
# 下面的代码使用 Condition 对象实现了一个周期定时器，每当定时器超时的时候，其他线程都可以监测到：
def test2_2():
    class PeriodicTimer:
        def __init__(self, interval):
            self._interval = interval
            self._flag = 0
            self._cv = threading.Condition()

        def start(self):
            t = threading.Thread(target=self.run)
            t.daemon = True
            t.start()

        def run(self):
            '''
            Run the timer and notify waiting threads after each interval
            '''
            while True:
                time.sleep(self._interval)
                with self._cv:
                    self._flag ^= 1
                    self._cv.notify_all()

        def wait_for_tick(self):
            '''
            Wait for the next tick of the timer
            '''
            with self._cv:
                last_flag = self._flag
                while last_flag == self._flag:
                    self._cv.wait()

    # Example use of the timer
    ptimer = PeriodicTimer(5)
    ptimer.start()

    # Two threads that synchronize on the timer
    def countdown(nticks):
        while nticks > 0:
            ptimer.wait_for_tick()
            print('T-minus', nticks)
            nticks -= 1

    def countup(last):
        n = 0
        while n < last:
            ptimer.wait_for_tick()
            print('Counting', n)
            n += 1

    threading.Thread(target=countdown, args=(10,)).start()
    threading.Thread(target=countup, args=(5,)).start()

# 互斥锁
#    # 创建锁
#     mutex = threading.Lock()
#     # 加锁
#     mutex.acquire()
#     # 释放
#     mutex.release()
# 错误实例 每个Node对象都有一个自己的Lock对象
ticket = 100000
num = 0
class Node(threading.Thread):
    def __init__(self, name):
        super(Node, self).__init__()
        self._name = name
        self._lock = threading.Lock()

    def run(self):
        global ticket
        global num
        while ticket > 0:
            with self._lock:
                ticket = ticket - 1
                print("{}:\t{}\t锁对象:{}".format(threading.current_thread(), ticket, self._lock))
                num = num+1
                print(num)
        print("最后输出:{}".format(num))

def test3():
    for i in range(10):
        thread = Node(i)
        thread.start()

# 　在Python中为了支持同一个线程中多次请求同一资源，Python提供了可重入锁。这个RLock内部维护着一个Lock和一个counter
# 　变量，counter记录了acquire的次数，从而使得资源可以被多次require。直到一个线程所有的acquire都被release，其他的线程才能获
#   得资源。

if __name__ == '__main__':
    # test1()
    # test1_1()
    # test2()
    # test2_2()
    test3()