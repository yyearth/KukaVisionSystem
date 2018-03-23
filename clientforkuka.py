#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time    : 2018/3/22 9:44
# @Author  : yy

import socket

'''
TCP socket client

'''


# addr = ('localhost', 9000)
def client(addr, data_q, pos_q):
    cli = socket.socket()
    cli.connect(addr)
    print('connect to KUKA server:', addr)
    while True:
        # if data_q.empty(): continue
        data = data_q.get()
        # TODO strategy and xml wrap

        cli.send(data.encode('ascii'))
        print('wait recv...')
        rec = cli.recv(1024).decode('ascii')
        print('got')
        # TODO xml parse

        # if pos_q.full()
        pos_q.put(rec)


if __name__ == '__main__':
    from queue import Queue
    import threading
    import time

    data_q = Queue(maxsize=1)
    pos_q = Queue(maxsize=1)

    threading.Thread(target=client, args=(('localhost', 9000), data_q, pos_q)).start()

    time.sleep(2)
    data_q.put('num:1')
    # time.sleep(1)
    print('main thread get:', pos_q.get())
    time.sleep(1)
    data_q.put('num:2')
    print('main thread get:', pos_q.get())




