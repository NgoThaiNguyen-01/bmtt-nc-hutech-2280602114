from flask import Flask, render_template
import subprocess
import os

app = Flask(__name__, template_folder='templates')

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/run/caesar")
def run_caesar():
    subprocess.Popen(["python", "../../lab-03/ui/caesar.py"], shell=True)
    return "✅ Đã mở form Caesar Cipher"

@app.route("/run/playfair")
def run_playfair():
    subprocess.Popen(["python", "../../lab-03/ui/playfair.py"], shell=True)
    return "✅ Đã mở form Playfair Cipher"

@app.route("/run/railfence")
def run_railfence():
    subprocess.Popen(["python", "../../lab-03/ui/railfence.py"], shell=True)
    return "✅ Đã mở form Rail Fence Cipher"

@app.route("/run/vigenere")
def run_vigenere():
    subprocess.Popen(["python", "../../lab-03/ui/vigenere.py"], shell=True)
    return "✅ Đã mở form Vigenère Cipher"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)