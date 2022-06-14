from PIL import ImageGrab
import os
import time
import win32api,win32con
import pyautogui
from wordle import *
from code import *
x_pad = 664
y_pad = 189

def leftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    
def mousePos(cord):
    win32api.SetCursorPos((x_pad+cord[0],y_pad+cord[1]))
def typeA():
    mousePos((107,736))
    leftClick()
    time.sleep(.1)
def typeB():
    mousePos((358,807))
    leftClick()
    time.sleep(.1)
def typeC():
    mousePos((258,807))
    leftClick()
    time.sleep(.1)
def typeD():
    mousePos((205,736))
    leftClick()
    time.sleep(.1)
def typeE():
    mousePos((184,670))
    leftClick()
    time.sleep(.1)
def typeF():
    mousePos((258,732))
    leftClick()
    time.sleep(.1)
def typeG():
    mousePos((305,732))
    leftClick()
    time.sleep(.1)
def typeH():
    mousePos((354,732))
    leftClick()
    time.sleep(.1)
def typeI():
    mousePos((429,670))
    leftClick()
    time.sleep(.1)
def typeJ():
    mousePos((404,732))
    leftClick()
    time.sleep(.1)
def typeK():
    mousePos((454,732))
    leftClick()
    time.sleep(.1)
def typeL():
    mousePos((504,732))
    leftClick()
    time.sleep(.1)
def typeM():
    mousePos((458,807))
    leftClick()
    time.sleep(.1)
def typeN():
    mousePos((408,807))
    leftClick()
    time.sleep(.1)
def typeO():
    mousePos((479,670))
    leftClick()
    time.sleep(.1)
def typeP():
    mousePos((529,670))
    leftClick()
    time.sleep(.1)
def typeQ():
    mousePos((84,670))
    leftClick()
    time.sleep(.1)
def typeR():
    mousePos((234,670))
    leftClick()
    time.sleep(.1)
def typeS():
    mousePos((155,732))
    leftClick()
    time.sleep(.1)
def typeT():
    mousePos((284,670))
    leftClick()
    time.sleep(.1)
def typeU():
    mousePos((384,670))
    leftClick()
    time.sleep(.1)
def typeV():
    mousePos((308,807))
    leftClick()
    time.sleep(.1)
def typeW():
    mousePos((134,670))
    leftClick()
    time.sleep(.1)
def typeX():
    mousePos((208,807))
    leftClick()
    time.sleep(.1)
def typeY():
    mousePos((334,670))
    leftClick()
    time.sleep(.1)
def typeZ():
    mousePos((158,807))
    leftClick()
    time.sleep(.1)
def playAgain():
    time.sleep(10)
    mousePos((194,529))
    leftClick()
    time.sleep(10)
    mousePos((-595,709))
    leftClick()
    time.sleep(5)






def typeWord(word):
    print(word)
    for x in word:
        if x == 'a':
            typeA()
        if x == 'b':
            typeB()
        if x == 'c':
            typeC()
        if x == 'd':
            typeD()
        if x == 'e':
            typeE()
        if x == 'f':
            typeF()
        if x == 'g':
            typeG()
        if x == 'h':
            typeH()
        if x == 'i':
            typeI()
        if x == 'j':
            typeJ()
        if x == 'k':
            typeK()
        if x == 'l':
            typeL()
        if x == 'm':
            typeM()
        if x == 'n':
            typeN()
        if x == 'o':
            typeO()
        if x == 'p':
            typeP()
        if x == 'q':
            typeQ()
        if x == 'r':
            typeR()
        if x == 's':
            typeS()
        if x == 't':
            typeT()
        if x == 'u':
            typeU()
        if x == 'v':
            typeV()
        if x == 'w':
            typeW()
        if x == 'x':
            typeX()
        if x == 'y':
            typeY()
        if x == 'z':
            typeZ()

    mousePos((92,800))
    leftClick()
    time.sleep(.1)