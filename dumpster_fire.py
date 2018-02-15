import curses
import random
import numpy as np
import traceback
from time import sleep

class DumpsterFire:
    def __init__(self, dump_model):
        self.dump_model = dump_model
        self.screen = curses.initscr()
        self.win_height = self.screen.getmaxyx()[0]
        self.win_width = self.screen.getmaxyx()[1]
        self.dumpster_height = 15
        self.dumpster_width = 50
        curses.curs_set(0)
        curses.start_color()
        curses.init_color(0, 0, 0, 0)
        curses.init_pair(1, 0, 0)
        curses.init_pair(2, 1, 0)
        curses.init_pair(3, 3, 0)
        curses.init_pair(4, 4, 0)
        curses.init_pair(5, 2, 0)
        self.screen.bkgd(' ', curses.color_pair(2))
        self.screen.clear

    def render(self):
        chars = [" ", ".", ":", "^", "*", "x", "s", "S", "#", "$"]
        width_start = self.win_width // 2 - self.dumpster_width // 2
        width_end = self.win_width // 2 + self.dumpster_width // 2
        dumpster_top = self.win_height - self.dumpster_height
        size = self.dumpster_width * self.dumpster_height
        buffer = np.zeros((self.dumpster_height, self.dumpster_width - 2), dtype=np.int)

        while True:
            for i in range(width_start, width_end):
                self.screen.addstr(
                    self.win_height - 1, i, "-", curses.color_pair(5))
                self.screen.addstr(dumpster_top, i, "-", curses.color_pair(5))

            for i in range(self.win_height - self.dumpster_height,
                           self.win_height):
                self.screen.addstr(i, width_start, "|", curses.color_pair(5))
                self.screen.addstr(i, width_end, "|", curses.color_pair(5))

            # Only attempt to start 7 fires.
            for i in range(7):
                buffer[0, int(random.random() * (self.dumpster_width - 2))] = 65

            for i in range(self.dumpster_height):
                for j in range(self.dumpster_width - 3):
                    buffer[i, j] = (buffer[i, j] +
                                    buffer[i, j + 1] + 
                                    buffer[i - 1, j + 1] +
                                    buffer[i - 1, j - 1]) // 4
                
                    color = 1
                    if buffer[i, j] > 15:
                        color = 4
                    elif buffer[i, j] > 9:
                        color = 3
                    elif buffer[i, j] > 4:
                        color = 2

                    self.screen.addstr(dumpster_top - i - 1,
                                       width_start + 2 + j,
                                       chars[9 if buffer[i,j] > 9 else buffer[i, j]],
                                       curses.color_pair(color) | curses.A_BOLD)

            sleep(0.016)
            self.screen.refresh()
            self.screen.timeout(30)
            if self.screen.getch() != -1:
                break

        curses.endwin()


if __name__ == "__main__":
    dump = DumpsterFire("Grizzly")
    try:
        dump.render()
    except:
        curses.endwin()
        print(traceback.format_exc())
