from PyQt6.QtWidgets import QApplication, QMessageBox

class Notifications(QMessageBox):
    def __init__(self, parent=None):
        super().__init__(parent)

    def new_dialog(self, title, text, icon, buttons):
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
