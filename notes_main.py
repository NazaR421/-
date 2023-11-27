from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QPushButton,QSpinBox, QLabel, QVBoxLayout,QRadioButton,\
    QHBoxLayout,QButtonGroup,QGroupBox,QApplication,QLineEdit,QListWidget,QTextEdit,QLineEdit

app=QApplication([])

notes_window=QWidget()
notes_window.setWindowTitle("Розумні замітки")
notes_window.resize(900,600)



list_notes_label=QLabel("Список заміток")
list_notes=QListWidget()
button_note_create=QPushButton("Створити замітку")
button_note_del=QPushButton("Видалити замітку")
button_note_save=QPushButton("Зберегти зміну")
field_text=QTextEdit()
list_tags_label=QLabel("Список тегів")
list_tags=QListWidget()
field_tag=QLineEdit()
field_tag.setPlaceholderText("Введіть тег... ")
button_tag_add=QPushButton("Додати до замітки")
button_tag_del=QPushButton("Відкріпіти від замітки")
button_tag_search=QPushButton("Шукати замітку по тегу")
