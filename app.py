import sys
import subprocess
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog, QMessageBox, QLabel, QLineEdit, QHBoxLayout, QCheckBox, QGridLayout, QGroupBox

def call_cli_tool(file_paths, output_dir, lambda_, wp, whittaker, xmin, xmax, threshold, multiply, add, intensities, overlay, nosave, save,show_summary):
    try:
        # 路徑修改為你的虛擬環境激活腳本路徑
        venv_activate = "env\\Scripts\\activate.bat"
        cli_tool = "raman_tl\\raman-tl.py"

        # 構建命令參數
        cmd = f' python {cli_tool} {" ".join(file_paths)} -l {lambda_} -w {whittaker}'
        if output_dir:
            cmd += f' -od {output_dir}'
        if wp:
            cmd += f' -p {wp}'
        if xmin:
            cmd += f' -xmin {xmin}'
        if xmax:
            cmd += f' -xmax {xmax}'
        if threshold:
            cmd += f' -t {threshold}'
        if multiply:
            cmd += f' -m {multiply}'
        if add:
            cmd += f' -a {add}'
        if intensities:
            cmd += f' -i {intensities}'
        if overlay:
            cmd += ' -o'
        if nosave:
            cmd += ' -n'
        if save:
            cmd += f' -s {save}'
        if show_summary:
            cmd += ' -ss'
        # print(cmd)
        # 使用 subprocess.run 執行虛擬環境並執行 CLI 工具
        result = subprocess.run(cmd, shell=True, check=True, capture_output=True, text=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(e.stderr)
        QMessageBox.critical(None, "錯誤", f"處理檔案時發生錯誤：\n{e.stderr}")

def process_files(file_paths, output_dir, lambda_, wp, whittaker, xmin, xmax, threshold, multiply, add, intensities, overlay, nosave, save,show_summary):
    
    call_cli_tool(file_paths, output_dir, lambda_, wp, whittaker, xmin, xmax, threshold, multiply, add, intensities, overlay, nosave, save,show_summary)
    QMessageBox.information(None, "完成", "所有檔案已處理完畢")

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = '多檔案處理工具'
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(100, 100, 600, 400)
        
        layout = QVBoxLayout()

        self.file_label = QLabel('選擇檔案：', self)
        layout.addWidget(self.file_label)

        self.select_button = QPushButton('選擇檔案', self)
        self.select_button.clicked.connect(self.open_file_dialog)
        layout.addWidget(self.select_button)

        self.output_dir_label = QLabel('輸出目錄：', self)
        layout.addWidget(self.output_dir_label)

        self.output_dir_line_edit = QLineEdit(self)
        layout.addWidget(self.output_dir_line_edit)

        self.output_dir_button = QPushButton('選擇輸出目錄', self)
        self.output_dir_button.clicked.connect(self.select_output_dir)
        layout.addWidget(self.output_dir_button)
        self.nosave_checkbox = QCheckBox('不保存PDF', self)
        self.nosave_checkbox.setChecked(True)
        layout.addWidget(self.nosave_checkbox)

        self.save_data_checkbox = QCheckBox('保存資料', self)
        self.save_data_checkbox.setChecked(True)
        layout.addWidget(self.save_data_checkbox)

        self.save_img_checkbox = QCheckBox('保存圖片', self)
        layout.addWidget(self.save_img_checkbox)

        self.show_summary_checkbox = QCheckBox('顯示Summary', self)
        self.show_summary_checkbox.setChecked(False)
        layout.addWidget(self.show_summary_checkbox)

        self.process_button = QPushButton('開始處理', self)
        self.process_button.clicked.connect(self.start_processing)
        layout.addWidget(self.process_button)

        self.advanced_button = QPushButton('顯示進階功能', self)
        self.advanced_button.clicked.connect(self.toggle_advanced)
        layout.addWidget(self.advanced_button)
        
        self.advanced_group = QGroupBox('進階功能')
        self.advanced_layout = QVBoxLayout()
        #---------------------------------------------------
        self.lambda_label = QLabel('Lambda:', self)
        self.advanced_layout.addWidget(self.lambda_label)

        self.lambda_line_edit = QLineEdit(self)
        self.lambda_line_edit.setText('1000')
        self.advanced_layout.addWidget(self.lambda_line_edit)

        self.wp_label = QLabel('Savitzky–Golay參數 :', self)
        self.advanced_layout.addWidget(self.wp_label)

        self.wp_line_edit = QLineEdit(self)
        self.advanced_layout.addWidget(self.wp_line_edit)

        self.whittaker_label = QLabel('Whittaker參數:', self)
        self.advanced_layout.addWidget(self.whittaker_label)

        self.whittaker_line_edit = QLineEdit(self)
        self.whittaker_line_edit.setText('1')
        self.advanced_layout.addWidget(self.whittaker_line_edit)

        self.xmin_label = QLabel('xmin:', self)
        self.advanced_layout.addWidget(self.xmin_label)

        self.xmin_line_edit = QLineEdit(self)
        self.advanced_layout.addWidget(self.xmin_line_edit)

        self.xmax_label = QLabel('xmax:', self)
        self.advanced_layout.addWidget(self.xmax_label)

        self.xmax_line_edit = QLineEdit(self)
        self.advanced_layout.addWidget(self.xmax_line_edit)

        self.threshold_label = QLabel('閾值:', self)
        self.advanced_layout.addWidget(self.threshold_label)

        self.threshold_line_edit = QLineEdit(self)
        self.advanced_layout.addWidget(self.threshold_line_edit)

        self.multiply_label = QLabel('強度乘數:', self)
        self.advanced_layout.addWidget(self.multiply_label)

        self.multiply_line_edit = QLineEdit(self)
        self.advanced_layout.addWidget(self.multiply_line_edit)

        self.add_label = QLabel('波數加值:', self)
        self.advanced_layout.addWidget(self.add_label)

        self.add_line_edit = QLineEdit(self)
        self.advanced_layout.addWidget(self.add_line_edit)

        self.intensities_label = QLabel('強度加值:', self)
        self.advanced_layout.addWidget(self.intensities_label)

        self.intensities_line_edit = QLineEdit(self)
        self.intensities_line_edit.setText('0')
        self.advanced_layout.addWidget(self.intensities_line_edit)

        self.overlay_checkbox = QCheckBox('疊加譜圖', self)
        self.overlay_checkbox.setVisible(False)
        # self.advanced_layout.addWidget(self.overlay_checkbox)

        self.advanced_group.setLayout(self.advanced_layout)
        self.advanced_group.setVisible(False)
        layout.addWidget(self.advanced_group)
        self.setLayout(layout)
    def toggle_advanced(self):
        if self.advanced_group.isVisible():
            self.advanced_group.setVisible(False)
            self.advanced_button.setText('顯示進階功能')
            self.adjustSize()
            self.setGeometry(100, 100, 600, 400)

        else:
            self.advanced_group.setVisible(True)
            self.advanced_button.setText('隱藏進階功能')
            self.setGeometry(100, 100, 600, 800)
        # self.adjustSize()
    def open_file_dialog(self):
        options = QFileDialog.Options()
        files, _ = QFileDialog.getOpenFileNames(self, "選擇檔案", "", "All Files (*);;Python Files (*.py)", options=options)
        if files:
            self.file_paths = files
            self.file_label.setText(f'選擇檔案：{len(files)} 個檔案已選擇')
    
    def select_output_dir(self):
        options = QFileDialog.Options()
        directory = QFileDialog.getExistingDirectory(self, "選擇輸出目錄", options=options)
        if directory:
            self.output_dir_line_edit.setText(directory)
    
    def start_processing(self):
        if hasattr(self, 'file_paths') and self.output_dir_line_edit.text():
            lambda_ = self.lambda_line_edit.text()
            wp = self.wp_line_edit.text()
            whittaker = self.whittaker_line_edit.text()
            xmin = self.xmin_line_edit.text()
            xmax = self.xmax_line_edit.text()
            threshold = self.threshold_line_edit.text()
            multiply = self.multiply_line_edit.text()
            add = self.add_line_edit.text()
            intensities = self.intensities_line_edit.text()
            overlay = self.overlay_checkbox.isChecked()
            nosave = self.nosave_checkbox.isChecked()
            save=''
            if self.save_data_checkbox.isChecked():
                save += 'd'
            if self.save_img_checkbox.isChecked():
                save += 'p'
            show_summary = self.show_summary_checkbox.isChecked()
            # save = self.save_line_edit.text()
            
            process_files(self.file_paths, self.output_dir_line_edit.text(), lambda_, wp, whittaker, xmin, xmax, threshold, multiply, add, intensities, overlay, nosave, save,show_summary)
        else:
            QMessageBox.warning(self, "錯誤", "請選擇檔案和輸出目錄")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())
