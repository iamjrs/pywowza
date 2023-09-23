from Keyboard import *
from Toggler import *
from Screen import *
import time

import warnings
warnings.filterwarnings("ignore")


class Wowza:


    def __init__(self):

        self.toggler    = Toggler()
        self.screen     = Screen()
        self.kb         = Keyboard()


    def start(self):

        print('[*] Wowza is running...')

        while True:

            try:

                self.screen.update()

                if self.toggler.enabled:

                    r, g, b = self.screen.image

                    if 0 <= r <= 7 and g == 0 and b != 0:
                        self.kb.send_keys( r, b )

                time.sleep(.05)
            
            except KeyboardInterrupt:
                break

        print('[*] Wowza has stopped.')
        exit()


if __name__ == '__main__':

    w = Wowza()
    w.start()
