# This Python file uses the following encoding: utf-8
import os
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from events_manager import EventsManager
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

        # Connecting buttons to events:

        raid = NewRaid()
        self.ui.button1_new.clicked.connect(lambda: EventsManager.new_window(raid))
        self.ui.button4_info.clicked.connect(lambda: EventsManager.read_output("--help"))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = RaidManager()
    main_window.show()
    sys.exit(app.exec())