# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_raid.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QLabel,
    QLayout, QLineEdit, QPushButton, QSizePolicy,
    QTextBrowser, QToolButton, QWidget)

class Ui_New_Raid(object):
    def setupUi(self, New_Raid):
        if not New_Raid.objectName():
            New_Raid.setObjectName(u"New_Raid")
        New_Raid.resize(720, 480)
        New_Raid.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.formLayoutWidget = QWidget(New_Raid)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(40, 40, 631, 361))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.formLayout.setHorizontalSpacing(6)
        self.formLayout.setVerticalSpacing(20)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.formLayoutWidget)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.lineEdit = QLineEdit(self.formLayoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit)

        self.rAIDLevelLabel = QLabel(self.formLayoutWidget)
        self.rAIDLevelLabel.setObjectName(u"rAIDLevelLabel")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.rAIDLevelLabel)

        self.rAIDLevelComboBox = QComboBox(self.formLayoutWidget)
        self.rAIDLevelComboBox.addItem("")
        self.rAIDLevelComboBox.addItem("")
        self.rAIDLevelComboBox.addItem("")
        self.rAIDLevelComboBox.addItem("")
        self.rAIDLevelComboBox.setObjectName(u"rAIDLevelComboBox")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.rAIDLevelComboBox)

        self.selectDevicesLabel = QLabel(self.formLayoutWidget)
        self.selectDevicesLabel.setObjectName(u"selectDevicesLabel")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.selectDevicesLabel)

        self.toolButton = QToolButton(self.formLayoutWidget)
        self.toolButton.setObjectName(u"toolButton")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.toolButton)

        self.textBrowser = QTextBrowser(self.formLayoutWidget)
        self.textBrowser.setObjectName(u"textBrowser")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy)
        self.textBrowser.setMaximumSize(QSize(500, 100))

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.textBrowser)

        self.pushButton_create = QPushButton(New_Raid)
        self.pushButton_create.setObjectName(u"pushButton_create")
        self.pushButton_create.setGeometry(QRect(590, 440, 80, 23))
        font = QFont()
        font.setBold(False)
        self.pushButton_create.setFont(font)
        self.pushButton_cancel = QPushButton(New_Raid)
        self.pushButton_cancel.setObjectName(u"pushButton_cancel")
        self.pushButton_cancel.setGeometry(QRect(500, 440, 80, 23))

        self.retranslateUi(New_Raid)

        QMetaObject.connectSlotsByName(New_Raid)
    # setupUi

    def retranslateUi(self, New_Raid):
        New_Raid.setWindowTitle(QCoreApplication.translate("New_Raid", u"Form", None))
        self.label.setText(QCoreApplication.translate("New_Raid", u"RAID Name:", None))
        self.rAIDLevelLabel.setText(QCoreApplication.translate("New_Raid", u"RAID Level:", None))
        self.rAIDLevelComboBox.setItemText(0, QCoreApplication.translate("New_Raid", u"0", None))
        self.rAIDLevelComboBox.setItemText(1, QCoreApplication.translate("New_Raid", u"1", None))
        self.rAIDLevelComboBox.setItemText(2, QCoreApplication.translate("New_Raid", u"5", None))
        self.rAIDLevelComboBox.setItemText(3, QCoreApplication.translate("New_Raid", u"6", None))

        self.selectDevicesLabel.setText(QCoreApplication.translate("New_Raid", u"RAID Devices:", None))
        self.toolButton.setText(QCoreApplication.translate("New_Raid", u"...", None))
        self.pushButton_create.setText(QCoreApplication.translate("New_Raid", u"Create", None))
        self.pushButton_cancel.setText(QCoreApplication.translate("New_Raid", u"Cancel", None))
    # retranslateUi

