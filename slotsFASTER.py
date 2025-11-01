import keyboard
import win32api
import win32con
import pyautogui
import pynput
from pynput.mouse import Button, Controller

import time

mouse = Controller()

def leftClick():
    time.sleep(0.1)
    mouse.click(Button.left, 1)

def Press(key):
    keyboard.press(key)
    time.sleep(0.1)
    keyboard.release(key)

def moveMouse(x,y):
    if x >= 0:
        for i in range(0,x):
            #time.sleep(0.0005)
            win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 1, 0, 0, 0)
    else:
        for i in range(x,0):
            #time.sleep(0.0005)
            win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, -1, 0, 0, 0)
    if y >= 0:
        for i in range(0,y):
            #time.sleep(0.0005)
            win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 0, 1, 0, 0)
    else:
        for i in range(y,0):
            #time.sleep(0.0005)
            win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 0, -1, 0, 0)
 
time.sleep(3)
 
while True:
    Press("e")
    moveMouse(800,0)
    moveMouse(0,50)
    #time.sleep(0.5)
    Press("e")
    moveMouse(750,0)
    moveMouse(0,-50)
    #time.sleep(0.5)
    Press("e")
    moveMouse(870,0)
    moveMouse(0,50)
    #time.sleep(0.5)
    Press("e")
    moveMouse(825,0)
    moveMouse(0,-50)
    Press("e")
    #moveMouse(550,0)
    #Press("e")
    #moveMouse(-100,0)
    #moveMouse(0,325)
    #time.sleep(1)
    #Press("e")
    #time.sleep(1)
    #leftClick()
    #time.sleep(1)
    #moveMouse(0,-325)
    #moveMouse(100,0)
    #moveMouse(-550,0)
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

