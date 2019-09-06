# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sys      # 导入系统模块


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(960, 700)
        MainWindow.setMinimumSize(QtCore.QSize(960, 700))
        MainWindow.setMaximumSize(QtCore.QSize(960, 700))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_title_img = QtWidgets.QLabel(self.centralwidget)
        self.label_title_img.setGeometry(QtCore.QRect(0, 0, 960, 141))
        self.label_title_img.setObjectName("label_title_img")
        self.widget_query = QtWidgets.QWidget(self.centralwidget)
        self.widget_query.setGeometry(QtCore.QRect(0, 141, 960, 80))
        self.widget_query.setObjectName("widget_query")
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
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 221, 960, 100))
        self.widget.setObjectName("widget")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(30, 22, 54, 12))
        self.label_4.setObjectName("label_4")
        self.checkBox = QtWidgets.QCheckBox(self.widget)
        self.checkBox.setGeometry(QtCore.QRect(100, 22, 71, 16))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.widget)
        self.checkBox_2.setGeometry(QtCore.QRect(250, 22, 71, 16))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.widget)
        self.checkBox_3.setGeometry(QtCore.QRect(400, 22, 71, 16))
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(self.widget)
        self.checkBox_4.setGeometry(QtCore.QRect(550, 22, 71, 16))
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_5 = QtWidgets.QCheckBox(self.widget)
        self.checkBox_5.setGeometry(QtCore.QRect(700, 22, 71, 16))
        self.checkBox_5.setObjectName("checkBox_5")
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(5, 325, 950, 370))
        self.listView.setObjectName("listView")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "快手爬票"))
        self.label_title_img.setText(_translate("MainWindow", "TextLabel"))
        self.label.setText(_translate("MainWindow", "出发地："))
        self.label_2.setText(_translate("MainWindow", "目的地："))
        self.label_3.setText(_translate("MainWindow", "出发日："))
        self.pushButton.setText(_translate("MainWindow", "查询"))
        self.label_4.setText(_translate("MainWindow", "车次类型："))
        self.checkBox.setText(_translate("MainWindow", "GC-高铁"))
        self.checkBox_2.setText(_translate("MainWindow", "D-动车"))
        self.checkBox_3.setText(_translate("MainWindow", "Z-直达"))
        self.checkBox_4.setText(_translate("MainWindow", "T-特快"))
        self.checkBox_5.setText(_translate("MainWindow", "K-快速"))


def show_MainWindow():
    app = QtWidgets.QApplication(sys.argv)    # 实例化QApplication类，作为GUI主程序入口
    MainWindow = QtWidgets.QMainWindow()      # 创建QMainWindow类
    ui = Ui_MainWindow()                      # 实例化UI类
    ui.setupUi(MainWindow)                    # 设置窗体UI
    MainWindow.show()                         # 显示窗体
    sys.exit(app.exec_())                     # 当窗体创建完成之后，需要结束主循环过程


if __name__ == '__main__':
    show_MainWindow()