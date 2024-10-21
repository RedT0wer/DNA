import json
import sys
import gui
import config

from PyQt5 import QtWidgets,QtGui
from PyQt5.QtWidgets import QFileDialog
from FunctionRequest import func_request
from ConfigWrite import Config

#pyuic5 1015.ui -o config.py
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
        self.BrowserTxtRequest.clicked.connect(self.read_browser_txt_request)
        self.BrowserTxtRequest1.clicked.connect(self.read_browser_txt_request1)
        self.ResultRequest.clicked.connect(self.res_request)
        self.LineEditRequest.textChanged.connect(self.change_request)

        self.path_json_origin = ''
        self.path_txt_origin = ''
        self.BrowserJsonOrigin.clicked.connect(self.read_browser_json_origin)
        self.BrowserTxtOrigin.clicked.connect(self.read_browser_txt_origin)
        self.ResultOrigin.clicked.connect(self.res_orig)
        self.NewNameOrigin.textChanged.connect(self.change_origin)

        self.path_txt_exon = ''
        self.BrowserTxtExon.clicked.connect(self.read_browser_txt_exon)
        self.ResultExon.clicked.connect(self.res_exon)
        self.NewNameExon.textChanged.connect(self.change_exon)
        self.CountExon.textChanged.connect(self.change_exon)

        self.Button.clicked.connect(self.OpenWindowSetting)

    def change_request(self):
        self.CheckResultRequest.setChecked(False)
        self.CheckFailRequest.setChecked(False)
    def read_browser_txt_request(self):
        name = QFileDialog.getOpenFileName(self, 'Open file', '', 'TXT file (*txt)')
        self.path_origin_request = name[0]
        self.change_request()
        self.FilenameTxtRequest.setText(name[0].split('/')[-1])
    def read_browser_txt_request1(self):
        name = QFileDialog.getOpenFileName(self, 'Open file', '', 'TXT file (*txt)')
        self.path_txt_request = name[0]
        self.change_request()
        self.FilenameTxtRequest1.setText(name[0].split('/')[-1])
    def res_request(self):
        if self.FilenameTxtRequest.text() and self.FilenameTxtRequest1.text() and self.LineEditRequest.text():
            try:
                output = func_request(self.LineEditRequest.text(),self.path_origin_request,self.path_txt_request, self.config)
                self.TextResult.setHtml(f"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:{self.config.font_size}; font-weight:400; font-style:normal;\">\n<span>{output}</span></body></html>")
                self.CheckResultRequest.setChecked(True)
                self.CheckFailRequest.setChecked(False)
            except:
                self.CheckFailRequest.setChecked(True)

    def change_origin(self):
        self.CheckResultOrigin.setChecked(False)
        self.CheckFailOrigin.setChecked(False)
    def read_browser_json_origin(self):
        name = QFileDialog.getOpenFileName(self, 'Open file', '', 'JSON file (*json)')
        self.path_json_origin = name[0]
        self.change_origin()
        self.FilenameJsonOrigin.setText(name[0].split('/')[-1])
    def read_browser_txt_origin(self):
        name = QFileDialog.getOpenFileName(self, 'Open file', '', 'TXT file (*txt)')
        self.path_txt_origin = name[0]
        self.change_origin()
        self.FilenameTxtOrigin.setText(name[0].split('/')[-1])
    def res_orig(self):
        if self.FilenameJsonOrigin.text() and self.FilenameTxtOrigin.text() and self.NewNameOrigin.text():
            try:
                self.create_file_origin(self.NewNameOrigin.text() + '.txt')
                self.CheckResultOrigin.setChecked(True)
                self.CheckFailOrigin.setChecked(False)
            except:
                self.CheckFailOrigin.setChecked(True)
    def create_file_origin(self, new_name):
        sequence = open(self.path_txt_origin,'r').readline()
        database_json = json.load(open(self.path_json_origin,'r'))['features']
        database = {}

        prev_st = -1
        for obj in database_json:
            st, end, name = int(obj['location']['start']['value']), int(obj['location']['end']['value']), obj['description']
            if prev_st != -1 and st < prev_st:
                break
            database[st] = [end, name, sequence[st-1:end]]
            prev_st = st

        new_file = open(new_name,'w')
        new_file.write(json.dumps(database))
        new_file.close()

    def change_exon(self):
        self.CheckResultExon.setChecked(False)
        self.CheckFailExon.setChecked(False)
    def read_browser_txt_exon(self):
        name = QFileDialog.getOpenFileName(self, 'Open file', '', 'TXT file (*txt)')
        self.path_txt_exon = name[0]
        self.change_exon()
        self.FilenameTxtExon.setText(name[0].split('/')[-1])
    def res_exon(self):
        if self.FilenameTxtExon.text() and self.NewNameExon.text() and self.CountExon.text():
            try:
                self.create_file_not_origin()
                self.CheckResultExon.setChecked(True)
                self.CheckFailExon.setChecked(False)
            except:
                self.CheckFailExon.setChecked(True)
    def create_file_not_origin(self):
        file_exon = open(self.path_txt_exon, 'r')

        count_string = 0

        all_string,string = '',''
        while file_exon:
            str_i = file_exon.readline()
            if str_i[0] == '>':
                if string:
                    all_string += str(len(string)) + ' ' + string + '\n'
                    string = ''

                if 'exon' in str_i:
                    count_string += 1
                else:
                    break
            else:
                string += str_i.strip()
        print(str(count_string) + ' ' + str(self.CountExon.text()) + '\n')
        new_file = open(self.NewNameExon.text() + '.txt','w')
        new_file.write(str(count_string) + ' ' + str(self.CountExon.text()) + '\n')
        new_file.write(all_string)
        new_file.close()

    def OpenWindowSetting(self):
        setting = SettingUI(self.config)
        setting.exec_()
        setting.show()

        

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = MainWindow()
    application.show()
    sys.exit(app.exec_())