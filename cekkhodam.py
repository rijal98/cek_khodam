import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt, QSize

import random
import datetime

class KhodamCheckerApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Aplikasi Cek Khodam")
        self.setGeometry(100, 100, 500, 400)

        self.background_label = QLabel(self)
        self.background_label.setGeometry(0, 0, 500, 400)
        self.background_label.setScaledContents(True)
        self.update_background()

        
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)

        
        self.title_label = QLabel("Aplikasi Cek Khodam", self)
        self.title_label.setFont(QFont('Arial', 18, QFont.Bold))
        self.title_label.setStyleSheet("color: white;")

        #inputannya
        self.label = QLabel("Masukkan Nama Anda:", self)
        self.label.setFont(QFont('Arial', 14))
        self.label.setStyleSheet("background-color: #F0FFFF; color: black; padding: 5px;")

        self.entry = QLineEdit(self)
        self.entry.setFont(QFont('Arial', 12))
        self.entry.setStyleSheet("background-color: white; color: black;")

        # Button
        self.button = QPushButton("Cek Khodam", self)
        self.button.setFont(QFont('Arial', 12))
        self.button.setStyleSheet("background-color: #F0FFFF; color: black; border: 5px;")
        self.button.setCursor(Qt.PointingHandCursor)
        self.button.clicked.connect(self.check_khodam)

        # Result Label
        self.result_label = QLabel("", self)
        self.result_label.setFont(QFont('Arial', 14))
        self.result_label.setStyleSheet("color: white;")
        self.result_label.setAlignment(Qt.AlignCenter)

        # Adding Widgets to Layout
        self.main_layout.addWidget(self.title_label, alignment=Qt.AlignCenter)
        self.main_layout.addWidget(self.label, alignment=Qt.AlignCenter)
        self.main_layout.addWidget(self.entry, alignment=Qt.AlignCenter)
        self.main_layout.addWidget(self.button, alignment=Qt.AlignCenter)
        self.main_layout.addWidget(self.result_label, alignment=Qt.AlignCenter)

    def update_background(self):
        pixmap = QPixmap('background.jpg').scaled(self.size())
        self.background_label.setPixmap(pixmap)

    def resizeEvent(self, event):
        self.update_background()
        event.accept()

    def check_khodam(self):
        nama = self.entry.text().strip()
        if not nama:
            self.show_message("Error", "Nama tidak boleh kosong!", QMessageBox.Critical)
            return

        khodam, deskripsi = self.generate_khodam(nama)
        result_text = f"<b>Khodam Anda:</b> {khodam}<br><b>Deskripsi:</b> {deskripsi}"
        self.result_label.setText(result_text)

        self.log_result(nama, khodam)

    def generate_khodam(self, nama):
        khodam_list = {
            "Khodam Api": "Khodam yang kuat dan penuh energi.",
            "Khodam Air": "Khodam yang tenang dan bijaksana.",
            "Khodam Angin": "Khodam yang cepat dan lincah.",
            "Khodam Tanah": "Khodam yang kuat dan stabil.",
            "Khodam Cahaya": "Khodam yang terang dan penuh kebijaksanaan.",
            "Khodam Kegelapan": "Khodam yang misterius dan penuh rahasia."
        }
        khodam = random.choice(list(khodam_list.keys()))
        deskripsi = khodam_list[khodam]
        return khodam, deskripsi

    def log_result(self, nama, khodam):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"{timestamp} - Nama: {nama}, Khodam: {khodam}\n"
        with open("khodam_log.txt", "a") as file:
            file.write(log_entry)
        self.show_message("Info", "Hasil cek telah disimpan di khodam_log.txt", QMessageBox.Information)

    def show_message(self, title, message, icon):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.setIcon(icon)
        msg.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = KhodamCheckerApp()
    window.show()
    sys.exit(app.exec_())
