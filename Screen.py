from desktopmagic.screengrab_win32 import getRectAsImage
from threading import Thread
import time
import os


class Screen:

    def __init__(self, rect=(0, 0, 1, 1)):
        self.rect = rect
        self.update()

    def start(self):
        t = Thread(target=self._start, args=())
        t.start()

    def _start(self):
        while True:
            self.update()

    def update(self):
        try:
            self.image = getRectAsImage(self.rect).getpixel((0, 0))
        except:
            pass


if __name__ == "__main__":

    screen = Screen()
