#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time    : 2018/3/22 9:44
# @Author  : yy

import socket
import xml.etree.ElementTree as ET

'''
TCP socket client

'''


def wrapper(x, y, z, a, b, c):
    root = ET.Element('Move')
    head_x = ET.SubElement(root, 'TX')
    head_y = ET.SubElement(root, 'TY')
    head_z = ET.SubElement(root, 'TZ')
    head_a = ET.SubElement(root, 'TA')
    head_b = ET.SubElement(root, 'TB')
    head_c = ET.SubElement(root, 'TC')
    head_x.text = str(x)
    head_y.text = str(y)
    head_z.text = str(z)
    head_a.text = str(a)
    head_b.text = str(b)
    head_c.text = str(c)
    return ET.tostring(root).decode('ascii')


def parser(sr):
    root = ET.fromstring(sr)
    # TODO

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
    # from queue import Queue
    # import threading
    # import time
    #
    # data_q = Queue(maxsize=1)
    # pos_q = Queue(maxsize=1)
    #
    # threading.Thread(target=client, args=(('localhost', 9000), data_q, pos_q)).start()
    #
    # time.sleep(2)
    # data_q.put('num:1')
    # # time.sleep(1)
    # print('main thread get:', pos_q.get())
    # time.sleep(1)
    # data_q.put('num:2')
    # print('main thread get:', pos_q.get())

    # import socket
    #
    # data = ''
    # cli = socket.socket()
    # cli.connect(('localhost', 9000))
    # print('connect to KUKA server')
    # while True:
    #     rec = cli.recv(1024).decode('ascii')
    #     data = input('>>>')
    #     cli.send(data.encode('ascii'))
    #     print(rec)
