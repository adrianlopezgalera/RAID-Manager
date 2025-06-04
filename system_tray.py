import sys

from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QSystemTrayIcon, QMenu

class Tray:

    def activate(self):
        tray_icon = QSystemTrayIcon()
        tray_icon.setIcon(QIcon('UI/hard-disk.png'))
        # tray_icon.showMessage("fwefw", "efwefwe", tray_icon.icon())

        menu = QMenu()
        action = menu.addAction("Show Message")
        action.triggered.connect(lambda: tray_icon.showMessage("Título", "Mensaje", QSystemTrayIcon.MessageIcon.NoIcon))
        tray_icon.setContextMenu(menu)
        tray_icon.show()


    def destroy(self):
        del self

    def show_notification(title, message):
        pass
