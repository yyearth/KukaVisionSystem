#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time    : 2018/3/22 9:42
# @Author  : yy

import numpy as np
import cv2

'''

'''

COLOR_TRACK = 0


# class FaceFinder(object):
#
#     def __init__(self):
#         super().__init__()


class ColorTracker(object):

    def __init__(self, bgr):
        # super().__init__()
        self._targetbgr = bgr
        self._sigma = 3
        hsv = cv2.cvtColor(np.uint8([[bgr]]), cv2.COLOR_BGR2HSV)
        self._color_l = np.array([cv2.add(hsv[0][0], - self._sigma)[0][0], 100, 100], np.uint8)
        self._color_u = np.array([cv2.add(hsv[0][0], self._sigma)[0][0], 255, 255], np.uint8)

    # use @property later
    def setColor(self, bgr):
        self._targetbgr = bgr
        hsv = cv2.cvtColor(np.uint8([[bgr]]), cv2.COLOR_BGR2HSV)
        self._color_l = np.array([cv2.add(hsv[0][0], - self._sigma)[0][0], 100, 100], np.uint8)
        self._color_u = np.array([cv2.add(hsv[0][0], self._sigma)[0][0], 255, 255], np.uint8)

    def track(self, img):
        err_x, err_y = 0, 0

        img2 = cv2.GaussianBlur(img, (21, 21), 1)
        img_hsv = cv2.cvtColor(img2, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(img_hsv, self._color_l, self._color_u)

        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        # mask = cv2.erode(mask, kernel)
        # mask = cv2.dilate(mask, kernel)
        mask, contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        cv2.imshow('img', mask)
        cv2.waitKey()
        for cnt in contours:
            if cv2.contourArea(cnt) < 500:
                continue
            # print(cv2.contourArea(cnt))
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 1)
        if len(contours) > 0:
            cnt_max = max(contours, key=cv2.contourArea)
            x, y, w, h = cv2.boundingRect(cnt_max)
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 225), 1)
            err_x = x + w // 2
            err_y = y + h // 2
            cv2.circle(img, (err_x, err_y), 2, (0, 0, 255), -1)
            # print(err_x, err_y)
        cv2.imshow('img', img)
        cv2.waitKey()

        return err_x, err_y


# def trackcolor(img, bgr):
#     '''
#
#     :param img: source. in-place.
#     :param bgr: bgr color to track
#     :return: err to the center
#     '''
#     delta = 3
#     ih, iw, ch = img.shape
#     err_x, err_y = 0, 0
#     print(ih, iw, ch)
#     hsv = cv2.cvtColor(np.uint8([[bgr]]), cv2.COLOR_BGR2HSV)
#     _color_l = np.array([cv2.add(hsv[0][0], - delta)[0][0], 100, 100], np.uint8)
#     _color_u = np.array([cv2.add(hsv[0][0], delta)[0][0], 255, 255], np.uint8)
#     print(bgr, hsv, _color_l, _color_u)
#
#     img2 = cv2.GaussianBlur(img, (21, 21), 1)
#     img_hsv = cv2.cvtColor(img2, cv2.COLOR_BGR2HSV)
#     mask = cv2.inRange(img_hsv, _color_l, _color_u)
#
#     kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
#     mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
#     # mask = cv2.erode(mask, kernel)
#     # mask = cv2.dilate(mask, kernel)
#     mask, contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#     cv2.imshow('img', mask)
#     cv2.waitKey()
#     for cnt in contours:
#         if cv2.contourArea(cnt) < 500:
#             continue
#         # print(cv2.contourArea(cnt))
#         x, y, w, h = cv2.boundingRect(cnt)
#         cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 1)
#     if len(contours) > 0:
#         cnt_max = max(contours, key=cv2.contourArea)
#         x, y, w, h = cv2.boundingRect(cnt_max)
#         cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 225), 1)
#         err_x = x + w // 2
#         err_y = y + h // 2
#         cv2.circle(img, (err_x, err_y), 2, (0, 0, 255), -1)
#         print(err_x, err_y)
#     cv2.imshow('img', img)
#     cv2.waitKey()
#
#     return err_x, err_y


def processing(img, mode):
    err = (0, 0)
    ih, iw, ch = img.shape
    if mode == COLOR_TRACK:
        pass

    return err


if __name__ == '__main__':
    img = cv2.imread('photo0.jpg')
    # trackcolor(img, [225, 114, 76])
    ct = ColorTracker([225, 114, 76])
    ex, ey = ct.track(img)
    print(ex, ey)
    ct.setColor([52, 207, 253])
    ex, ey = ct.track(img)
    print(ex, ey)

