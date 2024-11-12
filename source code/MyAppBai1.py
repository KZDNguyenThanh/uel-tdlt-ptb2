from PyQt6.QtWidgets import QApplication, QMainWindow

from bai1_ext import bai1_ext

app=QApplication([])

qMainWindow=QMainWindow()

myWindow=bai1_ext()

myWindow.setupUi(qMainWindow)

qMainWindow.show()

app.exec()
