import os
import tools
import shutil
from PySide6.QtCore import Qt, QSize
from PySide6.QtWidgets import QDialog, QPushButton, QLayout, QGridLayout, QHBoxLayout, QSizePolicy
from PySide6.QtGui import QIcon
from card_library_ui import Ui_Dialog
from functools import partial

class CardLibraryWindow(QDialog):
    def __init__(self, button:QPushButton):
        super().__init__()
        
        self.setWindowFlags(Qt.CustomizeWindowHint | Qt.WindowCloseButtonHint | Qt.WindowStaysOnTopHint )
        self.setGeometry(300, 100, 510, 400)  # 设置窗口位置和大小
        self.setStyleSheet("background-color: #EEE;")  # 设置背景透明
        self.setFixedWidth(510)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.cardLibraryRow = 0
        self.cardLibrarycolumn = 0
        self.lineupObjName = button.objectName()
        self.ui.lineup_text.setText(button.property('lineupName'))
        
        current_path = os.getcwd()
        self.lineup_path = current_path + '/select/' + self.lineupObjName
        if not os.path.exists(self.lineup_path):
            os.mkdir(self.lineup_path)
        self.lineup_images = tools.get_all_files(self.lineup_path)
        self.init_lineup_icon(self.lineup_path, self.lineup_images)
        self.card_library_path = current_path + '/cards'
        self.card_library_images = tools.get_all_files(self.card_library_path)
        self.init_card_library_icon(self.card_library_path, self.card_library_images)
        
    def get_card_button(self, objname: str, filename: str):
        
        pushButton = QPushButton()
        pushButton.setObjectName(objname)
        pushButton.setMinimumSize(QSize(50, 50))
        pushButton.setMaximumSize(QSize(50, 50))
        icon = QIcon()
        icon.addFile(filename , QSize(), QIcon.Normal, QIcon.Off)
        pushButton.setIcon(icon)
        pushButton.setIconSize(QSize(50, 50))
        pushButton.setFlat(True)
        pushButton.setSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        return pushButton
    
    def clean_layout(self, layout: QLayout):
        while layout.count(): # 清除所有控件
                item = layout.takeAt(0)
                widget = item.widget()
                if widget:
                    widget.deleteLater()
                else:
                    del item
    
    def card_click_event(self, button: QPushButton, currentLayout: QLayout, targetLayout: QLayout):

        self.clean_layout(currentLayout)
        self.clean_layout(targetLayout)
        if isinstance(targetLayout, QGridLayout):
            self.lineup_images.remove(button.objectName())
            os.remove(os.path.join(self.lineup_path, button.objectName()))
            
        if isinstance(targetLayout, QHBoxLayout):
            self.lineup_images.append(button.objectName())
            shutil.copy(os.path.join(self.card_library_path, button.objectName()), os.path.join(self.lineup_path))
        
        self.init_lineup_icon(self.lineup_path, self.lineup_images)
        self.init_card_library_icon(self.card_library_path, self.card_library_images)
        button.clicked.disconnect()
        button.clicked.connect(partial(self.card_click_event, button, targetLayout, currentLayout))
    
    def init_lineup_icon(self, path: str, filenames: list):
        self.lineupstretch = 0
        for filename in filenames:
            pushButton = self.get_card_button(filename, path + '/' + filename)
            pushButton.clicked.connect(partial(self.card_click_event, pushButton, self.ui.horizontalLayout, self.ui.gridLayout))
            self.ui.horizontalLayout.addWidget(pushButton, 0, Qt.AlignmentFlag.AlignLeft)
        self.ui.horizontalLayout.addStretch()

    def init_card_library_icon(self, path: str, filenames: list):
        
        self.cardLibraryRow = 0
        self.cardLibrarycolumn = 0
        for filename in filenames:
            
            if(filename in self.lineup_images): 
                continue
            pushButton = self.get_card_button(filename, path + '/' + filename)
            pushButton.clicked.connect(partial(self.card_click_event, pushButton, self.ui.gridLayout, self.ui.horizontalLayout))
            self.ui.gridLayout.addWidget(pushButton, self.cardLibraryRow, self.cardLibrarycolumn, 1, 1, Qt.AlignmentFlag.AlignLeft)
            self.cardLibrarycolumn += 1
            if self.cardLibrarycolumn == 9:
                self.cardLibrarycolumn = 0
                self.cardLibraryRow += 1
