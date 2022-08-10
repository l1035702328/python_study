# -*- coding: utf-8 -*-
# @Time    : 2022/8/10 11:13
# @Author  : LZZ
# @FileName: shangxiawen.py
# @Software: PyCharm

class File(object):
    def __init__(self, file_name, method):
        self.file_obj = open(file_name, method)

    def __enter__(self):
        return "ffff"

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file_obj.close()

with File("nihao.txt","w") as e:
    print(e)