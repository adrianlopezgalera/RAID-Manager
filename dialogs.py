import subprocess

from PySide6.QtWidgets import QWidget
from UI.ui_dialog import Ui_Dialog

class Dialogs(QWidget):

    def __init__(self):
        super().__init__(parent=None)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # Connecting buttons to events:
        self.ui.cancel_button.clicked.connect(self.close)
        #self.ui.cancel_button.clicked.connect(lambda: self.close)

"""
    def apply_change(self):
        if self.ui.label.selectedText().__contains__("Enter new RAID Name:"):
            selected_raid = self.ui.current_raid.text()
            new_name = self.ui.text.selectedText()
            EventsManager.read_output('pkexec mdadm --manage ' + selected_raid + '--name=' + new_name + ' && update-initramfs', shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
"""