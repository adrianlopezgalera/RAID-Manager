from PySide6 import QtCore
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

        # Element properties:
        self.ui.raid_level.setItemData(0, "Level 0: Striped volume, no parity information, redundancy, or fault tolerance.", role=QtCore.Qt.ItemDataRole.ToolTipRole)
        self.ui.raid_level.setItemData(1, "Level 1: Mirror volume, total redundancy without parity.", role=QtCore.Qt.ItemDataRole.ToolTipRole)
        self.ui.raid_level.setItemData(2, "Level 5: Block-level striped volume with parity. The array tolerates 1 faulty disk.", role=QtCore.Qt.ItemDataRole.ToolTipRole)
        self.ui.raid_level.setItemData(3, "Level 6: Block-level striped volume with parity. The array tolerates 2 faulty disks.", role=QtCore.Qt.ItemDataRole.ToolTipRole)

        # Executing functions:
        EventsManager.fill_device_list(self)

        # Connecting buttons to events:
        self.ui.new_raid_cancel.clicked.connect(self.close)
        self.ui.add_device.clicked.connect(lambda: self.set_selected_devices())
        self.ui.remove_devices.clicked.connect(lambda: self.clear_selected_devices())
        self.ui.new_raid_create.clicked.connect(lambda: self.create_new_raid())

    # Returns the selected device in the necessary format to function as a parameter to create the RAID:

    def select_devices(self):
       return '/dev/' + self.ui.selector.currentText()[0: self.ui.selector.currentText().find('-')]

    # Merges the strings of the selected devices:

    def set_selected_devices(self):

        self.selected_device = self.select_devices()

        # This avoids null, the repetition of devices already present and the interaction with an empty selector:

        if (self.selected_device == "") or (self.selected_devices.__contains__(self.selected_device)) or (self.selected_device.__eq__("/dev/")):
           pass
        else:
            self.selected_devices += '\n' + self.selected_device
            self.ui.devices_path.setText(self.selected_devices)

    # Clears the list of devices and updates the viewed list:

    def clear_selected_devices(self):
        self.selected_devices = ""
        self.ui.devices_path.setText(self.selected_devices)

    # Creates a new RAID with the entered settings:

    def create_new_raid(self):

        # Reads the fields of the form:

        self.raid_name = self.ui.raid_name.text()
        self.raid_level = self.ui.raid_level.currentText()

        # Fallback method in case of any device is mount on the system:

        EventsManager.run_command('umount ' + self.selected_devices.replace("\n", " "), shell=True)

        # Starts the process:

        process = EventsManager.read_output('sudo mdadm --create --verbose --force ' + '/dev/md/'+self.raid_name + ' --name='+self.raid_name + ' --level=' + self.raid_level + ' --raid-devices=' + str(self.selected_devices.count('\n')) + ' ' + self.selected_devices.replace("\n", " "))

        # Reads the output:

        response = process.stderr.readline()

        # Used to evaluate new exceptions from 'mdadm':

        print(response)

        # Flag to evaluate if the creating process should continue. By default, it is 'True'.

        continue_process = True

        # Evaluates if the output contains an exception from 'mdadm'. Each condition is a possible exception:

        if response.__contains__("chunk size defaults to 512K"):

            # Shows a notification dialog to inform the user:

            dialog = Notifications()

            user_input = dialog.new_notification(title="Warning", text="The chunk size will be defaulted to 512K." + "\nAre you sure that you want to continue?", icon="warning", buttons=["ok", "cancel"])

            # Evaluates if the user accepts. If 'yes', reads the new output from the previous process:

            if EventsManager.user_input_checking(user_input, process):

                lines = process.communicate()

                for line in lines:

                    # Used to evaluate new exceptions from 'mdadm':

                    print(line)

                    if line.__contains__("is already in use"):

                        # Overriding the previous object to avoid conflicts with buttons:

                        dialog = Notifications()

                        dialog.new_notification(title="Error", text="The entered name (" + self.raid_name + ") is already in use. Please, enter another name", icon="critical", buttons=[])
                        continue_process = False
                        

        elif response.__contains__("ext2fs file system"):
            dialog = Notifications()
            user_input = dialog.new_notification(title="Warning", text="At least one selected device appears to contain an ext2fs file system." + "\nAre you sure that you want to continue?", icon="warning", buttons=["ok", "cancel"])

            # Evaluates if the user accepts. If 'yes', reads the new output from the previous process:

            if EventsManager.user_input_checking(user_input, process):

                lines = process.communicate()

                for line in lines:

                    # Used to evaluate new exceptions from 'mdadm':

                    print(line)

                    if line.__contains__("is already in use"):
                        dialog = Notifications()
                        dialog.new_notification(title="Error", text="The entered name is already in use", icon="critical", buttons=["ok"])
                        continue_process = False

        elif response.__contains__("at least 2 raid-devices needed for level 5"):
            dialog = Notifications()

            dialog.new_notification(title="Error", text="At least 2 raid-devices are needed for level 5.", icon="critical", buttons=["ok"])
            continue_process = False


        elif response.__contains__("at least 4 raid-devices needed for level 6"):
            dialog = Notifications()

            dialog.new_notification(title="Error", text="At least 4 raid-devices are needed for level 6.", icon="critical", buttons=["ok"])
            continue_process = False


        elif response.__contains__("invalid number of raid devices"):
            dialog = Notifications()

            dialog.new_notification(title="Error", text="Invalid number of raid devices.", icon="critical", buttons=["ok"])
            continue_process = False


        elif response.__contains__("partition table exists"):
            dialog = Notifications()

            dialog.new_notification(title="Error", text="There is already a partition table in: " + self.selected_devices, icon="critical", buttons=["ok"])
            continue_process = False

        else:
            pass

        # If the flag remains being 'True':

        if continue_process:

            dialog = Notifications()

            # Informs the user and aks if restart the system to use the new created RAID:

            user_input = dialog.new_notification(title="Information", text="RAID created correctly. To use the created raid, you must restart the system. Press 'Apply' to restart now or click 'Cancel' to restart later.", icon="information",
                                    buttons=["apply", "cancel"])

            # If the user accepts, the system restarts:

            if user_input == QMessageBox.StandardButton.Apply:
                EventsManager.restart_system()