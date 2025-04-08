# This Python file uses the following encoding: utf-8
import os
import stringprep
import subprocess
import sys
from types import new_class

import psutil
from PySide6.QtWidgets import QWidget, QFileDialog, QLabel, QComboBox

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py

from UI.ui_new_raid import Ui_New_Raid
from dialogs import Dialogs
from events_manager import EventsManager

class NewRaid(QWidget):

    raid_name = ""
    raid_level = ""
    selected_device = ""
    selected_devices = ""


    def __init__(self):
        super().__init__(parent=None)
        self.ui = Ui_New_Raid()
        self.ui.setupUi(self)

        self.populate_device_list()


        # Connecting buttons to events:

        self.ui.new_raid_cancel.clicked.connect(self.close)
        self.ui.add_device.clicked.connect(lambda: self.set_selected_devices())
        self.ui.remove_devices.clicked.connect(lambda: self.clear_selected_devices())
        self.ui.new_raid_create.clicked.connect(lambda : self.create_new_raid())

    def set_selected_devices(self):

        self.selected_device = self.select_devices()

        if (self.selected_device == "") or (self.selected_devices.__contains__(self.selected_device)):
            print('')
        else:
            self.selected_devices = self.selected_devices + '\n' + self.selected_device
            self.ui.devices_path.setText(self.selected_devices)

    def clear_selected_devices(self):
        self.selected_devices = ""
        self.ui.devices_path.setText(self.selected_devices)

    def create_new_raid(self):

        self.raid_name = self.ui.raid_name.text()
        self.raid_level = self.ui.raid_level.currentText()

        # EventsManager.read_output('pkexec mdadm --create --verbose ' + '/dev/'+self.raid_name + ' ' + '--level=' + self.raid_level + ' ' + '--raid-devices=' + str(self.selected_devices.count('\n')) + ' ' + self.selected_devices.replace("\n", " "))
        response = EventsManager.run_command(
            'pkexec umount' + self.selected_devices.replace("\n", " ") + '&&' +
            'pkexec mdadm --create --verbose --force ' + '/dev/'+self.raid_name + ' ' + '--level=' + self.raid_level + ' ' + '--raid-devices=' + str(self.selected_devices.count('\n')) + ' ' + self.selected_devices.replace("\n", " "), shell=True, check=True, stdout=subprocess.PIPE, universal_newlines=True)

        dialog = Dialogs()
        dialog.new_dialog("hola", response.stdout, QMessageBox.Icon.Information,
                               [QMessageBox.StandardButton.Ok, QMessageBox.StandardButton.Cancel])




    def select_devices(self):
        return '/dev/' + self.ui.devices.currentText()[0: self.ui.devices.currentText().find('-')]


    def populate_device_list(self):

        result = EventsManager.run_command(['lsblk', '-o', 'NAME,SIZE,FSTYPE,MOUNTPOINT', '-l', '--noheadings'], capture_output=True, text=True)

        output = result.stdout

        devices = output.splitlines()
        for device in devices:
            device_info = device.split()
            if len(device_info) >= 4:
                device_name = device_info[0]
                mount_point = device_info[3]
                self.ui.devices.addItem(f"{device_name} - {mount_point}")