import math

from bai1 import Ui_MainWindow


class bai1_ext(Ui_MainWindow):
    def __init__(self):
        pass
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.label_x1.setText("")
        self.label_x2.setText("")
        self.label_func.setText("")
        self.pushButtoncalc.clicked.connect(self.process_calc)
        self.pushButtonreset.clicked.connect(self.process_reset)
    def process_calc(self):
        a = 0
        b = 0
        c = 0
        a = float(self.lineEditA.text()) if self.lineEditA.text() else 0
        b = float(self.lineEditB.text()) if self.lineEditB.text() else 0
        c = float(self.lineEditC.text()) if self.lineEditC.text() else 0
        if a == 0:
            if b == 0 and c == 0:
                ketqua = "Vo so nghiem"
                self.label_x1.setText(ketqua)
                self.label_x2.setText(ketqua)
            elif b == 0 and c != 0:
                ketqua ="Vo nghiem"
                self.label_x1.setText(ketqua)
                self.label_x2.setText(ketqua)
            else:
                ketqua = -c / b
                self.label_x1.setText(str(ketqua))
        else:
            delta = pow(b, 2) - 4 * a * c
            if delta < 0:
                ketqua ="Vo nghiem"
                self.label_x1.setText(ketqua)
                self.label_x2.setText(ketqua)
            elif delta == 0:
                ketqua = -b / (2 * a)
                self.label_x1.setText(ketqua)
                self.label_x2.clear()
            else:
                x1 = (-b + pow(delta,0.5)) / (2 * a)
                x2 = (-b - pow(delta,0.5)) / (2 * a)
                x1 = round(x1,2)
                x2 = round(x2,2)
                self.label_x1.setText(str(x1))
                self.label_x2.setText(str(x2))
        text = f"{a}x^2 + {b}x + {c} = 0"
        self.label_func.setText(text)
    def process_reset(self):
        self.lineEditA.setText("")
        self.lineEditB.setText("")
        self.lineEditC.setText("")
        self.lineEditA.setFocus()
        self.label_x1.setText("")
        self.label_x2.setText("")
        self.label_func.setText("")
    def show(self):
        self.MainWindow.show()


