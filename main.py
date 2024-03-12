import os
import time
import threading
import tkinter as tk
import tools
class Main():
    def __init__(self) -> None:
        self.toggle_button = None
        self.state_var = None
        self.num = 0
        self.clicked = False
    
    def detectCards(self):
        while True:
            if self.state_var.get():
                path = os.getcwd()+'\\select\\'+selectVar.get()
                files = tools.get_all_files(path)
                for filename in files:
                    self.clicked = tools.get_card(path+'\\'+filename)
            time.sleep(0.05)

    def get_all_folders(self,directory):
        return [f for f in os.listdir(directory) if os.path.isdir(os.path.join(directory, f))]

    def showRadiobutton(self, top):
        # 获取当前目录下的所有文件夹
        folders = self.get_all_folders(os.getcwd() + '\\select')
        label = tk.Label(top, text="选择拿卡阵容：", anchor='nw')
        label.pack()
        if len(folders) == 0 : return
        # 定义变量来存储单选框的选择
        global selectVar
        selectVar = tk.StringVar(value=folders[0]) 
        # 打印所有文件夹
        for folder in folders:
            # 创建单选框并添加到Frame中
            radio = tk.Radiobutton(top, text=folder, variable=selectVar, value=folder)
            radio.pack()

    def close_all_windows(self, top, root, event=None):
        top.destroy()
        root.destroy()
    
    def toggle_state(self, state_var):
        # 切换状态变量的值
        state_var.set(not state_var.get())
        # 在按钮上显示当前状态
        self.toggle_button.config(text="自动拿卡：开" if state_var.get() else "自动拿卡：关")
    
    def create_floating_window(self,root, width, height, text):
        # 创建顶级窗口
        top = tk.Toplevel(root)
        
        # 设置窗口大小
        top.geometry(f'{width}x{height}+5+5')
        top.resizable(False, False)
        top.wm_attributes('-topmost', True)
        #set_window_style(floating_window, ctypes.windll.user32.GetWindowLongPtrW(floating_window.winfo_id(), -16) & &#126;0x20)
        
        # 创建开关按钮
        # 创建一个变量来存储按钮的状态
        self.state_var = tk.BooleanVar()
        self.state_var.set(False)
        self.toggle_button = tk.Button(top, text="自动拿卡：关", command=lambda: self.toggle_state(self.state_var))
        self.toggle_button.pack(pady= 10)
        
        self.showRadiobutton(top)

        # 绑定悬浮窗口的关闭事件
        top.protocol("WM_DELETE_WINDOW", lambda: self.close_all_windows(top, root))
        
        return top
    
    def main(self):
        # 创建主窗口
        root = tk.Tk()
        root.title("Floating Window Example")
        root.withdraw()
        
        # 创建悬浮窗口
        floating_window = self.create_floating_window(root, 200, 200, "Floating Window!")
    
        # 创建一个线程对象
        thread = threading.Thread(target=self.detectCards, daemon=True)
        # 启动线程
        thread.start()
        
        # 创建一个线程对象
        thread2 = threading.Thread(target=self.screen, daemon=True)
        # 启动线程
        thread2.start()
        
        # 开始事件循环
        root.mainloop()
 
    def screen(self): 
        while True:
            if self.state_var.get():
                tools.extract_cards()
            time.sleep(0.5)
 
if __name__ == '__main__':
    Main().main()