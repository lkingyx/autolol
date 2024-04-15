import time
from pynput import keyboard

class KeyListener():
    
    def __init__(self) -> None:
        self.window = None
    
    def setWindow(self, window):
        self.window = window
    
    def on_press(self, key):
        if key == keyboard.Key.f1:
            self.window.activateWindow()
        if key == keyboard.Key.f2:
            self.window.activateWindow()
            self.window.on_start_state_clicked()
        if key == keyboard.Key.f3:
            self.window.activateWindow()
            self.window.on_save_card_clicked()
        if key == keyboard.KeyCode.from_char('f'):
            self.window.previous_position = (0,0)

    def on_release(self, key):
        pass
        
    def start(self):
        self.listener = keyboard.Listener(on_press = self.on_press,on_release = self.on_release)
        self.listener.start()
        
