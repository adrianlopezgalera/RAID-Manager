from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QSystemTrayIcon, QMenu

class Tray:

    # Enables the system tray:

    def activate(self):
        tray_icon = QSystemTrayIcon()
        tray_icon.setIcon(QIcon('UI/hard-disk.png'))

        menu = QMenu()
        action = menu.addAction("Status")
        action.triggered.connect(lambda: tray_icon.showMessage("Information", "All RAIDs are working correctly.", QSystemTrayIcon.MessageIcon.NoIcon))
        tray_icon.setContextMenu(menu)
        tray_icon.show()


    def destroy(self):
        del self

    def show_notification(title, message):
        pass
