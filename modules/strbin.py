# https://stackoverflow.com/questions/7396849/convert-binary-to-ascii-and-vice-versa

from . import b10b2

def text_to_bits(text):
    bits = ''
    for char in text:
        n = ord(char)
        b = b10b2.b10b2.base10base2(n).rjust(12,'0')
        bits += b
    return bits

def text_from_bits(bits):
    text = ''
    interations = int(len(bits)/12)
    for i in range(interations):
        b = bits[i*12:(i+1)*12]
        n = b10b2.b10b2.base2base10(b)
        text += chr(n)
    return text