import threading


class Test:
    def __init__(self, total_value, condition):
        super(Test, self).__init__()
        self._total_value = total_value
        self.__condition = condition
        self._value = 0

    def produce(self):
        print("生产者")
        print("每次取出十个水果供应消费者")
        while self._total_value:
            with self.__condition:
                if self._total_value == 0:
                    print("没有库存水果了 通知消费者结束这次消费")
                    self.__condition.notify()
                    break
                else:
                    # 等待消费者通知我送水果
                    self.__condition.wait()
                    self._value = 10
                    self._total_value -= self._value
                    print("水果库存{}".format(self._total_value))
                    # 通知消费者
                    self.__condition.notify()

    def consumer(self):
        print("消费者")
        print("每次取出十个水果消费,需要等待商家送来水果")
        while self._total_value:
            with self.__condition:
                if self._value == 0:
                    print("没有水果")
                    # 通知商家送水果顾客处于等待状态
                    self.__condition.notify()
                    self.__condition.wait()
                else:
                    self._value -= 1
                    print("正在消费水果:{}".format(self._value))


if __name__ == '__main__':
    condition = threading.Condition()
    test = Test(1000, condition)
    t1 = threading.Thread(target=test.produce, args=(), daemon=False)
    t2 = threading.Thread(target=test.consumer, args=(), daemon=False)
    t1.start()
    t2.start()
