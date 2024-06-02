from pyautogui import *
import pyautogui
import keyboard
import numpy as np
import random
import win32, win32con
import win32api
import random

ranx = random.randint(1,1980)
rany = random.randint(1,1080)

def click(x, y):
    win32api.SetCursorPos((x,y))
    #win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    #time.sleep(0.1)
    #win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
while True:
    click (ranx,rany)
    ranx = random.randint(1,1980)
    rany = random.randint(1,1080)
    
