import subprocess

from PySide6.QtWidgets import QWidget, QMessageBox
from UI.ui_info import Ui_Info
from events_manager import EventsManager


class Info(QWidget):

    def __init__(self):
        super().__init__(parent=None)
        self.ui = Ui_Info()
        self.ui.setupUi(self)

        # Executing functions:
        self.print_raid_list()

        # Connecting buttons to events:
        self.ui.OK_button.clicked.connect(self.close)
        self.ui.apply_button.clicked.connect(lambda: self.print_raid_details())


    def print_raid_list(self):

        arrays = EventsManager.fill_raid_list()

        for array in arrays:
            path = array[array.find('/'): array.find(' metadata')]
            self.ui.select_raid.addItem(path)


    def print_raid_details(self):

        # Taking selected RAID:

        raid = self.ui.select_raid.currentText()

        # Filling fields:

        arrays = EventsManager.run_command(['pkexec', 'mdadm', '--detail', raid], capture_output=True, text=True).stdout.splitlines()

        self.ui.raid_path.setText(raid)

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
                    state += " Active "
                if line.__contains__('clean'):
                    state += " Clean "
                if line.__contains__('resyncing'):
                    state += " Resyncing "
                if line.__contains__('degraded'):
                    state += " Degraded "
                if line.__contains__('recovering'):
                    state += " Recovering "

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