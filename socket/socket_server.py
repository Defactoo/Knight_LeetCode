#! /usr/bin/env python3
#! -*- encoding: utf-8 -*-
# Author: Knight
# @Time: 2018/10/3 下午9:48

import socket

server = socket.socket()

server.bind(('localhost',6969))

server.listen(5)

print('我要开始等电话')
while True:
    conn,addr = server.accept() # conn就是客户端连过来而在服务器端为其生成的一个连接实例

    while True:
        print('电话来了')
        data = conn.recv(1024)
        print('recv: ',data.decode())

        conn.send(data.upper())

server.close()