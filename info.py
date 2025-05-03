import subprocess

from PySide6.QtWidgets import QWidget, QMessageBox
from UI.ui_info import Ui_Info
from events_manager import EventsManager


class Info(QWidget):

    selected_raid = ""

    def __init__(self):
        super().__init__(parent=None)
        self.ui = Ui_Info()
        self.ui.setupUi(self)

        # Executing functions:
        EventsManager.fill_raid_list(window=self)
        self.ui.select_raid.currentIndexChanged.connect(lambda: self.print_raid_details())

        # Default values:
        self.print_raid_details()

        # Connecting buttons to events:
        self.ui.OK_button.clicked.connect(self.close)
        #self.ui.apply_button.clicked.connect(lambda: self.print_raid_details())

    def set_selected_raid(self):
        self.selected_raid = self.ui.select_raid.currentText()

    def print_raid_details(self):

        # Taking selected RAID:

        self.set_selected_raid()

        # Filling fields:

        arrays = EventsManager.run_command(['sudo', 'mdadm', '--detail', self.selected_raid], capture_output=True, text=True).stdout.splitlines()

        self.ui.raid_path.setText(self.selected_raid)

        for line in arrays:

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
                if line.__contains__('resyncing'):
                    state += "Resyncing "
                if line.__contains__('degraded'):
                    state += "Degraded "
                if line.__contains__('recovering'):
                    state += "Recovering "

                self.ui.raid_state.setText(state)

            if line.__contains__('/'):
                device = ""
                device += line[line.find('/'):] + ' '
                self.ui.raid_devices.setText(device)
            if line.__contains__('Active Devices'):
                self.ui.active_devices.setText(line[21:])
            if line.__contains__('Working Devices'):
                self.ui.working_devices.setText(line[21:])
            if line.__contains__('Failed Devices'):
                self.ui.failed_devices.setText(line[21:])
            if line.__contains__('Spare Devices'):
                self.ui.spare_devices.setText(line[21:])