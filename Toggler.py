from pynput import mouse
from winsound import Beep
from threading import Thread


class Toggler:

    def __init__(self):
        self.enabled = False
        self.listener = mouse.Listener(on_click=self.on_click)
        self.listener.start()

    def on_click(self, x, y, button, pressed):

        if button == mouse.Button.x1:
            if pressed:

                freq = 500
                if self.enabled:
                    freq = 250

                Thread(target=self.beep, args=(freq,)).start()

                self.enabled = not self.enabled

        return True

    def beep(self, frequency: int | None = None):
        Beep(frequency=frequency, duration=250)
        return True


if __name__ == "__main__":

    t = Toggler()
    t.listener.join()
