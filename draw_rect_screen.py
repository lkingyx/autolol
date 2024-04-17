import ctypes
import  win32gui, win32api, win32con
from pywinauto.win32functions import *
import pyautogui

class DrawRectScreen():
    
    def __init__(self):
        self.dc = win32gui.GetDC(0)
        self.brush=win32gui.CreateSolidBrush(win32api.RGB(0, 255, 0))
        self.rect_list = []
        self.colse = False

    def startDraw(self):
        while True:
            if self.colse:
                win32gui.DeleteObject(self.brush)
                win32gui.DeleteDC(self.dc)
                return
            for rect in self.rect_list:
                win32gui.FrameRect(self.dc, rect, self.brush)
            pyautogui.sleep(0.01)
                
    def set_rect_list(self, rect_list):
        new_rect_list = []
        for rect in rect_list:
            new_rect_list.append(rect)
            new_rect_list.append((rect[0] - 1, rect[1] - 1, rect[2] + 1, rect[3] + 1))
        self.rect_list = new_rect_list

    def clear(self):
        self.rect_list = []

draw = DrawRectScreen()
draw.set_rect_list([(100,100,200,200)])
draw.startDraw()