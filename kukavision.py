#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time    : 2018/3/22 9:50
# @Author  : yy

import cv2
import threading
from queue import Queue
from clientforkuka import client
from processingimg import ColorTracker
import socket
from clientforkuka import framewrappe, frameparse
'''
main application
2 thread: img processing and socket client 
img

'''

target = Queue(maxsize=1)
position = Queue(maxsize=1)

# err.put()
class Pos:
    def __init__(self, x, y, z, a, b, c):
        self.x = x
        self.y = y
        self.z = z
        self.a = a
        self.b = b
        self.c = c


class ImageThread(threading.Thread):

    def __init__(self):
        super().__init__()
        self.frame = None
        self.cap = cv2.VideoCapture(0)

    def run(self):
        ct = ColorTracker()
        cv2.namedWindow('img')
        cv2.setMouseCallback('img', self.mouseInteraction, param=ct)
        while True:
            ret, self.frame = self.cap.read()
            if not ret:
                continue
            print(ct.track(self.frame))
            cv2.imshow('img', self.frame)
            if cv2.waitKey(1) == 27:
                break
            # TODO
        cv2.destroyAllWindows()
        self.cap.release()

    def mouseInteraction(self, event, x, y, flags, ct):

        # print(x,y)
        if event == cv2.EVENT_LBUTTONUP:
            bgr = self.frame[y, x]
            ct.setColor(bgr)


class SocketThread(threading.Thread):

    def __init__(self, addr):
        super().__init__()
        self.addr = addr

    def run(self):
        sock = socket.socket()
        sock.connect(self.addr)
        print('connect to KUKA server', self.addr)
        while True:
            rec = sock.recv(1024).decode('ascii')
            data = frameparse(rec)
            print(data)
            data[0] = data[0] + 100
            print(data)
            data = framewrappe(*data).encode('ascii')
            sock.send(data)


if __name__ == '__main__':
    # ImageThread().start()
    SocketThread(('172.31.1.147', 54600)).start()

