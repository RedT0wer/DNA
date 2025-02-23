import json
import sys
import gui
import config
import time

from PyQt5 import QtWidgets,QtGui
from PyQt5.QtWidgets import QFileDialog
from FunctionRequest import func_request
from ConfigWrite import Config

#pyuic5 0901.ui -o gui.py
#ENST00000460472
#1 - NM_003319:c.65555find
#2 - NM_003319:c.2_3del
#3 - NM_001267550:c.92353-2A>C
#4 - NM_003319:c.1_2insTG
#5 - NM_003319:c.16argT

class SettingUI(QtWidgets.QDialog, config.Ui_Settings):
    def __init__(self, config):    
        super().__init__()
        self.setupUi(self)
        self.config = config

        self.ReadConfigForText(self.config)
        self.ReadConfigForColor()         

        self.button_diff.clicked.connect(self.get_color_diff)
        self.button_base.clicked.connect(self.get_color_base)
        self.button_stop.clicked.connect(self.get_color_stop)
        self.button_find.clicked.connect(self.get_color_find)
        self.button_path.clicked.connect(self.get_path)

        self.button_apply.clicked.connect(self.Apply)
        self.button_reset.clicked.connect(self.Reset)

    def on_value_changed(self, value):
        font_metrics = QtGui.QFontMetrics(self.path_folder.font())
        pixel_length = font_metrics.horizontalAdvance(self.path_folder.text())
        
        width_text = pixel_length
        width_block = self.path_folder.width()

        max_offset = width_text - width_block
        if max_offset < 0:
            max_offset = 0
        offset = (value / 100) * max_offset
        print(max_offset,value,offset)

        self.path_folder.setStyleSheet(f"background-color: rgba(255, 255, 255, 0);margin-right: {offset}px;")

    def get_html_code(self, string):
        return ''.join(string.split('color: ')[1][:7])

    def get_color_diff(self):
        old_name = self.difference_color_text.text()
        self.difference_color_text.setText(QtWidgets.QColorDialog().getColor(QtGui.QColor(old_name)).name())
        self.ReadConfigForColor()
    def get_color_base(self):
        old_name = self.base_color_text.text()
        self.base_color_text.setText(QtWidgets.QColorDialog().getColor(QtGui.QColor(old_name)).name())
        self.ReadConfigForColor()
    def get_color_stop(self):
        old_name = self.stop_color_text.text()
        self.stop_color_text.setText(QtWidgets.QColorDialog().getColor(QtGui.QColor(old_name)).name())
        self.ReadConfigForColor()
    def get_color_find(self):
        old_name = self.find_color_text.text()
        self.find_color_text.setText(QtWidgets.QColorDialog().getColor(QtGui.QColor(old_name)).name())
        self.ReadConfigForColor()
    def get_path(self):
        menu = QFileDialog.getExistingDirectory(self,"Select folder",self.path_folder.text())
        self.path_folder.setText(menu)

    def ReadConfigForText(self, config):
        self.base_color_text.setText(self.get_html_code(config.base_color_text))
        self.difference_color_text.setText(self.get_html_code(config.difference_color_text))
        self.stop_color_text.setText(self.get_html_code(config.stop_color_text))
        self.find_color_text.setText(self.get_html_code(config.find_color_text))
        self.line_fontsize.setText(config.font_size[:-2])
        self.path_folder.setText(config.path_folder_cache)

    def ReadConfigForColor(self):
        self.base_color.setStyleSheet(f"background-color: {self.base_color_text.text()}")
        self.diff_color.setStyleSheet(f"background-color: {self.difference_color_text.text()}")
        self.find_color.setStyleSheet(f"background-color: {self.find_color_text.text()}")
        self.stop_color.setStyleSheet(f"background-color: {self.stop_color_text.text()}")

    def Apply(self):
        self.config.base_color_text = "<span style=\"color: " + self.base_color_text.text() + ";\">"
        self.config.difference_color_text = "<span style=\"color: " + self.difference_color_text.text() + ";\">"
        self.config.find_color_text = "<span style=\"color: " + self.find_color_text.text() + ";\">"
        self.config.stop_color_text = "<span style=\"color: " + self.stop_color_text.text() + ";\">"
        self.config.font_size = self.line_fontsize.text() + "pt"
        self.config.path_folder_cache = self.path_folder.text()

        self.config.apply_settings()
    def Reset(self):
        self.config.return_default()
        self.ReadConfigForText(self.config)
        self.ReadConfigForColor()


class MainWindow(QtWidgets.QMainWindow, gui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.config = Config()

        self.path_origin_request = ''
        self.path_txt_request = ''
        self.ResultRequest.clicked.connect(self.res_request)
        self.LineEditRequest.textChanged.connect(self.change_request)

        self.Button.clicked.connect(self.OpenWindowSetting)

    def change_request(self):
        self.CheckResultRequest.setChecked(False)
        self.CheckFailRequest.setChecked(False)
    def res_request(self):
        if self.FilenameTxtRequest.text() and self.FilenameTxtRequest1.text() and self.LineEditRequest.text():
            #st = time.perf_counter()
            output = func_request(self.LineEditRequest.text(),self.FilenameTxtRequest.text(),self.FilenameTxtRequest1.text(), self.config)
            self.TextResult.setHtml(f"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:{self.config.font_size}; font-weight:400; font-style:normal;\">\n<span>{output}</span></body></html>")
            self.CheckResultRequest.setChecked(True)
            self.CheckFailRequest.setChecked(False)
            #print(time.perf_counter() - st)

    def OpenWindowSetting(self):
        setting = SettingUI(self.config)
        setting.exec_()
        setting.show()

        

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = MainWindow()
    application.show()
    sys.exit(app.exec_())