import sys
# from Calcul import *
from KG_gui import *
from PyQt5.QtWidgets import QMainWindow, QDialog, QApplication, QFileDialog
from pyautocad import Autocad, APoint, aDouble
import math


class MainWindow(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        # self.fname = ''
        self.K = float()
        self.alpha = float()

        self.show()

        # self.ui.brows.clicked.connect(self.browse_file)
        self.ui.drawing_btn.clicked.connect(self.web_A3)
        # self.ui.drawing_btn.clicked.connect(self.IEC)

        self.ui.IEC_A.toggled.connect(self.IEC_A)
        self.ui.IEC_B.toggled.connect(self.IEC_B)
        self.ui.IEC_C.toggled.connect(self.IEC_C)

    # def browse_file(self):
    #     self.fname = QFileDialog.getOpenFileName(self, "Выбор файла", 'D:\\', '*.dwg')
    #     self.ui.filename.setText(self.fname[0])

    def web_A3(self):
        # acad = Autocad()
        a = (0 - 360) / (math.log(1) - math.log(24000))
        b = 360 - a * math.log(24000)
        c = (0 - 180) / (math.log(0.01) - math.log(10000))
        d = 180 - c * math.log(10000)

        pi = APoint(a * math.log(24000) + b + 2, 3)
        pt = APoint(-2, c * math.log(10000) + d + 5)
        text_i = acad.model.AddMText(pi, 2, "I(A)")
        text_i.styleName = "ГОСТ"
        text_t = acad.model.AddMText(pt, 2, "t(sec)")
        text_t.styleName = "ГОСТ"

        y = 0.01
        for i in range(10):
            pt1 = APoint(0, c * math.log(y) + d)
            pt2 = APoint(a * math.log(24000) + b, c * math.log(y) + d)
            ptext = APoint(-5, c * math.log(y) + d)
            line = acad.model.AddLine(pt1, pt2)
            if i == 9 or i == 0:
                line.Lineweight = 30
                text = acad.model.AddMText(ptext, 2, y)
                text.styleName = "ГОСТ"
            y += 0.01

        y = 0.2
        for i in range(9):
            pt1 = APoint(0, c * math.log(y) + d)
            pt2 = APoint(a * math.log(24000) + b, c * math.log(y) + d)
            ptext = APoint(-3, c * math.log(y) + d)
            line = acad.model.AddLine(pt1, pt2)
            if i == 8:
                line.Lineweight = 30
                text = acad.model.AddMText(ptext, 2, y)
                text.styleName = "ГОСТ"
            y += 0.1

        y = 2
        for i in range(9):
            pt1 = APoint(0, c * math.log(y) + d)
            pt2 = APoint(a * math.log(24000) + b, c * math.log(y) + d)
            ptext = APoint(-4, c * math.log(y) + d)
            line = acad.model.AddLine(pt1, pt2)
            if i == 8:
                line.Lineweight = 30
                text = acad.model.AddMText(ptext, 2, y)
                text.styleName = "ГОСТ"
            y += 1

        y = 20
        for i in range(9):
            pt1 = APoint(0, c * math.log(y) + d)
            pt2 = APoint(a * math.log(24000) + b, c * math.log(y) + d)
            ptext = APoint(-5, c * math.log(y) + d)
            line = acad.model.AddLine(pt1, pt2)
            if i == 8:
                line.Lineweight = 30
                text = acad.model.AddMText(ptext, 2, y)
                text.styleName = "ГОСТ"
            y += 10

        y = 200
        for i in range(9):
            pt1 = APoint(0, c * math.log(y) + d)
            pt2 = APoint(a * math.log(24000) + b, c * math.log(y) + d)
            ptext = APoint(-6, c * math.log(y) + d)
            line = acad.model.AddLine(pt1, pt2)
            if i == 8:
                line.Lineweight = 30
                text = acad.model.AddMText(ptext, 2, y)
                text.styleName = "ГОСТ"
            y += 100

        y = 2000
        for i in range(9):
            pt1 = APoint(0, c * math.log(y) + d)
            pt2 = APoint(a * math.log(24000) + b, c * math.log(y) + d)
            ptext = APoint(-7, c * math.log(y) + d)
            line = acad.model.AddLine(pt1, pt2)
            if i == 8:
                line.Lineweight = 30
                text = acad.model.AddMText(ptext, 2, y)
                text.styleName = "ГОСТ"
            y += 1000

        x = 0
        y = 1000
        for i in range(49):
            pt1 = APoint(x, 0)
            pt2 = APoint(x, c * math.log(10000) + d)
            line = acad.model.AddLine(pt1, pt2)
            if x % 5 == 0:
                line.Lineweight = 30
                if y / 2 - 500 != 0:
                    point_text = APoint(x - 2, -1)
                    text = acad.model.AddMText(point_text, 2, y / 2 - 500)
                    text.styleName = "ГОСТ"
            x += 7.5
            y += 1000

    def IEC_A(self):
        self.K = 0.14
        self.alpha = 0.02

    def IEC_B(self):
        self.K = 13.5
        self.alpha = 1

    def IEC_C(self):
        self.K = 80
        self.alpha = 2

    def IEC(self):
        Imtz = float(self.ui.Imtz_edit.text().replace(',', '.'))
        Ito = float(self.ui.Ito_edit.text().replace(',', '.'))
        Tto = float(self.ui.Tto_edit.text().replace(',', '.'))
        TMS = float(self.ui.TMS_edit.text().replace(',', '.'))
        # acad = Autocad()
        a = (0 - 360) / (math.log(1) - math.log(24000))
        b = 360 - a * math.log(24000)
        c = (0 - 180) / (math.log(0.01) - math.log(10000))
        d = 180 - c * math.log(10000)

        Ir = [1.01, 1.05, 1.1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, Ito / Imtz]
        IEC = aDouble()
        startTan = aDouble(0, 0, 0)
        endTan = aDouble(0, 0, 0)
        for I in Ir:
            if I <= Ito / Imtz:
                It = Imtz * I
                IEC.append(It * 25 * 0.015)
                Tt = TMS * self.K / ((I ** self.alpha) - 1)
                IEC.append(c * math.log(Tt) + d)
                IEC.append(0)

        TO = aDouble()

        TO.append(Ito * 25 * 0.015)
        Tto0 = TMS * self.K / (((Ito / Imtz) ** self.alpha) - 1)
        TO.append(c * math.log(Tto0) + d)
        TO.append(0)

        TO.append(Ito * 25 * 0.015)
        TO.append(c * math.log(Tto) + d)
        TO.append(0)

        TO.append(a * math.log(24000) + b)
        TO.append(c * math.log(Tto) + d)
        TO.append(0)

        rza_mtz = acad.model.AddSpline(IEC, startTan, endTan)
        rza_mtz.color = 94
        rza_mtz.Lineweight = 100

        rza_to = acad.model.AddPolyLine(TO)
        rza_to.color = 94
        rza_to.Lineweight = 100


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ex = MainWindow()
    acad = Autocad(create_if_not_exists=True)
    sys.exit(app.exec_())