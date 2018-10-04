#! /usr/bin/env python3
#! -*- encoding: utf-8 -*-
# Author: Knight
# @Time: 2018/10/3 下午9:42

import socket

client = socket.socket()

client.connect(('localhost',6969))

#client.send(b"Hello World!")
#client.send("我要下载A片".encode('utf-8'))

while True:
    msg = input(">>: ").strip()

    client.send(msg.encode('utf-8'))
    data = client.recv(1024)
    print("recv:",data.decode())

client.close()

