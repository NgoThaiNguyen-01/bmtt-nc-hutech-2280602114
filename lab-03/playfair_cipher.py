import sys
import os
import requests
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.playfair import Ui_MainWindow  # ✅ Bạn phải chạy pyuic5 để tạo file này từ playfair.ui

# Bắt buộc: Chỉ định plugin Qt nếu chạy trên Windows
os.environ["QT_QPA_PLATFORM_PLUGIN_PATH"] = "./platforms"

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Gắn sự kiện các nút
        self.ui.pushButton.clicked.connect(self.call_api_encrypt)
        self.ui.pushButton_2.clicked.connect(self.call_api_decrypt)

    def call_api_encrypt(self):
        url = "http://127.0.0.1:5000/api/playfair/encrypt"
        payload = {
            "plain_text": self.ui.textEdit.toPlainText(),
            "key": self.ui.lineEdit.text()
        }

        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.textEdit_2.setText(data["encrypted_message"])
                self.show_message("Encrypted Successfully")
        except requests.exceptions.RequestException as e:
            print("Error calling API:", e)

    def call_api_decrypt(self):
        url = "http://127.0.0.1:5000/api/playfair/decrypt"
        payload = {
            "cipher_text": self.ui.textEdit_2.toPlainText(),
            "key": self.ui.lineEdit.text()
        }

        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.textEdit.setText(data["decrypted_message"])
                self.show_message("Decrypted Successfully")
        except requests.exceptions.RequestException as e:
            print("Error calling API:", e)

    def show_message(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(message)
        msg.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.setWindowTitle("Playfair Cipher - Giao diện API")
    window.show()
    sys.exit(app.exec_())
