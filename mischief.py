#!/usr/bin/python3
import os
import cv2
import random
import sys
import numpy as num
from pyfiglet import figlet_format
from time import sleep as timeout
import tkinter.filedialog

green = "\033[32m"
blue = "\033[34m"
red = "\033[31m"


def restart():
    stego = sys.executable
    os.execl(stego, stego, *sys.argv)
    os.system('clear')


def out():
    timeout(1)
    print()


print(blue + figlet_format('MISCHIEF', font='bubble'))


def timming(sentence):
    for word in sentence:
        print(word, end='', flush=True)
        timeout(0.090)
    print()


print(red +
      " Name        : Arya Davidson A.\n Course      : ADCD [Advanced Diploma in Cyber Defence]\n Institution : RedTeam Hacker Academy\n Github      : https://github.com/AryaDavidsonA\n LinkedIn    : https://www.linkedin.com/in/arya-davidson-a-0758581a6\n")
next = input(blue + ' >>>> [ Please press enter to move forward ] ')
os.system("clear")

print(red + figlet_format('MISCHIEF', font='bubble'))
timming(green +
        " Hello !!!\n You know it's a wonderful and tremendous\n idea,lets steal the biggest and the most\n obvious ship in the universe and escape\n in that.\n Remember me? I'm LOKI,Prince of Asgard!!\n And I am going to bless you to hide your\n secrets!!!! I am burdened with glorious\n purpose.")
