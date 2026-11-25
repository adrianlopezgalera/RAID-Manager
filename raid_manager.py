import sys

from PySide6.QtWidgets import QApplication, QMainWindow

from about import About
from edit import Edit
from events_manager import EventsManager
from info import Info
from new_raid import NewRaid
from UI.ui_main import Ui_RAID_Manager
from options import Options
from system_tray import Tray


class RaidManager(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_RAID_Manager()
        self.ui.setupUi(self)

        # The program shows its main window to let the user know that the program is active.
        # This allows the user to understand that the notifications, in the event that some dependencies are missing, come from the program itself.

        self.show()

        # Center window before starting:

        EventsManager.window_to_center(self)

        # If 'mdadm' and the policy file are installed on the system, the program starts:

        if EventsManager.is_installed('mdadm') and EventsManager.has_policy():

            # Declares and initializes objects for windows:

            new_raid = NewRaid()
            edit = Edit()
            info = Info()
            about = About()
            options = Options()

            # Declares the system tray and activates it if enabled:

            tray = Tray()
            options.evaluate_setting(tray)

            # Connecting buttons to events:

            self.ui.button1_new.clicked.connect(lambda: EventsManager.new_window(new_raid))
            self.ui.button2_edit.clicked.connect(lambda: EventsManager.new_window(edit))
            self.ui.button3_info.clicked.connect(lambda: EventsManager.new_window(info))
            self.ui.actionAbout.triggered.connect(lambda: EventsManager.new_window(about))
            self.ui.actionOptions.triggered.connect(lambda: EventsManager.new_window(options))
            self.ui.actionExit.triggered.connect(lambda: EventsManager.close())

            # Alternative way to create instances of the classes without declaring objects:

            #self.ui.button1_new.clicked.connect(lambda: EventsManager.create_object(NewRaid().show()))
            #self.ui.button2_edit.clicked.connect(lambda: EventsManager.create_object(Edit().show()))
            #self.ui.button3_info.clicked.connect(lambda: EventsManager.create_object(Info().show()))
            #self.ui.button3_info.clicked.connect(lambda: EventsManager.create_object(About().show()))


        # Checks if the policy file ins installed. If it is, the program installs 'mdadm'.

        elif EventsManager.has_policy():
            EventsManager.install_program('mdadm')

        # Checks if 'mdadm' is installed. If it is, the program installs the policy file.

        elif EventsManager.is_installed('mdadm'):
            EventsManager.install_policy()

        # If none is installed, the program installs both:

        else:
            EventsManager.install_program('mdadm')
            EventsManager.install_policy()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = RaidManager()
    sys.exit(app.exec())