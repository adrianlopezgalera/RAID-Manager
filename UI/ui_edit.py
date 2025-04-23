# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'edit.ui'
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

class Ui_Edit(object):
    def setupUi(self, Edit):
        if not Edit.objectName():
            Edit.setObjectName(u"Edit")
        Edit.setEnabled(True)
        Edit.resize(720, 480)
        Edit.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        Edit.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.formLayoutWidget = QWidget(Edit)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(40, 40, 621, 151))
        self.raid_selector = QFormLayout(self.formLayoutWidget)
        self.raid_selector.setObjectName(u"raid_selector")
        self.raid_selector.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.raid_selector.setHorizontalSpacing(6)
        self.raid_selector.setVerticalSpacing(20)
        self.raid_selector.setContentsMargins(0, 0, 0, 0)
        self.select_raid_label = QLabel(self.formLayoutWidget)
        self.select_raid_label.setObjectName(u"select_raid_label")

        self.raid_selector.setWidget(0, QFormLayout.LabelRole, self.select_raid_label)

        self.select_raid = QComboBox(self.formLayoutWidget)
        self.select_raid.setObjectName(u"select_raid")

        self.raid_selector.setWidget(0, QFormLayout.FieldRole, self.select_raid)

        self.apply_button = QPushButton(self.formLayoutWidget)
        self.apply_button.setObjectName(u"apply_button")

        self.raid_selector.setWidget(1, QFormLayout.FieldRole, self.apply_button)

        self.selected_raid_label = QLabel(self.formLayoutWidget)
        self.selected_raid_label.setObjectName(u"selected_raid_label")

        self.raid_selector.setWidget(2, QFormLayout.LabelRole, self.selected_raid_label)

        self.selected_raid = QLabel(self.formLayoutWidget)
        self.selected_raid.setObjectName(u"selected_raid")

        self.raid_selector.setWidget(2, QFormLayout.FieldRole, self.selected_raid)

        self.row_1 = QWidget(Edit)
        self.row_1.setObjectName(u"row_1")
        self.row_1.setGeometry(QRect(31, 220, 628, 43))
        self.horizontalLayout = QHBoxLayout(self.row_1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.change_name_button = QPushButton(self.row_1)
        self.change_name_button.setObjectName(u"change_name_button")

        self.horizontalLayout.addWidget(self.change_name_button)

        self.add_drive_button = QPushButton(self.row_1)
        self.add_drive_button.setObjectName(u"add_drive_button")

        self.horizontalLayout.addWidget(self.add_drive_button)

        self.remove_drive_button = QPushButton(self.row_1)
        self.remove_drive_button.setObjectName(u"remove_drive_button")

        self.horizontalLayout.addWidget(self.remove_drive_button)

        self.row_2 = QWidget(Edit)
        self.row_2.setObjectName(u"row_2")
        self.row_2.setGeometry(QRect(31, 270, 628, 43))
        self.horizontalLayout_2 = QHBoxLayout(self.row_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.change_level_button = QPushButton(self.row_2)
        self.change_level_button.setObjectName(u"change_level_button")

        self.horizontalLayout_2.addWidget(self.change_level_button)

        self.assemble_button = QPushButton(self.row_2)
        self.assemble_button.setObjectName(u"assemble_button")

        self.horizontalLayout_2.addWidget(self.assemble_button)

        self.stop_button = QPushButton(self.row_2)
        self.stop_button.setObjectName(u"stop_button")

        self.horizontalLayout_2.addWidget(self.stop_button)

        self.row_3 = QWidget(Edit)
        self.row_3.setObjectName(u"row_3")
        self.row_3.setGeometry(QRect(30, 320, 631, 43))
        self.horizontalLayout_3 = QHBoxLayout(self.row_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.delete_button = QPushButton(self.row_3)
        self.delete_button.setObjectName(u"delete_button")
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(238, 29, 0, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(255, 121, 102, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(246, 75, 51, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(119, 14, 0, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush4)
        brush5 = QBrush(QColor(159, 19, 0, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        brush6 = QBrush(QColor(255, 255, 255, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush6)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush)
        brush7 = QBrush(QColor(246, 142, 127, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush7)
        brush8 = QBrush(QColor(255, 255, 220, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush8)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
        brush9 = QBrush(QColor(0, 0, 0, 127))
        brush9.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush9)
#endif
        palette.setBrush(QPalette.Active, QPalette.Accent, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush7)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush8)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush9)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.Accent, brush6)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush6)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush8)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
        brush10 = QBrush(QColor(119, 14, 0, 127))
        brush10.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush10)
#endif
        brush11 = QBrush(QColor(255, 79, 54, 255))
        brush11.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Accent, brush11)
        self.delete_button.setPalette(palette)

        self.horizontalLayout_3.addWidget(self.delete_button)

        self.cancel_button = QPushButton(Edit)
        self.cancel_button.setObjectName(u"cancel_button")
        self.cancel_button.setGeometry(QRect(580, 430, 80, 23))

        self.retranslateUi(Edit)

        QMetaObject.connectSlotsByName(Edit)
    # setupUi

    def retranslateUi(self, Edit):
        Edit.setWindowTitle(QCoreApplication.translate("Edit", u"Edit a RAID", None))
        self.select_raid_label.setText(QCoreApplication.translate("Edit", u"Select RAID:", None))
        self.apply_button.setText(QCoreApplication.translate("Edit", u"Apply", None))
        self.selected_raid_label.setText(QCoreApplication.translate("Edit", u"Selected RAID:", None))
        self.selected_raid.setText("")
        self.change_name_button.setText(QCoreApplication.translate("Edit", u"Change name", None))
        self.add_drive_button.setText(QCoreApplication.translate("Edit", u"Add drive", None))
        self.remove_drive_button.setText(QCoreApplication.translate("Edit", u"Remove drive", None))
        self.change_level_button.setText(QCoreApplication.translate("Edit", u"Change level", None))
        self.assemble_button.setText(QCoreApplication.translate("Edit", u"Asemble", None))
        self.stop_button.setText(QCoreApplication.translate("Edit", u"Stop", None))
        self.delete_button.setText(QCoreApplication.translate("Edit", u"Delete", None))
        self.cancel_button.setText(QCoreApplication.translate("Edit", u"Cancel", None))
    # retranslateUi

