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
        self.formLayoutWidget.setGeometry(QRect(40, 40, 621, 132))
        self.raid_selector = QFormLayout(self.formLayoutWidget)
        self.raid_selector.setObjectName(u"raid_selector")
        self.raid_selector.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.raid_selector.setHorizontalSpacing(0)
        self.raid_selector.setVerticalSpacing(40)
        self.raid_selector.setContentsMargins(0, 0, 0, 0)
        self.select_raid_label = QLabel(self.formLayoutWidget)
        self.select_raid_label.setObjectName(u"select_raid_label")

        self.raid_selector.setWidget(0, QFormLayout.LabelRole, self.select_raid_label)

        self.select_raid = QComboBox(self.formLayoutWidget)
        self.select_raid.setObjectName(u"select_raid")

        self.raid_selector.setWidget(0, QFormLayout.FieldRole, self.select_raid)

        self.selected_raid = QLabel(self.formLayoutWidget)
        self.selected_raid.setObjectName(u"selected_raid")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.selected_raid.sizePolicy().hasHeightForWidth())
        self.selected_raid.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(18)
        self.selected_raid.setFont(font)

        self.raid_selector.setWidget(1, QFormLayout.FieldRole, self.selected_raid)

        self.selected_raid_label = QLabel(self.formLayoutWidget)
        self.selected_raid_label.setObjectName(u"selected_raid_label")

        self.raid_selector.setWidget(1, QFormLayout.LabelRole, self.selected_raid_label)

        self.row_1 = QWidget(Edit)
        self.row_1.setObjectName(u"row_1")
        self.row_1.setGeometry(QRect(30, 250, 628, 43))
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
        self.row_2.setGeometry(QRect(30, 300, 628, 43))
        self.horizontalLayout_2 = QHBoxLayout(self.row_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.change_level_button = QPushButton(self.row_2)
        self.change_level_button.setObjectName(u"change_level_button")

        self.horizontalLayout_2.addWidget(self.change_level_button)

        self.stop_button = QPushButton(self.row_2)
        self.stop_button.setObjectName(u"stop_button")

        self.horizontalLayout_2.addWidget(self.stop_button)

        self.delete_button = QPushButton(self.row_2)
        self.delete_button.setObjectName(u"delete_button")
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(251, 251, 251, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(255, 255, 255, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(253, 253, 253, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(125, 125, 125, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush4)
        brush5 = QBrush(QColor(167, 167, 167, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        brush6 = QBrush(QColor(255, 255, 220, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush6)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
        brush7 = QBrush(QColor(0, 0, 0, 127))
        brush7.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush7)
#endif
        palette.setBrush(QPalette.Active, QPalette.Accent, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush7)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.Accent, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush6)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
        brush8 = QBrush(QColor(125, 125, 125, 127))
        brush8.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush8)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.Accent, brush2)
        self.delete_button.setPalette(palette)

        self.horizontalLayout_2.addWidget(self.delete_button)

        self.cancel_button = QPushButton(Edit)
        self.cancel_button.setObjectName(u"cancel_button")
        self.cancel_button.setGeometry(QRect(570, 430, 80, 23))
        self.assemble_button = QPushButton(Edit)
        self.assemble_button.setObjectName(u"assemble_button")
        self.assemble_button.setGeometry(QRect(260, 380, 171, 31))

        self.retranslateUi(Edit)

        QMetaObject.connectSlotsByName(Edit)
    # setupUi

    def retranslateUi(self, Edit):
        Edit.setWindowTitle(QCoreApplication.translate("Edit", u"Edit a RAID", None))
        self.select_raid_label.setText(QCoreApplication.translate("Edit", u"Select RAID:", None))
        self.selected_raid.setText("")
        self.selected_raid_label.setText(QCoreApplication.translate("Edit", u"Selected RAID:", None))
        self.change_name_button.setText(QCoreApplication.translate("Edit", u"Change name", None))
        self.add_drive_button.setText(QCoreApplication.translate("Edit", u"Add drive", None))
        self.remove_drive_button.setText(QCoreApplication.translate("Edit", u"Remove drive", None))
        self.change_level_button.setText(QCoreApplication.translate("Edit", u"Change level", None))
        self.stop_button.setText(QCoreApplication.translate("Edit", u"Stop", None))
        self.delete_button.setText(QCoreApplication.translate("Edit", u"Delete", None))
        self.cancel_button.setText(QCoreApplication.translate("Edit", u"Cancel", None))
        self.assemble_button.setText(QCoreApplication.translate("Edit", u"Assemble existing RAIDs", None))
    # retranslateUi

