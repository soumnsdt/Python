# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtGui import  *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(960, 700)
        MainWindow.setMinimumSize(QtCore.QSize(960, 700))
        MainWindow.setMaximumSize(QtCore.QSize(960, 700))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        # 1、通过label控件显示顶部位图
        self.label_title_img = QtWidgets.QLabel(self.centralwidget)
        self.label_title_img.setGeometry(QtCore.QRect(0, 0, 960, 141))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_title_img.setFont(font)
        self.label_title_img.setObjectName("label_title_img")
        title_img = QPixmap('img/bg1.png')
        self.label_title_img.setPixmap(title_img)
        # 2、查询部分的widget
        self.widget_query = QtWidgets.QWidget(self.centralwidget)
        self.widget_query.setGeometry(QtCore.QRect(0, 141, 960, 80))
        self.widget_query.setObjectName("widget_query")
        self.widget_query.setAutoFillBackground(True)    # 开启自动填充背景
        palette = QPalette()                             # 调色板类
        palette.setBrush(QPalette.Background, QtGui.QBrush(QtGui.QPixmap('img/bg2.png')))  # 设置背景图片
        self.widget_query.setPalette(palette)            # 为控件设置对应的调色板即可

        self.label = QtWidgets.QLabel(self.widget_query)
        self.label.setGeometry(QtCore.QRect(30, 30, 54, 12))
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(self.widget_query)
        self.textEdit.setGeometry(QtCore.QRect(80, 25, 100, 25))
        self.textEdit.setObjectName("textEdit")
        self.label_2 = QtWidgets.QLabel(self.widget_query)
        self.label_2.setGeometry(QtCore.QRect(220, 30, 54, 12))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget_query)
        self.label_3.setGeometry(QtCore.QRect(410, 30, 54, 12))
        self.label_3.setObjectName("label_3")
        self.textEdit_2 = QtWidgets.QTextEdit(self.widget_query)
        self.textEdit_2.setGeometry(QtCore.QRect(270, 25, 100, 25))
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_3 = QtWidgets.QTextEdit(self.widget_query)
        self.textEdit_3.setGeometry(QtCore.QRect(460, 25, 100, 25))
        self.textEdit_3.setObjectName("textEdit_3")
        self.pushButton = QtWidgets.QPushButton(self.widget_query)
        self.pushButton.setGeometry(QtCore.QRect(600, 25, 75, 25))
        self.pushButton.setObjectName("pushButton")
        self.widget_checkbox = QtWidgets.QWidget(self.centralwidget)
        self.widget_checkbox.setGeometry(QtCore.QRect(0, 221, 960, 50))
        self.widget_checkbox.setObjectName("widget_checkbox")
        self.label_type = QtWidgets.QLabel(self.widget_checkbox)
        self.label_type.setGeometry(QtCore.QRect(30, 20, 54, 12))
        self.label_type.setObjectName("label_type")
        self.checkBox_G = QtWidgets.QCheckBox(self.widget_checkbox)
        self.checkBox_G.setGeometry(QtCore.QRect(100, 20, 71, 16))
        self.checkBox_G.setObjectName("checkBox_G")
        self.checkBox_D = QtWidgets.QCheckBox(self.widget_checkbox)
        self.checkBox_D.setGeometry(QtCore.QRect(250, 20, 71, 16))
        self.checkBox_D.setObjectName("checkBox_D")
        self.checkBox_Z = QtWidgets.QCheckBox(self.widget_checkbox)
        self.checkBox_Z.setGeometry(QtCore.QRect(400, 20, 71, 16))
        self.checkBox_Z.setObjectName("checkBox_Z")
        self.checkBox_T = QtWidgets.QCheckBox(self.widget_checkbox)
        self.checkBox_T.setGeometry(QtCore.QRect(550, 20, 71, 16))
        self.checkBox_T.setObjectName("checkBox_T")
        self.checkBox_K = QtWidgets.QCheckBox(self.widget_checkbox)
        self.checkBox_K.setGeometry(QtCore.QRect(700, 20, 71, 16))
        self.checkBox_K.setObjectName("checkBox_K")
        self.label_train_img = QtWidgets.QLabel(self.centralwidget)
        self.label_train_img.setGeometry(QtCore.QRect(0, 271, 960, 62))
        self.label_train_img.setObjectName("label_train_img")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(0, 333, 960, 365))
        self.tableView.setObjectName("tableView")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "快手爬票"))
        self.label.setText(_translate("MainWindow", "出发地："))
        self.label_2.setText(_translate("MainWindow", "目的地："))
        self.label_3.setText(_translate("MainWindow", "出发日："))
        self.pushButton.setText(_translate("MainWindow", "查询"))
        self.label_type.setText(_translate("MainWindow", "车次类型："))
        self.checkBox_G.setText(_translate("MainWindow", "GC-高铁"))
        self.checkBox_D.setText(_translate("MainWindow", "D-动车"))
        self.checkBox_Z.setText(_translate("MainWindow", "Z-直达"))
        self.checkBox_T.setText(_translate("MainWindow", "T-特快"))
        self.checkBox_K.setText(_translate("MainWindow", "K-快速"))


def show_MainWindow():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    show_MainWindow()