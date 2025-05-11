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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QFrame,
    QHBoxLayout, QLabel, QLayout, QPushButton,
    QSizePolicy, QTextBrowser, QWidget)

class Ui_Edit(object):
    def setupUi(self, Edit):
        if not Edit.objectName():
            Edit.setObjectName(u"Edit")
        Edit.setEnabled(True)
        Edit.resize(720, 480)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Edit.sizePolicy().hasHeightForWidth())
        Edit.setSizePolicy(sizePolicy)
        Edit.setMinimumSize(QSize(720, 480))
        Edit.setMaximumSize(QSize(720, 480))
        Edit.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        Edit.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.formLayoutWidget = QWidget(Edit)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(40, 40, 621, 111))
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

        self.selected_raid_label = QLabel(self.formLayoutWidget)
        self.selected_raid_label.setObjectName(u"selected_raid_label")

        self.raid_selector.setWidget(1, QFormLayout.LabelRole, self.selected_raid_label)

        self.selected_raid = QTextBrowser(self.formLayoutWidget)
        self.selected_raid.setObjectName(u"selected_raid")
        sizePolicy.setHeightForWidth(self.selected_raid.sizePolicy().hasHeightForWidth())
        self.selected_raid.setSizePolicy(sizePolicy)
        self.selected_raid.setMaximumSize(QSize(540, 25))
        self.selected_raid.setSizeIncrement(QSize(0, 0))
        self.selected_raid.setBaseSize(QSize(300, 0))
        font = QFont()
        font.setPointSize(10)
        self.selected_raid.setFont(font)
        self.selected_raid.viewport().setProperty(u"cursor", QCursor(Qt.CursorShape.IBeamCursor))
        self.selected_raid.setFrameShape(QFrame.Shape.StyledPanel)
        self.selected_raid.setFrameShadow(QFrame.Shadow.Raised)

        self.raid_selector.setWidget(1, QFormLayout.FieldRole, self.selected_raid)

        self.row_1 = QWidget(Edit)
        self.row_1.setObjectName(u"row_1")
        self.row_1.setGeometry(QRect(30, 220, 628, 43))
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
        self.row_2.setGeometry(QRect(30, 270, 628, 43))
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
        self.assemble_button.setGeometry(QRect(260, 350, 171, 31))

        self.retranslateUi(Edit)

        QMetaObject.connectSlotsByName(Edit)
    # setupUi

    def retranslateUi(self, Edit):
        Edit.setWindowTitle(QCoreApplication.translate("Edit", u"Edit a RAID", None))
        self.select_raid_label.setText(QCoreApplication.translate("Edit", u"Select RAID:", None))
        self.selected_raid_label.setText(QCoreApplication.translate("Edit", u"Selected RAID:", None))
        self.selected_raid.setHtml(QCoreApplication.translate("Edit", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Ubuntu'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.selected_raid.setPlaceholderText(QCoreApplication.translate("Edit", u"No RAID available", None))
        self.change_name_button.setText(QCoreApplication.translate("Edit", u"Change name", None))
        self.add_drive_button.setText(QCoreApplication.translate("Edit", u"Add drive", None))
        self.remove_drive_button.setText(QCoreApplication.translate("Edit", u"Remove drive", None))
        self.change_level_button.setText(QCoreApplication.translate("Edit", u"Change level", None))
        self.stop_button.setText(QCoreApplication.translate("Edit", u"Stop", None))
        self.delete_button.setText(QCoreApplication.translate("Edit", u"Delete", None))
        self.cancel_button.setText(QCoreApplication.translate("Edit", u"Cancel", None))
        self.assemble_button.setText(QCoreApplication.translate("Edit", u"Assemble existing RAIDs", None))
    # retranslateUi

