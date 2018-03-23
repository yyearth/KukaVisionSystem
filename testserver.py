#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time    : 2018/3/21 14:36
# @Author  : yy

import socket
import time
'''
imitate KUKA server

'''

server = socket.socket()
server.bind(('localhost', 9000))
server.listen()

while True:
    print('server listening...')
    conn, addr = server.accept()
    print('client: ', addr)
    while True:
        try:
            data = conn.recv(1024).decode('ascii')
            time.sleep(2)  # kuka moving
            conn.send((data+' ser').encode('ascii'))
        except ConnectionResetError as e:
            print(e)
            break

server.close()





