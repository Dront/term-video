#!/usr/bin/env python3
import argparse
import os
import sys
import shutil
from time import time, sleep
import cv2

CLEAR_SCREEN_CODE = '\x1b[2J'
RESET_COLOR_CODE = '\x1b[0m'

def grayscale(pixel):
    return '\x1b[48;5;%dm ' % (232 + pixel // (256 / 23))

def rgb(pixel):
    p = pixel // (256 / 5)
    return '\x1b[48;5;%dm ' % (16 + (p[2] * 36) + (p[1] * 6) + p[0])

def video(name):
    cap = cv2.VideoCapture(name)
    frames_read = 0
    while cap.isOpened():
        grabbed, frame = cap.read()
        if not grabbed:
            break
        yield frame
    cap.release()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='shows video in terminal')
    parser.add_argument("video", type=str, default='test.webm', help="path to the video file")
    parser.add_argument("-gs", "--grayscale", help="grayscale instead of rgb", action="store_true")
    args = parser.parse_args()

    tone_func = grayscale if args.grayscale else rgb
    if args.grayscale:
        color_conv_func = lambda img: cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    else:
        color_conv_func = lambda img: img

    for count, frame in enumerate(video(args.video)):
        if count % 3:
            continue

        frame = color_conv_func(frame)
        term_size = shutil.get_terminal_size()
        img = cv2.resize(frame, term_size, interpolation=cv2.INTER_CUBIC)

        res = []
        for x in range(img.shape[0]):
            res.append(''.join(tone_func(img[x, y]) for y in range(img.shape[1])))
        term_data = '\n'.join(res)
        # sys.stdout.write(CLEAR_SCREEN_CODE)
        os.system('clear')
        sys.stdout.write(term_data)
        sys.stdout.write(RESET_COLOR_CODE)
        sys.stdout.flush()
        sleep(1 / 8)
