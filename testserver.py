#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time    : 2018/3/21 14:36
# @Author  : yy

import socket
import time
'''
imitate KUKA server

'''
hi = '<Move><TX>12.11</TX><TY>2.10</TY><TZ>2.13</TZ><TA>2.13</TA><TB>2.13</TB><TC>2.13</TC></Move>'

server = socket.socket()
server.bind(('localhost', 9000))
server.listen()

while True:
    print('server listening...')
    conn, addr = server.accept()
    print('client: ', addr)
    while True:
        try:
            conn.send(hi.encode('ascii'))
            data = conn.recv(1024).decode('ascii')
            time.sleep(2)  # kuka moving
            conn.send((data+' ser').encode('ascii'))
        except ConnectionResetError as e:
            print(e)
            break

server.close()





