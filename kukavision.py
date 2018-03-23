#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time    : 2018/3/22 9:50
# @Author  : yy

import cv2
import threading
from queue import Queue
from clientforkuka import client
from processingimg import processing

'''
main application
2 thread: img processing and socket client 
img

'''

data_q = Queue(maxsize=1)
pos_q = Queue(maxsize=1)

cap = cv2.VideoCapture(0)
# err.put()


class ProcessThread(threading.Thread):

    def __init__(self):
        super().__init__()

    def run(self):
        while True:
            ret, frame = cap.read()
            if not ret: continue
            # err = processing(frame)
            # TODO


class SocketThread(threading.Thread):

    def __init__(self, addr):
        super().__init__()
        self.addr = addr

    def run(self):
        # TODO
        # client(self.addr, pos,)
        pass


if __name__ == '__main__':
    pass
