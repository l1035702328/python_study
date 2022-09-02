#!/usr/bin/env python
# -*- coding:utf-8 -*-

import socketserver
import time
from socketserver import BaseServer, BaseRequestHandler
from typing import Any, Tuple, Callable

import redis
import re
import logging


class MyServer(socketserver.BaseRequestHandler):

    """
    必须继承socketserver.BaseRequestHandler类
    """
    def setup(self):
        print("只执行一次")
        self.redis_pool = redis.ConnectionPool(host='119.91.55.183', port=6379, password='', db=1)

    def handle(self):
        """
        必须实现这个方法！
        :return:
        """
        conn = self.request         # request里封装了所有请求的数据
        conn.sendall('欢迎访问socketserver服务器！'.encode())

        #
        data = conn.recv(1024).decode()
        # 生成redis
        print("来自%s的客户端向你发来信息：%s" % (self.client_address, data))
        conn.sendall(('已收到你的消息<%s>' % data).encode())
        name = re.search('(?<=name:)\w+', data).group()
        for i in range(3):
            try:
                redis_conn = redis.Redis(connection_pool=self.redis_pool)
                flag = {'power_flag': '0', 'upgrade_flag': '0', 'filename': '0'}
                redis_conn.hset("{}_flag".format(name), mapping=flag)
                result_num = redis_conn.rpush(name, data)
                logging.info("插入成功")
                result = redis_conn.hgetall(name)
                if result['power_flag'] == '1':
                    print("执行关闭电源指令")
                if result['upgrade_flag'] == '1':
                    print("msg:upgrade;flag:1")
                    data = conn.recv(1024).decode()
                    if data == 'ok':
                        print("去调文件")
                break
            except Exception as e:
                logging.warning("插入失败{}".format(e))
                continue
        while True:
            data = conn.recv(1024).decode()
            if data == "exit":
                print("断开与%s的连接！" % (self.client_address,))
                break
            print("来自%s的客户端向你发来信息：%s" % (self.client_address, data))
            conn.sendall(('已收到你的消息<%s>' % data).encode())
            name = re.search('(?<=name:)\w+', data).group()
            for i in range(3):
                try:
                    redis_conn = redis.Redis(connection_pool=self.redis_pool)
                    result_num = redis_conn.rpush(name, data)
                    logging.info("插入成功")
                    result = redis_conn.hgetall(name)
                    if result['power_flag'] == '1':
                        print("执行关闭电源指令")
                    if result['upgrade_flag'] == '1':
                        print("msg:upgrade;flag:1")
                        data = conn.recv(1024).decode()
                        if data == 'ok':
                            print("去调文件")
                        # 升级完成应重置状态
                    break
                except Exception as e:
                    logging.warning("插入失败{}".format(e))
                    continue





if __name__ == '__main__':
    # 创建logger实例
    logging.basicConfig(handlers=[logging.FileHandler(filename="./hxya.log",
                        encoding='utf-8', mode='a+')], level=logging.DEBUG,
                        format='%(asctime)s %(message)s', datefmt='%Y/%m/%d %I:%M:%S')
    logging.debug('debug 信息')
    logging.info("hello")
    # 创建一个多线程TCP服务器
    server = socketserver.ThreadingTCPServer(('127.0.0.1', 5000), MyServer)
    with server:
        print("启动socketserver服务器！")
        # 启动服务器，服务器将一直保持运行状态
        server.serve_forever()
