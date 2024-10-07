from ahk.directives import *
from ahk import AHK
from winsound import Beep
import time
import os
from threading import Thread


class Toggler:

    def __init__(self):
        self.enabled = False
        self.start()

    def toggle(self, toggle):
        freq = {True: 500, False: 250}
        setattr(self, toggle, not getattr(self, toggle))
        Beep(freq[getattr(self, toggle)], 200)

    def start(self):
        ts = [self._start_xb1]
        for t in ts:
            Thread(target=t, args=()).start()

    def _start_xb1(self):
        ahk = AHK(directives={NoTrayIcon})
        while True:
            try:
                ahk.key_wait("XButton1")
                self.toggle("enabled")
            except Exception() as e:
                print(repr(e))
            finally:
                time.sleep(0.1)


if __name__ == "__main__":

    t = Toggler()
