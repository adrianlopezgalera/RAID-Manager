# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'about.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QPushButton,
    QSizePolicy, QTextBrowser, QWidget)

class Ui_About(object):
    def setupUi(self, About):
        if not About.objectName():
            About.setObjectName(u"About")
        About.resize(720, 480)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(About.sizePolicy().hasHeightForWidth())
        About.setSizePolicy(sizePolicy)
        About.setMinimumSize(QSize(720, 480))
        About.setMaximumSize(QSize(720, 480))
        About.setContextMenuPolicy(Qt.ContextMenuPolicy.ActionsContextMenu)
        About.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.OK_button = QPushButton(About)
        self.OK_button.setObjectName(u"OK_button")
        self.OK_button.setGeometry(QRect(590, 440, 80, 23))
        font = QFont()
        font.setBold(False)
        self.OK_button.setFont(font)
        self.OK_button.setContextMenuPolicy(Qt.ContextMenuPolicy.ActionsContextMenu)
        self.icon = QLabel(About)
        self.icon.setObjectName(u"icon")
        self.icon.setGeometry(QRect(320, 70, 61, 71))
        self.icon.setText(u"")
        self.icon.setTextFormat(Qt.TextFormat.PlainText)
        self.icon.setPixmap(QPixmap(u"hard-disk.png"))
        self.icon.setScaledContents(False)
        self.icon.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)
        self.title = QLabel(About)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(270, 150, 171, 31))
        font1 = QFont()
        font1.setPointSize(16)
        font1.setBold(True)
        font1.setKerning(False)
        self.title.setFont(font1)
        self.title.setCursor(QCursor(Qt.CursorShape.IBeamCursor))
        self.title.setWordWrap(True)
        self.title.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)
        self.textBrowser = QTextBrowser(About)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(90, 210, 541, 131))
        self.textBrowser.setFrameShape(QFrame.Shape.NoFrame)
        self.textBrowser.setOpenExternalLinks(True)
        self.github = QPushButton(About)
        self.github.setObjectName(u"github")
        self.github.setGeometry(QRect(290, 360, 121, 41))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        self.github.setFont(font2)
        self.github.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u"github.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.github.setIcon(icon1)
        self.github.setFlat(True)

        self.retranslateUi(About)

        QMetaObject.connectSlotsByName(About)
    # setupUi

    def retranslateUi(self, About):
        About.setWindowTitle(QCoreApplication.translate("About", u"About", None))
        self.OK_button.setText(QCoreApplication.translate("About", u"OK", None))
        self.title.setText(QCoreApplication.translate("About", u"RAID MANAGER", None))
        self.textBrowser.setHtml(QCoreApplication.translate("About", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Ubuntu'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">RAID Manager is a free software to manage RAIDs by using 'mdadm'.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-r"
                        "ight:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700;\">Author:</span><span style=\" font-size:12pt;\"> Adri\u00e1n L\u00f3pez Galera</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; font-weight:700;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700;\">License:</span><span style=\" font-size:12pt;\"> GPL3</span></p></body></html>", None))
        self.github.setText(QCoreApplication.translate("About", u"Github", None))
    # retranslateUi

