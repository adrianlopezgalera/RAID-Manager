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
from PySide6.QtWidgets import (QApplication, QFormLayout, QLabel, QLineEdit,
    QSizePolicy, QWidget)

class Ui_New_Raid(object):
    def setupUi(self, New_Raid):
        if not New_Raid.objectName():
            New_Raid.setObjectName(u"New_Raid")
        New_Raid.resize(720, 480)
        self.formLayoutWidget = QWidget(New_Raid)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(30, 40, 661, 411))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.lineEdit = QLineEdit(self.formLayoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit)

        self.label = QLabel(self.formLayoutWidget)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)


        self.retranslateUi(New_Raid)

        QMetaObject.connectSlotsByName(New_Raid)
    # setupUi

    def retranslateUi(self, New_Raid):
        New_Raid.setWindowTitle(QCoreApplication.translate("New_Raid", u"Form", None))
        self.label.setText(QCoreApplication.translate("New_Raid", u"RAID Name:", None))
    # retranslateUi

