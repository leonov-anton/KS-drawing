import sys
# from Calcul import *
from KSD_gui import *
from PyQt5.QtWidgets import QMainWindow, QDialog, QApplication, QFileDialog
from pyautocad import Autocad, APoint, aDouble
import math


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.K = float()
        self.alpha = float()

        self.show()

        self.ui.drawing_btn.clicked.connect(self.web_A3)
        self.ui.drawing_btn.clicked.connect(self.IEC)
        self.ui.drawing_btn.clicked.connect(self.fuse)

        self.ui.IEC_A.toggled.connect(self.IEC_A)
        self.ui.IEC_B.toggled.connect(self.IEC_B)
        self.ui.IEC_C.toggled.connect(self.IEC_C)

    def web_A3(self):
        if self.ui.wed_draw.isChecked():
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

        else:
            pass

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
        if self.K and self.alpha and self.ui.Imtz_edit.text() and self.ui.TMS_edit.text():
            Imtz = float(self.ui.Imtz_edit.text().replace(',', '.'))
            TMS = float(self.ui.TMS_edit.text().replace(',', '.'))
            try:
                Ito = float(self.ui.Ito_edit.text().replace(',', '.'))
                Tto = float(self.ui.Tto_edit.text().replace(',', '.'))

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

                print('Полная')

            except:
                Ir = [((TMS * self.K/10000)+1) ** (1/self.alpha), 1.01, 1.05, 1.1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 960/Imtz]
                IEC = aDouble()
                startTan = aDouble(0, 0, 0)
                endTan = aDouble(0, 0, 0)
                a = (0 - 360) / (math.log(1) - math.log(24000))
                b = 360 - a * math.log(24000)
                c = (0 - 180) / (math.log(0.01) - math.log(10000))
                d = 180 - c * math.log(10000)
                for I in Ir:
                    It = Imtz * I
                    IEC.append(It * 25 * 0.015)
                    Tt = TMS * self.K / ((I ** self.alpha) - 1)
                    IEC.append(c * math.log(Tt) + d)
                    IEC.append(0)

                rza_mtz = acad.model.AddSpline(IEC, startTan, endTan)
                rza_mtz.color = 94
                rza_mtz.Lineweight = 100

                print('Обрезанная')

        else:
            pass

    def fuse(self):
        a = (0 - 360) / (math.log(1) - math.log(24000))
        b = 360 - a * math.log(24000)
        c = (0 - 180) / (math.log(0.01) - math.log(10000))
        d = 180 - c * math.log(10000)
        fuse_func = aDouble()
        startTan = aDouble(0, 0, 0)
        endTan = aDouble(0, 0, 0)

        if self.ui.ppn_1250.isChecked():
            fuse_func = aDouble()
            startTan = aDouble(0, 0, 0)
            endTan = aDouble(0, 0, 0)
            ppn = ([67000, 0.01], [60000, 0.016], [50000, 0.03], [40000, 0.07], [30000, 0.2], [20000, 1], [10000, 16],
                   [9000, 20], [8000, 31], [7000, 50], [6000, 86], [5000, 180], [4000, 445], [3000, 1850], [2330.0, 10000])
            for i in ppn:
                fuse_func.append(i[0] * 0.015)
                fuse_func.append(c * math.log(i[1]) + d)
                fuse_func.append(0)

            fuse_f = acad.model.AddSpline(fuse_func, startTan, endTan)
            fuse_f.color = 30
            fuse_f.Lineweight = 100

        if self.ui.ppn_1000.isChecked():
            fuse_func = aDouble()
            startTan = aDouble(0, 0, 0)
            endTan = aDouble(0, 0, 0)
            ppn = ([50000, 0.01], [40000, 0.02], [30000, 0.05], [20000, 0.17], [10000, 3.3], [9000, 4.7], [8000, 7],
                   [7000, 12], [6000, 20], [5000, 40], [4000, 90], [3000, 300], [2000, 2800], [1700.0, 10000])
            for i in ppn:
                fuse_func.append(i[0] * 0.015)
                fuse_func.append(c * math.log(i[1]) + d)
                fuse_func.append(0)

            fuse_f = acad.model.AddSpline(fuse_func, startTan, endTan)
            fuse_f.color = 30
            fuse_f.Lineweight = 100

        if self.ui.ppn_800.isChecked():
            fuse_func = aDouble()
            startTan = aDouble(0, 0, 0)
            endTan = aDouble(0, 0, 0)
            ppn = ([37500.0, 0.01], [30000, 0.024], [20000, 0.1], [10000, 1.5], [9000, 2.3], [8000, 3.7], [7000, 6],
                   [6000, 11.5], [5000, 25], [4000, 60], [3000, 200], [2000, 1550], [1520.0, 10000])
            for i in ppn:
                fuse_func.append(i[0] * 0.015)
                fuse_func.append(c * math.log(i[1]) + d)
                fuse_func.append(0)

            fuse_f = acad.model.AddSpline(fuse_func, startTan, endTan)
            fuse_f.color = 30
            fuse_f.Lineweight = 100

        if self.ui.ppn_630.isChecked():
            fuse_func = aDouble()
            startTan = aDouble(0, 0, 0)
            endTan = aDouble(0, 0, 0)
            ppn = ([30000, 0.01], [20000, 0.0325], [10000, 0.31], [9000, 0.445], [8000, 0.66], [7000, 1.1], [6000, 2],
                   [5000, 4.3], [4000, 11], [3000, 42], [2000, 300], [1070.0, 10000])
            for i in ppn:
                fuse_func.append(i[0] * 0.015)
                fuse_func.append(c * math.log(i[1]) + d)
                fuse_func.append(0)

            fuse_f = acad.model.AddSpline(fuse_func, startTan, endTan)
            fuse_f.color = 30
            fuse_f.Lineweight = 100

        if self.ui.ppn_500.isChecked():
            fuse_func = aDouble()
            startTan = aDouble(0, 0, 0)
            endTan = aDouble(0, 0, 0)
            ppn = ([20000, 0.01], [10000, 0.14], [9000, 0.2], [8000, 0.3], [7000, 0.5], [6000, 0.875], [5000, 1.99],
                   [4000, 5], [3000, 20], [2000, 119], [1000, 4600], [900.0, 10000])
            for i in ppn:
                fuse_func.append(i[0] * 0.015)
                fuse_func.append(c * math.log(i[1]) + d)
                fuse_func.append(0)

            fuse_f = acad.model.AddSpline(fuse_func, startTan, endTan)
            fuse_f.color = 30
            fuse_f.Lineweight = 100

        if self.ui.ppn_400.isChecked():
            fuse_func = aDouble()
            startTan = aDouble(0, 0, 0)
            endTan = aDouble(0, 0, 0)
            ppn = ([16300.0, 0.01], [10000, 0.05], [9000, 0.07], [8000, 0.106], [7000, 0.175], [6000, 0.3],
                   [5000, 0.58], [4000, 1.45], [3000, 3.95], [2000, 18], [1000, 700], [900.0, 1000], [800.0, 2000],
                   [680.0, 10000])
            for i in ppn:
                fuse_func.append(i[0] * 0.015)
                fuse_func.append(c * math.log(i[1]) + d)
                fuse_func.append(0)

            fuse_f = acad.model.AddSpline(fuse_func, startTan, endTan)
            fuse_f.color = 30
            fuse_f.Lineweight = 100

        if self.ui.ppn_315.isChecked():
            fuse_func = aDouble()
            startTan = aDouble(0, 0, 0)
            endTan = aDouble(0, 0, 0)
            ppn = ([12000.0, 0.01], [10000, 0.017], [9000, 0.024], [8000, 0.036], [7000, 0.06], [6000, 0.1],
                   [5000, 0.2], [4000, 0.5], [3000, 1.75], [2000, 10], [1000, 300], [900.0, 500], [800.0, 900],
                   [700.0, 1850], [600.0, 5000], [550.0, 10000])
            for i in ppn:
                fuse_func.append(i[0] * 0.015)
                fuse_func.append(c * math.log(i[1]) + d)
                fuse_func.append(0)

            fuse_f = acad.model.AddSpline(fuse_func, startTan, endTan)
            fuse_f.color = 30
            fuse_f.Lineweight = 100

        if self.ui.ppn_250.isChecked():
            fuse_func = aDouble()
            startTan = aDouble(0, 0, 0)
            endTan = aDouble(0, 0, 0)
            ppn = ([9000, 0.01], [8000, 0.016], [7000, 0.024], [6000, 0.04], [5000, 0.07], [4000, 0.15], [3000, 0.4],
                   [2000, 2], [1000, 56], [900.0, 90], [800.0, 152], [700.0, 260], [600.0, 500], [500.0, 1400],
                   [400.0, 10000])
            for i in ppn:
                fuse_func.append(i[0] * 0.015)
                fuse_func.append(c * math.log(i[1]) + d)
                fuse_func.append(0)

            fuse_f = acad.model.AddSpline(fuse_func, startTan, endTan)
            fuse_f.color = 30
            fuse_f.Lineweight = 100

        if self.ui.ppn_200.isChecked():
            fuse_func = aDouble()
            startTan = aDouble(0, 0, 0)
            endTan = aDouble(0, 0, 0)
            ppn = ([6520.0, 0.01], [6000, 0.014], [5000, 0.026], [4000, 0.06], [3000, 0.2], [2000, 1.3], [1000, 23.5],
                   [900.0, 40], [800.0, 70], [700.0, 140], [600.0, 280], [500.0, 600], [400.0, 2000], [345.0, 10000])
            for i in ppn:
                fuse_func.append(i[0] * 0.015)
                fuse_func.append(c * math.log(i[1]) + d)
                fuse_func.append(0)

            fuse_f = acad.model.AddSpline(fuse_func, startTan, endTan)
            fuse_f.color = 30
            fuse_f.Lineweight = 100

        if self.ui.ppn_160.isChecked():
            fuse_func = aDouble()
            startTan = aDouble(0, 0, 0)
            endTan = aDouble(0, 0, 0)
            ppn = ([5000, 0.01], [4000, 0.022], [3000, 0.06], [2000, 0.24], [1000, 4], [900.0, 6.8], [800.0, 13],
                   [700.0, 26], [600.0, 50], [500.0, 130], [400.0, 330], [300.0, 1850], [265.0, 7000])
            for i in ppn:
                fuse_func.append(i[0] * 0.015)
                fuse_func.append(c * math.log(i[1]) + d)
                fuse_func.append(0)

            fuse_f = acad.model.AddSpline(fuse_func, startTan, endTan)
            fuse_f.color = 30
            fuse_f.Lineweight = 100

        if self.ui.ppn_125.isChecked():
            ppn = ([3700.0, 0.01], [3000, 0.023], [2000, 0.1], [1000, 2], [900.0, 3], [800.0, 5], [700.0, 8],
                   [600.0, 16.5], [500.0, 38], [400.0, 100], [300.0, 500], [210.0, 8000])
            for i in ppn:
                fuse_func.append(i[0] * 0.015)
                fuse_func.append(c * math.log(i[1]) + d)
                fuse_func.append(0)

            fuse_f = acad.model.AddSpline(fuse_func, startTan, endTan)
            fuse_f.color = 30
            fuse_f.Lineweight = 100

        pass

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ex = MainWindow()
    acad = Autocad(create_if_not_exists=True)
    sys.exit(app.exec_())