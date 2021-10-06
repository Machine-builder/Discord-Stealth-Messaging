from PIL import Image
from .b10b2 import b10b2

class constants:
    ending = '01110101001010011101011100110101'

def putBinary(binary, image):
    ims = image.size
    impx = image.load()

    total_binary = binary + constants.ending
    lsbs = 2
    lsbs3 = lsbs*3
    total_binary_length = len(total_binary)
    add_binary = '0'*(lsbs3 - total_binary_length%lsbs3)
    total_binary += add_binary

    finished = False

    for pixely in range(ims[1]):
        for pixelx in range(ims[0]):
            colour = list(impx[pixelx, pixely])
            new_colour = []
            for i,channel in enumerate(colour):
                channel_binary = b10b2.base10base2(channel)
                channel_binary = channel_binary.rjust(8, '0')
                channel_binary = channel_binary[:-lsbs]
                last_bits = total_binary[:lsbs]
                total_binary = total_binary[lsbs:]
                channel_binary += last_bits
                channel_value = b10b2.base2base10(channel_binary)
                new_colour.append(channel_value)
            colour = tuple(new_colour)
            impx[pixelx, pixely] = colour
            if len(total_binary) == 0:
                finished = True
                break
        if finished:
            break

def getBinary(image):
    ims = image.size
    impx = image.load()

    output = ''
    lsbs = 2
    finished = False
    ending_length = len(constants.ending)

    for pixely in range(ims[1]):
        for pixelx in range(ims[0]):
            colour = list(impx[pixelx, pixely])
            for i,channel in enumerate(colour):
                channel_binary = b10b2.base10base2(channel)
                channel_binary = channel_binary.rjust(8, '0')
                last_bits = channel_binary[-lsbs:]
                for bit in last_bits:
                    output += bit
                    if output[-ending_length:] == constants.ending:
                        finished = True
                        break
                if finished:
                    break
            if finished:
                break
        if finished:
            break
    
    output = output[:-ending_length]
    return output