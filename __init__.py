import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton
import subprocess

from click import command


class Ventana(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("RAID Manager")
        self.setGeometry(100, 100, 300, 200)

        # self.boton = QPushButton("Ejecutar comando", self)
        # self.boton.clicked.connect(lambda: self.ejecutar_comando(comando))


    def ejecutar_comando(self, comando):
        try:
            response = subprocess.run('mdadm ' + comando, shell=True, check=True, stdout=subprocess.PIPE, universal_newlines=True)
            print(response.stdout)

            # return response.stdout.decode('utf-8')
        except subprocess.CalledProcessError as e:
            print(f"Error al ejecutar el comando: {e}")

    def button_event (self, name, command):
        self.boton = QPushButton(name, self)
        self.boton.clicked.connect(lambda: self.ejecutar_comando(command))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Ventana()

    ventana.button_event("Ayuda", "--help")

    ventana.show()

    sys.exit(app.exec())