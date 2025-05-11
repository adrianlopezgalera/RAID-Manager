from PyQt6.QtCore import QUrl
from PyQt6.QtGui import QDesktopServices
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtWidgets import QWidget
from UI.ui_about import Ui_About


class About(QWidget):

    def __init__(self):
        super().__init__(parent=None)
        self.ui = Ui_About()
        self.ui.setupUi(self)

        # Pictures:
        self.ui.icon.setPixmap(QPixmap('UI/hard-disk.png'))
        self.ui.github.setIcon(QIcon('UI/github.png'))

        # Connecting buttons to events:
        self.ui.OK_button.clicked.connect(self.close)
        self.ui.github.clicked.connect(lambda: QDesktopServices.openUrl(QUrl("https://github.com/adrianlopezgalera/RAID-Manager")))
