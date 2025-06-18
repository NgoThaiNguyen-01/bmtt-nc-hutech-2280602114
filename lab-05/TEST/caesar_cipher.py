class CaesarCipher:
    def encrypt_text(self, text, key):
        result = ""
        for c in text:
            if c.isalpha():
                base = ord('A') if c.isupper() else ord('a')
                result += chr((ord(c) - base + key) % 26 + base)
            else:
                result += c
        return result

    def decrypt_text(self, text, key):
        return self.encrypt_text(text, -key)