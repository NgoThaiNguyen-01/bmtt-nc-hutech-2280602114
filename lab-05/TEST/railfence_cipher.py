class RailFenceCipher:
    def rail_fence_encrypt(self, text, key):
        fence = [[] for _ in range(key)]
        rail = 0
        var = 1
        for char in text:
            fence[rail].append(char)
            rail += var
            if rail == 0 or rail == key - 1:
                var = -var
        return ''.join(''.join(row) for row in fence)

    def rail_fence_decrypt(self, cipher, key):
        rail = 0
        var = 1
        marker = [['\n'] * len(cipher) for _ in range(key)]
        for i in range(len(cipher)):
            marker[rail][i] = '*'
            rail += var
            if rail == 0 or rail == key - 1:
                var = -var
        idx = 0
        for i in range(key):
            for j in range(len(cipher)):
                if marker[i][j] == '*' and idx < len(cipher):
                    marker[i][j] = cipher[idx]
                    idx += 1
        result = ''
        rail = 0
        var = 1
        for i in range(len(cipher)):
            result += marker[rail][i]
            rail += var
            if rail == 0 or rail == key - 1:
                var = -var
        return result