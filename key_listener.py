import time
from pynput import keyboard

class KeyListener():
    
    def __init__(self, activateWindow) -> None:
        self.activateWindow = activateWindow
    
    def on_press(self, key):
        if key == keyboard.Key.f1:
            self.activateWindow()
        try:
            print('Key {} pressed'.format(key.char))
        except AttributeError:
            print('Special Key {} pressed'.format(key))

    def on_release(self, key):
        print('Key released')
        
    def start(self):
        self.listener = keyboard.Listener(on_press = self.on_press,on_release = self.on_release)
        self.listener.start()
    
    def stop(self):
        self.listener.stop()
        
