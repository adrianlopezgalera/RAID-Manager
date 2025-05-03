import os
import subprocess
import sys

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
            return subprocess.Popen(*args, **kwargs, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                                            stderr=subprocess.PIPE, text=True)
        except subprocess.CalledProcessError as e:
            print(f"Error executing the command: {e}")

    @staticmethod
    def window_to_center(window):

        qr = window.frameGeometry()
        cp = window.screen().availableGeometry().center()

        qr.moveCenter(cp)
        window.move(qr.topLeft())

    @staticmethod
    def is_installed(program):

        try:
            subprocess.check_call(['which', program])
            return True
        except subprocess.CalledProcessError as e:
            print(f"Error code: {e}")
            return False

    @staticmethod
    def install_program(program_name):

        notification = Notifications()
        user_input = notification.question_notification(program_name)

        if user_input == QMessageBox.StandardButton.Ok:
            if EventsManager.is_installed('apt'):
                try:
                    subprocess.check_call(["pkexec", "apt", "install", program_name])
                    notification.success_notification(program_name, "installed")
                    EventsManager.restart()
                except subprocess.CalledProcessError as e:
                    print(f"Error installing {program_name}: {e}")
            if EventsManager.is_installed('yum'):
                try:
                    subprocess.check_call(["pkexec", "yum", "install", program_name])
                    notification.success_notification(program_name, "installed")
                    EventsManager.restart()
                except subprocess.CalledProcessError as e:
                    print(f"Error installing {program_name}: {e}")
            if EventsManager.is_installed('dnf'):
                try:
                    subprocess.check_call(["pkexec", "dnf", "install", program_name])
                    notification.success_notification(program_name, "installed")
                    EventsManager.restart()
                except subprocess.CalledProcessError as e:
                    print(f"Error installing {program_name}: {e}")
        else:
            EventsManager.close()

    @staticmethod
    def restart():
        os.execl(sys.executable, sys.executable, *sys.argv)

    @staticmethod
    def close():
        sys.exit()

    @staticmethod
    def has_policy():
        if os.path.exists("/etc/sudoers.d/mdadm"):
            return True
        else:
            return False


    @staticmethod
    def install_policy():

        notification = Notifications()
        user_input = notification.question_notification('a policy file')

        if user_input == QMessageBox.StandardButton.Ok:

            try:

                # Define the content of the file with user privilege specification:
                file_content = "# User privilege specification\nALL ALL = NOPASSWD: /usr/sbin/mdadm"

                # Define the file path and name:
                file_path = os.getcwd()
                file_name = "mdadm"

                # Create the file with user privilege specification:
                with open(os.path.join(file_path, file_name), "w") as file:
                    file.write(file_content)

                # Copy the file into /etc/sudoers.d:
                command = f"pkexec cp '{os.path.join(file_path, file_name)}' /etc/sudoers.d/{file_name}"

                # Execute the command using subprocess:
                EventsManager.run_command(command, shell=True)

                # Delete temporal file:
                os.remove(os.path.join(file_path, file_name))

                # Inform the user:
                notification.success_notification('The policy', "installed")

                # Restart the application:
                EventsManager.restart()

            except subprocess.CalledProcessError:

               notification = Notifications()
               notification.error_notification('the policy')

        else:
            EventsManager.close()


    @staticmethod
    def new_window(self):
        self.show()

    @staticmethod
    def create_object(class_name):
        return type(class_name)

    @staticmethod
    def print_selected_raid(window):
        #window.set_selected_raid()
        window.ui.selected_raid.setText(window.selected_raid)

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

    @staticmethod
    def fill_raid_list(window):

        window.ui.select_raid.clear()

        arrays = EventsManager.run_command(['sudo', 'mdadm', '--detail' , '--scan'], capture_output=True, text=True).stdout.splitlines()

        for array in arrays:
            window.ui.select_raid.addItem(array[array.find('/'): array.find(' metadata')])

    @staticmethod
    def fill_device_list(window):

        window.ui.selector.clear()

        devices = EventsManager.run_command(['lsblk', '-o', 'NAME,SIZE,TYPE,FSTYPE,MOUNTPOINT', '-l', '--noheadings'], capture_output=True, text=True).stdout.splitlines()

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
                    window.ui.selector.addItem(f"{device_name} - {device_size} ({device_fstype})")

    @staticmethod
    def fill_raid_member_list(raid):

        arrays = EventsManager.run_command(['sudo', 'mdadm', '--detail', raid], capture_output=True, text=True).stdout.splitlines()

        device = ""

        for line in arrays:

            if line.__contains__('/dev/s'):

                device += line[line.find('/'):] + '\n'

        return device.splitlines()


    @staticmethod
    def check_if_selected_raid(selected_raid):
        if selected_raid != "":
            return True
        else:
            notify = Notifications()
            notify.new_notification(title="Error", text="You must select a RAID first.", icon="critical", buttons=["ok"])
            return False

    @staticmethod
    def change_level_dialog(selected_raid):
        if EventsManager.check_if_selected_raid(selected_raid):
            dialog = Dialogs()

            # Dialog attributes:

            dialog.setWindowTitle("Change RAID Level")
            dialog.ui.label.setText("Enter new RAID Level:")
            dialog.ui.current_attribute_label.setText("Current RAID Path:")
            dialog.ui.current_attribute.setText(selected_raid)

            # Enabling selector:

            dialog.ui.selector.setEnabled(True)
            dialog.ui.text.setEnabled(False)

            # Filling selector:

            dialog.ui.selector.addItem("0")
            dialog.ui.selector.addItem("1")
            dialog.ui.selector.addItem("5")
            dialog.ui.selector.addItem("6")

            # Actions:

            dialog.show()

            dialog.ui.ok_button.clicked.connect(lambda: change_level_action())

            def change_level_action():

                new_level = dialog.ui.selector.currentText()
                process = EventsManager.read_output('sudo mdadm --grow ' + selected_raid + ' --level=' + new_level)
                response = process.stderr.readline()

                print(response)

                window = Notifications()

                if response.__contains__("no change requested"):
                    window.new_notification(title="Error", text="The raid already has the selected level", icon="critical", buttons=["ok"])

                if response.__contains__("Impossible level change requested"):
                    window.new_notification(title="Error", text="The raid cannot be changed to the level " + new_level,
                                            icon="critical", buttons=["ok"])
                if response.__contains__("Need 1 spare to avoid degraded array, and only have 0"):
                    window.new_notification(title="Error", text="You need 1 spare to avoid degraded array, and only have 0",
                                            icon="critical", buttons=["ok"])
                if response.__contains__("could not set level"):
                    window.new_notification(title="Error", text="The raid could not set level to " + new_level,
                                            icon="critical", buttons=["ok"])
                if response.__contains__("changed to"):
                    window.new_notification(title="Information",
                                            text="Level of " + selected_raid + " changed to " + new_level,
                                            icon="information", buttons=["ok"])



            """
            To change the level: mdadm --grow /dev/md0 --level=5

            To add a drive: mdadm --manage /dev/md0 --add /dev/sdb1

            To remove a drive: mdadm --manage /dev/md0 --remove /dev/sdb1

            To assemble: mdadm --assemble /dev/md0

            To stop: mdadm --stop /dev/md0
            'sudo mdadm --stop ' + selected_raid

            To delete an existing RAID: mdadm --stop /dev/md0 mdadm --remove /dev/md0
            
            process2 = EventsManager.read_output('sudo mdadm' + ' /dev/' + self.raid_name, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                print(process2)

                print(process2.stderr.readline())
            """

    @staticmethod
    def add_drive_dialog(selected_raid):
        if EventsManager.check_if_selected_raid(selected_raid):
            dialog = Dialogs()

            # Dialog attributes:

            dialog.setWindowTitle("Add drive to RAID")
            dialog.ui.label.setText("Select a drive to add:")
            dialog.ui.current_attribute_label.setText("Current RAID Path:")
            dialog.ui.current_attribute.setText(selected_raid)

            # Enabling selector:

            dialog.ui.selector.setEnabled(True)
            dialog.ui.text.setEnabled(False)

            # Filling selector:

            EventsManager.fill_device_list(dialog)

            # Actions:

            dialog.show()

            dialog.ui.ok_button.clicked.connect(lambda: add_drive_action())

            def add_drive_action():
                selected_drive = dialog.ui.selector.currentText()
                process = EventsManager.read_output('sudo mdadm --manage ' + selected_raid + ' --add=' + selected_drive)

                response = process.stderr.readline()

                print(response)


    @staticmethod
    def remove_drive_dialog(selected_raid):
        if EventsManager.check_if_selected_raid(selected_raid):
            dialog = Dialogs()

            # Dialog attributes:

            dialog.setWindowTitle("Remove drive from RAID")
            dialog.ui.label.setText("Select a drive to remove:")
            dialog.ui.current_attribute_label.setText("Current RAID Path:")
            dialog.ui.current_attribute.setText(selected_raid)

            # Enabling selector:

            dialog.ui.selector.setEnabled(True)
            dialog.ui.text.setEnabled(False)

            # Filling selector:

            devices = EventsManager.fill_raid_member_list(selected_raid)

            for device in devices:

                dialog.ui.selector.addItem(device)

            # Actions:

            dialog.show()

            dialog.ui.ok_button.clicked.connect(lambda: remove_drive_action())

            def remove_drive_action():
                selected_drive = dialog.ui.selector.currentText()
                EventsManager.run_command('umount ' + selected_drive, shell=True)
                #EventsManager.run_command('sudo mdadm --stop ' + selected_raid, shell=True)
                process = EventsManager.read_output('sudo mdadm ' + selected_raid + ' --fail ' + selected_drive + ' --remove ' + selected_drive)

                response = process.stderr.readline()

                print(response)

                if response.__contains__("Device or resource busy"):
                    notification = Notifications()
                    notification.new_notification(title="Error", text="Device or resource busy. If you have created the RAID in this session, you need to restart your system first.",
                                            icon="critical", buttons=["ok"])

    @staticmethod
    def assemble_dialog(window):
            process = EventsManager.read_output('sudo mdadm --assemble --scan')

            started_raid = ""

            output = process.stderr.readlines()

            for line in output:
                started_raid += line + "\n"

            notification = Notifications()
            notification.new_notification(title="Information",
                                              text=started_raid,
                                              icon="information", buttons=["ok"])
            EventsManager.fill_raid_list(window)

    @staticmethod
    def stop_dialog(window):
        if EventsManager.check_if_selected_raid(window.get_selected_raid()):
            process = EventsManager.read_output('sudo mdadm --stop ' + window.get_selected_raid())

            output = process.stderr.readline()
            print(output)

            if output.__contains__("No such file or directory"):
                notification = Notifications()
                notification.new_notification(title="Error",
                                              text="The RAID is already stopped",
                                              icon="critical", buttons=["ok"])

            if output.__contains__("stopped"):

                notification = Notifications()
                notification.success_notification(window.get_selected_raid(), "stopped")
                EventsManager.fill_raid_list(window)

    @staticmethod
    def delete_dialog(window):
        if EventsManager.check_if_selected_raid((window.get_selected_raid())):
            EventsManager.run_command('umount ' + window.get_selected_raid(), shell=True)
            EventsManager.run_command('sudo mdadm --stop ' + window.get_selected_raid(), shell=True)
            process = EventsManager.read_output('sudo mdadm --remove ' + window.get_selected_raid())

            output = process.stderr.readline()
            print(output)

            if output.__contains__("No such file or directory"):
                notification = Notifications()
                notification.new_notification(title="Error",
                                              text="The RAID is already deleted",
                                              icon="critical", buttons=["ok"])

            if output.__contains__("deleted"):
                notification = Notifications()
                notification.success_notification(window.get_selected_raid(), "deleted")
                EventsManager.fill_raid_list(window)
