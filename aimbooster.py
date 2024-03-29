import pyautogui
from PIL import Image
import win32api, win32con
import time

pixel_color = (255, 219, 195)
step = 10
time.sleep(2)

while True:
    screenshot = pyautogui.screenshot(region=(1120,345,601,422))

    for x in range(0, screenshot.width, step):
        for y in range(0, screenshot.height, step):
            if screenshot.getpixel((x, y)) == pixel_color:
                pixel_position = (x+1120, y+345)
                break
        else:
            continue 
        break 

    if 'pixel_position' in locals():
        win32api.SetCursorPos(pixel_position)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, pixel_position[0], pixel_position[1], 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, pixel_position[0], pixel_position[1], 0, 0)
        time.sleep(0.05)