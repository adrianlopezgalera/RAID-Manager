import subprocess

class EventsManager:

    @staticmethod
    def run_command(*args, **kwargs):
        try:
            return subprocess.run(*args, **kwargs)
        except subprocess.CalledProcessError as e:
            print(f"Error executing the command: {e}")
    @staticmethod
    def read_output(command):
        try:
            response = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, universal_newlines=True)
            print(response.stdout)
        except subprocess.CalledProcessError as e:
            print(f"Error executing the command: {e}")

    @staticmethod
    def new_window(self):
        self.show()

    @staticmethod
    def action(**kwargs):
        subprocess.run('mdadm ' + kwargs)
