import subprocess

from PySide6.QtWidgets import QWidget, QMessageBox
from UI.ui_info import Ui_Info
from events_manager import EventsManager


class Info(QWidget):

    raid = ""

    def __init__(self):
        super().__init__(parent=None)
        self.ui = Ui_Info()
        self.ui.setupUi(self)

        # Executing functions:
        self.fill_raid_list()

        # Connecting buttons to events:
        self.ui.OK_button.clicked.connect(self.close)
        self.ui.apply_button.clicked.connect(lambda: self.fill_raid_details())


    def fill_raid_list(self):
        result = EventsManager.run_command(['pkexec', 'mdadm', '--detail' , '--scan'], capture_output=True, text=True)

        output = result.stdout

        arrays = output.splitlines()

        print(arrays)
        for array in arrays:

            path = array[array.find('/'): array.find(' metadata')]
            self.ui.select_raid.addItem(path)

    def fill_raid_details(self):
        self.raid = self.ui.select_raid.currentText()

        print(self.raid)

        result = EventsManager.run_command(['pkexec', 'mdadm', '--detail', self.raid], capture_output=True, text=True)

        self.ui.raid_path.setText(self.raid)

        output = result.stdout

        info = output.splitlines()

        print(info)

        for line in info:
            if line.__contains__('Raid Level'):

                if line[21:].__eq__('raid0'):
                    self.ui.raid_level.setText('Raid 0')
                if line[21:].__eq__('raid1'):
                    self.ui.raid_level.setText('Raid 1')
                if line[21:].__eq__('raid5'):
                    self.ui.raid_level.setText('Raid 5')
                if line[21:].__eq__('raid6'):
                    self.ui.raid_level.setText('Raid 6')

            if line.__contains__('Array Size'):
                self.ui.raid_size.setText(line[21:])
            if line.__contains__('State : '):
                self.ui.raid_state.setText(line[21:])
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