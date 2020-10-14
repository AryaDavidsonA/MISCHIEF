import cv2
import numpy as num
import random


def encode(first_image, second_image):
    image1 = cv2.imread(first_image, 1)
    image2 = cv2.imread(second_image, 1)
    width = 250
    height = 250
    area = (width, height)
    im1 = cv2.resize(image1, area)
    im2 = cv2.resize(image2, area)
    for val in range(width):
        for val_1 in range(height):
            for val_2 in range(3):
                pixel1 = format(im1[val][val_1][val_2], '08b')
                pixel2 = format(im2[val][val_1][val_2], '08b')
                pixel = pixel1[0:4] + pixel2[0:4]
                im1[val][val_1][val_2] = int(pixel, 2)
    cv2.imwrite('hidden.png', im1)
    return 1


def decode():
    img = cv2.imread("hidden.png", 1)
    width = img.shape[0]
    height = img.shape[1]
    saved2img = num.zeros((width, height, 3), num.uint8)
    for val in range(width):
        for val_1 in range(height):
            for val_2 in range(3):
                bin_data = format(img[val][val_1][val_2], '08b')
                converted_bin = bin_data[-4:] + chr(random.randint(0, 1) + 48) * 4
                saved2img[val][val_1][val_2] = int(converted_bin, 2)
    cv2.imwrite('saved.png', saved2img)

def stego():
    print("Hey,It's me parrot!!!")
    Choice = int(input("Please choose your option!!! \n 1. Encode \n 2. Decode \n Enter your choice here : "))
    if Choice == 1:
        first = input("Enter the first image : ")
        second = input("Enter the hidden image : ")
        encode(first, second)
        print("Given image encrypted successfully and the image saved as hidden.png!!!")

    elif Choice == 2:
        dec = input("Enter the image for decode : ")
        decode()
        print("Your image decrypted successfully, the image encrypted from ", dec, " and saved as saved.png!!!")
    else:
        raise ValueError("Input valid data")


stego()

