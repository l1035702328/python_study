# -*- coding: utf-8 -*-
# @Time    : 2022/8/12 14:27
# @Author  : LZZ
# @FileName: socket_client.py
# @Software: PyCharm

import socket
import json
import time

import socket

def get_data():
    soc = '7'
    soh = '66%'
    localtime = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
    name = 'HXYA3958'
    data = 'name:{};soc:{};soh:{};local_time:{};'.format(name, soc, soh, localtime)
    return data


client = socket.socket()

# 连接服务器
addr = ('127.0.0.1', 6000)
client.connect(addr)

# 发送数据
while 1:
    data = get_data()
    client.send(data.encode('utf-8'))
    result = client.recv(1024)
    print(result.decode())
    time.sleep(20)
client.close()
