from flask import Flask, request, jsonify
from cipher.caesar.caesar_cipher import CaesarCipher
from cipher.vigenere.vigenere_cipher import VigenereCipher
from cipher.railfence.railfence_cipher import RailFenceCipher
#from cipher.playfair.playfair_cipher import PlayFairCipher

app = Flask(__name__)

# Khởi tạo đối tượng mã hóa
caesar_cipher = CaesarCipher()
vigenere_cipher = VigenereCipher()
railfence_cipher = RailFenceCipher()
#playfair_cipher = PlayFairCipher()

# ---- Caesar API ----
@app.route("/api/caesar/encrypt", methods=["POST"])
def caesar_encrypt():
    data = request.json
    plain_text = data.get("plain_text")
    key = int(data.get("key", 0))
    if plain_text is None:
        return jsonify({"error": "Missing 'plain_text'"}), 400
    encrypted_text = caesar_cipher.encrypt_text(plain_text, key)
    return jsonify({"encrypted_message": encrypted_text})

@app.route("/api/caesar/decrypt", methods=["POST"])
def caesar_decrypt():
    data = request.json
    cipher_text = data.get("cipher_text")
    key = int(data.get("key", 0))
    if cipher_text is None:
        return jsonify({"error": "Missing 'cipher_text'"}), 400
    decrypted_text = caesar_cipher.decrypt_text(cipher_text, key)
    return jsonify({"decrypted_message": decrypted_text})

# ---- Vigenère API ----
@app.route("/api/vigenere/encrypt", methods=["POST"])
def vigenere_encrypt():
    data = request.json
    plain_text = data.get("plain_text")
    key = data.get("key")
    if not plain_text or not key:
        return jsonify({"error": "Missing 'plain_text' or 'key'"}), 400
    encrypted_text = vigenere_cipher.vigenere_encrypt(plain_text, key)
    return jsonify({"encrypted_message": encrypted_text})

@app.route("/api/vigenere/decrypt", methods=["POST"])
def vigenere_decrypt():
    data = request.json
    cipher_text = data.get("cipher_text")
    key = data.get("key")
    if not cipher_text or not key:
        return jsonify({"error": "Missing 'cipher_text' or 'key'"}), 400
    decrypted_text = vigenere_cipher.vigenere_decrypt(cipher_text, key)
    return jsonify({"decrypted_message": decrypted_text})

# ---- Rail Fence API ----
@app.route("/api/railfence/encrypt", methods=["POST"])
def railfence_encrypt():
    data = request.json
    plain_text = data.get("plain_text")
    key = int(data.get("key", 0))
    if not plain_text or key <= 0:
        return jsonify({"error": "Missing 'plain_text' or invalid 'key'"}), 400
    encrypted_text = railfence_cipher.rail_fence_encrypt(plain_text, key)
    return jsonify({"encrypted_message": encrypted_text})

@app.route("/api/railfence/decrypt", methods=["POST"])
def railfence_decrypt():
    data = request.json
    cipher_text = data.get("cipher_text")
    key = int(data.get("key", 0))
    if not cipher_text or key <= 0:
        return jsonify({"error": "Missing 'cipher_text' or invalid 'key'"}), 400
    decrypted_text = railfence_cipher.rail_fence_decrypt(cipher_text, key)
    return jsonify({"decrypted_message": decrypted_text})

# ---- Playfair API ----
@app.route("/api/playfair/creatematrix", methods=["POST"])
def playfair_creatematrix():
    data = request.json
    key = data.get("key")
    if not key:
        return jsonify({"error": "Missing 'key'"}), 400
    matrix = playfair_cipher.create_playfair_matrix(key)
    return jsonify({"playfair_matrix": matrix})

@app.route("/api/playfair/encrypt", methods=["POST"])
def playfair_encrypt():
    data = request.json
    plain_text = data.get("plain_text")
    key = data.get("key")
    if not plain_text or not key:
        return jsonify({"error": "Missing 'plain_text' or 'key'"}), 400
    matrix = playfair_cipher.create_playfair_matrix(key)
    encrypted_text = playfair_cipher.playfair_encrypt(plain_text, matrix)
    return jsonify({"encrypted_message": encrypted_text})

@app.route("/api/playfair/decrypt", methods=["POST"])
def playfair_decrypt():
    data = request.json
    cipher_text = data.get("cipher_text")
    key = data.get("key")
    if not cipher_text or not key:
        return jsonify({"error": "Missing 'cipher_text' or 'key'"}), 400
    matrix = playfair_cipher.create_playfair_matrix(key)
    decrypted_text = playfair_cipher.playfair_decrypt(cipher_text, matrix)
    return jsonify({"decrypted_message": decrypted_text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
