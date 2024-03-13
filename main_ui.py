# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QPushButton,
    QRadioButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(200, 229)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.radioButton_5 = QRadioButton(Form)
        self.radioButton_5.setObjectName(u"radioButton_5")

        self.horizontalLayout_5.addWidget(self.radioButton_5)

        self.lineup5 = QPushButton(Form)
        self.lineup5.setObjectName(u"lineup5")

        self.horizontalLayout_5.addWidget(self.lineup5)


        self.gridLayout_2.addLayout(self.horizontalLayout_5, 12, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.radioButton_4 = QRadioButton(Form)
        self.radioButton_4.setObjectName(u"radioButton_4")

        self.horizontalLayout_4.addWidget(self.radioButton_4)

        self.lineup4 = QPushButton(Form)
        self.lineup4.setObjectName(u"lineup4")

        self.horizontalLayout_4.addWidget(self.lineup4)


        self.gridLayout_2.addLayout(self.horizontalLayout_4, 10, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.radioButton_2 = QRadioButton(Form)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.horizontalLayout_2.addWidget(self.radioButton_2)

        self.lineup2 = QPushButton(Form)
        self.lineup2.setObjectName(u"lineup2")

        self.horizontalLayout_2.addWidget(self.lineup2)


        self.gridLayout_2.addLayout(self.horizontalLayout_2, 5, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setProperty("get_state", False)

        self.verticalLayout.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setEnabled(True)

        self.verticalLayout.addWidget(self.pushButton)


        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.radioButton = QRadioButton(Form)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setChecked(True)

        self.horizontalLayout.addWidget(self.radioButton)

        self.lineup1 = QPushButton(Form)
        self.lineup1.setObjectName(u"lineup1")

        self.horizontalLayout.addWidget(self.lineup1)


        self.gridLayout_2.addLayout(self.horizontalLayout, 4, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.radioButton_3 = QRadioButton(Form)
        self.radioButton_3.setObjectName(u"radioButton_3")

        self.horizontalLayout_3.addWidget(self.radioButton_3)

        self.lineup3 = QPushButton(Form)
        self.lineup3.setObjectName(u"lineup3")

        self.horizontalLayout_3.addWidget(self.lineup3)


        self.gridLayout_2.addLayout(self.horizontalLayout_3, 8, 0, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_2, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Autolol", None))
        self.radioButton_5.setText(QCoreApplication.translate("Form", u"\u9635\u5bb95", None))
        self.lineup5.setText(QCoreApplication.translate("Form", u"\u7f16\u8f91", None))
        self.lineup5.setProperty("lineupName", QCoreApplication.translate("Form", u"\u9635\u5bb95", None))
        self.radioButton_4.setText(QCoreApplication.translate("Form", u"\u9635\u5bb94", None))
        self.lineup4.setText(QCoreApplication.translate("Form", u"\u7f16\u8f91", None))
        self.lineup4.setProperty("lineupName", QCoreApplication.translate("Form", u"\u9635\u5bb94", None))
        self.radioButton_2.setText(QCoreApplication.translate("Form", u"\u9635\u5bb92", None))
        self.lineup2.setText(QCoreApplication.translate("Form", u"\u7f16\u8f91", None))
        self.lineup2.setProperty("lineupName", QCoreApplication.translate("Form", u"\u9635\u5bb92", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"\u81ea\u52a8\u62ff\u5361\uff1a\u5173", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u81ea\u52a8\u5b58\u5361\uff1a\u5173", None))
        self.radioButton.setText(QCoreApplication.translate("Form", u"\u9635\u5bb91", None))
        self.lineup1.setText(QCoreApplication.translate("Form", u"\u7f16\u8f91", None))
        self.lineup1.setProperty("lineupName", QCoreApplication.translate("Form", u"\u9635\u5bb91", None))
        self.radioButton_3.setText(QCoreApplication.translate("Form", u"\u9635\u5bb93", None))
        self.lineup3.setText(QCoreApplication.translate("Form", u"\u7f16\u8f91", None))
        self.lineup3.setProperty("lineupName", QCoreApplication.translate("Form", u"\u9635\u5bb93", None))
    # retranslateUi

