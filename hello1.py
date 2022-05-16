class A:
    def __init__(self):
        print("a")

    def __iter__(self):
        ss = list(range(20, 1, -2))
        print(ss)
        return iter(ss)


if __name__ == '__main__':
    b = A()
    for i in b:
        print(i)