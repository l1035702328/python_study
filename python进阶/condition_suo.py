import threading


class Test:
    def __init__(self, total_value, condition):
        super(Test, self).__init__()
        self._total_value = total_value
        self.__condition = condition
        self._value = 0
        self._flag = False

    def produce(self):
        print("生产者")
        print("每次取出十个水果供应消费者")
        while 1:
            with self.__condition:
                print("等待消费者通知")
                self.__condition.wait()
                if self._total_value == 0:
                    print("没有库存水果了 通知所有消费者结束这次消费")
                    self._flag = True
                    self.__condition.notify(2)
                    break
                else:
                    # 等待消费者通知我送水果
                    self._value = 10
                    self._total_value -= self._value
                    print("水果库存{}".format(self._total_value))
                    # 通知消费者
                    self.__condition.notify()

    def consumer(self):
        print("消费者")
        print("每次取出十个水果消费,需要等待商家送来水果")
        while 1:
            with self.__condition:
                # 商家水果已无库存 跳出循环
                if self._flag:
                    print("{}消费者接收到商家水果已无库存".format(threading.current_thread().getName()))
                    break
                if self._value:
                    self._value -= 1
                    print("{}正在消费水果:{}".format(threading.current_thread().getName(), self._value))
                else:
                    print("{}没有水果".format(threading.current_thread().getName()))
                    # 通知商家送水果顾客处于等待状态
                    self.__condition.notify()
                    self.__condition.wait()


if __name__ == '__main__':
    condition = threading.Condition()
    test = Test(1000, condition)
    t1 = threading.Thread(target=test.produce, args=(), daemon=False)
    t2 = threading.Thread(target=test.consumer, args=(), daemon=False)
    t3 = threading.Thread(target=test.consumer, args=(), daemon=False)
    t1.start()
    t2.start()
    t3.start()
