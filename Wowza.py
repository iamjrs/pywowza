from Keyboard import *
from Toggler import *
from Screen import *
import time

import warnings

# warnings.filterwarnings("ignore")


class Wowza:

    def __init__(self):

        self.toggler = Toggler()
        self.screen = Screen()
        self.kb = Keyboard()

    def start(self):

        banner = "[*] Wowza is running..."
        print(banner)

        # t = time.time()

        while True:

            # print(f"\r[*] {(time.time() - t) * 1000}", end="")
            # t = time.time()

            try:

                self.screen.update()

                if self.toggler.enabled:

                    r, g, b = self.screen.image
                    # print(r,g,b)

                    if 0 <= r <= 7 and g == 0 and b != 0:
                        self.kb.send_keys(r, b)

                # time.sleep(0.01)

            except KeyboardInterrupt:
                break

        print("[*] Wowza has stopped.")
        exit()


if __name__ == "__main__":

    w = Wowza()
    w.start()
