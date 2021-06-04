
import curses
import os, subprocess
for root, dir, files in os.walk(os.getcwd()):
    break

files.append("BACK")
menu = ['Create local home', 'Quit (q)']


def print_menu(stdscr, selected_row_idx, arr):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    for idx, row in enumerate(arr):
        x = w//2 - len(row)//2
        y = h//2 - len(menu)//2 + idx
        if idx == selected_row_idx:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, x, row)
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(y, x, row)
    stdscr.refresh()


def print_center(stdscr, text):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    x = w//2 - len(text)//2
    y = h//2
    stdscr.addstr(y, x, text)
    stdscr.refresh()


def cr_home(stdscr):
    current_row_files = 0
    print_menu(stdscr, current_row_files, files)

    while 1:
        key = stdscr.getch()

        if key == 98:
            break
        if key == curses.KEY_UP and current_row_files > 0:
            current_row_files -= 1

        elif key == curses.KEY_DOWN and current_row_files < len(files)-1:
            current_row_files += 1

        elif key == curses.KEY_ENTER or key in [10, 13]:
            if current_row_files != len(files)-1:
                stdscr.attron(curses.color_pair(1))
                print_center(stdscr, "create local home and make appimage executable")
                stdscr.attroff(curses.color_pair(1))
                key = stdscr.getch()

                if key == curses.KEY_ENTER or key in [10, 13]:
                    mkdir = subprocess.run(['mkdir',  files[current_row_files].strip()+'.home'], universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

                    chmod = subprocess.run(['chmod', '+x', files[current_row_files].strip()], universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

                    if mkdir.stderr:
                        stdscr.clear()
                        stdscr.addstr(mkdir.stderr)
                        stdscr.refresh()
                        stdscr.getch()

                    if chmod.stderr:
                        stdscr.clear()
                        stdscr.addstr(chmod.stderr)
                        stdscr.refresh()
                        stdscr.getch()

            # if user selected last row, exit the program
            elif current_row_files == len(files)-1:
                break

        print_menu(stdscr, current_row_files, files)


def main(stdscr):
    # turn off cursor blinking
    curses.curs_set(0)

    # color scheme for selected row
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

    # specify the current selected row
    current_row = 0

    # print the menu
    print_menu(stdscr, current_row, menu)

    while 1:
        
        key = stdscr.getch()
        # stdscr.clear()
        # stdscr.addstr(str(key))
        # stdscr.refresh()
        # stdscr.getch()
        if key == 113:
            # q to quit application
            break
        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(menu)-1:
            current_row += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            # if user selected last row, exit the program
            if current_row == len(menu)-1:
                break
            if current_row == 0:
                cr_home(stdscr)

        print_menu(stdscr, current_row, menu)


curses.wrapper(main)
