import cv2
import numpy as num
import random


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
    return 1

