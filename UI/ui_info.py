# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'info.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QHBoxLayout,
    QLabel, QLayout, QPushButton, QSizePolicy,
    QWidget)

class Ui_Info(object):
    def setupUi(self, Info):
        if not Info.objectName():
            Info.setObjectName(u"Info")
        Info.resize(720, 480)
        Info.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.formLayoutWidget = QWidget(Info)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(40, 40, 631, 281))
        self.raid_details = QFormLayout(self.formLayoutWidget)
        self.raid_details.setObjectName(u"raid_details")
        self.raid_details.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.raid_details.setHorizontalSpacing(6)
        self.raid_details.setVerticalSpacing(20)
        self.raid_details.setContentsMargins(0, 0, 0, 0)
        self.select_raid_label = QLabel(self.formLayoutWidget)
        self.select_raid_label.setObjectName(u"select_raid_label")

        self.raid_details.setWidget(0, QFormLayout.LabelRole, self.select_raid_label)

        self.select_raid = QComboBox(self.formLayoutWidget)
        self.select_raid.setObjectName(u"select_raid")

        self.raid_details.setWidget(0, QFormLayout.FieldRole, self.select_raid)

        self.raid_path_label = QLabel(self.formLayoutWidget)
        self.raid_path_label.setObjectName(u"raid_path_label")

        self.raid_details.setWidget(2, QFormLayout.LabelRole, self.raid_path_label)

        self.raid_path = QLabel(self.formLayoutWidget)
        self.raid_path.setObjectName(u"raid_path")

        self.raid_details.setWidget(2, QFormLayout.FieldRole, self.raid_path)

        self.raid_level_label = QLabel(self.formLayoutWidget)
        self.raid_level_label.setObjectName(u"raid_level_label")

        self.raid_details.setWidget(3, QFormLayout.LabelRole, self.raid_level_label)

        self.raid_level = QLabel(self.formLayoutWidget)
        self.raid_level.setObjectName(u"raid_level")

        self.raid_details.setWidget(3, QFormLayout.FieldRole, self.raid_level)

        self.select_size_label = QLabel(self.formLayoutWidget)
        self.select_size_label.setObjectName(u"select_size_label")

        self.raid_details.setWidget(4, QFormLayout.LabelRole, self.select_size_label)

        self.raid_size = QLabel(self.formLayoutWidget)
        self.raid_size.setObjectName(u"raid_size")

        self.raid_details.setWidget(4, QFormLayout.FieldRole, self.raid_size)

        self.raid_state_label = QLabel(self.formLayoutWidget)
        self.raid_state_label.setObjectName(u"raid_state_label")

        self.raid_details.setWidget(5, QFormLayout.LabelRole, self.raid_state_label)

        self.raid_state = QLabel(self.formLayoutWidget)
        self.raid_state.setObjectName(u"raid_state")

        self.raid_details.setWidget(5, QFormLayout.FieldRole, self.raid_state)

        self.raid_devices_label = QLabel(self.formLayoutWidget)
        self.raid_devices_label.setObjectName(u"raid_devices_label")

        self.raid_details.setWidget(6, QFormLayout.LabelRole, self.raid_devices_label)

        self.raid_devices = QLabel(self.formLayoutWidget)
        self.raid_devices.setObjectName(u"raid_devices")

        self.raid_details.setWidget(6, QFormLayout.FieldRole, self.raid_devices)

        self.apply_button = QPushButton(self.formLayoutWidget)
        self.apply_button.setObjectName(u"apply_button")

        self.raid_details.setWidget(1, QFormLayout.FieldRole, self.apply_button)

        self.OK_button = QPushButton(Info)
        self.OK_button.setObjectName(u"OK_button")
        self.OK_button.setGeometry(QRect(590, 440, 80, 23))
        font = QFont()
        font.setBold(False)
        self.OK_button.setFont(font)
        self.OK_button.setContextMenuPolicy(Qt.ContextMenuPolicy.ActionsContextMenu)
        self.row1 = QWidget(Info)
        self.row1.setObjectName(u"row1")
        self.row1.setGeometry(QRect(30, 350, 631, 33))
        self.horizontalLayout = QHBoxLayout(self.row1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.active_label = QLabel(self.row1)
        self.active_label.setObjectName(u"active_label")

        self.horizontalLayout.addWidget(self.active_label)

        self.active_devices = QLabel(self.row1)
        self.active_devices.setObjectName(u"active_devices")

        self.horizontalLayout.addWidget(self.active_devices)

        self.working_label = QLabel(self.row1)
        self.working_label.setObjectName(u"working_label")

        self.horizontalLayout.addWidget(self.working_label)

        self.working_devices = QLabel(self.row1)
        self.working_devices.setObjectName(u"working_devices")

        self.horizontalLayout.addWidget(self.working_devices)

        self.row2 = QWidget(Info)
        self.row2.setObjectName(u"row2")
        self.row2.setGeometry(QRect(30, 390, 631, 33))
        self.horizontalLayout_3 = QHBoxLayout(self.row2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.failed_label = QLabel(self.row2)
        self.failed_label.setObjectName(u"failed_label")

        self.horizontalLayout_3.addWidget(self.failed_label)

        self.failed_devices = QLabel(self.row2)
        self.failed_devices.setObjectName(u"failed_devices")

        self.horizontalLayout_3.addWidget(self.failed_devices)

        self.spare_label = QLabel(self.row2)
        self.spare_label.setObjectName(u"spare_label")

        self.horizontalLayout_3.addWidget(self.spare_label)

        self.spare_devices = QLabel(self.row2)
        self.spare_devices.setObjectName(u"spare_devices")

        self.horizontalLayout_3.addWidget(self.spare_devices)


        self.retranslateUi(Info)

        QMetaObject.connectSlotsByName(Info)
    # setupUi

    def retranslateUi(self, Info):
        Info.setWindowTitle(QCoreApplication.translate("Info", u"Info about a RAID", None))
        self.select_raid_label.setText(QCoreApplication.translate("Info", u"Select RAID:", None))
        self.raid_path_label.setText(QCoreApplication.translate("Info", u"RAID Path:", None))
        self.raid_path.setText("")
        self.raid_level_label.setText(QCoreApplication.translate("Info", u"RAID Level:", None))
        self.raid_level.setText("")
        self.select_size_label.setText(QCoreApplication.translate("Info", u"RAID Size:", None))
        self.raid_size.setText("")
        self.raid_state_label.setText(QCoreApplication.translate("Info", u"RAID State:", None))
        self.raid_state.setText("")
        self.raid_devices_label.setText(QCoreApplication.translate("Info", u"RAID Devices:", None))
        self.raid_devices.setText("")
        self.apply_button.setText(QCoreApplication.translate("Info", u"Apply", None))
        self.OK_button.setText(QCoreApplication.translate("Info", u"OK", None))
        self.active_label.setText(QCoreApplication.translate("Info", u"Active devices:", None))
        self.active_devices.setText("")
        self.working_label.setText(QCoreApplication.translate("Info", u"Working devices:", None))
        self.working_devices.setText("")
        self.failed_label.setText(QCoreApplication.translate("Info", u"Failed devices:", None))
        self.failed_devices.setText("")
        self.spare_label.setText(QCoreApplication.translate("Info", u"Spare devices:", None))
        self.spare_devices.setText("")
    # retranslateUi

