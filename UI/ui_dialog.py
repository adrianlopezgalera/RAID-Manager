# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.setWindowModality(Qt.WindowModality.WindowModal)
        Dialog.resize(678, 266)
        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(40, 19, 631, 211))
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 70, 131, 41))
        self.text = QLineEdit(self.widget)
        self.text.setObjectName(u"text")
        self.text.setEnabled(False)
        self.text.setGeometry(QRect(210, 80, 381, 22))
        self.text.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.current_attribute = QLabel(self.widget)
        self.current_attribute.setObjectName(u"current_attribute")
        self.current_attribute.setGeometry(QRect(210, 30, 381, 20))
        self.current_attribute_label = QLabel(self.widget)
        self.current_attribute_label.setObjectName(u"current_attribute_label")
        self.current_attribute_label.setGeometry(QRect(40, 30, 121, 20))
        self.selector = QComboBox(self.widget)
        self.selector.setObjectName(u"selector")
        self.selector.setEnabled(False)
        self.selector.setGeometry(QRect(208, 80, 391, 23))
        self.ok_button = QPushButton(Dialog)
        self.ok_button.setObjectName(u"ok_button")
        self.ok_button.setGeometry(QRect(590, 230, 80, 23))
        font = QFont()
        font.setBold(False)
        self.ok_button.setFont(font)
        self.cancel_button = QPushButton(Dialog)
        self.cancel_button.setObjectName(u"cancel_button")
        self.cancel_button.setGeometry(QRect(500, 230, 80, 23))
        self.cancel_button.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText("")
#if QT_CONFIG(statustip)
        self.text.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.text.setText("")
        self.current_attribute.setText("")
        self.current_attribute_label.setText("")
        self.ok_button.setText(QCoreApplication.translate("Dialog", u"OK", None))
        self.cancel_button.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
    # retranslateUi

