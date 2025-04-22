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
    QWidget)

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
        self.raid_name_label = QLabel(self.formLayoutWidget)
        self.raid_name_label.setObjectName(u"raid_name_label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.raid_name_label)

        self.raid_name = QLineEdit(self.formLayoutWidget)
        self.raid_name.setObjectName(u"raid_name")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.raid_name)

        self.raid_Level_Llabel = QLabel(self.formLayoutWidget)
        self.raid_Level_Llabel.setObjectName(u"raid_Level_Llabel")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.raid_Level_Llabel)

        self.raid_level = QComboBox(self.formLayoutWidget)
        self.raid_level.addItem("")
        self.raid_level.addItem("")
        self.raid_level.addItem("")
        self.raid_level.addItem("")
        self.raid_level.setObjectName(u"raid_level")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.raid_level)

        self.select_devices_label = QLabel(self.formLayoutWidget)
        self.select_devices_label.setObjectName(u"select_devices_label")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.select_devices_label)

        self.devices_path = QLabel(self.formLayoutWidget)
        self.devices_path.setObjectName(u"devices_path")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.devices_path)

        self.remove_devices = QPushButton(self.formLayoutWidget)
        self.remove_devices.setObjectName(u"remove_devices")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.remove_devices)

        self.devices = QComboBox(self.formLayoutWidget)
        self.devices.setObjectName(u"devices")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.devices)

        self.add_device = QPushButton(self.formLayoutWidget)
        self.add_device.setObjectName(u"add_device")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.add_device)

        self.new_raid_create = QPushButton(New_Raid)
        self.new_raid_create.setObjectName(u"new_raid_create")
        self.new_raid_create.setGeometry(QRect(590, 440, 80, 23))
        font = QFont()
        font.setBold(False)
        self.new_raid_create.setFont(font)
        self.new_raid_cancel = QPushButton(New_Raid)
        self.new_raid_cancel.setObjectName(u"new_raid_cancel")
        self.new_raid_cancel.setGeometry(QRect(500, 440, 80, 23))

        self.retranslateUi(New_Raid)

        QMetaObject.connectSlotsByName(New_Raid)
    # setupUi

    def retranslateUi(self, New_Raid):
        New_Raid.setWindowTitle(QCoreApplication.translate("New_Raid", u"New RAID", None))
        self.raid_name_label.setText(QCoreApplication.translate("New_Raid", u"RAID Name:", None))
#if QT_CONFIG(statustip)
        self.raid_name.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.raid_name.setText(QCoreApplication.translate("New_Raid", u"md0", None))
        self.raid_Level_Llabel.setText(QCoreApplication.translate("New_Raid", u"RAID Level:", None))
        self.raid_level.setItemText(0, QCoreApplication.translate("New_Raid", u"0", None))
        self.raid_level.setItemText(1, QCoreApplication.translate("New_Raid", u"1", None))
        self.raid_level.setItemText(2, QCoreApplication.translate("New_Raid", u"5", None))
        self.raid_level.setItemText(3, QCoreApplication.translate("New_Raid", u"6", None))

        self.select_devices_label.setText(QCoreApplication.translate("New_Raid", u"RAID Devices:", None))
        self.devices_path.setText("")
        self.remove_devices.setText(QCoreApplication.translate("New_Raid", u"Remove Selected Devices", None))
        self.add_device.setText(QCoreApplication.translate("New_Raid", u"Add Selected Device", None))
        self.new_raid_create.setText(QCoreApplication.translate("New_Raid", u"Create", None))
        self.new_raid_cancel.setText(QCoreApplication.translate("New_Raid", u"Cancel", None))
    # retranslateUi

