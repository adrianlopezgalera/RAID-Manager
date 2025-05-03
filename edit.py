import subprocess

from PySide6.QtWidgets import QWidget, QMessageBox
from UI.ui_edit import Ui_Edit
from dialogs import Dialogs
from events_manager import EventsManager
from notifications import Notifications


class Edit(QWidget):

    selected_raid = ""

    def __init__(self):
        super().__init__(parent=None)
        self.ui = Ui_Edit()
        self.ui.setupUi(self)

        # Executing functions:
        EventsManager.fill_raid_list(window=self)
        self.ui.select_raid.currentIndexChanged.connect(lambda: self.print_selected_raid())

        # Default values:
        self.set_selected_raid()
        self.ui.selected_raid.setText(self.ui.select_raid.currentText())

        # Connecting buttons to events:
        self.ui.cancel_button.clicked.connect(self.close)
        #self.ui.apply_button.clicked.connect(lambda: self.print_selected_raid())

        self.ui.change_level_button.clicked.connect(lambda: EventsManager.change_level_dialog(selected_raid=self.selected_raid))
        self.ui.add_drive_button.clicked.connect(lambda: EventsManager.add_drive_dialog(selected_raid=self.selected_raid))
        self.ui.remove_drive_button.clicked.connect(lambda: EventsManager.remove_drive_dialog(selected_raid=self.selected_raid))
        self.ui.assemble_button.clicked.connect(lambda: EventsManager.assemble_dialog(self))
        self.ui.stop_button.clicked.connect(lambda: EventsManager.stop_dialog(self))
        self.ui.delete_button.clicked.connect(lambda: EventsManager.delete_dialog(self))


    def get_selected_raid(self):
        return self.selected_raid

    def set_selected_raid(self):
        self.selected_raid = self.ui.select_raid.currentText()

    def print_selected_raid(self):
        self.set_selected_raid()
        self.ui.selected_raid.setText(self.selected_raid)
