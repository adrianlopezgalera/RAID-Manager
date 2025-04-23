import subprocess

from PySide6.QtWidgets import QWidget, QMessageBox
from UI.ui_dialog import Ui_Dialog

class Dialogs(QWidget):

    def __init__(self):
        super().__init__(parent=None)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # Connecting buttons to events:
        self.ui.cancel_button.clicked.connect(lambda: self.close)
        #self.ui.cancel_button.clicked.connect(lambda: self.close)