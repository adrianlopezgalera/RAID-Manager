# This Python file uses the following encoding: utf-8
import os
import subprocess
import sys
from PySide6.QtWidgets import QApplication, QMainWindow

from edit import Edit
from events_manager import EventsManager
from info import Info
from new_raid import NewRaid

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from UI.ui_main import Ui_RAID_Manager

class RaidManager(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_RAID_Manager()
        self.ui.setupUi(self)

      #  new_raid = NewRaid()
     #   edit = Edit()
      #  info = Info()

        # Connecting buttons to events:
        self.ui.button1_new.clicked.connect(lambda: EventsManager.create_object(NewRaid().show()))

       # self.ui.button1_new.clicked.connect(lambda: EventsManager.new_window(new_raid))
        #self.ui.button2_edit.clicked.connect(lambda: EventsManager.new_window(edit))
        #self.ui.button3_info.clicked.connect(lambda: EventsManager.new_window(info))
        self.ui.button2_edit.clicked.connect(lambda: EventsManager.create_object(Edit().show()))

        self.ui.button3_info.clicked.connect(lambda: EventsManager.create_object(Info().show()))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = RaidManager()
    main_window.show()
    sys.exit(app.exec())