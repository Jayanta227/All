from typing import List
import random, curses, time
rand_arr = 0

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
    if y > 0 and x < w-1:
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
    temp = [[j for j in i] for i in rand_arr]
    for row, data in enumerate(rand_arr):
        for col, state in enumerate(data):
            if state == 1 and count_live_nbs(col, row) not in [2,3]:
                temp[row][col] = 0
            if state == 0 and count_live_nbs(col, row) == 3:
                temp[row][col] = 1
    rand_arr = [[j for j in i] for i in temp]


def print_grid(scr):
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
                block(scr, j+1, i+1)

def block(scr, x, y):
    scr.addch(y-1, 2*x-1, '■') # ■	█ 

def start(scr: curses.window):
    while True:
        # scr.clear()
        print_grid(scr)
        print_arr(scr, rand_arr)
        scr.refresh()
        next_gen()
        ch = scr.getch()
        if ch == curses.KEY_ENTER or ch in [10, 13, 113] :
            break
        if ch == 32:
            scr.nodelay(False)
            ch2 = scr.getch()
            if ch2 == 32:
                scr.nodelay(True)
        time.sleep(.3)


def main(scr: curses.window):
    global rand_arr
    h,w = scr.getmaxyx()
    curses.curs_set(0)
    create_rand_arr(w//2-1,h)
    message1 = "play pause this game by pressing spacebar"
    message2 = "press any key to start and exit game by pressing 'q' "
    message3 = "press spacebar then any other key to manually go to next generation"
    scr.addstr(h//2-1, w//2-len(message1)//2, message1)
    scr.addstr(h//2, w//2-len(message2)//2, message2)
    scr.addstr(h//2+1, w//2-len(message3)//2, message3)
    scr.getch()
    scr.nodelay(True)
    start(scr)


curses.wrapper(main)
