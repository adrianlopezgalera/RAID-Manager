import locale
import sys
import subprocess

from PyQt6.QtGui import QBrush, QColor
from PyQt6.QtWidgets import QApplication, QGraphicsScene, QGraphicsView, QGraphicsEllipseItem, QGraphicsSimpleTextItem

# Get disk usage information using df command
df_output = subprocess.run(['df', '-h'], capture_output=True, text=True).stdout
lines = df_output.replace(",", ".").splitlines()

total_disk_space = float(lines[1].split()[1][:-1])
used_disk_space = float(lines[1].split()[2][:-1])
free_disk_space = float(lines[1].split()[3][:-1])

# Calculate angles for pie chart
total_angle = 360
used_angle = (used_disk_space / total_disk_space) * total_angle
free_angle = (free_disk_space / total_disk_space) * total_angle

# Create Qt application
app = QApplication(sys.argv)

# Create graphics scene and view
scene = QGraphicsScene()
view = QGraphicsView(scene)
view.setWindowTitle('Disk Usage')
view.resize(400, 400)

# Draw free disk space sector
free_sector = QGraphicsEllipseItem(50, 50, 300, 300)
free_sector.setStartAngle(0)
free_sector.setSpanAngle(int(free_angle * 16))
free_sector.setBrush(QBrush(QColor("lightgray")))
scene.addItem(free_sector)

# Draw used disk space sector
used_sector = QGraphicsEllipseItem(50, 50, 300, 300)
used_sector.setStartAngle(int(free_angle * 16))
used_sector.setSpanAngle(int(used_angle * 16))
used_sector.setBrush(QBrush(QColor("red")))
scene.addItem(used_sector)

# Add text labels
scene.addItem(QGraphicsSimpleTextItem(f"Free Space: {free_disk_space} GB"))
scene.addItem(QGraphicsSimpleTextItem(f"Used Space: {used_disk_space} GB"))

# Show graphical view
view.show()

sys.exit(app.exec())