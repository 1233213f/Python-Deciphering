import hashlib
import itertools

s = ['\x00', '\x01', '\x02', '\x03', '\x04', '\x05', '\x06', '\x07', '\x08']
hashkey = open('Gesture.key', 'rb').read()

for a, b, c, d, e, f, g, h, i in itertools.permutations(s, 9):
    if hashlib.sha1(a + b + c + d + e + f + g + h + i).digest() == hashkey:
        for x in a, b, c, d, e, f, g, h, i:
            print
            chr(ord(x) + 0x30),
        print
        "\n"
        break