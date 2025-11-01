import sys
import keyboard
import win32api
import win32con

import time

def shouldIquit():
    if keyboard.is_pressed('esc'):
        sys.exit()

def Press(key):
    shouldIquit()
    keyboard.press(key)
    shouldIquit()
    time.sleep(0.1)
    keyboard.release(key)
    shouldIquit()

def moveMouse(x,y):
    shouldIquit()
    if x >= 0:
        for i in range(0,x):
            shouldIquit()
            win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 1, 0, 0, 0)
    else:
        for i in range(x,0):
            shouldIquit()
            win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, -1, 0, 0, 0)
    if y >= 0:
        for i in range(0,y):
            shouldIquit()
            win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 0, 1, 0, 0)
    else:
        for i in range(y,0):
            shouldIquit()
            win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 0, -1, 0, 0)
 
time.sleep(3)
 
while True:
    Press("e")
    moveMouse(800,0)
    moveMouse(0,50)
    Press("e")
    moveMouse(750,0)
    moveMouse(0,-50)
    Press("e")
    moveMouse(870,0)
    moveMouse(0,50)
    Press("e")
    moveMouse(825,0)
    moveMouse(0,-50)
    Press("e")
    Press("e")
    moveMouse(0,50)
    moveMouse(-825,0)
    Press("e")
    moveMouse(0,-50)
    moveMouse(-870,0)
    Press("e")
    moveMouse(0,50)
    moveMouse(-750,0)
    Press("e")
    moveMouse(0,-50)
    moveMouse(-800,0)
    Press("e")

