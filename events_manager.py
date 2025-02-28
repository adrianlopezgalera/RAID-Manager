import subprocess

class Events_Manager:

    @staticmethod
    def read_output(command):
        try:
            response = subprocess.run('mdadm ' + command, shell=True, check=True, stdout=subprocess.PIPE, universal_newlines=True)
            print(response.stdout)
        except subprocess.CalledProcessError as e:
            print(f"Error executing the command: {e}")