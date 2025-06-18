from flask import Flask, render_template, request
from caesar_cipher import CaesarCipher
from playfair_cipher import PlayFairCipher
from railfence_cipher import RailFenceCipher
from vigenere_cipher import VigenereCipher

app = Flask(__name__, template_folder='templates')

@app.route("/")
def home():
    return render_template("index.html")

# ========== CAESAR ==========
@app.route("/encrypt/caesar", methods=["POST"])
def caesar_encrypt():
    text = request.form["inputPlainText"]
    key = int(request.form["inputKeyPlain"])
    cipher = CaesarCipher()
    result = cipher.encrypt_text(text, key)
    return f"<h3>Kết quả mã hóa Caesar:</h3><p>{result}</p>"

@app.route("/decrypt/caesar", methods=["POST"])
def caesar_decrypt():
    text = request.form["inputCipherText"]
    key = int(request.form["inputKeyCipher"])
    cipher = CaesarCipher()
    result = cipher.decrypt_text(text, key)
    return f"<h3>Kết quả giải mã Caesar:</h3><p>{result}</p>"

# ========== PLAYFAIR ==========
@app.route("/encrypt/playfair", methods=["POST"])
def playfair_encrypt():
    text = request.form["inputPlainText"]
    key = request.form["inputKeyPlain"]
    cipher = PlayFairCipher()
    matrix = cipher.create_playfair_matrix(key)
    result = cipher.playfair_encrypt(text, matrix)
    return f"<h3>Kết quả mã hóa Playfair:</h3><p>{result}</p>"

@app.route("/decrypt/playfair", methods=["POST"])
def playfair_decrypt():
    text = request.form["inputCipherText"]
    key = request.form["inputKeyCipher"]
    cipher = PlayFairCipher()
    matrix = cipher.create_playfair_matrix(key)
    result = cipher.playfair_decrypt(text, matrix)
    return f"<h3>Kết quả giải mã Playfair:</h3><p>{result}</p>"

# ========== RAIL FENCE ==========
@app.route("/encrypt/railfence", methods=["POST"])
def railfence_encrypt():
    text = request.form["inputPlainText"]
    key = int(request.form["inputKeyPlain"])
    cipher = RailFenceCipher()
    result = cipher.rail_fence_encrypt(text, key)
    return f"<h3>Kết quả mã hóa Rail Fence:</h3><p>{result}</p>"

@app.route("/decrypt/railfence", methods=["POST"])
def railfence_decrypt():
    text = request.form["inputCipherText"]
    key = int(request.form["inputKeyCipher"])
    cipher = RailFenceCipher()
    result = cipher.rail_fence_decrypt(text, key)
    return f"<h3>Kết quả giải mã Rail Fence:</h3><p>{result}</p>"

# ========== VIGENÈRE ==========
@app.route("/encrypt/vigenere", methods=["POST"])
def vigenere_encrypt():
    text = request.form["inputPlainText"]
    key = request.form["inputKeyPlain"]
    cipher = VigenereCipher()
    result = cipher.vigenere_encrypt(text, key)
    return f"<h3>Kết quả mã hóa Vigenère:</h3><p>{result}</p>"

@app.route("/decrypt/vigenere", methods=["POST"])
def vigenere_decrypt():
    text = request.form["inputCipherText"]
    key = request.form["inputKeyCipher"]
    cipher = VigenereCipher()
    result = cipher.vigenere_decrypt(text, key)
    return f"<h3>Kết quả giải mã Vigenère:</h3><p>{result}</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)
