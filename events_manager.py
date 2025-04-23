import subprocess
from operator import truediv

from PySide6.QtWidgets import QMessageBox

from dialogs import Dialogs
from notifications import Notifications


class EventsManager:

    @staticmethod
    def run_command(*args, **kwargs):
        try:
            return subprocess.run(*args, **kwargs)
        except subprocess.CalledProcessError as e:
            print(f"Error executing the command: {e}")
    @staticmethod
    def read_output(*args, **kwargs):
        try:
            return subprocess.Popen(*args, **kwargs)
        except subprocess.CalledProcessError as e:
            print(f"Error executing the command: {e}")

    @staticmethod
    def new_window(self):
        self.show()

    @staticmethod
    def create_object(class_name):
        return type(class_name)

    @staticmethod
    def action(**kwargs):
        subprocess.run('mdadm ' + kwargs)

    @staticmethod
    def user_input_checking(dialog, process):

        if dialog == QMessageBox.StandardButton.Ok:
            process.stdin.write('y')
            process.stdin.flush()
        elif dialog == QMessageBox.StandardButton.Cancel:
            process.stdin.write('n')
            process.stdin.flush()

    @staticmethod
    def fill_raid_list():
        return EventsManager.run_command(['pkexec', 'mdadm', '--detail' , '--scan'], capture_output=True, text=True).stdout.splitlines()

    @staticmethod
    def check_if_selected_raid(selected_raid):
        if selected_raid != "":
            return True
        else:
            dialog = Notifications()
            dialog.new_dialog(title="Error", text="You must select a RAID first", icon="critical", buttons=["ok"])
            return False

    @staticmethod
    def change_name_dialog(selected_raid):
        if EventsManager.check_if_selected_raid(selected_raid):
            dialog = Dialogs()
            dialog.ui.current_raid.setText(selected_raid)
            dialog.setWindowTitle("Change RAID Name")
            dialog.ui.label.setText("Enter new RAID Name:")
            dialog.show()