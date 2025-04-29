from PyQt6.QtWidgets import QApplication, QMessageBox

class Notifications(QMessageBox):
    def __init__(self, parent=None):
        super().__init__(parent)

    def new_notification(self, title, text, icon, buttons):
        self.setWindowTitle(title)
        self.setText(text)

        # Set icon
        if icon == "information":
            self.setIcon(QMessageBox.Icon.Information)
        elif icon == "warning":
            self.setIcon(QMessageBox.Icon.Warning)
        elif icon == "question":
            self.setIcon(QMessageBox.Icon.Question)
        elif icon == "critical":
            self.setIcon(QMessageBox.Icon.Critical)

        # Set buttons
        if "ok" in buttons:
            self.addButton(QMessageBox.StandardButton.Ok)
        if "cancel" in buttons:
            self.addButton(QMessageBox.StandardButton.Cancel)
        if "yes" in buttons:
            self.addButton(QMessageBox.StandardButton.Yes)
        if "no" in buttons:
            self.addButton(QMessageBox.StandardButton.No)

        return self.exec()

    def question_notification(self, element_name):

        return self.new_notification(title="Warning",
                                      text="Raid Manager needs to use " + element_name + " on your system to work, do you want to install it now?",
                                      icon="warning", buttons=["ok", "cancel"])

    def success_notification(self, element_name, action_name):
            self.new_notification(title="Information",
                                  text=element_name + " has been " + action_name + " correctly",
                                  icon="information", buttons=["ok"])

    def error_notification(self, element_name):
            self.new_notification(title="Error",
                                  text="It has not been possible to install " + element_name + " on yor system",
                                  icon="critical", buttons=["ok"])
