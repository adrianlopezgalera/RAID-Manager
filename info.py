from PySide6.QtWidgets import QWidget
from UI.ui_info import Ui_Info
from events_manager import EventsManager


class Info(QWidget):

    selected_raid = ""

    def __init__(self):
        super().__init__(parent=None)
        self.ui = Ui_Info()
        self.ui.setupUi(self)

        # Executing functions:
        EventsManager.fill_raid_list(self)
        self.ui.select_raid.currentIndexChanged.connect(lambda: self.print_raid_details())

        # Load the available RAIDs selector:
        EventsManager.fill_raid_list(self)

        # By default, it loads the details of the first RAID:
        self.print_raid_details()

        # Connecting buttons to events:
        self.ui.OK_button.clicked.connect(self.close)
        self.ui.export_button.clicked.connect(lambda: EventsManager.export_selected_raid_info(self))

    def set_selected_raid(self):
        self.selected_raid = self.ui.select_raid.currentText()

    # Looks up and extracts the strings to fill the form:

    def print_raid_details(self):

        # Reads the selected RAID:

        self.set_selected_raid()

        # Extract info about the selected RAID:

        raid_info = EventsManager.get_selected_raid_info(self.selected_raid).splitlines()

        self.ui.raid_path.setText(self.selected_raid)

        # Variable to save a string with the drives of the selected RAID:

        drives = ""

        # Fills the fields by evaluating the content of each line:

        for line in raid_info:

            if line.__contains__('Name'):
                self.ui.raid_name.setText(line[21:])

            if line.__contains__('Raid Level'):

                if line.__contains__('raid0'):
                    self.ui.raid_level.setText('Raid 0')
                if line.__contains__('raid1'):
                    self.ui.raid_level.setText('Raid 1')
                if line.__contains__('raid5'):
                    self.ui.raid_level.setText('Raid 5')
                if line.__contains__('raid6'):
                    self.ui.raid_level.setText('Raid 6')

            if line.__contains__('Array Size'):
                self.ui.raid_size.setText(line[21:])
            if line.__contains__('State : '):
                state = ""
                if line.__contains__('active'):
                    state += "Active "
                if line.__contains__('clean'):
                    state += "Clean "
                if line.__contains__('FAILED'):
                    state += "Failed "
                if line.__contains__('resyncing'):
                    state += "Resyncing "
                if line.__contains__('degraded'):
                    state += "Degraded "
                if line.__contains__('recovering'):
                    state += "Recovering "

                if state.__contains__("Failed"):
                    self.ui.working_devices.setText("0")
                    self.ui.raid_name.setText("None")

                self.ui.raid_state.setText(state)

            if line.__contains__('/dev/s'):
                drives += line[line.find('/'):] + ' '
                self.ui.raid_devices.setText(drives)
            if line.__contains__('Active Devices'):
                self.ui.active_devices.setText(line[21:])
            if line.__contains__('Working Devices'):
                self.ui.working_devices.setText(line[21:])
            if line.__contains__('Failed Devices'):
                self.ui.failed_devices.setText(line[21:])
            if line.__contains__('Spare Devices'):
                self.ui.spare_devices.setText(line[21:])
