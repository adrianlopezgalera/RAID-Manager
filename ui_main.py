# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLayout, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_RAID_Manager(object):
    def setupUi(self, RAID_Manager):
        if not RAID_Manager.objectName():
            RAID_Manager.setObjectName(u"RAID_Manager")
        RAID_Manager.resize(720, 480)
        RAID_Manager.setMinimumSize(QSize(720, 480))
        font = QFont()
        font.setKerning(False)
        RAID_Manager.setFont(font)
        RAID_Manager.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        RAID_Manager.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        RAID_Manager.setDocumentMode(False)
        self.centralwidget = QWidget(RAID_Manager)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalFrame = QFrame(self.centralwidget)
        self.verticalFrame.setObjectName(u"verticalFrame")
        self.verticalFrame.setGeometry(QRect(0, 90, 721, 211))
        self.verticalLayout_2 = QVBoxLayout(self.verticalFrame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.button1_new = QPushButton(self.verticalFrame)
        self.button1_new.setObjectName(u"button1_new")
        font1 = QFont()
        font1.setBold(False)
        font1.setKerning(True)
        self.button1_new.setFont(font1)
        self.button1_new.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ListAdd))
        self.button1_new.setIcon(icon)

        self.verticalLayout_2.addWidget(self.button1_new)

        self.button2_assemble = QPushButton(self.verticalFrame)
        self.button2_assemble.setObjectName(u"button2_assemble")
        self.button2_assemble.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.MediaPlaylistRepeat))
        self.button2_assemble.setIcon(icon1)

        self.verticalLayout_2.addWidget(self.button2_assemble)

        self.button3_edit = QPushButton(self.verticalFrame)
        self.button3_edit.setObjectName(u"button3_edit")
        self.button3_edit.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon2 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DriveHarddisk))
        self.button3_edit.setIcon(icon2)

        self.verticalLayout_2.addWidget(self.button3_edit)

        self.button4_info = QPushButton(self.verticalFrame)
        self.button4_info.setObjectName(u"button4_info")
        self.button4_info.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon3 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.HelpAbout))
        self.button4_info.setIcon(icon3)

        self.verticalLayout_2.addWidget(self.button4_info)

        RAID_Manager.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(RAID_Manager)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 720, 20))
        self.menuFiler = QMenu(self.menubar)
        self.menuFiler.setObjectName(u"menuFiler")
        self.menuSettings = QMenu(self.menubar)
        self.menuSettings.setObjectName(u"menuSettings")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        RAID_Manager.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(RAID_Manager)
        self.statusbar.setObjectName(u"statusbar")
        RAID_Manager.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFiler.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(RAID_Manager)

        QMetaObject.connectSlotsByName(RAID_Manager)
    # setupUi

    def retranslateUi(self, RAID_Manager):
        RAID_Manager.setWindowTitle(QCoreApplication.translate("RAID Manager", u"RAID_Manager", None))
#if QT_CONFIG(tooltip)
        self.button1_new.setToolTip(QCoreApplication.translate("RAID Manager", u"It creates a new RAID with selected devices", None))
#endif // QT_CONFIG(tooltip)
        self.button1_new.setText(QCoreApplication.translate("RAID Manager", u"Create a new RAID...", None))
        self.button2_assemble.setText(QCoreApplication.translate("RAID Manager", u"Assemble an existing RAID...", None))
        self.button3_edit.setText(QCoreApplication.translate("RAID Manager", u"Edit an existing RAID...", None))
        self.button4_info.setText(QCoreApplication.translate("RAID Manager", u"Get info about an existing raid", None))
        self.menuFiler.setTitle(QCoreApplication.translate("RAID Manager", u"File", None))
        self.menuSettings.setTitle(QCoreApplication.translate("RAID Manager", u"Settings", None))
        self.menuHelp.setTitle(QCoreApplication.translate("RAID Manager", u"Help", None))
    # retranslateUi

