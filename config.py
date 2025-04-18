# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '1015.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Settings(object):
    def setupUi(self, Settings):
        Settings.setObjectName("Settings")
        Settings.resize(277, 608)
        self.label_2 = QtWidgets.QLabel(Settings)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.groupBox = QtWidgets.QGroupBox(Settings)
        self.groupBox.setGeometry(QtCore.QRect(20, 40, 231, 45))
        self.groupBox.setStyleSheet("background-color: white;")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.base_color = QtWidgets.QLabel(self.groupBox)
        self.base_color.setGeometry(QtCore.QRect(10, 10, 25, 25))
        self.base_color.setMinimumSize(QtCore.QSize(25, 25))
        self.base_color.setMaximumSize(QtCore.QSize(25, 25))
        self.base_color.setStyleSheet("background-color: black;")
        self.base_color.setText("")
        self.base_color.setObjectName("base_color")
        self.base_color_text = QtWidgets.QLabel(self.groupBox)
        self.base_color_text.setGeometry(QtCore.QRect(50, 10, 128, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.base_color_text.setFont(font)
        self.base_color_text.setStyleSheet("margin-left:2px;")
        self.base_color_text.setObjectName("base_color_text")
        self.button_base = QtWidgets.QToolButton(self.groupBox)
        self.button_base.setGeometry(QtCore.QRect(200, 10, 25, 25))
        self.button_base.setStyleSheet("border: 2px solid gray")
        self.button_base.setObjectName("button_base")
        self.label_4 = QtWidgets.QLabel(Settings)
        self.label_4.setGeometry(QtCore.QRect(20, 100, 161, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.groupBox_2 = QtWidgets.QGroupBox(Settings)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 130, 231, 45))
        self.groupBox_2.setStyleSheet("background-color: white;")
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.diff_color = QtWidgets.QLabel(self.groupBox_2)
        self.diff_color.setGeometry(QtCore.QRect(10, 10, 25, 25))
        self.diff_color.setMinimumSize(QtCore.QSize(25, 25))
        self.diff_color.setMaximumSize(QtCore.QSize(25, 25))
        self.diff_color.setStyleSheet("background-color: blue;")
        self.diff_color.setText("")
        self.diff_color.setObjectName("diff_color")
        self.difference_color_text = QtWidgets.QLabel(self.groupBox_2)
        self.difference_color_text.setGeometry(QtCore.QRect(50, 10, 128, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.difference_color_text.setFont(font)
        self.difference_color_text.setStyleSheet("margin-left:2px;")
        self.difference_color_text.setObjectName("difference_color_text")
        self.button_diff = QtWidgets.QToolButton(self.groupBox_2)
        self.button_diff.setGeometry(QtCore.QRect(200, 10, 25, 25))
        self.button_diff.setStyleSheet("border: 2px solid gray")
        self.button_diff.setObjectName("button_diff")
        self.label_7 = QtWidgets.QLabel(Settings)
        self.label_7.setGeometry(QtCore.QRect(20, 190, 161, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.groupBox_3 = QtWidgets.QGroupBox(Settings)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 220, 231, 45))
        self.groupBox_3.setStyleSheet("background-color: white;")
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.find_color = QtWidgets.QLabel(self.groupBox_3)
        self.find_color.setGeometry(QtCore.QRect(10, 10, 25, 25))
        self.find_color.setMinimumSize(QtCore.QSize(25, 25))
        self.find_color.setMaximumSize(QtCore.QSize(25, 25))
        self.find_color.setStyleSheet("background-color: red;")
        self.find_color.setText("")
        self.find_color.setObjectName("find_color")
        self.find_color_text = QtWidgets.QLabel(self.groupBox_3)
        self.find_color_text.setGeometry(QtCore.QRect(50, 10, 128, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.find_color_text.setFont(font)
        self.find_color_text.setStyleSheet("margin-left:2px;")
        self.find_color_text.setObjectName("find_color_text")
        self.button_find = QtWidgets.QToolButton(self.groupBox_3)
        self.button_find.setGeometry(QtCore.QRect(200, 10, 25, 25))
        self.button_find.setStyleSheet("border: 2px solid gray")
        self.button_find.setObjectName("button_find")
        self.label_12 = QtWidgets.QLabel(Settings)
        self.label_12.setGeometry(QtCore.QRect(20, 280, 161, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.groupBox_4 = QtWidgets.QGroupBox(Settings)
        self.groupBox_4.setGeometry(QtCore.QRect(20, 310, 231, 45))
        self.groupBox_4.setStyleSheet("background-color: white;")
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.stop_color = QtWidgets.QLabel(self.groupBox_4)
        self.stop_color.setGeometry(QtCore.QRect(10, 10, 25, 25))
        self.stop_color.setMinimumSize(QtCore.QSize(25, 25))
        self.stop_color.setMaximumSize(QtCore.QSize(25, 25))
        self.stop_color.setStyleSheet("background-color: pink;")
        self.stop_color.setText("")
        self.stop_color.setObjectName("stop_color")
        self.stop_color_text = QtWidgets.QLabel(self.groupBox_4)
        self.stop_color_text.setGeometry(QtCore.QRect(50, 10, 128, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.stop_color_text.setFont(font)
        self.stop_color_text.setStyleSheet("margin-left:2px;")
        self.stop_color_text.setObjectName("stop_color_text")
        self.button_stop = QtWidgets.QToolButton(self.groupBox_4)
        self.button_stop.setGeometry(QtCore.QRect(200, 10, 25, 25))
        self.button_stop.setStyleSheet("border: 2px solid gray")
        self.button_stop.setObjectName("button_stop")
        self.label_15 = QtWidgets.QLabel(Settings)
        self.label_15.setGeometry(QtCore.QRect(20, 370, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.groupBox_5 = QtWidgets.QGroupBox(Settings)
        self.groupBox_5.setGeometry(QtCore.QRect(20, 400, 231, 45))
        self.groupBox_5.setStyleSheet("background-color: white;")
        self.groupBox_5.setTitle("")
        self.groupBox_5.setObjectName("groupBox_5")
        self.line_fontsize = QtWidgets.QLineEdit(self.groupBox_5)
        self.line_fontsize.setGeometry(QtCore.QRect(10, 10, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setKerning(True)
        self.line_fontsize.setFont(font)
        self.line_fontsize.setStyleSheet("border: 0px;")
        self.line_fontsize.setObjectName("line_fontsize")
        self.label_16 = QtWidgets.QLabel(Settings)
        self.label_16.setGeometry(QtCore.QRect(20, 460, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.groupBox_6 = QtWidgets.QGroupBox(Settings)
        self.groupBox_6.setGeometry(QtCore.QRect(20, 490, 231, 51))
        self.groupBox_6.setStyleSheet("background-color: white;")
        self.groupBox_6.setTitle("")
        self.groupBox_6.setObjectName("groupBox_6")
        self.button_path = QtWidgets.QToolButton(self.groupBox_6)
        self.button_path.setGeometry(QtCore.QRect(200, 10, 25, 25))
        self.button_path.setStyleSheet("border: 2px solid gray")
        self.button_path.setObjectName("button_path")
        self.scrollArea = QtWidgets.QScrollArea(self.groupBox_6)
        self.scrollArea.setGeometry(QtCore.QRect(0, 0, 191, 51))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.path_folder = QtWidgets.QLabel()
        self.path_folder.setGeometry(QtCore.QRect(6, 2, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.path_folder.setFont(font)
        self.path_folder.setObjectName("path_folder")
        self.scrollArea.setWidget(self.path_folder)
        self.button_apply = QtWidgets.QToolButton(Settings)
        self.button_apply.setGeometry(QtCore.QRect(20, 560, 111, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button_apply.setFont(font)
        self.button_apply.setStyleSheet("border: 2px solid gray")
        self.button_apply.setObjectName("button_apply")
        self.button_reset = QtWidgets.QToolButton(Settings)
        self.button_reset.setGeometry(QtCore.QRect(140, 560, 111, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button_reset.setFont(font)
        self.button_reset.setStyleSheet("border: 2px solid gray")
        self.button_reset.setObjectName("button_reset")

        self.retranslateUi(Settings)
        QtCore.QMetaObject.connectSlotsByName(Settings)

    def retranslateUi(self, Settings):
        _translate = QtCore.QCoreApplication.translate
        Settings.setWindowTitle(_translate("Settings", "Настройки"))
        self.label_2.setText(_translate("Settings", "Цвет текста"))
        self.base_color_text.setText(_translate("Settings", "цвет"))
        self.button_base.setText(_translate("Settings", "..."))
        self.label_4.setText(_translate("Settings", "Цвет текста отличие"))
        self.difference_color_text.setText(_translate("Settings", "цвет"))
        self.button_diff.setText(_translate("Settings", "..."))
        self.label_7.setText(_translate("Settings", "Цвет текста цель"))
        self.find_color_text.setText(_translate("Settings", "цвет"))
        self.button_find.setText(_translate("Settings", "..."))
        self.label_12.setText(_translate("Settings", "Цвет текста стоп"))
        self.stop_color_text.setText(_translate("Settings", "цвет"))
        self.button_stop.setText(_translate("Settings", "..."))
        self.label_15.setText(_translate("Settings", "Размер шрифта"))
        self.line_fontsize.setText(_translate("Settings", "12"))
        self.label_16.setText(_translate("Settings", "Путь к папке CACHE"))
        self.button_path.setText(_translate("Settings", "..."))
        self.path_folder.setText(_translate("Settings", "../CACHE"))
        self.button_apply.setText(_translate("Settings", "Сохранить"))
        self.button_reset.setText(_translate("Settings", "Сбросить"))
