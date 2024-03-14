import os
import sys
import time
import pyautogui
from concurrent.futures import ThreadPoolExecutor, as_completed
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QWidget, QButtonGroup, QPushButton
from PySide6.QtGui import QCloseEvent
import tools
from main_ui import Ui_Form
from card_library import CardLibraryWindow
from key_listener import KeyListener


class TransparentWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowFlags(Qt.WindowType.CustomizeWindowHint | Qt.WindowType.WindowCloseButtonHint | Qt.WindowType.WindowStaysOnTopHint)
        self.setGeometry(100, 100, 200, 200)  # 设置窗口位置和大小
        self.setStyleSheet("background-color: #EEE;")  # 设置背景透明
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.buttonGroup = QButtonGroup()
        self.buttonGroup.addButton(self.ui.radioButton)
        self.buttonGroup.addButton(self.ui.radioButton_2)
        self.buttonGroup.addButton(self.ui.radioButton_3)
        self.buttonGroup.addButton(self.ui.radioButton_4)
        self.buttonGroup.addButton(self.ui.radioButton_5)
        self.buttonGroup.buttonClicked.connect(self.on_button_clicked)

        self.ui.lineup1.clicked.connect(lambda: self.show_card_library_window(self.ui.lineup1))
        self.ui.lineup2.clicked.connect(lambda: self.show_card_library_window(self.ui.lineup2))
        self.ui.lineup3.clicked.connect(lambda: self.show_card_library_window(self.ui.lineup3))
        self.ui.lineup4.clicked.connect(lambda: self.show_card_library_window(self.ui.lineup4))
        self.ui.lineup5.clicked.connect(lambda: self.show_card_library_window(self.ui.lineup5))

        self.ui.pushButton_2.clicked.connect(self.on_start_state_clicked)
        self.ui.pushButton.clicked.connect(self.on_save_card_clicked)

        self.select_lineup_name = self.ui.radioButton.property('lineup')
        self.start_state = False
        self.save_card = False
        self.colse = False

        # 创建一个线程池对象
        self.executor = ThreadPoolExecutor(max_workers=15)

        # 添加拿卡任务
        self.executor.submit(self.detectCards)

        # 添加存卡任务
        self.executor.submit(self.screen)

    def detectCards(self):
        while True:
            if self.colse: return
            if self.start_state:
                path = os.getcwd() + '\\select\\' + self.select_lineup_name
                files = tools.get_all_files(path)
                image = pyautogui.screenshot(region=tools.card_locate)
                # 提交任务给线程池执行
                results = [self.executor.submit(tools.get_card, image, path + '\\' + filename) for filename in files]

                # 获取任务执行结果
                for future in as_completed(results):
                    future.result()

    def screen(self):
        while True:
            if self.colse:
                return
            if self.save_card:
                tools.extract_cards()
            time.sleep(0.5)

    def on_button_clicked(self, button: QButtonGroup):
        self.select_lineup_name = button.property('lineup')

    def on_start_state_clicked(self):
        if self.start_state:
            self.start_state = False
            self.ui.pushButton_2.setText(self.ui.pushButton_2.text().replace("开", "关"))
        else:
            self.start_state = True
            self.ui.pushButton_2.setText(self.ui.pushButton_2.text().replace("关", "开"))

    def on_save_card_clicked(self):
        if self.save_card:
            self.save_card = False
            self.ui.pushButton.setText(self.ui.pushButton.text().replace("开", "关"))
        else:
            self.save_card = True
            self.ui.pushButton.setText(self.ui.pushButton.text().replace("关", "开"))

    def show_card_library_window(self, button: QPushButton):
        CardLibraryWindow(button).exec()

    def closeEvent(self, event: QCloseEvent):
        # 在这里编写窗口关闭时的处理逻辑
        self.colse = True
        self.executor.shutdown()
        event.accept()


if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    window = TransparentWindow()
    window.show()
    KeyListener(window.activateWindow)
    #self.executor.submit(.start)
    sys.exit(app.exec())
