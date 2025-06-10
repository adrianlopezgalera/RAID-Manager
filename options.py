from PySide6.QtWidgets import QWidget
from UI.ui_options import Ui_Options
from events_manager import EventsManager
from system_tray import Tray


class Options(QWidget):

    def __init__(self):
        super().__init__(parent=None)
        self.ui = Ui_Options()
        self.ui.setupUi(self)

        # Executing functions:
        saved_options = EventsManager.read_saved_options()

        # Connecting buttons to events:
        self.ui.save_button.clicked.connect(lambda: self.save_options())
        self.ui.cancel_button.clicked.connect(self.close)

        # Updating default values:
        self.load_options(saved_options)


    def save_options(self):

        text =  (("system_tray : " + self.get_system_tray())
                 + "")

        EventsManager.save_txt_file(".config", text)

        # System tray:

        tray = Tray()

        self.evaluate_setting(tray)

        self.close()

    # Sets the current values in the selector according to the saved settings:

    def load_options(self, saved_options):

        if saved_options != "":

            for line in saved_options.splitlines():

                if line.__contains__("system_tray"):
                    if line.__contains__("Enabled"):
                        self.ui.system_tray_selector.setCurrentIndex(0)
                    else:
                        self.ui.system_tray_selector.setCurrentIndex(1)

    # Evaluates the saved settings:

    def evaluate_setting(self, tray):

        if self.ui.system_tray_selector.currentText() == "Enabled":
            tray.activate()
        else:
            tray.destroy()

    # Returns the current value of the system tray selector:

    def get_system_tray(self):
        return self.ui.system_tray_selector.currentText()