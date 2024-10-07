import win32gui
import win32api


def get_pixel_color(x, y):
    hdc = win32gui.GetDC(0)
    color = win32gui.GetPixel(hdc, x, y)
    win32api.ReleaseDC(0, hdc)
    return color


print(get_pixel_color(0, 0))
