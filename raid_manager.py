# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from events_manager import Events_Manager
from new_raid import New_raid

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_main import Ui_RAID_Manager

class RAID_Manager(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_RAID_Manager()
        self.ui.setupUi(self)

        # Connecting buttons to events:

        self.ui.button1_new.clicked.connect(lambda: New_raid().show(self))
        self.ui.button4_info.clicked.connect(lambda: Events_Manager.read_output("--help"))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = RAID_Manager()
    main_window.show()
    sys.exit(app.exec())

