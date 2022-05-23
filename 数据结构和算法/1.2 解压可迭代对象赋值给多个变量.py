class Test:
    def __iter__(self):
        self.value = 10
        return self

    def __next__(self):
        if self.value > 0:
            self.value = self.value-1
            return self.value
        else:
            raise StopIteration

if __name__ == '__main__':
    test = Test()
    a, *b, c = test
    print(b)