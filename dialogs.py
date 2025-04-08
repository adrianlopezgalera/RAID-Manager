import sys
from PyQt6.QtWidgets import QApplication, QMessageBox

class Dialogs(QMessageBox):
    def __init__(self, parent=None):
        super().__init__(parent)
    
    def new_dialog(self, window_title, text, icon=None, buttons=None):
        self.setWindowTitle(window_title)
        self.setText(text)
        
        if icon:
            self.setIcon(icon)
        
        if buttons:
            for button in buttons:
                self.addButton(button)



if __name__ == '__main__':
    app = QApplication([])

    message_box = Dialogs()
    message_box.new_dialog("hola","Hello, this is a custom message box!",
                               QMessageBox.Icon.Information,
                               [QMessageBox.StandardButton.Ok, QMessageBox.StandardButton.Cancel])


    message_box.exec()

    sys.exit(app.exec())