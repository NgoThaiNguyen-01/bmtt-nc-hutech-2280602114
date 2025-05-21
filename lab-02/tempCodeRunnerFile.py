from flask import Flask, request, jsonify
from cipher.caesar.caesar_cipher import CaesarCipher  # Giữ nguyên nếu chạy bằng "python -m lab-02.api"
# Nếu chạy trực tiếp file này bằng "python api.py" thì sửa thành:
# from caesar_cipher import CaesarCipher

import sys
import os

# Thêm đoạn này để chắc chắn Python tìm thấy thư mục cipher
sys.path.append(os.path.join(os.path.dirname(__file__), "."))

app = Flask(__name__)

caesar_cipher = CaesarCipher()

@app.route("/api/caesar/encrypt", methods=["POST"])
def caesar_encrypt():
    data = request.json
    plain_text = data["plain_text"]
    key = int(data["key"])
    encrypted_text = caesar_cipher.encrypt_text(plain_text, key)
    return jsonify({"encrypted_message": encrypted_text})

@app.route("/api/caesar/decrypt", methods=["POST"])
def caesar_decrypt():
    data = request.json
    cipher_text = data["cipher_text"]
    key = int(data["key"])
    decrypted_text = caesar_cipher.decrypt_text(cipher_text, key)
    return jsonify({"decrypted_message": decrypted_text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
