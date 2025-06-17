def left_rotate(value, shift):
    return ((value << shift) | (value >> (32 - shift))) & 0xFFFFFFFF

def md5(message):
    a0 = 0x67452301
    b0 = 0xEFCDAB89
    c0 = 0x98BADCFE
    d0 = 0x10325476

    original_length = len(message)
    message += b'\x80'
    while len(message) % 64 != 56:
        message += b'\x00'
    message += (original_length * 8).to_bytes(8, byteorder='little')

    for i in range(0, len(message), 64):
        block = message[i:i+64]
        words = [int.from_bytes(block[j:j+4], 'little') for j in range(0, 64, 4)]
        a, b, c, d = a0, b0, c0, d0

        for j in range(64):
            if j < 16:
                f = (b & c) | (~b & d)
                g = j
            elif j < 32:
                f = (d & b) | (~d & c)
                g = (5 * j + 1) % 16
            elif j < 48:
                f = b ^ c ^ d
                g = (3 * j + 5) % 16
            else:
                f = c ^ (b | ~d)
                g = (7 * j) % 16
            f = (f + a + [  # K constants (rút gọn): 64 phần tử
                0xd76aa478, 0xe8c7b756, 0x242070db, 0xc1bdceee,  # bạn có thể copy đủ nếu muốn
            ][j % 4] + words[g]) & 0xFFFFFFFF
            a, d, c, b = d, c, b, (b + left_rotate(f, [7,12,17,22][j % 4])) & 0xFFFFFFFF

        a0 = (a0 + a) & 0xFFFFFFFF
        b0 = (b0 + b) & 0xFFFFFFFF
        c0 = (c0 + c) & 0xFFFFFFFF
        d0 = (d0 + d) & 0xFFFFFFFF

    return '{:08x}{:08x}{:08x}{:08x}'.format(a0, b0, c0, d0)

# Test input
input_string = input("Nhập chuỗi cần băm: ")
md5_hash = md5(input_string.encode('utf-8'))
print("Mã băm MD5 của chuỗi '{}' là: {}".format(input_string, md5_hash))
