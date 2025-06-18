class PlayFairCipher:
    def create_playfair_matrix(self, key):
        matrix = []
        seen = set()
        key = key.upper().replace('J', 'I')
        for char in key:
            if char not in seen and char.isalpha():
                seen.add(char)
                matrix.append(char)
        for char in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
            if char not in seen:
                seen.add(char)
                matrix.append(char)
        return [matrix[i:i+5] for i in range(0, 25, 5)]

    def find_position(self, matrix, char):
        for i, row in enumerate(matrix):
            if char in row:
                return i, row.index(char)
        return None

    def playfair_encrypt(self, text, matrix):
        text = text.upper().replace('J', 'I').replace(" ", "")
        if len(text) % 2 != 0:
            text += 'X'
        result = ""
        for i in range(0, len(text), 2):
            a, b = text[i], text[i+1]
            r1, c1 = self.find_position(matrix, a)
            r2, c2 = self.find_position(matrix, b)
            if r1 == r2:
                result += matrix[r1][(c1+1)%5] + matrix[r2][(c2+1)%5]
            elif c1 == c2:
                result += matrix[(r1+1)%5][c1] + matrix[(r2+1)%5][c2]
            else:
                result += matrix[r1][c2] + matrix[r2][c1]
        return result

    def playfair_decrypt(self, text, matrix):
        result = ""
        for i in range(0, len(text), 2):
            a, b = text[i], text[i+1]
            r1, c1 = self.find_position(matrix, a)
            r2, c2 = self.find_position(matrix, b)
            if r1 == r2:
                result += matrix[r1][(c1-1)%5] + matrix[r2][(c2-1)%5]
            elif c1 == c2:
                result += matrix[(r1-1)%5][c1] + matrix[(r2-1)%5][c2]
            else:
                result += matrix[r1][c2] + matrix[r2][c1]
        return result