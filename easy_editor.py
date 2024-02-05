from PyQt5.QtCore import Qt
import os
from PyQt5.QtWidgets import( QWidget, QPushButton, QLabel, QVBoxLayout, \
    QHBoxLayout, QApplication, QListWidget,QFileDialog
)
from Pil import ImageFilter,Image
from PyQt5.QtGui import QPixmap                 


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
photo = QLabel("Тут буде картинка")

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

workdir=""

def choooseWorkdir():
    global workdir
    workdir=QFileDialog.getExistingDirectory()

def filter(files,extensions):
    result=[]
    for filename in files:
        for ext in extensions:
            if filename.endswith(ext):
                result.append(filename)
    return result

def showFilenamesList():
    global workdir
    extensions=[".jpg",".jpeg",".png",".gif"]
    choooseWorkdir()
    files=os.listdir(workdir)
    filenames= filter(os.listdir(workdir),extensions)
    list_photo.clear()
    for filename in filenames:
        list_photo.addItem(filename)
btn_folder.clicked.connect(showFilenamesList)


class ImageProcessor():
    def __init__(self):
        self.image=None
        self.dir=None
        self.filename=None
        self.save_dir="Mified/"
    def LoadImage(self,dir,filename):
        self.dir=dir
        self.filename=filename
        image_path=os.path.join(dir,filename)
        self.image = Image.open(image_path)
    def showImage(self,path):
        photo.hide()
        pixmapimage=QPixmap(path)
        w,h=photo.width(),photo.height()
        pixmapimage=pixmapimage.scaled(w,h,Qt.KeepAspectRatio)
        photo.setPixmap(pixmapimage)
        photo.show()



editor_window.show()
app.exec_()
