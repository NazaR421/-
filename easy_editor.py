from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QVBoxLayout, \
    QHBoxLayout, QApplication, QListWidget

app = QApplication([])

editor_window = QWidget()
editor_window.setWindowTitle("Easy Editor")
editor_window.resize(900, 600)

btn_left = QPushButton("Вліво")
btn_right = QPushButton("Вправо")
btn_mirror = QPushButton("Дзеркало")
btn_sharpness = QPushButton("Різкість")
btn_gray = QPushButton("Ч/Б")
btn_folder = QPushButton("Папка")
list_photo = QListWidget()
photo = QLabel("")

layout_list = QVBoxLayout()
layout_list.addWidget(btn_folder)
layout_list.addWidget(list_photo)

layout_photo = QVBoxLayout()
layout_photo.addWidget(photo)

layout_btn = QHBoxLayout()
layout_btn.addWidget(btn_left)
layout_btn.addWidget(btn_right)
layout_btn.addWidget(btn_mirror)
layout_btn.addWidget(btn_sharpness)
layout_btn.addWidget(btn_gray)

layout_main = QHBoxLayout()

layout_photo.addLayout(layout_btn)
layout_main.addLayout(layout_list, 20)
layout_main.addLayout(layout_photo, 80)

editor_window.setLayout(layout_main)
editor_window.show()
app.exec_()
