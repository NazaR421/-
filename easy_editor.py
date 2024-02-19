from PyQt5.QtCore import Qt
import os
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QPushButton, QListWidget, QLabel, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QPixmap 
from PIL import Image
from PIL.ImageFilter import (SHARPEN)



app = QApplication([])
window = QWidget()
window.setWindowTitle("Міні-фотошоп")
window.resize(900,700)
window.move(600,300)

but_dir = QPushButton("Папка")
but_left = QPushButton("Вліво")
but_right = QPushButton("Вправо")
but_mirrow = QPushButton("Дзеркально")
but_blur = QPushButton("Різкість")
but_bw = QPushButton("Ч/Б")

lb_img = QLabel("Тут буде картинка")

list_w = QListWidget()

lineV1 = QVBoxLayout()
lineV2 = QVBoxLayout()

lineH1 = QHBoxLayout()

lineG = QHBoxLayout()

lineV1.addWidget(but_dir)
lineV1.addWidget(list_w)

lineH1.addWidget(but_left)
lineH1.addWidget(but_right)
lineH1.addWidget(but_mirrow)
lineH1.addWidget(but_blur)
lineH1.addWidget(but_bw)

lineV2.addWidget(lb_img,95)
lineV2.addLayout(lineH1)

lineG.addLayout(lineV1,20)
lineG.addLayout(lineV2,80)

window.setLayout(lineG)

def filter(files, extensions):
    result=[]
    for filename in files:
        for e in extensions:
            if filename.endswith(e):
                result.append(filename)
    return result

def chooseWorkdir():
    global workdir
    workdir = QFileDialog.getExistingDirectory()

def showFilenameList():
    extensions = ['.jpg', '.jpeg', '.png', 'gif','.bmp']
    chooseWorkdir()
    filenames = filter(os.listdir(workdir),extensions)
    list_w.clear()
    for filename in filenames:
        list_w.addItem(filename)

but_dir.clicked.connect(showFilenameList)

class ImageProcessor():
    def __init__(self):
        self.image = None
        self.dir = None
        self.filename = None
        self.save_dir = "Modified/" 

    def loadImage(self,dir,filename):
        self.dir = dir
        self.filename = filename
        image_path = os.path.join(dir, filename)
        self.image = Image.open(image_path)        

    def do_bw(self):
        self.image = self.image.convert("L")
        self.saveImage()
        image_path = os.path.join(self.dir, self.save_dir, self.filename)
        self.showImage(image_path)

    def do_left(self):
        self.image = self.image.transpose(Image.ROTATE_90)
        self.saveImage()
        image_path = os.path.join(self.dir, self.save_dir, self.filename)
        self.showImage(image_path)


    def do_right(self):
        self.image = self.image.transpose(Image.ROTATE_270)
        self.saveImage()
        image_path = os.path.join(self.dir, self.save_dir, self.filename)
        self.showImage(image_path)

    def do_mirrow(self):
        self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
        self.saveImage()
        image_path = os.path.join(self.dir, self.save_dir, self.filename)
        self.showImage(image_path)

    def do_blur(self):
        self.image = self.image.filter(SHARPEN)
        self.saveImage()
        image_path = os.path.join(self.dir, self.save_dir, self.filename)
        self.showImage(image_path)

    def saveImage(self):
        path = os.path.join(self.dir, self.save_dir)
        if not(os.path.exists(path) or os.path.isdir(path)):
            os.mkdir(path)
        image_path = os.path.join(path, self.filename)
        self.image.save(image_path)    

    def showImage(self, path):
        lb_img.hide()
        pixmapimage = QPixmap(path)
        w, h = lb_img.width(), lb_img.height()
        pixmapimage = pixmapimage.scaled(w, h, Qt.KeepAspectRatio)
        lb_img.setPixmap(pixmapimage)
        lb_img.show()
    
def showChosenImage(self):
    if list_w.currentRow() >= 0:
        filename = list_w.currentItem().text()
        workimage.loadImage(workdir, filename)
        image_path = os.path.join(workimage.dir, workimage.filename)
        workimage.showImage(image_path)

workimage = ImageProcessor()
list_w.currentRowChanged.connect(showChosenImage)

but_bw.clicked.connect(workimage.do_bw)
but_left.clicked.connect(workimage.do_left)
but_right.clicked.connect(workimage.do_right)
but_mirrow.clicked.connect(workimage.do_mirrow)

window.show()
app.exec_()
