import pyautogui
import threading
from pynput import mouse

class ZDYQ():
    press = False
    is_lock = False
    mouse_location = (0,0)
    
    def __init__(self) -> None:
        threading.Thread(target=self.lock_location).start()
        listener = mouse.Listener(on_click=self.on_click)
        listener.start()
        
    def on_click(self, x,y,b,is_press):
        self.press = is_press;
        if(self.press and b == mouse.Button.left):
            self.mouse_location = (x, y)
            self.is_lock = True
        else:
            self.is_lock = False

    def lock_location(self):
        while True:
            if self.is_lock:
                pyautogui.moveTo(self.mouse_location[0], self.mouse_location[1])
            pyautogui.sleep(0.005)

ZDYQ()  
