import cv2
import numpy as num
import random


def encode(first_image, second_image, third_image):
    image1 = cv2.imread(first_image, 1)
    image2 = cv2.imread(second_image, 1)
    image3 = cv2.imread(third_image, 1)
    width = 250
    height = 250
    area = (width, height)
    im1 = cv2.resize(image1, area)
    im2 = cv2.resize(image2, area)
    im3 = cv2.resize(image3, area)
    for val in range(height):
        for val_1 in range(width):
            for val_2 in range(3):
                pixel1 = format(im1[val][val_1][val_2], '08b')
                pixel2 = format(im2[val][val_1][val_2], '08b')
                pixel3 = format(im3[val][val_1][val_2], '08b')
                pix1 = pixel1[0:4] + pixel2[0:4]
                pix2 = pixel2[0:4] + pixel3[0:4]
                im1[val][val_1][val_2] = int(pix1, 2)
                im2[val][val_1][val_2] = int(pix2, 2)
    cv2.imwrite('hidden.png', im1)
    cv2.imwrite('secret.png', im2)
    return 1


def decode():
    img = cv2.imread("hidden.png", 1)
    img1 = cv2.imread("secret.png", 1)
    width, height = img.shape[0], img.shape[1]
    width_1, height_1 = img1.shape[0], img1.shape[1]
    saved2img = num.zeros((width, height, 3), num.uint8)
    saved2img_1 = num.zeros((width_1, height_1, 3), num.uint8)
    for val in range(width):
        for val_1 in range(height):
            for val_2 in range(3):
                bin_data = format(img[val][val_1][val_2], '08b')
                converted_bin = bin_data[-4:] + chr(random.randint(0, 1) + 48) * 4
                saved2img[val][val_1][val_2] = int(converted_bin, 2)
    cv2.imwrite('stego.png', saved2img)

    for val in range(width_1):
        for val_1 in range(height_1):
            for val_2 in range(3):
                bin_data_1 = format(img1[val][val_1][val_2], '08b')
                converted_bin_1 = bin_data_1[-4:] + chr(random.randint(0, 1) + 48) * 4
                saved2img_1[val][val_1][val_2] = int(converted_bin_1, 2)
    cv2.imwrite('stego1.png', saved2img_1)


def stegano():
    Choice = int(input("Please choose your option!!! \n 1. Encode \n 2. Decode \n Enter your choice here : "))
    if Choice == 1:
        first = input("Enter your first image : ")
        second = input("Enter your second image : ")
        third = input("Enter your third image : ")
        encode(first, second, third)
        print("Given image encrypted successfully!!!")
        print("Image saved as hidden.png and secret.png!!!")

    elif Choice == 2:

        dec = input("Enter your image for decode : ")
        dec_1 = input("Enter your image for decode : ")
        decode()
        print("Your image decrypted successfully!!!")
        print("Image decrypted from ", dec, "and", dec_1, "!!!")
        print("Both image saved as stego.png and stego1.png!!!")
    else:
        raise Exception("Choose the correct option!!!")


stegano()

