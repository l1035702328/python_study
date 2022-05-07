import unittest

class Test1(unittest.TestCase):
    # 闭包陷阱 返回闭包中不要引用任何循环变量，或者后续会发生变化的变量。
    def my_func(*args):
        fs = []
        for i in range(3):
            def func():
                return i * i
            fs.append(func)
        return fs
    def test1(self):
        fs1, fs2, fs3 = self.my_func()
        print(fs1())
        print(fs2())
        print(fs3())


    def test2(self):
        list1 = [1,3,5]
        a,b,c = list1
        print(a)
        print(b)
        print(c)
# 上层变量对于下层而言是只读的
    def test3(self):
        a = 1
        def bb():
            a = a+1
        return bb

if __name__ == '__main__':
    unittest.main()