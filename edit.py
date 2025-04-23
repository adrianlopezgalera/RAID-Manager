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
        self.print_raid_list()

        # Connecting buttons to events:

        self.ui.cancel_button.clicked.connect(lambda: self.close)
        self.ui.apply_button.clicked.connect(lambda: self.set_selected_raid())


        self.ui.change_name_button.clicked.connect(lambda: EventsManager.change_name_dialog(selected_raid=self.selected_raid))
        #self.ui.change_name_button.clicked.connect(lambda: EventsManager.new_window(dialog))
        #self.ui.apply_button.clicked.connect(lambda:)


    def print_raid_list(self):

        arrays = EventsManager.fill_raid_list()

        for array in arrays:

            path = array[array.find('/'): array.find(' metadata')]
            self.ui.select_raid.addItem(path)

    def set_selected_raid(self):
        selected_raid = self.ui.select_raid.currentText()
        self.selected_raid = selected_raid
        self.ui.selected_raid.setText(self.selected_raid)