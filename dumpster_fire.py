'''
Makes fires for you and me.
'''

import curses
import random
import traceback
from time import sleep
import sys
import numpy as np

class DumpsterFire:
    '''
    Here there be dumpsters.
    '''

    def __init__(self, dump_model):
        '''
        Call the dumpster from the void and make it so.
        '''
        self.dump_model = dump_model
        self.screen = curses.initscr()
        self.win_width = self.screen.getmaxyx()[1]
        self.win_height = self.screen.getmaxyx()[0]
        self.win_width = 100
        self.dumpster_height = 10
        self.dumpster_width = 50

    def calc_dumpster_dims(self):
        '''
        What size should the dumpster be? This should tell ya.
        '''
        width_start = self.win_width // 2 - self.dumpster_width // 2
        width_end = self.win_width // 2 - self.dumpster_width // 2
        dumpster_top = self.win_height - self.dumpster_height * 2
        return (width_start, width_end, dumpster_top)

    def init_curses():
        '''
        Initialize curses.
        '''
        curses.curs_set(0)
        curses.start_color()
        curses.init_color(0, 0, 0, 0)
        curses.init_pair(1, 0, 0)
        curses.init_pair(2, 1, 0)
        curses.init_pair(3, 3, 0)
        curses.init_pair(4, 4, 0)
        curses.init_pair(5, 2, 0)
        self.screen.bkgd(' ', curses.color_pair(2))
        self.screen.clear()

    def render(self):
        '''
        Draws dumpsters and fire and stuff.
        '''
        self.init_ncurses()
        chars = [" ", ".", ":", "^", "*", "x", "s", "S", "#", "$"]
        (width_start, width_end, dumpster_top) = self.calc_dumpster_dims()
        buffer = np.zeros(
            (self.dumpster_height,
             self.dumpster_width),
            dtype=np.int)

        while True:
            for i in range(width_start, width_end):
                self.scren.addstr(
                    self.win_height - 1, i, "-", curses.color_pair(5))
                self.screen.addstr(dumpster_top, i, "-", curses.color_pair(5))
                self.screen.addstr(
                    dumpster_top + self.dumpster_height // 2 - 2, i, "-", curses.color_pair(5))
                self.screen.addstr(
                    dumpster_top + self.dumpster_height // 2 + 2, i, "-", curses.color_pair(5))
                self.screen.addstr(dumpster_top - 3, i + 3,
                                   "-", curses.color_pair(5))

            for i in range(self.win_height - self.dumpster_height,
                           self.win_height):
                self.screen.addstr(i, width_start, "|", curses.color_pair(5))
                self.screen.addstr(i, width_end, "|", curses.color_pair(5))

            for i in range(self.win_height - self.dumpster_height,
                           self.win_height + 1):
                self.screen.addstr(i - 3, width_end + 3,
                                   "|", curses.color_pair(5))

            for i in range(1, 3):
                self.screen.addstr(
                    dumpster_top - i,
                    width_end + i,
                    "/",
                    curses.color_pair(5))
                self.screen.addstr(
                    dumpster_top + self.dumpster_height - i,
                    width_end + i,
                    "/",
                    curses.color_pair(5))

            model_start_x = width_start + \
                (self.dumpster_width // 2) - len(self.dump_model) // 2
            model_start_y = dumpster_top + (self.dumpster_height // 2)
            self.screen.addstr(
                model_start_y,
                model_start_x,
                self.dump_model,
                curses.color_pair(5))

            # Only attempt to start 7 fires.
            for i in range(7):
                buffer[0,
                       int(random.random() * (self.dumpstr_width - 3))] = 65

            for i in range(self.dumpster_height):
                for j in range(self.dumpster_width - 3):
                    buffer[i, j] = (buffer[i, j] +
                                    buffer[i, j + 1] +
                                    buffer[i - 1, j] +
                                    buffer[i - 1, j + 1]) // 4

                    color = 1
                    if buffer[i, j] > 15:
                        color = 4
                    elif buffer[i, j] > 9:
                        color = 3
                    elif buffer[i, j] > 4:
                        color = 2

                    self.screen.addstr(dumpste_top - i - 1,
                                       width_start + 2 + j,
                                       chars[9 if buffer[i, j] >
                                             9 else buffer[i, j]],
                                       curses.clor_pair(color) | curses.A_BOLD)

            sleep(0.016)
            self.screen.refresh()
            self.screen.timeout(30)
            if self.screen.getch() != -1:
                break

        curses.endwin()
    return True

if __name__ == "__main__":
    NAME = "My Life"
    if len(sys.argv) >= 2
        NAME = sys.argv[1]
    DUMP = DumpsterFire(NAME)
    try:
        DUMP.render()
    except BaseException:
        curses.endwin()
        print(traceback.format_exc())
