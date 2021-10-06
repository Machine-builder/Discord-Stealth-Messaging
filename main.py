from modules import image_process
from modules import strbin
from modules import clip_image
from PIL import Image, ImageGrab
import os
import random

message_queue = []
message_history = []

while 1:

    os.system('cls')

    print(('''\


                             XXXXXXXX     
         XXXXXXXX           XXX    XXX    
        XXX    XXX          XX      XX    
        XX      XX          XX            
    XXXXXXXXXXXXXXXXXX  XXXXXXXXXXXXXXXXXX
    XXX            XXX  XXX            XXX
    XX              XX  XX              XX
    XX              XX  XX              XX
    XX      XX      XX  XX      XX      XX
    XX      XX      XX  XX      XX      XX
    XX              XX  XX              XX
    XXX            XXX  XXX            XXX
    XXXXXXXXXXXXXXXXXX  XXXXXXXXXXXXXXXXXX
    
        +----------------------------+
        |         S . D . M          |
        |  Secure Discord Messaging  |
        +----------------------------+'''))

    if len(message_history)>0:
        print()
        print("    ==+ Chat History +==")
    for m in message_history:
        print("    "+m)

    if len(message_queue)>0:
        print()
        print("    ==+ Recent Actions +==")
    for m in message_queue:
        print("    "+m)
    message_queue = []

    option = input((
        '\n'
        '    ==+  Options  +== \n'
        '    S : Send a message\n'
        '    C : Send a message using clipboard\n'
        '    R : Receive a message\n'
        '    D : Delete chat history\n'
        '    \n'
        '    >>> '
    )).lower()

    if option == 's':
        all_images = os.listdir('./images/')
        image_to_use = random.choice(all_images)
        image = Image.open(f'./images/{image_to_use}')

    if option == 'c':
        image = ImageGrab.grabclipboard()

    if option in 'sc' and option:
        message = input("\n    ==+  Enter Message  +==\n    >>> ")
        binary = strbin.text_to_bits(message)
        image_process.putBinary(binary, image)
        clip_image.sendToClipboard(image)

        image2 = ImageGrab.grabclipboard()
        if image2 is not None:
            binary = image_process.getBinary(image2)
            text = strbin.text_from_bits(binary)
            if text != message:
                message_queue.append("Uh oh! Something went wrong")
                message_queue.append("The encryption process failed.")
            else:
                message_queue.append("Encryption was successful!")
                message_history.append("[YOU]   "+message)
        else:
            message_queue.append("Uh oh! Something went wrong")
            message_queue.append("and no image was found in")
            message_queue.append("your clipboard!")

    elif option == 'r':
        message_queue.append("Receiving message...")
        image = ImageGrab.grabclipboard()
        if image is not None:
            binary = image_process.getBinary(image)
            text = strbin.text_from_bits(binary)

            message_queue.append("Message from image")
            message_queue.append("  "+text)
            message_history.append("[OTHER] "+text)

        else:
            message_queue.append("Uh oh! Something went wrong")
            message_queue.append("and no image was found in")
            message_queue.append("your clipboard!")

    elif option == 'd':
        message_queue.append("Cleared chat history!")
        message_history = []