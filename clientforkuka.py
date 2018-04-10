#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time    : 2018/3/22 9:44
# @Author  : yy

import socket
import xml.etree.ElementTree as ET

'''
TCP socket client

'''


# def wrapper(x, y, z, a, b, c):
#     root = ET.Element('Move')
#     head_x = ET.SubElement(root, 'TX')
#     head_y = ET.SubElement(root, 'TY')
#     head_z = ET.SubElement(root, 'TZ')
#     head_a = ET.SubElement(root, 'TA')
#     head_b = ET.SubElement(root, 'TB')
#     head_c = ET.SubElement(root, 'TC')
#     head_x.text = str(x)
#     head_y.text = str(y)
#     head_z.text = str(z)
#     head_a.text = str(a)
#     head_b.text = str(b)
#     head_c.text = str(c)
#     return ET.tostring(root).decode('ascii')


def framewrapper(x, y, z, a, b, c):
    att = {'X': str('%.6f' % x), 'Y': str('%.6f' % y), 'Z': str('%.6f' % z),
           'A': str('%.6f' % a), 'B': str('%.6f' % b), 'C': str('%.6f' % c)}
    root = ET.Element('Sensor')
    head = ET.SubElement(root, 'frame', attrib=att)
    return ET.tostring(root).decode('ascii')


def frameparser(sr):
    root = ET.fromstring(sr)
    if root is None:
        return None
    att = root[0].attrib
    return float(att['X']), float(att['Y']), float(att['Z']), float(att['A']), float(att['B']), float(att['C'])


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

    import socket

    data1 = '<Move><TX>12.11</TX><TY>2.10</TY><TZ>2.13</TZ><TA>2.13</TA><TB>2.13</TB><TC>2.13</TC></Move>'
    data2 = '<Move><TX="12.11" TY="0.000000" TZ="0.000000" TA="0.000000" TB="0.000000" TC="0.000000"</Move>'
    cli = socket.socket()
    cli.connect(('172.31.1.147', 54600))
    print('connect to KUKA server')
    while True:
        rec = cli.recv(1024).decode('ascii')
        print(rec)
        # data = input('>>>').encode('ascii')
        cli.send(data1.encode('ascii'))
        # cli.send(rec.encode('ascii'))
        # print(rec)
# <Robot><frame X="915.000000" Y="0.000000" Z="1120.000000" A="0.000000" B="90.000000" C="0.000000"></frame></Robot>
