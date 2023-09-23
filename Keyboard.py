from pynput.keyboard import Key, Controller

MOD_CONTROL = 1
MOD_SHIFT   = 2
MOD_ALT     = 4

class Keyboard:

    def __init__(self):
        
        self.kb = Controller()


    def send_keys( self, mod, key ):

        keys = []

        if mod >= MOD_ALT:
            keys.append(Key.alt)
            mod -= MOD_ALT

        if mod >= MOD_SHIFT:
            keys.append(Key.shift)
            mod -= MOD_SHIFT

        if mod >= MOD_CONTROL:
            keys.append(Key.ctrl)
            mod -= MOD_CONTROL

        keys.append(key)

        for k in keys:
            if type(k) == Key:
                self.kb.press(k)
            elif type(k) == int:
                self.kb.press( chr(k) )

        for k in keys:
            if type(k) == Key:
                self.kb.release(k)
            elif type(k) == int:
                self.kb.release( chr(k) )


if __name__ == '__main__':

    kb = Keyboard()
    kb.kb.press(chr(9))
    kb.kb.release(chr(9))
    