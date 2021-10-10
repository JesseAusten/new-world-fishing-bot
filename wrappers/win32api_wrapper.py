import win32api, win32con, win32gui, win32process
from time import sleep
import random

def click_mouse_with_coordinates(x, y):
    win32api.SetCursorPos((x, y))
    sleep(random.gauss(0.1, 0.05))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    sleep(random.gauss(0.09, 0.02))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

VK_CODE = {'tab':0x09,
           'b':0x42,
           'e':0x45,
           'r':0x52,
           'F3':0x72}

def press_key(key):
    win32api.keybd_event(VK_CODE[key], 0,0,0)

def release_key(key):
    win32api.keybd_event(VK_CODE[key],0 ,win32con.KEYEVENTF_KEYUP ,0)

def press_mouse_key():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)

def release_mouse_key():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

def make_fg():
    # Current window
    hcurr = win32gui.GetForegroundWindow()
    tcurr, _ = win32process.GetWindowThreadProcessId(hcurr)
    
    # New World window
    hremote = win32gui.FindWindow(None, 'New World')
    tremote, _ = win32process.GetWindowThreadProcessId(hremote)

    posx, posy = win32gui.GetCursorPos()

    win32process.AttachThreadInput(tcurr, tremote, True)
    win32gui.SetForegroundWindow(hremote)
    win32process.AttachThreadInput(tcurr, tremote, False)

    return hcurr, tcurr, tremote, posx, posy

def undo_fg(hprev, tprev, tcurr, posx, posy):
    win32process.AttachThreadInput(tcurr, tprev, True)
    win32gui.SetForegroundWindow(hprev)
    win32process.AttachThreadInput(tcurr, tprev, False)
    win32api.SetCursorPos((posx, posy))