print()
timming(red + " >>>> [ Type y/n to hide your secrets ]")
try:
    in_ = input(' >>>> ')
    if in_ == 'y':
        os.system('clear')
        print(red + figlet_format('LOKI SECRET', font='bubble'))
        timming(green + " Keep calm and kneel down!!!")
        timming(" Just kiddin'!!!")
        timming(" No I mean it!!! hahahahaha")
        timeout(2)
        timming(" If you want to hide your secret,\n you should come to Asgard with me!!!\n")
        timming(red + " >>>> [ If you are ready to come with me ]")
        timming(" >>>> [ Please type y/n to the next step ]")
    elif in_ == 'n':
        print()
        timming(red + "\n >>>> [ You lied to me!!! I'm impressed!!! ]")
        out()
        os.system("clear")
        restart()
        if not in_:
            raise ValueError("Error! Empty String")
    else:
        timming(red + "\n >>>> [ You lied to me!!! I'm impressed!!! ]")
        os.system("clear")
        restart()
    try:
        in_1 = input(" >>>> ")
        if in_1 == 'y':
            os.system('clear')
            print(red + figlet_format('MISCHIEF', font='bubble'))
            timming(green + " Oh, no no no!!!\n You need Heimdall's permission!!!\n")
            timeout(2)
            timming(red + " >>>> [ Type y/n to get the permission ]")
        elif in_1 == 'n':
            print()
            timming(red + "\n >>>> [ You lied to me!!! I'm impressed!!! ]")
            out()
            os.system("clear")
            restart()
            if not in_1:
                raise ValueError("Error! Empty String")
            restart()
        else:
            timming(red + "\n >>>> [ You lied to me!!! I'm impressed!!! ]")
            os.system("clear")
            restart()
        try:
            in_2 = input(" >>>> ")
            if in_2 == 'y':
                print()
                timming(green + " Waiting=====                 ||||")
                timeout(1)
                timming(" Waiting=========             ||||")
                timeout(1)
                timming(" Waiting============          ||||")
                timeout(1)
                timming(" Waiting=================     ||||")
                timeout(1)
                timming(" Waiting======================||||")
                timeout(3)
                timming(red + "  ----------------------------")
                timming(" | Permission Granted!!!      |")
                timming("  ----------------------------")
                timeout(4)
                os.system('clear')
            elif in_2 == 'n':
                print()
                timming(red + "\n >>>> [ You lied to me!!! I'm impressed!!! ]")
                out()
                if not in_2:
                    raise ValueError("Error! Empty String")
                os.system("clear")
                restart()
            else:
                timming(red + "\n >>>> [ You lied to me!!! I'm impressed!!! ]")
                os.system("clear")
                restart()


            def lsb():
                area = (width, height)
                im1 = cv2.resize(image1, area)
                im2 = cv2.resize(image2, area)
                for valu in range(height):
                    for valu1 in range(width):
                        for valu2 in range(3):
                            pixel1 = format(im1[valu][valu1][valu2], '08b')
                            pixel2 = format(im2[valu][valu1][valu2], '08b')
                            pix1 = pixel1[:4] + pixel2[:4]
                            im1[valu][valu1][valu2] = int(pix1, 2)
                cv2.imwrite('kneel.png', im1)


            def lsb1():
                area = (width, height)
                im2 = cv2.resize(image2, area)
                im3 = cv2.resize(image3, area)
                for value in range(height):
                    for value1 in range(width):
                        for value2 in range(3):
                            pixel2 = format(im2[value][value1][value2], '08b')
                            pixel3 = format(im3[value][value1][value2], '08b')
                            pix2 = pixel2[:4] + pixel3[:4]
                            im2[value][value1][value2] = int(pix2, 2)
                cv2.imwrite('loki.png', im2)


            print(red + figlet_format('WELCOME TO ASGARD', font='bubble'))
            timming(
                green + " Here,My thoughts entirely depends on the rest of the\n information you're about to give me!!! ")
            print()
            timeout(1)
            timming(" [1] Encode \n [2] Decode \n")
            while True:
                try:
                    Choice = input(" Enter your choice here : ")
                    if Choice == '1':
                        os.system('clear')
                        print(red + figlet_format('MISCHIEF ENCRYPTION', font='bubble'))
                        timming(green +
                                " Everything's a choice!!! Nobody's born good!!!\n Nobody's born evil!!! It's always a choice!!! ")
                        print()
                        timeout(1)
                        timming(" [1] Hide single image\n [2] Hide double image\n [3] Hide camera image\n")
                        try:
                            Type = int(input(" Enter your choice here : "))
                            if Type == 1:
                                os.system('clear')
                                print(red + figlet_format('MISCHIEF ENCRYPTION', font='bubble'))
                                timeout(1)
                                timming(
                                    green + " It's not how well you play the game,it's deciding what\n game you want to play!!! ")
                                print()
                                timming(green + " [ Please select the cover image from the directory!!! ]")
                                timeout(2)

                                filename = tkinter.filedialog.askopenfilename(
                                    initialdir='/root', title='ENCRYPTION',
                                    filetypes=[("Jpeg", "*.jpeg"), ('Png Images', '*.png'), ("jpg", "*.jpg")])
                                image1 = cv2.imread(filename, 1)

                                timming(green + " [ Please select the secret image from the directory!!! ]")
                                timeout(2)
                                filename1 = tkinter.filedialog.askopenfilename(
                                    initialdir='/root', title='ENCRYPTION',
                                    filetypes=[("Jpeg", "*.jpeg"), ('Png Images', '*.png'), ("jpg", "*.jpg")])
                                image2 = cv2.imread(filename1, 1)
                                width = image1.shape[1]
                                height = image2.shape[0]
                                lsb()
                                print("")
                                timming(" Encoding=====            ||||")
                                timeout(1)
                                timming(" Encoding===========      ||||")
                                timeout(1)
                                timming(" Encoding=================||||")
                                timeout(2)
                                timming("  -----------------------------------------")
                                timming(" | In the end!!! You always kneel.png!!!   |")
                                timming("  -----------------------------------------")
                                out()
                                break

                            elif Type == 2:
                                os.system('clear')
                                print(red + figlet_format('MISCHIEF ENCRYPTION', font='bubble'))
                                timming(
                                    green + " It's not how well you play the game,it's deciding what\n game you want to play!!! ")
                                print()
                                timming(green + " [ Please select the cover image from the directory!!! ]")
                                timeout(2)
                                filename = tkinter.filedialog.askopenfilename(
                                    initialdir='/root', title='ENCRYPTION',
                                    filetypes=[("Jpeg", "*.jpeg"), ('Png Images', '*.png'), ("jpg", "*.jpg")])
                                image1 = cv2.imread(filename, 1)
                                timming(green + " [ Please select the cover/secret image from the directory!!! ]")
                                timeout(2)
                                filename1 = tkinter.filedialog.askopenfilename(
                                    initialdir='/root', title='ENCRYPTION',
                                    filetypes=[("Jpeg", "*.jpeg"), ('Png Images', '*.png'), ("jpg", "*.jpg")])
                                image2 = cv2.imread(filename1, 1)
                                timming(green + " [ Please select the secret image from the directory!!! ]")
                                timeout(2)
                                filename2 = tkinter.filedialog.askopenfilename(
                                    initialdir='/root', title='ENCRYPTION',
                                    filetypes=[("Jpeg", "*.jpeg"), ('Png Images', '*.png'), ("jpg", "*.jpg")])
                                image3 = cv2.imread(filename2, 1)
                                width = image1.shape[1]
                                height = image2.shape[0]
                                lsb()
                                lsb1()
                                print()
                                timming(" Encoding=====            ||||")
                                timeout(1)
                                timming(" Encoding===========      ||||")
                                timeout(1)
                                timming(" Encoding=================||||")
                                timeout(2)
                                timming("  ------------------------------------------------------")
                                timming(" | In the end!!! You always kneel.png and loki.png!!!   |")
                                timming("  ------------------------------------------------------")
                                out()
                                break
                            elif Type == 3:
                                os.system('clear')
                                print(red + figlet_format('MISCHIEF ENCRYPTION', font='bubble'))
                                timming(
                                    green + " It's not how well you play the game,it's deciding what\n game you want to play!!! ")
                                print()
                                timming(green + " [ Please select the cover image from the directory!!! ]")
                                timeout(2)
                                filename = tkinter.filedialog.askopenfilename(
                                    initialdir='/root', title='ENCRYPTION',
                                    filetypes=[("Jpeg", "*.jpeg"), ('Png Images', '*.png'), ("jpg", "*.jpg")])
                                image1 = cv2.imread(filename, 1)
                                camera = cv2.VideoCapture(0)
                                ret, frame = camera.read()
                                cv2.imwrite("evil.png", frame)
                                cv2.destroyAllWindows()
                                timming(" [ The secret image [camera image] : You always evil.png!!! ]")
                                image2 = cv2.imread('evil.png', 1)
                                width = 750
                                height = 750
                                lsb()
                                print()
                                timming(" Encoding=====            ||||")
                                timeout(1)
                                timming(" Encoding===========      ||||")
                                timeout(1)
                                timming(" Encoding=================||||")
                                timeout(2)
                                timming("  -----------------------------------------")
                                timming(" | In the end!!! You always kneel.png!!!   |")
                                timming("  -----------------------------------------")
                                out()
                                break
                            elif Type >= 4:
                                print()
                                timming(red + " >>>> [ You lied to me!!! I'm impressed!!! ]")
                                timeout(2)
                                os.system("clear")
                                restart()
                            elif Type == 0:
                                timming(red + " >>>> [ You lied to me!!! I'm impressed!!! ]")
                                timeout(2)
                                os.system("clear")
                                restart()

                            else:
                                timming(red + "\n >>>> [ You lied to me!!! I'm impressed!!! ]")
                                timeout(2)
                                os.system("clear")
                                restart()
                                if not Choice:
                                    raise ValueError("Error! Empty String")
                                os.system("clear")
                                restart()
                        except ValueError:
                            timming(red + "\n >>>> [ You lied to me!!! I'm impressed!!! ]")
                            os.system("clear")
                            restart()
                    elif Choice == '2':
                        os.system('clear')
                        print(red + figlet_format('MISCHIEF DECRYPTION', font='bubble'))
                        timming(green + " Hitting does not solve everything!!!")
                        print()
                        timming(green + " [ Please select the cover image from the directory!!! ]")
                        timeout(2)
                        filename = tkinter.filedialog.askopenfilename(
                            initialdir='/root', title='DECRYPTION',
                            filetypes=[('Png Images', '*.png'), ("Jpeg", "*.jpeg"), ("jpg", "*.jpg")])
                        img = cv2.imread(filename, 1)
                        width, height = img.shape[0], img.shape[1]

                        saved2img = num.zeros((width, height, 3), num.uint8)
                        for value in range(width):
                            for value1 in range(height):
                                for value2 in range(3):
                                    bin_data = format(img[value][value1][value2], '08b')
                                    converted_bin = bin_data[4:] + chr(random.randint(0, 1) + 48) * 4
                                    saved2img[value][value1][value2] = int(converted_bin, 2)
                        cv2.imwrite('king.png', saved2img)
                        print()

                        timming(" Decoding=====            ||||")
                        timeout(1)
                        timming(" Decoding===========      ||||")
                        timeout(1)
                        timming(" Decoding=================||||")
                        timeout(2)
                        timming("  -----------------------------------------")
                        timming(" | In the end!!! You always king.png!!!    |")
                        timming("  -----------------------------------------")
                        out()
                        break
                    elif Choice >= '3':
                        print()
                        timming(red + " >>>> [ You lied to me!!! I'm impressed!!! ]")
                        out()
                        os.system("clear")
                        restart()
                        break

                    elif Choice == '0':
                        print()
                        timming(red + " >>>> [ You lied to me!!! I'm impressed!!! ]")
                        out()
                        os.system("clear")
                        restart()

                        if not Choice:
                            raise ValueError("Error! Empty String")
                        restart()
                    else:
                        timming(red + "\n >>>> [ You lied to me!!! I'm impressed!!! ]")
                        os.system("clear")
                        restart()

                except ValueError:
                    restart()
        except ValueError:
            restart()
    except ValueError:
        restart()
except ValueError:
    restart()
