# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QWidget

from events_manager import Events_Manager

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_new_raid import Ui_New_Raid



class New_raid(QWidget):
    def __init__(self):
        super().__init__(self.parent)
        self.ui = New_raid()
        self.ui.setupUi(self)

        # Connecting buttons to events:
if __name__ == "__main__":
    app = QWidget(sys.argv)
    main_window = New_raid()
    main_window.show()
    sys.exit(app.exec())