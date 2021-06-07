import curses, time
from typing import List
import numpy as np
import random
rand_arr = 0
live_nbs = 0
h = 0
w = 0

def create_rand_arr(x,y):
    global rand_arr
    rand_arr = [[random.randint(0,1) for i in range(x)] for j in range(y)]
    # print(rand_arr)

def count_live_nbs(x,y):

    h = len(rand_arr)
    w = len(rand_arr[0])
    live_nbs =0
    if y > 0 and x > 0:
        if rand_arr[y-1][x-1] == 1:
            live_nbs += 1
    if y > 0:
        if rand_arr[y-1][x] == 1:
            live_nbs += 1
    if y > 0 and x < h-1:
        if rand_arr[y-1][x+1] == 1:
            live_nbs += 1
    if (x > 0):
        if (rand_arr[y][x-1] == 1):
            live_nbs += 1
    if x < w-1:
        if rand_arr[y][x+1] == 1:
            live_nbs += 1
    if y < h-1 and x > 0:
        if rand_arr[y+1][x-1] == 1:
            live_nbs += 1
    if y < h-1:
        if rand_arr[y+1][x] == 1:
            live_nbs += 1
    if y < h-1 and x < w-1:
        if rand_arr[y+1][x+1] == 1:
            live_nbs += 1

    return live_nbs

def next_gen():
    global rand_arr
    temp = rand_arr.copy()
    for row, data in enumerate(rand_arr):
        for col, state in enumerate(data):
            if state == 1 and count_live_nbs(col, row) not in [2,3]:
                temp[row][col] = 0
            if state == 0 and count_live_nbs(col, row) == 3:
                temp[row][col] = 1
    rand_arr = temp.copy()


def print_borders(scr: curses.window):
    h,w = scr.getmaxyx()
    for i in range(h-1):
        for j in range(w-1):
            if i in [0, h-2]:
                scr.addch(i, j, '_')

            if j in [0, w-2]:
                scr.addch(i, j, '|')
    scr.refresh()

def print_grid(scr):
    global h,w
    h,w = scr.getmaxyx()
    for i in range(h):
        for j in range(w-1):
            scr.addch(i, j, '_')

            if j%2 == 0:
                scr.addch(i, j, '|')

    scr.refresh()

def print_arr(scr:curses.window, arr:List):#prints cell array to terminal
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == 1:
                block(j+1,i+1)

def block(x,y):
    scrn.addch(y-1, 2*x-1, '■') # ■	█ 




def main(scr: curses.window):
    global scrn , rand_arr,h, w
    h,w = scr.getmaxyx()
    # print_grid(scr)
    scrn = scr
    scr.nodelay(1)
    curses.curs_set(0)
    create_rand_arr(w//2-1,h)
    # create_rand_arr(10,10)
    # print_arr(scr, rand_arr)
    # scr.refresh()
    # scr.getch()

    while 1:
        # scr.clear()
        # print_borders(scr)
        # print_grid(scr)
        scr.clear()
        print_arr(scr, rand_arr)
        time.sleep(.5)
        scrn.refresh()
        next_gen()
        ch = scr.getch()
        if ch==113:
            break

curses.wrapper(main)
