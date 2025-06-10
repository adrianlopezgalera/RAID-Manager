import os
import subprocess
import sys
import json

from PySide6.QtWidgets import QMessageBox, QFileDialog
from dialogs import Dialogs
from notifications import Notifications

# This controller class carries out all shared operations across the application.

class EventsManager:

    # Executes a command via subprocess until its exit:

    @staticmethod
    def run_command(*args, **kwargs):
        try:
            return subprocess.run(*args, **kwargs)
        except subprocess.CalledProcessError as e:
            print(f"Error executing the command: {e}")

    # Executes a command via subprocess with interaction and sets pipelines:

    @staticmethod
    def read_output(*args, **kwargs):
        try:
            return subprocess.Popen(*args, **kwargs, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        except subprocess.CalledProcessError as e:
            print(f"Error executing the command: {e}")

    # Unmounts an entered device:

    @staticmethod
    def unmount_device(device):
        EventsManager.run_command('umount ' + device, shell=True)

    # Centers an entered window:

    @staticmethod
    def window_to_center(window):

        qr = window.frameGeometry()
        cp = window.screen().availableGeometry().center()

        qr.moveCenter(cp)
        window.move(qr.topLeft())

    # Checks if a program (dependency) is installed:

    @staticmethod
    def is_installed(program):

        try:
            subprocess.check_call(['which', program])
            return True
        except subprocess.CalledProcessError as e:
            print(f"Error code: {e}")
            return False

    # Installs an entered program with the proper package manager:

    @staticmethod
    def install_program(program_name):

        notification = Notifications()

        # Asks user for confirmation:

        user_input = notification.question_notification(program_name)

        if user_input == QMessageBox.StandardButton.Ok:
            if EventsManager.is_installed('apt'):
                try:
                    subprocess.check_call(["pkexec", "apt", "install", program_name])
                    notification.success_notification(program_name, "installed")
                    EventsManager.restart_app()
                except subprocess.CalledProcessError as e:
                    print(f"Error installing {program_name}: {e}")
            elif EventsManager.is_installed('yum'):
                try:
                    subprocess.check_call(["pkexec", "yum", "install", program_name])
                    notification.success_notification(program_name, "installed")
                    EventsManager.restart_app()
                except subprocess.CalledProcessError as e:
                    print(f"Error installing {program_name}: {e}")
            elif EventsManager.is_installed('dnf'):
                try:
                    subprocess.check_call(["pkexec", "dnf", "install", program_name])
                    notification.success_notification(program_name, "installed")
                    EventsManager.restart_app()
                except subprocess.CalledProcessError as e:
                    print(f"Error installing {program_name}: {e}")
            else:
                notification.error_notification(program_name)

        else:
            EventsManager.close()

    # Restarts the application:

    @staticmethod
    def restart_app():
        os.execl(sys.executable, sys.executable, *sys.argv)

    # Restarts the system:

    @staticmethod
    def restart_system():
        os.system('systemctl reboot -i')

    # Closes the application:

    @staticmethod
    def close():
        sys.exit()

    # Checks if the policy file is installed in the proper path:

    @staticmethod
    def has_policy():
        return os.path.exists("/etc/sudoers.d/mdadm")

    # Installs the policy file:

    @staticmethod
    def install_policy():

        notification = Notifications()

        # Asks user for confirmation:

        user_input = notification.question_notification('a policy file')

        if user_input == QMessageBox.StandardButton.Ok:

            try:

                # Defines the content of the file with user privilege specification:
                file_content = "# User privilege specification\nALL ALL = NOPASSWD: /usr/sbin/mdadm"

                # Defines the file path and name:
                file_path = os.getcwd()
                file_name = "mdadm"

                # Creates the file with user privilege specification:
                with open(os.path.join(file_path, file_name), "w") as file:
                    file.write(file_content)

                # Copies the file into /etc/sudoers.d:
                command = f"pkexec cp '{os.path.join(file_path, file_name)}' /etc/sudoers.d/{file_name}"

                # Executes the command using subprocess:
                EventsManager.run_command(command, shell=True)

                # Deletes temporal file:
                os.remove(os.path.join(file_path, file_name))

                # Informs the user:
                notification = Notifications()
                notification.success_notification('The policy', "installed")

                # Restarts the application:
                EventsManager.restart_app()

            except subprocess.CalledProcessError:

               notification = Notifications()
               notification.error_notification('the policy')

        else:
            EventsManager.close()

    # Shows a window of the entered class:

    @staticmethod
    def new_window(self):
        self.show()

    # Creates dynamically a new object from an entered class:

    @staticmethod
    def create_object(class_name):
        return type(class_name)

    # Updates the RAID selector of the entered window:

    @staticmethod
    def print_selected_raid(window):
        window.ui.selected_raid.setText(window.selected_raid)

    # Asks user for confirmation in order to continue with an entered process:

    @staticmethod
    def user_input_checking(dialog, process):

        if dialog == QMessageBox.StandardButton.Ok:
            process.stdin.write('y')
            process.stdin.flush()
            return True
        elif dialog == QMessageBox.StandardButton.Cancel:
            process.stdin.write('n')
            process.stdin.flush()
            return False
        else:
            process.stdin.write('n')
            process.stdin.flush()
            return False

    # Fill the RAID selector of the entered window:

    @staticmethod
    def fill_raid_list(window):

        # Clears the RAID selector:

        window.ui.select_raid.clear()

        # Get info about the entered RAID as a string array:

        raid_info = EventsManager.run_command(['sudo', 'mdadm', '--detail' , '--scan'], capture_output=True, text=True).stdout.splitlines()

        # If the output is empty:

        if not raid_info:
            window.ui.select_raid.setPlaceholderText("No RAID available")
            window.ui.select_raid.setToolTip("No RAID available")
        else:
            for array in raid_info:

                # Extracts the data by avoiding conflicting lines:

                if "Value" not in array:

                    window.ui.select_raid.addItem(array[array.find('/'): array.find(' metadata')])

    # Gets info about an entered RAID:

    @staticmethod
    def get_selected_raid_info(selected_raid):
        return EventsManager.run_command(['sudo', 'mdadm', '--detail', selected_raid], capture_output=True, text=True).stdout

    # Fallback fix to avoid a POSIX format conflict:

    @staticmethod
    def fix_posix(selected_raid):

        if selected_raid.__contains__(':'):
            selected_raid = "/dev/md/" + selected_raid[selected_raid.find(':') + 1:]

        return selected_raid

    # Exports the selected RAID in the chosen format:

    @staticmethod
    def export_selected_raid_info(window):

        # If there is no an available RAID, a dialog is shown:

        if window.selected_raid == "":
            notification = Notifications()
            notification.new_notification("Export", "No RAID available to export.", "critical", "ok")
        else:
            selected_option = window.ui.export_selector.currentText()

            match selected_option:
                case "TXT":
                    text = EventsManager.get_selected_raid_info(window.selected_raid)
                    EventsManager.save_to_text_file_dialog(text)

    # Saves an entered content into a file with a name:

    @staticmethod
    def save_txt_file(file_name, content):
        with open(file_name, 'w') as file:
            file.write(content)

    # Returns the content of a TXT file:

    @staticmethod
    def read_txt_file(file_name):
        try:
            with open(file_name, 'r') as file:
                return file.read()

        except FileNotFoundError:
            print("File not found.")
            return None

    # Generates a dynamic dialog to prompt the user to choose a name and location for the file:

    @staticmethod
    def save_to_text_file_dialog(text):
        file_dialog = QFileDialog()
        file_dialog.setWindowTitle("Save File")
        file_dialog.setAcceptMode(QFileDialog.AcceptMode.AcceptSave)

        file_name, _ = file_dialog.getSaveFileName(None, "Save File", "", "Text Files (*.txt)")

        # Checks if the extension exists to include it of avoid its repetition:

        if ".txt" or ".TXT" not in file_name:
            file_name += ".txt"

        # If the user chooses to save the file, the file is saved:

        if file_name:
            EventsManager.save_txt_file(file_name, text)

    # Saves a JSON with the entered content:

    @staticmethod
    def save_to_json_file(data, filename):

        try:
            with open(filename, 'w') as file:
                json.dump(data, file)
        except IOError:
            print ("Config file cannot be saved")

    # Returns the parsed content of a JSON file:

    @staticmethod
    def parse_json(filename):
        try:
            with open(filename, 'r') as file:
                #if os.stat(str(file)).st_size != 0:
                return json.load(file)

        except FileNotFoundError:
            return print("Config no found")

    # Returns of the content of the configuration file:

    @staticmethod
    def read_saved_options():
        return EventsManager.read_txt_file(".config")

    # Fills the list with the available drives to create a new RAID or add into one:

    @staticmethod
    def fill_device_list(window):

        # Clears the drive selector:

        window.ui.selector.clear()

        devices = EventsManager.run_command(['lsblk', '-o', 'NAME,SIZE,TYPE,FSTYPE,MOUNTPOINT', '-l', '--noheadings'], capture_output=True, text=True).stdout.splitlines()

        for device in devices:
            device_info = device.split()
            if len(device_info) >= 4:
                device_name = device_info[0]
                device_size = device_info[1]
                device_type = device_info[2]
                device_fstype = device_info[3]

                # Avoids the device if it's already part of a Linux RAID:

                if device_fstype == "linux_raid_member":
                    continue

                if len(device_info) == 5:
                    device_mount_point = device_info[4]

                    # Avoids the device if it's root, home or an EFI partition:

                    if (len(device_mount_point) == 1) or (device_mount_point.__contains__("/home")) or (device_mount_point.__contains__("/boot/efi")):
                        continue

                if device_type == "part":
                    window.ui.selector.addItem(f"{device_name} - {device_size} ({device_fstype})")

        if not window.ui.selector.currentText():
            window.ui.selector.setToolTip("No device available")

    # Returns a string with the drives that are part of entered RAID:

    @staticmethod
    def get_raid_member_string(selected_raid):

        arrays = EventsManager.run_command(['sudo', 'mdadm', '--detail', selected_raid], capture_output=True, text=True).stdout.splitlines()

        # A variable to save a string with all drives:

        device = ""

        for line in arrays:

            if line.__contains__('/dev/s'):
                device += line[line.find('/'):] + ' '

        return device

    # Returns a string array with the drives that are part of entered RAID:

    @staticmethod
    def fill_raid_member_list(selected_raid):

        arrays = EventsManager.run_command(['sudo', 'mdadm', '--detail', selected_raid], capture_output=True, text=True).stdout.splitlines()

        device = ""

        for line in arrays:

            if line.__contains__('/dev/s'):

                device += line[line.find('/'):] + '\n'

        return device.splitlines()

    # Checks if there is a selected RAID:

    @staticmethod
    def check_if_selected_raid(selected_raid):
        if selected_raid != "":
            return True
        else:
            notify = Notifications()
            notify.new_notification(title="Error", text="You must select a RAID first.", icon="critical", buttons=["ok"])
            return False

    # Method for changing RAID level. It creates a dynamic dialog first:

    @staticmethod
    def change_level_dialog(window):
        if EventsManager.check_if_selected_raid(window.selected_raid):
            dialog = Dialogs()

            # Dialog attributes:

            dialog.setWindowTitle("Change RAID Level")
            dialog.ui.label.setText("Enter new RAID Level:")
            dialog.ui.current_attribute_label.setText("Current RAID Path:")
            dialog.ui.current_attribute.setText(window.selected_raid)

            # Enabling selector:

            dialog.ui.selector.setEnabled(True)
            dialog.ui.text.setEnabled(False)
            dialog.ui.selector_mode.setEnabled(False)
            dialog.ui.selector_mode.setHidden(True)

            # Filling selector:

            dialog.ui.selector.addItem("0")
            dialog.ui.selector.addItem("1")
            dialog.ui.selector.addItem("5")
            dialog.ui.selector.addItem("6")

            # Actions:

            dialog.show()

            dialog.ui.ok_button.clicked.connect(lambda: change_level_action())

            # Nested method for changing RAID level:

            def change_level_action():

                new_level = dialog.ui.selector.currentText()
                process = EventsManager.read_output('sudo mdadm --grow ' + window.selected_raid + ' --level=' + new_level)
                response = process.stderr.readline()

                notification = Notifications()

                if response.__contains__("no change requested"):
                    notification.new_notification(title="Error", text="The selected raid already has the selected level", icon="critical", buttons=["ok"])

                if response.__contains__("Impossible level change requested"):
                    notification.new_notification(title="Error", text="The selected raid cannot be changed to the level " + new_level,
                                            icon="critical", buttons=["ok"])
                if response.__contains__("Need 1 spare to avoid degraded array, and only have 0"):
                    notification.new_notification(title="Error", text="You need 1 spare to avoid degraded array, and only have 0",
                                            icon="critical", buttons=["ok"])
                if response.__contains__("could not set level"):
                    notification.new_notification(title="Error", text="The selected raid could not set level to " + new_level,
                                            icon="critical", buttons=["ok"])
                if response.__contains__("changed to"):
                    notification.new_notification(title="Information",
                                            text="Level of " + window.selected_raid + " changed to " + new_level,
                                            icon="information", buttons=["ok"])

    # Method for changing RAID name. It creates a dynamic dialog first:

    @staticmethod
    def change_name_dialog(window):
        if EventsManager.check_if_selected_raid(window.selected_raid):
            dialog = Dialogs()

            # Dialog attributes:

            dialog.setWindowTitle("New name")
            dialog.ui.label.setText("Enter a new name:")
            dialog.ui.current_attribute_label.setText("Current RAID Path:")
            dialog.ui.current_attribute.setText(window.selected_raid)

            # Enabling selectors:

            dialog.ui.text.setEnabled(True)
            dialog.ui.selector.setEnabled(False)
            dialog.ui.selector.setHidden(True)
            dialog.ui.selector_mode.setEnabled(False)
            dialog.ui.selector_mode.setHidden(True)

            # Actions:

            dialog.show()

            dialog.ui.ok_button.clicked.connect(lambda: change_name_action())

            # Nested method for changing RAID name:

            def change_name_action():

                # Get new name for the selected RAID:

                new_name = dialog.ui.text.text()

                if new_name != "":

                    # Get devices from selected RAID:

                    devices = EventsManager.get_raid_member_string(window.selected_raid)

                    # Stop the RAID:

                    EventsManager.stop_dialog(window)

                    # Update name for the selected RAID:

                    process = EventsManager.read_output('sudo mdadm --assemble --update=name --name=2 ' + new_name + ' ' +  window.selected_raid + ' ' + devices)

                    response = process.stderr.readline()

                    notification = Notifications()
                    notification.new_notification(title="Information", text=response[6:], icon="information", buttons=["ok"])
                    EventsManager.fill_raid_list(window)
                else:
                    notification = Notifications()
                    notification.new_notification(title="Error", text="The new name cannot be empty.", icon="critical", buttons=["ok"])

    # Method for adding a drive to a selected RAID. It creates a dynamic dialog first:

    @staticmethod
    def add_drive_dialog(window):
        if EventsManager.check_if_selected_raid(window.selected_raid):

            selected_raid = EventsManager.fix_posix(window.get_selected_raid())

            dialog = Dialogs()

            # Dialog attributes:

            dialog.setWindowTitle("Add drive to RAID")
            dialog.ui.label.setText("Select a drive to add:")
            dialog.ui.label_mode.setText("Starting drive as:")
            dialog.ui.current_attribute_label.setText("Current RAID Path:")
            dialog.ui.current_attribute.setText(window.selected_raid)

            # Enable selectors:

            dialog.ui.selector.setEnabled(True)
            dialog.ui.selector_mode.setEnabled(True)
            dialog.ui.text.setEnabled(False)

            # Fill selectors:

            EventsManager.fill_device_list(dialog)
            dialog.ui.selector_mode.addItem("Active")
            dialog.ui.selector_mode.addItem("Spare")


            # Actions:

            dialog.show()

            dialog.ui.ok_button.clicked.connect(lambda: add_drive_action())

            # Nested method for adding a drive to a RAID:

            def add_drive_action():

                selected_option = dialog.ui.selector_mode.currentText()

                match selected_option:
                    case "Active":
                        selected_drive = '/dev/' + dialog.ui.selector.currentText()[0: dialog.ui.selector.currentText().find('-')].strip()

                        EventsManager.unmount_device(selected_drive)

                        process = EventsManager.read_output('sudo mdadm --manage ' + selected_raid + ' --add ' + selected_drive)

                        response = process.stderr.readline()

                        if response.__contains__("not large enough to join array"):
                            notification = Notifications()
                            notification.new_notification(title="Error", text="The selected drive (" + selected_drive + ") is not large enough to join array", icon="critical", buttons=["ok"])

                        if response.__contains__("added"):
                            notification = Notifications()
                            notification.new_notification(title="Information", text="The selected drive (" + selected_drive + ") has been added to the RAID (" + window.selected_raid + ") as an active drive", icon="information", buttons=["ok"])


                    case "Spare":
                        selected_drive = '/dev/' + dialog.ui.selector.currentText()[0: dialog.ui.selector.currentText().find('-')].strip()

                        EventsManager.unmount_device(selected_drive)

                        process = EventsManager.read_output('sudo mdadm --manage ' + selected_raid + ' --add-spare ' + selected_drive)

                        response = process.stderr.readline()

                        if response.__contains__("not large enough to join array"):
                            notification = Notifications()
                            notification.new_notification(title="Error", text="The selected drive (" + selected_drive + ") is not large enough to join array", icon="critical", buttons=["ok"])

                        if response.__contains__("added"):
                            notification = Notifications()
                            notification.new_notification(title="Information", text="The selected drive (" + selected_drive + ") has been added to the RAID (" + window.selected_raid + ") as a spare drive", icon="information", buttons=["ok"])


    # Method for removing a drive from a selected RAID. It creates a dynamic dialog first:

    @staticmethod
    def remove_drive_dialog(window):
        if EventsManager.check_if_selected_raid(window.selected_raid):

            selected_raid = EventsManager.fix_posix(window.get_selected_raid())

            dialog = Dialogs()

            # Dialog attributes:

            dialog.setWindowTitle("Remove drive from RAID")
            dialog.ui.label.setText("Select a drive to remove:")
            dialog.ui.current_attribute_label.setText("Current RAID Path:")
            dialog.ui.current_attribute.setText(window.selected_raid)

            # Enable selector:

            dialog.ui.selector.setEnabled(True)
            dialog.ui.text.setEnabled(False)
            dialog.ui.selector_mode.setEnabled(False)
            dialog.ui.selector_mode.setHidden(True)

            # Fill selector:

            devices = EventsManager.fill_raid_member_list(window.selected_raid)

            for device in devices:

                dialog.ui.selector.addItem(device)

            # Actions:

            dialog.show()

            dialog.ui.ok_button.clicked.connect(lambda: remove_drive_action())

            def remove_drive_action():
                selected_drive = dialog.ui.selector.currentText()

                if selected_drive:

                    EventsManager.unmount_device(selected_drive)
                    EventsManager.run_command('sudo mdadm ' + selected_raid + ' --fail ' + selected_drive, shell=True)
                    process = EventsManager.read_output('sudo mdadm ' + window.selected_raid + ' --remove ' + selected_drive)

                    response = process.stderr.readline()

                    print(response)

                    if response.__contains__("resource busy"):
                        notification = Notifications()
                        notification.new_notification(title="Error", text="Device or resource busy. If you have created the RAID in this session, you need to restart your system first. If not, wait for while and try it again",
                                                icon="critical", buttons=["ok"])

                    if response.__contains__("removed"):
                        notification = Notifications()
                        notification.new_notification(title="Information",
                                                      text="The selected drive (" + selected_drive + ") has been removed from the RAID (" + window.selected_raid + ")",
                                                      icon="information", buttons=["ok"])
                else:
                    notification = Notifications()
                    notification.new_notification(title="Error",
                                                  text="No device available to remove",
                                                  icon="critical", buttons=["ok"])

    # Method for assembling existing RAIDs::

    @staticmethod
    def assemble_dialog(window):
        process = EventsManager.read_output('sudo mdadm --assemble --scan')

        started_raid = ""

        output = process.stderr.readlines()

        for line in output:
            started_raid += line[6:] + "\n"

        if started_raid.__eq__('') or started_raid.__contains__("mdadm: No arrays found in config file or automatically"):
            notification = Notifications()
            notification.new_notification(title="Information", text="There are no RAIDs available to assemble.", icon="information", buttons=["ok"])
            EventsManager.fill_raid_list(window)
        else:
            notification = Notifications()
            notification.new_notification(title="Information", text=started_raid, icon="information", buttons=["ok"])

            # Updates the current RAID list:

            EventsManager.fill_raid_list(window)

    # Method for stopping a selected RAID:

    @staticmethod
    def stop_dialog(window):
        if EventsManager.check_if_selected_raid(window.get_selected_raid()):
            process = EventsManager.read_output('sudo mdadm --stop ' + window.get_selected_raid())

            output = process.stderr.readline()

            if output.__contains__("No such file or directory"):
                notification = Notifications()
                notification.new_notification(title="Error", text="The RAID is already stopped", icon="critical", buttons=["ok"])

            if output.__contains__("stopped"):
                notification = Notifications()
                notification.success_notification(window.get_selected_raid(), "stopped")

        # Updates the current RAID list:

        EventsManager.fill_raid_list(window)

    # Method for deleting a selected RAID:

    @staticmethod
    def delete_dialog(window):
        if EventsManager.check_if_selected_raid((window.get_selected_raid())):

            selected_raid = EventsManager.fix_posix(window.get_selected_raid())

            notification = Notifications()
            user_input = notification.new_notification(title="Warning", text="The selected RAID (" + window.get_selected_raid() + ") will be permanently deleted. This action cannot be undone. Are you sure that you want to continue?", icon="warning", buttons=["ok", "cancel"])

            if user_input == QMessageBox.StandardButton.Ok:

                raid_info = EventsManager.run_command(['sudo', 'mdadm', '--detail', window.selected_raid], capture_output=True, text=True).stdout.splitlines()

                devices = ""

                for line in raid_info[1:]:

                    if line.__contains__('/'):
                        devices += line[line.find('/'):] + ' '

                EventsManager.run_command('sudo mdadm --stop ' + window.get_selected_raid(), shell=True)
                process = EventsManager.read_output('sudo mdadm --zero-superblock ' + window.get_selected_raid() +  ' ' + devices)
                EventsManager.run_command('sudo mdadm --remove ' + window.get_selected_raid(), shell=True)

                output = process.stderr.readline()

                if output.__contains__("No such file or directory"):
                    notification = Notifications()
                    notification.new_notification(title="Error",
                                                  text="The RAID is already deleted",
                                                  icon="critical", buttons=["ok"])
                else:
                    notification = Notifications()
                    notification.success_notification(selected_raid, "deleted")

                # Updates the current RAID list:

                EventsManager.fill_raid_list(window)