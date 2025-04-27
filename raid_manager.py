import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from edit import Edit
from events_manager import EventsManager
from info import Info
from new_raid import NewRaid
from UI.ui_main import Ui_RAID_Manager

class RaidManager(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_RAID_Manager()
        self.ui.setupUi(self)

        # Center window:

        EventsManager.window_to_center(self)

        if EventsManager.is_installed('mdadm') and EventsManager.has_policy():

            # Declare and initialize objects for windows:

            new_raid = NewRaid()
            edit = Edit()
            info = Info()

            # Connecting buttons to events:

            self.ui.button1_new.clicked.connect(lambda: EventsManager.new_window(new_raid))
            self.ui.button2_edit.clicked.connect(lambda: EventsManager.new_window(edit))
            self.ui.button3_info.clicked.connect(lambda: EventsManager.new_window(info))

            #self.ui.button1_new.clicked.connect(lambda: EventsManager.create_object(NewRaid().show()))
            #self.ui.button2_edit.clicked.connect(lambda: EventsManager.create_object(Edit().show()))
            #self.ui.button3_info.clicked.connect(lambda: EventsManager.create_object(Info().show()))

        elif EventsManager.has_policy():
            EventsManager.install_program('mdadm')

        elif EventsManager.is_installed('mdadm'):
            EventsManager.install_policy()
        else:
            EventsManager.install_program('mdadm')
            EventsManager.install_policy()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = RaidManager()
    main_window.show()
    sys.exit(app.exec())