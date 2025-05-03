import subprocess

from PyQt6.QtWidgets import QAbstractButton
from PySide6.QtWidgets import QWidget, QMessageBox
from UI.ui_new_raid import Ui_New_Raid
from notifications import Notifications
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

        # Executing functions:
        EventsManager.fill_device_list(self)

        # Connecting buttons to events:
        self.ui.new_raid_cancel.clicked.connect(self.close)
        self.ui.add_device.clicked.connect(lambda: self.set_selected_devices())
        self.ui.remove_devices.clicked.connect(lambda: self.clear_selected_devices())
        self.ui.new_raid_create.clicked.connect(lambda: self.create_new_raid())

    def select_devices(self):
       return '/dev/' + self.ui.selector.currentText()[0: self.ui.selector.currentText().find('-')]

    def set_selected_devices(self):

        self.selected_device = self.select_devices()

        if (self.selected_device == "") or (self.selected_devices.__contains__(self.selected_device)) or (self.selected_device.__eq__("/dev/")):
           pass
        else:
            self.selected_devices += '\n' + self.selected_device
            self.ui.devices_path.setText(self.selected_devices)

    def clear_selected_devices(self):
        self.selected_devices = ""
        self.ui.devices_path.setText(self.selected_devices)

    def create_new_raid(self):

        self.raid_name = self.ui.raid_name.text()
        self.raid_level = self.ui.raid_level.currentText()

        EventsManager.run_command('umount ' + self.selected_devices.replace("\n", " "), shell=True)

        process = EventsManager.read_output('sudo mdadm --create --verbose --force ' + '/dev/'+self.raid_name + ' ' + '--level=' + self.raid_level + ' ' + '--raid-devices=' + str(self.selected_devices.count('\n')) + ' ' + self.selected_devices.replace("\n", " "))

        response = process.stderr.readline()

        print(response)

        """
        if response.__contains__("'1' is an unusual number of drives for an array"):
            dialog.new_notification(title="Error", text="At least 2 raid-devices are needed for level 5.", icon="critical", buttons=["ok"])
            
            mdadm: Note: this array has metadata at the start and
    may not be suitable as a boot device.  If you plan to
    store '/boot' on this device please ensure that
    your boot-loader understands md/v1.x metadata, or use
    --metadata=0.90
        """
        if response.__contains__("chunk size defaults to 512K"):
            dialog = Notifications()

            user_input = dialog.new_notification(title="Warning", text="The chunk size will be defaulted to 512K." + "\nAre you sure that you want to continue?", icon="warning", buttons=["ok", "cancel"])

            if EventsManager.user_input_checking(user_input, process):
                lines = process.communicate()

                for line in lines:
                    print(line)

                    if line.__contains__("is already in use"):
                        dialog.new_notification(title="Error", text="The entered name is already in use", icon="critical", buttons=[])

            #EventsManager.fill_raid_list(edit)
        elif response.__contains__("ext2fs file system"):
            dialog = Notifications()
            user_input = dialog.new_notification(title="Warning", text="At least one selected device appears to contain an ext2fs file system." + "\nAre you sure that you want to continue?", icon="warning", buttons=["ok", "cancel"])

            if EventsManager.user_input_checking(user_input, process):

                lines = process.communicate()

                for line in lines:
                    print(line)

                    if line.__contains__("is already in use"):
                        dialog.new_notification(title="Error", text="The entered name is already in use", icon="critical", buttons=[])

        elif response.__contains__("at least 2 raid-devices needed for level 5"):
            dialog = Notifications()

            dialog.new_notification(title="Error", text="At least 2 raid-devices are needed for level 5.", icon="critical", buttons=["ok"])

        elif response.__contains__("at least 4 raid-devices needed for level 6"):
            dialog = Notifications()

            dialog.new_notification(title="Error", text="At least 3 raid-devices are needed for level 6.", icon="critical", buttons=["ok"])

        elif response.__contains__("invalid number of raid devices"):
            dialog = Notifications()

            dialog.new_notification(title="Error", text="Invalid number of raid devices.", icon="critical", buttons=["ok"])

        elif response.__contains__("partition table exists"):
            dialog = Notifications()

            dialog.new_notification(title="Error", text="There is already a partition table in: " + self.selected_devices, icon="critical", buttons=["ok"])
        else:
            pass

        # Metadatos para crear RAID sin interrupciones: --metadata = 0.90 - -run
        # Metadatos de procesos: shell=True, check=True, stdout=subprocess.PIPE, universal_newlines=True

"""
    def fill_device_list(self):

        result = EventsManager.run_command(['lsblk', '-o', 'NAME,SIZE,TYPE,FSTYPE,MOUNTPOINT', '-l', '--noheadings'], capture_output=True, text=True)

        output = result.stdout

        devices = output.splitlines()
        for device in devices:
            device_info = device.split()
            if len(device_info) >= 4:
                device_name = device_info[0]
                device_size = device_info[1]
                device_type = device_info[2]
                device_fstype = device_info[3]

                if device_fstype == "linux_raid_member":
                    continue

                if len(device_info) == 5:
                    device_mount_point = device_info[4]

                    if (len(device_mount_point) == 1) or (device_mount_point.__contains__("/home")) or (device_mount_point.__contains__("/boot/efi")):
                        continue

                if device_type == "part":
                    self.ui.devices.addItem(f"{device_name} - {device_size} ({device_fstype})")

"""