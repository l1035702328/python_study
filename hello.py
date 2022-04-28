# coding = utf =8
from collections import Iterable


def qiao(lists):
    for i in lists:
        if isinstance(i, Iterable):
            for j in qiao(i):
                yield j
        else:
            yield i
if __name__ == '__main__':
    a = [1, 3, 4, [33, 44, [99, 100], 55, 66, ], 8]
    for ss in qiao(a):
        print(ss)