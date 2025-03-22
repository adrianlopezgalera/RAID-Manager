# This Python file uses the following encoding: utf-8
import sys
from types import new_class

from PyQt6.QtWidgets import QFileDialog
from PySide6.QtWidgets import QWidget

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py

from UI.ui_new_raid import Ui_New_Raid
from events_manager import EventsManager


class New_raid(QWidget):

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        return instance

    def __init__(self):
        super().__init__(parent=None)
        self.ui = Ui_New_Raid()
        self.ui.setupUi(self)

        # Connecting buttons to events:
        self.ui.pushButton_cancel.clicked.connect(self.close)





        devices = self.ui.toolButton.clicked.connect(lambda device: print(EventsManager.select_devices()))




