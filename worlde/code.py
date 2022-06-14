from PIL import ImageGrab
import os
import time
import win32api,win32con
import pyautogui
from newGuesser import *
from typer import *
#This assumes your resolution is 1920x1080
x_pad = 664
y_pad = 189
def screenGrab():
    box = (x_pad+1,y_pad+1,x_pad+1091,y_pad+357) 
    im = ImageGrab.grab(box)
    im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) + '.png','PNG')
def main():
    pass
def leftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def mousePos(cord):
    win32api.SetCursorPos((x_pad+cord[0],y_pad+cord[1]))
def get_cords():
    x,y = win32api.GetCursorPos()
    x = x - x_pad
    y = y - y_pad
    print(x,y)
    return (x,y)
    
def start_game():
    # S 157,737
    # A 108,737
    # L 501,737
    # E 181,668
    # T 282,668
    # ENTER KEY 
    mousePos((157,737))
    leftClick()
    time.sleep(.1)

    mousePos((108,737))
    leftClick()
    time.sleep(.1)
    
    mousePos((501,737))
    leftClick()
    time.sleep(.1)

    mousePos((181,668))
    leftClick()
    time.sleep(.1)

    mousePos((282,668))
    leftClick()
    time.sleep(.1)

    mousePos((92,800))
    leftClick()
    time.sleep(.1)
def colorScan():

    x, y = pyautogui.position()
    r,g,b = pyautogui.pixel(x, y)
    return r,g,b
 
        #time.sleep(0.1)
def colorCheck(r,g,b):
    if [r,g,b] == [181,159,59]:
        return 1
    elif [r,g,b] == [83,141,78]:
        return 2
    else:
        return 0
def scanLineOne():
    result = []
    #BLOCK 1 150,115
    #BLOCK 2 210,115
    #BLOCK 3 285,115
    #BLOCK 4 350,115
    #BLOCK 5 420,115
    mousePos((160,115))
    r,g,b = colorScan()
    result.append(colorCheck(r,g,b))

    mousePos((220,115))
    r,g,b = colorScan()
    result.append(colorCheck(r,g,b))

    mousePos((295,115)) #was 285
    r,g,b = colorScan()
    result.append(colorCheck(r,g,b))

    mousePos((360,115)) #was 350
    r,g,b = colorScan()
    result.append(colorCheck(r,g,b))

    mousePos((420,115))
    r,g,b = colorScan()
    result.append(colorCheck(r,g,b))

    print(result)
    return result

def scanLineTwo():
    result = []
    #BLOCK 1 150,205
    #BLOCK 2 210,295
    #BLOCK 3 285,385
    #BLOCK 4 350,475
    #BLOCK 5 420,565
    mousePos((160,177))
    r,g,b = colorScan()
    result.append(colorCheck(r,g,b))
    time.sleep(.1)

    mousePos((225,177))
    r,g,b = colorScan()
    result.append(colorCheck(r,g,b))
    time.sleep(.1)

    mousePos((295,177))
    r,g,b = colorScan()
    result.append(colorCheck(r,g,b))
    time.sleep(.1)

    mousePos((360,177))
    r,g,b = colorScan()
    result.append(colorCheck(r,g,b))
    time.sleep(.1)

    mousePos((420,177))
    r,g,b = colorScan()
    result.append(colorCheck(r,g,b))
    time.sleep(.1)

    print(result)
    return result
def scanLineThree():
    result = []
    #BLOCK 1 150,205
    #BLOCK 2 210,295
    #BLOCK 3 285,385
    #BLOCK 4 350,475
    #BLOCK 5 420,565
    mousePos((160,247))
    r,g,b = colorScan()
    result.append(colorCheck(r,g,b))
    time.sleep(.1)

    mousePos((225,247))
    r,g,b = colorScan()
    result.append(colorCheck(r,g,b))
    time.sleep(.1)

    mousePos((295,247))
    r,g,b = colorScan()
    result.append(colorCheck(r,g,b))
    time.sleep(.1)

    mousePos((360,247))
    r,g,b = colorScan()
    result.append(colorCheck(r,g,b))
    time.sleep(.1)

    mousePos((420,247))
    r,g,b = colorScan()
    result.append(colorCheck(r,g,b))
    time.sleep(.1)

    print(result)
    return result

def scanLineFour():
    result = []
    #BLOCK 1 150,205
    #BLOCK 2 210,295
    #BLOCK 3 285,385
    #BLOCK 4 350,475
    #BLOCK 5 420,565
    mousePos((160,317))
    r,g,b = colorScan()
    result.append(colorCheck(r,g,b))
    time.sleep(.1)

    mousePos((225,317))
    r,g,b = colorScan()
    result.append(colorCheck(r,g,b))
    time.sleep(.1)

    mousePos((295,317))
    r,g,b = colorScan()
    result.append(colorCheck(r,g,b))
    time.sleep(.1)

    mousePos((360,317))
    r,g,b = colorScan()
    result.append(colorCheck(r,g,b))
    time.sleep(.1)

    mousePos((420,317))
    r,g,b = colorScan()
    result.append(colorCheck(r,g,b))
    time.sleep(.1)

    print(result)
    return result

def scanLineFive():
    result = []
    #BLOCK 1 150,205
    #BLOCK 2 210,295
    #BLOCK 3 285,385
    #BLOCK 4 350,475
    #BLOCK 5 420,565
    mousePos((150,387))
    r,g,b = colorScan()
    result.append(colorCheck(r,g,b))
    time.sleep(.1)

    mousePos((225,387))
    r,g,b = colorScan()
    result.append(colorCheck(r,g,b))
    time.sleep(.1)

    mousePos((295,387))
    r,g,b = colorScan()
    result.append(colorCheck(r,g,b))
    time.sleep(.1)

    mousePos((360,387))
    r,g,b = colorScan()
    result.append(colorCheck(r,g,b))
    time.sleep(.1)

    mousePos((420,387))
    r,g,b = colorScan()
    result.append(colorCheck(r,g,b))
    time.sleep(.1)

    print(result)
    return result

if __name__ == '__main__':
    start_game() #SALET
    time.sleep(2)
    result1 = scanLineOne()
    result2 = []
    result3 = []
    result4 = []
    result5 = []
    if result1 != [2,2,2,2,2]:
        
        newWord,wordBank = grayFilter('salet',result1)
        typeWord(newWord)
        time.sleep(2)
        result2 = scanLineTwo()
    else:
        exit()
    
    if result2 != [2,2,2,2,2]:
        newWord1,wordBank1 = grayFilter(newWord,result2,wordBank)
        typeWord(newWord1)
        time.sleep(2)
        result3 = scanLineThree()
    else:
        exit()

    if result3 != [2,2,2,2,2]:
        newWord2,wordBank2 = grayFilter(newWord1,result3,wordBank1)
        typeWord(newWord2)
        time.sleep(2)
        result4 = scanLineFour()
    else:
        exit()
    
    if result4 != [2,2,2,2,2]:
        newWord3,wordBank3 = grayFilter(newWord2,result4,wordBank2)
        typeWord(newWord3)
        time.sleep(2)
        result5 = scanLineFive()
    else:
        exit()

    if result5 != [2,2,2,2,2]:
        newWord4,wordBank4 = grayFilter(newWord3,result5,wordBank3)
        typeWord(newWord4)
        time.sleep(2)
    else:
        exit()
    exit()
    
        

    
        
