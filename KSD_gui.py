# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'KSD_gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.WindowModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(468, 348)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.wed_draw = QtWidgets.QCheckBox(self.centralwidget)
        self.wed_draw.setGeometry(QtCore.QRect(330, 210, 81, 20))
        self.wed_draw.setTabletTracking(False)
        self.wed_draw.setCheckable(True)
        self.wed_draw.setChecked(True)
        self.wed_draw.setTristate(False)
        self.wed_draw.setObjectName("wed_draw")
        self.drawing_btn = QtWidgets.QPushButton(self.centralwidget)
        self.drawing_btn.setGeometry(QtCore.QRect(360, 270, 75, 25))
        self.drawing_btn.setObjectName("drawing_btn")
        self.RZ = QtWidgets.QFrame(self.centralwidget)
        self.RZ.setGeometry(QtCore.QRect(160, 10, 160, 291))
        self.RZ.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.RZ.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.RZ.setLineWidth(1)
        self.RZ.setObjectName("RZ")
        self.IEC_A = QtWidgets.QRadioButton(self.RZ)
        self.IEC_A.setGeometry(QtCore.QRect(10, 45, 82, 17))
        self.IEC_A.setObjectName("IEC_A")
        self.IEC_B = QtWidgets.QRadioButton(self.RZ)
        self.IEC_B.setGeometry(QtCore.QRect(10, 65, 82, 17))
        self.IEC_B.setObjectName("IEC_B")
        self.IEC_C = QtWidgets.QRadioButton(self.RZ)
        self.IEC_C.setGeometry(QtCore.QRect(10, 85, 82, 17))
        self.IEC_C.setObjectName("IEC_C")
        self.label = QtWidgets.QLabel(self.RZ)
        self.label.setGeometry(QtCore.QRect(10, 25, 111, 16))
        self.label.setObjectName("label")
        self.Imtz_edit = QtWidgets.QLineEdit(self.RZ)
        self.Imtz_edit.setGeometry(QtCore.QRect(70, 45, 51, 20))
        self.Imtz_edit.setObjectName("Imtz_edit")
        self.label_2 = QtWidgets.QLabel(self.RZ)
        self.label_2.setGeometry(QtCore.QRect(130, 45, 91, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.RZ)
        self.label_3.setGeometry(QtCore.QRect(130, 70, 91, 16))
        self.label_3.setObjectName("label_3")
        self.TMS_edit = QtWidgets.QLineEdit(self.RZ)
        self.TMS_edit.setGeometry(QtCore.QRect(70, 70, 51, 20))
        self.TMS_edit.setObjectName("TMS_edit")
        self.label_4 = QtWidgets.QLabel(self.RZ)
        self.label_4.setGeometry(QtCore.QRect(70, 170, 91, 16))
        self.label_4.setObjectName("label_4")
        self.Tto_edit = QtWidgets.QLineEdit(self.RZ)
        self.Tto_edit.setGeometry(QtCore.QRect(10, 195, 51, 20))
        self.Tto_edit.setObjectName("Tto_edit")
        self.label_5 = QtWidgets.QLabel(self.RZ)
        self.label_5.setGeometry(QtCore.QRect(70, 195, 91, 16))
        self.label_5.setObjectName("label_5")
        self.Ito_edit = QtWidgets.QLineEdit(self.RZ)
        self.Ito_edit.setGeometry(QtCore.QRect(10, 170, 51, 20))
        self.Ito_edit.setObjectName("Ito_edit")
        self.IEC_ = QtWidgets.QRadioButton(self.RZ)
        self.IEC_.setGeometry(QtCore.QRect(10, 105, 82, 17))
        self.IEC_.setObjectName("IEC_")
        self.label_7 = QtWidgets.QLabel(self.RZ)
        self.label_7.setGeometry(QtCore.QRect(10, 130, 111, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.RZ)
        self.label_8.setGeometry(QtCore.QRect(10, -5, 131, 31))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.RZ)
        self.label_9.setGeometry(QtCore.QRect(10, 145, 121, 16))
        self.label_9.setObjectName("label_9")
        self.label_17 = QtWidgets.QLabel(self.RZ)
        self.label_17.setGeometry(QtCore.QRect(10, 225, 111, 16))
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.RZ)
        self.label_18.setGeometry(QtCore.QRect(10, 240, 121, 16))
        self.label_18.setObjectName("label_18")
        self.I0to_edit = QtWidgets.QLineEdit(self.RZ)
        self.I0to_edit.setGeometry(QtCore.QRect(10, 265, 51, 20))
        self.I0to_edit.setObjectName("I0to_edit")
        self.label_19 = QtWidgets.QLabel(self.RZ)
        self.label_19.setGeometry(QtCore.QRect(70, 265, 91, 16))
        self.label_19.setObjectName("label_19")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 10, 131, 151))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setObjectName("frame")
        self.ppn_250 = QtWidgets.QCheckBox(self.frame)
        self.ppn_250.setGeometry(QtCore.QRect(10, 110, 70, 17))
        self.ppn_250.setObjectName("ppn_250")
        self.ppn_315 = QtWidgets.QCheckBox(self.frame)
        self.ppn_315.setGeometry(QtCore.QRect(10, 130, 70, 17))
        self.ppn_315.setObjectName("ppn_315")
        self.ppn_400 = QtWidgets.QCheckBox(self.frame)
        self.ppn_400.setGeometry(QtCore.QRect(70, 30, 70, 17))
        self.ppn_400.setObjectName("ppn_400")
        self.ppn_500 = QtWidgets.QCheckBox(self.frame)
        self.ppn_500.setGeometry(QtCore.QRect(70, 50, 70, 17))
        self.ppn_500.setObjectName("ppn_500")
        self.ppn_630 = QtWidgets.QCheckBox(self.frame)
        self.ppn_630.setGeometry(QtCore.QRect(70, 70, 70, 17))
        self.ppn_630.setObjectName("ppn_630")
        self.ppn_800 = QtWidgets.QCheckBox(self.frame)
        self.ppn_800.setGeometry(QtCore.QRect(70, 90, 70, 17))
        self.ppn_800.setObjectName("ppn_800")
        self.ppn_1000 = QtWidgets.QCheckBox(self.frame)
        self.ppn_1000.setGeometry(QtCore.QRect(70, 110, 70, 17))
        self.ppn_1000.setObjectName("ppn_1000")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(10, 5, 111, 16))
        self.label_6.setTextFormat(QtCore.Qt.AutoText)
        self.label_6.setScaledContents(False)
        self.label_6.setObjectName("label_6")
        self.ppn_200 = QtWidgets.QCheckBox(self.frame)
        self.ppn_200.setGeometry(QtCore.QRect(10, 90, 70, 17))
        self.ppn_200.setObjectName("ppn_200")
        self.ppn_125 = QtWidgets.QCheckBox(self.frame)
        self.ppn_125.setGeometry(QtCore.QRect(10, 50, 70, 17))
        self.ppn_125.setObjectName("ppn_125")
        self.ppn_160 = QtWidgets.QCheckBox(self.frame)
        self.ppn_160.setGeometry(QtCore.QRect(10, 70, 70, 17))
        self.ppn_160.setObjectName("ppn_160")
        self.ppn_1250 = QtWidgets.QCheckBox(self.frame)
        self.ppn_1250.setGeometry(QtCore.QRect(70, 130, 70, 17))
        self.ppn_1250.setObjectName("ppn_1250")
        self.ppn_100 = QtWidgets.QCheckBox(self.frame)
        self.ppn_100.setGeometry(QtCore.QRect(10, 30, 70, 17))
        self.ppn_100.setObjectName("ppn_100")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(20, 170, 131, 131))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_2.setObjectName("frame_2")
        self.label_10 = QtWidgets.QLabel(self.frame_2)
        self.label_10.setGeometry(QtCore.QRect(10, 5, 47, 13))
        self.label_10.setObjectName("label_10")
        self.pkt_10 = QtWidgets.QCheckBox(self.frame_2)
        self.pkt_10.setGeometry(QtCore.QRect(10, 30, 70, 17))
        self.pkt_10.setObjectName("pkt_10")
        self.pkt_16 = QtWidgets.QCheckBox(self.frame_2)
        self.pkt_16.setGeometry(QtCore.QRect(10, 50, 70, 17))
        self.pkt_16.setObjectName("pkt_16")
        self.pkt_20 = QtWidgets.QCheckBox(self.frame_2)
        self.pkt_20.setGeometry(QtCore.QRect(10, 70, 70, 17))
        self.pkt_20.setObjectName("pkt_20")
        self.pkt_31_5 = QtWidgets.QCheckBox(self.frame_2)
        self.pkt_31_5.setGeometry(QtCore.QRect(10, 90, 70, 17))
        self.pkt_31_5.setObjectName("pkt_31_5")
        self.pkt_40 = QtWidgets.QCheckBox(self.frame_2)
        self.pkt_40.setGeometry(QtCore.QRect(70, 30, 70, 17))
        self.pkt_40.setObjectName("pkt_40")
        self.pkt_50 = QtWidgets.QCheckBox(self.frame_2)
        self.pkt_50.setGeometry(QtCore.QRect(70, 50, 70, 17))
        self.pkt_50.setObjectName("pkt_50")
        self.pkt_80 = QtWidgets.QCheckBox(self.frame_2)
        self.pkt_80.setGeometry(QtCore.QRect(70, 70, 70, 17))
        self.pkt_80.setObjectName("pkt_80")
        self.pkt_100 = QtWidgets.QCheckBox(self.frame_2)
        self.pkt_100.setGeometry(QtCore.QRect(70, 90, 70, 17))
        self.pkt_100.setObjectName("pkt_100")
        self.pkt_160 = QtWidgets.QCheckBox(self.frame_2)
        self.pkt_160.setGeometry(QtCore.QRect(40, 110, 70, 17))
        self.pkt_160.setObjectName("pkt_160")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(330, 10, 121, 91))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_3.setObjectName("frame_3")
        self.label_11 = QtWidgets.QLabel(self.frame_3)
        self.label_11.setGeometry(QtCore.QRect(10, 5, 47, 13))
        self.label_11.setObjectName("label_11")
        self.I1_edit = QtWidgets.QLineEdit(self.frame_3)
        self.I1_edit.setGeometry(QtCore.QRect(10, 30, 51, 20))
        self.I1_edit.setText("")
        self.I1_edit.setObjectName("I1_edit")
        self.label_12 = QtWidgets.QLabel(self.frame_3)
        self.label_12.setGeometry(QtCore.QRect(70, 60, 91, 16))
        self.label_12.setObjectName("label_12")
        self.T1_edit = QtWidgets.QLineEdit(self.frame_3)
        self.T1_edit.setGeometry(QtCore.QRect(10, 60, 51, 20))
        self.T1_edit.setText("")
        self.T1_edit.setObjectName("T1_edit")
        self.label_13 = QtWidgets.QLabel(self.frame_3)
        self.label_13.setGeometry(QtCore.QRect(70, 30, 91, 16))
        self.label_13.setObjectName("label_13")
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setGeometry(QtCore.QRect(330, 110, 121, 91))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_4.setObjectName("frame_4")
        self.label_14 = QtWidgets.QLabel(self.frame_4)
        self.label_14.setGeometry(QtCore.QRect(10, 10, 47, 13))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.frame_4)
        self.label_15.setGeometry(QtCore.QRect(70, 60, 91, 16))
        self.label_15.setObjectName("label_15")
        self.T4_edit = QtWidgets.QLineEdit(self.frame_4)
        self.T4_edit.setGeometry(QtCore.QRect(10, 60, 51, 20))
        self.T4_edit.setText("")
        self.T4_edit.setObjectName("T4_edit")
        self.label_16 = QtWidgets.QLabel(self.frame_4)
        self.label_16.setGeometry(QtCore.QRect(70, 30, 91, 16))
        self.label_16.setObjectName("label_16")
        self.I4_edit = QtWidgets.QLineEdit(self.frame_4)
        self.I4_edit.setGeometry(QtCore.QRect(10, 30, 51, 20))
        self.I4_edit.setText("")
        self.I4_edit.setObjectName("I4_edit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 468, 21))
        self.menubar.setObjectName("menubar")
        self.menufile = QtWidgets.QMenu(self.menubar)
        self.menufile.setObjectName("menufile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menufile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.wed_draw.setText(_translate("MainWindow", "Разметка"))
        self.drawing_btn.setText(_translate("MainWindow", "Построить"))
        self.IEC_A.setText(_translate("MainWindow", "IEC/A"))
        self.IEC_B.setText(_translate("MainWindow", "IEC/B"))
        self.IEC_C.setText(_translate("MainWindow", "IEC/C"))
        self.label.setText(_translate("MainWindow", "Тип кривой МТЗ:"))
        self.label_2.setText(_translate("MainWindow", "I>"))
        self.label_3.setText(_translate("MainWindow", "TMS"))
        self.label_4.setText(_translate("MainWindow", "I>>"))
        self.label_5.setText(_translate("MainWindow", "T>>"))
        self.IEC_.setText(_translate("MainWindow", "IEC"))
        self.label_7.setText(_translate("MainWindow", "Парамерты ТО"))
        self.label_8.setText(_translate("MainWindow", "Парамерты цифровой РЗА:"))
        self.label_9.setText(_translate("MainWindow", "с выдержкой времени:"))
        self.label_17.setText(_translate("MainWindow", "Парамерты ТО"))
        self.label_18.setText(_translate("MainWindow", "без выдержки времени:"))
        self.label_19.setText(_translate("MainWindow", "I0>>"))
        self.ppn_250.setText(_translate("MainWindow", "250 A"))
        self.ppn_315.setText(_translate("MainWindow", "315 A"))
        self.ppn_400.setText(_translate("MainWindow", "400 A"))
        self.ppn_500.setText(_translate("MainWindow", "500 A"))
        self.ppn_630.setText(_translate("MainWindow", "630 A"))
        self.ppn_800.setText(_translate("MainWindow", "800 A"))
        self.ppn_1000.setText(_translate("MainWindow", "1000 A"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p>ППН 0,4 кВ:</p></body></html>"))
        self.ppn_200.setText(_translate("MainWindow", "200 A"))
        self.ppn_125.setText(_translate("MainWindow", "125 A"))
        self.ppn_160.setText(_translate("MainWindow", "160 A"))
        self.ppn_1250.setText(_translate("MainWindow", "1250 A"))
        self.ppn_100.setText(_translate("MainWindow", "100 A"))
        self.label_10.setText(_translate("MainWindow", "ПКН:"))
        self.pkt_10.setText(_translate("MainWindow", "10 A"))
        self.pkt_16.setText(_translate("MainWindow", "16 A"))
        self.pkt_20.setText(_translate("MainWindow", "20 A"))
        self.pkt_31_5.setText(_translate("MainWindow", "31.5 A"))
        self.pkt_40.setText(_translate("MainWindow", "40 A"))
        self.pkt_50.setText(_translate("MainWindow", "50 A"))
        self.pkt_80.setText(_translate("MainWindow", "80 A"))
        self.pkt_100.setText(_translate("MainWindow", "100 A"))
        self.pkt_160.setText(_translate("MainWindow", "160 A"))
        self.label_11.setText(_translate("MainWindow", "РТВ-I:"))
        self.label_12.setText(_translate("MainWindow", "T"))
        self.label_13.setText(_translate("MainWindow", "I"))
        self.label_14.setText(_translate("MainWindow", "РТВ-IV:"))
        self.label_15.setText(_translate("MainWindow", "T"))
        self.label_16.setText(_translate("MainWindow", "I"))
        self.menufile.setTitle(_translate("MainWindow", "About"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
