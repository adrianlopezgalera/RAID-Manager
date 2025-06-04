# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'options.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QGroupBox,
    QLabel, QLayout, QPushButton, QSizePolicy,
    QWidget)

class Ui_Options(object):
    def setupUi(self, Options):
        if not Options.objectName():
            Options.setObjectName(u"Options")
        Options.setWindowModality(Qt.WindowModality.WindowModal)
        Options.resize(720, 480)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Options.sizePolicy().hasHeightForWidth())
        Options.setSizePolicy(sizePolicy)
        Options.setMinimumSize(QSize(720, 480))
        Options.setMaximumSize(QSize(720, 480))
        Options.setContextMenuPolicy(Qt.ContextMenuPolicy.ActionsContextMenu)
        Options.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.save_button = QPushButton(Options)
        self.save_button.setObjectName(u"save_button")
        self.save_button.setGeometry(QRect(590, 440, 80, 23))
        font = QFont()
        font.setBold(False)
        self.save_button.setFont(font)
        self.save_button.setContextMenuPolicy(Qt.ContextMenuPolicy.ActionsContextMenu)
        self.formGroupBox = QGroupBox(Options)
        self.formGroupBox.setObjectName(u"formGroupBox")
        self.formGroupBox.setGeometry(QRect(20, 40, 661, 258))
        self.raid_details = QFormLayout(self.formGroupBox)
        self.raid_details.setObjectName(u"raid_details")
        self.raid_details.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.raid_details.setHorizontalSpacing(6)
        self.raid_details.setVerticalSpacing(20)
        self.raid_details.setContentsMargins(1, -1, -1, -1)
        self.system_tray_label = QLabel(self.formGroupBox)
        self.system_tray_label.setObjectName(u"system_tray_label")

        self.raid_details.setWidget(0, QFormLayout.LabelRole, self.system_tray_label)

        self.system_tray_selector = QComboBox(self.formGroupBox)
        self.system_tray_selector.addItem("")
        self.system_tray_selector.addItem("")
        self.system_tray_selector.setObjectName(u"system_tray_selector")

        self.raid_details.setWidget(0, QFormLayout.FieldRole, self.system_tray_selector)

        self.cancel_button = QPushButton(Options)
        self.cancel_button.setObjectName(u"cancel_button")
        self.cancel_button.setGeometry(QRect(500, 440, 80, 23))

        self.retranslateUi(Options)

        QMetaObject.connectSlotsByName(Options)
    # setupUi

    def retranslateUi(self, Options):
        Options.setWindowTitle(QCoreApplication.translate("Options", u"Settings", None))
        self.save_button.setText(QCoreApplication.translate("Options", u"Save", None))
        self.system_tray_label.setText(QCoreApplication.translate("Options", u"System tray:", None))
        self.system_tray_selector.setItemText(0, QCoreApplication.translate("Options", u"Enabled", None))
        self.system_tray_selector.setItemText(1, QCoreApplication.translate("Options", u"Disabled", None))

        self.cancel_button.setText(QCoreApplication.translate("Options", u"Cancel", None))
    # retranslateUi

