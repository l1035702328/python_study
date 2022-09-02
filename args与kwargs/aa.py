# -*- coding: utf-8 -*-
# @Time    : 2022/9/1 9:28
# @Author  : LZZ
# @FileName: aa.py
# @Software: PyCharm

class DD:
    def __init__(self,nihao,wohao,tahao):
        self.nihao =nihao
        self.wohao = wohao
        self.tahao = tahao

    def __str__(self):
        return '{}{}{}'.format(self.nihao,self.wohao,self.tahao)
def aa(**kwargs):

    mydd = DD(**kwargs)
    print(mydd)

if __name__ == '__main__':
    bb = {'nihao':1,'wohao':32,'tahao':33}
    aa(**bb)
