# This Python file uses the following encoding: utf-8
import sys
from types import new_class

from PySide6.QtWidgets import QWidget, QFileDialog

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py

from UI.ui_new_raid import Ui_New_Raid
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

        # Connecting buttons to events:

        self.ui.new_raid_cancel.clicked.connect(self.close)
        self.ui.select_devices.clicked.connect(lambda: self.set_selected_devices())
        self.ui.remove_devices.clicked.connect(lambda: self.clear_selected_devices())
        self.ui.new_raid_create.clicked.connect(lambda : self.create_new_raid())

    def set_selected_devices(self):
        self.selected_device = self.select_devices()
        self.selected_devices = self.selected_devices + '\n' + self.selected_device
        self.ui.devices_path.setText(self.selected_devices)

    def clear_selected_devices(self):
        self.selected_devices = ""
        self.ui.devices_path.setText(self.selected_devices)

    def create_new_raid(self):
        self.raid_name = self.ui.raid_name.text()
        self.raid_level = self.ui.raid_level.currentText()

        creating = EventsManager()
        creating.read_output('--create --verbose ' + '/dev/'+self.raid_name + ' ' + '--level=' + self.raid_level + ' ' + '--raid-devices=' + str(self.selected_devices.count('\n')) + ' ' + self.selected_devices.replace("\n", " "))




    @staticmethod
    def select_devices():
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.FileMode.Directory)
        dialog.setOption(QFileDialog.Option.ShowDirsOnly, True)

        return QFileDialog.getExistingDirectory(dialog, "Select a drive")
