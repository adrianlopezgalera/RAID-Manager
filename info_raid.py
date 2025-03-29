# This Python file uses the following encoding: utf-8
import sys
from types import new_class

from PySide6.QtWidgets import QWidget

from UI.ui_info import Ui_Dialog
# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py

from events_manager import EventsManager


class InfoRAID(QWidget):

    def __init__(self):
        super().__init__(parent=None)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # Connecting buttons to events:

