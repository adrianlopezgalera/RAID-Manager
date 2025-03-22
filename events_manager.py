import subprocess

from PySide6.QtWidgets import QFileDialog


class EventsManager:

    @staticmethod
    def read_output(command):
        try:
            response = subprocess.run('mdadm ' + command, shell=True, check=True, stdout=subprocess.PIPE, universal_newlines=True)
            print(response.stdout)
        except subprocess.CalledProcessError as e:
            print(f"Error executing the command: {e}")

    @staticmethod
    def new_window(self):
        self.show()

    @staticmethod
    def action(**kwargs):
        subprocess.run('mdadm ' + kwargs)

    @staticmethod
    def select_devices():
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.FileMode.Directory)
        dialog.setOption(QFileDialog.Option.ShowDirsOnly, True)
        return str(QFileDialog.getExistingDirectory(dialog, "Select Directory"))