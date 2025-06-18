class VigenereCipher:
    def vigenere_encrypt(self, text, key):
        text = text.upper()
        key = key.upper()
        result = ""
        for i in range(len(text)):
            if text[i].isalpha():
                shift = ord(key[i % len(key)]) - ord('A')
                result += chr((ord(text[i]) - ord('A') + shift) % 26 + ord('A'))
            else:
                result += text[i]
        return result

    def vigenere_decrypt(self, text, key):
        text = text.upper()
        key = key.upper()
        result = ""
        for i in range(len(text)):
            if text[i].isalpha():
                shift = ord(key[i % len(key)]) - ord('A')
                result += chr((ord(text[i]) - ord('A') - shift + 26) % 26 + ord('A'))
            else:
                result += text[i]
        return result